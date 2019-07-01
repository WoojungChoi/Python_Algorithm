import pymongo
import sys
import csv

#DB 연결
username = 'woochoi'
password = '123123'
connection = pymongo.MongoClient('localhost', 27017)

#DB 목록 출력하기
print('DB목록')
for db in connection.list_databases():
    print(db)

#DB 선택
db_sample = connection.get_database('sample')

#Collection 목록 출력
collection_list = db_sample.collection_names()
print('Collection 목록 출력', collection_list)

#Collection(Table) 선택
collection = db_sample.get_collection('user')

#Collection에서 조회하기
results = collection.find()
for result in results:
    print(result)
'''
with open('solar_2013.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
        try:
            collection.insert(row)
            print('succeed')
        except:
            print("insert failed", "\nData: ", row , sys.exc_info()[0])
'''