"""
날짜 : 2020/12/28
이름 : 김철학
내용 : 파이썬 XML 문서 파싱(Parsing)하기
"""
import requests as req
from bs4 import BeautifulSoup as bs

# XML 문서 요청
response = req.get('https://www.w3schools.com/xml/simple.xml')

# XML 문서 파싱
dom = bs(response.text, 'html.parser')
foods = dom.select('breakfast_menu > food')

# 데이터 출력
for food in foods:
    print('---------------')
    print('이름 : ', food.name)
    print('가격 : ', food.price.text)
    print('열량 : ', food.calories.text)
