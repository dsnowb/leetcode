class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        i = 0
        while i < len(str) and str[i] == ' ':
            i += 1

        num_str = ''
        if i < len(str) and (str[i] == '-' or str[i] == '+'):
            num_str += str[i]
            i += 1

        while True:
            if i < len(str) and str[i].isnumeric():
                num_str += str[i]
                i += 1
                continue
            break

        try:
            num = int(num_str)
        except:
            return 0

        max_num = 2**31 - 1
        return (num if num < max_num and num >= -max_num else
                max_num if num >= -max_num else
                -max_num - 1)
