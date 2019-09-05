def reverse_str(str):
    reversed_str = ''
    for char in str:
        reversed_str = char + reversed_str
    return reversed_str

def is_palindrome(num):
    num_as_string = str(num)
    if num_as_string == reverse_str(num_as_string):
        return True
    return False

max_palindrome = 0
max_i = 0
max_j = 0
for i in range(100,999+1):
    for j in range(100,999+1):
        if is_palindrome(i * j):
            if (i * j) > max_palindrome:
                max_palindrome = i * j
                max_i = i
                max_j = j

print('max_palindrome: ',max_palindrome)
print('max_j : ', max_j)
print('max_i : ',max_j)
