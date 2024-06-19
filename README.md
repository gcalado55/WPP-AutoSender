# WhatsApp Auto Sender <img src="https://github.com/appicons/Whatsapp/blob/master/icons/whatsapp_194x194.png" alt="drawing" width="25"/>

Este é um script em Python para enviar automaticamente mensagens e arquivos via WhatsApp usando a biblioteca pywhatkit. Ele foi desenvolvido para facilitar o envio de relatórios diários ou outras mensagens programadas para contatos específicos via WhatsApp.

## Funcionalidades

- *Envio de Mensagens*: O script permite o envio automático de mensagens formatadas para números de telefone especificados.
- *Saudações Automáticas*: As mensagens são personalizadas com saudações adequadas ao horário do dia (Bom dia, Boa tarde, Boa noite).

## Configuração

### Passos para Configuração

1. *Instalação das Dependências*:
   - Certifique-se de ter o Python instalado em seu ambiente.
   - Instale a biblioteca pywhatkit com o seguinte comando:
     
     pip install pywhatkit
     

2. *Configuração do Arquivo config.json*:
   - Crie um arquivo config.json com as seguintes informações:
     json
     {
         "destinatarios": [
             {
                 "numero": "+5511999999999",
                 "nome": "João",
                 "mensagem": "Aqui está seu relatório diário."
             },
             {
                 "numero": "+5511888888888",
                 "nome": "Maria",
                 "mensagem": "Seu relatório está pronto."
             }
         ],
         "delay_segundos": 2
     }
     
   - Ajuste os números de telefone, nomes e mensagens que deseja enviar.

3. *Execução do Script*:
   - Execute o script enviar_whatsapp.py:
     
     python enviar_whatsapp.py
     
   - Certifique-se de que seu WhatsApp Web esteja conectado para o envio das mensagens.

## Notas Importantes

- *Formato do Número*: Os números de telefone devem seguir o formato internacional (+5511999999999).
- *WhatsApp Web*: O script depende do WhatsApp Web para enviar as mensagens. Mantenha seu WhatsApp Web aberto e não bloqueie pop-ups.
