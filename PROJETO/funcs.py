import os
import datetime
from config_bot import voltar
from menssages import MenuOptions

log_directory = r'/home/teletron/Área de Trabalho/project/bot/PROJETO/logs'
os.makedirs(log_directory, exist_ok=True)

# menu inicial
menu_inicial_message = ("*MENU INICIAL*\n\n*TELETRON INDUSTRIA E COMERCIO LTDA.*\n\nOlá! seja Bem-vindo a Teletron, Para acessar qualquer um dos menus abaixo apenas escolha a opção desejada\n")
# Financeiro Menu
menu_financeiro_message = ("*FINANCEIRO*\n\n*BEM VINDO AO FINANCEIRO ESCOLHA UMA DAS OPÇOES ABAIXO*\nDigite *voltar* para voltar ao *MENU INICIAL*")
# Suporte Técnico Menu
menu_suporte_tecnico_message1 = ("*SUPORTE*\n\n*PARA SUPORTE PEDIMOS QUE CONFIRME SE JA TEM CONTRATO COM A GENTE*")
menu_suporte_tecnico_message2 = ("SELECIONE UMA DAS OPÇOES DE SUPORTE ABAIXO")
menu_suporte_tecnico_message3 = ("Por favor envie uma menssagem detalhando seu problema:")
# Comercial Menu
menu_comercial_message = ("*COMERCIAL*\n\n*BEM VINDO AO COMERCIAL ESCOLHA UMA DAS OPÇOES ABAIXO*\nDigite *voltar* para voltar ao *MENU INICIAL*")
# comercial voz
menu_comercial_voz = ("*O que podemos oferecer*:\n\n*Voz*\n\nSIP Server - Serviço de servidor de voz SIP\n\nGravador de Chamadas - Serviço de gravação de chamadas\n\nAparelhos IP - Serviço de telefonia com aparelhos IP\n\nURA - Atendimento automático de voz\n\nGateways - Serviço de integração de rede\n\nCorreio de Voz - Serviço de caixa de correio de voz\n\nRelatórios - Geração de relatórios de chamadas")
# comercial dados
menu_comercial_dados = ("*O que podemos oferecer*:\n\n*Voz*\n\nSIP Server - Serviço de servidor de voz SIP\n\nGravador de Chamadas - Serviço de gravação de chamadas\n\nAparelhos IP - Serviço de telefonia com aparelhos IP\n\nURA - Atendimento automático de voz\n\nGateways - Serviço de integração de rede\n\nCorreio de Voz - Serviço de caixa de correio de voz\n\nRelatórios - Geração de relatórios de chamadas")

