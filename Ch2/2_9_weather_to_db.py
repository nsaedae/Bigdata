"""
날짜 : 2020/12/30
이름 : 김철학
내용 : 파이썬 기상청 날씨 데이터 수집 DB 저장하기
"""
import os
import requests as req
import pymysql as mysql
from bs4 import BeautifulSoup as bs
from datetime import datetime
from selenium import webdriver



chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument('--headless')
chrome_option.add_argument('--no-sandbox')
chrome_option.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome('./chromedriver.exe', options=chrome_option)
browser.implicitly_wait(3)

browser.get('https://www.weather.go.kr/w/weather/now.do')
browser.implicitly_wait(3)

trs = browser.find_elements_by_css_selector('#sfc-city-weather > div.cont-box02 > div > div.cont02 > div > table > tbody > tr')

# 테이블 생성
# 테이블명 구하기
table_name = "{:%Y-%m-%d}".format(datetime.now())

# 1단계 - 데이터베이스 접속
conn = mysql.connect(host='192.168.56.101',
                     user='root',
                     password='1234',
                     db='weather',
                     charset='utf8')

# 2단계 - SQL 실행객체
cursor = conn.cursor()

# 3단계 - SQL 실행
sql  = "CREATE TABLE IF NOT EXISTS `%s` ("
sql += "`col1`  VARCHAR(10) COMMENT '지역',"
sql += "`col2`  VARCHAR(10) COMMENT '현재일기',"
sql += "`col3`  VARCHAR(10) COMMENT '시정',"
sql += "`col4`  TINYINT COMMENT '운량',"
sql += "`col5`  TINYINT COMMENT '중하운량',"
sql += "`col6`  DOUBLE  COMMENT '현재온도',"
sql += "`col7`  DOUBLE  COMMENT '이슬점온도',"
sql += "`col8`  DOUBLE  COMMENT '체감온도',"
sql += "`col9`  DOUBLE  COMMENT '일강수',"
sql += "`col10` DOUBLE  COMMENT '적설',"
sql += "`col11` TINYINT COMMENT '습도',"
sql += "`col12` VARCHAR(10) COMMENT '풍향',"
sql += "`col13` DOUBLE COMMENT '풍속',"
sql += "`col14` DOUBLE COMMENT '해면기압',"
sql += "`rdate` DATETIME COMMENT '수집일'"
sql += ");"

cursor.execute(sql % table_name)

# 테이블 저장(INSERT)
sql_insert  = "INSERT INTO `"+table_name+"` SET "
sql_insert += "`col1`='%s',"
sql_insert += "`col2`='%s',"
sql_insert += "`col3`='%s',"
sql_insert += "`col4`='%s',"
sql_insert += "`col5`='%s',"
sql_insert += "`col6`='%s',"
sql_insert += "`col7`='%s',"
sql_insert += "`col8`='%s',"
sql_insert += "`col9`='%s',"
sql_insert += "`col10`='%s',"
sql_insert += "`col11`='%s',"
sql_insert += "`col12`='%s',"
sql_insert += "`col13`='%s',"
sql_insert += "`col14`='%s',"
sql_insert += "`rdate`=NOW()"

for tr in trs:
    v1 = tr.find_element_by_css_selector('td:nth-child(1) > a').text
    v2 = tr.find_element_by_css_selector('td:nth-child(2)').text
    v3 = tr.find_element_by_css_selector('td:nth-child(3)').text
    v4 = tr.find_element_by_css_selector('td:nth-child(4)').text
    v5 = tr.find_element_by_css_selector('td:nth-child(5)').text
    v6 = tr.find_element_by_css_selector('td:nth-child(6)').text
    v7 = tr.find_element_by_css_selector('td:nth-child(7)').text
    v8 = tr.find_element_by_css_selector('td:nth-child(8)').text
    v9 = tr.find_element_by_css_selector('td:nth-child(9)').text
    v10 = tr.find_element_by_css_selector('td:nth-child(10)').text
    v11 = tr.find_element_by_css_selector('td:nth-child(11)').text
    v12 = tr.find_element_by_css_selector('td:nth-child(12)').text
    v13 = tr.find_element_by_css_selector('td:nth-child(13)').text
    v14 = tr.find_element_by_css_selector('td:nth-child(14)').text

    cursor.execute(sql_insert % (v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14))
    conn.commit()


# 4단계 - 데이터베이스 종료
conn.close()

# 브라우저 종료
browser.close()
browser.quit()

print('날씨 데이터 INSERT 완료')

