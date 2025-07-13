# cook your dish here
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    n=int(x/10)
    print(n*y)