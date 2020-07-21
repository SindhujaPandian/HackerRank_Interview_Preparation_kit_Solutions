n=input()
num=int(input())
slen,newstr=len(n),''
if(n=='a'):
    print(num)
else:
    for i in range(0,num,slen):
        newstr+=n
    if(len(newstr)!=num):
        rem=num-len(newstr)
        newstr+=n[:rem]
    count=0
    for i in range(num):
        if(newstr[i]=='a'):
            count+=1
    print(count)        
