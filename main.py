import os
import file
import list_function
import ui
def main():
    os.system('cls')
    ui.show_menu()
    try:
        choice = ui.choice_menu()
        if choice ==7:
            ui.show_data(file.read_file(input("Введите путь к файлу ")))
    except:
        print("Данные не верны")
        input()
        main()


main()