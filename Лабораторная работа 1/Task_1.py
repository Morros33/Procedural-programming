numbers = [2, -93, -2, 8, None,-44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", ...)

right_part = numbers[5:]
left_part = numbers[:4]
mean_number = (sum(right_part) + sum(left_part))/ len(numbers)
numbers[4] = mean_number
print("Измененный список:", numbers)
