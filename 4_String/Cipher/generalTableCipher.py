def encipher(p, k):
    c = ''
    for i in range(len(p)):
        a = ord(p[i])
        if a == 32:
            a = 0
        else:
            a -= 64
        c += k[a]
    return c

plainText = 'SAVE PRIVATE RYAN'
K = 'QHCBEJKARWSTUVD IOPXZFGLMNY'
print('평  문 : ', plainText)
cipherText = encipher(plainText, K)
print('암호문 : ', cipherText)