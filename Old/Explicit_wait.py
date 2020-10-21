from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import DesiredCapabilities,ActionChains
import time

driver = webdriver.Chrome()

driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")

driver.find_element(By.ID,"justAnInputBox").click()

multi = driver.find_elements(By.CSS_SELECTOR,"span.comboTreeItemTitle")

values = ['choice 1','choice 2','choice 2 1']


def mul_sel(m_sel, value, val=None):
    for ele in multi:
        print(ele.text)
        for k in range(len(values)):
            if ele.text == values[k]:
                ele.click()


mul_sel(multi,values)