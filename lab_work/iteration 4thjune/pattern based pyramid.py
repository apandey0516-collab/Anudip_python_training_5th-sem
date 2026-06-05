#program to display pattern based pyramid
rows = int(input("Enter number of rows: "))

# Straight pattern
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print("Reverse Pattern")

# Reverse pattern
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()