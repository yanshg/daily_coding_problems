#!/usr/bin/python

"""

This problem was asked by Facebook.

In chess, the Elo rating system is used to calculate player strengths based on game results.

A simplified description of the Elo system is as follows. Every player begins at the same score. For each subsequent game, the loser transfers some points to the winner, where the amount of points transferred depends on how unlikely the win is. For example, a 1200-ranked player should gain much more points for beating a 2000-ranked player than for beating a 1300-ranked player.

Implement this system.

"""

# Idea:  https://www.thechesspiece.com/what_is_an_elo_rating.asp

#        Ra:  Rating of a
#        Sa:  Actual score of a  (1: win,  0: loss,  0.5: draw)
#        Ea:  Expected score of a.  (probability for a to win b)
#
#        Rb:  Rating of b
#        Sb:  Actual score of b  (1: win,  0: loss,  0.5: draw)
#        Eb:  Expected score of b.  (probability for b to win a)
#
#        Ra'=Ra + K * (Sa - Ea)
#        Rb'=Rb + K * (Sb - Eb)
#
#        Ea = 1.0/(1.0+pow(10, (Rb - Ra)/400))
#        Eb = 1.0/(1.0+pow(10, (Ra - Rb)/400))
#
#        K=30
#        Sa + Sb = 1    
#        Ea + Eb = 1
#
import math

def probability(rating1,rating2):
    return 1.0/(1.0+math.pow(10, float(rating2-rating1)/400))

def compute_rating(rating1,rating2,score1):
    k=30
    prob1=probability(rating1,rating2)
    prob2=1-prob1
    score2=1-score1
    return round(rating1+k*(score1-prob1)),round(rating2+k*(score2-prob2))

assert compute_rating(1200,1000,1)==(1207, 993)
assert compute_rating(1200,1000,0)==(1177, 1023)
assert compute_rating(1200,1000,0.5)==(1192, 1008)

assert compute_rating(1200,2000,1)==(1230, 1970)
assert compute_rating(1200,2000,0)==(1200, 2000)
assert compute_rating(1200,2000,0.5)==(1215, 1985)
