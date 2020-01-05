#!/usr/bin/python

"""
This problem was asked Microsoft.

Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

For example, given a file with the content "Hello world", three read7() returns "Hello w", "orld" and then "".
"""

class FileProxy():
    def __init__(self,contents):
        self.contents=contents
        self.offset=0
        self.buffer=""

    def read_7(self):
        start=self.offset
        end=min(start+7, len(self.contents))
        self.offset=end
        return self.contents[start:end]

    def read_n(self,n):
        while len(self.buffer) < n:
            chars=self.read_7()
            if not chars:
                break
            self.buffer+=chars
        n_chars=self.buffer[:n]
        self.buffer=self.buffer[n:]
        return n_chars.strip()


fp=FileProxy("Hello World")
assert fp.read_7() == "Hello W"
assert fp.read_7() == "orld"
assert fp.read_7() == ""

fp=FileProxy("Hello World")
assert fp.read_n(8) == "Hello Wo"
assert fp.read_n(8) == "rld"
assert fp.read_n(8) == ""

fp=FileProxy("Hello World")
assert fp.read_n(4) == "Hell"
assert fp.read_n(4) == "o Wo"
assert fp.read_n(4) == "rld"
