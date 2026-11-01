n = int(input("enter number of jobs "))

jobs = []

for i  in range(n):

    job = input("enter job name ")
    deadline = int(input("enter deadline "))
    profit = int(input("enter profit "))

    jobs.append([job, deadline, profit])

    jobs.sort(key=lambda x: x[2], reverse=True)

    max_profit = max(job[1] for job in jobs)

    slots = [None] * max_profit

    total_profit = 0

for job in jobs: