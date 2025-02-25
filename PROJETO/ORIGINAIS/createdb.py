import mysql.connector
import random

def gerar_codigo_aleatorio():
    codigo = ''.join(str(random.randint(0, 9)) for _ in range(10))
    return codigo

# Configurar as informaÃ§Ãµes de conexÃ£o
config = {
    'user': 'root',
    'password': '!Senha123',
    'host': 'localhost'
}

# Criar a conexÃ£o
conexao = mysql.connector.connect(**config)

# Criar um cursor para executar comandos SQL
cursor = conexao.cursor()

# Criar o banco de dados 'chatbot2'
cursor.execute("CREATE DATABASE IF NOT EXISTS chatbot3")

# Selecionar o banco de dados recÃ©m-criado
cursor.execute("USE chatbot2")

# Criar a tabela 'usuarios'
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255),
        numero VARCHAR(255),
        numero_contrato INT,
        termos_aceitos BOOLEAN
    )
""")

# Fechar o cursor e a conexÃ£o
cursor.close()
conexao.close()
