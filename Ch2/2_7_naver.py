"""
날짜 : 2020/12/29
이름 : 김철학
내용 : 네이버 실시간 검색어 수집하기
"""
import requests as req
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from datetime import datetime

# 크롬 가상 웹브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')
browser.implicitly_wait(3)

# 네이버 데이터랩 이동
browser.get('https://datalab.naver.com/keyword/realtimeList.naver')
browser.implicitly_wait(3)

# 네이버 실검 1 ~ 10까지 파싱
item_boxs = browser.find_elements_by_css_selector('#content .selection_area .field_list ul:nth-child(1) > li > .item_box')

# 디렉터리 생성

# 파일 저장
fname = "{:%y-%m-%d-%H-%M.txt}".format(datetime.now())
file = open('./naver/'+fname, mode='w', encoding='utf8')
file.write('순위,제목,날짜\n')

for item_box in item_boxs:
    file.write('%s,' % item_box.find_element_by_css_selector('.item_num').text)
    file.write('%s,' % item_box.find_element_by_css_selector('.item_title').text)
    file.write('%s\n' % "{:%y%m%d%H%M%S}".format(datetime.now()))


file.close()

print('수집완료...')


