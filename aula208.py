from threading import Lock, Thread
from time import sleep

# class MeuThread(Thread):
#     def __init__(self, texto, tempo):
#         self.texto = texto
#         self.tempo = tempo

#         super().__init__()

#     def run(self):
#         sleep(self.tempo)
#         print(self.texto)


# t1 = MeuThread("Thread 1", 5)
# t1.start()
# t2 = MeuThread("Thread 2", 2)
# t2.start()
# t3 = MeuThread("Thread 3", 3)
# t3.start()

# for i in range(20):
#     print(i)
#     sleep(1)

"""
As threads são executadas junto ao processo principal, ela será executada
independende se outra ação estiver sendo executada. E cada um é um thread,
você escolhe as ordens e tudo mais.

Inclusive possui a principal, que é por exemplo, esse for i in range.
Essa thread, está sendo feita puxando a própria classe da thread, colocando
numa outra classe, porém existe outra forma, usando function.
"""


# def vai_demorar(texto: str, tempo: int):
#     sleep(tempo)
#     print(texto)


# t1 = Thread(target=vai_demorar, args=("Hello world", 6))
# t1.start()

# t2 = Thread(target=vai_demorar, args=("Bungas", 8))
# t2.start()

# t3 = Thread(target=vai_demorar, args=("Fanfas", 2))
# t3.start()

# for i in range(10):
#     print(i)
#     sleep(1)

"""
Target é a função, e os args é para passar os argumentos da função. E o start,
inicia a thread.
"""


# def vai_demorar(texto: str, tempo: int):
#     sleep(tempo)
#     print(texto)


# t1 = Thread(target=vai_demorar, args=("Hello world", 5))
# t1.start()
# t1.join()
# Agora, a thread principal irá esperar essa thread acabar, para ser
# Executada, usando "t1.join()".

# while t1.is_alive():  # Quando a thread terminar, o código acaba.
#     print("Esperando a thread.")
#     sleep(2)

# print("Thread acabou")


class Ingressos:
    def __init__(self, estoque: int | float) -> None:
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade: int | float) -> None:
        self.lock.acquire()  # Nisso aqui, ele trancou o método por dentro.
        if self.estoque < quantidade:
            print("Não temos ingressos suficientes.")
            self.lock.release()
            return

        sleep(1)  # Aqui houve um problema, pois essa espera segurou as
        # threads, o que causou em números negativos.

        self.estoque -= quantidade
        print(
            f"Você comprou {quantidade} ingresso(s). "
            f"Ainda temos {self.estoque} em estoque."
        )

        self.lock.release()  # Libera a chave, e a chave só libera se o que
        # Houve lá dentro terminou de executar.


if __name__ == "__main__":
    ingressos = Ingressos(10)

    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()

    print(ingressos.estoque)
