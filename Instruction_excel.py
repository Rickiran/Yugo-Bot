import openpyxl
import speech_recognition as sr
import openpyxl as op
import os

r = sr.Recognizer()

def get_prompt(prompt):
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print(prompt)
        audio=r.listen(source)
    try:
        prompt=r.recognize_google(audio)
        return prompt
    except sr.UnknownValueError:
        print("Valor ingresado no reconocido")
        return ""



def name_file():
    file_name=get_prompt("Ingrese el nombre del archivo")
    list_path = []
    start_path="C:\\Users\\Default\\Downloads"
    if file_name:
        for file in os.walk(start_path):
            list_path.append(os.path.join(start_path,file_name))
            return list_path[0]
        else:
            print("Ruta no encontrada por favor intentelo otra vez")
            return ""
    else:
        print("Ruta no encontrada por favor intentelo otra vez")

def new_valor():
    return get_prompt("Ingrese el valor a modificar en el archivo")
def cell_location():
    return get_prompt("Ingrese la celda a modificar en el archivo")
def mod_excel(cm,nv,rf):
    try:
        wb=openpyxl.load_workbook(f"{rf}")
        ws=wb.active
        ws[cm]=nv
        wb.save(rf)
        print("Archivo exitosamente modificado!")
    except Exception as e:
        print("Hubo un error intentelo mas tarde")
