attivita = [
    {"compito": "studiare Python", "fatto": False},
    {"compito": "fare la spesa", "fatto": True}
]
def ripetere():
    for numero, istruzione in enumerate(attivita):
        stato = "✅" if istruzione["fatto"] else "❌"
        print(f"{numero+1}. {stato}   {istruzione['compito']}")

ripetere()

utente = input("C'é qualcosa di nuovo?")
if utente.lower() != "no":
    attivita.append({"compito": utente, "fatto": False})

ripetere()

cambio = int(input("che cosa cambi?"))
if attivita[cambio-1]["fatto"] == False: 
    attivita[cambio-1]["fatto"] = True 
else:
    attivita[cambio-1]["fatto"] = False

ripetere()

