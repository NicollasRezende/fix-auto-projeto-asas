import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",  #socorro
    password="!Senha123",
    user="root",
    database="config_asas"
)

mycursor = mydb.cursor()


def atualizar_var_menu(var_atualizada, id_menu):
    sql = "UPDATE menu SET var = %s WHERE var = %s"
    values = (var_atualizada, id_menu)

    mycursor.execute(sql, values)
    mydb.commit()

    print(f"Variavel do menu com ID {id_menu} atualizada para {var_atualizada}")


def atualizar_aguardando_resposta_menu(aguardando_resposta_atualizado, id_menu):
    sql = "UPDATE menu SET aguardando_resposta = %s WHERE aguardando_resposta = %s"
    values = (aguardando_resposta_atualizado, id_menu)

    mycursor.execute(sql, values)
    mydb.commit()

    print(f"Campo 'aguardando_resposta' do menu com ID {id_menu} atualizado para {aguardando_resposta_atualizado}")

def atualizar_form_preenchido_menu(form_preenchido_atualizado, id_menu):
    sql = "UPDATE menu SET form_preenchido = %s WHERE form_preenchido = %s"
    values = (form_preenchido_atualizado, id_menu)

    mycursor.execute(sql, values)
    mydb.commit()

    print(f"Campo 'form_preenchido' do menu com ID {id_menu} atu    alizado para {form_preenchido_atualizado}")


def mostrar_status_menu():
    # Faz a consulta SELECT
    mycursor.execute("SELECT * FROM menu")

    # Busca todos os resultados
    resultado = mycursor.fetchall()
    print("")
    print("Dados da tabela usuarios:")
    print("")

    # Itera pelos resultados e imprime
    for linha in resultado:
        print("")
        print("------")
        print(f"menu_atual: {linha[0]}")
        print(f"resposta: {linha[1]}")
        print(f"form: {linha[2]}")
        print(f"numero: {linha[3]}")
        print("------")
        print("")


def inserir_var_menu(var):
    sql = "INSERT INTO menu (var) VALUES (%s)"
    values = (var,)

    mycursor.execute(sql, values)
    mydb.commit()

    print(f"Variavel do menu inserida com sucesso: {var}")


def inserir_aguardando_resposta_menu(aguardando_resposta):
    sql = "INSERT INTO menu (aguardando_resposta) VALUES (%s)"
    values = (aguardando_resposta,)

    mycursor.execute(sql, values)
    mydb.commit()

    print(f"Aguardando Resposta do menu inserido com sucesso: {aguardando_resposta}")


def inserir_form_preenchido_menu(form_preenchido):
    sql = "INSERT INTO menu (form_preenchido) VALUES (%s)"
    values = (form_preenchido,)

    mycursor.execute(sql, values)
    mydb.commit()

    print(f"Formulario Preenchido do menu inserido com sucesso: {form_preenchido}")


def buscar_var_menu(var):
    sql = "SELECT * FROM menu WHERE var = %s"
    values = (var,)

    mycursor.execute(sql, values)

    resultado = mycursor.fetchall()

    if resultado:
        for linha in resultado:
            print(linha[0])
            return linha[0]
    else:
        print(f"Nenhum dado encontrado para a variavel {var}")


def buscar_aguardando_resposta_menu(aguardando_resposta):
    sql = "SELECT * FROM menu WHERE aguardando_resposta = %s"
    values = (aguardando_resposta,)

    mycursor.execute(sql, values)

    resultado = mycursor.fetchall()

    if resultado:
        for linha in resultado:
            print(linha[1])
            return linha[1]
    else:
        print(f"Nenhum dado encontrado para 'Aguardando Resposta' {aguardando_resposta}")


def buscar_form_preenchido_menu(form_preenchido):
    sql = "SELECT * FROM menu WHERE form_preenchido = %s"
    values = (form_preenchido,)

    mycursor.execute(sql, values)

    resultado = mycursor.fetchall()

    if resultado:
        for linha in resultado:
            print(linha[2])
            return linha[2]
    else:
        print(f"Nenhum dado encontrado para 'FormulÃ¡rio Preenchido' {form_preenchido}")


def obter_var_menu():
    mycursor.execute("SELECT var FROM menu WHERE var IS NOT NULL LIMIT 1")
    resultado = mycursor.fetchone()

    if resultado:
        return resultado[0]
    else:
        return None


def obter_aguardando_resposta_menu():
    mycursor.execute("SELECT aguardando_resposta FROM menu WHERE aguardando_resposta IS NOT NULL LIMIT 1")
    resultado = mycursor.fetchone()

    if resultado:
        return resultado[0]
    else:
        return None


