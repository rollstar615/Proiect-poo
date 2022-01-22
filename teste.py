from domain.class1 import Class1
from service.class1_service import Class1


def test_class1_service():

    class1_service = Class1Service()
    class1 = Class1(1, 2, , "finalizat")
    class1_service.add_class1(class1.id_entity,
                        class1.cerinta1,
                        class1.cerinta2,)
    assert class1_service.get_all() == [class1]

    try:
        class1_service.add_class1(class1.id_entity,
                            class1.cerinta1,
                            class1.cerinta2)
        assert False
    except KeyError:
        assert True

test_classs1_service()


from domain.class2 import Class2
from service.class2_service import Class2Service
def test_class2_service():

    class2_service = Class2Service()
    class2 = Class2(1, 2, 3, 4)
    class2_service.add_class2(class2.id_entity,
                        class2.id_class1,
                        class2.propr1,
                        class2.propr2,)
    assert class2_service.get_all() == [class2]

    try:
        class2_service.add_class2(class2.id_entity,
                            class2.id_class1,
                            class2.propr1,
                            class2.propr2)
        assert False
    except KeyError:
        assert True

test_class2_service()

def cerinta3():
    class2_service = Class2Service()
    class2 = Class2(1, 2, 3, 4)
    class1_service = Class1Service()
    class1 = Class1(1, 2,, "inceput")
    class2_service.add_class2(class2.id_entity,
                              class2.id_class1,
                              class2.propr1,
                              class2.propr2, )
    assert class2_service.get_all() == [class2]
    assert class1_service.get_all() ==[class1]

    try:
        class2_service.add_class2(class2.id_entity,
                                  class2.id_class1,
                                  class2.propr1,
                                  class2.propr2)
        assert False
    except KeyError:
        assert True




