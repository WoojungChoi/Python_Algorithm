def bruteForce(p, t, k):
    M = len(p)
    N = len(t)
    i=k
    j=0
    while j< M and i < N:
        if t[i] !=p[j]:
            i -=j
            j = -1
        i +=1
        j +=1
    if j==M: return i-M

    else: return i

def findmail(num, t):
    x = '"'
    dump = num + 7
    while True:
        if(x == t[dump]):break
        print(t[dump], end='')
        dump+=1

text = '<ul> <li> <a href="mailto:gdhong@hanmail.net">Gildong Hong</a> <li> <a href="mailto:gsjang@yahoo.co.kr">Gilsan Jang</a> <li> <a href="mailto:yhkim@naver.com">Younghee Kim</a> <li> <a href="mailto:cslee@gmail.com">Cheolsu Lee</a> </ul>'
pattern = 'mailto:'
M = len(pattern)
N = len(text)
K=0
while True:
    pos = bruteForce(pattern, text, K)
    K = pos + M
    if K<N:
        #print(findmail(pos, text))
        findmail(pos, text)
        print()
    else:break
