import sqlite3 as sql
import random
from random import randint

connection = sql.connect('parcial2Datos.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE cliente(idCliente VARCHAR(6),nit VARCHAR(9),nombre VARCHAR(40),credito FLOAT,CONSTRAINT PK_cliente PRIMARY KEY (idCliente))')
cursor.execute('CREATE TABLE tienda(idTienda VARCHAR(6),nombre VARCHAR(40),direccion VARCHAR(60),CONSTRAINT PK_tienda PRIMARY KEY (idTienda))')
cursor.execute('CREATE TABLE compra(idCompra VARCHAR(6),idCliente VARCHAR(6),idTienda VARCHAR(6),total FLOAT,fecha VARCHAR,CONSTRAINT PK_compra PRIMARY KEY (idCompra),FOREIGN KEY (idCliente) REFERENCES cliente(idCliente),FOREIGN KEY (idTienda) REFERENCES tienda(idTienda))')

nameList = [
    'Juan',  
    'Jose'  ,
    'Esteban'  ,
    'Raul'  ,
    'Jaime'  ,
    'Rocio' , 
    'Ana' , 
    'Sofia'  ,
    'Camila' , 
    'Luis' , 
    'Roberto', 
    'Jorge' , 
    'Laura' , 
    'Antonio' , 
    'Natalia' , 
    'Javier' , 
    'Francisco' , 
    'Alejandro' , 
    'Gonzalo' , 
    'Susana' , 
    'Fernando' , 
    'Rodrigo' , 
    'Cristobal' , 
    'Lucrecia' , 
    'Valeria' , 
    'Sasha' , 
    'Cristina',  
    'Mario' , 
    'Carlos'
    ]

lastnameList = [
    'Cabrera',
    'Hernandez',
    'Garcia',
    'Martinez',
    'Maldonado',
    'Arevalo',
    'Guerra',
    'Cozza',
    'Rivera',
    'Rosales',
    'Ahuat',
    'Bran',
    'Casillas',
    'Ramos',
    'Van Dyk',
    'Quezada',
    'Quinones',
    'Lopez',
    'De Leon',
    'Alvarado'
]

addressList = [
    '14 Ave A Zona 15',
    '17 Ave B Zona 2',
    '2 Ave A Zona 1',
    '15 Ave C Zona 18',
    '12 Ave B Zona 4',
    '12 Ave C Zona 6',
    '14 Ave C Zona 2',
    '16 Ave B Zona 1',
    '2 Ave B Zona 3',
    '1 Ave C Zona 15',
    '18 Ave A Zona 16',
    '3 Ave A Zona 16',
    '5 Ave C Zona 10',
    '10 Ave A Zona 11',
    '2 Ave B Zona 12',
    '5 Ave B Zona 13',
    '7 Ave A Zona 5',
    '10 Ave C Zona 1'
]

storeNameList = [
    'Cemaco',
    'Siman',
    'Modas Caramelos',
    'Paiz',
    'La Torre',
    'Clau',
    'El Duende',
    'Lacoste',
    'Adidas',
    'Nike',
    'Pull&Bear',
    'Zara',
    'Columbia',
    'Artemis Edinter',
    'Sophos',
    'Vans',
    'Do Mi Sol',
    'Casa Instrumental',
    'Kodak'
]

idsClientes = []
idsTiendas = []
nombresTiendas = []

def generate_random_name():
    nombre = random.choice(nameList)
    apellido = random.choice(lastnameList)
    completo = f'{nombre} {apellido}'
    return completo

def generate_nit():
    nit = random.randint(1111111, 9999999)
    return nit

def generate_date():
    day = random.randint(0,28)
    month = random.randint(1,12)
    year = random.randint(2012, 2019)
    date = f'{day}/{month}/{year}'
    return date

def insert_cliente(id_cliente):
    nombre = generate_random_name()
    nit = generate_nit()
    credito = random.randrange(1000, 10000)
    query = f"INSERT INTO cliente VALUES({id_cliente}, {nit}, '{nombre}', {credito})"
    cursor.execute(query)
    return query

def insert_tienda(id_tienda):
    bandera = True
    direccion = random.choice(addressList)
    nombre = random.choice(storeNameList)
    query = f"INSERT INTO tienda VALUES({id_tienda}, '{nombre}', '{direccion}')"
    if (not(nombre in nombresTiendas)):
        cursor.execute(query)
        nombresTiendas.append(nombre)
    return query

def insert_compra(id_compra, id_cliente, id_tienda):
    total = random.randrange(10, 10000)
    date = generate_date()
    query = f"INSERT INTO compra VALUES ({id_compra}, {id_cliente}, {id_tienda}, {total}, '{date}')"
    cursor.execute(query)
    return query


if __name__ == '__main__':
    for i in range(0, 499):
        idcliente = randint(000000,999999)
        idsClientes.append(idcliente)
        idtienda = randint(000000,999999)
        idsTiendas.append(idtienda)     
        insert_cliente(idcliente)
        insert_tienda(idtienda)
    for i in range(0, 1499):
        insert_compra(randint(000000,999999), random.choice(idsClientes), random.choice(idsTiendas))
    connection.commit()


