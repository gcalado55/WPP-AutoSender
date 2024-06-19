import pywhatkit
import datetime
import re
import time

def validar_numero_telefone(numero):
    # Verifica se o número está no formato correto (+5511999999999)
    padrao = r"^\+\d{1,3}\d{8,15}$"
    if re.match(padrao, numero):
        return True
    else:
        print("Número de telefone inválido. Certifique-se de usar o formato correto.")
        return False

def obter_saudacao():
    # Obtém a hora atual
    hora_atual = datetime.datetime.now().hour

    # Define a saudação com base na hora do dia
    if 5 <= hora_atual < 12:
        return "Bom dia"
    elif 12 <= hora_atual < 18:
        return "Boa tarde"
    else:
        return "Boa noite"

def formatar_mensagem(nome, mensagem):
    # Obtém a saudação apropriada
    saudacao = obter_saudacao()
    # Adiciona formatação à mensagem
    mensagem_formatada = f"{saudacao} {nome}!\n\n{mensagem}\n\n*Atenciosamente, Equipe de Relatórios*"
    return mensagem_formatada

def enviar_relatorio_whatsapp(numero, nome, mensagem, delay_segundos):
    if not validar_numero_telefone(numero):
        return

    # Formata a mensagem
    mensagem_formatada = formatar_mensagem(nome, mensagem)

    # Aguarda o tempo especificado (em segundos)
    time.sleep(delay_segundos)
    
    # Pega a hora e minuto atual
    hora_atual = datetime.datetime.now()
    
    try:
        # Envia a mensagem
        pywhatkit.sendwhatmsg(numero, mensagem_formatada, hora_atual.hour, hora_atual.minute + 1)
        print(f"Mensagem enviada com sucesso às {hora_atual.strftime('%H:%M:%S')}!")
    except Exception as e:
        print("Ocorreu um erro ao enviar a mensagem:", e)

# Número do destinatário (deve começar com código do país, ex: '+5511999999999')
numero_destinatario = '+5581996959564'
# Nome do destinatário
nome_destinatario = 'Michelle Sá'
# Mensagem a ser enviada
mensagem_relatorio = 'Aqui está seu relatório diário.'

# Tempo de espera em segundos
delay_segundos = 2

enviar_relatorio_whatsapp(numero_destinatario, nome_destinatario, mensagem_relatorio, delay_segundos)