def bubbleSort_(a, n):
    for i in range(1, 11):
        if(i%2==0):
            for j in range(i-1, 10):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
        else:
            for j in range(10-1, i-2, -1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
        print('i=',i,',', a)

def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if (a[i] > a[i+1]):
            isSorted = False
        if (not isSorted):
            break
    if isSorted:
        print('정렬 완료')
    else:
        print('정렬 오류 발생')

import random, time
a = [0,7,5,6,4,10,9,8,1,3,2]
N = len(a)
print('a = ',a)
bubbleSort_(a, N-1)
print('정렬 완료')