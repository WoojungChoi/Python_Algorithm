
def encipher(p, k):
    solve = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
    string  = str()
    for i in range(len(p)):
        for j in range(len(solve)):
            if (p[i]==solve[j]):
                dump = j
        #new_list.append(solve[(dump-k)%27])
        string = string + solve[(dump-k)%27]

    return string


while True:
    inputkey = int(input())
    print('키:',inputkey)
    if(inputkey == 999):
        print('프로그램 종료')
        break
    inputval  = str(input())
    print('암호문:',inputval)
    print('평  문:', encipher(inputval, inputkey))



