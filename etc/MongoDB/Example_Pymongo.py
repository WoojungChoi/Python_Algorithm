import pymongo
import sys

#MongoDB 접속 'default: localhost 27017'
username = 'woochoi'
password = '123123'
connection = pymongo.MongoClient('localhost', 27017)

#DB생성
'''
db_new = connection.new
'''

#Collection(Table) 생성
'''
collection_new = db_new.collectionName
'''

#DB 목록 출력하기
print('DB목록 출력')
for db in connection.list_databases():
    print(db)

#DB선택(로컬 내 DB 이름: sample)
db_sample = connection.get_database('sample')

#Collection 목록 출력하기
collection_list = db_sample.collection_names()
print('Collection 목록 출력', collection_list)

#Collection(Table)선택(로컬 내 Collection 이름: user)
collection = db_sample.get_collection('user')

#Collection에서 조회하기
results = collection.find()
for result in results:
    print(result)

##$gt: '~보다 크다'
results = collection.find({'empno': {"$gt":10001}})
#for result in results:
#    print(result)

#Update문
#collection.update({업데이트를 위해 선택할 key-value쌍}, {수정될 내용의 key-value쌍}
# ,upsert=false, multi=false) upsert, multicond 파라미터 디폴트:false
collection.update({'name':'park'}, {'name':'park', 'empno':10004,'phone':'010-0000-0010'},
                  upsert=False, multi = False)

doc = dict(name='park', empno=10005, phone='010-0000-0005', age=55)
try:
    collection.insert(doc)
except:
    print("insert failed", "\nData: ", doc ,sys.exc_info()[0])

#Remove문
collection.remove({'name':'park'}, {'empno': 10001})





#Documents: RDB의 Records
#examples
doc1 = {'empno':10001, 'name': 'Hong', 'phone': '010-0000-0001', 'age': 11}
doc2 = {'empno':10002, 'name': 'Choi', 'phone': '010-0000-0002', 'age': 22}
doc3 = {'empno':10003, 'name': 'Park', 'phone': '010-0000-0003', 'age': 33}
