from repository.GenericFileRepository import GenericFileRepository
from repository.class1_repository import Class1InMemoryRepository
from repository.class2_repository import Class2InMemoryRepository
from service.class1_service import Class1Service
from service.class2_service import Class2Service
from user_interface.console import Console

class1_repository = Class1InMemoryRepository()
class2_repository = Class2InMemoryRepository()
class1_repository = GenericFileRepository('class1.pkl')
class2_repository = GenericFileRepository('class2.pkl')


class1_service = Class1Service(class1_repository, class2_repository)
class2_service = Class2Service(class2_repository, class1_repository)


console = Console(class1_service,class2_service)
console.run_console()