class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p, q = l1, l2
        result_head = ListNode(0)
        result = result_head
        val1 = val2 = ''
        while p:
            val1 += str(p.val)
            p = p.next
        while q:
            val2 += str(q.val)
            q = q.next

        sum_vals = str(int(val1[::-1]) + int(val2[::-1]))[::-1]

        for i in sum_vals:
            newNode = ListNode(i)
            result.next = newNode
            result = result.next

        return result_head.next
