n = int(input("Enter number of items: "))

weight = []
profit = []

for i in range(n):
    weight.append(int(input("Enter weight: ")))
    profit.append(int(input("Enter profit: ")))

capacity = int(input("Enter knapsack capacity: "))

# Create DP table
dp = [[0] * (capacity + 1) for i in range(n + 1)]

# Dynamic Programming
for i in range(1, n + 1):
    for w in range(capacity + 1):
        if weight[i-1] <= w:
            dp[i][w] = max(profit[i-1] + dp[i-1][w-weight[i-1]],
                           dp[i-1][w])
        else:
            dp[i][w] = dp[i-1][w]

print("Maximum Profit:", dp[n][capacity])