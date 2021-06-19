#!/usr/bin/python

"""

This problem was asked by Google.

The game of Nim is played as follows. Starting with three heaps, each containing a variable number of items, two players take turns removing one or more items from a single pile. The player who eventually is forced to take the last stone loses. For example, if the initial heap sizes are 3, 4, and 5, a game could be played as shown below:

  A  |  B  |  C
-----------------
  3  |  4  |  5
  3  |  1  |  3
  3  |  1  |  3
  0  |  1  |  3
  0  |  1  |  0
  0  |  0  |  0

In other words, to start, the first player takes three items from pile B. The second player responds by removing two stones from pile C. The game continues in this way until player one takes last stone and loses.

Given a list of non-zero starting values [a, b, c], and assuming optimal play, determine whether the first player has a forced win.

"""

### code for week 1, 3-heap Nim with computer player ###

### game is for player vs. player, but the computer
### tells you the optimal strategy to use on your turn
import copy

def main():
    print "Enter an integer for each pile size or else the program will crash!"
    pile1 = int(raw_input("Enter the size of nim-heap 1: "))
    pile2 = int(raw_input("Enter the size of nim-heap 2: "))
    pile3 = int(raw_input("Enter the size of nim-heap 3: "))

    dict = {'A':pile1,'B': pile2,'C':pile3}

    while sum(dict.values()) > 0:
        nimsum = dict['A']^dict['B']^dict['C']
        print "A   B   C"
        print str(dict['A'])+'   '+ str(dict['B'])+'   '+str(dict['C'])
        print "The nim sum of the heaps is currently %s (%s) \n" % (nimsum, str(int2bin(nimsum)).lstrip('0') )
        print "The winning strategy is:\n"
        print strategy(dict)
        valid = False
        while(valid==False):
            takepile = raw_input("Player 1, enter which pile you are taking from ")
            if takepile == 'A' or takepile=='B' or takepile=='C':
                valid = True

        valid = False
        while(valid ==False):
            takenum = raw_input("Player 1, enter how many stones to take from pile %s " % takepile)
            if takenum.isalnum() and not(takenum.isalpha()):
                if int(takenum)<= dict[takepile]:
                       valid = True

        dict[takepile]= dict[takepile]-int(takenum)
        nimsum = dict['A']^dict['B']^dict['C']
        if sum(dict.values()) == 0:
            print 'Congratulations, player 1 wins!'
            break

        print "A   B   C"
        print str(dict['A'])+'   '+ str(dict['B'])+'   '+str(dict['C'])
        print "The nim sum of the heaps is currently %s (%s) \n" % (nimsum, str(int2bin(nimsum)).lstrip('0') )
        print "The winning strategy is:\n"
        print strategy(dict)
        valid = False
        while(valid==False):
            takepile = raw_input("Player 2, enter which pile you are taking from ")
            if takepile == 'A' or takepile=='B' or takepile=='C':
                valid = True

        valid = False
        while(valid ==False):
            takenum = raw_input("Player 2, enter how many stones to take from pile %s "% takepile)
            if takenum.isalnum() and not(takenum.isalpha()):
                if int(takenum) <= dict[takepile]:
                       valid = True
        dict[takepile]= dict[takepile]-int(takenum)
        nimsum = dict['A']^dict['B']^dict['C']
        if sum(dict.values()) == 0:
            print 'Congratulations, player 1 wins!'
            break



def int2bin(n, count=24):
    return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])

### the strategy function takes a dictionary of key(heap name): value(size of heap)
### example dictionary would be {'A':6,'B':9,'C':10}
### notation follows that of the proof in the lecture notes
def strategy(dict):
    ndict = copy.deepcopy(dict) # copy the dictionary
    nimsum = 0
    for item in ndict.values():
        nimsum = nimsum ^ item # nimsum is the xor of all the heap sizes
    # if the nimsum is 0, there is no hope
    if nimsum ==0: return 'The nimsum is already 0. You have no winning strategy unless your opponent makes a mistake'
    # else, there must be a winning strategy!
    else:
        nimsumb = int2bin(nimsum) # will use nimsumb for nimsum in binary
        nimsumb_str = str(nimsumb).lstrip('0') # the string strips off all the leading 0s
        mostsig = len(nimsumb_str) # most significant power of 2, from the proof in the lecture notes, there must be some
                                # pile that has at least 2**(mostsig-1) stones, and this is the pile we'll take from
        highest = 2**(mostsig-1)
        xk = ''
        takeaway = -1 # we don't want to return a negative value of coins to take away (we can't add coins)
        while takeaway <1:
            for item in ndict.keys():
                if ndict[item] >= highest:
                    xk = item # find the pile with at least 2**(mostsig-1) stones
            ### start with pile xk
            ### want to make yk = nimsum +* xk
            yk = nimsum ^ int(ndict[xk]) # take away the appropriate number of stones
            takeaway = ndict[xk]-yk
            del ndict[xk]
        return "Take %s away from pile %s " %(takeaway, xk) # return the winning strategy

main()