# comercial segurança
menu_comercial_seguranca = ("O que podemos oferecer*:\n\n*SEGURANÇA*\n\nCFTV - Serviço de Circuito Fechado de TV\n\nCentral de Cerca Elétrica - Serviço de Cerca Elétrica\n\nCentral de Alarme - Serviço de Alarme de Segurança")
# comercial cabeamento
menu_comercial_cabeamento = ("\n*O que podemos oferecer*:\n\n*CABEAMENTO*\n\nCabeamento Estruturado - Serviço de Cabeamento Estruturado")
# comercial locação
menu_comercial_locacao = ("O que podemos oferecer*:\n\n*LOCAÇÃO*\n\nLocação de Equipamentos - Serviço de locação de equipamentos")
# comercial sip
menu_sip = (
    "*SipServer*"
    "\n\nPara solicitar esse serviço, você deve enviar uma mensagem contendo as seguintes informações:"
    "\n\nInformações que precisam estar na mensagem:"
    "\n\nInformações do contratante:"
    "\n   Nome: [Seu Nome]"
    "\n   Nome da empresa: [Nome da empresa]"
    "\n   Setor da empresa: [Setor da empresa]"
    "\n\n   Tamanho da empresa: [número de funcionários]"
    "\n\nDetalhes técnicos:"
    "\n   Número de linhas SIP necessárias"
    "\n   Necessidades específicas de chamadas (ex.: videoconferência)"
    "\n   Requisitos de segurança"
    "\n\nPreferências de serviço:"
    "\n   Tipo de serviço (hospedagem de SIP, SIP trunking)"
    "\n   Duração do contrato desejada"
    "\n   Suporte técnico"
    "\n   Integração com outros sistemas"
    "\n\nTráfego estimado:"
    "\n   Número estimado de chamadas simultâneas"
    "\n   Volume de tráfego de voz ou dados"
)
# comercial gravador
menu_gravador = (
    "*Gravador de chamadas*"
    "\n\nPara solicitar esse serviço, você deve enviar uma mensagem contendo as seguintes informações:"
    "\n\nInformações que precisam estar na mensagem:"
    "\n\nInformações do contratante:"
    "\n   Nome: [Seu Nome]"
    "\n   Nome da empresa: [Nome da empresa]"
    "\n   Setor da empresa: [Setor da empresa]"
    "\n   Tamanho da empresa: [número de funcionários]"
    "\n\nDetalhes do serviço:"
    "\n   Estimativa de usuários do serviço de gravação"
    "\n   Tipo de linha telefônica (análogica, digital, VoIP, etc.)"
    "\n   Número de linhas a serem gravadas"
    "\n   Duração esperada das gravações (horas por dia)"
    "\n\nRequisitos específicos:"
    "\n   Integrações necessárias (ex.: integração com CRM)"
    "\n   Funcionalidades desejadas (marcação de chamadas importantes, pesquisa de palavras-chave, etc.)"
    "\n\nArmazenamento e retenção dos dados:"
    "\n   Duração de retenção das gravações (meses, anos)"
    "\n   Capacidade de armazenamento necessária"
    "\n\nComentários ou observações adicionais: (Opcional)"
)
# comercial aparelho ip
menu_ip = (
    "*Aparelhos IP*"
    "\n\nPara solicitar esse serviço, você deve enviar uma mensagem contendo as seguintes informações:"
    "\n\nInformações que precisam estar na mensagem:"
    "\n\nInformações do contratante:"
    "\n   Nome: [Seu Nome]"
    "\n   Nome da empresa: [Nome da empresa]"
    "\n   Setor da empresa: [Setor da empresa]"
    "\n   Tamanho da empresa: [número de funcionários]"
    "\n\nTipo de serviço:"
    "\n   Tipo de aparelho IP desejado (VoIP, SIP, softphone, etc.)"
    "\n\nNecessidades de hardware:"
    "\n   Número ou estimativa de aparelhos IP necessários"
    "\n   Modelo ou especificações desejadas (opcional)"
    "\n\nLocalização e rede:"
    "\n   Localização da instalação (se houver várias filiais)"
    "\n   Detalhes sobre a infraestrutura de rede existente (opcional)"
    "\n\nIntegrações e recursos:"
    "\n   Integrações com outros sistemas ou aplicativos"
    "\n   Recursos desejados (conferência, gravação de chamadas, transferência de chamadas, etc.)"
    "\n\nRequisitos de segurança:"
    "\n   Medidas de segurança necessárias (criptografia, autenticação de chamadas)"
    "\n\nVolume de chamadas:"
    "\n   Número estimado de chamadas por dia/semana/mês"
    "\n\nNecessidades de suporte:"
    "\n   Nível de suporte desejado (ex.: suporte presencial)"
    "\n\nComentários ou observações adicionais: (Opcional)"
)
# comercial ura
menu_ura = (
    "*URA*"
    "\n\nPara solicitar esse serviço, você deve enviar uma mensagem contendo as seguintes informações:"
    "\n\nInformações que precisam estar na mensagem:"
    "\n\nInformações do contratante:"
    "\n   Nome: [Seu Nome]"
    "\n   Nome da empresa: [Nome da empresa]"
    "\n   Setor da empresa: [Setor da empresa]"
    "\n   Tamanho da empresa: [número de funcionários]"
    "\n\nDetalhes do serviço:"
    "\n   Tipo de serviço de URA desejado (menu de atendimento, resposta a FAQs, pesquisa de satisfação, etc.)"
    "\n   Número estimado de ramais ou extensões necessárias"
    "\n   Complexidade do menu (simples, intermediária, avançada)"
    "\n   Integração com sistemas existentes (opcional)"
    "\n\nVolume de chamadas:"
    "\n   Estimativa do número de chamadas recebidas por dia/semana/mês"
    "\n   Horário de pico das chamadas"
    "\n\nOutros recursos:"
    "\n   Necessidade de encaminhamento de chamadas para atendentes humanos"
    "\n   Integração com serviços de atendimento ao cliente (CRM)"
    "\n\nComentários ou observações adicionais: (Opcional)"
)
# comercial gateway
menu_gateway = (
    "*Gateways*"
    "\n\nPara solicitar esse serviço, você deve enviar uma mensagem contendo as seguintes informações:"
    "\n\nInformações que precisam estar na mensagem:"
    "\n\nInformações do contratante:"
    "\n   Nome: [Seu Nome]"
    "\n   Nome da empresa: [Nome da empresa]"
    "\n   Setor da empresa: [Setor da empresa]"
    "\n   Tamanho da empresa: [número de funcionários]"
    "\n\nDetalhes do serviço:"
    "\n   Tipo de serviço de gateways (integração de pagamento, SMS, API, etc.)"
    "\n   Descrição das necessidades do projeto"
    "\n   Plataformas ou sistemas com os quais o gateway deve ser compatível"
    "\n\nVolume de transações:"
    "\n   Número médio de transações por mês"
    "\n   Valor médio por transação"
    "\n\nRequisitos técnicos:"
    "\n   Integração necessária (REST API, Webhooks, etc.)"
    "\n   Recursos específicos (segurança, criptografia)"
    "\n   Plataformas ou linguagens de programação usadas"
    "\n\nComentários ou observações adicionais: (Opcional)"
)
# comercial correio voz
menu_correio = (
    "*Correio de voz*"
    "\n\nPara solicitar esse serviço, você deve enviar uma mensagem contendo as seguintes informações:"
    "\n\nInformações que precisam estar na mensagem:"
    "\n\nInformações do contratante:"
    "\n   Nome: [Seu Nome]"
    "\n   Nome da empresa: [Nome da empresa]"
    "\n   Setor da empresa: [Setor da empresa]"
    "\n   Tamanho da empresa: [número de funcionários]"
    "\n\nDetalhes do serviço de Correio de Voz:"
    "\n   Número de usuários"
    "\n   Necessidade de integração com e-mail"
    "\n   Fuso horário preferido para receber mensagens de voz"
    "\n\nPreferências de mensagem:"
    "\n   Formato do arquivo de áudio preferido (MP3, WAV, etc.)"
    "\n   Informações a serem incluídas no corpo do e-mail (data, hora, duração, número identificado)"
    "\n\nComentários ou observações adicionais: (Opcional)"
)
# comercial relatorio
menu_relatorio = (
    "*Relatórios*"
    "\n\nPara solicitar esse serviço, você deve enviar uma mensagem contendo as seguintes informações:"
    "\n\nInformações que precisam estar na mensagem:"
    "\n\nInformações do contratante:"
    "\n   Nome: [Seu Nome]"
    "\n   Nome da empresa: [Nome da empresa]"
    "\n   Setor da empresa: [Setor da empresa]"
    "\n   Tamanho da empresa: [número de funcionários]"
    "\n\nDetalhes do Serviço Desejado:"
    "\n   Tipo de relatório (relatório de desempenho, fluxo de chamadas, custos, etc.)"
    "\n   Abrangência (chamadas internas, chamadas externas, entrada, saída)"
    "\n   Objetivos do relatório (aprimoramento na distribuição de chamadas, redução de custos, etc.)"
    "\n\nInformações sobre a infraestrutura de telecomunicações:"
    "\n   Tipo de sistema telefônico (por exemplo, PBX, VoIP)"
    "\n   Número de linhas telefônicas"
    "\n   Número de ramais"
    "\n   Integrações com outros sistemas (opcional)"
    "\n\nRequisitos Específicos:"
    "\n   Período de análise desejado"
    "\n   Necessidades de customização"
    "\n\nComentários ou observações adicionais: (Opcional)"
)
# comercial vpn
menu_vpn = (
    "*VPN*"
    "\n\nPara solicitar esse serviço voce deve enviar uma menssagem contendo as seguintes infomaçoes:"
    "\n\nInformaçoes que precisam estar na menssagem:"
    "\n\nInformações do contratante:"
    "\n   Nome: [Seu Nome]"
    "\n   Nome da empresa: [Nome da empresa]"
    "\n   Setor da empresa: [Setor da empresa]"
    "\n   Tamanho da empresa: [número de funcionários]"
    "\n\nDetalhes do serviço:"
    "\n   Número de usuários da VPN"
    "\n   Localização dos usuários (local, nacional, internacional)"
    "\n   Tipo de dispositivos a serem usados (desktop, celular, ambos)"
    "\n   Integração com infraestrutura existente (opcional)"
    "\n\nRequisitos de segurança:"
    "\n   Requisitos específicos de conformidade (por exemplo, GDPR, LGPD)"
    "\n\nRecursos adicionais:"
    "\n   Velocidade de conexão desejada"
    "\n   Serviços adicionais (ex.: proteção contra malware)"
    "\n\nComentários ou observações adicionais:(Opcional)"
)
# comercial firewall
menu_firewall = (
    "*Firewall*"
    "\n\nPara solicitar esse serviço voce deve enviar uma menssagem contendo as seguintes infomaçoes:"
    "\n\nInformaçoes que precisam estar na menssagem:"
    "\n\nInformações do contratante:"
    "\n   Nome: [Seu Nome]"
    "\n   Nome da empresa: [Nome da empresa]"
    "\n   Setor da empresa: [Setor da empresa]"
    "\n   Tamanho da empresa: [número de funcionários]"
    "\n\nDetalhes do serviço:"
    "\n   Número de usuários do firewall"
    "\n   Localização dos usuários (local, nacional, internacional)"
    "\n   Tipo de dispositivos a serem usados (desktop, celular, ambos)"
    "\n   Integração com infraestrutura existente (opcional)"
    "\n\nRequisitos de segurança:"
    "\n   Requisitos específicos de conformidade (por exemplo, GDPR, LGPD)"
    "\n\nRecursos adicionais:"
    "\n   Captive Portal para HOTSPOT (Check-in em redes sociais, personalização da página de login)"
    "\n   VPN para atividades EXTRA OFFICE ou HOME OFFICE (Número de conexões VPN necessárias, tipo de VPN (por exemplo, PPTP, L2TP/IPsec, OpenVPN))"
    "\n\nComentários ou observações adicionais:(Opcional)"
)
# comercial virtualização
menu_virtua = (
    "*Virtualizacao*"
    "\n\nPara solicitar esse serviço voce deve enviar uma menssagem contendo as seguintes infomaçoes:"
    "\n\nInformaçoes que precisam estar na menssagem:"
    "\n\nInformações do contratante:"
    "\n   Nome: [Seu Nome]"
    "\n   Nome da empresa: [Nome da empresa]"
    "\n   Setor da empresa: [Setor da empresa]"
    "\n   Tamanho da empresa: [número de funcionários]"
    "\n\nDetalhes do serviço:"
    "\n   Número de servidores a serem virtualizados"
    "\n   Sistema operacional dos servidores"
    "\n   Recursos necessários por servidor (CPU, RAM, armazenamento)"
    "\n\nServiço de Virtualização PVE:"
    "\n   Número de usuários da interface web"
    "\n   Quantidade de VMs necessárias"
    "\n   Sistema operacional"
    "\n\nCLUSTER:"
    "\n   Número de processos com alta complexidade"
    "\n   Requisitos de alta disponibilidade"
    "\n   Necessidade de configuração de cluster"
    "\n\nServiço de autoconfiguração – WPAD"
    "\n   Controlador de Domínio + GPOs + FileServer"
    "\n     Número de máquinas Windows na rede"
    "\n     Políticas de segurança específicas"
    "\n     File Server"
    "\n     Capacidade de armazenamento"
    "\n     Número de grupos"
    "\n     Restrições de acesso específicas"
    "\n   Servidor de e-mails:"
    "\n     Número de contas de e-mail"
    "\n     Políticas anti-spam específicas"
    "\n   Backup"
    "\n     Frequência do backup (diário, semanal, mensal)"
    "\n     Tamanho dos dados para backup"
    "\n\nComentários ou observações adicionais:(Opcional)"
)
# comercial cftv
menu_cftv = (
            "*CFTV*"
            "\n\nPara solicitar esse serviço voce deve enviar uma menssagem contendo as seguintes infomaçoes:"
            "\n\nInformaçoes que precisam estar na menssagem:"
            "\n\nInformações do contratante:"
            "\n   Nome: [Seu Nome]"
            "\n   Nome da empresa: [Nome da empresa]"
            "\n   Setor da empresa: [Setor da empresa]"
            "\n   Tamanho da empresa: [número de funcionários]"
            "\n\nDetalhes do serviço:"
            "\n   Virtualizacao"
            "\n   Tipo de câmeras (interna, externa, infravermelho, etc.)"
            "\n   Resolução das câmeras (SD, HD, Full HD, 4K)"
            "\n   Necessidade de gravação contínua ou por detecção de movimento"
            "\n\nInstalação:"
            "\n   Localização da instalação (endereço)"
            "\n   Tipo de propriedade (residencial, comercial, industrial)"
            "\n   Necessidade de fiação ou preferência por câmeras sem fio"
            "\n\nMonitoramento:"
            "\n   Necessidade de monitoramento remoto (via smartphone ou computador)"
            "\n   Necessidade de serviço de monitoramento profissional"
            "\n\nRecursos adicionais:"
            "\n   Visão noturna"
            "\n   Armazenamento em nuvem"
            "\n\nManutenção:"
            "\n   Frequência desejada de manutenção (mensal, trimestral, anual)"
            "\n\nComentários ou observações adicionais:(Opcional)"
)
# cerca eletrica
menu_cerca = (
    "*Central de Cerca Elétrica*"
    "\n\nPara solicitar esse serviço, você deve enviar uma mensagem contendo as seguintes informações:"
    "\n\nInformações que precisam estar na mensagem:"
    "\n\nInformações do contratante:"
    "\n   Nome: [Seu Nome]"
    "\n   Nome da empresa: [Nome da empresa]"
    "\n   Setor da empresa: [Setor da empresa]"
    "\n   Tamanho da empresa: [número de funcionários]"
    "\n\nDetalhes do serviço:"
    "\n   Comprimento total da cerca elétrica (em metros)"
    "\n   Altura da cerca elétrica (em metros)"
    "\n   Número de linhas de fio na cerca"
    "\n   Tipo de propriedade (residencial, comercial, industrial)"
    "\n   Tipo de cerca (convencional, com alarme, etc.)"
    "\n\nRecursos adicionais:"
    "\n   Controle remoto (opcional)"
    "\n   Sistema de alerta"
    "\n\nInstalação:"
    "\n   Localização da instalação (endereço)"
    "\n   Necessidade de remoção de uma cerca existente"
    "\n\nManutenção:"
    "\n   Frequência desejada de manutenção (mensal, trimestral, anual)"
    "\n\nComentários ou observações adicionais: (Opcional)"
)
# comercial central alarme
menu_alarme = (
    "*Central de Alarme*"
    "\n\nPara solicitar esse serviço, você deve enviar uma mensagem contendo as seguintes informações:"
    "\n\nInformações que precisam estar na mensagem:"
    "\n\nInformações do contratante:"
    "\n   Nome: [Seu Nome]"
    "\n   Nome da empresa: [Nome da empresa]"
    "\n   Setor da empresa: [Setor da empresa]"
    "\n   Tamanho da empresa: [número de funcionários]"
    "\n\nDetalhes do serviço:"
    "\n   Tipo de propriedade (residencial, comercial, industrial)"
    "\n   Tamanho da propriedade (em metros quadrados)"
    "\n   Número de Entradas/Saídas"
    "\n   Número de Janelas"
    "\n   Existência de áreas sensíveis (como cofres, áreas restritas)"
    "\n\nPreferências do sistema de alarme:"
    "\n   Tipo de sistema de alarme (Monitorado ou Não Monitorado)"
    "\n   Números de telefone para alertas (se o sistema não for monitorado)"
    "\n   Preferência por sensores sem fio ou com fio"
    "\n   Integração com CFTV"
    "\n\nComentários ou observações adicionais: (Opcional)"
)
# info menu
menu_info = ("enviou contato\n\nenviou link: https://teletronweb.com.br/\n\n")
# menu adm
menu_adm1 = ("em desenvolvimento...")
menu_adm2 = ("Status da aplicação:\n\nServiço DB: *OK*;\n\nServiço API: *OK*;\n\nServiço Mensagens: *OK*;\n\nStatus Geral: *Funcionando*")
menu_adm3 = (
    'Bem vindo ao menu de configuração use os comandos listados abaixo para poder alterar a propriedade desejada:\n\nPara alterar o inicio do horario comercial digite "horario1_alterar", e aguarde a confirmação do bot, apos isso digite um numero inteiro\n\n  Exemplo:\n\n  voce: *horario1_alterar*\n\n  bot: *comfirmação do bot*\n\n  voce: 17\n\nvoce deve usar apenas numeros entre 0 e 23 sendo    0 = 00:00 e 23 = 23:00\n\n'
    'para alterar o horario comercial final voce deve digitar "horario2_alterar" e seguir o exemplo acima\n\n mais funções serão adicionadas com o tempo...'
)
# menu suporte
menu_suporte = (
    "*SUPORTE*"
    "\n"
    "\nPor favor, envie uma mensagem detalhando seu problema:"
    "\n"
    "\nBasta enviar uma mensagem detalhando seu problema que em breve entraremos em contato."
)
menu_suporte2 = ("Infelizmente, a opção de suporte não está disponível para você, já que você não é um de nossos clientes. Por favor, vá ao MENU COMERCIAL para começar a usar nossos serviços.")

