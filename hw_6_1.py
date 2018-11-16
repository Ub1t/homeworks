from string import whitespace

def string_processing(text, *args, **kwargs):
    loop = 1
    for i in text:
        if i in whitespace:
            try:
                raise ValueError('value is incorrect')
            except ValueError as error:
                print('Exception:', error)
        elif loop == len(text):
            result = text.upper()
            return result
        else:
            loop += 1
if __name__ == "__main__":
    strings = input('Введите текст или слово >>> ')
    print(string_processing(strings))
