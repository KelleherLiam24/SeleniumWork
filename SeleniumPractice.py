from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com/")

print(driver.title) #Prints out title of webpage



search = driver.find_element_by_name("q")
search.clear()
search.send_keys("test")
search.send_keys(Keys.RETURN)

link = driver.find_element_by_link_text("Settings")
link.click()

link = driver.find_element_by_link_text("Search settings")
link.click()

link = driver.find_element_by_link_text("Languages")
link.click()

link = driver.find_element_by_xpath('//*[@id="langtes"]/div/span[1]')
link.click()

link = driver.find_element_by_xpath('//*[@id="form-buttons"]/div[1]')
link.click()



#try:
    #main = WebDriverWait(driver, 10).until(
     #   EC.presence_of_element_located((By.ID, "rso"))
    #)
    #articles = main.find_elements_by_class_name("g")
    #for article in articles:
     #   header = article.find_element_by_tag_name("h3")
      #  print(header.text)
#finally:
  #  driver.quit()

