attivita = [
    {"compito": "studiare Python", "fatto": False},
    {"compito": "fare la spesa", "fatto": True}
]

for numero, istruzione in enumerate(attivita):
    stato = "✅" if istruzione["fatto"] else "❌"
    print(f"{numero+1}. {stato}   {istruzione['compito']}")


utente = input("metti un nuovo compito")
attivita.append({"compito": utente, "fatto": False})

for numero, istruzione in enumerate(attivita):
    stato = "✅" if istruzione["fatto"] else "❌"
    print(f"{numero+1}. {stato}   {istruzione['compito']}")



