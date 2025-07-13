# cook your dish here
t=int(input())
for _ in range(t):
    n,x,y=map(int,input().split())
    total_pages = x*y
    
    # Check if Chef can complete the book
    if total_pages >= n:
        print("YES")
    else:
        print("NO")