"""
날짜 : 2020/12/29
이름 : 김철학
내용 : 네이버 실시간 검색어 수집하기
"""
import os
import requests as req
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from datetime import datetime

# 리눅스용 Chrome 브라우저 설치
# 크롬 가상 웹브라우저 실행(headless 모드)
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument('--headless')
chrome_option.add_argument('--no-sandbox')
chrome_option.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome('./chromedriver.exe', options=chrome_option)
browser.implicitly_wait(3)

# 네이버 데이터랩 이동
browser.get('https://datalab.naver.com/keyword/realtimeList.naver')
browser.implicitly_wait(3)

# 네이버 실검 1 ~ 10까지 파싱
item_boxs = browser.find_elements_by_css_selector('#content .selection_area .field_list ul:nth-child(1) > li > .item_box')

# 디렉터리 생성
dir = "./naver/{:%Y-%m-%d}".format(datetime.now())

if not os.path.exists(dir):
    os.makedirs(dir)

# 파일 저장
fname = "{:%y-%m-%d-%H-%M.txt}".format(datetime.now())
file = open(dir+'/'+fname, mode='w', encoding='utf8')
file.write('순위,제목,날짜\n')

for item_box in item_boxs:
    file.write('%s,' % item_box.find_element_by_css_selector('.item_num').text)
    file.write('%s,' % item_box.find_element_by_css_selector('.item_title').text)
    file.write('%s\n' % "{:%y%m%d%H%M%S}".format(datetime.now()))

file.close()

# 브라우저 종료
browser.close()

print('수집완료...')


