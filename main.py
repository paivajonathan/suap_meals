from os import getenv
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class SuapDriver:
    def __init__(self, browser):
        self.__driver = None

        match browser.lower():
            case "chrome":
                options = ChromeOptions()
            
                options.add_argument("--headless")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")

                self.__driver = webdriver.Chrome(
                    service=ChromeService(ChromeDriverManager().install()),
                    options=options
                )
            case "edge":
                options = EdgeOptions()
                
                options.add_argument("--headless")
                
                self.__driver = webdriver.Edge(
                    options=options, service=EdgeService(EdgeChromiumDriverManager().install())
                )
            case _:
                raise Exception("Navegador desconhecido!")
            
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
        
    def book_meal(self):
        print("Reservando refeição...")
        
        self.__driver.get("https://suap.ifpi.edu.br/ae/refeicoes-do-dia/")
        
        book_meal_button = self.__wait_for_element(
            By.XPATH, "//a[contains(@href, '/ae/reservar-refeicao/')]"
        )
        
        book_meal_button.click()
        
        elements = self.__driver.find_elements(By.ID, "feedback_message")
        
        if elements:
            message_text = elements[0].text.strip()
            print(message_text)

    def __wait_for_element(self, by, value, timeout=10):
        try:
            element = WebDriverWait(self.__driver, timeout).until(
                expected_conditions.presence_of_element_located((by, value))
            )
            return element
        except Exception as e:
            print(f"Error waiting for element: {e}")
            return None


def main():
    suap_driver = SuapDriver("chrome")
    
    suap_driver.login()
    sleep(3)
    
    suap_driver.book_meal()
    sleep(3)
    
    suap_driver.quit()
    sleep(3)


if __name__ == "__main__":
    main()
