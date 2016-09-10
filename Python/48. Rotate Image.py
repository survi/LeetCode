class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix) - 1
        for i in range(l/2+1):
            for j in range(i,len(matrix[i]) -i - 1,1):
                matrix[i][j], matrix[j][l-i], matrix[l-i][l-j], matrix[l-j][i] = matrix[l-j][i], matrix[i][j], matrix[j][l-i], matrix[l-i][l-j]
