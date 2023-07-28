from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
import Pass    #a dictionary used for storing credentials
from selenium.webdriver.common.by import By





opt=input('enter a for away or l for local: ')
if opt=='a':
   
    driver = webdriver.Chrome()# Open URL
    driver.get("https://away.ethiotelecom.et")
    #user=os.environ.get("away_account") if I have admin rights
    #user_pass=os.environ.get("away_account_pass")   if I have admin rights
    user=Pass.credentials.get("away_account")
    user_pass = Pass.credentials.get("away_account_pass")
    time.sleep(5)
    driver.find_element(By.ID,'username').send_keys(user)
    driver.find_element(By.ID,'credential').send_keys(user_pass)
    time.sleep(3)
    driver.find_element(By.ID,'login_button').click()
    
    # Store the ID of the original window
    original_window = driver.current_window_handle


    # Check we don't have other windows open already
    assert len(driver.window_handles) == 1

    # Click the link which opens in a new window
    
    time.sleep(5)
    # Wait for the new window or tab
    wait = WebDriverWait(driver, 10)
    wait.until(EC.number_of_windows_to_be(2))
    time.sleep(10)

    # Loop through until we find a new window handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    # Wait for the new tab to finish loading content
    #wait.until(EC.title_is("SeleniumHQ Browser Automation"))

    # Find an element by ID and interact with it
    #element = driver.find_element(By.ID,"details-button")
    #element.click()
    #time.sleep(3)
    #driver.find_element(By.ID,"proceed-link").click()
    time.sleep(10)
    driver.find_element(By.ID,"unamebean").send_keys(Pass.credentials.get("ERP_USER"))
    driver.find_element(By.ID,"pwdbean").send_keys(Pass.credentials.get("ERP_USER_PASS"))
    driver.find_element(By.ID,"SubmitButton").click()
    # Setup wait for later
    #wait = WebDriverWait(driver, 10)

   
    
else:
    driver = webdriver.Chrome()# Open URL
    driver.get("https://eterp.ethiotelecom.et")


    # Find an element by ID and interact with it
    #element = driver.find_element(By.ID,"details-button")
    #element.click()
    time.sleep(3)
    #driver.find_element(By.ID,"proceed-link").click()
    time.sleep(10)
    driver.find_element(By.ID,"unamebean").send_keys(Pass.credentials.get("ERP_USER"))
    driver.find_element(By.ID,"pwdbean").send_keys(Pass.credentials.get("ERP_USER_PASS"))
    driver.find_element(By.ID,"SubmitButton").click()
    # Setup wait for later
    
