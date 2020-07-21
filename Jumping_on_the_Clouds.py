n=int(input())
arr=list(map(int,input().split()))
i,count=0,-1
while(i<n):
    if(arr[i]!=1):
        print(i,'->',end='')
        count+=1
    if(i!=n-1 and arr[i+2]!=0):
        i+=1
    else:
        i+=2
print('\ncount = ',count)
