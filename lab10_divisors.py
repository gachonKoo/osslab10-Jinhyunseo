numbers = int(input("Enter a number: "))

for i in range(1, numbers + 1):
    if numbers % i == 0:
        print(i, end=" ")

print()
