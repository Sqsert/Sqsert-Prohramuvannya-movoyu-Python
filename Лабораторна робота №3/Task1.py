my_string = str(input("Введіть слово: "))

length = len(my_string)

if length >= 7:
    slice_result = my_string[-6:-2]
    print("Отриманий зріз:", slice_result)
else:
    print("Рядок надто короткий для виконання операції зрізу")
