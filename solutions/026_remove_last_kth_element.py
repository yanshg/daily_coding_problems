#!/usr/bin/python

"""
This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.

"""
#!/usr/bin/python

class Node():
    def __init__(self, val):
        self.val=val
        self.next=None

    def __repr__(self):
        return "{}=>{}".format(self.val,self.next)

class List():
    def __init__(self):
        self.head=None
        self.tail=None

    def __str__(self):
        return str(self.head)

    # append and delete need take care head and tail pointer
    def append(self,val):
        newnode=Node(val)
        if self.tail:
            self.tail.next=newnode
        self.tail=newnode

        if not self.head:
            self.head=newnode

    def reverse(self):
        prev=None
        cur=self.head
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp

        self.tail=self.head
        self.head=prev

    def _reverse_recursive(self,cur):
        # no elements
        if cur == None:
           return (None,None)

        # if 1 elements
        if cur.next == None:
           return (cur,cur)

        head,tail=self._reverse_recursive(cur.next)
        tail.next=cur
        tail=cur
        tail.next=None
        return (head,tail)

    def reverse_recursive(self):
        self.head,self.tail=self._reverse_recursive(self.head)

    def del_nth(self,n):
        prev=None
        cur=self.head

        i=0
        while cur and i<n:
            prev=cur
            cur=cur.next
            i+=1

        # n > len(list)
        if cur==None:
            return

        # remove the only 1 element
        if prev==None:
            self.head=None
            self.tail=None
            return

        prev.next=cur.next

        if prev.next==None:
            self.tail=prev

    def get_last_nth(self,n):
        fast=self.head
        i=0
        while fast and i<n:
            fast=fast.next
            i+=1

        # if n>len(list)
        if i<n:
            return None

        slow=self.head
        while fast:
            slow=slow.next
            fast=fast.next

        return slow.val

arr=[1,2,3,4,5,6,7,8,9,10]
li=List()
for num in arr:
    li.append(num)

assert li.get_last_nth(1)==10
assert li.get_last_nth(2)==9
