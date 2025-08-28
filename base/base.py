from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )
    

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    def is_displayed(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except:
            return False

    def wait_for_visible(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def find_elements(self, locator):
        '''
        获取多个元素，适用于 className 等重复控件
        locator: 元组，如 (By.CLASS_NAME, "your_class_name")
        '''
        return WebDriverWait(self.driver, self.timeout).until(
            lambda driver: driver.find_elements(*locator)
        )
