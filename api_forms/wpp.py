from flask import Flask, request
import requests
from config_bot import (VERIFY_TOKEN,
                        WHATSAPP_TOKEN,
                        BASE_URL,
                        PAGE_ID,
                        )
# from funcs import registrar_mensagem
import mysql.connector

clientes = []
cliente_encontrado = None
app = Flask(__name__)
mydb = mysql.connector.connect(
    host="localhost",
    password="!Senha123",
    user="root",
    database="chatbot2"
)


@app.route('/', methods=['GET'])
def verify_webhook():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Verificação falhou", 403


@app.route('/', methods=['POST'])
def receive_messages():
    data = request.get_json()

    text = None
    name = None
    numero_user = None
    messagess = []
    user_name = []
    nome = None
    wa_id = None
    button_reply_id = None
    list_reply_id = None
    global opcao_menu
    global equipe
    global aguardando_resposta
    global mensagem_usuario
    mensagem_usuario = None

# MENU LISTA

    try:

        for entry in data['entry']:
            for change in entry['changes']:
                if 'value' in change and 'contacts' in change['value']:
                    for contact in change['value']['contacts']:
                        if 'profile' in contact and 'name' in contact['profile']:
                            nome = contact['profile']['name']
                        if 'wa_id' in contact:
                            wa_id = contact['wa_id']

        for entry in data['entry']:
            for change in entry['changes']:
                if 'value' in change and 'messages' in change['value']:
                    for message in change['value']['messages']:
                        if 'interactive' in message and 'list_reply' in message['interactive']:
                            list_reply = message['interactive']['list_reply']
                            if list_reply['id']:
                                list_reply_id = list_reply['id']
                                break

# RESPOSTAS MENU LISTA

        try:

            print("_________________________________________")
            print("Recebido POST das Opçoes:")
            print("USUARIO SELECIONOU", list_reply_id)
            print("NOME:", nome)
            print("NUMERO:", wa_id)
            print("_________________________________________")
        except UnboundLocalError:
            pass

    except ValueError:
        pass

# MENU BOTAO

    try:

        for entry in data['entry']:
            for change in entry['changes']:
                if 'value' in change and 'contacts' in change['value']:
                    for contact in change['value']['contacts']:
                        if 'profile' in contact and 'name' in contact['profile']:
                            nome = contact['profile']['name']
                        if 'wa_id' in contact:
                            wa_id = contact['wa_id']

        for entry in data['entry']:
            for change in entry['changes']:
                if 'value' in change and 'messages' in change['value']:
                    for message in change['value']['messages']:
                        if 'interactive' in message and 'button_reply' in message['interactive']:
                            button_reply = message['interactive']['button_reply']
                            if button_reply['id']:
                                button_reply_id = button_reply['id']
                                break

    except ValueError:
        pass

    try:
        messagess = data['entry'][0]['changes'][0]['value']['messages']
        user_name = data['entry'][0]['changes'][0]['value']['contacts']

        for user in user_name:
            name = user['profile']['name']

        for messaging in messagess:
            text = messaging['text']['body']
            numero_user = messaging['from']

        print("_________________________________________")
        print("Recebido POST do Usuario:")
        print("USUARIO DIGITOU", text)
        print("NOME':", name)
        print("NUMERO", numero_user)
        print("_________________________________________")

    except (KeyError):
        pass

    return "OK"


def enviar_msg(numero, mensagem):

    url = f"{BASE_URL}/{PAGE_ID}/messages"

    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "text",
        "text": {"body": mensagem}
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        return response
    except requests.exceptions.RequestException as e:
        print(f"Erro ao enviar mensagem: {e}")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
