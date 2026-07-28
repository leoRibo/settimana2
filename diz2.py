attivita = {
    "studiare Python": False,
    "fare la spesa": True,
    "chiamare mamma": False
}
for compito in attivita:
    print(f"{compito}: {'✅ fatto' if attivita[compito] else '❌ da fare'}")


familia = {
    "io" : {
        "capelli": "biondi",
        "occhi": "verdi",
        "altezza_cm": 187,
        "piedi": 2,
        "taglia_piedi": 44,
    },
    "mamma": {
        "capelli": "blu",
        "occhi": "arancio",
        "altezza_cm": 204,
        "piedi": 5,
        "taglia_piedi": 98,
    }
}
familia["io"]["colore preferito"] = "jallo"
print(familia["mamma"]["occhi"])
print(familia["io"]["colore preferito"])
