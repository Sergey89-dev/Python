#Задание 4
repl = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_repl = []
with open('one.txt', 'r') as user:

    for i in user:
        i = i.split(' ', 1)
        new_repl.append(repl[i[0]] + '  ' + i[1])
    print(new_repl)

with open('one2.txt', 'w') as user2:
    user2.writelines(new_repl)