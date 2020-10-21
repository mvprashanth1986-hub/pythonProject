from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
action = ActionChains(driver)

driver.maximize_window()
driver.implicitly_wait(10)

# driver.get("http://testautomationpractice.blogspot.com/")
# driver.execute_script("window.scrollBy(0,600)","")
# ele = driver.find_element_by_xpath(("//span[@class='ui-slider-handle ui-corner-all ui-state-default' and @style='left: 0%;']"))
# action.click_and_hold(ele).move_by_offset(40,0).release().perform()

