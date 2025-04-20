from selenium import webdriver
from locator import CreatePageLocator
from element import BasePage
from selenium.webdriver.common.by import By

class CreateNewProfile(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver
        
        
    def get_title(self):
        title = self.driver.title
        return title
    
    def get_intro_text(self):
        intro_text = self.driver.find_element(By.CLASS_NAME, CreatePageLocator.into_para_class_name).text
        return intro_text
    
    def firstName(self, val):
        e = BasePage(self.driver)
        e.set_element(CreatePageLocator.id_firstName, val)
        


