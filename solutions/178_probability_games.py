#!/usr/bin/python

"""
This problem was asked by Two Sigma.

Alice wants to join her school's Probability Student Club. Membership dues are computed via one of two simple probabilistic games.

The first game: roll a die repeatedly. Stop rolling once you get a five followed by a six. Your number of rolls is the amount you pay, in dollars.

The second game: same, except that the stopping condition is a five followed by a five.

Which of the two games should Alice elect to play? Does it even matter? Write a program to simulate the two games and calculate their expected value.

"""

# Idea:  Should choose first game which end with five followed by a six.

# With single roll:
#
# Both games are identical until Alice rolls a 5.
# At that point, on the next roll, she has a 1/6 chance of rolling a 5, and a 1/6 chance of rolling a 6.
# So her chances of winning at this point are identical between both games.

# The problem is how many rolls need be done and finally win in the long run after multiple start-overs
#
# So the problem become the probability to start over after rolling first 5.

# After rolling the first 5,
# A player of the first game has a 1/6 chance of winning(6), a 1/6 chance of trying again(5), and a 4/6 chance of starting over(1-4).
# A player of the second game has a 1/6 chance of winning(5) and a 5/6 chance of having to start over(1-4, 6).

# So the first game will take fewer rolls to win, on average.

import random

def game(exit1,exit2):
    prev,sum=0,0
    while True:
        curr=random.randint(1,6)
        sum+=1
        if prev==exit1 and curr==exit2:
            return sum
        prev=curr

num_experiments=10000


# First game: average 36

print("\n===== Game with 5/6 to end ======")
sum=0
for i in range(num_experiments):
    rolls=game(5,6)
    sum+=rolls
average1=sum//num_experiments
print("average rolls for first game: ",average1)


# Second game: average 41

print("\n===== Game with 5/5 to end ======")
sum=0
for i in range(num_experiments):
    rolls=game(5,5)
    sum+=rolls
average2=sum//num_experiments
print("average rolls for second game: ",average2)

assert average1<average2



