import pywhatkit
import datetime
import re
import time
import json
import logging
import os

# Configuração do logging para registrar eventos em um arquivo
logging.basicConfig(filename='envio_whatsapp.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def carregar_configuracao(arquivo):
    #Carrega as configurações do arquivo JSON especificado.
    if not os.path.exists(arquivo):
        logging.error("Arquivo de configuração não encontrado.")
        return None
    
    with open(arquivo, 'r') as f:
        return json.load(f)

def formatar_numero_telefone(numero):
    #Formata o número de telefone removendo caracteres não numéricos e adicionando o prefixo internacional se necessário.
    numero_formatado = re.sub(r'\D', '', numero)  # Remove tudo exceto dígitos
    if not numero_formatado.startswith('+'):
        numero_formatado = '+' + numero_formatado  # Adiciona o prefixo '+' se não estiver presente
    return numero_formatado

def validar_numero_telefone(numero):
    #Valida se o número de telefone está no formato internacional correto.
    numero = formatar_numero_telefone(numero)
    padrao = r"^\+\d{1,3}\d{8,15}$"  # Padrao: + seguido de 1 a 3 dígitos de código de país e 8 a 15 dígitos numéricos
    if re.match(padrao, numero):
        return True, numero  # Retorna True se o número for válido
    else:
        logging.error(f"Número de telefone inválido: {numero}")
        return False, numero  # Retorna False se o número for inválido

def obter_saudacao():
    #Retorna a saudação apropriada baseada na hora atual.
    hora_atual = datetime.datetime.now().hour
    if 5 <= hora_atual < 12:
        return "Bom dia"
    elif 12 <= hora_atual < 18:
        return "Boa tarde"
    else:
        return "Boa noite"

def formatar_mensagem(nome, mensagem):
    #Formata a mensagem de WhatsApp com saudação, nome e assinatura.
    saudacao = obter_saudacao()
    mensagem_formatada = f"{saudacao} {nome}!\n\n{mensagem}\n\n*Atenciosamente, Equipe de Relatórios*"
    return mensagem_formatada

def enviar_relatorio_whatsapp(destinatarios, delay_segundos):
    #Envia relatórios por WhatsApp para os destinatários listados.
    for destinatario in destinatarios:
        numero = destinatario['numero']
        nome = destinatario['nome']
        mensagem = destinatario['mensagem']
        
        valido, numero_formatado = validar_numero_telefone(numero)
        if not valido:
            continue  # Pula o destinatário se o número for inválido
        
        mensagem_formatada = formatar_mensagem(nome, mensagem)
        time.sleep(delay_segundos)  # Aguarda o delay configurado antes de enviar a próxima mensagem
        hora_atual = datetime.datetime.now()
        
        try:
            # Envia a mensagem usando pywhatkit.sendwhatmsg
            pywhatkit.sendwhatmsg(numero_formatado, mensagem_formatada, hora_atual.hour, hora_atual.minute + 1)
            logging.info(f"Mensagem para {nome} enviada com sucesso às {hora_atual.strftime('%H:%M:%S')}")
        except Exception as e:
            logging.error(f"Erro ao enviar mensagem para {nome}: {e}")

if __name__ == "__main__":
    # Carrega a configuração do arquivo JSON e inicia o envio de mensagens
    config = carregar_configuracao('config.json')
    if config:
        enviar_relatorio_whatsapp(config['destinatarios'], config['delay_segundos'])
    else:
        logging.error("Falha ao carregar a configuração.")