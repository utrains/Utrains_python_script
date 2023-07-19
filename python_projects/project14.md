## You work as DevOps Engineer for a company. Your team have built and deployed an application in pre-production. Before pushing the app in production you need to make some tests on it. 
## The testing process was manual, and your task is to build a Python script that automates web testing using the Selenium WebDriver. The script will be able to log in as a user to the application through the login form and navigate the menu to make sure each page is accessible.

### The script below is made based on the geolocation app project of Utrains' Class

```python
# Prerequisite: install selenium module

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

#open Google Chrome browser  
driver=webdriver.Chrome()

print(f"The test case started")
#maximize the window size
driver.maximize_window()

#delete the cookies  
driver.delete_all_cookies()

#navigate to the URL  
driver.get("http://45.33.11.12:8082/showMyLoginPage")

# get the browser's title
title1= driver.title # title of the login page
print(f"Connecting to {title1} page of Geolocation app")

# identify the username box and enter the value  
elem1 = driver.find_element(by=By.NAME, value="username")
elem1.send_keys("root@utrains.test")

# identify the password box and enter the value  
elem2 = driver.find_element(by=By.NAME, value="password")
elem2.send_keys("root_pass")

# Click on the Log in button
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
submit_button.click()
title2= driver.title # title of the home page

if title1 == title2:
    print("Wrong credentials")
    driver.quit()
    exit()
else:
    print("Connected to website")

time.sleep(5)

# navigate to About us page
elem3= driver.find_element(By.LINK_TEXT, "About")
elem3.click()
time.sleep(5)

# navigate to Departments' page
elem4= driver.find_element(By.LINK_TEXT, "Departments")
elem4.click()
time.sleep(5)

# navigate to Doctors' page
elem5= driver.find_element(By.LINK_TEXT, "Doctors")
elem5.click()
time.sleep(5)

# navigate to Blog page
elem6= driver.find_element(By.LINK_TEXT, "Blog")
elem6.click()
time.sleep(5)

# navigate to Contact page
elem7= driver.find_element(By.LINK_TEXT, "Contact")
elem7.click()
time.sleep(5)

# close the driver
driver.quit()
print("Login to Geolocation app has been successfully completed")
