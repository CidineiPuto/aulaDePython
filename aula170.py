# Valores padrão e field em dataclasses
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass, field


@dataclass
class Pessoa:
    # nome: str = 'Missing'
    # ou
    nome: str = field(
        default='MISSINGs')
    sobrenome: str = 'Not sent'
    idade: int = 0  # só é possível definir valores padrões em valores
    # imutáveis
    enderecos: list[str] = field(default_factory=list)
    # só é possível definir valores padrões mutáveis se o field for usado
    # desta maneira


if __name__ == '__main__':
    p1 = Pessoa('Bungas', 'Fanfas')
    print(p1)
