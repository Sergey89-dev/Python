# Задание 5
def my_funk ():
    job = 0
    general = 0
    
    while job == 0:
        numbers = input('Введите значения через пробел или нажмите Y, чтобы выйти:').split()

        first_sum = 0
        for i in range(len(numbers)):
            if numbers[i] == 'y' or numbers[i] == 'Y':
                job = 1
                break
            else:
                first_sum = first_sum + int(numbers[i])
        general = general + first_sum
        print(f'Сумма значений: {general}')
    
    
    print(f'Итоговая сумма: {general}')

my_funk()
input("Нажмите enter, чтобы выйти.")





