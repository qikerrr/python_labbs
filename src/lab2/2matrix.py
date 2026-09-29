def proverka(mat):
    if len(mat) == 0:
        return mat #если матрица пустая сразу возвращаем пустую матрицу

    raz = len(mat[0]) #сохраняем размер строки для проверки рваной матрицы

    for i in mat:
        if len(i) != raz:
            return "ValueError" #рваная матрица

def transpose(mat):
    res = [] #результат = новая измененная матрица

    if proverka(mat) != "ValueError":
        if len(mat) == 0: #если матрица пустая = выводим пустую матрицу
            return res

        for j in range(len(mat[0])): #проходимся по столбцам
            nrow = [] #новые ряды для составления новой матрицы
            for i in range(len(mat)): #проход по строкам
                nrow.append(mat[i][j]) #составление новой матрицы
            res.append(nrow)
    else: return 'ValueError'
    return res

#print(transpose([[1, 2, 3]]))
#print(transpose([[1], [2], [3]]))
#print(transpose([[1, 2], [3, 4]]))
#print(transpose([]))
#print(transpose([[1, 2], [3]]))


def row_sums(mat):
    res = []

    if proverka(mat) != 'ValueError':
        if len(mat) != len(mat[0]): #проверка на прямоугольную матрицу

            for j in range(len(mat)): #проход по строкам
                sum = 0
                for i in range(len(mat[j])): #проход по элементам строки
                    sum += mat[j][i]
                res.append(sum)
        else:
            return 'матрица не прямоугольная'
    return res
            
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))

def col_sums(mat):
    res = []
    if proverka(mat) != 'ValueError':
        if len(mat) != len(mat[0]): #проверка прям.матрицы

            for i in range(len(mat[0])):
                sum = 0
                for j in range(len(mat)): #проход по строкам
                    sum += mat[j][i]
                res.append(sum)
        else: return 'матрица не прямоугольная'   
    return res

#print(col_sums([[1, 2, 3], [4, 5, 6]]))