#!/usr/bin/python

"""
This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
"""

# Reservoir Sampling: https://gregable.com/2007/10/reservoir-sampling.html

# Reservoir Sampling where k != 1
#
# 1) Create an array reservoir[0..k-1] and copy first k items of stream[] to it.
# 2) Now one by one consider all items from (k+1)th item to nth item.
# ..a) Generate a random number from 0 to i where i is index of current item in stream[]. Let the generated random number is j.
# ..b) If j is in range 0 to k-1, replace reservoir[j] with arr[i]

# Reservoir Sampling where k = 1
#
# 1) Initialize ‘count’ as 0, ‘count’ is used to store count of numbers seen so far in stream.
# 2) For each number ‘x’ from stream, do following
# ..a) Increment ‘count’ by 1.
# ..b) If count is 1, set result as x, and return result.
# ..c) Generate a random number from 0 to ‘count-1’. Let the generated random number be i.
# ..d) If i is equal to ‘count – 1’, update the result as x.

import random

count_so_far = 0
result=None

def pick_random_element(x):
    global count_so_far,result
    count_so_far += 1

    if count_so_far == 1:
        result = x
    else:
        random_value = random.randrange(count_so_far)
        if random_value == count_so_far - 1:
            result = x

    return result


sample_stream = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for index, element in enumerate(sample_stream):
    random_element = pick_random_element(element)
    print("Random element of the first {} is {}".format(index + 1, random_element))

