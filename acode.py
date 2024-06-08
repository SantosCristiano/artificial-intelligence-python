#antes hay que installar las librerias
#en inicio - ejecutar - cmd
#poner:
#pip install selenium
#si te faltan mas librerias hacer lo mismo
#con el programa (ide) pycharm te avisa y te las instala
#tambien hay que tener firefox instalado en ordenador

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from subprocess import check_output
import webbrowser

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
print ("Productos más vendidos Amazon por categoría seleccionada:")
print ("Cargando...")
driver.get("https://www.amazon.es/gp/bestsellers/industrial/ref=zg_bs_nav_0")
like = driver.find_elements_by_class_name('a-link-normal')
contar = 0
for x in range(0,len(like)):
    if like[x].is_displayed():
        element = like[x].text
        print (element)
        datos = ""
        contarcaracteres = len(element)
        if "€" in element:
            datos = "precio:"
        if contarcaracteres > 20:
            datos = "producto:"
        a = open('test.txt', 'a+')
        a.write(datos + element)
        if datos == "precio:":
            a.write("\n" + "----------------")
        a.write("\n")
        a.close()
        print("...")
webbrowser.open("test.txt")