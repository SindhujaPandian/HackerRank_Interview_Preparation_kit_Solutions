height,count = 0,0
n=int(input())
s=input()
for i in range(n):
    if(s[i]=='U'):
        height+=1
        if height==0:
            count+=1
    else:
        height-=1
            
print(count)
        
