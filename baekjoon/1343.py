board=input()

before=[]
answer=''
#AAAA BB
for i in range(len(board)):
    if board[i]=='.':
        if not before:
            answer+='.'
            continue
        else:
            if len(before)%4==0:
                k=len(before)//4
                answer+='AAAA'*k
            else:
                if len(before)%2==0:
                    k=len(before)//4
                    m=(len(before)-4*k)//2
                    answer+='AAAA'*k
                    answer+='BB'*m
                else:
                    answer='-1'
                    break
        answer+='.'
        before.clear()
    else:
        before.append(board[i])


if before:
    if len(before)%4==0:
        k=len(before)//4
        answer+='AAAA'*k
    else:
        if len(before)%2==0:
            k=len(before)//4
            m=(len(before)-4*k)//2
            answer+='AAAA'*k
            answer+='BB'*m
        else:
            answer='-1'    

print(answer)
