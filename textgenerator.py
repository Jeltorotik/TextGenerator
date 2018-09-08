# Первая версия. Самая простая. То есть выбираем слова не по частоте появления в
# тренировочном тексте, а рандомно. Поэтому генерируемый текст получается немного несвзяанным.
#Думаю, как исправить.

#P.S. Накормил словарь Войной и миром, Гарри Поттером, анектодами, и Егором Летовым. Получилось очень даже ничего. (Все файлы есть на гитхабе)

import re
import random

# Считываем наши тексты для обучения. (Работает только с форматом utf-8. Я не знаю как это улучшить) 
importing_data = open('firstdataset.txt', encoding='utf-8').read()
# Добавляем ещё один датасет, для разнообразия.
importing_data += open('seconddataset.txt', encoding='utf-8').read()

# Избавляемся от всех ненужных символов и разбиваем текст на слова.
# (Я не решил, что сделать с пунктуацией,
# т.е. не понимаю, как разбить текст на слова и знаки пунктуации.
# Но вовсе убирать их тоже не стоит)
reg = re.compile('[^а-яА-Я .,]')
data = reg.sub(' ', importing_data).split()

# Разбиваем список слов на пары.
def generate_bigrama(data):
    for i in range(len(data)-1):
        yield (data[i], data[i+1])
        
pairs_of_words = list(generate_bigrama(data))

# Создаём словарь
dictionary = {}

# Добавляем слова из пар в словарь по принципу:
# Если первое слово из пары есть в словаре, то
# прикрепляем к этому слову второе слово,
# т.е. если из [('Hello', 'world!'), ...] слово 'Hello' уже есть в слове, то
# dictionary = {'Hello':['world!', ...], ...}. 
for first_word, second_word in pairs_of_words:
    if first_word in dictionary.keys():
        dictionary[first_word].append(second_word)
    else:
        dictionary[first_word] = [second_word]

# Выбираем рандомно первое слово
first_word = random.choice(data)

# Выбираем до тех пор, пока в этом слове не найдётся заглавная буква
# (можно бы улучшить, ведь в некоторых словах заглавная буква идёт не первой)
while first_word.islower():
    first_word = random.choice(data)

#Создаём список, который будем использовать для создания нового теста.
#Добавляем туда выбранное нам слово с заглавной буквой - оно будет нашим стартовым словом.
new_text = [first_word]

#Задаём переменную с длинной текста.
new_text_length = int(input('Введите длину желаемого текста:\n'))

# Добавляем в наш список рандомно слова из словаря.
for i in range(new_text_length):
    new_text.append(random.choice(dictionary[new_text[-1]]))

#Преобразуем список в текст и выводим его.
print(' '.join(new_text))

