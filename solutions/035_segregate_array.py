#!/usr/bin/python

"""
This problem was asked by Google.

Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""

# Idea:  for each character:
#            get first left position which is not the letter searching from start to end
#            get first right position which is the letter searching from end to start
#            swap the characters

# Get left position searching from start to end that the char is NOT the 'letter'
def get_next_left_swap_pos(arr,start,end,letter):
    while start<=end and arr[start]==letter:
        start+=1
    return start

# Get first right position searching from end to start that the char is the 'letter'
def get_next_right_swap_pos(arr,start,end,letter):
    while end>=start and arr[end]!=letter:
        end-=1
    return end

def segregate_array_for_letter(arr,start,end,letter):
    while True:
        start=get_next_left_swap_pos(arr,start,end,letter)
        end=get_next_right_swap_pos(arr,start,end,letter)
        if start<end:
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1
        else:
            break

    return start

def segregate_array(arr):
    print("arr:", arr)
    n=len(arr)-1
    pos=segregate_array_for_letter(arr,0,n,'R')
    pos=segregate_array_for_letter(arr,pos,n,'G')
    print("arr:", arr)
    return arr

assert segregate_array(['G', 'B', 'R', 'R', 'B', 'R', 'G']) == ['R', 'R', 'R', 'G', 'G', 'B', 'B']
