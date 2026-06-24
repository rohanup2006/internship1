t = (12, 45, 7, 89, 23)

total = 0
highest = t[0]
lowest = t[0]

for num in t:
    total += num

    if num > highest:
        highest = num

    if num < lowest:
        lowest = num

print("Total =", total)
print("Highest =", highest)
print("Lowest =", lowest)