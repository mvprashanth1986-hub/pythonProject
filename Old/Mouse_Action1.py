from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()

driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
#driver.maximize_window()
#driver.implicitly_wait(10)

action = ActionChains(driver)

ele= driver.find_element_by_xpath("//span[contains(text(),'right click me')]")


action.context_click(ele)
