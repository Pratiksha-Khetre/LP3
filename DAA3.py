def fractional_knapsack(items, capacity):

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

    return total_profit


def main():

    n = int(input("Enter number of items: "))

    items = []

    for i in range(n):
        weight = int(input("Enter weight: "))
        profit = int(input("Enter profit: "))

        ratio = profit / weight
        items.append([weight, profit, ratio])

    capacity = int(input("Enter knapsack capacity: "))

    max_profit = fractional_knapsack(items, capacity)

    print("Maximum Profit:", max_profit)


main()