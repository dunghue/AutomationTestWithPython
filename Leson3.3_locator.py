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

usernameInputField = driver.find_element(By.ID, "id_username")
usernameInputField.send_keys("DunHue")

passwordInputfield = driver.find_element(By.ID, "id_password")
passwordInputfield.send_keys("12345")

dateInputField = driver.find_element(By.ID, "id_date")
dateInputField.send_keys("02/02/2000")


driver.find_element(By.ID, "id_gender_1").click()

#Example 3: Select a value from dropdown list
from selenium.webdriver.support.ui import Select

time.sleep(3)
state = Select(driver.find_element(By.ID, "id_state"))
state.select_by_visible_text("Texas")

fee = Select(driver.find_element(By.ID, "id_fee"))
fee.select_by_visible_text("$150 : Gold")
time.sleep(3)

#Example 4: Deal with any alert window (pop up)
button = driver.find_element(By.ID, "js_button")
print("Is Button enabled", button.is_enabled())
      #is_enabled(): method returns True if the button is enabled, otherwise False.
button.click()
time.sleep(2)

alert = driver.switch_to.alert #switch_to.alert: method is used to switch the control to alert window.
alert.accept() #accept(): method is used to accept the alert.(click OK button)
time.sleep(2)

#Example 5: check the paragraph text matches with the expected text
receivedText = driver.find_element(By.XPATH, "//p[contains(., 'Home Food Delivery Service')]").text
expectedText = "Greetings, Please fill the form below to get enrolled into the World's Best Home Food Delivery Service"
if receivedText == expectedText:
    print("Test Passed")
else:
    print("The text does not match")
    
#Example 6: GET the value from the First Name field 

valueOfFirstName = firstName.get_attribute("value")
print("The first name is:", valueOfFirstName)

#Example 7: Get URL and title of the page
print("The url is", driver.current_url)

expectedTitle = "Tasty Home Food Delivery Service"
actualTitle = driver.title
if(actualTitle == expectedTitle):
    print("The title is correct")
else:
    print("The title is incorrect")     
    
print("The actual title is", actualTitle)

#Example 9: Cick submit button
submitButton = driver.find_element(By.CLASS_NAME, "submitButton").click()
time.sleep(3)



