#!/usr/bin/python

"""

This problem was asked by Dropbox.

What does the below code snippet print out? How can we fix the anonymous functions to behave as we'd expect?

functions = []
for i in range(10):
    functions.append(lambda : i)

for f in functions:
    print(f())

Upgrade to premium and get in-depth solutions to every problem, including this one. Since you were referred by one of our affiliates, you'll get a 10% discount on checkout!

If you liked this problem, feel free to forward it along so they can subscribe here! As always, shoot us an email if there's anything we can help with!

"""

# This is a issue about Python closures and later binding.
# http://quickinsights.io/python/python-closures-and-late-binding/
#
# Python closures are late binding. that means:
# The values of variables used in closures are looked up at the time the inner function is called.

# Idea:  re-set 'i' at the time when call the virtual methods due to later binding

functions = []
for i in range(10):
    functions.append(lambda : i)

i=0
for f in functions:
    print(f())
    i+=1


# Another Idea:  use local varible in the virtual method

functions = []
for i in range(10):
    functions.append(lambda x=i: x)

for f in functions:
    print(f())


# Another Example for later binding:

def multipliers():
    return [lambda x : i*x for i in range(4)]

print([m(2) for m in multipliers()]) # [6, 6, 6, 6]

# Solution

def multipliers():
  return [lambda x, i=i : i * x for i in range(4)]

print([m(2) for m in multipliers()]) # [0, 2, 4, 6]
