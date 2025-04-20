from selenium import webdriver
from locator import HomePageLocators

class HomePage:
    def __init__(self,driver):
        self.driver = driver
        
    def test_title(self):
        get_title = self.driver.title
        return get_title
    
    def test_heading(self):
        get_heading = self.driver.find_element_by_xpath(HomePageLocators.heading_xpath)
        return get_heading.text
    
    def test_link(self):
        get_link = self.driver.find_element_by_link_text(HomePageLocators.link_text_1)
        return get_link.text