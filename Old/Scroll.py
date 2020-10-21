from selenium import webdriver
from Old import logging_test

driver = webdriver.Chrome()
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
#driver.execute_script("window.scrollBy(0,5000)","")
#ele = driver.find_element_by_xpath("//td[contains(text(),'India')]")
#driver.execute_script("arguments[0].scrollIntoView();",ele)
#driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
#driver.save_screenshot("C:\pythonutils\photo.jpg")
#driver.get_screenshot_as_file("C:\pythonutils\photo1.jpg")

logging_test.debug("debug")
logging_test.info("info")
logging_test.warning("warning")
logging_test.error("error")
logging_test.critical("critical")


