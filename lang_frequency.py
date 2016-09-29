import os
import re
import operator


def load_data(filepath):
    if not os.path.exists(filepath):
        print('File does not exists.')
        exit()
    with open(filepath) as file_handler:
        return file_handler.read()


def get_most_frequent_words(text):
    words = re.findall(r'\w+', text.lower())
    words_count = {}
    for word in words:
        words_count[word] = words_count.get(word, 0) + 1
    words_count = sorted(words_count.items(), key=operator.itemgetter(1), reverse=True)
    return words_count[:10]


if __name__ == '__main__':
    filepath = input('Enter the path to the file: ')
    words_dict = get_most_frequent_words(load_data(filepath))
    print('Most frequent words')
    [print('{}: {}'.format(key, str(value))) for key, value in words_dict]
