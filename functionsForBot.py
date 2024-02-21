import requests
import credentials

def welcomeMessage(message):
    #This function return the Welcome messange.
    welcomeMessageTxt = f"<b>Bienvenid@, {message.from_user.first_name}.</b> \n" 
    welcomeMessageTxt+="Soy un bot que te va a davolver datos de la biblioteca de la <b>NASA</b>. \n \n "
    welcomeMessageTxt+="- <b>Imagen. 📸</b> \n" 
    welcomeMessageTxt+="Si quieres una imagen tomada por la <b>NASA</b> en un dia especifico usa el comando: /imagenNasa"
    welcomeMessageTxt+="\n\nSi necesitas ayuda usa el comando /help"
    return welcomeMessageTxt

def helpMesange():
    #This function return the help messange.
    helpMesangeTxt="Soy un bot que te va a davolver datos de la biblioteca de la <b>NASA</b>. \n \n "
    helpMesangeTxt+="- <b>Imagen. 📸</b> \n" 
    helpMesangeTxt+="Si quieres una imagen tomada por la <b>NASA</b> en un dia especifico usa el comando: /imagenNasa"
    return helpMesangeTxt
    
def obtainPicture_nasa(messaje):
    #We instantiate the parameters where the request will be.
    url_base = "https://api.nasa.gov/planetary/apod"
    parametros = {"api_key": credentials.apiKey(), "date": messaje}

    #Make the request to the NASA API
    respuesta = requests.get(url_base, params=parametros)

    #Check if the request was successful (status code 200)
    if respuesta.status_code == 200:
        #Return the JSON of the response
        return respuesta.json()
    elif(respuesta.status_code == 400):
        #If the date is not found in the library, it returns a message.
        return("La fecha no se encontró en la base de datos.")
    else:
        # Show an error message if the request was not successful
        return "Hubo un error en la busqueda. Intenta usar el comando /imagen nuevamente o intenta otra fecha."