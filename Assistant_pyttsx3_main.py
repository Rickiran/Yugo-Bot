import pyttsx3
import speech_recognition as sr
import time
import Instruction_excel as ie
import Instruction_open as io
import webbrowser
import os
import pandas as pd
import Instruction_Connection_DB_SAP_B1_Hana as iHana
from Python_Project.Weather_Interface import weather
###############################---HERE ARE DEFINED YUGO BOT FUNCTIONS---###########################################

def Speak(text):
    rate=100
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate',rate+50)
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()
keywords=[("hola", 1),("hey yugobot", 1),]
source = sr.Microphone()

def callback(recognizer, audio):
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        text =r.recognize_google(audio).lower()
        print(text)

        if "hola" in text or "hey yugobot":
            Speak("Hola señor, como puedo ayudarte hoy?")
            prompt()

    except sr.UnknownValueError:
        Speak("Oops No pude entenderte")

def start_recognizer():
    print("waiting for a keyword...Yugo Bot or Turn on the bot")
    r.listen_in_background(source,callback)
    time.sleep(1000000)

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        Speak("Estoy a la espera de sus comentarios")
        audio = r.listen(source)
    try:
        data = r.recognize_google(audio)
        return data
    except sr.UnknownValueError:
        print("Yugo bot no pudo entender su solicitud")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service {0}".format(e))

def prompt():

    prompt=listen_command()

    if "como estas hoy" in prompt:
            Speak("me está yendo super bien y a ti?")
    elif "modificar excel" in prompt:
        Speak("Perfecto necesito que me brindes el nombre del archivo")
        time.sleep(2)
        rf=ie.name_file()
        if rf:
            Speak("Ahora necesito en que celda deseas que lo modifiques")
            time.sleep(2)
            cm = ie.cell_location()
            Speak("Por ultimo necesito que me brindes el nuevo valor")
            time.sleep(2)
            nv = ie.new_valor()
            ie.mod_excel(cm, nv, rf)
        else:
            Speak("Archivo no encontrado por ")

    elif "reporte socio" in prompt:
        # Steps to consider making a connection to Hana
        # Take into consideration that this variables must be called at main class and execute the function
        host = ''  # Open config file located in C and take a look and fill as value in variable host
        port = 30015  # Default HANA port but you can set another one checking out config file
        user = 'throw an username'
        password = 'throw a password'
        database = 'stick a database up'
        connect = iHana.connect_hana(host, port, user, password, database)
        if connect:
            Speak("Indicame el nombre del socio de negocios a considerar")
            cn = listen_command()
            iHana.create_business_part_report(connect, cn)
        else:
            Speak("Falló en conectarse a la base de datos.")


    elif "reporte items" in prompt:
        host = ''
        port = 30015
        user = ''
        password = ''
        database = ''
        connect = iHana.connect_hana(host, port, user, password, database)
        if connect:
            Speak("Indicame el articulo a insertar por favor")
            item_name = listen_command()
            iHana.create_item_report(connect, item_name)
        else:
            Speak("Failed to connect to the database.")

    elif "abre youtube por favor" in prompt:
        Speak("Okey procederé a abrir youtube")
        webbrowser.open("http://www.youtube.com")

    elif "abre google por favor" in prompt:
        Speak("Okey procederé a abrir google")
        webbrowser.open("http://www.google.com")

    elif "abre notepad por favor" in prompt:
        Speak("Okey procederé a abrir notepad")
        os.system("notepad.exe")

    elif "reproducir musica" in prompt:
        Speak("Que musica le gustaría escuchar?")
        io.play_music()

    elif "buscar en google" in prompt:
        query = prompt.split("buscar en google")[-1].strip()
        Speak(f"Buscando {query} en Google")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    else:
        Speak("Perdon no pude entender su solicitud vuelva a intentarlo por favor")



while 1:
    start_recognizer()
###############################--HERE WILL START YUGO BOT GUI---##################################################
