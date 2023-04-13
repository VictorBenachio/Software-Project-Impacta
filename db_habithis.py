from datetime import date
import mysql.connector

connection = mysql.connector.connect(host='localhost', user='root', password='SistemaHabitos12!', database='habithis_db')
cursor = connection.cursor()

def criarUser():
    nome = "guilherme"
    birthday = "1999-03-23"
    email = "teste@teste.com"
    password = "1234"
    gender = 0
    command = f'INSERT INTO user (NAME, BIRTHDAY, EMAIL, PASSWORD, GENDER) VALUES ("{nome}", "{birthday}", "{email}", "{password}", {gender})'
    cursor.execute(command)
    connection.commit()

def lerUser():
    command = 'SELECT * FROM user;'
    cursor.execute(command)
    resultado = cursor.fetchall()
    print(resultado)

def updateUser():
    user = 7
    colunm = 'NAME'
    updateValue = 'Guilherme'
    command = f'UPDATE user SET {colunm} = "{updateValue}" WHERE USER_ID = {user}'
    cursor.execute(command)
    connection.commit()

def deleteUser():
    user = 7
    command = f'DELETE FROM user WHERE USER_ID = {user}'
    cursor.execute(command)
    connection.commit()

deleteUser()
cursor.close()
connection.close()

