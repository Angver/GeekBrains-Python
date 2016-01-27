import string

author = 'Alexey Peshekhonov'
version = '0.1'

def get_dictionary(filename):
    """
    Возвращает словарь, считанный из файла

    :param filename: str Файл с текстом из которого считывается словарь
    :return: dict Возвращает словарь
    """

    f = open(filename, encoding='utf-8')
    text = f.read()
    words = text.split()
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
