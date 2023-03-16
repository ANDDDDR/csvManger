def show_menu():
    print('''
    \tCSV MANAGER
    1.Создать .csv
    2.Поиск элемента в файле
    3.Сортировка данных
    4.Добавление данных
    5.Удаление данных
    6.Добавление элементов в группу
    7.Вывести файл
    ''')

def choice_menu():
    try:
        choice = int(input("Введите номер пункта: "))
        if choice in range(1,8):
            return choice
        else:
            raise ValueError
    except:
        raise ValueError

def show_data(input_str):
    for i in input_str.split('\n'):
        for j in i.split(';'):
            a = 6-(len(j)//4)
            print(j,end="\t"*int(a))
        print()