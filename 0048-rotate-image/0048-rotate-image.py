class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        row  = len(matrix)
        col = len(matrix[0])
        trans = []

        for i in range(row):
            r = []
            for j in range(col):
                r.append(matrix[j][i])
            r.reverse()
            trans.append(r)
        matrix[:] = trans
