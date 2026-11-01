n = int(input("Enter the number of terms: "))

a = 0
b = 1
count = 0

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    count += 1

    c = a + b
    count += 1

    a = b
    count += 1

    b = c
    count += 1

print("\nStep Count:", count)