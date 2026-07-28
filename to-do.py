attivita = [
    {"compito": "studiare Python", "fatto": False},
    {"compito": "fare la spesa", "fatto": True}
]

for numero, istruzione in enumerate(attivita):
    stato = "✅" if istruzione["fatto"] else "❌"
    print(f"{numero+1}. {stato}   {istruzione['compito']}")


utente = input("C'é qualcosa di nuovo?")
if utente.lower() != "no":
    attivita.append({"compito": utente, "fatto": False})

for numero, istruzione in enumerate(attivita):
    stato = "✅" if istruzione["fatto"] else "❌"
    print(f"{numero+1}. {stato}   {istruzione['compito']}")

cambio = int(input("che cosa cambi?"))
if attivita[cambio-1]["fatto"] == False: 
    attivita[cambio-1]["fatto"] = True 
else:
    attivita[cambio-1]["fatto"] = False

for numero, istruzione in enumerate(attivita):
    stato = "✅" if istruzione["fatto"] else "❌"
    print(f"{numero+1}. {stato}   {istruzione['compito']}")


