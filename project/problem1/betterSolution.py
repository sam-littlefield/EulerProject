# Limiting numbers we loop through by multiples of 5 and 3
max3 = 999//3
max5 = 999//5

total = 0
for i in range(1, max3+1):
    total += i*3
for j in range(1, max5+1):
    if (j % 3) == 0:
        pass
    else:
        total += j*5
print('Total: ', total)
