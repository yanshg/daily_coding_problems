#!/usr/bin/python

"""
This problem was asked by Two Sigma.

Alice wants to join her school's Probability Student Club. Membership dues are computed via one of two simple probabilistic games.

The first game: roll a die repeatedly. Stop rolling once you get a five followed by a six. Your number of rolls is the amount you pay, in dollars.

The second game: same, except that the stopping condition is a five followed by a five.

Which of the two games should Alice elect to play? Does it even matter? Write a program to simulate the two games and calculate their expected value.

"""

# Idea:  Should choose first game

# Both games are identical until Alice rolls a 5. At that point, on the next roll, she has a 1/6 chance of rolling a 5, and a 1/6 chance of rolling a 6.
# So her chances of winning at this point are identical between both games.

# But what makes this interesting is what happens if she does not win immediately after rolling her first 5.

# In the second game, suppose Alice rolls a 5 and then a non-5. She's now back to square one, having to roll a 5 again before looking for her second 5. She will require a minimum of two more rolls to win.
# In contrast, in the first game, it's possible for Alice to roll a 5 followed by a non-6, which could be a 5. In the second game, failure to win doesn't necessarily revert the player to square one - there's a possibility she could still be just one roll away from winning.

# After rolling the first 5,
# A player of the first game has a 1/6 chance of winning, a 1/6 chance of trying again, and a 4/6 chance of starting over.
# A player of the second game has a 1/6 chance of winning and a 5/6 chance of having to start over.

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

print("\n===== 5, 6 ======")
sum=0
for i in range(num_experiments):
    rolls=game(5,6)
    sum+=rolls
average1=sum//num_experiments
print("average rolls for first game: ",average1)


# Second game: average 41

print("\n===== 5, 5 ======")
sum=0
for i in range(num_experiments):
    rolls=game(5,5)
    sum+=rolls
average2=sum//num_experiments
print("average rolls for second game: ",average2)

assert average1<average2



