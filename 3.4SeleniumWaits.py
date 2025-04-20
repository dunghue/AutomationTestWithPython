from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximixe_windown()
driver.get("https://sbasu.pythonanywhere.com/tastyFoodApp/create")

#------Implicit Waits--------
driver.implicitly_wait(10)

#------Explicit Waits--------
wait = WebDriverWait(driver,10)
element = wait.until(EC.present_of_element_located(By.ID, "id_firstName")) #wait until the element is present in the DOM of a page.
element.send_keys("KiaToca")