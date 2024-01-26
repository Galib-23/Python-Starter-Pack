numbers = [1, 2, 2, 3, 4, 3, 5, 6, 7, 7]
unique = []
for i in numbers:
    if i not in unique:
        unique.append(i)
print(unique)