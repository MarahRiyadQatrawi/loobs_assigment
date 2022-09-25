num = 76542
num = str(num)

reversed_num ="".join(reversed(num))

print(reversed_num)


num = 76542
reversed_num = 0
while num > 0:
    the_last_number = num % 10
    reversed_num = reversed_num * 10
    reversed_num  += the_last_number
    num = num / 10
    num = num.__floor__()

print(reversed_num)

