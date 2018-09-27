class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        combos = set()
        
        def recurse(c, sub='', opens=0):
            nonlocal combos
            if c == 0:
                combos.add(sub)
                return
            
            if c > opens:
                recurse(c - 1, sub + '(', opens + 1)
            
            if opens:
                recurse(c - 1, sub + ')', opens - 1)    
        
        recurse(n * 2)
        
        return list(combos)