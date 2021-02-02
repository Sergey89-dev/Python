#Задание 2
num_lines = 0
num_words = 0

with open('Строки и слова.txt', 'r') as br:
    for i in br:
        words = i.split()

        num_lines = num_lines + 1
        num_words += len(words)

print(f"Количество слов:{num_words},\n количество строк:{num_lines}")