"""
Задание 1.
Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
Пример:
1 2 3    1 2 3
4 5 6    4 5 6
7 8 9    7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18
"""


class Matrix:
    def __init__(self, rows):
        self.rows = rows

    def __str__(self):
        matrix = f"{list(self.rows)}".replace("[[", "[")
        matrix = f"{matrix}".replace("]]", "]")
        matrix = f"{matrix}".replace("], [", "]\n[")
        return f"{matrix}".replace(", ", " ")

    def __add__(self, other):
        try:
            my_list = []
            for el in list(self.rows):
                sum_list = []
                for i in el:
                    sum_m = i + list(other.rows)[list(self.rows).index(el)][el.index(i)]
                    sum_list.append(sum_m)
                my_list.append(sum_list.copy())
                sum_list.clear()
            return Matrix(my_list)
        except IndexError:
            return "Ошибка! Нельзя складывать матрицы разных размеров"


a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(f'Первая матрица:\n{a}')
print(f'Вторая матрица:\n{b}')
print(f'Сумма матриц:\n{a + b}')
