#!/usr/bin/python

"""

This problem was asked by Microsoft.

Given a clock time in hh:mm format, determine, to the nearest degree, the angle between the hour and the minute hands.

Bonus: When, during the course of a day, will the angle be zero?

"""

def get_angle(h,m):
    # 1h = 30 degree (360/12)
    # 1m = 6 degree (360/60)
    # angle_h=h*30 + m*(30/60) = h*30 + m*0.5
    # angle_m=m*6
    angle_h=h*30+m*0.5
    angle_m=m*6
    angle=abs(angle_m - angle_h)
    if angle>180:
        angle=360-angle
    return angle

