def calculate_y(n):
    if n <= 0:
        return "Помилка: n має бути більше 0"
    else:
        result = 1
        for i in range(2, 2*n + 1, 2):
            result *= i
        return result
