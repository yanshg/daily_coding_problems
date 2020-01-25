#!/usr/bin/python

"""
This problem was asked by Microsoft.

Describe and give an example of each of the following types of polymorphism:

    Ad-hoc polymorphism
    Parametric polymorphism
    Subtype polymorphism

"""

* Ad-hoc polymorphism
     * Allow multiple functions that perform an operation on different
     * `add(int, int)` and `add(str, str)` would be separately implemented

* Parametric polymorphism
     * This allows a function to deal with generics, and therefore on any concrete definition of the generic.
     * e.g. A `List` type in Java, regardless of which objects are in the list

* Subtype polymorphism
     * This allows subclass instances to be treated by a function they same way as it would superclass instances
     * e.g. Instances of `Cat` will be operated on a function the same way as instances of it's superclass `Animal`.

