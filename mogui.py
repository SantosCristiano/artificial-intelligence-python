import pymongo
from pymongo import MongoClient


cluster = MongoClient("")
db = cluster["BASE2"]
collection = db["alumnos"]
datos = {"id" :1, "alumno": "Maria", "examen": "Matematicas", "nota": 10}
datos2 = {"id" :2, "alumno": "Marko", "examen": "Matematicas", "nota": 3}
#Meter datos en colecciones:
collection.insert_many([datos,datos2])
#Encontrar datos:
resultados = collection.find({"alumno":"Marko"})
for consulta in resultados:
    print(consulta)