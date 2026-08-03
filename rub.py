rubbrica = [
    {"nome": "Marco", "numero_cell": "3208635679"},
    {"nome": "Luca", "numero_cell": "3345678960"}
]

def mostra_contatti(lista):
    for numero, contatto in enumerate(lista):
        print(f"{numero+1}. {contatto['nome']} - {contatto['numero_cell'][0:3]} - {contatto['numero_cell'][3:]}")

mostra_contatti(rubbrica)

        