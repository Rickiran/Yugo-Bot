import pyttsx3
import speech_recognition as sr
import time
import Instruction_excel as ie
import Instruction_open as io
import webbrowser
import os
import pandas as pd

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
            recognize_main()

    except sr.UnknownValueError:
        Speak("Oops No pude entenderte")

def start_recognizer():
    print("waiting for a keyword...Yugo Bot or Turn on the bot")
    r.listen_in_background(source,callback)
    time.sleep(1000000)

def recognize_main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    data=""
    try:
        data= r.recognize_google(audio)
        print("You said:" + data.lower())

        if "como estas hoy" in data:
            Speak("me está yendo super bien y a ti?")
        elif "modificar excel" in data:
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
        elif "abre youtube por favor" in data:
            Speak("Okey procederé a abrir youtube")
            webbrowser.open("http://www.youtube.com")

        elif "abre google por favor" in data:
            Speak("Okey procederé a abrir google")
            webbrowser.open("http://www.google.com")

        elif "abre notepad por favor" in data:
            Speak("Okey procederé a abrir notepad")
            os.system("notepad.exe")

        elif "reproducir musica" in data:
            Speak("Que musica le gustaría escuchar?")
            io.play_music()

        elif "buscar en google" in data:
            query = data.split("buscar en google")[-1].strip()
            Speak(f"Buscando {query} en Google")
            webbrowser.open(f"https://www.google.com/search?q={query}")

        else:
            Speak("Perdon no pude entender su solicitud vuelva a intentarlo por favor")

    except sr.UnknownValueError:
        print("Yugo bot no pudo entender su solicitud")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service {0}".format(e))

while 1:
    start_recognizer()