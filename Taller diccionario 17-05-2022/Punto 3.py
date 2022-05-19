usuarios = {
    "iperurena": {
        "nombre": "Iñaki",
        "apellido": "Perurena",
        "password": "123123"
        },
        "fmuguruza": {
            "nombre": "Fermín",
            "apellido": "Muguruza",
            "password": "654321"
        },
        "aolaizola": {
            "nombre": "Aimar",
            "apellido": "Olaizola",
            "password": "123456"
        }
    }
for intentos in range(0,3):
    u=input("Usuario: ")
    c=int(input("Contraseña: "))
    for i in usuarios:
        if i==u:
            if int((usuarios[i]["password"]))==c:
                print(usuarios[i]["nombre"],usuarios[i]["apellido"])
                break