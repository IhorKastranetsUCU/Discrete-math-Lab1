from dyscr import *

print("\n", "=" * 50, "\n")
print("Візьмемо файл input.csv та прочитаємо з нього матрицю: А\n")
matrix = read_matrix("input.csv")
for i in matrix:
    print(i)
print()

if matrix == reflexive_closure(matrix):
    print("Матриця уже є рефлексивною")
else:
    print("А^r матриця")
    for i in reflexive_closure(matrix):
        print(i)
print()
if matrix == symmetric_closure(matrix):
    print("Матриця симетрична")
else:
    print("A^s матриця")
    for i in symmetric_closure(matrix):
        print(i)
print()
if check_tranz(matrix):
    print("Матриця уже є транзитивною")
else:
    print("A^t матриця")
    for i in transitive_closure(matrix):
        print(i)

equal_matrix = transitive_closure(symmetric_closure(reflexive_closure(matrix)))

print("\n" + "=" * 50)
print("\nТепер визначимо класи еквівалентності\n")
print(relation_equl(equal_matrix))

print("\nЗапишемо нашу матрицю у файл:")
file = input("Введіть назву файлу в який запишеться відношення еквіваленції A ")
write_relation(f"{file}.csv", equal_matrix)
print("\n Запис відбувся")
print(f"\nТепер прочитаємо файл {file}.txt\n")

matrix_writen = read_matrix(f"{file}.csv")
for i in matrix_writen:
    print(i)

print("\n", "=" * 50, "\n")
print("\nТепер визначимо скільки всього існує транзитивних замикань на множині розміром n")
print(f"\nДля 2: {count_transitive_relations(2)}")
print(f"Для 3: {count_transitive_relations(3)}")
print(f"Для 4: {count_transitive_relations(4)}")
print("Для 5 перевіряти не будемо, бо то буде фест як довго. Повірте на слово, що там буде 154303")