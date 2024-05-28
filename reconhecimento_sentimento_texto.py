from textblob import TextBlob
from googletrans import Translator

translator = Translator()
print("Analizando sentimiento de poesía...")
texto = ['Me gusta las flores',
         "Mirar el mar en el cielo",
         "Amaba y me encantaban los pajaros",
         "No odiaba el alma del paisaje",
         "Disfrutaba cada paso del dia"]
comentarios = []
contar = 0
for cont in range(len(texto)):
    traduccion = translator.translate(texto[contar], src='es', dest='en')
    comentarios.append(traduccion.text + "")
    contar = contar + 1

positive_feedbacks = []
negative_feedbacks = []
for feedback in comentarios:
    feedback_polarity = TextBlob(feedback).sentiment.polarity
    if feedback_polarity > 0:
        positive_feedbacks.append(feedback)
        continue
    negative_feedbacks.append(feedback)

print(positive_feedbacks)
print(negative_feedbacks)
print("La poesia analizada tiene un sentimiento:")
if positive_feedbacks > negative_feedbacks:
    print("Sentimiento positivo.")
else:
    print("Sentimiento negativo.")