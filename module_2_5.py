def get_matrix (n,m, value):
    matrix = []
    for i in range (n):
        str = []
        matrix.append(str)
        for j in range (m):
            str.append(value)
    return matrix
result1 = get_matrix(3, 3, 15)
result2 = get_matrix(4,5,42)
result3 = get_matrix(5, 2, 18)
print(result1)
print(result2)
print(result3)
