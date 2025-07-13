# cook your dish here
# Function to determine runs needed to win
def runs_needed_to_win(test_cases):
    results = []
    for case in test_cases:
        X, Y = case
        runs_needed = X - Y
        results.append(runs_needed)
    return results

# Input handling
T = int(input())  # Number of test cases
test_cases = []

for _ in range(T):
    X, Y = map(int, input().split())  # Read the target and current score
    test_cases.append((X, Y))

# Calculate and print results
results = runs_needed_to_win(test_cases)
for result in results:
    print(result)
