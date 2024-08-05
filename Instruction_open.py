import speech_recognition as sr
import Assistant_pyttsx3_main as am
import webbrowser

def play_music():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        am.Speak("Please throw something...:")
        audio=r.listen(source)

    try:
        song =r.recognize_google(audio)
        am.Speak(f"Tocando {song} en YouTube")
        webbrowser.open(f"https://www.youtube.com/results?search_query={song}")
    except sr.UnknownValueError:
        am.Speak("Perdon no pude entender su solicitud intentelo otra vez")
    except sr.RequestError as e:
        am.Speak(f"No se obtuvo respuesta del servicio google; {e}")
