def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    minm = 0
    maxm = len(matrix[0]) - 1

    while minm < maxm:
        for i, j in zip(range(minm, maxm), range(0, maxm - minm)):
            # Get values
            el1 = matrix[minm][i]
            el2 = matrix[i][maxm]
            el3 = matrix[maxm][maxm - j]
            el4 = matrix[maxm - j][minm]

            # Rotate values
            matrix[i][maxm] = el1
            matrix[maxm][maxm - j] = el2
            matrix[maxm - j][minm] = el3
            matrix[minm][i] = el4

        minm += 1
        maxm -= 1
