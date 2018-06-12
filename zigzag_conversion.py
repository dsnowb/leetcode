class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        zz = ['' for _ in range(numRows)]
        descent = True
        y = 0
        for c in s:
            zz[y] += c
            if descent:
                y += 1
                if y == numRows - 1:
                    descent = False
            else:
                y -= 1
                if not y:
                    descent = True

        return ''.join(zz)
