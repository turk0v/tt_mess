from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import time

pass_to_chromedriver = "/Users/matveyturkov/Downloads/chromedriver"
url = "http://localhost:3000/chats"

class SeleniumTests(unittest.TestCase):
	def test_find_and_click(self):
		driver = webdriver.Chrome(pass_to_chromedriver)
		driver.get(url)
		driver.find_element_by_xpath("//*[@id='root']/a[1]").click()
		element = WebDriverWait(driver, 10).until(
		    lambda x: x.find_element_by_xpath("//*[@id='root']/div[3]/div[3]"))


if __name__ == '__main__':
	unittest.main()
