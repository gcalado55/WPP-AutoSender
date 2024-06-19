import pywhatkit
import datetime

def enviar_relatorio_whatsapp(numero, mensagem):
    # Pega a hora e minuto atual
    hora_atual = datetime.datetime.now()
    
    try:
        # Calcula a hora e minuto para envio da mensagem
        hora_envio = hora_atual + datetime.timedelta(seconds==1)
        hora = hora_envio.hour
        minuto = hora_envio.minute

        # Envia a mensagem
        pywhatkit.sendwhatmsg(numero, mensagem, hora, minuto)
        print(f"Mensagem agendada para {hora_envio.strftime('%H:%M')} com sucesso!")
    except Exception as e:
        print("Ocorreu um erro ao enviar a mensagem:", e)

# Número do destinatário (deve começar com código do país, ex: '+5511999999999')
numero_destinatario = '+5581987822580'
# Mensagem que você quer enviar
mensagem_relatorio = 'Olá! Aqui está seu relatório diário.'

enviar_relatorio_whatsapp(numero_destinatario, mensagem_relatorio)