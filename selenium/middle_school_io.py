from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
import openpyxl as op

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
for i in range(6, 3279):
    search_box = driver.find_element(By.XPATH, '//*[@id="searchWord"]')
    search_box.click()

    ### 2. Input.txt에서 검색어를 따와서 입력
    target_school_name = input_sheet.cell(row=i, column = 10).value
    search_box.send_keys(target_school_name)
    time.sleep(0.5)
    search_box.send_keys(Keys.ENTER)

    ### 3. 엔터 입력
    time.sleep(0.5)
    search_box.send_keys(Keys.ENTER)

    ### 4. 검색버튼 클릭
    driver.find_element(By.XPATH,'//*[@id="webSearchButton"]').click()
    all_windows = driver.window_handles
    child_window = [window for window in all_windows if window != parent_window][0]
    driver.switch_to.window(child_window)
    time.sleep(0.5)

    ### 5. 대표번호, 관할교육청 읽기
    ### 6. 공시정보 옆 년도칸 클릭, 22년 선택
    select = Select(driver.find_element(By.XPATH, '//*[@id="gsYear"]'))
    select.select_by_value('2022')

    ### 7. 선택버튼 클릭
    driver.find_element(By.XPATH,'//*[@id="gsYearBtn"]').click()
    time.sleep(0.05)

    ### 8. 학생현황 클릭 
    driver.find_element(By.XPATH,'/html/body/div/div[3]/div[2]/ul/li[3]/a').click()
    time.sleep(0.05)


    ### 9. 졸업생의 진로 현황 클릭 
    driver.find_element(By.XPATH,'/html/body/div/div[3]/div[2]/div/div[3]/ul/li[7]/a').click()
    time.sleep(1)

    ### 10. 명시적 wait 이후 남 졸업자~무직자 및 미상, 여 졸업자~무직자 및 미상 긁기 --> 한 행에 저장
    output_sheet.cell(row=i, column=1).value = i
    output_sheet.cell(row=i, column=2).value = target_school_name
    time.sleep(2)
    
    output_sheet.cell(row=i, column=6).value = driver.find_element(By.XPATH,'//*[@id="mCSB_11_container"]/table/tbody/tr[1]/td[1]').text
    output_sheet.cell(row=i, column=7).value = driver.find_element(By.XPATH,'//*[@id="mCSB_11_container"]/table/tbody/tr[1]/td[2]').text

    output_book.save('/Users/snp/web/Selenium/output.xlsx')

    driver.close() ### 자녀 창 작업 종료
    driver.switch_to.window(parent_window) ## 부모창으로 전환

    search_box.click()
    search_box.send_keys(Keys.COMMAND + 'a')
    search_box.send_keys(Keys.DELETE)

    
    time.sleep(1)

