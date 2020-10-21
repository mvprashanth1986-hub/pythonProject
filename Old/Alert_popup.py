from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
#options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.set_window_position(110, 220)
driver.set_window_size(1080,800)
driver.get("http://www.gmail.com")

driver

