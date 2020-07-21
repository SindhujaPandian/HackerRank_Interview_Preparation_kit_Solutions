from collections import Counter
n=int(input())
arr=list(map(int,input().split()))
count=0
for val in Counter(arr).values():
    count+=val//2
print(count)
