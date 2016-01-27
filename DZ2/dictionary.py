import string

__author__ = 'Alexey Peshekhonov'
__version__ = '0.2'


def get_words_for_dictionary(filename):
    f = open(filename, encoding='utf-8')
    text = f.read()
    words = text.split()

    return words


def get_dictionary(filename):
    """
    Возвращает словарь, считанный из файла

    :param filename: str Файл с текстом из которого считывается словарь
    :return: dict Возвращает словарь
    """

    words = get_words_for_dictionary(filename)

    dictionary = {}
    strip = string.whitespace + string.punctuation + string.digits + "\"'"
    for word in words:
        word = word.strip(strip)
        if word == '':
            continue

        if word.lower() in dictionary:
            dictionary[word.lower()] += 1
        else:
            dictionary[word.lower()] = 1

    return dictionary
