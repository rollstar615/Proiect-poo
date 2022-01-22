from domain.class1 import Class1
from repository.class1_repository import Class1InMemoryRepository


class Class1Service:
    """
    Manages car logic.
    """

    def __init__(self, class1_repository , repository):
        """
        Creates a class1 service.
        """
        self.__class1_repository = class1_repository
        self.__repository = repository


    def add_class1(self, id_class1, cerinta1, cerinta2):
        """
                it adds a class checking first if the id_class1 is unique
                :param id_class1:
                :param cerinta1:
                :param cerinta2:
                :return: a new element of the class
                """

        class1 = Class1(id_class1,cerinta1, cerinta2)
        self.__class1_repository.create(class1)



    def remove_class1(self, id_class1):
        """

        :param id_class1:
        :return: the list without the object which contained id_class1
        """

        class1_to_delete = self.__class1_repository.read(id_class1)
        if class1_to_delete is not None:
            self.__class1_repository.delete(id_class1)


    def update_class1(self,id_class1, cerinta1, cerinta2):
        """
                it updates a class1 where the given parameters form class1
                :param id_class1:
                :param cerinta1:
                :param cerinta2:
                :return:  class1 updated by user input param
                """

        class1_to_update=self.__class1_repository.read(id_class1)
        if class1_to_update is not None:
            class1 = Class1(id_class1,cerinta1, cerinta2)
            self.__class1_repository.update(class1)

    def get_all(self):
        """
        :return: a list of all the class1.
        """
        return self.__class1_repository.read()