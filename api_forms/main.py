import pandas as pd
from plyer import notification
import mysql.connector
from cfgdb import alterar_form_preenchido_numero, inserir_form_preenchido_menu, verificar_form_preenchido, buscar_form_preenchido_menu

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="!Senha123",
    database="forms"
)

mycursor = mydb.cursor()


# Função para buscar o valor da quantidade
def buscar_quantidade():
    mycursor.execute("SELECT quantidade FROM quantidade_linhas")
    resultado = mycursor.fetchone()
    if resultado:
        return resultado[0]
    else:
        return None


# Função para alterar o valor da quantidade
def alterar_quantidade(novo_valor):
    mycursor.execute("UPDATE quantidade_linhas SET quantidade = %s", (novo_valor,))
    mydb.commit()
# https://docs.google.com/spreadsheets/d/16qknEKv5gTh172a_ggYFaWjP8n7KWq6CEM9Tx2iWc5M/edit?usp=sharing


sheet_id = "16qknEKv5gTh172a_ggYFaWjP8n7KWq6CEM9Tx2iWc5M"


data_frame = pd.read_csv(
    f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

coluna = 0
timer = 0
linhas_antigas = buscar_quantidade()

print(linhas_antigas)
print(f"Número de linhas: {len(data_frame)}")
print(f'numero de colunas {linhas_antigas}')

while True:
    timer += 1

    # Lê os dados atuais
    data_frame = pd.read_csv(
        f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

    # Verifica novo conteúdo
    if len(data_frame) > linhas_antigas:
        # Há novas linhas
        novas_linhas = data_frame.iloc[linhas_antigas:, :]

        # Notifica sobre as novas linhas
        for _, row in novas_linhas.iterrows():
            # Processa e exibe os dados
            data_hora = row[0]
            nome = row[1]
            email_user = row[2]
            celular = row[4]

            # Exibe os dados
            print("-------------------")
            print(f'{data_hora} \n')
            print(f'{nome} \n')
            print(f'{email_user} \n')
            print(f'{celular} \n')
            print("-------------------")

            # Envia uma notificação
            notification.notify(
                title='Nova Linha Adicionada',
                message=f'Nova linha adicionada:\n{data_hora}\n{nome}\n{email_user}\n{celular}',
            )

        # Atualiza o número de linhas antigo
        alterar_quantidade(linhas_antigas + 1)
        linhas_antigas = buscar_quantidade()
        update_query = "UPDATE menu SET form_preenchido = 1"
        # Conectar ao banco de dados "config"
        config_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="!Senha123",
            database="config"
        )
        # Conectar ao banco de dados "forms"
        config_cursor = config_db.cursor()
        config_cursor.execute(update_query)
        config_db.commit()
        alterar_form_preenchido_numero("556191769500", 1)
        print(verificar_form_preenchido("556191769500"))
        # Conectar ao banco de dados "forms"
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="!Senha123",
            database="forms"
        )
        mycursor = mydb.cursor()

    if timer == 10:

        # Roda seu código aqui
        try:
            for coluna in range(len(data_frame.columns)):
                data_hora = data_frame.iloc[coluna, 0]
                nome = data_frame.iloc[coluna, 1]
                email_user = data_frame.iloc[coluna, 2]
                celular = data_frame.iloc[coluna, 4]
                print("-------------------")
                print(f'{data_hora} \n')
                print(f'{nome} \n')
                print(f'{email_user} \n')
                print(f'{celular} \n')
                print("-------------------")
                coluna += 1
        except IndexError:
            print('Não há mais colunas')

        # Guarda número de linhas para comparar na próxima execução
        linhas_antigas = len(data_frame)

        timer = 0
