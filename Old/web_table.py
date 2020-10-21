from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://testautomationpractice.blogspot.com/")
time.sleep(10)

rows = driver.find_elements(By.XPATH,"//*[@id='HTML1']/div[1]/table/tbody/tr")
cols = driver.find_elements(By.XPATH,"//*[@id='HTML1']/div[1]/table/tbody/tr[1]/th")

rs = len(rows)
cs = len(cols)

for r in range(2, rs+1):
    for c in range(1, cs+1):
        ele = driver.find_elements(By.XPATH, "/HTML1/div[1]/table/tbody/tr["+str(r)+"]/th["+str(c)+"]")
        print(ele.text)


