from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_experimental_option('detach',True)

driver = webdriver.Chrome('/opt/homebrew/bin/chromedriver',options=options)
driver.get("https://www.google.com/")

