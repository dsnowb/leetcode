class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        prev = cur = runner = head
        for _ in range(n - 1):
            runner = runner.next
        
        while runner.next:
            runner = runner.next
            prev = cur
            cur = cur.next
        
        prev.next = cur.next
        
        if cur == head:
            return head.next
        
        return head