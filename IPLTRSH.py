# cook your dish here
t=int(input())
i=1
while(i<=t):
    x,y=map(int,input().split())
    if((x-y)<=0):
        print(0)
    else:
        print(x-y)
    i+=1