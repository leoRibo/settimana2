rubbrica = [
    {"nome": "Marco", "numero_cell": "3208635679"},
    {"nome": "Luca", "numero_cell": "3345678960"}
]

def mostra_contatti(lista):
    for numero, contatto in enumerate(lista):
        print(f"{numero+1}. {contatto['nome']} - {contatto['numero_cell'][0:3]}-{contatto['numero_cell'][3:]}")

mostra_contatti(rubbrica)

def aggiungi_contatto(lista):
    nuovo_nome = input("aggiugi nome").title()
    nuovo_numero = input("aggiugi il numero di telefono").title()
    lista.append({"nome": nuovo_nome, "numero_cell": nuovo_numero})

aggiungi_contatto(rubbrica)
mostra_contatti(rubbrica)






        