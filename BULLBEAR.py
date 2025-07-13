# cook your dish here
T=int(input())
for _ in range(T):
    x,y=map(int,input().split())
    if(x>y):
        print("LOSS")
    elif(y>x):
        print("PROFIT")
    else:
        print("NEUTRAL")