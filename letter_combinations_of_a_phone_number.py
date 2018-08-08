class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not len(digits):
            return []
        
        ltrs = 'abc def ghi jkl mno pqrs tuv wxyz'.split(' ')
        out = []
        def recurse(idx, combo):
            nonlocal ltrs, out
            if idx == len(digits):
                out.append(combo)
                return
            for ltr in ltrs[int(digits[idx]) - 2]:
                new_combo = combo + ltr
                recurse(idx + 1, new_combo)
        
        recurse(0, '')
        return out
