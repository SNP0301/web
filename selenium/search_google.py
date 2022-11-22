from selenium import webdriver
import time
driver = webdriver.Chrome('/opt/homebrew/bin/chromedriver')
driver.get("https://google.com")

elem = driver.find_element_by_name('q')

elem.clear()
elem.send_keys('hi')
elem.submit()

time.sleep(100000)
