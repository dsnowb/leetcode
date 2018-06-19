class Solution:
    def isPalindrome(self, val):
        """
        :type x: int
        :rtype: bool
        """
        if val < 0:
            return False
        if val < 10:
            return True
        lst = []
        while True:
            lst.append(val % 10)
            if val < 10:
                break
            val = val // 10
        l = 0
        r = len(lst) - 1
        while l < r:
            if lst[l] != lst[r]:
                return False
            l += 1
            r -= 1
        return True
