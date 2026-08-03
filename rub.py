rubbrica = [
    {"nome": "Marco", "numero_cell": "3208635679"},
    {"nome": "Luca", "numero_cell": "3345678960"}
]

def mostra_contatti(lista):
    for numero, contatto in enumerate(lista):
        print(f"{numero+1}. {contatto['nome']} - {contatto['numero_cell'][0:3]}-{contatto['numero_cell'][3:]}")

mostra_contatti(rubbrica)

def aggiungi_contatto(lista):
    nuovo_nome = input("aggiugi nome: ").title()
    nuovo_numero = input("aggiugi il numero di telefono: ")
    lista.append({"nome": nuovo_nome, "numero_cell": nuovo_numero})

aggiungi_contatto(rubbrica)
mostra_contatti(rubbrica)

def cerca_contatto( lista, nome_cercato):
    for contatto in lista:
        if contatto['nome'] == nome_cercato:
            print(f"Trovato! {contatto['nome']}: {contatto['numero_cell']}")
        

chi_cerco = input("CHi vuoi cercare? ").title()
cerca_contatto(rubbrica, chi_cerco)    