from domain.class1 import Class1
from domain.class2 import Class2
from domain.class1class2_viewmodel import Class2ViewModel


class Class2Service:

    """
    Manages location logic.
    """

    def __init__(self, class2_repository,class1_repository ):
        """
        Creates a class2 service.
        """
        self.__class2_repository = class2_repository
        self.__class1_repository=class1_repository


    def add_class2(self,id_class2,id_class1,propr1,propr2):
        """
        it adds a class checking first if the id_class2 is unique and if id_class1 exists in class1
        :param id_class2:
        :param id_class1:
        :param propr1:
        :param propr2:
        :return: a new element of the class
        """
        if not propr1:
            raise ValueError('Trebuie introdusa valoare')
        if propr2<0:
            raise ValueError('Trebuie Valoare pozitiva')
        if self.__class1_repository.read(id_class1) is None:
            raise ValueError('Nu exista nicio grupa cu id-ul ')
        class2 = Class2(id_class2,id_class1,propr1, propr2)
        self.__class2_repository.create(class2)
        for class1 in self.__class1_repository.read():
            class1=self.__class1_repository.read(class1.id_entity)
            id_class1=class1.id_entity
            cerinta1=class1.cerinta1
            for class2 in self.__class2_repository.read():
                id_cla=class2.id_class1
                if id_class1==id_cla:
                    cerinta2="inceput"
                class1=Class1(id_class1,cerinta1,cerinta2)
                self.__class1_repository.update(class1)
        return self.__class1_repository.read()

    def get_all(self):
        """
        :return: a list of all the classes, containing class1 and class2 objects.
        """
        return self.__class2_repository.read()

    def remove_class2(self, id_class2):
        """

        :param id_class2:
        :return: the list without the object which contained id_class2
        """
        class2_to_delete = self.__class2_repository.read(id_class2)
        if class2_to_delete is not None:
            self.__class2_repository.delete(id_class2)

    def update_class2(self, id_class2, id_class1, propr1, propr2):
        """
        it updates a class where the given parameters form class2
        :param id_class2:
        :param id_class1:
        :param propr1:
        :param propr2:
        :return:  class2 updated by user input param
        """

        if self.__class1_repository.read(id_class1) is None:
            raise ValueError('Nu exista nicio grupa cu id-ul ')
        class2 = Class2(id_class2, id_class1, propr1, propr2)
        self.__class2_repository.update(class2)

    def schimbare_status_in_functie_de_comision(self):
        """

        :return: an updated version of class1 where it changes the cerinta2 if the numbers of appereances id_class1 in class2 is more than 1
        """
        for class1 in self.__class1_repository.read():
            class1=self.__class1_repository.read(class1.id_entity)
            id_class1=class1.id_entity
            cerinta1=class1.cerinta1
            for class2 in self.__class2_repository.read():
                id_cla=class2.id_class1
                if id_class1==id_cla:
                    cerinta2="inceput"
                class1=Class1(id_class1,cerinta1,cerinta2)
                self.__class1_repository.update(class1)
        return self.__class1_repository.read()

    def finalizare_comision(self):
        """
        input: class1, class2
        it checks if the numbers of appereances of id_class1 in class2 is more than 2
        :return: the updated version of propr2 from class2
        """
        r=0
        for class1 in self.__class1_repository.read():
            class1=self.__class1_repository.read(class1.id_entity)
            id_class1=class1.id_entity
            cerinta1=class1.cerinta1
            for class2 in self.__class2_repository.read():
                id_cla=class2.id_class1
                if id_cla==id_class1:
                    r=r+1
            if r>=2:
                cerinta2="finalizat"
                class1=Class1(id_class1,cerinta1,cerinta2)
                self.__class1_repository.update(class1)
            r=0

        return self.__class1_repository.read()

    def sortare_comisioane_dupa_durata(self):
        """
        input:class1, class2
        :return: a list containing the sum and the id of the sorted comision descending by sum
        """
        s=0
        lista=[]
        for class1 in self.__class1_repository.read():
            class1=self.__class1_repository.read(class1.id_entity)
            id_class1=class1.id_entity
            for class2 in self.__class2_repository.read():
                class2=self.__class2_repository.read(class2.id_entity)
                id_cla=class2.id_class1
                propr2=class2.propr2
                if id_cla==id_class1:
                    s=s+propr2
            lista.append((s,id_class1))
            s=0
        lista.sort(reverse=True)
        return lista

    def finalizare_comision_dupa_id(self,x):
        r=0
        for class2 in self.__class2_repository.read():
            id_cla=class2.id_class1
            if id_cla==x:
                r=r+1
        if r>=2:
            from service.class1_service import Class1Service
            class1=self.__class1_repository.read(id_cla)
            cerinta1=class1.cerinta1
            cerinta2="finalizat"
            class_to_update=Class1(id_cla,cerinta1,cerinta2)
            self.__class1_repository.update(class1)
        return self.__class1_repository.read()




        


