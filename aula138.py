# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self,user):
        # setter, configura valor de algum atributo que não foi configuradox  
        self.user = user

    def set_password(self,password):
        self.password = password

    @classmethod
    def create_with_auth(cls,user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection # método de classe ao invés do método normal, recebe a classe
    
    """
    Este método acima é uma função que recebe a classe, para de uma vez, já criar o user
    e o password automaticamente, utilizando a própria class.    
    """

    @staticmethod
    def log(msg):
        return ('LOG:', msg)
# IMPORTANTE: É sempre necessário do self dentro do método, então é necessário o método de instância

c1 = Connection.create_with_auth('Bungas', 'não sei')
# c1.set_user('Luiz')
# c1.set_password(2112)
print(Connection.log('Essa é a mensagem de log...apdo'))
print(c1.user)
print(c1.password)