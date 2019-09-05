
def sum_squares_min_to_max(min, max):
    sum = 0
    for i in range(min,max+1):
        sum += i * i
    return sum

def square_sum_min_to_max(min, max):
    sum = 0
    for i in range(min,max+1):
        sum += i
    return sum * sum
min= 1
max= 100
print( square_sum_min_to_max(min, max) - sum_squares_min_to_max(min, max) )
