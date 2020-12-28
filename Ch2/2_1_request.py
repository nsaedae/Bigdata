"""
날짜 : 2020/12/28
이름 : 김철학
내용 : 파이썬 HTML 요청 실습하기
"""
import urllib.request as req

# 네이버 페이지 요청
response = req.urlopen('http://naver.com').read()
html = response.decode('utf-8')

# 요청페이지 출력
print(html)