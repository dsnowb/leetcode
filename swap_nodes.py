class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l = head
        try:
            r = head.next
        except AttributeError:
            return head
        head = r
        
        try:
            l.next = r.next
        except AttributeError:
            return l
        
        r.next = l
        
        while l and l.next and l.next.next:
            pre = l
            l = l.next
            r = l.next
            pre.next = r
            l.next = r.next
            r.next = l
            
        return head
