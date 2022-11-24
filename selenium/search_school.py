from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd
import openpyxl as op

## 00. Setup Environment
options = Options()
options.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=options)
driver.get("https://schoolzone.emac.kr/gis/gis.do")

school_list = pd.read_excel('/Users/snp/Documents/schools.xlsx')

w_book = op.load_workbook('/Users/snp/Documents/schools.xlsx')
w_sheet = w_book.active
print(w_sheet.cell(row=1,column=2).value)
print(w_sheet.cell(row=2,column=3).value)
print(w_sheet.cell(row=3,column=4).value)

school_name = driver.find_element(By.ID,'searchText')
school_name.send_keys('살레시오고등학교' + Keys.ENTER)

#time.sleep(0.5) ## wait for 500m
#driver.find_element(By.XPATH,'/html/body/div[1]/div[11]/div[1]/p/input').send_keys(Keys.ENTER)
#driver.find_element(By.XPATH,'/html/body/div[1]/div[10]/div[1]/p/input').send_keys(Keys.ENTER)

## 01. Move on search frame and get attribute: address of x and y
e_frame = driver.find_element(By.XPATH,'//*[@id="searchIframe"]')
driver.switch_to.frame(e_frame)

elem = driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/ul[1]')
x_addr = elem.get_attribute('x')
y_addr = elem.get_attribute('y')

## 02. Search school area using address
cmd_dup = "parent.fn_getSchoolArea(" + x_addr + ',' + y_addr + ',\'middleSchoolArea\',\'vworld\');'
driver.execute_script(cmd_dup)
driver.switch_to.default_content()

## 03. Move on search frame and extract school area text
driver.find_element(By.XPATH,'/html/body/div[1]/div[10]/div[1]/p/input').send_keys(Keys.ENTER)
i_frame = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[2]/div/div[2]/iframe')
driver.switch_to.frame(i_frame)

area_name = driver.find_element(By.XPATH,'//*[@id="middleSchoolArea"]/div/p').text
print(area_name)
driver.switch_to.default_content()