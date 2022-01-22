from domain.class1 import Class1
from repository.repository_error import RepositoryError
from repository.class2_repository import Class2InMemoryRepository

class Console:

    def __init__(self, class1_service, class2_service):
        self.__class1_service = class1_service
        self.__class2_service = class2_service

    def __show_menu(self):
        print('1. Class1')
        print('2. Class2')
        print('x. Exit')

    def run_console(self):

        while True:
            self.__show_menu()
            op = input('Optiune: ')
            if op == '1':
                self.__show_class1()
            elif op == '2':
                self.__show_class2()
            elif op == 'x':
                break
            else:
                print('Comanda invalida!')

    def __show_class1(self):

        while True:
            self.__show_menu_class1()
            op = input('Optiune: ')
            if op == '1':
                self.__handle_class1_add()
            elif op == '2':
                self.__handle_class1_remove()
            elif op=='3':
                self.__handle_class1_update()
            elif op == 'a':
                self.__show_list(self.__class1_service.get_all())
            elif op == 'b':
                break
            else:
                print('Comanda invalida!')

    def __show_menu_class1(self):
        print('--- Class1')
        print('1. Adauga')
        print('2. Sterge')
        print('3. Update')
        print('a. Afisare')
        print('b. Back')


    def __handle_class1_add(self):
        try:
            id_class1=int(input("id ul e"))
            cerinta1=int(input("descriere e"))
            cerinta2="neinceput"
            self.__class1_service.add_class1(
                id_class1,
                cerinta1,
                cerinta2
            )
            print(' a fost adaugata!')
        except RepositoryError as re:
            print('Eroare:', re)

            #print('Avem erori:', ve)

    def __show_list(self, objects):
        for object in objects:
            print(object)

    def __handle_class1_remove(self):
        try:
            id_class1 = int(input('Dati id-ul de sters: '))
            self.__class1_service.remove_class1(id_class1)
        except Exception:
            print("TODO BETTER EXCEPTION HANDLING")

    def __handle_class1_update(self):
            id_class1 = int(input("id ul e"))
            cerinta1 = int(input("descriere e"))
            cerinta2="neinceput"
            self.__class1_service.update_class1(
                id_class1,
                cerinta1,
                cerinta2
            )
            print('Masina a fost adaugata!')

    def __show_class2(self):

        while True:
            self.__show_menu_class2()
            op = input('Optiune: ')
            if op == '1':
                self.__handle_class2_add()
            elif op == '2':
                self.__handle_class2_remove()
            elif op == '3':
                self.__handle_class2_update()
            elif op=='4':
                self.__show_list(self.__class2_service.schimbare_status_in_functie_de_comision())
            elif op=='5':
                self.__show_list(self.__class2_service.finalizare_comision())
            elif op=='6':
                self.__show_list(self.__class2_service.sortare_comisioane_dupa_durata())
            elif op=='7':
                x=int(input("idul este"))
                self.__show_list(self.__class2_service.finalizare_comision_dupa_id(x))
            elif op == 'a':
                self.__show_list(self.__class2_service.get_all())
            elif op == 'b':
                break
            else:
                print('Comanda invalida!')

    def __show_menu_class2(self):
        print('--- Activitati')
        print('1. Adauga')
        print('2. Sterge')
        print('3. Update')
        print('4.Schimbare status comision')
        print('5. Finalizare comision ')
        print('6. Sortare comision dupa durata')
        print('7.Finalizare comision dupa id')
        print('a. Afisare')
        print('b. Back')


    def __handle_class2_add(self):
        try:
            id_class2=int(input("activitate id"))
            id_class1=int(input("comision id"))
            propr1=str(input("descriere"))
            propr2=int(input("durata"))
            self.__class2_service.add_class2(
                id_class2,
                id_class1,
                propr1,
                propr2
                )
            print('a fost adaugat')
        except ValueError as ve:
            print('Erori:')
            for error in ve.args[0]:
                print(error)

    def __handle_class2_remove(self):
        try:
            id_class2=int(input('dati idul de sters'))
            self.__class2_service.remove_class2(id_class2)
        except Exception:
            print("slab")

    def __handle_class2_update(self):
        id_class2= int(input("activitate id"))
        id_class1 = int(input("comision id"))
        propr1 = float(input("descriere"))
        propr2 = int(input("durata este"))

        self.__class2_service.update_class2(
            id_class2,
            id_class1,
            propr1,
            propr2

        )
        print('s a facut')
