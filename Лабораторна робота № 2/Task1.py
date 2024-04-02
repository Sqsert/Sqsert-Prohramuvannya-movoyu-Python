import math

def calculate_z(m):
    if m == 3:
        return "Помилка: m не може дорівнювати 3"
    elif m < 3:
        return "Помилка: m має бути більше 3 для обчислення кореня"
    else:
        return math.sqrt((m + 3) / (m - 3))

def calculate_y(n):
    if n <= 0:
        return "Помилка: n має бути більше 0"
    else:
        result = 1
        for i in range(2, 2*n + 1, 2):
            result *= i
        return result


m = float(input("Введіть значення m: "))
n = int(input("Введіть натуральне число n: "))
    
z_result = calculate_z(m)
print("Результат обчислення z:", z_result)
    
y_result = calculate_y(n)
print("Результат обчислення у:", y_result)
