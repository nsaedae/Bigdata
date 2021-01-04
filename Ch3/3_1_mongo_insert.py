"""
날짜 : 2021/01/04
이름 : 김철학
내용 : 파이썬 Mongodb 프로그래밍
"""
from pymongo import MongoClient as mongo
from datetime import datetime

# 1단계 - mongodb 접속
conn = mongo('mongodb://chhak:1234@192.168.56.101:27017')

# 2단계 - DB 선택
db = conn.get_database('chhak')

# 3단계 - Collection(테이블) 선택
collection = db.get_collection('member')

# 4단계 - 쿼리실행
collection.insert_one({'uid':'a101', 'name':'김유신', 'hp':'010-1234-1111', 'pos':'사원', 'dep':101, 'rdate': datetime.now()})
collection.insert_one({'uid':'a102', 'name':'김춘추', 'hp':'010-1234-2222', 'pos':'과장', 'dep':103, 'rdate': datetime.now()})
collection.insert_one({'uid':'a103', 'name':'장보고', 'hp':'010-1234-3333', 'pos':'대리', 'dep':102, 'rdate': datetime.now()})
collection.insert_many([{'uid':'a104', 'name':'강감찬', 'hp':'010-1234-4444', 'pos':'차장', 'dep':104, 'rdate': datetime.now()},
                        {'uid':'a105', 'name':'이순신', 'hp':'010-1234-5555', 'pos':'부장', 'dep':105, 'rdate': datetime.now()}])

print('Insert 완료...')









