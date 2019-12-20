class node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

class Dict:
    x = p = node

    z = node(key=0, left=0, right=0)
    z.left = z
    z.right = z
    head = node(key=0, left=0, right=z)

    def search(self, search_key):
        x = self.head.right
        while x != self.z:
            if x.key == search_key:
                return x.key
            if x.key > search_key:
                x= x.left
                print('left ', end='')
            else:
                x = x.right
                print('right ', end='')
        return -1

    def insert(self, v):
        x = p = self.head
        while (x != self.z):
            p = x
            if x.key ==v:
                return
            if x.key > v:
                x = x.left

            else:
                x = x.right

        x = node(key=v, left = self.z, right = self.z)
        if p.key > v:
            p.left = x
        else:
            p.right = x

import random, time, sys

N = 8
#key = list(range(1, N+1))
#s_key = list(range(1, N+1))
#random.shuffle(key)
key = [2,1,7,8,6,3,5,4]
#s_key = [8,5,10]
d = Dict()
for i in range(N):
    d.insert(key[i])
start_time = time.time()
'''
for i in range(len(s_key)):
    print('탐색 키 입력: ', s_key[i])
    result = d.search(s_key[i])
    if (result == -1) or (result != s_key[i]):
        print('\n탐색 실패')
    else:
        print('\n탐색 성공')
    print()
'''

while True:
    inputval  = int(input())
    print('탐색 키 입력 : ', inputval)
    if(inputval == 999):
        print('프로그램 종료')
        break

    result = d.search(inputval)
    if (result == -1):
        print('\n탐색 실패')
    else:
        print('\n탐색 성공')
    print()



