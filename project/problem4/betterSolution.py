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

def is_divisible(num):
    for i in range(100, 999+1):
        if ((num % i) == 0):
            if ((num / i) >= 100) and ((num / i) <= 999):
                return True
            else:
                # both numbers need to be triple digits
                pass
        else:
            # numbers dont divide evenly
            pass
    return False

def get_first_half_of_number(num):
    num_to_str = str(num)
    if len(num_to_str) % 2 == 0:
        middle_index = len(num_to_str)//2
        return int(num_to_str[:middle_index])
    else:
        # TODO: need a solution for odd length strings
        first_half = int(num_to_str[:len(num_to_str)//2])
        middle_bit = int(num_to_str[len(num_to_str)//2+1])
        print('first_half: ', first_half)
        print('middle_bit: ', middle_bit)
        return 0

max_product_of_two_3_digit = 999 * 999
max_palindrome = 0
first_half = get_first_half_of_number(max_product_of_two_3_digit)
while( True ):
    first_half -= 1
    combined_str = str(first_half) + reverse_str(str(first_half))
    combined_int = int(combined_str)
    if combined_int > max_product_of_two_3_digit:
        continue
    if is_divisible( combined_int ):
        max_palindrome = combined_int
        break

print('max_palindrome: ', max_palindrome)
