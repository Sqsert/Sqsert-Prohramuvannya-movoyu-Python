N = int(input("Введіть розмір масиву: "))

arr = []

for i in range(N):
    num = int(input("Введіть елемент масиву: "))
    arr.append(num)

print("Додатні елементи масиву:")
for num in arr:
    if num > 0:
        print(num)
