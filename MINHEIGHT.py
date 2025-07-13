# cook your dish here
# Number of test cases
T = int(input())

# Loop over each test case
for _ in range(T):
    # Read the height of Chef's son and the minimum required height
    X, H = map(int, input().split())
    
    # Check if Chef's son can go on the ride
    if X >= H:
        print("YES")
    else:
        print("NO")
