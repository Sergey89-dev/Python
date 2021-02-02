#Задание 5
with open('sum.txt', 'w+') as numbers:
    line = input('Введите цифры через пробел:')
    numbers.writelines(line)
    my_numb = line.split()
print(sum(map(int, my_numb)))
    