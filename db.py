from datetime import date
import mysql.connector

def criarUser(name, birthday, email, password, gender):
    connection = mysql.connector.connect(host='localhost', user='root', password='SistemaHabitos12!', database='habithis_db')
    cursor = connection.cursor()
    command = f'INSERT INTO user (NAME, BIRTHDAY, EMAIL, PASSWORD, GENDER) VALUES ("{name}", "{birthday}", "{email}", "{password}", "{gender}")'
    cursor.execute(command)
    connection.commit()
    cursor.close()
    connection.close()

def lerUser():
    connection = mysql.connector.connect(host='localhost', user='root', password='SistemaHabitos12!', database='habithis_db')
    cursor = connection.cursor()
    command = 'SELECT * FROM user;'
    cursor.execute(command)
    resultado = cursor.fetchall()
    print(resultado)
    cursor.close()
    connection.close()

def updateUser():
    connection = mysql.connector.connect(host='localhost', user='root', password='SistemaHabitos12!', database='habithis_db')
    cursor = connection.cursor()
    user = 7
    colunm = 'NAME'
    updateValue = 'Guilherme'
    command = f'UPDATE user SET {colunm} = "{updateValue}" WHERE USER_ID = {user}'
    cursor.execute(command)
    connection.commit()
    cursor.close()
    connection.close()

def deleteUser():
    connection = mysql.connector.connect(host='localhost', user='root', password='SistemaHabitos12!', database='habithis_db')
    cursor = connection.cursor()
    user = 7
    command = f'DELETE FROM user WHERE USER_ID = {user}'
    cursor.execute(command)
    connection.commit()
    cursor.close()
    connection.close()

