from os import getenv
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class SuapDriver:
    def __init__(self):
        self.__driver = None

        options = ChromeOptions()
    
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        self.__driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
            
    def quit(self):
        self.__driver.quit()
                
    def login(self):
        print("Realizando login...")
        
        username = getenv("SUAP_USERNAME")
        password = getenv("SUAP_PASSWORD")
        
        self.__driver.get("https://suap.ifpi.edu.br/accounts/login/?next=/")
        
        username_field = self.__wait_for_element(By.NAME, "username")
        password_field = self.__wait_for_element(By.NAME, "password")
        
        submit_button = self.__wait_for_element(
            By.XPATH, "//input[@type='submit' and @value='Acessar']"
        )

        username_field.send_keys(username)
        password_field.send_keys(password)
        
        submit_button.click()

        sleep(3)
        
    def book_meal(self):
        print("Reservando refeição...")
        
        self.__driver.get("https://suap.ifpi.edu.br/ae/refeicoes-do-dia/")
        
        # Use a more specific XPath if possible, but the original is fine
        book_meal_button_locator = (By.XPATH, "//a[contains(@href, '/ae/reservar-refeicao/')]")

        # Wait for the button to be clickable, not just present
        book_meal_button = self.__wait_for_element_to_be_clickable(book_meal_button_locator)
        
        if book_meal_button:
            # Use JavaScript to click the button, which is more robust
            self.__driver.execute_script("arguments[0].click();", book_meal_button)
        
        elements = self.__driver.find_elements(By.ID, "feedback_message")
        
        if elements:
            message_text = elements[0].text.strip()
            print(message_text)
        
        sleep(3)

    def __wait_for_element(self, by, value, timeout=10):
        try:
            element = WebDriverWait(self.__driver, timeout).until(
                expected_conditions.presence_of_element_located((by, value))
            )
            return element
        except Exception as e:
            print(f"Error waiting for element: {e}")
            return None

    def __wait_for_element_to_be_clickable(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.__driver, timeout).until(
                expected_conditions.element_to_be_clickable(locator)
            )
            return element
        except Exception as e:
            print(f"Error waiting for element to be clickable: {e}")
            return None


def main():
    suap_driver = SuapDriver()
    
    suap_driver.login()
    suap_driver.book_meal()
    suap_driver.quit()


if __name__ == "__main__":
    main()
