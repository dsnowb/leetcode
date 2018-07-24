class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = list('aeiouAEIOU')
        
        # build words
        words = []
        wd = ''
        for char in S:
            if char == ' ':
                words.append(wd)
                wd = ''
            else:
                wd += char
        words.append(wd)
    
        out = ''
        for i, word in enumerate(words):
            if word[0] not in vowels:
                out += word[1:] + word[0]
            else:
                out += word
            out += 'ma' + 'a' * (i + 1) + ' '
        
        return out[:-1]
