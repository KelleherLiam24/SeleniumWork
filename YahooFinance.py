from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://finance.yahoo.com/")

search = driver.find_element_by_id("yfin-usr-qry")
search.clear()
search.send_keys(sys.argv[1])
search.send_keys(Keys.RETURN)


signIn = driver.find_element_by_link_text("Sign in")
signIn.click()

signIn = driver.find_element_by_id("tpa-google-button")
signIn.click()

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "identifierId"))
        )
    main.send_keys(sys.argv[2])
    main.send_keys(Keys.RETURN)
except:
    driver.quit()