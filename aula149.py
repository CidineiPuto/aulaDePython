# abstractmethod para qualquer método já decorado (@property e setter)
# É possível criar @property @property.setter @classmethod
# @staticmethod e métodos normais como abstratos, para isso
# use @abstractmethod como decorator mais interno.
# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação.
from abc import ABC, abstractmethod


class PessoaAbstrada(ABC): # o nome anterior era "AbstractFoo" mas classes com tais nome, podem ser trocados
    def __init__(self, name):
        self._name = None
        self.name1 = name

    @property
    def name1(self):
        return self._name

    @name1.setter
    @abstractmethod
    def name1(self, name): ...


class Pessoa(PessoaAbstrada):
    def __init__(self, name):
        super().__init__(name)
        # print('Sou inútil')

    @PessoaAbstrada.name1.setter
    def name1(self, name):
        self._name = name


Bungas = PessoaAbstrada()