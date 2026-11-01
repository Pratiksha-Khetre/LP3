n = int(input("Enter number of items: "))

items = []

for i in range(n):
    weight = int(input("Enter weight: "))
    profit = int(input("Enter profit: "))
    items.append([weight, profit, profit / weight])

capacity = int(input("Enter knapsack capacity: "))

# Sort items by profit/weight ratio
items.sort(key=lambda x: x[2], reverse=True)

total_profit = 0

for item in items:
    weight, profit, ratio = item

    if capacity >= weight:
        total_profit += profit
        capacity -= weight
    else:
        total_profit += ratio * capacity
        break

print("Maximum Profit:", total_profit)