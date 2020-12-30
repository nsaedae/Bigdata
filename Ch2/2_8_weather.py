"""
날짜 : 2020/12/30
이름 : 김철학
내용 : 파이썬 기상청 날씨 데이터 수집하기
"""
import os
import requests as req
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

# 디렉터리 생성
dir = "./weather/{:%Y-%m-%d}".format(datetime.now())

if not os.path.exists(dir):
    os.makedirs(dir)


# 파일 저장
fname = "{:%y-%m-%d-%H-%M.txt}".format(datetime.now())
file = open(dir+'/'+fname, mode='w', encoding='utf-8')

file.write('지점,현재일기,시정,운량,중하운량,현재기온,이슬점온도,체감온도,일강수,적설,습도,풍향,풍속,해면기압\n')

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

    file.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14))

# 파일닫기
file.close()

# 브라우저 종료
browser.close()
browser.quit()

print('날씨 데이터 수집완료')

