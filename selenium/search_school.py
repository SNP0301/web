from selenium import webdriver ### import webdriver

def open_default_url():
    driver = webdriver.Chrome()
    driver.get("https://schoolzone.emac.kr/gis/gis.do")

    while(True):
        pass ###  .get(url)함수가 종료되면 브라우저도 함께 종료되는 것을 방지하기 위해 무한 루프 생성

open_default_url()

time.sleep(3)

elem = driver.find_element_by_id('searchText')

elem.clear()
elem.send_keys("search text is here!")
elem.send_keys(Keys.RETURN)
