# https://leetcode.com/problems/palindrome-number/submissions/
# 01/26/2021


# given an int x
#   if x == palindrome 
#       return true

# an int is a palindrome when it reads the same backward as forward.
#   121 == 121 is a palindrome -121 != 121- not a palindrome.


def is_palindrome(x):
    
    string_x = str(abs(x))
    reverse_x = string_x[::-1]
    
    if x < 0: return False
    
    if string_x == reverse_x: 
        return True

    return False
