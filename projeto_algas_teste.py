import time
import sys
import mysql.connector

con = mysql.connector.connect(host='localhost',
database='atividade_sprint',
user='root',
password = 'temp123')

mycursor = con.cursor()
sql = "INSERT INTO tblProjetoSprint VALUES (null, %s, %s)"

tempo_inicial = (time.time())

def transaction(range):
    x_points = []
    y_points = []

    lista = []

    for item in range:
        # time.sleep(0.1)
        lista.append(item)
        tempo_append = (time.time())

        tempo_final = (tempo_append - tempo_inicial)
        x_points.append(tempo_final*100)
        y_points.append(sys.getsizeof(lista))
        val = (f"{tempo_final*100}", f"{sys.getsizeof(lista)}")
        mycursor.execute(sql, val)
    con.commit()

    print(lista)

transaction(range(100000, 600000, 100000))
transaction(range(1000, 6000, 100))
transaction(range(100, 600, 100))
transaction(range(10, 60, 10))
transaction(range(1000000, 6000000, 1000000))