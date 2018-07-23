def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    def recurse(m):
        pset = set()
        if m:
            for pstring in recurse(m - 1):

                pset.add('()' + pstring)
                pset.add(pstring + '()')
                pset.add(({}).format(pstring))

        return pset
        
    recurse(n)
