"""
날짜 : 2020/12/28
이름 : 김철학
내용 : 파이썬 데이터 전송하기
"""
import requests as req
from bs4 import BeautifulSoup as bs

# 세션시작
sess = req.session()

# 부산일보 로그인 요청
url = 'https://here.busan.com/bbs/login_check.php'
sess.post(url, data={'mb_id': 'ksb0503', 'mb_password': '123456789'})

# 마이페이지 요청
html = sess.get('https://here.busan.com/member/member_mypage.php')

# HTML 파싱 후 데이터 출력
dom = bs(html.text, 'html.parser')
span_id = dom.select_one('#design_contents > dl > dd > span.id')
point = dom.select_one('#design_contents > div.point > font:nth-child(1)')

print('아이디 : ', span_id.text)
print('포인트 : ', point.text)






