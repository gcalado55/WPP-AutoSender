import pywhatkit
import datetime
import re
import time
import json
import logging
import os

# Configurações de Log
# Configura o sistema de logging para registrar mensagens em um arquivo de log.
logging.basicConfig(filename='envio_whatsapp.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Função para carregar as configurações de um arquivo JSON
def carregar_configuracao(arquivo):
    # Verifica se o arquivo existe
    if not os.path.exists(arquivo):
        logging.error("Arquivo de configuração não encontrado.")
        return None
    
    # Abre o arquivo e carrega o conteúdo JSON
    with open(arquivo, 'r') as f:
        return json.load(f)

# Função para validar um número de telefone usando uma expressão regular
def validar_numero_telefone(numero):
    # Padrão de regex para um número de telefone internacional
    padrao = r"^\+\d{1,3}\d{8,15}$"
    # Verifica se o número corresponde ao padrão
    if re.match(padrao, numero):
        return True
    else:
        logging.error(f"Número de telefone inválido: {numero}")
        return False

# Função para obter a saudação adequada baseada na hora do dia
def obter_saudacao():
    hora_atual = datetime.datetime.now().hour
    if 5 <= hora_atual < 12:
        return "Bom dia"
    elif 12 <= hora_atual < 18:
        return "Boa tarde"
    else:
        return "Boa noite"

# Função para formatar a mensagem a ser enviada
def formatar_mensagem(nome, mensagem):
    saudacao = obter_saudacao()
    mensagem_formatada = f"{saudacao} {nome}!\n\n{mensagem}\n\n*Atenciosamente, Equipe de Relatórios*"
    return mensagem_formatada

# Função para enviar mensagens de WhatsApp
def enviar_relatorio_whatsapp(destinatarios, delay_segundos):
    for destinatario in destinatarios:
        numero = destinatario['numero']
        nome = destinatario['nome']
        mensagem = destinatario['mensagem']
        
        # Valida o número de telefone antes de enviar a mensagem
        if not validar_numero_telefone(numero):
            continue

        # Formata a mensagem
        mensagem_formatada = formatar_mensagem(nome, mensagem)
        
        # Espera pelo número de segundos especificado
        time.sleep(delay_segundos)
        hora_atual = datetime.datetime.now()
        
        try:
            # Envia a mensagem usando pywhatkit
            pywhatkit.sendwhatmsg(numero, mensagem_formatada, hora_atual.hour, hora_atual.minute + 1)
            logging.info(f"Mensagem para {nome} enviada com sucesso às {hora_atual.strftime('%H:%M:%S')}")
        except Exception as e:
            logging.error(f"Erro ao enviar mensagem para {nome}: {e}")

# Execução principal do script
if __name__ == "__main__":
    # Carrega as configurações do arquivo JSON
    config = carregar_configuracao('config.json')
    if config:
        # Envia os relatórios via WhatsApp se a configuração foi carregada com sucesso
        enviar_relatorio_whatsapp(config['destinatarios'], config['delay_segundos'])
    else:
        logging.error("Falha ao carregar a configuração.")