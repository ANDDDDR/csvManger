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
            if len(j)<4:
                a=5
            elif len(j)<8:
                a=4
            elif len(j)<12:
                a=3
            elif len(j)<16:
                a=2
            else:
                a=1
            print(j,end="\t"*a)
        print()