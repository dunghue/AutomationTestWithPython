import unittest
from selenium import webdriver
import homePage

class Testing_HomePage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://sbasu.pythonanywhere.com/tastyFoodApp/")
    
    def test_HomePage(self):
        driver = self.driver
        home = homePage.HomePage(driver)
        title = home.test_title()
        self.assertEqual(title, "Tasty Home Food Delivery Service", "Title does not match")
        heading = home.test_heading()
        self.assertEqual(heading, "Tasty Home Food Delivery Service", "Heading does not match")
        link_1 = home.test_link()
        self.assertTrue(link_1.is_enabled(), "Link is not enabled")
        link_1.click()
        
    def tearDown(self):
        self.driver.quit()
        
        
if __name__ == "__main__":
    unittest.main()

        

        