from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

import time
import pandas as pd
import openpyxl as op

def clear():
    search_box = driver.find_element(By.XPATH, '//*[@id="searchWord"]')
    search_box.click()
    search_box.send_keys(Keys.COMMAND + 'A')
    search_box.send_keys(Keys.DELETE)
    time.sleep(0.7)
    return True

### input excel
input_book = op.load_workbook('/Users/snp/web/Selenium/search_list.xlsx')
input_sheet = input_book.active

### output excel
output_book = op.load_workbook('/Users/snp/web/Selenium/output.xlsx') ## output file directory
output_sheet = output_book.active

### 0. 창을 연다
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.schoolinfo.go.kr/ei/ss/pneiss_a03_s0.do#")
parent_window = driver.current_window_handle

### 1. 검색창을 클릭
for i in range(1965, 2000):
    time.sleep(0.5)

    clear()
    search_box = driver.find_element(By.XPATH, '//*[@id="searchWord"]')
    search_box.click()

    ### 2. Input.txt에서 검색어를 따와서 입력
    time.sleep(0.5)
    target_school_name = output_sheet.cell(row=i, column = 14).value
    clear()
    search_box.click()
    search_box.send_keys(target_school_name)
    time.sleep(0.5)
    ##search_box.send_keys(Keys.ENTER)


    ### 3. 엔터 입력
    school_name_title = '//*[@title=\"' + output_sheet.cell(row=i, column = 7).value + '\"]'

   ### print(school_name_title)
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,school_name_title)))
    driver.find_element(By.XPATH,school_name_title).click()

    ### 4. 검색버튼 클릭
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="webSearchButton"]')))
    driver.find_element(By.XPATH,'//*[@id="webSearchButton"]').click()
    all_windows = driver.window_handles
    child_window = [window for window in all_windows if window != parent_window][0]
    driver.switch_to.window(child_window)

    ### 5. 대표번호, 관할교육청 읽기
    ## passed

    ### 6. 공시정보 옆 년도칸 클릭, 22년 선택
    WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="gsYear"]')))
    select = Select(driver.find_element(By.XPATH, '//*[@id="gsYear"]'))
    select.select_by_value('2022')

    ### 7. 선택버튼 클릭
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="gsYearBtn"]')))
    driver.find_element(By.XPATH,'//*[@id="gsYearBtn"]').click()

    ### 8. 학생현황 클릭 
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div/div[3]/div[2]/ul/li[3]/a')))
    driver.find_element(By.XPATH,'/html/body/div/div[3]/div[2]/ul/li[3]/a').click()


    ### 9. 졸업생의 진로 현황 클릭 
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div/div[3]/div[2]/div/div[3]/ul/li[7]/a')))
    driver.find_element(By.XPATH,'/html/body/div/div[3]/div[2]/div/div[3]/ul/li[7]/a').click()

    ### 10. 명시적 wait 이후 남 졸업자~무직자 및 미상, 여 졸업자~무직자 및 미상 긁기 --> 한 행에 저장
    ##남자
    td_arr = [1,2,3,4,5,6,7,9,10,12,14,15,16]

    WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div/div[3]/div[4]/div[3]/div[1]/div[2]/div/div[1]/table/tbody/tr[1]/td[1]')))

    k = 15
    for j in range(0,13):
        xpath_parameter_male = '/html/body/div/div[3]/div[4]/div[3]/div[1]/div[2]/div/div[1]/table/tbody/tr[1]/td[' + str(td_arr[j]) + ']'
        output_sheet.cell(row=i,column=k).value = driver.find_element(By.XPATH,xpath_parameter_male).text


        xpath_parameter_female = '/html/body/div/div[3]/div[4]/div[3]/div[1]/div[2]/div/div[1]/table/tbody/tr[2]/td[' + str(td_arr[j]) + ']'
        output_sheet.cell(row=i,column=k+13).value = driver.find_element(By.XPATH,xpath_parameter_female).text

        k = k + 1

    output_book.save('/Users/snp/web/Selenium/output.xlsx')

    driver.close() ### 자녀 창 작업 종료
    driver.switch_to.window(parent_window) ## 부모창으로 전환   
    time.sleep(0.5)

    clear()
    if(clear()==True):
        print("[%d]: %s done"%(i,target_school_name))
        time.sleep(0.3)
    else:
        time.sleep(0.3)
        clear()
