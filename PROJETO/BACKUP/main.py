from flask import Flask, request
import requests
from config_bot import (VERIFY_TOKEN,
                        WHATSAPP_TOKEN,
                        BASE_URL,
                        PAGE_ID,
                        )
from menssages import Menus, MenuOptions
# from funcs import registrar_mensagem
from db import inserir_user, verificar_usuario, verificar_termos, atualizar_usuario, codigo_aleatorio_contrato, buscar_valor
import mysql.connector
from dbcfg import (adicionar_numero,
                   obter_var_numero,
                   verificar_aguardando_resposta,
                   alterar_aguardando_resposta_numero,
                   alterar_var_numero
                   )
import datetime
from dbcfg import (obter_horario1, obter_horario2)
from dbcfg import (session_timeout_set,
                   session_timeout_view,
                   atualizar_horario_atual_com_relogio,
                   obter_horario_atual)
from db import session_timeout_set_db, session_timeout_view_db
import time

horario_atual = datetime.datetime.now()
horario_formatado = horario_atual.strftime("Dia:%d.%m.%y/Hora:%H:%M")

clientes = []
cliente_encontrado = None
app = Flask(__name__)
mydb = mysql.connector.connect(
    host="localhost",
    password="!Senha123",
    user="root",
    database="chatbot_asas"
)


hora_inicio = obter_horario1()
hora_final = obter_horario2()


def horario_comercial():
    if horario_atual.weekday() in range(0, 5):
        if hora_inicio <= horario_atual.hour < hora_final:
            return True
    return False


@app.route('/', methods=['GET'])
def verify_webhook():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Verificação falhou", 403


