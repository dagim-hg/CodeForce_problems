rows = int(input("How many rows? "))
nested_list = []

for i in range(rows):
    row = list(map(int, input(f"Enter row {i+1}: ").split()))
    nested_list.append(row)

print(nested_list)
count = 0
for i in nested_list:
    row1 = i .count(1)
    if row1 == 3:
        count += 1
    elif row1 == 2:
        count += 1
    else:
        count += 0
print(count)