from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.implicitly_wait(3)
action = ActionChains(driver)
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")

ele = driver.find_element_by_xpath("//p/child::span[contains(text(),'right click me')]")
time.sleep(4)
action.context_click(ele)
#driver.find_element_by_xpath("//ul[@class='context-menu-list context-menu-root']/li[2]").click()