def obter_form_preenchido_menu():
    mycursor.execute("SELECT form_preenchido FROM menu WHERE form_preenchido IS NOT NULL LIMIT 1")
    resultado = mycursor.fetchone()

    if resultado:
        return resultado[0]
    else:
        return None


def verificar_aguardando_resposta(numero):
    sql = "SELECT aguardando_resposta FROM menu WHERE numero = %s"
    values = (numero,)

    mycursor.execute(sql, values)
    resultado = mycursor.fetchone()

    if resultado:
        return resultado[0]
    else:
        return None


def verificar_form_preenchido(numero):
    sql = "SELECT form_preenchido FROM menu WHERE numero = %s"
    values = (numero,)

    mycursor.execute(sql, values)
    resultado = mycursor.fetchone()

    if resultado:
        return resultado[0]
    else:
        return None


def obter_var_numero(numero):
    sql = "SELECT var FROM menu WHERE numero = %s"
    values = (numero,)

    mycursor.execute(sql, values)
    resultado = mycursor.fetchone()

    if resultado:
        return resultado[0]
    else:
        return None


def adicionar_numero(numero):
    var = None
    aguardando_resposta = 0
    form_preenchido = 0

    sql = "INSERT INTO menu (numero, var, aguardando_resposta, form_preenchido) VALUES (%s, %s, %s, %s)"
    values = (numero, var, aguardando_resposta, form_preenchido)

    mycursor.execute(sql, values)
    mydb.commit()

    print(f"Numero {numero} adicionado com sucesso!")


def alterar_var_numero(numero, nova_var):
    sql = "UPDATE menu SET var = %s WHERE numero = %s"
    values = (nova_var, numero)

    mycursor.execute(sql, values)
    mydb.commit()

    print(f"Variavel do numero {numero} alterada para {nova_var}")


def alterar_aguardando_resposta_numero(numero, novo_aguardando_resposta):
    sql = "UPDATE menu SET aguardando_resposta = %s WHERE numero = %s"
    values = (novo_aguardando_resposta, numero)

    mycursor.execute(sql, values)
    mydb.commit()

    print(f"Aguardando Resposta do nÃºmero {numero} alterado para {novo_aguardando_resposta}")


def alterar_form_preenchido_numero(numero, novo_form_preenchido):
    sql = "UPDATE menu SET form_preenchido = %s WHERE numero = %s"
    values = (novo_form_preenchido, numero)

    mycursor.execute(sql, values)
    mydb.commit()

    print(f"Formulario Preenchido do numero {numero} alterado para {novo_form_preenchido}")


# Exemplo de uso
# numero_alterar_aguardando_resposta = 456  # Substitua pelo nÃºmero que deseja alterar
# novo_aguardando_resposta_valor = False
# alterar_aguardando_resposta_numero(numero_alterar_aguardando_resposta, novo_aguardando_resposta_valor)

# Exemplo de uso
# numero_alterar_var = 456  # Substitua pelo nÃºmero que deseja alterar
# nova_var_valor = "NovaVar"
# alterar_var_numero(numero_alterar_var, nova_var_valor)

# Exemplo de uso
# numero_alterar_form_preenchido = 456  # Substitua pelo nÃºmero que deseja alterar
# novo_form_preenchido_valor = True
# alterar_form_preenchido_numero(numero_alterar_form_preenchido, novo_form_preenchido_valor)

# Exemplo de uso
# numero_adicionar = 456  # Substitua pelo nÃºmero que deseja adicionar
# adicionar_numero(numero_adicionar)


# numero_procurado = 456  # Substitua pelo nÃºmero real que vocÃª estÃ¡ procurando
# print(verificar_aguardando_resposta(numero_procurado))
# print(verificar_form_preenchido(numero_procurado))
# print(obter_var_numero(numero_procurado))

# Exemplo de uso
# valor_var_menu = obter_var_menu()
# valor_aguardando_resposta = obter_aguardando_resposta_menu()
# valor_form_preenchido = obter_form_preenchido_menu()

# print(valor_var_menu)
# print(valor_aguardando_resposta)
# print(valor_form_preenchido)

# Exemplo de uso
# var_procurada = "ExemploVar"
# buscar_var_menu(var_procurada)

# aguardando_resposta_procurada = True
# buscar_aguardando_resposta_menu(aguardando_resposta_procurada)

# form_preenchido_procurado = False
# buscar_form_preenchido_menu(form_preenchido_procurado)

# Exemplo de uso
# var_menu = "ExemploVar"
# inserir_var_menu(var_menu)

# aguardando_resposta_menu = True
# inserir_aguardando_resposta_menu(aguardando_resposta_menu)

# form_preenchido_menu = False
# inserir_form_preenchido_menu(form_preenchido_menu)

mostrar_status_menu()
