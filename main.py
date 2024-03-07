' forbiddenfruitをインストールすること
' pip install forbiddenfruit

from forbiddenfruit import curse

' matmulを実装するためのMatrixクラス定義(__getitem__とかも適宜実装する)
class Matrix(list):
    def __init__(self, values): self.__values = values
    def __matmul__(self, other): return Matrix(Matrix.multiply(self.__values, other.__values))
    def __imatmul__(self, other): return self.__matmul__(other)
    def __rmatmul__(self, other): return Matrix(Matrix.multiply(self.__values, other.__values))
    def __repr__(self): return f'<Matrix values="{self.__values}">'
    def __getitem__ (self, index): return self.__values[index]
    def __setitem__ (self, index, value): self.__values[index] = value
    @staticmethod
    def multiply(mat1, mat2): return [[sum(mat1 * mat2 for mat1, mat2 in zip(mat1_row, mat2_col)) for mat2_col in zip(*mat2)] for mat1_row in mat1]

' 標準オブジェクトに__matmul__を追加する
curse(list, '__matmul__', lambda self, other: Matrix(self) @ Matrix(other))

a = [[1, 2, 3], [4, 5, 6],]
b = [[7, 8], [9, 10], [11, 12]]

c = a @ b
print(c[0])
' > [58, 64]