# financeiro
menu_resumo = ("Envie-nos uma menssagem detalhando o que voce deseja:")
menu_suporte_fin = ("Envie-nos uma menssagem detalhando o tipo de suporte financeiro desejado:")
# comercial locação
menu_locacao2 = (
    "*Locação*"
    "\n\nPara solicitar esse serviço, você deve enviar uma mensagem contendo as seguintes informações:"
    "\n\nInformações que precisam estar na mensagem:"
    "\n\nInformações do contratante:"
    "\n   Nome: [Seu Nome]"
    "\n   Nome da empresa: [Nome da empresa]"
    "\n   Setor da empresa: [Setor da empresa]"
    "\n   Tamanho da empresa: [número de funcionários]"
    "\n\nDetalhes do serviço:"
    "\n   Tipo de Serviço (Dados, Voz ou Ambos)"
    "\n   Número de Usuários"
    "\n   Número de Locais"
    "\n\nEquipamentos e Serviços Necessários:"
    "\n   Equipamentos de Dados (VPN, Firewall, Servidores Virtuais)"
    "\n   Equipamentos de Voz (Sip Server, Gravador de Chamadas, Aparelhos IP, URA, Gateways, Correio de Voz ou Relatórios)"
    "\n\nDescrição da infraestrutura desejada: (Descreva a infraestrutura desejada)"
    "\n\nComentários ou observações adicionais: (Opcional)"
)
comercial_cab = (
    "*Cabeamento*"
    "\n\nPara solicitar esse serviço, você deve enviar uma mensagem contendo as seguintes informações:"
    "\n\nInformações que precisam estar na mensagem:"
    "\n\nInformações do contratante:"
    "\n   Nome: [Seu Nome]"
    "\n   Nome da empresa: [Nome da empresa]"
    "\n   Setor da empresa: [Setor da empresa]"
    "\n   Tamanho da empresa: [número de funcionários]"
    "\n\nDetalhes do projeto:"
    "\n   Tipo de propriedade (residencial, comercial, industrial)"
    "\n   Tamanho da propriedade (em metros quadrados)"
    "\n   Número de andares/pisos"
    "\n   Número de salas/áreas de trabalho"
    "\n   Número de pontos de rede por sala/área"
    "\n\nNecessidades de Rede:"
    "\n   Velocidade de transmissão desejada (1 Gbps, 10 Gbps, etc.)"
    "\n   Tipo de serviço (voz, dados, vídeo)"
    "\n\nPreferências do sistema:"
    "\n   Tipo de cabo (UTP, STP, etc.)"
    "\n   Categoria do cabo (Cat5e, Cat6, Cat6a, etc.)"
    "\n   Tipo de conector (RJ45, etc.)"
    "\n   Necessidade de Patch Panels"
    "\n   Necessidade de racks ou armários"
    "\n\nComentários ou observações adicionais:(Opcional)"
)


