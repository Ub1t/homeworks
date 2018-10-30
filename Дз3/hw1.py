def name():
    s = input("Введите ваше имя >>> ")
    myname = "Владислав"
    if len(s) >= 1:
        print("Здравствуйте {}!".format(s))
    else:
        print("Здравствуйте {}!".format(myname))
name()