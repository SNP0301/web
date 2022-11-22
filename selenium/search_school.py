from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('detach',True)

driver = webdriver.Chrome('/opt/homebrew/bin/chromedriver',options=options)
driver.get("https://schoolzone.emac.kr/gis/gis.do/")

elem = driver.find_element(By.ID,'searchText')
elem.send_keys('hi' + Keys.ENTER)