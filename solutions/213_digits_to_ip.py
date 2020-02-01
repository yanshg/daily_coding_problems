#!/usr/bin/python

"""

This problem was asked by Snapchat.

Given a string of digits, generate all possible valid IP address combinations.

IP addresses must follow the format A.B.C.D, where A, B, C, and D are numbers between 0 and 255. Zero-prefixed numbers, such as 01 and 065, are not allowed, except for 0 itself.

For example, given "2542540123", you should return ['254.25.40.123', '254.254.0.123'].

"""

def is_valid_ip_field(s):
    if s[0]=='0' and len(s)>=2:
        return False
    if 0<=int(s)<=255:
        return True
    return False

def helper(string,fields=[],all_ips=set()):
    lfs=len(fields)
    if not string:
        if lfs==4:
            all_ips.add('.'.join(fields))
    elif lfs<4:
        field_len=min(3,len(string))+1
        for l in range(1,field_len):
            field_str=string[:l]
            if is_valid_ip_field(field_str):
                helper(string[l:],fields+[field_str],all_ips)

def get_valid_ips(string):
    if len(string)>12:
        return None

    if not string.isdigit():
        return None

    all_ips=set()
    helper(string,[],all_ips)
    return all_ips

assert not get_valid_ips('2542540123a')
assert not get_valid_ips('2542540123342')
assert not get_valid_ips('254254012334')
assert not get_valid_ips('2562540123')
assert get_valid_ips('2542540123')=={'254.25.40.123', '254.254.0.123'}
assert get_valid_ips('255255255255')=={'255.255.255.255'}
assert get_valid_ips("100100110") == {'100.10.0.110', '10.0.100.110', '100.100.11.0', '100.100.1.10'}
