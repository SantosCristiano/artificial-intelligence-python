import requests, re, csv
from bs4 import BeautifulSoup
from collections import Counter
import matplotlib.pyplot as plt


#Descarga informacion de la web
###############################################################
###############################################################
###############################################################
###############################################################
###############################################################
###############################################################
link = 'https://www.burbuja.info/inmobiliaria/forums/cov_19/'
res = requests.get(link)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)
set([t.parent.name for t in text])





###############################################################
###############################################################
###############################################################
###############################################################
###############################################################
###############################################################
################################
#Comienza a limpiar texto y análisis de palabras
texto = ''
blacklist = [
    '[document]','noscript', 'header', 'html','meta','head', 'input','script',
]
for t in text:
    if t.parent.name not in blacklist:
        texto += '{} '.format(t)
#Banear palabras 
#dic = [ 'Registrarse','inicio','Visitas','div', 'class', 'Visitas', 'Respuestas', 'Buscar', 'mensajes', 'Hoy', 'Ayer', 'Foros',"Siguiente","Hace","Economia","Última","Hora",]
b = {'Respuestas': '', 'Inicio': '', 'Visitas': '', 'Hoy': '', 'Ayer': '', 'Última': '','Temas': '','Mensaje': '','sesión': '','mensajes': '','siguiente': '','Hora': '','Foros': '',
'página': '','AM': '','PM': '','Visitas': '','Visitas': '','Foros': '','Economía': '','Buscar': '', 'Siguiente': '','Bolsa': '', 'Hace': '','minutos': '','Último': '','Hace': '',
'Buscar': '','Adherido': '','Nuevos': '','Adherido': '','JavaScript': '','Trending': '','Foros': '','Menú': '','Miembros': '','Registrarse': '','foros': '','Foro': '','Navegador': '',
'Xenforo': '','2022': '','Burbuja.info': '','by': '','Iniciar': '','navegador': '','foro': '','momento': '','hace': '',':': '','Lunes': '','Martes': '','Miércoles': '','Jueves': '',
'Viernes': '','Sábado': '','Domingo': '','solo': '','Hilo': '','ahora': '','-': '','ahora': '','sólo': '','para': '','como': '','|': '','%': '','.': ''}
for x,y in b.items():
    texto = texto.replace(x, y)

###Quitas numeros
texto2 = ''.join([i for i in texto if not i.isdigit()])
texto = texto2
#Quitar monososilabas
shortword = re.compile(r'\W*\b\w{1,3}\b')
texto = shortword.sub('', texto)
######
#print(datoslimpieza)
limpieza = texto
#Detectar palabras más repetidas
split_it = limpieza.split()
Counter = Counter(split_it)
most_occur = Counter.most_common(20)
print("######")
diccionariodepalabras = dict(most_occur)
print(diccionariodepalabras)




###############################################################
###############################################################
###############################################################
###############################################################
###############################################################
###############################################################
#Almacenar en archivo
import csv
new_path = open("data.csv", "w")
z = csv.writer(new_path)
for new_k, new_v in diccionariodepalabras.items():
    z.writerow([new_k, new_v])

new_path.close()


#Hacer gráfico
###############################################################
###############################################################
###############################################################
###############################################################
###############################################################
###############################################################
###############################################################
###############################################################
###############################################################
keys = diccionariodepalabras.keys()
values = diccionariodepalabras.values()
plt.bar(keys, values)
plt.show()
