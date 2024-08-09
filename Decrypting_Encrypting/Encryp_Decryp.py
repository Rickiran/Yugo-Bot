from tkinter import *
from tkinter import Tk
from tkinter import messagebox
import base64
import os


class Encryp_Decryp:
    def __init__(self):
        self.screen =Tk()
        self.screen.geometry("375x398")
        self.screen.title("PctApp")

    def reset(self):
         self.code.set("")
         self.text1.delete(1.0,END)

    def Encryp_Decryp_GUI(self):
        Label(text="Enter text for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=10)
        self.text1 = (Text(font="Robote 20", bg="white", relief=GROOVE, wrap=WORD, bd=0))
        self.text1.place(x=10, y=50, width=355, height=100)

        Label(text="Enter a secret key for encryption a decryption", fg="black", font=("calibri", 13)).place(x=10,
                                                                                                             y=170)

        self.code = StringVar()
        Entry(textvariable=self.code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)

        Button(text="ENCRYPT", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=self.encrypt).place(x=10, y=250)
        Button(text="DECRYPT", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=self.decrypt).place(x=200,
                                                                                                            y=250)
        Button(text="RESET", height="2", width=50, bg="#1089ff", fg="white", bd=0, command=self.reset).place(x=10, y=300)


    def decrypt(self):
        password = self.code.get()

        if password == "1234":
            screen2 = Toplevel(self.screen)
            screen2.title("Decryption")
            screen2.geometry("400x200")
            screen2.configure(bg="#00bd56")

            message = self.text1.get(1.0, END)
            decode_message = message.encode("ascii")
            base64_bytes = base64.b64decode(decode_message)
            decrypt = base64_bytes.decode("ascii")

            Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
            text2 = (Text(screen2, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0))
            text2.place(x=10, y=40, width=380, height=150)

            text2.insert(END, decrypt)

        elif password == "":
            messagebox.showerror("Encryption", "Input Password")
        elif password != "1234":
            messagebox.showerror("Encryption", "Invalid Password")

    def encrypt(self):
        password = self.code.get()

        if password == "1234":
            screen1 = Toplevel(self.screen)
            screen1.title("Encryption")
            screen1.geometry("400x200")
            screen1.configure(bg="#ed3833")

            message = self.text1.get(1.0, END)
            encode_message = message.encode("ascii")
            base64_bytes = base64.b64encode(encode_message)
            encrypt = base64_bytes.decode("ascii")

            Label(screen1, text="ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
            text3 = (Text(screen1, font="Robote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0))
            text3.place(x=10, y=40, width=380, height=150)
            text3.insert(END, encrypt)

        elif password == "":
            messagebox.showerror("Encryption", "Input Password")
        elif password != "1234":
            messagebox.showerror("Encryption", "Invalid Password")
    def run_Encryp_Decryp(self):
        self.screen.mainloop()

def open_Encryp_Decryp():
    oed=Encryp_Decryp()
    oed.Encryp_Decryp_GUI()
    oed.run_Encryp_Decryp()





