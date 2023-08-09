exercicio_usados = [
    "pular corda",
    "polichinelos",
    "Cordida estacionária",
    "Mountain climber",
    "Dança aeróbica",
    "Subir e descer escadas",
    "Polichinelos de braço",
    "Corrida na esteira",
    "Box jumps",
    "Abdominais de bicicleta",
    "flexões de braço",
    "Agachamentos",
    "Prancha",
    "Lunges",
    "Abdominais",
    "Burpees",
    "Prancha lateral",
    "Elevação de panturrilha",
    "Agachamento com salto",
    "Corrida",
    "Flexões com toque alternado no ombro",
    "Agachamento com chute",
    "Escalador de montanha",
    "Prancha com deslize de joelhos",
    "Flexões com bíceps curl",
    "Flexões com salto",
    "sprint de 30 segundos",
    "Elevação de panturrilha com salto",
    "jumping jacks com agachamento",
    "Swing de kettlebell",
    "Ponte",
    "Cem ou The Hundred",
    "Swan Dive",
    "Spine Stretch Forward",
    "Roll Up",
    "Spine Twist",
    "Saw",
    "the snake / twist",
    "Control Balance",
]

exercicios_sendo_usado = input("Digite o nome de algum exercício: ")
exercicios_ja_usados = 0

for exercicio in exercicio_usados:
    if exercicios_sendo_usado.capitalize() in exercicio:
        print(f'Há um exercício parecido com o nome de "{exercicio}"')
        exercicios_ja_usados += 1
    elif exercicios_sendo_usado in exercicio:
        print(f'Há um alimento parecido com o nome de "{exercicio}"')
        exercicios_ja_usados += 1


if exercicios_ja_usados > 0:
    print(f'O exercício digitado foi usado "{exercicios_ja_usados}" vezes.')
else:
    print("O exercício não está sendo usado")
