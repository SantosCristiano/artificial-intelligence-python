import csv
import json
import pandas as pd 
with open("archivo.json", "w") as archivo:
    archivo.write("")
    archivo.close()
pasarlo = pd.DataFrame(pd.read_csv("series.csv", sep = ",", header = 0, index_col = False))
pasarlo.to_json("archivo.json", orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)
print(pasarlo)
# print("Aprende inteligencia artificial gratis: https://creditosrapidos.cash/formacion")