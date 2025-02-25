from config_bot import BASE_URL, PAGE_ID, WHATSAPP_TOKEN
import requests
from enum import Enum
import random
import string


def gerar_codigo_aleatorio(tamanho):
    # Letras maiúsculas, minúsculas e dígitos
    caracteres = string.ascii_letters + string.digits
    codigo = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return codigo


codigo_aleatorio = gerar_codigo_aleatorio(8)


class MenuOptions(Enum):
    INICIAL = 'inicial'
    FINANCEIRO = 'financeiro'
    SUPORTE1 = 'suporte1'
    SUPORTE2 = 'suporte2'
    SUPORTE3 = 'suporte3'
    SUPORTE4 = 'suporte4'
    OUTROS = 'OUTROS'
    COMERCIAL = 'comercial'
    PRIVACIDADE = 'privacidade'
    ADM = 'administracao'
    VOLTAR = "voltar"


class Menus():

    menu_escolhido = None

    # ---------------------------------privacidade---------------------------------

    def menu_privacidade(numero):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        menu = (
                "\n"
                "\n*PROJETO ASAS GAMA*\n\nOlá, sejam bem-vindos ao PROJETO ASAS!\n\nÉ um prazer atendê-los aqui!\n\nAntes de iniciarmos nossa interação neste canal, solicitamos que leia nossa política de privacidade:"
                "\n"
                "\nLink: "
                "\n"
                '\nSe estiver de acordo com nossos termos, por favor, clique em "ACEITO". Caso contrário, clique em "SAIR".'
                "\n"
                "\nSalientamos que ao aceitar nossos termos estará contribuindo para que possamos melhorar ainda mais sua experiência conosco."
                "\n")

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {"text": menu},
                "action": {
                    "buttons": [{'type': "reply",
                                 'reply': {"id": "ACEITOU",
                                           "title": "ACEITO"}},
                                {'type': "reply",
                                 'reply': {"id": "NEGOU",
                                           "title": "SAIR"}},
                                ]}}
        }

        try:
            # Usar 'json' em vez de 'data'
            response = requests.post(url, headers=headers, json=data)
            print(response.status_code)
            print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    # ---------------------------------inicial---------------------------------

    def menu_inicial(numero, nome):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        menu = (
                "\n"
                "\nOlá!\n\nQue legal você por aqui!\n\nSou o Assistente Virtual do *PROJETO ASAS* é sempre um prazer lhe atender!\nEspero conseguir sanar todas as suas dúvidas, dar suporte e lhe orientar sobre como participar do *PROJETO*.\n\n*Informações Gerais*\n\n  - Conheça-nos um pouco mais. Aqui você terá acesso às normativas do *PROJETO*, nossa origem, objetivos, valores e nossa metodologia.\n\n*Suporte e Feedback*\n\n  - Tire dúvidas, conheça nossos Contatos Institucionais, nossa Ouvidoria e deixe sua opinião, sugestões e/ou reclamações.\n\n*Como Participar*\n\n  - Saiba como participar de nossos treinos, atividades e eventos. Mantenha-se atualizado com depoimentos e outros registros dos participantes envolvidos com o *PROJETO*.\n\n*Escolha uma das opções abaixo para continuar:*"
                "\n")

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {"text": menu},
                "action": {
                    "buttons": [{'type': "reply",
                                 'reply': {"id": "INFO_GERAL",
                                           "title": "Informações Gerais"}},
                                {'type': "reply",
                                 'reply': {"id": "SUPORTE",
                                           "title": "Suporte e Feedback"}},
                                {'type': "reply",
                                 'reply': {"id": "PARTICIPAR",
                                           "title": "Participe e Conheça"}},
                                ]}}
        }

        try:
            # Usar 'json' em vez de 'data'
            response = requests.post(url, headers=headers, json=data)
            print(response.status_code)
            print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    def menu_voltar(numero, nome):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        menu = (
            "\n"
            "\nSelecione *VOLTAR* para retornar ao *MENU INICIAL*"
            "\n")

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {"text": menu},
                "action": {
                    "buttons": [{'type': "reply",
                                 'reply': {"id": "voltar",
                                           "title": "VOLTAR"}},
                                {'type': "reply",
                                 'reply': {"id": "encerrar",
                                           "title": "ENCERRAR Atendimento"}},
                                ]}}
        }

        try:
            # Usar 'json' em vez de 'data'
            response = requests.post(url, headers=headers, json=data)
            print(response.status_code)
            print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    def submenu_voltar(numero, nome):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        menu = (
            "\n"
            "\nSelecione *VOLTAR* para retornar ao MENU anterior"
            "\n")

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {"text": menu},
                "action": {
                    "buttons": [{'type': "reply",
                                 'reply': {"id": "voltar2",
                                           "title": "VOLTAR"}},
                                {'type': "reply",
                                 'reply': {"id": "encerrar",
                                           "title": "ENCERRAR Atendimento"}},
                                ]}}
        }

        try:
            # Usar 'json' em vez de 'data'
            response = requests.post(url, headers=headers, json=data)
            print(response.status_code)
            print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    def menu_encerrar(numero, nome):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        menu = (
            "\n"
            "\n- Podemos auxiliar em algo mais?\n\n- Deseja encerrar esse atendimento?"
            "\n")

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {"text": menu},
                "action": {
                    "buttons": [{'type': "reply",
                                 'reply': {"id": "encerrar",
                                           "title": "ENCERRAR"}},
                                {'type': "reply",
                                 'reply': {"id": "continuar",
                                           "title": "CONTINUAR"}},
                                ]}}
        }

        try:
            # Usar 'json' em vez de 'data'
            response = requests.post(url, headers=headers, json=data)
            print(response.status_code)
            print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    def menu_avaliacao(numero, nome):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "list",
                "header": {
                    "type": "text",
                    "text": "Foi um prazer lhe atender por aqui!"
                },
                "body": {
                    "text": "*AVALIE NOSSO ATENDIMENTO*\n\nPor favor, avalie este atendimento para que possamos melhorá-lo. Clique no link abaixo e faça sua avaliação."
                },
                "footer": {
                    "text": "Opções de Abaixo:"
                },
                "action": {
                    "button": "Clique aqui",
                    "sections": [{
                        "title": "Opções de serviço",
                        "rows": [
                            {"id": "muito_bom", "title": "😁 Muito bom."},
                            {"id": "bom", "title": "😄 Bom."},
                            {"id": "mediano", "title": "🙂 Mediano."},
                            {"id": "ruim", "title": "🥲 Ruim."},
                            {"id": "pessimo", "title": "😓 Péssimo"},
                        ]
                    }]
                }
            }
        }

        try:
            # Usar 'json' em vez de 'data'
            response = requests.post(url, headers=headers, json=data)
            print(response.status_code)
            print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    def menu_informacoes(numero, nome):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "list",
                "header": {
                    "type": "text",
                    "text": "Informações"
                },
                "body": {
                    "text": "*Sobre o PROJETO ASAS*\n\n - Entenda como o projeto surgiu e o que buscamos realizar através do esporte.\n\n*Missão, Visão e Valores*\n\n - Nossos princípios, diretrizes e normativas.\n\n*Metodologia*\n\n - Como trabalhamos para transformar vidas através de esportes coletivos.\n\n*Contatos e Mídias Sociais*\n\n - Nossos canais institucionais de comunicação e mídias sociais."
                },
                "footer": {
                    "text": "Opções de Abaixo:"
                },
                "action": {
                    "button": "Clique aqui",
                    "sections": [{
                        "title": "Opções de serviço",
                        "rows": [
                            {"id": "SOBRE", "title": "Sobre o PROJETO ASAS"},
                            {"id": "MISSAO", "title": "Missão, Visão e Valores"},
                            {"id": "METODO", "title": "Nossa Metodologia"},
                            {"id": "CONTATO", "title": "Contatos Institucionais"},
                            {"id": "CONTAT2", "title": "Mídias Sociais"},
                            {"id": "VOLTAR", "title": "Voltar ao MENU principal"},
                            {"id": "encerrar", "title": "Encerrar atendimento"},
                        ]
                    }]
                }
            }
        }

        try:
            # Usar 'json' em vez de 'data'
            response = requests.post(url, headers=headers, json=data)
            print(response.status_code)
            print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    def suporte_feedback(numero, nome):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        menu = (
                "\n"
                "\n*Suporte e Feedback*\n\n*Dúvidas Frequentes*\n\n - Respostas para as perguntas mais comuns.\n\n*Fale Conosco*\n\n - Canal para entrar em contato com nossa equipe de suporte.\n\n*Ouvidoria*\n\n - Deixe sua opinião, crítica ou sugestão sobre o PROJETO ASAS.\n\nEscolha uma das opções abaixo para continuar:"
                "\n")

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {"text": menu},
                "action": {
                    "buttons": [{'type': "reply",
                                 'reply': {"id": "DUVIDAS",
                                           "title": "Dúvidas Frequentes"}},
                                {'type': "reply",
                                 'reply': {"id": "FALE",
                                           "title": "Fale Conosco"}},
                                {'type': "reply",
                                 'reply': {"id": "OUVIDORIA",
                                           "title": "Ouvidoria"}},
                                ]}}
        }

        try:
            # Usar 'json' em vez de 'data'
            response = requests.post(url, headers=headers, json=data)
            print(response.status_code)
            print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    def menu_participar(numero, nome):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "list",
                "header": {
                    "type": "text",
                    "text": "Participe e Conheça"
                },
                "body": {
                    "text": "*CONHEÇA-NOS, PARTICIPE, APOIE OU INVISTA NO PROJETO ASAS*\n\n*Treinos Abertos ao Público*\n\n- Datas, horários e locais dos treinos gratuitos\n\n*Como Participar*\n\n- Saiba como se inscrever e fazer parte do *PROJETO ASAS*.\n\n*Apoie ou Invista no PROJETO ASAS*\n\n- Faça parte do *PROJETO ASAS*. Apoie ou Invista nesta iniciativa. Conheça nossos parceiros e patrocinadores. Adote um integrante do *PROJETO*\n\n*Galeria de Fotos e Vídeos*\n\n- Registros dos treinos e atividades com nossos participantes.\n\n*Depoimentos*\n\n- Depoimentos dos envolvidos com o *PROJETO ASAS*."
                },
                "footer": {
                    "text": "Opções de Abaixo:"
                },
                "action": {
                    "button": "Clique aqui",
                    "sections": [{
                        "title": "Opções de serviço",
                        "rows": [
                            {"id": "TREINOS", "title": "Treinos Abertos"},
                            {"id": "PARTICIPAR", "title": "Como Participar"},
                            {"id": "INVISTA", "title": "Apoie ou invista"},
                            {"id": "GALERIA", "title": "Galeria"},
                            {"id": "DEPOIMENTO", "title": "Depoimentos"},
                            {"id": "VOLTAR", "title": "Voltar ao menu principal"},
                            {"id": "encerrar", "title": "Encerrar atendimento"},
                        ]
                    }]
                }
            }
        }

        try:
            # Usar 'json' em vez de 'data'
            response = requests.post(url, headers=headers, json=data)
            print(response.status_code)
            print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    # ---------------------------------------templates---------------------------------------

    def menu_opçoes_lista_template(numero: str, nome: str) -> any:
        '''
        esta funçao envia um menu de lista interativo

        passe os parametros:

            número(número de destino)

            nome(nome do usuário)
        '''

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "list",
                "header": {
                    "type": "text",
                    "text": "TESTE"
                },
                "body": {
                    "text": "MENU TESTE"
                },
                "footer": {
                    "text": "MENU TESTE"
                },
                "action": {
                    "button": "Clique aqui",
                    "sections": [{
                        "title": "Opções do menu teste",
                        "rows": [
                            {"id": "row1", "title": "TESTE 1"},
                            {"id": "row2", "title": "TESTE 2"},
                            {"id": "row3", "title": "TESTE 3"},
                        ]
                    }]
                }
            }
        }

        try:
            # Usar 'json' em vez de 'data'
            response = requests.post(url, headers=headers, json=data)
            print(response.status_code)
            print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    def menu_opçao_botao_interativo_template(numero: str, nome: str) -> any:
        '''
        esta funçao envia menu com ate 3 botoes clicaveis

        passe os parametros:

            número(número de destino)

            nome(nome do usuário)
        '''
        url = f"{BASE_URL}/{PAGE_ID}/messages"
        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }
        menu = ("*TITULO*"
                "\n"
                "\n*TEXTO*"
                "\n"
                "\nDigite *voltar* para voltar ao *MENU INICIAL*")
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {"text": menu},
                "action": {
                    "buttons": [{'type': "reply",
                                'reply': {"id": "ID do BOTAO",
                                          "title": "titulo bota"}},
                                {'type': "reply",
                                'reply': {"id": "ID do BOTAO",
                                          "title": "titulo bota"}},
                                {'type': "reply",
                                'reply': {"id": "ID do BOTAO",
                                          "title": "titulo bota"}},
                                ]}}
        }

        try:
            # Usar 'json' em vez de 'data'
            response = requests.post(url, headers=headers, json=data)
            print(response.status_code)
            print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    def enviar_link2(numero: str, link: str, titulo, texto, texto_botao):
        '''
        esta função envia um contato para o usuário

        passe os parametros:

            número(número de destino)

            url(url que será anexada)
        '''
        url = f"{BASE_URL}/{PAGE_ID}/messages"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        }
        menu = (f"*{titulo}*"
                "\n"
                f"\n{texto}")
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "cta_url",
                "body": {"text": menu},
                "action": {
                    'name': "cta_url",
                    'parameters': {
                        "display_text": f"{texto_botao}",
                        "url": link
                    }
                }
            }
        }

        try:
            # Usar 'json' em vez de 'data'
            response = requests.post(url, headers=headers, json=data)
            print(response.status_code)
            print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    def enviar_link(numero: str, link: str):
        '''
        esta funçao envia um contato para o usuário

        passe os parametros:

            número(número de destino)

            url(url que será anexada)
        '''
        url = f"{BASE_URL}/{PAGE_ID}/messages"
        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }
        menu = ("*NOSSO SITE*"
                "\n"
                "\n*Clique o Link abaixo para acessar nosso site*:")
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "cta_url",
                "body": {"text": menu},
                "action": {
                    'name': "cta_url",
                    'parameters': {
                        "display_text": "Clique aqui",
                        "url": link
                    }
                }
            }
        }

        try:
            # Usar 'json' em vez de 'data'
            response = requests.post(url, headers=headers, json=data)
            print(response.status_code)
            print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    def upload_arquivo(media_path: str, file_type) -> str:
        upload_url = f"{BASE_URL}/{PAGE_ID}/media"
        headers = {"Authorization": f"Bearer {WHATSAPP_TOKEN}"}

        files = {
            "file": (media_path.split("/")[-1], open(media_path, "rb"), file_type),
            "messaging_product": (None, "whatsapp")
        }

        try:
            response = requests.post(upload_url, headers=headers, files=files)
            response.raise_for_status()
            media_id = response.json().get("id", "")
            return media_id
        except requests.exceptions.RequestException as e:
            print(f"Erro ao fazer upload do vídeo: {e}")
            print(response.text)
            raise Exception("Falha ao fazer upload do vídeo.")

    def enviar_documento(numero: str, path_file: str, nome_arquivo: str, formato: str) -> any:
        '''
        esta funçao envia uma imagem para o usuário

        passe os parametros:

            número(número de destino)

            path_file(exemplo: "C:\\Users\\nicollas\\Desktop\\projeto_asas\\PROJETO\\projeto.docx")

            nome_arquivo(nome do arquivo))
        '''
        try:
            media_id = Menus.upload_arquivo(
                path_file, f"{formato}")
            print(f"Media ID: {media_id}")
        except Exception as e:
            print(f"Erro: {e}")

        url = f"{BASE_URL}/{PAGE_ID}/messages"
        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "document",
            "document": {
                "id": media_id,
                "filename": nome_arquivo,
            }
        }

        try:
            # Usar 'json' em vez de 'data'
            response = requests.post(url, headers=headers, json=data)
            print(response.status_code)
            print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    def enviar_imagem(numero: str, path_file: str) -> any:
        '''
        esta funçao envia uma imagem para o usuário

        passe os parametros:

            número(número de destino)

            path_file(exemplo: "C:\\Users\\nicollas\\Desktop\\projeto_asas\\PROJETO\\Sem título.jpeg")

            provider(o provedor(Google, Google Drive, AWS etc))
        '''
        try:
            media_id = Menus.upload_arquivo(path_file, "image/jpeg")
            print(f"Media ID: {media_id}")
        except Exception as e:
            print(f"Erro: {e}")

        url = f"{BASE_URL}/{PAGE_ID}/messages"
        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "image",
            "image": {
                "id": media_id,
            }
        }

        try:
            # Usar 'json' em vez de 'data'
            response = requests.post(url, headers=headers, json=data)
            print(response.status_code)
            print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    def enviar_video(numero: str, path_file: str) -> any:
        '''
        esta funçao envia um video para o usuário

        passe os parametros:

            número(número de destino)

            path_file(exemplo: "C:\\Users\\nicollas\\Desktop\\projeto_asas\\PROJETO\\video.mp4")

        '''
        try:
            media_id = Menus.upload_arquivo(path_file, "video/mp4")
            print(f"Media ID: {media_id}")
        except Exception as e:
            print(f"Erro: {e}")

        url = f"{BASE_URL}/{PAGE_ID}/messages"
        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "video",
            "video": {
                "id": media_id,
            }
        }

        try:
            # Usar 'json' em vez de 'data'
            response = requests.post(url, headers=headers, json=data)
            print(response.status_code)
            print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    def enviar_audio(numero: str, path_file: str, extencao: str) -> any:
        '''
        esta funçao envia um video para o usuário

        passe os parametros:

            número(número de destino)

            path_file(exemplo: "C:\\Users\\nicollas\\Desktop\\projeto_asas\\PROJETO\\audio.ogg")

        '''
        try:
            media_id = Menus.upload_arquivo(path_file, f"{extencao}")
            print(f"Media ID: {media_id}")
        except Exception as e:
            print(f"Erro: {e}")

        url = f"{BASE_URL}/{PAGE_ID}/messages"
        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "audio",
            "audio": {
                "id": media_id,
            }
        }

        try:
            # Usar 'json' em vez de 'data'
            response = requests.post(url, headers=headers, json=data)
            print(response.status_code)
            print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    def enviar_contato(numero: str, nome_do_contato: str, numero_contato: str) -> any:
        '''
        esta funçao envia um contato para o usuário

        passe os parametros:

            número(número de destino)

            nome_do_contato(nome que vai aparecer no contato enviado)

            número_contato(o número que vai aparecer no contato enviado)
        '''
        url = f"{BASE_URL}/243259005527427/messages"
        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        data = {
            "messaging_product": "whatsapp",
            "to": numero,
            "type": "contacts",
            "contacts": [{
                "name": {
                    "first_name": nome_do_contato,
                    "formatted_name": nome_do_contato
                },
                "phones": [{
                    "phone": numero_contato,
                    "wa_id": numero_contato,
                    "type": "Celular"
                }]
            }]
        }

        try:
            # Usar 'json' em vez de 'data'
            response = requests.post(url, headers=headers, json=data)
            print(response.status_code)
            print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    def enviar_loc(numero: str, lat: str, long: str, endereco: str, nome_local: str) -> any:
        '''
        esta funçao envia um contato para o usuário

        passe os parametros:

            número(número de destino)

            nome_do_contato(nome que vai aparecer no contato enviado)

            número_contato(o número que vai aparecer no contato enviado)
        '''
        url = f"{BASE_URL}/243259005527427/messages"
        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        data = {
            "messaging_product": "whatsapp",
            "to": numero,
            "type": "location",
            "location": {
                "latitude": f"{lat}",
                "longitude": f"{long}",
                "name": f"{nome_local}",
                "address": f"{endereco}"
                },
            }

        try:
            # Usar 'json' em vez de 'data'
            response = requests.post(url, headers=headers, json=data)
            print(response.status_code)
            print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    def enviar_mensagem_template(numero, nome, detalhes):
        nome_template = "request"
        idioma = "pt_BR"
        url = f"{BASE_URL}/{PAGE_ID}/messages"
        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "template",
            "template": {
                "name": nome_template,
                "language": {
                    "code": idioma
                },
                "components": [
                    {
                        "type": "header",
                        "parameters": [
                            {
                                "type": "text",
                                "text": f"{nome}"
                            }
                        ]
                    },
                    {
                        "type": "body",
                        "parameters": [
                            {
                                "type": "text",
                                "text": f"{nome}"
                            },
                            {
                                "type": "text",
                                "text": f"{numero}"
                            }
                        ]
                    }
                ]
            }
        }
        try:
            # Usar 'json' em vez de 'data'
            response = requests.post(url, headers=headers, json=data)
            print(response.status_code)
            print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    def enviar_mensagem_template2(numero, nome, detalhes):
        nome_template = "request2"
        idioma = "pt_BR"
        url = f"{BASE_URL}/{PAGE_ID}/messages"
        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "template",
            "template": {
                "name": nome_template,
                "language": {
                    "code": idioma
                },
                "components": [
                    {
                        "type": "header",
                        "parameters": [
                            {
                                "type": "text",
                                "text": f"{nome}"
                            }
                        ]
                    },
                    {
                        "type": "body",
                        "parameters": [
                            {
                                "type": "text",
                                "text": f"{detalhes}"
                            }
                        ]
                    }
                ]
            }
        }
        try:
            # Usar 'json' em vez de 'data'
            response = requests.post(url, headers=headers, json=data)
            print(response.status_code)
            print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    def enviar_mensagem_template3(numero, numero_user, nome, detalhes):
        nome_template = "request2"
        idioma = "pt_BR"
        url = f"{BASE_URL}/{PAGE_ID}/messages"
        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "template",
            "template": {
                "name": nome_template,
                "language": {
                    "code": idioma
                },
                "components": [
                    {
                        "type": "header",
                        "parameters": [
                            {
                                "type": "text",
                                "text": f"{nome}"
                            }
                        ]
                    },
                    {
                        "type": "body",
                        "parameters": [
                            {
                                "type": "text",
                                "text": f"{nome}"
                            },
                            {
                                "type": "text",
                                "text": f"{numero_user}"
                            },
                            {
                                "type": "text",
                                "text": f"{detalhes}"
                            }
                        ]
                    }
                ]
            }
        }
        try:
            # Usar 'json' em vez de 'data'
            response = requests.post(url, headers=headers, json=data)
            print(response.status_code)
            print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")
