# https://leetcode.com/problems/two-sum/submissions/
# 01/23/2021

def two_sum(array, target):
    first_element = 0
    for element in array:
        i = first_element + 1
        while i < len(array):
            if (element + array[i] == target):
                return [first_element, i]
            i += 1
        first_element += 1



array = [2, 15, 11, 7]
target = 9

print(two_sum(array, target))
