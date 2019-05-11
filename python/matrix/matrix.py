class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = self.createMatrix(matrix_string.split("\n"))

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return list(map(lambda x: x[index - 1], self.matrix))
    
    def createMatrix(self, matrix_string_split):
        buildingMatrix = []
        for row in matrix_string_split:
            splitRow = row.split(" ")
            buildingMatrix.append(list(map(lambda x: int(x), splitRow)))
        return buildingMatrix
