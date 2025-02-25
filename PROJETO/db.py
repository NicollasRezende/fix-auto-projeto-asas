import mysql.connector
import random


def gerar_codigo_aleatorio():
    codigo = ''.join(str(random.randint(0, 9)) for _ in range(10))
    return codigo


# Exemplo de uso
codigo_aleatorio_contrato = gerar_codigo_aleatorio()

# Conecte-se ao seu banco de dados MySQL
# usando a função connect() do módulo mysql.connector.
# Passe os parâmetros necessários, como host,
# usuário, senha e nome do banco de dados:
mydb1 = mysql.connector.connect(
    host="localhost",
    password="!Senha123",
    user="root",
    database="chatbot_asas"
)

#  Crie um objeto cursor para executar consultas SQL:
mycursor = mydb1.cursor()

# Execute consultas SQL usando o método execute() do objeto cursor:


def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        password="!Senha123",
        user="root",
        database="chatbot_asas"
    )


def session_timeout_set_db():
    sql = "SET SESSION wait_timeout = 31536000;"
    mycursor.execute(sql)


def session_timeout_view_db():
    sql = "SHOW VARIABLES LIKE 'wait_timeout';"
    mycursor.execute(sql)
    result = mycursor.fetchone()
    if result:
        return result[1]
    else:
        return None


def inserir_user(nome, numero, contrato, termos_aceitos):

    sql = ("INSERT INTO usuarios (nome, numero, numero_contrato,"
           "termos_aceitos) VALUES (%s, %s, %s, %s)")
    values = (nome, numero, contrato, termos_aceitos)
    mycursor.execute(sql, values)
    mydb1.commit()
    print("")
    print(f"Usuário {nome} inserido com sucesso!")
    print("")


def deletar_user(id):
    sql = "DELETE FROM usuarios WHERE id = %s"
    values = (id,)

    mycursor.execute(sql, values)
    mydb1.commit()
    print("")
    print(f"Usuário de id {id} removido com sucesso!")
    print("")


def mostrar_users():
    # Faz a consulta SELECT
    mycursor.execute("SELECT * FROM usuarios")

    # Busca todos os resultados
    resultado = mycursor.fetchall()
    print("")
    print("Dados da tabela usuarios:")
    print("")

    # Itera pelos resultados e imprime
    for linha in resultado:
        print("")
        print("------")
        print(f"ID: {linha[0]}")
        print(f"Nome: {linha[1]}")
        print(f"Número: {linha[2]}")
        print(f"Numero do contrato: {linha[3]}")
        print(f"Termo aceito: {linha[4]}")
        print("------")
        print("")


# vai de 0 a 4 sendo 0 id, 1 nome, 2 numero cel, 3 contrato, 4 termos
def buscar_valor(numero, coluna):

    sql = f"SELECT {coluna} FROM usuarios WHERE numero = %s"

    values = (numero,)

    mycursor.execute(sql, values)

    resultado = mycursor.fetchone()

    valor = resultado[0]

    print("")
    print(f"Valor {coluna} do usuário {numero}: {valor}")
    print("")

    return valor


def atualizar_usuario(numero, coluna, novo_valor):

    campos = {
        'nome': novo_valor,
        'numero': novo_valor,
        'numero_contrato': novo_valor,
        'termos_aceitos': novo_valor
    }

    valor = campos[coluna]

    # SQL Update
    sql = f"UPDATE usuarios SET {coluna} = %s WHERE numero = %s"

    values = (valor, numero)
    mycursor.execute(sql, values)

    mydb1.commit()

    print(f"{coluna} do usuário {numero} atualizado para {valor}")


def verificar_usuario(numero):
    try:
        with conectar_banco() as mydb, mydb.cursor() as mycursor:
            sql = "SELECT * FROM usuarios WHERE numero = %s ORDER BY numero LIMIT 1"
            values = (numero,)

            mycursor.execute(sql, values)

            resultado = mycursor.fetchone()

            existe = (resultado != None)

            return existe

    except mysql.connector.Error as err:
        print(f"Erro ao acessar o banco de dados: {err}")


def verificar_termos(numero):
    try:
        with conectar_banco() as mydb, mydb.cursor() as mycursor:

            sql = "SELECT termos_aceitos FROM usuarios WHERE numero = %s ORDER BY numero LIMIT 1"

            values = (numero,)

            mycursor.execute(sql, values)

            resultado = mycursor.fetchone()

            if resultado:
                termos_aceitos = resultado[0]
                return termos_aceitos
            else:
                termos_aceitos = False
    except mysql.connector.Error as err:
        print(f"Erro ao acessar o banco de dados: {err}")


def editar_termos(numero):

    sql = "SELECT termos_aceitos FROM usuarios WHERE numero = %s"

    values = (numero,)

    mycursor.execute(sql, values)

    resultado = mycursor.fetchone()

    if resultado:
        termos_aceitos = resultado[0]
        return termos_aceitos
    else:
        termos_aceitos = False
