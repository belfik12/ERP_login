from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
import Pass    #a dictionary used for storing credentials
from selenium.webdriver.common.by import By


def away(driver):                        
   
   driver.get("https://away.ethiotelecom.et")               #opens the specified URL
   
   user=Pass.credentials.get("away_account")                #user=os.environ.get("away_account") is better if you have admin previlage on your windows machine
   user_pass = Pass.credentials.get("away_account_pass")    #user_pass=os.environ.get("away_account_pass")
   
   time.sleep(5)
   
   driver.find_element(By.ID,'username').send_keys(user)
   driver.find_element(By.ID,'credential').send_keys(user_pass)
   driver.find_element(By.ID,'login_button').click()
   
   original_window = driver.current_window_handle            # Store the ID of the original window
   
   time.sleep(5)
  
   assert len(driver.window_handles) == 1                    # Check we don't have other windows open already
   wait = WebDriverWait(driver, 10)
   #This try except block is used if the element is not located after specified time limit
   #from experience refreshing the page solves the problem
   try:
    
    wait.until(EC.presence_of_element_located((By.XPATH,'''//*[@id="navbar-view-section"]/div/div/div[2]/div[2]/div[5]/button[1]''')))
   except:
    driver.refresh()
    wait.until(EC.presence_of_element_located((By.XPATH,'''//*[@id="navbar-view-section"]/div/div/div[2]/div[2]/div[5]/button[1]''')))
    
   #this clicks a link that will open a new window 
   driver.find_element(By.XPATH,'''//*[@id="navbar-view-section"]/div/div/div[2]/div[2]/div[5]/button[1]''').click()
   
   # Loop through until we find a new window handle
   for window_handle in driver.window_handles:
     if window_handle != original_window:
         driver.switch_to.window(window_handle)
         break
   
   ERP_LOGIN_PAGE(driver)

def local_network(driver):
   
   driver.get("https://eterp.ethiotelecom.et")

   #uncomment the bellow two lines if there is a security check
   
   #driver.find_element(By.ID,"details-button").click()
   #driver.find_element(By.ID,"proceed-link").click()
   
   time.sleep(5)
   ERP_LOGIN_PAGE(driver)


def ERP_LOGIN_PAGE(driver):
   
   wait = WebDriverWait(driver, 10)
   #This try except block is used if the element is not located after specified time limit
   #from experience refreshing the page solves the problem
   try:
      wait.until(EC.presence_of_element_located((By.ID,"unamebean")))
   except:                                                  
      driver.refresh()
      wait.until(EC.presence_of_element_located((By.ID,"unamebean")))
   driver.find_element(By.ID,"unamebean").send_keys(Pass.credentials.get("ERP_USER"))
   driver.find_element(By.ID,"pwdbean").send_keys(Pass.credentials.get("ERP_USER_PASS"))
   driver.find_element(By.ID,"SubmitButton").click()

   
def main():
    
    opt=input('enter a for away or l for local: ')
    driver=driver=webdriver.Chrome()
    if opt=="a":
        away(driver)
    else:
        local_network(driver)
    
    time.sleep(15)
   

if __name__ == "__main__":
  main()
       
   
    
    
