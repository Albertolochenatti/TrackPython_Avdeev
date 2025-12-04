numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
count = len(numbers) # кол-во элементов в списке
total = 0 # сумма элементов в списке через переменную
for i in numbers:
    if i is not None:
        total += i
average = total / count # среднее арифметическое
for i in range(len(numbers)): # Заменяем  None на среднее арифметическое
    if numbers[i] is None:
        numbers[i] = average
print("Измененный список:", numbers)
