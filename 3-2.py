l = [2, 3, 4, 5, 6]
result = []
for i in range(len(l) // 2 + len(l) % 2):
    result.append(l[i] * l[len(l) - i - 1])

print(result)