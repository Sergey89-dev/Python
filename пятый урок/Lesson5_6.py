#Задание 6
stud_mater = {}
with open('study.txt', 'r') as init_f:
    for line in init_f:
        material, lect, pr, lab = line.split()
        stud_mater[material] = int(lect) + int(pr) + int(lab)
    print(f'Общее количество часов по предмету:{stud_mater}')