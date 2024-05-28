import psycopg2
try:
    connection = psycopg2.connect(user = "admin",
                                  password = "1234",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "base2")

    cursor = connection.cursor()
    print ( connection.get_dsn_parameters(),"\n")
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("Te has conectado - ", record,"\n")

except (Exception, psycopg2.Error) as error :
    print ("Error al conectarse a la base de datos", error)

def consultarbase(palabraclave):
    consulta = palabraclave
    cursor.execute("SELECT * from respuestas where contenido like " + "'%" + consulta + "%';")
    record = cursor.fetchone()
    print("Respuesta - ", record,"\n")

while(True):
    print("Hazme una pregunta:")
    teclado = input()
    consultarbase(teclado)