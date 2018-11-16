""" Задание №2.
Переделать Задание №1 с созданием и использованием собственное исключение
WhitespaceError с атрибутами:
    position - позиция в строке
    symbol - какой именно непечатный символ
Функция main() демонстрирует работу вашей функции, должна красиво показывать
что именно вызвало исключение.
"""

from string import whitespace
class WhitespaceError(Exception):
    def __init__(self, position, symbol):
        self.position = position
        self.symbol = symbol


def string_processing(text, *args, **kwargs):
    loop = 1
    for i in text:
        if i in whitespace:
            try:
                raise WhitespaceError(loop, i)
            except WhitespaceError:
                print("Позиция непечатного символа: {}.".format(loop), "Символ: '{}'.".format(i))
        elif loop == len(text):
            result = text.upper()
            return result
        else:
            loop += 1


def main():
    strings = input('Введите текст или слово >>> ')
    print(string_processing(strings))


if __name__ == "__main__":
    main()

