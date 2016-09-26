import os
import re
import operator


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, encoding='cp1251') as file_handler:
        return file_handler.read()


def get_most_frequent_words(text):
    words = re.findall(r'\w+', text)
    words_count = {}
    for word in words:
        words_count[word] = words_count.get(word, 0) + 1
    words_count = sorted(words_count.items(), key=operator.itemgetter(1), reverse=True)
    return words_count[:10]


if __name__ == '__main__':
    filepath = input('Введите путь до файла: ')
    words_dict = get_most_frequent_words(load_data(filepath))
    print('Самые частые слова')
    [print('{}: {}'.format(key, str(value))) for key, value in words_dict]
