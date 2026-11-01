n = int(input("Enter number of jobs: "))

jobs = []

for i in range(n):
    job = input("Enter job name: ")
    deadline = int(input("Enter deadline: "))
    profit = int(input("Enter profit: "))
    jobs.append([job, deadline, profit])

jobs.sort(key=lambda x: x[2], reverse=True)

max_deadline = max(job[1] for job in jobs)
slots = [None] * max_deadline

total_profit = 0

for job in jobs:
    for j in range(job[1] - 1, -1, -1):
        if slots[j] is None:
            slots[j] = job[0]
            total_profit += job[2]
            break

print("\nScheduled Jobs:", [j for j in slots if j is not None])
print("Maximum Profit:", total_profit)