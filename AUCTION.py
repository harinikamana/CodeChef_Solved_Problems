# cook your dish here
t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    if((a>b)and(a>c)):
        print("Alice")
    elif((b>a)and(b>c)):
        print("Bob")
    else:
        print("Charlie")