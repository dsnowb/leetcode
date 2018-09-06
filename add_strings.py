def addStrings(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    out = ''
    rem = 0
    if len(num1) < len(num2):
        s, lon = num1, num2
    else:
        s, lon = num2, num1
    s, lon = reversed(s), reversed(lon)

    for c in s:
        place = int(c) + int(next(lon)) + rem
        out += str(place % 10)
        rem = place // 10

    for c in lon:
        place = int(c) + rem
        out += str(place % 10)
        rem = place // 10

    if rem:
        out += str(rem)

    return ''.join(list(reversed(out)))
