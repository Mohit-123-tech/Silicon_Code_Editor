from tkinter import *
from modules.Apprunner import Apprun, CodeRunner
import os
import json
import datetime
import sqlite3
import random

# Connect With Database
try:
    global c
    con = sqlite3.connect("src/database/Appdata.db")
    c = con.cursor()
    print("Connection Sucsses Fully")
except(Exception):
    try:
        con = sqlite3.connect("database/Appdata.db")
        c = con.cursor()
        print("Connection Sucsses Fully")
    except(Exception):
        print("Connection Feiled")

# Connect With Json File
try:
    data = open(file="src/json/api.json")
    js = json.load(data)
    print("Json File Connected")
except(Exception):
    try:
        data = open(file="json/api.json")
        js = json.load(data)
        print("Json File Connected")
    except(Exception):
        print("File Not Found")

# Json Odjects
FontColor = js["FontColor"]
Background = js["Background"]
Resizable = js["Resizable"]
Title = js["Title"]
Font = js["Font"]
FontSize = js["FontSize"]
Path = js["Path"]
Date = datetime.date.today()
Cli = js["Terminal"]
UserData = js["developerData"]
version = js["Version"]

AR = Apprun()
AR0 = CodeRunner()


# App Functions Class
class AppRunner():
    # Save Data Window And Insert FileName In DataBase
    def saveData(self):
        kali = Tk()
        kali.geometry('200x100')
        kali.configure(bg='black')
        kali.title(Title)
        kali.resizable(False, False)
        Label(kali, text='File Name', bg='yellow', fg='green').pack()
        global fileName
        fileName = Entry(kali, borderwidth=0)
        fileName.pack()
        global bt

        # Button Function Create File & Save
        def bt():
            try:
                global fileN, codeData
                fileN = fileName.get()
                os.system(f'touch {fileN}')
                codeData = EnterText.get(1.0, END)
                with open(f'{fileN}', 'w') as f:
                    print(f.write(codeData))
                    f.close()
                os.system(f'mv {fileN} {Path}')
                try:
                    with open(f"src/doc/Filename.txt", "w") as f:
                        f.write(fileN)
                        f.close()
                except(Exception):
                    pass

                try:
                    c.execute(f"""INSERT INTO UserFiles VALUES (
                        '{Date}',
                        '{fileN}'
                    )""")
                    con.commit()
                    con.close()
                except(Exception):
                    pass
                kali.destroy()
            except(Exception):
                print("File Not Found")

        bt1 = Button(kali, borderwidth=0, text='Save File',
                     bg='black', fg='red', activebackground='lime', command=bt)
        bt1.pack(side=BOTTOM)

        kali.mainloop()

    # Encrypt File Data
    def encrypt(self):
        AR.enc(Path, fileN, fileN)

    # Decrypt File Data
    def decrypt(self):
        AR.dec(Path, fileN, fileN)

    # Clear Inputed Data
    def clearData(self):
        EnterText.delete(1.0, END)

    # Open Your Terminal
    def terminal(self):
        os.system(f'cd {Path} && {Cli}')

    def help(self):
        window2 = Tk()
        window2.geometry('300x100')
        window2.title(Title)
        window2.configure(bg='black')
        window2.resizable(False, False)
        Label(window2, text="Version: "+version, bg='yellow', fg='red').pack()
        window2.mainloop()

    # Save File Data

    def saveFile(self):
        try:
            codeDataTwo = EnterText.get(1.0, END)
            with open(f'{fileN}', 'w') as f:
                print(f.write(codeDataTwo))
                f.close()
            os.system(f"mv {fileN} {Path}")
        except(Exception):
            pass

    def AppJson(self):
        window4 = Tk()
        window4.geometry('500x500')
        window4.configure(bg=Background)
        window4.title(Title)
        window4.resizable(False, False)
        
        try:
            with open('src/json/api.json', 'r') as f:
                global rd
                rd = f.read()
                f.close()
        except(Exception):
            pass

        t = Text(window4, bg=Background, fg=FontColor, font=(Font, FontSize), inactiveselectbackground='green', insertbackground='green', selectbackground='yellow')
        t.pack()
        t.insert(0.1, rd)

        def saveChanges():
            code = t.get(0.1, END)
            try:
                with open('src/json/api.json', 'w') as f:
                    print(f.write(code))
                    f.close()
            except(Exception):
                pass
            window4.destroy()

        b1 = Button(window4, text='Save Changes', bg='black', fg='red', activebackground='lime', command=saveChanges)
        b1.pack()

        window4.mainloop()


    # Open File In App
    def ope(self):
        window3 = Tk()
        window3.geometry('200x100')
        window3.configure(bg='black')
        window3.title(Title)
        window3.resizable(False, False)
        Label(window3, text='Enter file path',
              background='yellow', fg='red').pack()
        e1 = Entry(window3)
        e1.pack()

        # Internal Open Function
        def pat():
            try:
                global fdata
                e = e1.get()
                with open(f'{e}', 'r') as re:
                    fdata = re.read()
                    re.close()
                EnterText.insert(0.1, fdata)
                os.system(f'cp {e} {Path}')
                window3.destroy()
            except(Exception):
                print("File Not Found")

        b = Button(window3, borderwidth=0, text='Summit', bg='black',
                   fg='red', activebackground='lime', command=pat)
        b.pack(side=BOTTOM)

        window3.mainloop()

    # Make Qrcode With Random Name
    def qr(self):
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        num = '1234567890'
        lenght = 6
        all = num+alpha
        try:
            fname = ''.join(random.sample(all, lenght))
            textdata = EnterText.get(1.0, END)
            AR.makeqr(textdata, fname)
            os.system(f'mv {fname}.png {Path}')
        except(Exception):
            print(f"Qr Not Make")

    #reade the file data
    def fileData(self):
        window1 = Tk()
        window1.geometry('1000x550')
        window1.title(Title)
        window1.configure(bg='black')
        window1.resizable(False, False)
        Label(window1, text='Enter file path', bg='yellow', fg='red').pack(fill=X)
        e1 = Entry(window1)
        e1.pack()
        et = Text(window1, bg='black', fg='lime', font='hack')
        et.pack(fill=X)
        def readFile():
            filer = e1.get()
            try:
                data = open(f'{filer}', 'r')
                fd = data.read()
            except(Exception):
                pass
            et.insert(1.0, fd)

        bt = Button(window1, text='read_file', fg='red', bg='black', activebackground='lime', command=readFile)
        bt.pack(side=BOTTOM)
    
        window1.mainloop()



Ar1 = AppRunner()


class code(Tk):
    # Start Make App Form This Function
    def App(self):
        # input text or code data in App
        global EnterText
        EnterText = Text(width=500, borderwidth=0, height=500, bg=Background, fg=FontColor, font=(
            Font, FontSize), insertbackground=FontColor, selectbackground="yellow", selectforeground="red")
        EnterText.pack()

        mainloop()


Ap = code()

Ap.title(Title)
Ap.resizable(Resizable, Resizable)
Ap.geometry("1000x650")
Ap.configure(bg=Background)

# Create Manu In App
MainMenu = Menu(bg=Background, borderwidth=0,
                fg=FontColor, activebackground=FontColor)
m1 = Menu(MainMenu, bg=Background, borderwidth=0,
          fg=FontColor, activebackground=FontColor, tearoff=0)
MainMenu.add_cascade(label="File", menu=m1)
m1.add_command(label="Open", command=Ar1.ope)
m1.add_command(label="Save", command=Ar1.saveFile)
m1.add_command(label="Save as", command=Ar1.saveData)

m3 = Menu(MainMenu, bg=Background, borderwidth=0,
          fg=FontColor, activebackground=FontColor, tearoff=0)
m1.add_cascade(label="Encrypter", menu=m3)
m3.add_command(label="Makeqr", command=Ar1.qr)
m3.add_command(label="EncryptData", command=Ar1.encrypt)
m3.add_command(label="DecryptData", command=Ar1.decrypt)

m1.add_separator()
m1.add_command(label="Clear", command=Ar1.clearData)
m1.add_command(label="Exit", command=quit)

m2 = Menu(MainMenu, bg=Background, borderwidth=0,
          fg=FontColor, activebackground=FontColor, tearoff=0)
MainMenu.add_cascade(label="CodeRunner", menu=m2)
m2.add_command(label="Python", command=AR0.Python)
m2.add_command(label="Cpp", command=AR0.cpp)
m2.add_command(label="Java", command=AR0.java)
m2.add_command(label="Html", command=AR0.html)
m2.add_command(label="JavaScript", command=AR0.javaScript)
m2.add_command(label="C", command=AR0.c)

MainMenu.add_command(label="Terminal", command=Ar1.terminal)
MainMenu.add_command(label="Show_File_Data", command=Ar1.fileData)

m4 = Menu(MainMenu, bg=Background, borderwidth=0,
          fg=FontColor, activebackground=FontColor, tearoff=0)
MainMenu.add_cascade(label="Date", menu=m4)
m4.add_command(label=Date)

MainMenu.add_command(label="App Json", command=Ar1.AppJson)
MainMenu.add_command(label="About!", command=Ar1.help)
Ap.config(menu=MainMenu)

# App Logo
try:
    icon = PhotoImage(file="src/icon/ico2.png")
    Ap.iconphoto(False, icon)
    print("icon is set")
except(Exception):
    try:
        icon = PhotoImage(file="icon/ico2.png")
        Ap.iconphoto(False, icon)
        print("icon is set")
    except(Exception):
        print("Icon Not Found")
print("all system is working")

# Start App
Ap.App()
os.system("clear")
