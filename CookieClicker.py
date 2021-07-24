from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
actions = ActionChains(driver)
actions.double_click(cookie)
upgrades_count = 1
while True:
    try:
         test = driver.find_element_by_id("productPrice" + str(upgrades_count))
         upgrades_count += 1
    except:
         break 

while True:
    items = [driver.find_element_by_id("productPrice" + str(i)) for i in range((upgrades_count-1),-1,-1)]
    actions.perform()
    str_count = ""
    countlist = cookie_count.text.split(" ")[0].replace(',',' ').split(" ")
    for n in countlist:
        str_count = str_count + n
    count = int(str_count)
    for item in items:
        if item.text == '':
            continue
        numlist = item.text.replace(',',' ').split(" ")
        if len(numlist) == 1:
            str_value = item.text.split(" ")[0]
        else:
            str_value = ""
            for num in numlist:
                str_value = str_value + num  
        value = int(str_value)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()



