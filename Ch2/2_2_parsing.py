"""
날짜 : 2020/12/28
이름 : 김철학
내용 : 파이썬 HTML 페이지 파싱(Parsing)하기

parsing
 - 문서 해독을 의미하는 용어
 - 마크업 문서(HTML, XML)에서 특정 태그의 데이터를 추출하는 처리과정
"""
import requests as req
from bs4 import BeautifulSoup as bs

# HTML 요청(Anti-Crawling 적용)
response = req.get('https://news.naver.com/', headers={'User-Agent':'Mozilla/5.0'})

# HTML 파싱
dom = bs(response.text, 'html.parser')
titles = dom.select('#today_main_news > div.hdline_news div.hdline_article_tit > a')

# 데이터 출력(strip() : 공백제거)
for tit in titles:
    print(tit.text.strip())

