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
    for word in words:
        word = word.strip('!"$%&\'()*+,-./::<=>?@[\\]^_{|}~` ')
        if word == '':
            continue

        if word.lower() in dictionary:
            dictionary[word.lower()] += 1
        else:
            dictionary[word.lower()] = 1

    return dictionary

def sort_dict_by_keys(dictionary):
    """
    Сортировка словаря по ключам

    :param dictionary: dict Несортированный словарь
    :return: dict Отсортированный словарь
    """

    k = dict.keys(dictionary)
    k = sorted(k)

    new_dictionary = {}
    for key in k:
        new_dictionary[key] = dictionary.pop(key)

    return new_dictionary
