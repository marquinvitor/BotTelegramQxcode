import telebot
import schedule
import threading
import json


def CarregarConfig():
    with open('Bot/tokens.json', 'r') as f:
        return json.load(f)
    
config = CarregarConfig()
botToken = config['BOT_TOKEN']
chat_id = config['CHAT_ID']
topicoId = config.get('TOPICO_ID')

bot = telebot.TeleBot(botToken)


def enviarLembrete():
    textoLembrete = "Não esqueçam de responder o diário de turmas!!!"
    bot.send_message(chat_id, textoLembrete, message_thread_id=topicoId)
    print("mensagem enviada com sucesso")


horarioAgendado = "19:00" 
schedule.every().monday.at(horarioAgendado).do(enviarLembrete)
schedule.every().tuesday.at(horarioAgendado).do(enviarLembrete)
schedule.every().wednesday.at(horarioAgendado).do(enviarLembrete)
schedule.every().thursday.at(horarioAgendado).do(enviarLembrete)
schedule.every().friday.at(horarioAgendado).do(enviarLembrete)
schedule.every().saturday.at(horarioAgendado).do(enviarLembrete)

def rodarAgendador():
    while True:
        schedule.run_pending()
        


if __name__ == "__main__":
    print("iniciando bot")

    threadAgendador = threading.Thread(target=rodarAgendador)
    threadAgendador.daemon = True
    threadAgendador.start()
    bot.infinity_polling()

