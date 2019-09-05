
def isPrime(test_prime):
    num = 3
    while True:
        num += 2
        if num > (test_prime / num):
            break
        if (test_prime % num) == 0:
            return False
    return True

test_prime_factor = 600851475143
max_factor = 0

num = 3
while True:
    num += 2
    if num > (test_prime_factor / num):
        break
    if ((num % 3) == 0):
        continue
    if isPrime(num):
        if test_prime_factor % num == 0:
            max_factor = num
            print (max_factor)

print ('best: ', max_factor)
