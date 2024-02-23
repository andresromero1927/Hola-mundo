import pandas as pd
import sqlite3

# Conectarse a la base de datos SQLite
conn = sqlite3.connect('travel.sqlite')

# Crear un cursor para ejecutar consultas
cursor = conn.cursor()

# Consulta SQL para obtener los tipos de asientos únicos
consulta = "SELECT DISTINCT fare_conditions FROM seats;"

# Ejecutar la consulta
cursor.execute(consulta)


# Obtener los resultados de la consulta
tipos_de_asientos = cursor.fetchall()

#Imprimir los tipos de asientos únicos
print("Tipos de asientos únicos:")
for tipo_de_asiento in tipos_de_asientos:
   print(tipo_de_asiento[0])



consulta1= "SELECT DISTINCT fare_conditions FROM ticket_flights;"

cursor.execute(consulta1)

tipos_de_tiquetes= cursor.fetchall()
print("Tipos de tikets:")
for tipo_de_tiquetes in tipos_de_tiquetes:
    print(tipo_de_tiquetes[0])




consulta2= "SELECT DISTINCT model FROM aircrafts_data;"

cursor.execute(consulta2)

tipos_de_aviones= cursor.fetchall()
print("Tipos de aviones:")
for tipo_de_aviones in tipos_de_aviones:
    print(tipo_de_aviones[0])


consulta3= "SELECT DISTINCT total_amount FROM bookings;"

cursor.execute(consulta3)

cantidad_de_reservas=  cursor.fetchone()[0]
print("Cantidad de reservas:", cantidad_de_reservas)


# Cerrar el cursor y la conexión
cursor.close()
conn.close()