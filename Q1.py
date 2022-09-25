numbers = [12, 75, 150, 180, 145, 525, 50]
result_number = []

for item in numbers:

    if item > 500:
        break
    if item > 150:
        continue
    if item % 5 == 0:
        result_number.append(item)

print(result_number)