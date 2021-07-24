from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

PATH = "C:\Program Files (x86)\chromedriver.exe"
option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(PATH,options=option)

driver.get("https://www.google.com/")

search = driver.find_element_by_name("q")
search.clear()
search.send_keys("english to " + sys.argv[1])
search.send_keys(Keys.RETURN)

con = driver.find_element_by_id("tw-source-text-ta")
con.clear()
sentence = " ".join(sys.argv[2:])
con.send_keys(sentence)


time.sleep(1)
con_final = driver.find_element_by_id("tw-target-text")
print(sentence + " in " + sys.argv[1] + " is " + con_final.text)

driver.quit()