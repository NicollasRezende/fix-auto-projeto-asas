from flask import Flask, request
import requests
from config_bot import (VERIFY_TOKEN,
                        WHATSAPP_TOKEN,
                        BASE_URL,
                        PAGE_ID,
                        saudacoes_portugues)
from menssages import Menus, MenuOptions, codigo_aleatorio
# from funcs import registrar_mensagem
from db import inserir_user, verificar_usuario, verificar_termos, atualizar_usuario, codigo_aleatorio_contrato, buscar_valor
import mysql.connector
from dbcfg import (adicionar_numero, 
                   obter_var_numero,
                   verificar_form_preenchido,
                   verificar_aguardando_resposta,
                   alterar_aguardando_resposta_numero,
                   alterar_form_preenchido_numero,
                   alterar_var_numero
                   )

clientes = []
cliente_encontrado = None
app = Flask(__name__)
mydb = mysql.connector.connect(
    host="localhost",
    password="!Senha123",
    user="root",
    database="chatbot2"
)


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


@app.route('/', methods=['GET'])
def verify_webhook():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Verificação falhou", 403


@app.route('/', methods=['POST'])
def receive_messages():
    data = request.get_json()

    numero_para_enviar = "556199831166"
    numero_comercial = "5561991769500"
    detalhes = None
    palavra_chave = codigo_aleatorio
    text = None
    name = None
    numero_user = None
    messagess = []
    user_name = []
    nome = None
    wa_id = None
    button_reply_id = None
    list_reply_id = None
    menu_atual = None
    global opcao_menu
    global equipe
    global aguardando_resposta
    aguardando_resposta = False
    global mensagem_usuario
    mensagem_usuario = None
    numero_contrato_cliente = None
    pronto = ["Pronto", "pronto", "Pronto.", "pronto."]
    tipo_menssagem = None

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

            if list_reply_id == 'VOLTAR':
                opcao_menu = 'voltar'
                alterar_var_numero(wa_id, "voltar")
                Menus.menu_inicial(wa_id, nome)

            if list_reply_id == 'SOBRE':
                opcao_menu = 'SOBRE'
                alterar_var_numero(wa_id, "sobre")
                enviar_msg(wa_id, "O *PROJETO ASAS*, iniciado em 2018, tem como objetivo promover qualidade de vida e bem-estar social por meio da prática regular de esportes.\n\nAtualmente, oferecemos gratuitamente treinos de vôlei de quadra, com planos de expandir para vôlei de praia, futsal, basquete e mais.\n\nContamos com quase *200 participantes* e buscamos parcerias para fortalecer o projeto.")
                Menus.menu_voltar(wa_id, name)
                alterar_var_numero(numero_user, "inicial")

            if list_reply_id == 'MISSAO':
                opcao_menu = 'MISSAO'
                alterar_var_numero(wa_id, "missao")
                enviar_msg(wa_id, "*Missão:* Promover qualidade de vida por meio de esportes.\n\n*Visão:* Formar bons cidadãos e atletas amadores/profissionais.\n\n*Valores:* Comprometimento, cooperação, respeito coletivo.\n\n")
                Menus.menu_voltar(wa_id, name)
                alterar_var_numero(numero_user, "inicial")

            if list_reply_id == 'METODO':
                opcao_menu = 'METODO'
                alterar_var_numero(wa_id, "metodo")
                enviar_msg(wa_id, "Nossa metodologia visa fortalecer a construção da cidadania e inclusão social através do esporte.\n\nNão há restrições de idade, mas menores de idade precisam de autorização dos pais.")
                Menus.menu_voltar(wa_id, name)
                alterar_var_numero(numero_user, "inicial")

            if list_reply_id == 'CONTATO':
                opcao_menu = 'CONTATO'
                alterar_var_numero(wa_id, "contato")
                enviar_msg(wa_id, "O siga o contato abaixo para entrar em contato com a nossa cordenação\n\nOu caso seja de sua preferencia nos envie um e-mail: asasvoleigama@gmail.com")
                Menus.enviar_contato(wa_id, 'Coordenação Geral', "552199999999")
                Menus.menu_voltar(wa_id, name)
                alterar_var_numero(numero_user, "inicial")

            if list_reply_id == 'CONTAT2':
                opcao_menu = 'MIDIAS'
                alterar_var_numero(wa_id, "midias")
                enviar_msg(wa_id, "Clique nos links abaixo para conhecer nossas *Midias Sociais*: ")
                Menus.enviar_link2(wa_id, "https://www.projetoasasgama.com.br",  "Nosso Site", "Clique no link abaixo para ser redirecionado ao nosso site:", "clique aqui")
                Menus.enviar_link2(wa_id, "https://www.youtube.com/@asasvoleigama",  "Nosso Canal do YouTube", "Clique no link abaixo para ser redirecionado ao nosso canal do YouTube:", "clique aqui")
                Menus.enviar_link2(wa_id, "hhttps://www.instagram.com/asasvoleigama?igsh=Mnh2ZHQxMjF2YnBm",  "Nosso Instagram", "Clique no link abaixo para ser redirecionado ao nosso Instagram:", "clique aqui")
                Menus.menu_voltar(wa_id, name)
                alterar_var_numero(numero_user, "inicial")

            if list_reply_id == 'TREINOS':
                opcao_menu = 'TREINOS'
                alterar_var_numero(wa_id, "treinos")
                enviar_msg(wa_id, "Todos os nossos treinos são gratuitos! Apareça nos treinos abertos ao público:\n\n  - Sábados das 8h às 12h no CÓSE Gama Leste\n\n   - Domingos das 9h às 12h no CEF 5 Gama Oeste\n\n  - Apresente-se ao condutor e recomendamos o pré-cadastro online.")
                Menus.enviar_loc(wa_id, "-16.012637467390302", "-48.04766338650559", "St. Leste EQ 8/10 Area Especial - Gama, Brasília - DF, 72450-085", "COSE-GAMA")
                Menus.menu_voltar(wa_id, name)

            if list_reply_id == 'PARTICIPAR':
                opcao_menu = 'PARTICIPAR'
                alterar_var_numero(wa_id, "participar")
                enviar_msg(wa_id, "Para participar de nossas atividades voce deve preencher o formulario abaixo, apos isso sera enviada uma confirmação.")
                Menus.enviar_link2(wa_id, "https://forms.gle/XCMhN6tt8rUd8x6X8", "LINK DO FORMULÁRIO DE CADASTRO ASAS", "Clique no link abaixo para ser redirecionado para o formulario de inscrição do nosso projeto", "clique aqui")
                enviar_msg(wa_id, 'Apos preencher o formulario digite "Pronto".')
                menu_atual = 'PRONTO'


            if list_reply_id == 'GALERIA':
                opcao_menu = 'GALERIA'
                alterar_var_numero(wa_id, "galeria")
                enviar_msg(wa_id, "Aqui estao alguns videos e imagens do nosso projeto:")
                Menus.enviar_imagem(wa_id, "/home/teletron/Área de Trabalho/project/bot/PROJETO/imagem_asas.jpeg")
                Menus.enviar_imagem(wa_id, "/home/teletron/Área de Trabalho/project/bot/PROJETO/escudo.jpeg")
                Menus.enviar_link2(wa_id, "https://www.instagram.com/asasvoleigama?igsh=Mnh2ZHQxMjF2YnBm", "NOTA DO DESENVOLVEDOR:", "Não tenho acesso ao *Drive*, entao coloquei o instagram...", "clique aqui")
                Menus.menu_voltar(wa_id, name)
                alterar_var_numero(numero_user, "inicial")

            if list_reply_id == 'DEPOIMENTO':
                opcao_menu = 'DEPOIMENTO'
                alterar_var_numero(wa_id, "depoimento")
                enviar_msg(wa_id, "Nota do desenvolvedor: Sem videos de depoimento...")
                Menus.menu_voltar(wa_id, name)
                alterar_var_numero(numero_user, "inicial")

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

        # VOLTAR/OCONTATO

        if button_reply_id == 'contato':
            opcao_menu = 'contato'
            alterar_var_numero(wa_id, "contato")
            Menus.enviar_contato(wa_id, "Coordenação Geral", "552199999999")
            Menus.enviar_link(wa_id, "https://www.projetoasasgama.com.br")
            alterar_var_numero(numero_user, "inicial")

        if button_reply_id == 'voltar':
            opcao_menu = 'inicial'
            alterar_var_numero(wa_id, "voltar")
            Menus.menu_inicial(wa_id, nome)

        # INFO GERAL

        if button_reply_id == 'INFO_GERAL':
            equipe = 'INFO_GERAL'
            opcao_menu = 'INFO_GERAL'
            alterar_var_numero(wa_id, "info_geral")
            Menus.menu_informacoes(wa_id, nome)
            alterar_var_numero(numero_user, "inicial")

        # SUPORTE E FEEDBACK

        if button_reply_id == 'SUPORTE':
            equipe = 'SUPORTE'
            opcao_menu = 'SUPORTE'
            alterar_var_numero(wa_id, "suporte_feedback")
            Menus.suporte_feedback(wa_id, nome)
            Menus.menu_voltar(wa_id, nome)
            alterar_var_numero(numero_user, "inicial")

        # MENUS ASAS

        if button_reply_id == 'PARTICIPAR':
            equipe = 'PARTICIPAR'
            opcao_menu = 'PARTICIPAR'
            alterar_var_numero(wa_id, "participar_menu")
            Menus.menu_participar(wa_id, nome)
            alterar_var_numero(numero_user, "inicial")

        if button_reply_id == 'DUVIDAS':
            equipe = 'DUVIDAS'
            opcao_menu = 'DUVIDAS'
            alterar_var_numero(wa_id, "duvidas")
            Menus.enviar_imagem(wa_id, "/home/teletron/Área de Trabalho/project/bot/PROJETO/duvidas1.jpeg")
            Menus.enviar_imagem(wa_id, "/home/teletron/Área de Trabalho/project/bot/PROJETO/duvidas2.jpeg")
            Menus.menu_voltar(wa_id, name)
            alterar_var_numero(numero_user, "inicial")

        if button_reply_id == 'FALE':
            equipe = 'FALE'
            opcao_menu = 'FALE'
            alterar_var_numero(wa_id, "fale")
            enviar_msg(wa_id, "Siga o contato abaixo para entrar em contato com a nossa cordenação\n\nOu envie-nos um e-mail: asasvoleigama@gmail.com")
            Menus.enviar_contato(wa_id, 'Coordenação Geral', "552199999999")
            Menus.menu_voltar(wa_id, name)

        if button_reply_id == 'OUVIDORIA':
            equipe = 'OUVIDORIA'
            opcao_menu = 'OUVIDORIA'
            alterar_var_numero(wa_id, "ouvidoria")
            alterar_aguardando_resposta_numero(wa_id, 1)
            enviar_msg(wa_id, "Deixe sua sugestão, opinião ou reclamação.\n\nGarantimos sigilo absoluto.\n\n")
            enviar_msg(wa_id, "Apos o envio, aguarde a confirmação.")
            Menus.menu_voltar(wa_id, name)
            alterar_var_numero(numero_user, "inicial")

        # TERMOS

        if button_reply_id == 'ACEITOU':
            atualizar_usuario(wa_id, "termos_aceitos", 1)
            MenuOptions.INICIAL
            alterar_var_numero(wa_id, "inicial")
            Menus.menu_inicial(wa_id, nome)
            alterar_var_numero(numero_user, "inicial")

        if button_reply_id == 'NEGOU':
            enviar_msg(
                wa_id, "Não será possivel prosseguir. Agradecemos seu contato!")
