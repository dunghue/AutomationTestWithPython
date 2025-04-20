import unittest
from selenium import webdriver
import createNewProfile

class Testing(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://sbasu.pythonanywhere.com/tastyFoodApp/create")
    
    def test_CreatePage(self):
        driver = self.driver
        home = createNewProfile.CreateNewProfile(driver)
        title = home.get_title()
        self.assertEqual(title, "Create New Profile - Tasty Home Food Delivery Service", "Title does not match")
        intro = home.get_intro_text()
        self.assertEqual(intro, "Greetings, Please fill the form below to get enrolled into the World's Best Home Food Delivery Service", "Intro text does not match")
        home.firstName("KiaToca")
        
    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()