@app.route('/', methods=['POST'])
def receive_messages():
    data = request.get_json()

    numero_para_enviar = "556121951085"
    comunicacao = "556121951087"
    secretaria = "556121951086"
    abraao = "55999831166"
    detalhes = None
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
    aguardando_resposta = False
    global mensagem_usuario
    mensagem_usuario = None
    pronto = ["Pronto", "pronto", "Pronto.", "pronto."]
    hora_inicio = obter_horario1()
    hora_final = obter_horario2()
    lista_menus = ["participar", "ouvidoria", ""]

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
                opcao_menu = 'inicial'
                alterar_var_numero(wa_id, "inicial")
                Menus.menu_inicial(wa_id, nome)
                alterar_var_numero(wa_id, "inicial")

            if list_reply_id == 'SOBRE':
                opcao_menu = 'SOBRE'
                alterar_var_numero(wa_id, "sobre")
                enviar_msg(wa_id, "*SOBRE O PROJETO*\n\n*PROJETO SOCIAL* de iniciativa privada, sem fins monetários lucrativos e voltado para a comunidade local e região metropolitana.\n\nO *PROJETO ASAS*, iniciado em 2018, tem como objetivo promover qualidade de vida e bem-estar social através da prática regular de esportes coletivos ou individuais.\n\nOferecemos gratuitamente treinos de vôlei de quadra, com planos de estender para vôlei de praia, futsal, basquete, entre outros.\n\nAtualmente contamos com aproximadamente *duzentos participantes*, jovens de todas as idades e buscamos parcerias para fortalecer o *PROJETO* através de contribuições voluntárias em quaisquer valores, com prestação mensal de contas para todos os envolvidos direta ou indiretamente com o *PROJETO ASAS.*")
                Menus.submenu_voltar(wa_id, name)

            if list_reply_id == 'MISSAO':
                opcao_menu = 'MISSAO'
                alterar_var_numero(wa_id, "missao")
                enviar_msg(wa_id, "*MISSÃO, VISÃO E VALORES*\n\n*Nossa MISSÃO:* Promover qualidade de vida através da prática regular de esportes coletivos ou individuais.\n\n*Nossa VISÃO:* Formar bons cidadãos e cidadãs, atletas amadores e profissionais.\n\n*Nossos VALORES:* Comprometimento, cooperação e respeito coletivo.")
                Menus.submenu_voltar(wa_id, name)

            if list_reply_id == 'METODO':
                opcao_menu = 'METODO'
                alterar_var_numero(wa_id, "metodo")
                enviar_msg(wa_id, "*NOSSA METODOLOGIA*\n\n_Nossa metodologia baseia-se no princípio de fortalecimento da *PRÁTICA* diretamente alinhada à *TEORIA*, onde os iniciantes em nossas atividades estudam e aprendem as regras, normativas e exigências de cada esporte, aplicando-as em nossos treinos técnicos e táticos, com a repetição necessária em cada uma das etapas neste processo. Alinhado a tudo isso, buscamos fortalecer o comprometimento, o empenho, o foco, a dedicação, a aplicação e o coletivismo na formação das equipes, agregando valores, formando pessoas de bem e abraçando a inclusão social através do esporte, pois acolhemos jovens a partir de doze anos, sempre com autorização e acompanhamento dos pais ou responsáveis. Atualmente participam de nossas atividades alguns jovens da *MELHOR IDADE* com mais de cinquenta anos._")
                Menus.submenu_voltar(wa_id, name)

            if list_reply_id == 'CONTATO':
                opcao_menu = 'CONTATO'
                alterar_var_numero(wa_id, "contato")
                enviar_msg(wa_id, "- Encaminharemos a seguir os contatos institucionais do *PROJETO ASAS* para que possam entrar em contato com nossos setores:\n\n - Coordenação\n - Secretaria\n - Comunicação Social\n - Financeiro\n - Patrimônio\n\n- Envie-nos e-mail: asasvoleigama@gmail.com\n\n- Se preferir, ligue-nos a partir de um telefone fixo ou móvel para este contato ou quaisquer dos contatos listados abaixo, você será atendido em nossa *Central de Atendimento Automático* com *URA* _(Unidade de Resposta Audível)_:")
                Menus.enviar_contato(wa_id, 'ASAS - Coordenação Geral', "556121951085")
                Menus.enviar_contato(wa_id, 'ASAS - Secretaria', "556121951086")
                Menus.enviar_contato(wa_id, 'ASAS - Comunicação Social', "556121951087")
                Menus.enviar_contato(wa_id, 'ASAS - Financeiro', "556121951088")
                Menus.enviar_contato(wa_id, 'ASAS - Patrimônio', "556121951089")
                Menus.submenu_voltar(wa_id, name)

            if list_reply_id == 'CONTAT2':
                opcao_menu = 'MIDIAS'
                alterar_var_numero(wa_id, "midias")
                enviar_msg(wa_id, "Clique nos links abaixo para conhecer nossas *Midias Sociais*: ")
                Menus.enviar_link2(wa_id, "https://www.projetoasasgama.com.br", "Site Projeto ASAS", "Clique no link abaixo para ser redirecionado ao nosso *site:*", "clique aqui")
                Menus.enviar_link2(wa_id, "https://www.youtube.com/@asasvoleigama", "Canal do YouTube", "Clique no link abaixo para ser redirecionado ao nosso *YouTube:*", "clique aqui")
                Menus.enviar_link2(wa_id, "https://www.instagram.com/asasvoleigama?igsh=Mnh2ZHQxMjF2YnBm", "Instagram", "Clique no link abaixo para ser redirecionado ao nosso *Instagram:*", "clique aqui")
                Menus.submenu_voltar(wa_id, name)

            if list_reply_id == 'TREINOS':
                opcao_menu = 'TREINOS'
                alterar_var_numero(wa_id, "treinos")
                enviar_msg(wa_id, '_Todos os nossos treinos são gratuitos e, para participar ou conhecer nossa metodologia, basta comparecer em quaisquer de nossos treinos abertos ao público geral e apresentar-se ao treinador, condutor ou coordenador sempre presentes nestes, nos locais e horários listados abaixo:_\n\n- Na *Escola Classe 15*, localizada no Setor Norte, próxima ao Corpo de Bombeiros, atrás do Supermercado Condor - Aos sábados das 8h ao meio-dia;\n\n- No *CEF 05* - Gama Oeste - Aos domingos das 8h ao meio-dia;\n\n_Caso queira continuar participando, será necessária a realização de um pré-cadastro online. Para mais informações, retorne ao menu anterior e selecione *Como Participar*._')
                Menus.enviar_loc(wa_id, "-16.00363263265545", "-48.06105367603416", "Setor Norte, Quadra 02 - Área Especial - Gama, Brasília - DF, 72430-230", "EC15-GAMA")
                Menus.enviar_loc(wa_id, "-16.0153709486732", "-48.07848496320848", "Setor Oeste, E/Q 26/29 - Gama, Brasília - DF, 72420-265", "CEF05-GAMA")
                Menus.submenu_voltar(wa_id, name)

            if list_reply_id == 'PARTICIPAR':
                opcao_menu = 'PARTICIPAR'
                alterar_var_numero(wa_id, "participar")
                enviar_msg(wa_id, "*COMO PARTICIPAR*\n\n- Para continuar participando de nossos treinos gratuitos e abertos à comunidade, por questões de controle, melhor gestão e visando melhorias e manutenção na qualidade destes treinos, será necessário preencher nosso formulário de cadastro online no link a seguir.\n\n- Assim que recebermos a confirmação do preenchimento, para um melhor acompanhamento de nossos informativos e comunicados, você será adicionado(a) no grupo de *INTEGRANTES* oficial do *PROJETO ASAS*.")
                Menus.enviar_link2(wa_id, "https://forms.gle/XCMhN6tt8rUd8x6X8", "Formulário de Inscrição", "Para acessar o nosso Formulário de Inscrição e cadastrar-se no PROJETO, clique no link abaixo:", "clique aqui")
                enviar_msg(wa_id, 'Após preencher o formulário, retorne a essa mensagem e digite "Pronto".')

            if list_reply_id == 'GALERIA':
                opcao_menu = 'GALERIA'
                alterar_var_numero(wa_id, "galeria")
                enviar_msg(wa_id, "Aqui estão alguns vídeos e imagens do nosso projeto:")
                Menus.enviar_imagem(wa_id, "/home/teletron/Área de Trabalho/project/bot/PROJETO/imagens-depoimentos/imagem1.jpeg")
                Menus.enviar_imagem(wa_id, "/home/teletron/Área de Trabalho/project/bot/PROJETO/imagens-depoimentos/imagem2.jpeg")
                # imagem a adicionar: Menus.enviar_imagem(wa_id, "/home/teletron/Área de Trabalho/project/bot/PROJETO/imagens-depoimentos/imagem3.jpeg")
                Menus.enviar_link2(wa_id, "https://www.instagram.com/asasvoleigama?igsh=Mnh2ZHQxMjF2YnBm", "FOTOS E VIDEOS", "Opção em *DESENVOLVIMENTO*. Em breve teremos novidades!", "clique aqui")
                Menus.submenu_voltar(wa_id, name)

            if list_reply_id == 'DEPOIMENTO':
                opcao_menu = 'DEPOIMENTO'
                alterar_var_numero(wa_id, "depoimento")
                # imagem a adicionar: Menus.enviar_imagem(wa_id, "/home/teletron/Área de Trabalho/project/bot/PROJETO/imagens-depoimentos/imagem3.jpeg")
                enviar_msg(wa_id, "Opção em *DESENVOLVIMENTO*.\n\n- Em breve disponibilizaremos alguns depoimentos dos integrantes do *PROJETO ASAS*")
                Menus.submenu_voltar(wa_id, name)

            if list_reply_id == "INVISTA":
                alterar_var_numero(wa_id, "investir")
                enviar_msg(wa_id, "Opção em *DESENVOLVIMENTO*.\n\nSaiba como fortalecer nosso propósito.\n\nApoie, invista ou patrocine o *PROJETO ASAS*.\n\nAdote um *INICIANTE* com contribuições voluntárias e regulares a partir de *R$ 1,00*.\n\nPara mais informações clique no link abaixo e fale com nosso *Financeiro:*\n\n- wa.me/556121951088.")
                Menus.submenu_voltar(wa_id, "user")

            if list_reply_id == "muito_bom":
                alterar_var_numero(wa_id, "inicial")
                enviar_msg(wa_id, "Ficamos felizes com sua avaliação e agradecemos seu feedback positivo!\n\nSalve este contato em sua agenda e envie-nos um *oi* sempre que precisar.\n\nAtendimento encerrado. Até logo!")
                enviar_msg(numero_para_enviar, f"Nosso atendimento foi avaliado como:\n\n- *Muito BOM!*")
                Menus.enviar_contato(numero_para_enviar, name, numero_user)


            if list_reply_id == "bom":
                alterar_var_numero(wa_id, "inicial")
                enviar_msg(wa_id, "Que bom, agradecemos seu feedback positivo!\n\nSalve este contato em sua agenda e envie-nos um *oi* sempre que precisar.\n\nAtendimento encerrado. Até logo!")
                enviar_msg(numero_para_enviar, f"Nosso atendimento foi avaliado como:\n\n- *BOM!*")
                Menus.enviar_mensagem_template2(numero_para_enviar, nome, "(Bom)")


            if list_reply_id == "mediano":
                alterar_var_numero(wa_id, "inicial")
                enviar_msg(wa_id, "Agradecemos seu feedback!\n\nEstamos apenas no começo e saiba que não mediremos esforços para melhorar nosso atendimento. Envie-nos um *oi* sempre que precisar.\n\nAtendimento encerrado. Até logo!")
                enviar_msg(numero_para_enviar, f"Nosso atendimento foi avaliado como:\n\n- *Mediano!*")
                Menus.enviar_mensagem_template2(numero_para_enviar, nome, "(Mediano)")

            if list_reply_id == "ruim":
                alterar_var_numero(wa_id, "inicial")
                enviar_msg(wa_id, "Agradecemos seu feedback e lamentamos profundamente não conseguir lhe atender plenamente.\n\nSaiba que não mediremos esforços na busca por melhorias neste canal de atendimento e em todos os demais meios de comunicação com o *PROJETO ASAS*.\n\nSalientamos que temos uma Ouvidoria à sua disposição.\n\nAtendimento encerrado!")
                enviar_msg(numero_para_enviar, f"Nosso atendimento foi avaliado como:\n\n- *RUIM!*")
                Menus.enviar_mensagem_template2(numero_para_enviar, nome, "(Ruim)")

            if list_reply_id == "pessimo":
                alterar_var_numero(wa_id, "inicial")
                enviar_msg(wa_id, "Agradecemos seu feedback e lamentamos profundamente não conseguir lhe atender plenamente.\n\nEstamos apenas no começo e saiba que não mediremos esforços para melhorar nosso atendimento neste e em todos os demais meios de comunicação com o *PROJETO ASAS*.\n\nSalientamos que temos uma *OUVIDORIA* à sua disposição.\n\nEsperamos lhe atender melhor em outra oportunidade, portanto, envie-nos um *oi* sempre que precisar.\n\nAtendimento encerrado!")
                enviar_msg(numero_para_enviar, f"Nosso atendimento foi avaliado como:\n\n- *PÉSSIMO!*\n\nRecomendamos acompanhar esse atendimento, identificar as falhas e buscar reverter essa avaliação.")
                Menus.enviar_mensagem_template2(numero_para_enviar, nome, "(Pessimo)")

            if list_reply_id == "encerrar":
                alterar_var_numero(wa_id, "inicial")
                Menus.menu_avaliacao(wa_id, "user")

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
            enviar_msg(wa_id, "- Encaminharemos a seguir os contatos institucionais do *PROJETO ASAS* para que possam entrar em contato com nossos setores:\n\n - Coordenação\n - Secretaria\n - Comunicação Social\n - Financeiro\n - Patrimônio\n\n- Envie-nos e-mail: asasvoleigama@gmail.com\n\n- Se preferir, ligue-nos a partir de um telefone fixo ou móvel para este contato ou quaisquer dos contatos listados abaixo, você será atendido em nossa *Central de Atendimento Automático* com *URA* _(Unidade de Resposta Audível)_:")
            Menus.enviar_contato(wa_id, 'ASAS - Coordenação Geral', "556121951085")
            Menus.enviar_contato(wa_id, 'ASAS - Secretaria', "556121951086")
            Menus.enviar_contato(wa_id, 'ASAS - Comunicação Social', "556121951087")
            Menus.enviar_contato(wa_id, 'ASAS - Financeiro', "556121951088")
            Menus.enviar_contato(wa_id, 'ASAS - Patrimônio', "556121951089")
            Menus.enviar_link(wa_id, "https://www.projetoasasgama.com.br")
            alterar_var_numero(numero_user, "inicial")
            Menus.menu_voltar(wa_id, name)

        if button_reply_id == 'voltar':
            opcao_menu = 'inicial'
            alterar_var_numero(wa_id, "inicial")
            Menus.menu_inicial(wa_id, nome)
            alterar_var_numero(wa_id, "inicial")

        if button_reply_id == 'voltar2':
            if obter_var_numero(wa_id) == "sobre":
                alterar_var_numero(wa_id, "inicial")
                Menus.menu_informacoes(wa_id, nome)

            if obter_var_numero(wa_id) == 'missao':
                alterar_var_numero(wa_id, "inicial")
                Menus.menu_informacoes(wa_id, name)

            if obter_var_numero(wa_id) == 'metodo':
                alterar_var_numero(wa_id, "inicial")
                Menus.menu_informacoes(wa_id, name)

            if obter_var_numero(wa_id) == 'contato':
                alterar_var_numero(wa_id, "inicial")
                Menus.menu_informacoes(wa_id, name)

            if obter_var_numero(wa_id) == 'midias':
                alterar_var_numero(wa_id, "inicial")
                Menus.menu_informacoes(wa_id, name)

        if button_reply_id == 'voltar2':
            if obter_var_numero(wa_id) == 'duvidas':
                alterar_var_numero(wa_id, "inicial")
                Menus.suporte_feedback(wa_id, name)
                Menus.menu_voltar(wa_id, nome)

            if obter_var_numero(wa_id) == 'fale':
                alterar_var_numero(wa_id, "inicial")
                Menus.suporte_feedback(wa_id, name)
                Menus.menu_voltar(wa_id, nome)

            if obter_var_numero(wa_id) == 'ouvidoria':
                alterar_var_numero(wa_id, "inicial")
                Menus.suporte_feedback(wa_id, name)
                Menus.menu_voltar(wa_id, nome)

        if button_reply_id == 'voltar2':
            if obter_var_numero(wa_id) == 'treinos':
                alterar_var_numero(wa_id, "inicial")
                Menus.menu_participar(wa_id, name)

            if obter_var_numero(wa_id) == 'participar':
                alterar_var_numero(wa_id, "inicial")
                Menus.menu_participar(wa_id, name)

            if obter_var_numero(wa_id) == 'galeria':
                alterar_var_numero(wa_id, "inicial")
                Menus.menu_participar(wa_id, name)

            if obter_var_numero(wa_id) == 'investir':
                alterar_var_numero(wa_id, "inicial")
                Menus.menu_participar(wa_id, name)

            if obter_var_numero(wa_id) == 'depoimento':
                alterar_var_numero(wa_id, "inicial")
                Menus.menu_participar(wa_id, name)

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

        if button_reply_id == 'DUVIDAS':
            equipe = 'DUVIDAS'
            opcao_menu = 'DUVIDAS'
            alterar_var_numero(wa_id, "duvidas")
            Menus.enviar_imagem(wa_id, "/home/teletron/Área de Trabalho/project/bot/PROJETO/duvidas1.jpeg")
            Menus.enviar_imagem(wa_id, "/home/teletron/Área de Trabalho/project/bot/PROJETO/duvidas2.jpeg")
            Menus.submenu_voltar(wa_id, name)

        if button_reply_id == 'FALE':
            equipe = 'FALE'
            opcao_menu = 'FALE'
            alterar_var_numero(wa_id, "fale")
            enviar_msg(wa_id, "- Encaminharemos a seguir os contatos institucionais do *PROJETO ASAS* para que possam entrar em contato com nossos setores:\n\n - Coordenação\n - Secretaria\n - Comunicação Social\n - Financeiro\n - Patrimônio\n\n- Envie-nos e-mail: asasvoleigama@gmail.com\n\n- Se preferir, ligue-nos a partir de um telefone fixo ou móvel para este contato ou quaisquer dos contatos listados abaixo, você será atendido em nossa *Central de Atendimento Automático* com *URA* _(Unidade de Resposta Audível)_:")
            Menus.enviar_contato(wa_id, 'ASAS - Coordenação Geral', "556121951085")
            Menus.enviar_contato(wa_id, 'ASAS - Secretaria', "556121951086")
            Menus.enviar_contato(wa_id, 'ASAS - Comunicação Social', "556121951087")
            Menus.enviar_contato(wa_id, 'ASAS - Financeiro', "556121951088")
            Menus.enviar_contato(wa_id, 'ASAS - Patrimônio', "556121951089")
            Menus.submenu_voltar(wa_id, name)

        if button_reply_id == 'OUVIDORIA':
            equipe = 'OUVIDORIA'
            opcao_menu = 'OUVIDORIA'
            alterar_var_numero(wa_id, "ouvidoria")
            enviar_msg(wa_id, "*OUVIDORIA*\n\nEnvie-nos uma mensagem com sua denuncia, dúvida, opinião, sugestão ou reclamação.\n\nGarantimos sigilo absoluto na condução das tratativas.")
            enviar_msg(wa_id, "Se preferir, ligue a partir de um telefone fixo ou móvel para quaisquer dos contatos institucionais do *PROJETO*. Você será atendido(a) em nossa nossa *Central de Atendimento Automático* através de uma *URA* _(Unidade de Resposta Audível)_.\n\nNavegue nas opções do prompt de atendimento para esclarecer dúvidas ou digite/tecle 6 (seis) e envie-nos uma mensagem de voz com sua denúncia, dúvida, reclamação ou sugestão.\n\nSaiba que neste canal de atendimento garantimos sigilo absoluto na condução das tratativas.")
            enviar_msg(wa_id, "Após o envio, aguarde a confirmação.")
            Menus.submenu_voltar(wa_id, name)

        # TERMOS

        if button_reply_id == 'ACEITOU':
            inserir_user(nome, wa_id, codigo_aleatorio_contrato, 0)
            atualizar_usuario(wa_id, "termos_aceitos", 1)
            alterar_var_numero(wa_id, "inicial")
            alterar_var_numero(numero_user, "inicial")
            Menus.menu_inicial(wa_id, nome)

        if button_reply_id == 'NEGOU':
            enviar_msg(
                wa_id, "Não será possivel prosseguir. Agradecemos seu contato!")
