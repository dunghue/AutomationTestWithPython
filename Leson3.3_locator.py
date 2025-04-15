#Example 1: Find element by link text
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sbasu.pythonanywhere.com/tastyFoodApp/")
element = driver.find_element(By.LINK_TEXT, "Create New Profile")
element.click()

#Example 2: Find element by id and use send keys method
import time
time.sleep(3)
firstName = driver.find_element(By.ID, "id_firstName")
firstName.send_keys("Kia")

lastName = driver.find_element(By.ID, "id_lastName")
lastName.send_keys("Sabrina")

driver.find_element(By.ID, "id_gender_1").click()

#Example 3: Select a value from dropdown list
from selenium.webdriver.support.ui import Select

time.sleep(3)
state = Select(driver.find_element(By.ID, "id_state"))
state.select_by_visible_text("Texas")

fee = Select(driver.find_element(By.ID, "id_fee"))
fee.select_by_visible_text("$150 : Gold")
time.sleep(3)
