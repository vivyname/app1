from base.base import BasePage

from selenium.webdriver.common.by import By

class BaiduPage(BasePage):
	search_input = (By.ID, "chat-textarea")
	search_button = (By.ID, "chat-submit-button")

	def search(self, keyword):
		self.driver.get("https://www.baidu.com")
		self.send_keys(self.search_input, keyword)
		self.click(self.search_button)
	test_loc=(By.CLASS_NAME,'title-content-title')


	def click_title(self):
		self.driver.get("https://www.baidu.com")
		locs= self.find_elements(self.test_loc)
		locs[0].click()
    

