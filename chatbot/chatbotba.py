from nltk.chat.util import Chat, reflections
mis_reflexions = {
"ir": "fui",
"hola": "hey"
}

pares = [
    [
        r"se me ha caido el hosting (.*)",
        ["Sentimos ese fallo, para reiniciarlo, entra en CPANEL y selecciona reiniciar",]
    ],
     [
        r"cuando hay que pagar la factura (.*)",
        ["Hay que pagarla el dia 15 de cada mes por tarjeta de crédito",]
    ],
    [
        r"(.*) ampliar el servicio",
        ["Para ampliar el servicio, contacta con facturacion",]
    ],
    [
        r"disculpa (.*)",
        ["No pasa nada",]
    ],
    [
        r"hola|hey|buenas",
        ["Hola", "Que tal",]
    ],
    [
        r"que (.*) quieres ?",
        ["Nada gracias",]
        
    ],
    [
        r"(.*) creado ?",
        ["Fui creado hoy",]
    ],
    [
        r"finalizar",
        ["Chao","Fue bueno hablar contigo"]
],
]
def chatear():
    print("Hola, soy el servicio de hosting") #mensaje por defecto
    chat = Chat(pares, mis_reflexions)
    chat.converse()
if __name__ == "__main__":
    chatear()

chatear()