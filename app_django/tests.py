from django.test import TestCase

# Create your tests here.
# Подсчет количества слов в текстовом файле
word_map = [] # разбивка текста на слова и добавление в список слов
word_count = {} # словарь, в котором в качестве ключа - слово, в качестве значения - количество повторений слова
with open("test.txt", "r") as file:
    for line in file:
        for word in line.split():
            word_map.append(word)
            print(word)
    print(word_map)

# Цикл по каждому элементу списка слов
for i in range(0, len(word_map)):
    word_count[word_map[i]] = word_map.count(word_map[i])
    # print(word_map.count(word_map[i]))
for w in word_count:
    print(f'Слово {w} встречается {word_count[w]} раз(а)')

# print(word_count)

        # print(line, end="")