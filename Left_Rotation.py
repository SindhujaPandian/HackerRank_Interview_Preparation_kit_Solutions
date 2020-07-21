n=list(map(int,input().split()))
size,num=n[0],n[1]
arr=list(map(int,input().split()))
for i in range(num):
    arr=arr[1:]+arr[:1]
for i in range(size):
    print(arr[i],end=' ')
