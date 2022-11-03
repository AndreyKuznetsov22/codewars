# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        r1=ListNode(0)
        r2=ListNode(0)
        r=r2
        t=r1
        count=0
        while head:
            if count%2!=0:
                r1.next=ListNode(head.val)
                r1=r1.next
            else:
                r2.next=ListNode(head.val)
                r2=r2.next
            count+=1
            head=head.next
        r2.next=t.next
        return r.next