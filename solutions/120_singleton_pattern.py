#!/usr/bin/python

"""
This problem was asked by Microsoft.

Implement the singleton pattern with a twist. First, instead of storing one instance, store two instances. And in every even call of getInstance(), return the first instance and in every odd call of getInstance(), return the second instance.
"""

class Singleton:
    instances=dict()
    even_instance=False

    def __init__(self,instance_num):
        self.instance_num=instance_num

    @staticmethod
    def initialize():
        Singleton.instances[0]=Singleton(0)
        Singleton.instances[1]=Singleton(1)

    @staticmethod
    def get_instance():
        if not Singleton.instances:
           Singleton.initialize()

        Singleton.even_instance=not Singleton.even_instance
        return Singleton.instances[int(Singleton.even_instance)]

Singleton.initialize()

i1=Singleton.get_instance()
assert i1.instance_num==1

i2=Singleton.get_instance()
assert i2.instance_num==0

i3=Singleton.get_instance()
assert i3.instance_num==1

i4=Singleton.get_instance()
assert i4.instance_num==0

            
