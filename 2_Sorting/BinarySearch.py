def binarySearch(a, key, left, right)
    if(left<=right):
        mid = (left+right)/2
        if(key < a[mid]): return binarySearch(a, key, left, mid-1)
        elif(key > a[mid]): return binarySearch(a, key, left, mid+1)
        else: return mid
    else: return -1

a=[1,3,5,8,13,15,19,23,24,30]