def check_params_type(*args, **kwargs):
    s = input('Введите символы: ')
    for i in s:
        try:
            i = int(i)
            print('Символ "{}" относится к int()'.format(i))
        except ValueError:
            print('Символ "{}" не относится к int(), а относится к {}'.format(i, type(i)))

def main():
    check_params_type()
if __name__ == "__main__":
    main()
