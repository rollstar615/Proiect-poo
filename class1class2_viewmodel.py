class Class2ViewModel:

    def __init__(self, Class1, Class2) :

        self.Class1 = Class1
        self.Class2 = Class2

    def __str__(self):
        return '{}. Class2 {} '.format(
            self.Class2.id_entity,
            self.Class1,)