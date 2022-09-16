s=input()

#()를 기준으로 앞 뒤를 나눠서 숫자를 셈
#|||()|||이라면 앞3 뒤3
index=s.find('(')
f=index
b=len(s)-(index+2)

#앞뒤 갯수가 같으면 correct 아니면 fix
if(f==b): print('correct')
else: print('fix')