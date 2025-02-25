from db import (atualizar_usuario,
                inserir_user,
                deletar_user,
                mostrar_users,
                buscar_valor,
                verificar_termos)

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    password="!Senha123",
    user="root",
    database="chatbot2"
)


while True:

    print("")
    print("--------")
    print("\n\n1 para buscar valor, ",
          "\n\n2 para mostrar todos os usuarios ",
          "\n\n3 para inserir usuario, ",
          "\n\n4 para deletar usuario, ",
          "\n\n5 para atualizar o usuario"
          "\n\n6 para verificar termos do usuario\n\n")
    print("--------")
    dg = input("DIGITE:")
    print("--------")
    print("")

    if dg == '1':
        print("")
        print("--------")
        x = input('Digite o numero: ')
        y = input('Digite o valor buscado(nome, contrato, etc): ')
        buscar_valor(x, y)
        print("--------")
        print("")

    if dg == '2':
        mostrar_users()

    if dg == '3':
        print("")
        print("\n\n--------\n\n")
        x = input('Digite nome: ')
        y = input('Digite numero: ')
        z = input('Digite contrato: ')
        inserir_user(x, y, z, True)
        print("\n\n--------\n\n")
        print("")

    if dg == '4':
        print("")
        print("\n\n--------\n\n")
        x = input('Digite o id: ')
        deletar_user(x)
        print("\n\n--------\n\n")
        print("")

    if dg == '5':
        print("")
        print("\n\n--------\n\n")
        x = input('Digite o id: ')
        y = input('Digite a coluna(nome, numero, numero de contrato): ')
        z = input('Digite o novo valor: ')
        atualizar_usuario(x, y, z)
        print("\n\n--------\n\n")
        print("")

    if dg == '6':
        print("")
        print("\n\n--------\n\n")
        x = input('Digite o numero: ')
        if verificar_termos(x) == 1:
            print("usuario aceitou os termos")
        elif not verificar_termos(x):
            print("usuario nao aceitou os termos")
        print("\n\n--------\n\n")
        print("")
