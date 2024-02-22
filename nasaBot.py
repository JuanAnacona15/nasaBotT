#QImport the librarys
import telebot
#Import the modules
import functionsForBot
import credentials
import requests
from flask import Flask, request 
import time

#Obtain the Token
TOKEN = credentials.token()

#Initialize bot
bot = telebot.TeleBot(TOKEN)

webServer = Flask(__name__)

@webServer.route('/', methods=['POST'])
def webHook():
    if request.headers.get("content-type") == "aplication/json":
        update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
        bot.process_new_updates([update])
    return "Ok", 200

def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    data = response.json()
    return data['ip']

#Function to respond to the /start command
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, 
                 functionsForBot.welcomeMessage(message),
                 parse_mode='html')

#Function to respond to the /help command
@bot.message_handler(commands=['help'])
def handle_start(message):
    bot.reply_to(message, 
                 functionsForBot.helpMesange(),
                 parse_mode='html')
    
#Function to respond to the /imagenNasa command 
@bot.message_handler(commands=['imagenNasa'])
def handle_imagenNasa(message):
    msg = bot.send_message(message.chat.id, "Escribe y la fecha de la imagen en formato <b>Año-Mes-Día.</b>\n<b>Ejemplo: </b>2008-01-13 \n<code>Si no recibes una respuesta, intenta de nuevo o usa otra fecha</code>", parse_mode='HTML')    
    bot.register_next_step_handler(msg, send_image)
    
#Funcion que llama envia la imagen al usuario
def send_image(message):
    resp = functionsForBot.obtainPicture_nasa(message.text)
    if type(resp) == str:
        bot.send_message(message.chat.id, resp)
    else:
        label = f"<b>{resp['title']}</b> \n"
        label += f"<code>{resp['date']}</code> \n"
        label += f"{resp['explanation']} \n"
        bot.send_photo(message.chat.id, resp["url"], label, parse_mode='HTML')

#This function handles any messages or text type.
@bot.message_handler(content_types=['text'])
def send_messages(message):
    #If the user is trying to invoke a command that is not in the library, send a message.
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "El comando que enviaste no está disponible")
    #Send the help message.
    bot.send_message(message.chat.id, functionsForBot.helpMesange(), parse_mode='HTML')

    
if __name__ == "__main__":
    print("Bot iniciado -/- -/- -/- -/- -/- -/- -/- -/- -/- -/- -/- -/- -/- -/- -/- -/- -/- -/- -/- -/-")
    severUrl = get_public_ip()
    print("Url del servidor: ", severUrl)
    bot.remove_webhook()
    time.sleep(1)
    bot.set_webhook(url=severUrl)
    webServer.run(host="0.0.0.0", port=443)
