#21HW
#EASY
import os

# while True:
#     filename = 'ethics.txt'
#     if os.path.isfile(filename):
#         break
#     else:
#         print("Такого файла не существует.")
#         break

# with open(filename, 'r') as f:
#     for i in range(5):
#         line = f.readline()
#         if line:
#             print(line.strip())
#         else:
#             break

#MEDIUM
# f = open('ethics.txt', 'r')
# lines = f.readlines()
# odd_lines = [line.strip() for i, line in enumerate(lines) if i % 2 != 0]
# even_lines = [line.strip() for i, line in enumerate(lines) if i % 2 == 0]

# print("Нечетные строки:")
# for line in odd_lines:
#     print(line)

# print("Четные строки:")
# for line in even_lines:
#     print(line)

