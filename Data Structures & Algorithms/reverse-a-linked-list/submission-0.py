# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #  0    ->     1       ->        2       ->     3
        #head

       # we need it to become null at the end

        prev=None
        curr=head

        while curr:
            temp=curr.next #temp= to hold spot in pointer
            curr.next=prev #setting next pointer to previous
            prev=curr #moving prev pointer forward
            curr=temp

        return prev








