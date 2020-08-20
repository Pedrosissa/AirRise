import serial
#import mysql.connector
import datetime
import pymysql.cursors

ser = serial.Serial('COM6', 9600)

mysqldb = pymysql.connect(
    host="sql173.main-hosting.eu",
    user="u385256052_airrise",
    db="u385256052_airrise",
    password="airrise",
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=True
)

mycursor = mysqldb.cursor()

def inserir(data, hora, leitura):
    try:
        mycursor.execute("INSERT INTO detector ( data, hora, leitura) VALUES (%s, %s, %s)",(data,hora[:8],leitura))
        print("Inseriu")
        mysqldb.commit()
    except Exception as error:
        print(error)

def dados():
    while(1):
        recebi = ser.readline().strip().decode('UTF-8')
        print(recebi)
        data = datetime.datetime.now().date()
        hora = datetime.datetime.now().time()
        inserir(str(data), str(hora),str(recebi));

dados()