#            Menus.menu_privacidade(wa_id)

    except ValueError:
        pass

    try:
        messagess = data['entry'][0]['changes'][0]['value']['messages']
        user_name = data['entry'][0]['changes'][0]['value']['contacts']

        for entry in data['entry']:
            for change in entry['changes']:
                if 'value' in change and 'messages' in change['value']:
                    for message in change['value']['messages']:
                        message_type = message.get('type')
                        if message_type:
                            print("Type of message:", message_type)

        for entry in data['entry']:
            for change in entry['changes']:
                if 'value' in change and 'contacts' in change['value']:
                    for contact in change['value']['contacts']:
                        if 'wa_id' in contact:
                            numero_user = contact['wa_id']
                            break

        for entry in data['entry']:
            for change in entry['changes']:
                if 'value' in change and 'messages' in change['value']:
                    for message in change['value']['messages']:
                        if message['type'] == 'image':
                            enviar_msg(numero_user, "Infelizmente nao pude indentificar sua mensagem, por favor envie-nos uma menssagem de texto.")
                            alterar_var_numero(wa_id, "inicial")
                        if message['type'] == 'video':
                            enviar_msg(numero_user, "Infelizmente nao pude indentificar sua mensagem, por favor envie-nos uma menssagem de texto.")
                            alterar_var_numero(wa_id, "inicial")
                        if message['type'] == 'audio':
                            enviar_msg(numero_user, "Infelizmente nao pude indentificar sua mensagem, por favor envie-nos uma menssagem de texto.")
                            alterar_var_numero(wa_id, "inicial")

        for user in user_name:
            name = user['profile']['name']

        for messaging in messagess:
            text = messaging['text']['body']
            numero_user = messaging['from']

            if obter_var_numero(numero_user) == "inicial":
                if text:
                    opcao_menu = 'inicial'
                    numero_user = numero_user
                    text = text
                    if verificar_usuario(numero_user):
                        print("passou")
                        if verificar_termos(numero_user) == 1:
                            print("passou1")
                            MenuOptions.INICIAL
                            alterar_var_numero(wa_id, "inicial")
                            Menus.menu_inicial(numero_user, name)
                        if not verificar_termos(numero_user):
                            Menus.menu_privacidade(numero_user)
                    else:
                        adicionar_numero(numero_user)
                        inserir_user(name, numero_user,
                                     codigo_aleatorio_contrato, 0)
                        alterar_var_numero(wa_id, "privacidade")
                        Menus.menu_privacidade(numero_user)

            if text == "enviar_doc":
                opcao_menu = 'inicial'
                alterar_var_numero(wa_id, "inicial")
                numero_user = numero_user
                text = text
                Menus.enviar_documento(
                    numero_user, "/home/teletron/Área de Trabalho/project/bot/PROJETO/ASAS-CAMISETA-PASSEIO.pdf", "camisetas", "application/pdf")

            if text == "enviar_img":
                opcao_menu = 'inicial'
                alterar_var_numero(wa_id, "inicial")
                numero_user = numero_user
                text = text
                Menus.enviar_imagem(
                    numero_user, "/home/teletron/Área de Trabalho/project/bot/PROJETO/imagem_asas.jpeg")

            if text == "enviar_vdo":
                opcao_menu = 'inicial'
                alterar_var_numero(wa_id, "inicial")
                numero_user = numero_user
                text = text
                Menus.enviar_video(
                    numero_user, "/home/teletron/Área de Trabalho/project/bot/PROJETO/video_asas.mp4")

            if text == "enviar_aud":
                opcao_menu = 'inicial'
                alterar_var_numero(wa_id, "inicial")
                numero_user = numero_user
                text = text
                Menus.enviar_audio(
                    numero_user, "/home/teletron/Área de Trabalho/project/bot/PROJETO/audio_asas.mpeg", "audio/mpeg")

            if text == "enviar_link":
                # opcao_menu == "inicial"
                numero_user == numero_user
                text = text
                Menus.enviar_link2(numero_user, "https://forms.gle/XCMhN6tt8rUd8x6X8", "Formulario", "Clique no link abaixo para acessar o formulario de inscrição", "clique aqui" )

            if text in pronto:
                if obter_var_numero(numero_user) == "participar":
                    numero_user = numero_user
                    text = text
                    enviar_msg(wa_id, f"Considere-se acolhido(a) {nome}, e desejamos que você se sinta bem entre nós, que faça parte das nossas vivências, que encontre oportunidades e condições de aprender e crescer.\n\nEsperamos sinceramente que a sua experiência conosco seja excelente e duradoura.\n\nSinta-se muito bem-vindo(a)!\n\nDivulgue o *PROJETO ASAS!*\n\nSiga-nos, curta e compartilhe nossas mídias sociais (@asasvoleigama). Se preferir, contate-nos por telefone (6121951085) ou envie-nos um e-mail (asasvoleigama@gmail.com).\n\n\n*#SomosTodosASAS*")
                    Menus.enviar_imagem(wa_id, "/home/teletron/Área de Trabalho/project/bot/PROJETO/escudo.jpeg")
                    enviar_msg(wa_id, "Caso não tenha baixado o termo de uso de imagem acesse o link abaixo, imprima, preencha e entregue-nos quando vier participar de nossas atividades")
                    Menus.enviar_link2(wa_id, "https://docs.google.com/document/d/1O9ulUP6yCmil8-i_7tHi9lBGJGN0vLMg/edit", "Termo de uso de imagem", "Clique no link abaixo para poder ter acesso ao documento:", "clique aqui")
                    enviar_msg(wa_id, "Nos encontre aqui:")
                    Menus.enviar_loc(wa_id, "-16.012637467390302", "-48.04766338650559", "St. Leste EQ 8/10 Area Especial - Gama, Brasília - DF, 72450-085", "COSE-GAMA")
                    Menus.menu_voltar(wa_id, name)
                    enviar_msg(numero_para_enviar, f"\nO usuario: {name}\n\nnumero: {numero_user}\n\nPreencheu o formulario de inscrição.")
                    Menus.enviar_contato(numero_para_enviar, name, numero_user)
                    alterar_var_numero(numero_user, "inicial")

            if text:
                if obter_var_numero(numero_user) == "ouvidoria":
                    if verificar_aguardando_resposta(numero_user) == 1:
                        numero_contrato_cliente = buscar_valor(
                            wa_id, "numero_contrato")
                        detalhes = text
                        enviar_msg(
                            numero_para_enviar, f"\nO usuario: {name}\n\nnumero: {numero_user}\n\ncontrato: {numero_contrato_cliente}\n\requisitou a opçao ouvidoria os detalhes da mensagem enviada estão logo a baixo:\n\n {detalhes}\n\n")
                        Menus.enviar_contato(numero_para_enviar, name, numero_user)
                        Menus.menu_voltar_suporte2(numero_user)
                        alterar_aguardando_resposta_numero(numero_user, 0)
                        alterar_var_numero(numero_user, "inicial")

        print("_________________________________________")
        print("Recebido POST do Usuario:")
        print("USUARIO DIGITOU", text)
        print("NOME':", name)
        print("NUMERO", numero_user)
        print("_________________________________________")

    except (KeyError):
        pass

    try:

        if menu_atual == MenuOptions.INICIAL:
            Menus.menu_inicial(numero_user, name)
    except UnboundLocalError:
        pass
    except requests.exceptions.RequestException as e:
        print(f"Erro ao enviar mensagem: {e}")

    return "OK"


if __name__ == '__main__':
    app.run(debug=True, port=5000)
