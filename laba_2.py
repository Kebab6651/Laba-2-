import numpy as np

def factorial(current_fact, fact):
    if fact > 2:
        new_fact = current_fact * (fact - 2) * (fact - 1) * fact
    else:
        if fact == 0 or fact == 1:
            return 1
        else:
            return 2
    return new_fact

def fact_matrix (matrix):
    matrix1 = matrix.dot(matrix)
    return matrix1

def algorithm(n, cur_fact, cur_matrix):
    fact = 2 * n - 2
    current_fact = factorial(cur_fact, fact)
    if current_fact >= 2:
        cur_matrix = fact_matrix(cur_matrix)
    sign, logdet = np.linalg.slogdet(cur_matrix)
#вычисляем определитель матрицы
    if logdet < 700:
        def_matrix = np.linalg.det(cur_matrix)
        summand = det_matrix / current_fact * (-1) **(n-1)
        return summand, current_fact,cur_matrix
    else:
        return 0, 0, 0

try:
    while True:
        size_m = input("Введите длину матрицы(положительное, целое число, в диапозоне от 3 до 10):")
        accur = input("Введите точность вычисления (кол-во знаков после запятой, в диапозоне от 1 до 5):")
        size_m = size_m.strip()
        accur = accur.strip()
        if size_m.isdigit() and accur.isdigit():
            size_m = int(size_m)
            accur = int(accur)
            if (size_m >= 3) and (size_m <= 10) and (accur <= 5) and (accur >=1):
                break
            else:
                print("Ошибка.Заданное число не входит в разрешеннный диапозон.")
        else:
            print("Неверный ввод данных.")

    n = 1
    cur_fact = 1
    sum_row = 0

    while True:
        cur_matrix = np.random.randint(-10, 11, size = (size_m, size_m))
        cur_matrix = cur_matrix/10
        det_matrix = np.linalg.det(cur_matrix)
        if det_matrix == 0:
            continue
        break

    while True:
        summand, current_fact, cur_matrix = algorithm(n,cur_fact,cur_matrix)
        if summand == 0 and current_fact == 0 and cur_matrix == 0:
            print("Определитель матрицы слишком большой!")
            break
        sum_row += summand
        n += 1
        if abs(summand) <= 10**(-accur):
            print("Сумма знакопеременного ряда равна с точность {0},"
                  " после запятой: {1:.10f}".format(accur,sum_row))
            break
except:
    print("Извините, произошла ошибка")

