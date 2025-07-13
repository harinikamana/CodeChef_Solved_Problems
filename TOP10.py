# cook your dish here
n = int(input())

# Iterate over each test case
for _ in range(n):
    rank = int(input())
    
    # Check if the rank is less than or equal to 10
    if rank <= 10:
        print("YES")
    else:
        print("NO")