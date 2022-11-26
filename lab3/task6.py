list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_number = list_numbers[0]


for index, value in enumerate(list_numbers):
    if value >= max_number:
        max_number = value
        index_number = index

index_last = len(list_numbers)-1

list_numbers[index_number], list_numbers[index_last] = list_numbers[index_last], list_numbers[index_number]

# TODO Оформить решение

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
