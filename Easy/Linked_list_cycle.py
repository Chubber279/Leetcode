from typing import Optional
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        turtle = head
        rabbit = head
        while rabbit:
            turtle = turtle.next
            rabbit = rabbit.next
            try:
                rabbit = rabbit.next
            except:
                return False
            if rabbit == turtle:
                return True
        return False