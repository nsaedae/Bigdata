"""
날짜 : 2022/03/02
이름 : 김철학
내용 : 파이썬 영화리뷰 크롤링 실습
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import logging
import time

# 가상 브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')

# 네이버 영화 랭킹 이동
browser.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt')
