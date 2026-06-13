n = (3, 14, 7, 22, 9, 41, 18, 5)

filtered = ()

for num in n:
    if num > 10:
        filtered += (num,)

print("Filtered Tuple:", filtered)
