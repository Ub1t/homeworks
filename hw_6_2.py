
from string import whitespace
class WhitespaceError(Exception):
    def __init__(self, position, symbol):
        self.position = position
        self.symbol = symbol
    def posym(self):
        print("Позиция непечатного символа: {}.".format(self.position), "Символ: '{}'.".format(self.symbol))


def string_processing(text, *args, **kwargs):
    loop = 1
    for i in text:
        if i in whitespace:
            try:
                raise ValueError
            except ValueError:
                s = WhitespaceError(loop, i)
                s.posym()
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

