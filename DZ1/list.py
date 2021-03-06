#!/usr/bin/python3

# Списки

# Заполните код преведенных ниже функций. Функция main() уже настроена
# для вызова функций с несколькими различными параметрами,
# и выводит 'OK' в случае, если вызов функции корректен.
# Начальный код каждой функции содержит 'return'
# и является просто заготовкой для вашего кода.


# A. Начало и конец совпадают
# Функция принимает в качестве аргумента список строк.
# Необходимо вернуть количество строк,
# длина которых составляет 2 символа и более, 
# а первый и последний символы этих строк совпадают.
# Примечание: в python нет оператора ++. Но += сработает.
def match_ends(words):  # 2016.01.22_19:21:35 checked. prusanov
    # +++ ваш код +++
    s_count = 0
    for s in words:
        if len(s) >= 2 and s[0] == s[-1]: # Переделал на один if. apeshekhonov
            s_count += 1                    # 2016.01.23_13:51:15 checked. prusanov OK

    return s_count


# B. Начинающиеся с X в начале
# Функция принимает в качестве аргумента список строк.
# Необходимо вернуть отсортированный список строк, в котором:
# сначала идет группа строк, начинающихся на 'x', затем все остальные.
# Наример: из ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] получится
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Подсказка: это можно сделать при помощи склеивания 2х заранее отсортированных списков
def front_x(words):  # 2016.01.22_19:21:44 checked. prusanov
    # +++ ваш код +++
    strings_with_x = []
    other_strings = []

    for s in words:
        if s[0] == 'x' and s != '':  # а что будет, если придет строка '' ?
            # Ответ: строка пойдёт в массив с остальными строками. apeshekhonov
            # # 2016.01.23_13:51:48 checked. prusanov  - проверили? :)
            strings_with_x.append(s)
        else:
            other_strings.append(s)

    strings_with_x.sort()
    other_strings.sort()

    return strings_with_x + other_strings


# C. Сортировка по последнему числу
# Дан спискок непустых списков. 
# Нужно вернуть список, отсортированный по 
# возрастанию последнего элемента каждого подсписка.
# Например: из [[1, 7], [1, 3], [3, 4, 5], [2, 2]] получится
# [[2, 2], [1, 3], [3, 4, 5], [1, 7]]
# Подсказка: используйте параметр key= функции сортировки, 
# чтобы получить последний элемент подсписка.

def sort_last(lists):  # 2016.01.22_19:33:11 checked. prusanov
    # +++ ваш код +++
    return sorted(lists, key=lambda current_list: current_list[-1])   # Переименовал переменную. apeshekhonov
                                        # 2016.01.23_13:52:20 checked. prusanov  OK
    # Хорошо, но сортировать надо по последнему элементу
    # Сделал сортировку по последнему элементу. apeshekhonov
    # но будьте аккуратны с использованием имен вроде list, str, dict, tuple и др. - могут всплыть интересные вещи :)


# D. Удаление соседей
# Дан список чисел.
# Нужно вернуть список, где все соседние элементы
# были бы сведены к одному элементу.
# Таким образом, из [1, 2, 2, 3, 4, 4] получится [1, 2, 3, 4]. 
def remove_adjacent(nums):  # 2016.01.22_19:33:16 checked. prusanov
    # +++ ваш код +++
    checked = []
    for num in nums:
        if not len(checked) or num != checked[-1]:
            checked.append(num)
    return checked


# Простая функция test() используется в main() для вывода
# сравнения того, что возвращает с функция с тем, что она должна возвращать.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s Получено: %s | Ожидалось: %s' % (prefix, repr(got), repr(expected)))


# Вызывает фунции выше с тестовыми параметрами.
def main():
    print('Начало и конец совпадают')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print()
    print('Начинающиеся с X в начале')
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    print()
    print('Сортировка по последнему числу')
    test(sort_last([[1, 3], [3, 2], [2, 1]]),
         [[2, 1], [3, 2], [1, 3]])
    test(sort_last([[2, 3], [1, 2], [3, 1]]),
         [[3, 1], [1, 2], [2, 3]])
    test(sort_last([[1, 7], [1, 6], [3, 4, 5], [2, 2]]),
         [[2, 2], [3, 4, 5], [1, 6], [1, 7]])

    print()
    print('Удаление соседей')
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3, 3]), [2, 3])
    test(remove_adjacent([4, 5, 5, 4, 4]), [4, 5, 4])
    test(remove_adjacent([]), [])


if __name__ == '__main__':
    main()
