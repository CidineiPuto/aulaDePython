
class Foo:
    def soma(self,x: int | float, y: int | float) -> int | float:
        """Soma x e y

        Este módulo contém funções e exemplos de documentação de funções.
        A função soma você já conhece bastante.

        :param x: Número 1
        :type x: int or float
        :param y: Número 2
        :type y: int or float

        :return: A soma entre x e y
        :rtype: int or float
        """
        return x + y

    def bar(self) -> int:
        """ O que ele faz
        
        :raises NotImplementedError: Se o método não for definido
        """

        raise NotImplementedError('teste')


    def multiplica(self,
        x: int | float,
        y: int | float,
        z: int | float | None = None
    ) -> int | float:
        """Multiplica x, y e/ou z
        Multiplica x e y. Se z for enviado, multiplica x, y, z.
        """
        if z is None:
            return x * y
        return x * y * z