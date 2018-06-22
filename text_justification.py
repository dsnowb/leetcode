def fullJustify(words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    output = []
    avail_chars = maxWidth
    spaces = []

    def get_newline():
        nonlocal output, avail_chars, spaces
        output.append('')
        avail_chars = maxWidth
        spaces = []

    def justify_line(line):
        nonlocal output
        line = line.strip()
        flag = False
        if not len(spaces) and len(line) < maxWidth:
            line += ' ' * (maxWidth - len(line))
        else:
            if len(line) < maxWidth:
                while not flag:
                    for i, space in enumerate(spaces):
                        line = line[:space + i] + ' ' + line[space + i:]
                        spaces[i] = space + i

                        if len(line) == maxWidth:
                            flag = True
                            break
        output[-1] = line

    if not len(words):
        return []

    get_newline()
    for word in words:
        if len(word) > avail_chars:
            spaces = spaces[:-1]
            justify_line(output[-1])
            get_newline()

        output[-1] += '{} '.format(word)
        avail_chars -= len(word) + 1
        spaces.append(len(output[-1]) - 1)
    
    output[-1] += ' ' * (maxWidth - len(output[-1]))
    if len(output[-1]) > maxWidth:
        output[-1] = output[-1][:maxWidth]
        
    return output
