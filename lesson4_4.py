my_list = [4, 7, 6, 4, 9, 1, 7, 1, 5, 3]
print("Исходные элементы списка:\n", my_list)
new_list = [i for i in my_list if my_list.count(i) == 1]
print("Элементы списка, не имеющие повторений:\n", new_list)