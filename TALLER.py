# cook your dish here
# Read the number of test cases
T = int(input())

# Loop through each test case
for _ in range(T):
    # Read the two integers X and Y
    X, Y = map(int, input().split())
    
    # Compare the heights and print the result
    if X > Y:
        print("A")
    else:
        print("B")