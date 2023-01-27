from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time
import pandas as pd
import openpyxl as op



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.schoolinfo.go.kr/ei/ss/pneiss_a03_s0.do#")
parent_window = driver.current_window_handle

output_book = op.load_workbook('/Users/snp/web/Selenium/output.xlsx') ## output file directory
output_sheet = output_book.active

input_book = op.load_workbook('/Users/snp/web/Selenium/search_list.xlsx')
input_sheet = input_book.active


### 0. 창을 연다
### 1. 검색창을 클릭
### 2. Input.txt에서 검색어를 따와서 입력
### 3. 밑에 뜨는 목록 박스의 첫번째 칸을 클릭
### 4. 검색버튼 클릭
### 5. 대표번호, 관할교육청 읽기
### 6. 공시정보 옆 년도칸 클릭, 22년 선택
### 7. 선택버튼 클릭
### 8. 학생현황 클릭
### 9. 졸업생의 진로 현황 클릭
### 10. 명시적 wait 이후 남 졸업자~무직자 및 미상, 여 졸업자~무직자 및 미상 긁기 --> 한 행에 저장