#            Menus.menu_privacidade(wa_id)

        if button_reply_id == 'encerrar':
            Menus.menu_avaliacao(wa_id, "user")
            alterar_var_numero(wa_id, "inicial")

        if button_reply_id == 'continuar':
            alterar_var_numero(wa_id, "inicial")
            Menus.menu_inicial(wa_id, "user")

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

        if text:
            if obter_var_numero(wa_id) not in lista_menus:
                alterar_var_numero(wa_id, "inicial")
            atualizar_horario_atual_com_relogio()
            print(obter_horario_atual())

        if text:
            horario_atual = datetime.datetime.now()
            horario_formatado = horario_atual.strftime("Dia:%d.%m.%y/Hora:%H:%M")
            print(horario_formatado)
            if verificar_usuario(numero_user):
                pass
            else:
                adicionar_numero(numero_user)
                alterar_var_numero(numero_user, "inicial")

            if verificar_usuario(numero_user):
                print(obter_var_numero(numero_user))
                if obter_var_numero(numero_user) == "inicial":
                    numero_user = numero_user
                    opcao_menu = 'inicial'
                    numero_user = numero_user
                    text = text
                    if verificar_termos(numero_user) == 1:
                        alterar_var_numero(wa_id, "inicial")
                        Menus.menu_inicial(numero_user, name)
            else:
                Menus.menu_privacidade(numero_user)

            if text == "#sair":
                opcao_menu = "inicial"
                alterar_var_numero(wa_id, "inicial")
                enviar_msg(wa_id, "Finalizando atendimento...")

            if text == "enviar_doc":
                opcao_menu = 'inicial'
                alterar_var_numero(wa_id, "inicial")
                numero_user = numero_user
                text = text
                Menus.enviar_documento(
                    numero_user, "/home/teletron/Área de Trabalho/project/bot/PROJETO/ASAS-CAMISETA-PASSEIO.pdf", "camisetas", "application/pdf")

            if text == "enviar_temp":
                opcao_menu = 'inicial'
                alterar_var_numero(wa_id, "inicial")
                numero_user = numero_user
                text = text
                enviar_msg(wa_id, "Recebendo request de usuario...")
                Menus.enviar_mensagem_template2(numero_user, nome, f"O usuário: {nome}, número: {numero_user}. Preencheu o cadastro no Formulário de Inscrições do PROJETO ASAS.")

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
                Menus.enviar_link2(numero_user, "https://forms.gle/XCMhN6tt8rUd8x6X8", "Formulário", "Clique no link abaixo para acessar o formulário de inscrição", "clique aqui" )

            if text in pronto:
                if obter_var_numero(numero_user) == "participar":
                    numero_user = numero_user
                    text = text
                    enviar_msg(wa_id, f"*PROJETO ASAS*\n\nConsidere-se acolhido(a) {name}!\n\nDesejamos que você se sinta bem entre nós, que faça parte das nossas vivências, que encontre oportunidades e condições de aprender e crescer.\n\nEsperamos sinceramente que a sua experiência conosco seja excelente e duradoura.\n\nSinta-se muito bem-vindo(a)!\n\nDivulgue o *PROJETO ASAS*!\n\nSiga-nos, curta e compartilhe nossas mídias sociais (@asasvoleigama). Se preferir, contate-nos por telefone ou envie-nos um e-mail (asasvoleigama@gmail.com).\n\n*#SomosTodosASAS*")
                    enviar_msg(wa_id, "Caso não tenha realizado o download do *TERMO DE USO DE IMAGEM*, acesse o link abaixo, imprima, preencha e entregue à um dos coordenadores, treinadores ou representantes do *PROJETO ASAS* quando vier participar de nossas atividades.")
                    Menus.enviar_link2(wa_id, "https://docs.google.com/document/d/1O9ulUP6yCmil8-i_7tHi9lBGJGN0vLMg/edit", "Termo de uso de imagem", "Clique no link abaixo para fazer o download:", "clique aqui")
                    enviar_msg(wa_id, 'Para saber os horários e locais dos treinos, por favor, dirija-se ao menu: *"Treinos Abertos"*')
                    enviar_msg(numero_para_enviar, f"O contato número: {numero_user}, informa que preencheu nosso formulário de Cadastro, por favor, acompanhar, confirmar e adicionar este contato no grupo de *INTEGRANTES* do *PROJETO*.")
                    enviar_msg(abraao, f"O contato número: {numero_user}, informa que preencheu nosso formulário de Cadastro, por favor, acompanhar, confirmar e adicionar este contato no grupo de *INTEGRANTES* do *PROJETO*.")
                    Menus.enviar_mensagem_template2(numero_para_enviar, nome, f"Em: {obter_horario_atual()}. Número: {numero_user}. Preencheu o cadastro no Formulário de Inscrições do PROJETO ASAS.")
                    Menus.enviar_mensagem_template2(comunicacao, nome, f"Em: {obter_horario_atual()}. Número: {numero_user}. Preencheu o cadastro no Formulário de Inscrições do PROJETO ASAS.")
                    Menus.menu_encerrar(wa_id, "user")
                    alterar_var_numero(numero_user, "inicial")

            if text:
                if obter_var_numero(numero_user) == "ouvidoria":
                    if text:
                        detalhes = text
                        enviar_msg(wa_id, "*Agradecemos o seu feedback!*\n\n- Sua participação é fundamental para alcançarmos nossos objetivos.\n\n- Iremos conduzir os próximos passos com a atenção que sua mensagem requer e, se necessário, entraremos em contato em breve.")
                        enviar_msg(numero_para_enviar, f"O contato número: {numero_user}, está requisitando *OUVIDORIA* conforme detalhamento a seguir:\n\n- {detalhes}")
                        Menus.enviar_contato(numero_para_enviar, name, numero_user)
                        alterar_aguardando_resposta_numero(numero_user, 0)
                        Menus.menu_encerrar(wa_id, "user")

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
    session_timeout_set()
    session_timeout_set_db()
    print("session dbcfg:", session_timeout_view())
    print("seesion db: ", session_timeout_view_db())
    app.run(debug=True, port=4000)
