# cook your dish here
t=int(input())
for _ in range(t):
    n,x,k=map(int,input().split())
    total_cost = n * x
    
    # Check if Chef has enough money
    if k >= total_cost:
        print("YES")
    else:
        print("NO")
        