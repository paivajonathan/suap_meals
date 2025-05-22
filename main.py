from os import getenv

from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(
    options=options, service=ChromeService(ChromeDriverManager().install())
)
driver.get("https://suap.ifpi.edu.br/accounts/login/?next=/")


def wait_for_element(driver, by, value, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
            expected_conditions.presence_of_element_located((by, value))
        )
        return element
    except Exception as e:
        print(f"Error waiting for element: {e}")
        return None


def login(username, password):
    username_field = wait_for_element(driver, By.NAME, "username")
    password_field = wait_for_element(driver, By.NAME, "password")
    submit_button = wait_for_element(
        driver, By.XPATH, "//input[@type='submit' and @value='Acessar']"
    )

    username_field.send_keys(username)
    password_field.send_keys(password)
    submit_button.click()


def book_meal():
    driver.get("https://suap.ifpi.edu.br/ae/refeicoes-do-dia/")
    book_meal_button = wait_for_element(
        driver, By.XPATH, "//a[contains(@href, '/ae/reservar-refeicao/')]"
    )
    print("Testando")
    print("Conteudo do USERNAME:", getenv("SUAP_USERNAME"))
    print("Conteudo do PASSWORD:", getenv("SUAP_PASSWORD"))
    book_meal_button.click()

username = getenv("SUAP_USERNAME")
password = getenv("SUAP_PASSWORD")

login(username, password)
book_meal()
driver.quit()