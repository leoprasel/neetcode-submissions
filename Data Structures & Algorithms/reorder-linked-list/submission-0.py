# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #find middle of linked list
        def findMiddle(head):
            slow, fast = head, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def reverseList(head):
            prev = None
            curr = head
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev


        middle = findMiddle(head)
        second_list = middle.next
        middle.next = None
        reversed_list = reverseList(second_list)
        
        first, second = head, reversed_list
        
        while second:
            next_first = first.next
            next_second = second.next
            first.next = second
            second.next = next_first
            first = next_first
            second = next_second


