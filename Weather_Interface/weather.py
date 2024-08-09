from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

class WeatherInterface:
    def __init__(self):
        self.root = Tk()
        self.root.title("App de Clima - Rick")
        self.root.geometry("900x500+300+200")
        self.root.resizable(False, False)
        self.setup_ui()

    def setup_ui(self):
        # searchbox
        Search_image = PhotoImage(file="Weather_Interface/box.png")
        myimage = Label(self.root, image=Search_image)
        myimage.place(x=20, y=20)
        self.root.Search_image = Search_image

        self.textfield = tk.Entry(self.root, justify="center", width=33, font=("poppins", 15, "bold"), bg="#33FFA5", border=0, fg="white")
        self.textfield.place(x=38, y=32)
        self.textfield.focus()

        search_icon = PhotoImage(file="Weather_Interface/rf.png")
        myimage_icon = Button(self.root, image=search_icon, borderwidth=0, cursor="hand2", bg="#33FFA5", command=self.getWeather)
        myimage_icon.place(x=400, y=34)
        self.root.search_icon = search_icon

        # Logo
        Logo_image = PhotoImage(file="Weather_Interface/weather.png")
        logo = Label(self.root, image=Logo_image)
        logo.place(x=150, y=140)
        self.root.Logo_image = Logo_image

        # Time
        self.Time = Label(self.root, font=("arial", 15, "bold"))
        self.Time.place(x=30, y=100)
        self.clock = Label(self.root, font=("Helvetica", 20))
        self.clock.place(x=30, y=130)

        # bottom box
        Frame_image = PhotoImage(file="Weather_Interface/bottom_box.png")
        Frame_myImage = Label(self.root, image=Frame_image)
        Frame_myImage.pack(padx=5, pady=5, side=BOTTOM)
        Frame_myImage.place(x=49, y=320)
        self.root.Frame_image = Frame_image

        # labels
        labels = [("VIENTO", 120, 370), ("HUMEDAD", 250, 370), ("DESCRIPCIÓN", 430, 370), ("PRESIÓN", 650, 370)]
        for text, x, y in labels:
            label = Label(self.root, text=text, font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
            label.place(x=x, y=y)

        self.t = Label(font=("arial", 70, "bold"), fg="#ee666d")
        self.t.place(x=400, y=150)
        self.c = Label(font=("arial", 15, "bold"))
        self.c.place(x=400, y=250)

        self.w = Label(text="....", font=("arial", 20, "bold"), bg="#1ab5ef")
        self.w.place(x=120, y=410)

        self.h = Label(text="....", font=("arial", 20, "bold"), bg="#1ab5ef")
        self.h.place(x=280, y=410)

        self.d = Label(text="....", font=("arial", 20, "bold"), bg="#1ab5ef")
        self.d.place(x=450, y=410)

        self.p = Label(text="....", font=("arial", 20, "bold"), bg="#1ab5ef")
        self.p.place(x=670, y=410)

    def getWeather(self):
        try:
            city = self.textfield.get()
            geolocator = Nominatim(user_agent="geoapiExercises")
            location = geolocator.geocode(city)
            obj = TimezoneFinder()
            result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

            home = pytz.timezone(result)
            local_time = datetime.now(home)
            current_time = local_time.strftime("%I: %M: %p")
            self.clock.config(text=current_time)
            self.Time.config(text="CLIMA ACTUAL:")

            # Weather
            api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=36b57fc6d1fa6bc939c1ef5aa3962b10"

            json_data = requests.get(api).json()
            condition = json_data['weather'][0]['main']
            description = json_data['weather'][0]['description']
            temp = int(json_data['main']['temp'] - 273.15)
            pressure = json_data['main']['pressure']
            humidity = json_data['main']['humidity']
            wind = json_data['wind']['speed']

            self.t.config(text=(temp, "°"))
            self.c.config(text=(condition, "|", "Temperatura:", temp, "°"))

            self.w.config(text=wind)
            self.h.config(text=humidity)
            self.d.config(text=description)
            self.p.config(text=pressure)

        except Exception as e:
            messagebox.showerror("App de Clima", "Dato inválido")

    def run(self):
        self.root.mainloop()

def open_weather_interface():
    interface = WeatherInterface()
    interface.run()

