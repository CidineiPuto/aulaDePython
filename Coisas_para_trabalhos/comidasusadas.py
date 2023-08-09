comidas_usadas = [
    "Filé de salmão grelhado com brócolis e purê de couve flor",
    "Omelete de queijo com bacon e abacate",
    "Frango assado com couve refogada e cogumelos",
    "Hambúrguer de carne com queijo cheddar derretido e espinafre refogado",
    "Salmão assado com espargos e molho de manteiga e limão",
    "Bife grelhado com salada de rúcula, tomate e cebola roxa",
    "Costeletas de porco assadas com abobrinha e cenoura grelhadas",
    "Frango frito sem farinha com couve-flor gratinada",
    "Bife de frango grelhado com pimentões e cebolas assados",
    "Ensopado de carne com abóbora e couve",
    "Salada de frutas com nozes e sementes",
    "Omelete de vegetais: preparado com ovos, cebola, pimentão, tomate\
    e espinafre",
    "Carne de porco assada com abobrinha e cenoura grelhadas",
    "Curry de legumes com carne bovina",
    "Frango grelhado com salada de folhas verdes e nozes",
    "Ovos mexidos com espinafre e tomate",
    "Frango com curry e couve-flor assada",
    "Salada de camarão com abacate e rúcula",
    "Guacamole com chips de vegetais",
    "Omelete de queijo e cogumelos",
    "Frango grelhado com brócolis",
    "Taco de alface com carne moída e guacamole",
    "Espaguete de abobrinha com almôndegas de carne",
    "Salada de atum com abacate",
    "Ovos mexidos com abacate",
    "Costeletas de porco com couve-flor gratinada",
    "bife à milanesa com salada de folhas verdes",
    "Sopa de legumes com carne desfiada",
    "Bolinho de carne com legumes refogados",
    "Frango à parmegiana com berinjela assada",
    "Sopa de lentilha com legumes frescos, acompanhado de uma porção de frutas\
    frescas",
    "ceviche de camarão com abacate, pimentão e cebola roxa, servido com chips\
    de tortilha integral",
    "Salmão assado com molho de iogurte, ervas e limão, acompanhado de arroz\
    integral e legumes no vapor.",
    "Tacos de peixe grelhado com coentro, cebola roxa, abacate e molho de\
    iogurte, servido com arroz integral e feijão preto.",
    "Omelete de cogumelos, espinafre e tomate com uma fatia de pão integral",
    "Espaguete integral com molho de tomate fresco e almôndegas de peru",
    "Curry de Legumes com Arroz Integral",
    "Pão integral com abacate amassado, tomate e ovo poché",
    "Peixe assado com batatas doces e couve-flor assada",
    "salada de quinoa com legumes grelhados",
    "Risoto de cogumelos e espinafre",
    "Tabule de quinoa com pepino, tomate e hortelã",
    "Tacos vegetarianos com guacamole e pico de gallo",
    "Arroz integral com legumes e tofu grelhado",
    "Salada de grão-de-bico com tomate e pepino",
    "Lasanha de berinjela e queijo",
    "Pizza de queijo com espinafre e tomate",
    "salada grega com azeitonas e queijo feta",
    "ratatouille",
    "tomates recheados",
    "Moussaka",
    "Cuscuz marroquino",
    "Paella",
    "Tzatziki",
    "Hummus",
    "tabule",
    "Salada de frutos do mar",
]

alimento_sendo_usado = input("Digite o nome de algum alimento: ")
comidas_ja_usadas = 0

for comida in comidas_usadas:
    if alimento_sendo_usado.capitalize() in comida:
        print(f'Há um alimento parecido com o nome de "{comida}"')
        comidas_ja_usadas += 1
    elif alimento_sendo_usado in comida:
        print(f'Há um alimento parecido com o nome de "{comida}"')
        comidas_ja_usadas += 1


if comidas_ja_usadas > 0:
    print(f'A comida digitada foi usada "{comidas_ja_usadas}" vezes.')
else:
    print("A comida não está sendo usada")
