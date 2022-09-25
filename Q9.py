tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
tuple1 = list(tuple1)
flatList = []

for i in tuple1:
    for k in i:
        flatList.append(k)

print(flatList)
print(flatList[7])






