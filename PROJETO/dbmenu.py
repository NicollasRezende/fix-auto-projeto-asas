from db import (atualizar_usuario,
                inserir_user,
                deletar_user,
                mostrar_users,
                buscar_valor,
                verificar_termos
                )

from db import session_timeout_set_db, session_timeout_view_db

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    password="!Senha123",
    user="root",
    database="chatbot_asas"
)


while True:

    print("")
    print("--------")
    print("\n\n1 para buscar valor, ",
          "\n\n2 para mostrar todos os usuários ",
          "\n\n3 para inserir usuário, ",
          "\n\n4 para deletar usuário, ",
          "\n\n5 para atualizar o usuário"
          "\n\n6 para verificar termos do usuário\n\n")
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
            print("Usuário aceitou os termos")
        elif not verificar_termos(x):
            print("Usuário não aceitou os termos")
        print("\n\n--------\n\n")
        print("")

    if dg == "7":
        session_timeout_set_db()
        print(session_timeout_view_db())
