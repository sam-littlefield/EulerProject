def divisible_by_11_to_19(num):
    divisible = True
    for i in range(11,19+1):
        if not (num % i == 0):
            return False
    return True

num = 20
while True:
    num += 20
    if divisible_by_1_to_20(num):
        print('num', num)
        break
