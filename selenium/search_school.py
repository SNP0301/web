from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_experimental_option('detach',True)

driver = webdriver.Chrome('/opt/homebrew/bin/chromedriver',options=options)
driver.get("https://schoolzone.emac.kr/gis/gis.do")

school_name = driver.find_element(By.ID,'searchText')
school_name.send_keys('살레시오고등학교' + Keys.ENTER)
time.sleep(0.5)

driver.find_element(By.XPATH,'/html/body/div[1]/div[11]/div[1]/p/input').send_keys(Keys.ENTER)
driver.find_element(By.XPATH,'/html/body/div[1]/div[10]/div[1]/p/input').send_keys(Keys.ENTER)

time.sleep(3)
b = driver.find_elements(By.XPATH,'/html/body/div[4]/div[1]/ul[2]/li[2]/input')
driver.execute_script("parent.fn_getSchoolArea(126.892490626667,35.2166294135392,'middleSchoolArea','vworld');")
address = driver.find_element(By.CLASS_NAME,'address_list')

print(address.get_attribute('x'))
print(address.get_attribute('y'))