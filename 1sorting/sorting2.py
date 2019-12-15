import time
import numpy as np
import random


def quickSort(a, l,r):
    if r-l > 1:
        mid = int((l+r)/2)
        if a[l] > a[mid] :
            a[l], a[mid] = a[mid], a[l]
        if a[mid] > a[r]:
            a[mid], a[r]=a[r], a[mid]
        if a[l] > a[mid]:
            a[l], a[mid] = a[mid], a[l]
        a[mid], a[r-1] = a[r-1], a[mid]

        v,i,j = a[r], l-1, r
        while True:
            i+=1
            while a[i] < v:
                i+=1
            j-=1
            while a[j] >v:
                j-=1
            if i>=j:
                break
            a[i], a[j] = a[j], a[i]
        a[i], a[r] = a[r], a[i]
        quickSort(a, l, i-1)
        quickSort(a, i+1, r)

def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if(a[i] > a[i+1]):
            isSorted = False
        if (not isSorted):
            break
        if isSorted:
            print("정렬완료")
        else:
            print("정렬오류")



# 난수 추출하기!!
def makerandintlist(n):
    randlist = []
    for n in range(0, n):
        randlist.append(random.randint(1,100000))
    return randlist



#_________________________________________________________________________#
if __name__ == '__main__':

    M=15

    lists=[]
    # 난수 추출하기
    for i in range(7):
        temp_list = makerandintlist((i+1)*300000)
        print(len(temp_list))
        lists.append(temp_list)
        lists[i].insert(0, -1)

    time_quick = []


    for i in range(len(lists)):
        starttime= time.time()
        quickSort(lists[i], 1, len(lists[i])-1)
        time_quick.append(time.time()-starttime)
        print('iter', i, ' 실행시간: ', time_quick[i])

