# -*- coding:utf-8 -*-

import pprint
import pymongo
from pymongo import MongoClient
from pymongo.errors import BulkWriteError
import time
import pandas as pd
import os
import sys
import math
import re
from datetime import timedelta, datetime
from pytz import timezone
import copy
import csv

#start_time = time.time()

KST = timezone('Asia/Seoul')

MONGO_DB_LIST = ['elex', 'hanuri', 'umc', 'public']
_db_name = MONGO_DB_LIST[1]
skip_num = 168735981

client = MongoClient('125.140.110.217:27017', username='guest', password = 'keti', authSource='guest')

print('\nDB 목록 출력')
for db in client.list_databases():
    print(db)
time.sleep(1)

#db = client[_db_name]
db_elex = client.get_database('elex')
db = client[_db_name]

#Collection 목록 출력하기
collection_list = db_elex.collection_names()
print('\nCollection 목록 출력\n', collection_list, '\n\n')

select_collection = input("Collection을 선택해주세요\n")
coll = db[select_collection]
print('\nCollection 내 레코드 수:\n', coll.count())

cursor = coll.find()
print('\n조회된 레코드 수:\n', cursor.count(), '\n')

#------------------------------------------------#
print('Wait');time.sleep(2)
#for result in cursor:
#    print(result)
#------------------------------------------------#

#ToPandasDF
start_time=time.time()
print('DataFrame으로 변환중...')
df = pd.DataFrame(list(cursor))
print(df.head())
print(df.dtypes)

#df_ggplot = df.iloc[:,[7,8,10]]

print("코드 실행시간 :", time.time() - start_time)

#ToCSV
#filename = input('CSV 형태로 저장할 파일명을 입력하세요\n')
#df.to_csv(filename, index=False, encoding='utf-8')


#Collection 내 데이터 조회하기
#cursor_hanuri_all = db_hanuri_all.find()
#print(cursor_hanuri_all.count())
'''
if skip_num==int(0):
    cursor_hanuri_all = db_hanuri_all.find(no_cursor_timeout=True)
else:
    cursor_hanuri_all = db_hanuri_all.find(no_cursor_timeout=True).skip(skip_num)
'''
#print(type(cursor_hanuri_all), cursor_hanuri_all)
#for i in cursor_hanuri_all:
#    print(i)

#results = db_hanuri_201901.find()
#df = pd.DataFrame(list(cursor_hanuri_all))
#print(df.head())

'''
df.to_csv('D:/MongoDB/db_hanuri_201901.csv', index=False)
'''

#_코드실행시간 측정___________________________________________________________
