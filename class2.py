from domain.entity import Entity


class Class2(Entity):

    def __init__(self,id_class2, id_class1, propr1, propr2):
        super().__init__(id_class2)
        self.__id_class1 = id_class1
        self.__propr1 = propr1
        self.__propr2 = propr2


    @property
    def id_class1(self):
        return self.__id_class1

    @property
    def propr1(self):
        return self.__propr1

    @property
    def propr2(self):
        return self.__propr2

    def __str__(self):
        return 'Class2- id activitate{},id comision {}, descriere {},durata {} '.format( self.id_entity,
                                                self.id_class1,
                                                self.propr1,
                                                self.__propr2)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.id_entity == other.id_entity