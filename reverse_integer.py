class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = False
        if x < 0:
            x = -x
            neg = True
        res = int(''.join(reversed(str(x))))
        if neg:
            res = -res
        max_res = 2**31
        return res if res < max_res and res > -max_res else 0
