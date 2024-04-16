# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Iterative Solution - neetocde

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # set the current node to head to start at the beginning of the linked list
        # previous is None because there is nothing that comes before it
        previous, current = None, head

        while current:
            # save the link to the rest of the list
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous

# Recursive - neetcode YouTube comment
class Solution:
    def reverseList(self, head):
        def reverse(cur, prev):
            if cur is None:
                return prev
            else:
                next = cur.next
                cur.next = prev
                return reverse(next, cur)

        return reverse(head, None)