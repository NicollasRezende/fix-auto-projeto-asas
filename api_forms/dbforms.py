from ast import While
import mysql.connector
from numpy import true_divide

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="!Senha123",
    database="forms"
)

mycursor = mydb.cursor()


# FunÃ§Ã£o para buscar o valor da quantidade
def buscar_quantidade():
    mycursor.execute("SELECT quantidade FROM quantidade_linhas")
    resultado = mycursor.fetchone()
    if resultado:
        return resultado[0]
    else:
        return None


# FunÃ§Ã£o para alterar o valor da quantidade
def alterar_quantidade(novo_valor):
    mycursor.execute("UPDATE quantidade_linhas SET quantidade = %s", (novo_valor,))
    mydb.commit()

alterar_quantidade(0)
# Exemplo de uso:
# Buscar e exibir a quantidade atual
# quantidade_atual = buscar_quantidade()
# print("Quantidade atual:", quantidade_atual)

# Alterar a quantidade para um novo valor (por exemplo, 15)
# novo_valor = 4
# alterar_quantidade(novo_valor)
# print("Quantidade alterada para:", novo_valor)

# Buscar e exibir a quantidade atualizada
# quantidade_atualizada = buscar_quantidade()
# print("Quantidade atualizada:", quantidade_atualizada)
