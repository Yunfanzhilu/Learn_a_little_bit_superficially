class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        a=91
        n=len(matrix[0])
        for i in range(n):
            for j in range(n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for k in range(n):
            matrix[k].reverse()
