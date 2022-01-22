from domain.class2 import Class2


class Class2InMemoryRepository:
    '''
    Repository for storing data in memory
    '''

    def __init__(self):
        '''
        Creates an in memory repository.
        '''
        self.__storage = {}



    def create(self, Class2):
        '''
        Adds a new class2.
        :param class2: the given class2
        :return: -
        :raises: KeyError if the id already exists
        '''
        class2_id = Class2.id_class2
        if class2_id in self.__storage:
            raise KeyError('The examinare id already exists!')
        self.__storage[class2_id] = Class2

    def read(self, class2_id=None):
        '''
        Gets a class2 by id or all the class2
        :param class2_id: optional, the class2 id
        :return: the list of class2 or the class2 with the given id
        '''
        self.__load_from_file(class2.pkl)
        if class2_id is None:
            return self.__storage.values()

        if class2_id in self.__storage:
            return self.__storage[class2_id]
        return None

    def update(self, Class2):
        '''
        Updates class2.
        :param class2: the class2 to update
        :return: -
        :raises: KeyError if the id does not exist
        '''
        class2_id = Class2.id_class2
        if class2_id not in self.__storage:
            raise KeyError('There is no car with that id!')
        self.__storage[class2_id] = Class2

    def delete(self, class2_id):
        '''
        Deletes a car.
        :param class2_id: the class2 id to delete.
        :return: -
        :raises KeyError: if no class2 with class2_id
        '''
        if class2_id not in self.__storage:
            raise KeyError('There is no class2 with that id!')
        del self.__storage[class2_id]

    def clear(self):
        self.__storage.clear()