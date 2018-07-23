class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        # Dict not implemented
        # ltrs = {k:v for k, v in zip(''.split('abcdefghijklmnopqrstuvwxyz'), widths)}
        
        max_len = 100
        num_lines = 1
        line_length = 0
        
        for char in S:
            char_width = widths[ord(char) - 97]
            if line_length + char_width > max_len:
                num_lines += 1
                line_length = char_width
            else:
                line_length += char_width
        
        return [num_lines, line_length]
