#MongoDB

import pprint
from pymongo import MongoClient
from pymongo.errors import BulkWriteError
from datetime import datetime
import time
import pandas as pd
import numpy as np
import sys
import re
from pytz import timezone
import copy

KST = timezone('Asia/Seoul')

def MongoDB_query(_db_name, skip_num):
    # mongodb에서 data를 query하기 위한 함수(read 권한만 있는 계정)
    client = MongoClient('125.140.110.217:27017', username='guest', password='keti', authSource='guest')

    # Select 'Hanuri Tien' DB
    db = client[_db_name]

    # Select ALL collection of Hanuri Tien DB
    coll = db["ALL"]
    if skip_num == int(0):
        hanuri_all = coll.find(no_cursor_timeout=True)
    else:
        hanuri_all = coll.find(no_cursor_timeout = True).skip(skip_num)

    return hanuri_all

def MongoDB_insert(_data, _db_name, _collection_name):
    #mongodb에 data를 insert하기 위한 함수(read and write 권한이 있는 계정)
    MONGO_URL = 'mongodb://root:keti1234@125.140.110.217:27017/admin?authSource=admin'
    with MongoClient(MONGO_URL) as client:
        db = client[_db_name]
        coll = db['A'+_collection_name]
        try:
            coll.insert_many(_data)
        except BulkWriteError as exc:
            print('\n')
            pprint.pprint(exc.details['writeErrors'][0]['errmsg'])
            print('\n')
            pass

def MongoDB_query(_db_name):
    client = MongoClient('125.140.110.217:2701', username = 'guest', password='keti', authSourc='guest')
    db=client[_db_name]
    coll = db["201905"]
    Elex_all = coll.find(no_cursor_timeout= True).skip(4000000).limit(100000000)


#_____________________________________Sourced by xiewenqian
#MongoDB 연결 이거 굳이?
def _connect_mongo(host, port, username, password, db):
    if username and password:
        mongo_uri = 'mongodb://%s:%s@%s/%s' % (username, password, host, port, db)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)
    return conn[db]

#MongoDB 읽기
def read_mongo(db, collection, query={}, host='localhost', port = 27017, username=None, password=None, no_id=True)
    db = _connect_mongo(host=host, port=port, username=username, password=password, db=db)

    # Make a query to the specific DB and Collection
    cursor = db[collection].find(query)

    # Expand the cursor and construct the DataFrame
    df = pd.DataFrame(list(cursor))

    #Delete the _id
    if no_id and '_id' in df:
        del df['_id']

    return df
'''
if __name__ == '__main__':
    df = read_mongo('db_test', 'db_collection', {}, '172.168.203.174', 10800)
    df.to_csv('', index=False)
'''