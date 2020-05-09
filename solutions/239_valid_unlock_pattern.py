#!/usr/bin/python

"""

This problem was asked by Uber.

One way to unlock an Android phone is through a pattern of swipes across a 1-9 keypad.

For a pattern to be valid, it must satisfy the following:

    All of its keys must be distinct.
    It must not connect two keys by jumping over a third key, unless that key has already been used.

For example, 4 - 2 - 1 - 7 is a valid pattern, whereas 2 - 1 - 7 is not.

Find the total number of valid unlock patterns of length N, where 1 <= N <= 9.

"""

# DFS

matrix={
    # source_key: [ (target_key, jumped_key)]
    '1': [('2','0'),('4','0'),('5','0'),('3','2'),('7','4'),('9','5')],
    '3': [('2','0'),('5','0'),('6','0'),('1','2'),('7','5'),('9','6')],
    '7': [('4','0'),('5','0'),('8','0'),('1','4'),('3','5'),('9','8')],
    '9': [('6','0'),('5','0'),('8','0'),('3','6'),('7','8'),('1','5')],
    '2': [('1','0'),('3','0'),('4','0'),('5','0'),('6','0'),('8','5')],
    '4': [('1','0'),('2','0'),('5','0'),('7','0'),('8','0'),('6','5')],
    '6': [('2','0'),('3','0'),('5','0'),('8','0'),('9','0'),('4','5')],
    '8': [('4','0'),('5','0'),('6','0'),('7','0'),('9','0'),('2','5')],
    '5': [('1','0'),('2','0'),('3','0'),('4','0'),('6','0'),('7','0'),('8','0'),('9','0')],
}

# DFS
def get_valid_pattern_nums(matrix,n,start,length,path,visited):
    if length==n:
        print("path:", path)
        return 1
    elif length>n:
        return 0

    visited.add(start)

    ways=0
    for target,jump in matrix[start]:
        if target not in visited and \
            (jump=='0' or jump in visited):
            ways+=get_valid_pattern_nums(matrix,n,target,length+1,path+[target],visited.copy())
    return ways

def get_total_valid_pattern_nums(matrix,n):
    return 4 * get_valid_pattern_nums(matrix,n,'1',1,['1'],set()) + \
           4 * get_valid_pattern_nums(matrix,n,'2',1,['2'],set()) + \
           get_valid_pattern_nums(matrix,n,'5',1,['5'],set())

assert get_total_valid_pattern_nums(matrix,1)==9
assert get_total_valid_pattern_nums(matrix,3)==176
assert get_total_valid_pattern_nums(matrix,4)==648
assert get_total_valid_pattern_nums(matrix,5)==2040
