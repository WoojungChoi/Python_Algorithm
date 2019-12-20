def mergeSort(a, l, r):
    if r> l:
        mid = int((r+1)/ 2)
        mergeSort(a, l, mid)
        mergeSort(a, mid+1, r)
        for i in range(mid+1, l, -1):
            b[i-1] = a[i-1]
        i -= 1
        for j in range(mid, r):
            b[r+mid-j] = a[j+1]
        j+=1
        for k in range(l, r+1):
            if b[i] < b[j]:
                a[k] = b[i]
                i+=1
            else:
                a[k] = b[j]
                j-=1


def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if (a[i] > a[i + 1]):
            isSorted = False
        if (not isSorted):
            break
    if isSorted:
        print('정렬 완료')
    else:
        print('정렬 오류 발생')


import random ,time, sys

N = 10000
a = []
a.append(None)
for i in range(N):
    a.append(random.randint(1, N))
b = a.copy()
start_time = time.time()
mergeSort(a, 1, N)
end_time = time.time() - start_time
print('합병 정렬의 실행 시간 (N=%d) : %0.3f' %(N, end_time))
checkSort(a, N)