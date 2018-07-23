class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        lst = list(bin(N))[2:]
        
        # Find left 1
        maxcount = 0
        for i in range(len(lst)):
            if lst[i] == '1':
                j = i
                for j in range(i + 1, len(lst)):
                    if lst[j] == '1':
                        diff = j - i
                        if diff > maxcount:
                            maxcount = diff
                        i = j
                        break
        
        return maxcount
