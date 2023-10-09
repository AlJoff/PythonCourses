numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
missing_item_index = 4
new_numbers = numbers[:missing_item_index]+numbers[missing_item_index+1:]  # Список чисел без пропуска
avg_numbers = sum(new_numbers)/len(numbers) # Среднее арифметическое списка numbers
numbers[missing_item_index] = avg_numbers
print("Измененный список:", numbers)
