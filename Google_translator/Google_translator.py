from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
from langdetect import detect
import googletrans
from textblob.exceptions import NotTranslated, TranslatorError


class Google_Translator:
    def __init__(self):
        self.root=Tk()
        self.root.title("Google Translator")
        self.root.geometry("1070x400")

    def gui_translator(self):
        # Icon
        # Icon_Image=PhotoImage("Google.png")
        # root.iconphoto(False,Icon_Image)

        # Arrow
        arrow_image = PhotoImage("arrow.png")
        image_label = Label(self.root, image=arrow_image, width=150)
        image_label.place(x=460, y=50)
        self.root.arrow_image=arrow_image

        self.language = googletrans.LANGUAGES
        self.languageV = list(self.language.values())
        lang1 = self.language.keys()

        self.combo1 = ttk.Combobox(self.root, values=self.languageV)
        self.combo1.place(x=110, y=20)
        self.combo1.set("english")

        self.label1 = Label(self.root, text="English", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
        self.label1.place(x=10, y=50)

        self.f = Frame(self.root, bg="Black", bd=5)
        self.f.place(x=10, y=118, width=440, height=210)

        self.text1 = Text(self.f, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
        self.text1.place(x=0, y=0, width=430, height=200)

        scrollbar1 = Scrollbar(self.f)
        scrollbar1.pack(side="right", fill="y")
        scrollbar1.configure(command=self.text1.yview)
        self.text1.configure(yscrollcommand=scrollbar1.set)

        ##################################################################################

        self.combo2 = ttk.Combobox(self.root, values=self.languageV, font="RobotV 14", state="r")
        self.combo2.place(x=730, y=20)
        self.combo2.set("SELECT LANGUAGE")

        self.label2 = Label(self.root, text="English", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
        self.label2.place(x=620, y=50)

        self.f2 = Frame(self.root, bg="Black", bd=5)
        self.f2.place(x=620, y=118, width=440, height=210)

        self.text2 = Text(self.f2, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
        self.text2.place(x=0, y=0, width=430, height=200)

        scrollbar2 = Scrollbar(self.f2)
        scrollbar2.pack(side="right", fill="y")
        scrollbar2.configure(command=self.text2.yview)
        self.text2.configure(yscrollcommand=scrollbar2.set)

        # Translate_button
        translate = Button(self.root, text="TRANSLATE", font="Roboto 15 bold italic", activebackground="purple"
                           , cursor="hand2", bd=5, bg="red", fg="white", command=self.translate_now)
        translate.place(x=465, y=285)

        # Swap Values
        swap = Button(self.root, text="SWAP", font="Roboto 15 bold italic", activebackground="purple"
                      , cursor="hand2", bd=5, bg="red", fg="white", command=self.swap_values)
        swap.place(x=485, y=120)

    def label_change(self):
        c = self.combo1.get()
        c1 = self.combo2.get()
        self.label1.configure(text=c)
        self.label2.configure(text=c1)
        self.root.after(1000, self.label_change)

    def swap_values(self):
        value_c1 = self.combo1.get()
        value_c2 = self.combo2.get()
        vt = self.text1.get(1.0, END)
        vt2 = self.text2.get(1.0, END)

        self.label1.configure(text=value_c1)
        self.label2.configure(text=value_c2)
        self.combo1.set(value_c2)
        self.combo2.set(value_c1)
        self.text1.delete(1.0, END)
        self.text1.insert(END, vt2)
        self.text2.delete(1.0, END)
        self.text2.insert(END, vt)

    def translate_now(self):

        try:
            text_ = self.text1.get(1.0, END)
            detect_lang = detect(text_)
            c3 = self.combo2.get()
            for x, y in self.language.items():
                if y == c3:
                    self.lan_f_ = x
            text_toTransl = GoogleTranslator(src=detect_lang, target=self.lan_f_)
            text_translated = text_toTransl.translate(text_)
            self.text2.delete(1.0, END)
            self.text2.insert(END, str(text_translated))

        except Exception as e:
            messagebox.showerror("googletrans", "Error interno:")
        except NotTranslated as e:
            messagebox.showerror("Error en la traducción:", "Error en la traducción:")
        except TranslatorError as e:
            messagebox.showerror("Error en el traductor:", "Error en el traductor:")

        self.label_change()

    def run_translator(self):
        self.root.configure(bg="white")
        self.root.mainloop()

def open_translator():
    gt= Google_Translator()
    gt.gui_translator()
    gt.run_translator()



