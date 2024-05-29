from deepface import DeepFace

foto = "foto3.jpg"
analisis = DeepFace.analyze(foto,actions=["emotion","age"])
print(analisis)
print("############")
print("edad:",analisis["age"])
