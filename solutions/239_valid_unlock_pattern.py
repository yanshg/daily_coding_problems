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

# Idea:  DFS
#
# source_key: [ (target_key, jump_key) ]
# jump_key is '', means the target_key is directly connected from source_key

matrix={
    '1': [('2',''),('4',''),('5',''),('3','2'),('7','4'),('9','5')],
    '3': [('2',''),('5',''),('6',''),('1','2'),('7','5'),('9','6')],
    '7': [('4',''),('5',''),('8',''),('1','4'),('3','5'),('9','8')],
    '9': [('6',''),('5',''),('8',''),('3','6'),('7','8'),('1','5')],
    '2': [('1',''),('3',''),('4',''),('5',''),('6',''),('8','5')],
    '4': [('1',''),('2',''),('5',''),('7',''),('8',''),('6','5')],
    '6': [('2',''),('3',''),('5',''),('8',''),('9',''),('4','5')],
    '8': [('4',''),('5',''),('6',''),('7',''),('9',''),('2','5')],
    '5': [('1',''),('2',''),('3',''),('4',''),('6',''),('7',''),('8',''),('9','')],
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
            (not jump or jump in visited):
            ways+=get_valid_pattern_nums(matrix,n,target,length+1,path+[target],visited.copy())
    return ways

def get_total_valid_pattern_nums(matrix,n):
    # 1, 3, 7, 9 are symmetric so multiplying by 4
    # 2, 4, 6, 8 are symmetric so multiplying by 4
    return 4 * get_valid_pattern_nums(matrix,n,'1',1,['1'],set()) + \
           4 * get_valid_pattern_nums(matrix,n,'2',1,['2'],set()) + \
           get_valid_pattern_nums(matrix,n,'5',1,['5'],set())

assert get_total_valid_pattern_nums(matrix,1)==9
assert get_total_valid_pattern_nums(matrix,2)==40
assert get_total_valid_pattern_nums(matrix,3)==176
assert get_total_valid_pattern_nums(matrix,4)==648
assert get_total_valid_pattern_nums(matrix,5)==2040
