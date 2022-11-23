from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=options)
driver.get("https://schoolzone.emac.kr/gis/gis.do")

school_name = driver.find_element(By.ID,'searchText')
school_name.send_keys('살레시오고등학교' + Keys.ENTER)
time.sleep(0.5)
driver.find_element(By.XPATH,'/html/body/div[1]/div[11]/div[1]/p/input').send_keys(Keys.ENTER)
driver.find_element(By.XPATH,'/html/body/div[1]/div[10]/div[1]/p/input').send_keys(Keys.ENTER)

time.sleep(1)

elem = driver.find_element(By.CSS_SELECTOR,'body > div:nth-child(4) > div:nth-child(3) > ul.address_list')
x_addr = elem.get_attribute('x')
y_addr = elem.get_attribute('y')
x = "126.892490626667"
y = "35.2166294135392"
cmd_dup = "parent.fn_getSchoolArea("
cmd_dup = cmd_dup + x + ',' + y + ',\'middleSchoolArea\',\'vworld\');'
cmd_dup + ','
print(cmd_dup)

driver.execute_script(cmd_dup)