# 9.182 Даны два предложения. Напечатать слова, которые есть только в одном из
# них (в том числе повторяющиеся)

# sentence1 = input('input sentence1 \n')
# sentence2 = input('input sentence2 \n')
# words1 = set(sentence1.split())
# words2 = set(sentence2.split())
# print(words1)
# print(words2)
# unique_words = words1.symmetric_difference(words2)
# for word in unique_words:
# print(word)

# 9.183 Даны два предложения. Напечатать слова, которые встречаются в двух предложениях только один раз.

# sentence1 = input('input sentence1 \n')
# sentence2 = input('input sentence2 \n')
# words1 = sentence1.split()
# words2 = sentence2.split()
# set1 = set(words1)
# set2 = set(words2)
# print(set1)
# print(set2)
# unique_words = (set1 - set2) | (set2 - set1)
# print(unique_words)

# 8.54. Дано натуральное число n. Получить все простые делители этого числа.

# import random
# n = random.randint(1, 10)
# print(n)
# i = 2
# factors = []
# while i * i <= n:
# if n % i:
# i += 1
# else:
# n //= i
# factors.append(i)
# if n > 1:
# factors.append(n)
# print(factors.append(n))

# 11.245 Дан массив. Переписать его элементы в другой массив такого же размера
# следующим образом: сначала должны идти все отрицательные элементы,
# а затем все остальные. Использовать только один проход по исходному
# массиву.

# import numpy as np
# arr = np.array([1, -2, 3, -4, 5, -6, 7, -8, 9])
# negatives = arr[arr < 0]
# non_negatives = arr[arr >= 0]
# result = np.concatenate((negatives, non_negatives))
# print(result)

# Даны две матрицы. Написать функцию для нахождения суммы этих матриц.

# import numpy as np

# def sum_matrices(matrix1, matrix2):
# return np.add(matrix1, matrix2)

# matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# matrix2 = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
# print (matrix1)
# print(matrix2)
# print(sum_matrices(matrix1, matrix2))
