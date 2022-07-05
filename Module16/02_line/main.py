class_A = list(range(160, 178, 2))
class_B = list(range(162, 183, 3))
class_A.extend(class_B)
for i in range(len(class_A) - 1):
    for j in range(i, len(class_A)):
        if class_A[j] < class_A[i]:
            class_A[j], class_A[i] = class_A[i], class_A[j]
print(f'Список учеников: {class_A}')
