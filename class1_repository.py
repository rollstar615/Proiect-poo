from domain.class1 import Class1


class Class1InMemoryRepository:
    '''
    Repository for storing data in memory
    '''

    def __init__(self):
        '''
        Creates an in memory repository.
        '''
        self.__storage = {}



    def create(self, Class1):
        class1_id = Class1.id_class1
        if class_id in self.__storage:
            raise KeyError('The grupa id already exists!')
        self.__storage[class1_id] = Class1

    def read(self, class1_id=None):
        self.__load_from_file(class1.pkl)
        if class1_id is None:
            return self.__storage.values()

        if class1_id in self.__storage:
            return self.__storage[class1_id]
        return None

    def update(self, Class1):
        class1_id = Class1.id_class1
        if class1_id not in self.__storage:
            raise KeyError('There is no class1 with that id!')
        self.__storage[class1_id] = Class1

    def delete(self, class1_id):
        if class1_id not in self.__storage:
            raise KeyError('There is no grupa with that id!')
        del self.__storage[class1_id]

    def clear(self):
        self.__storage.clear()