
def f1(string_reverse: str) -> str:
    """
    Возвращает перевернутую строку.
    :param string_reverse: Исходная строка
    :return: Перевернутая строка
    """
    # Есть еще куча способов, но, наверно, нужно показать, именно, знание Python.
    return string_reverse[::-1]


def f2(text: str) -> int:
    """
    Возвращает количество слов в строке.
    :param text: Исходная строка
    :return: Количество слов в исходной строке
    """
    words = text.split()
    return len(words)


def f3(sort_list: list) -> list:
    """
    Сортирует список по возрастанию.
    :param sort_list: Исходный список
    :return: Отсортированный список
    """
    # Есть еще sort_list.sort(), он вернет тот же список
    # Либо использовать один из алгоритмов сортировки(пузырек, например)
    # for i in range(len(sort_list) - 1):
    #     for j in range(len(sort_list) - 1 - i):
    #         if sort_list[j] > sort_list[j + 1]:
    #             sort_list[j], sort_list[j + 1] = sort_list[j + 1], sort_list[j]
    return sorted(sort_list)


def f4(string_palindrome: str) -> bool:
    """
    Возвращает True если строка является палиндромом,
    :param string_palindrome: Исходная строка
    :return: True если является палиндромом, иначе False
    """
    if string_palindrome == string_palindrome[::-1]:
        return True
    return False


def f5(factorial_number: int) -> int:
    """
    Находит факториал заданного числа.
    :param factorial_number: Заданное число
    :return: значение факториала
    """
    # С помощью цикла:
    # fact = 1
    # for i in range(2, factorial_number + 1):
    #     fact *= i
    # return fact
    # С помощью рекурсии:
    if factorial_number == 1:
        return 1
    return f5(factorial_number - 1) * factorial_number


def f6(simple_number: int) -> list:
    result_list: list = []
    """
    Выводит простые числа до заданного числа
    :param simple_number: Заданное число
    :return: Список простых чисел
    """
    for number in range(2, simple_number):
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            result_list.append(number)
    return result_list


if __name__ == '__main__':
    string_f1: str = 'Hello, kmv!'
    string_f2: str = 'Hello, kmv!'
    list_f3: list = [0, 9, 5, 2, 7, 1, 3, 3, 3]
    string_f4_v1: str = 'Hello, kmv!!vmk ,olleH'
    string_f4_v2: str = 'Hello, kmv!'
    int_f5: int = 5
    int_f6: int = 100

    print(f"Input string - {string_f1}. Output string - {f1(string_f1)}")
    print(f"Number of words per line - '{string_f2}' - {f2(string_f2)}")
    print(f"List - {list_f3}\n"
          f"Sorted_list - {f3(list_f3)}")
    print(f"Palindrome - {string_f4_v1} - {f4(string_f4_v1)}")
    print(f"Palindrome - {string_f4_v2} - {f4(string_f4_v2)}")
    print(f"Factorial - {int_f5} = {f5(int_f5)}")
    print(f"List of prime numbers for the number {int_f6} - {f6(int_f6)}")

