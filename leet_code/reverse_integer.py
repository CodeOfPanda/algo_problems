# https://leetcode.com/problems/reverse-integer/submissions/
# 01/23/2021

#  -2,147,483,648 to +2,147,483,647 is the range for a signed 32-bit integer

# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.


def reverse_int(value):  
    # taking the absolute value now so that we can reverse it without having to worry about it's negative sign
    string_val = str(abs(value))  # changing value in to a string to be iterable
    reverse_string = string_val[::-1]  # this reverses by slicing the string
    
    int_value = int(reverse_string)
    # I started by checking the range of 32-bit integer at the begining but moved it
    # to check the reversal of the int value incase the reversal is out of range.
    if int_value > (2**31 - 1) or int_value < -2**31:
        return 0
    
    if value < 0:
        # this is where we add back in the negative if it had it.
        # rather than trying to slice the string and keep the negation it is much easier to add it back after the reversal.
        return int_value * -1  
    else:
        return int_value
    
    
    
        

value = 1534236469
print(reverse_int(value))