def registrar_mensagem(numero_user, nome, mensagem, opcao_menu=None):
    log_filename = f"{log_directory}/{numero_user}_log.txt"

    current_time = datetime.datetime.now()
    log_entry = f"\nAs: {current_time}\n \nDe: {nome} ({numero_user})\n \nMensagem: {mensagem}\n"

    if opcao_menu == "None":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + "\n-------\n"

    if opcao_menu == "inicial":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_inicial_message}\n"

    if opcao_menu == "suporte1":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_suporte_tecnico_message1}\n"

    if opcao_menu == "suporte2":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_suporte_tecnico_message2}\n"

    if opcao_menu == "suporte3":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_suporte_tecnico_message3}\n"

    if opcao_menu == "financeiro":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_financeiro_message}\n"

    if opcao_menu == "comercial":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_comercial_message}"

    if opcao_menu == "VOZ":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_comercial_voz}"

    if opcao_menu == "DADOS":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_comercial_voz}"

    if opcao_menu == "SEGURANCA":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_comercial_seguranca}"

    if opcao_menu == "CABEAMENTO":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_comercial_cabeamento}"

    if opcao_menu == "LOCACAO":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_comercial_locacao}"

    if opcao_menu == "SIP SERVER":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_sip}"

    if opcao_menu == "GRAVADOR CHAMADAS":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_gravador}"

    if opcao_menu == "APARELHOS IP":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_ip}"

    if opcao_menu == "URA":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_ura}"

    if opcao_menu == "GATEWAYS":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_gateway}"

    if opcao_menu == "CORREIO DE VOZ":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_correio}"

    if opcao_menu == "RELATORIOS":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_comercial_message}"

    if opcao_menu == "VPN":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_vpn}"

    if opcao_menu == "FIREWALL":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_firewall}"

    if opcao_menu == "Virtualização":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_virtua}"

    if opcao_menu == "CFTV":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_cftv}"

    if opcao_menu == "CERCA ELETRICA'":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_cerca}"

    if opcao_menu == "ALARME":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_alarme}"

    if opcao_menu == "INFO":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_info}"

    if opcao_menu == "ADM1":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_adm1}"

    if opcao_menu == "ADM2":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_adm2}"

    if opcao_menu == "ADM3":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_adm3}"

    if opcao_menu == "Suporte Tecnico":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_suporte}"

    if opcao_menu == "suporte4":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_suporte2}"

    if opcao_menu == "Resumo de contas":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_resumo}"

    if opcao_menu == "Suporte Financeiro":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_suporte_fin}"

    if opcao_menu == "Locação":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_locacao2}"

    with open(log_filename, 'a') as log_file:
        log_file.write(log_entry + '\n')
