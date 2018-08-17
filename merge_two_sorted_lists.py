class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not (l1 or l2):
            return l1
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val < l2.val:
            cur, opp = l1, l2
        else:
            cur, opp = l2, l1
        head = cur
        
        while cur.next and opp:
            if cur.next.val > opp.val:
                cur.next, opp = opp, cur.next
            cur = cur.next
        
        if opp:
            cur.next = opp
            
        return head
