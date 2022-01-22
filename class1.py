from domain.entity import Entity


class Class1(Entity):

    def __init__(self,id_class1, cerinta1, cerinta2):
        super().__init__(id_class1)
        self.__cerinta1 = cerinta1
        self.__cerinta2 = cerinta2


    @property
    def cerinta1(self):
        return self.__cerinta1

    @property
    def cerinta2(self):
        return self.__cerinta2

    def __str__(self):
        return 'Comision -id-ul {},descriere {},status {}'.format( self.id_entity,
                                                                     self.cerinta1,
                                                                     self.cerinta2
                                                                    )

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.id_entity == other.id_entity