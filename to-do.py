attivita = [
    {"compito": "studiare Python", "fatto": False},
    {"compito": "fare la spesa", "fatto": True}
]

for numero, istruzione in enumerate(attivita):
    stato = "✅" if istruzione["fatto"] else "❌"
    print(f"{numero+1}. {stato}   {istruzione['compito']}")
