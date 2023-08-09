"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)

Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)

Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco

Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""

# Minha solução________________________________________________________________

# from abc import ABC, abstractmethod

# class Account(ABC):
#     def __init__(self,agency, account_number, balance: float):
#       self.agency = agency # agência
#       self.account_number = account_number # numero da conta
#       self.balance = balance  # saldo
#       self.authenticated = False


#     def depositary(self, value) -> float: # depositar
#         self._balance += value


#     @abstractmethod
#     def to_withdraw(self, value) -> float: #sacar
#        ...

# class Bank:
#     def __init__(self):
#         self.clients = []
#         self.accounts = []
#         self.agencies = []

#     def autentication(self,client, account: Account):
#         if client not in self.clients:
#             print('O cliente não está cadastrado no banco')
#             return False
#         elif account not in self.accounts:
#             print('A conta não está cadastrada no banco')
#             return False
#         elif account.agency not in self.agencies:
#             print('A agência não está no banco')
#             return False

#         account.authenticated = True
#         return True

#     def add_account(self,account: Account):
#         self.accounts.append(account)
#         self.agencies.append(account.agency)

#     def add_client(self, client):
#         self.clients.append(client)

# class People(ABC):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.account = None

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, value):
#         self._name = value

#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, value):
#         self._age = value

#     @property
#     def account(self):
#         return self._account

#     @account.setter
#     @abstractmethod
#     def account(self, value): ...


# class SavingsAccount(Account):
#     def depositary(self, value: int):
#         self.balance += value
#         return self.balance

#     def to_withdraw(self, value):
#         if self.authenticated:
#             if  self.balance >= value:
#                 self.balance -= value
#                 return self.balance
#             print('Saldo insuficiente.')
#         else:
#             print('É necessário uma autenticação do banco.')

# class CheckingAccount(Account):
#     def __init__(self, agency, account_number, balance, extra_limit):
#         super().__init__(agency, account_number, balance)
#         self.extra_limit = extra_limit


#     def depositary(self, value: int):
#         self.balance += value
#         return self.balance


#     def to_withdraw(self, value):
#         if self.authenticated:
#             if self.extra_limit + self.balance >= value:
#                 if self.balance == 0:
#                     print(f'Alcançou o seu limite extra')
#                 self.balance -= value
#                 return  self.balance
#             return print('Saldo insuficiente.')
#         print('É necessário uma autenticação do banco.')


# class Client(People):
#     def __init__(self, nome, idade, account: Account):
#         super().__init__(nome, idade)
#         self.account = account

#     @People.account.setter
#     def account(self,value):
#         if isinstance(value, Account):
#             self._account = value


# bank = Bank()
# saving_account = SavingsAccount('Bungas', '001', 100)
# cheking_account = CheckingAccount('Fanfas', '002', 150,100)
# client_1 = Client('Gerêncio','23',saving_account)

# bank.add_client(client_1)
# bank.add_account(cheking_account)
# bank.autentication(client_1,cheking_account)

# cheking_account.to_withdraw(100)
# print(cheking_account.balance)


# Solução professor____________________________________________________________

# A RESOLUÇÃO DO PROFESSOR ESTARÁ NO ARQUIVO "AULA 166"
