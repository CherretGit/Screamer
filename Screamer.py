import customtkinter
from customtkinter import *
import os
import vlc
import time
from threading import Timer
import pathlib
from pathlib import Path


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

dir = Path(pathlib.Path.cwd(), 'Player')

app = customtkinter.CTk()
app.title('')
app.iconbitmap('Icon.ico')
app.geometry("700x500")


def select_video():
    file_path = filedialog.askopenfile(defaultextension=".mp4")
    global video_path
    video_path = file_path.name
    path.delete(0, END)
    path.insert(0, f'{video_path}')

def clear():
    path.delete(0, END)
    entry_time.delete(0, END)
    pin_entry.delete(0, END)
    pin_out.delete(0, END)


title = customtkinter.CTkLabel(app, text='Screamer')
title.pack()


def play():
    my_media = vlc.MediaPlayer(f"{video_path}")
    my_media.play()


def timer():
    sleep_time = int(entry_time.get())
    global pincode
    pincode = int(pin_entry.get())
    global pin
    pin = ({pincode})
    path.configure(state="disabled")
    entry_time.configure(state="disabled")
    pin_entry.configure(state="disabled")
    t = Timer(sleep_time, play)
    t.start()




def exit():
    pin_out_get = int(pin_out.get())
    if pin == {pin_out_get}:
        sys.exit(1)
    else:
        print('0')


def theme_switcher():
    if switch_var.get() == 'on':
        customtkinter.set_appearance_mode("dark")
    elif switch_var.get() == 'off':
        customtkinter.set_appearance_mode("light")

switch_var = customtkinter.StringVar(value="on")
switch = customtkinter.CTkSwitch(app, text="Dark Mode", command=theme_switcher,variable=switch_var, onvalue="on", offvalue="off")
switch.pack()

select_video = customtkinter.CTkButton(master=app, text="Select File", command=select_video)
select_video.pack(padx=10, pady=10)

play_button = customtkinter.CTkButton(master=app, text="Start Timer", command=timer)
play_button.pack(padx=10, pady=10)

clear = customtkinter.CTkButton(master=app, text="Clear", command=clear)
clear.pack(padx=10, pady=10)

path = customtkinter.CTkEntry(app, width=300, height=35)
path.insert(0, 'Path to file')
path.pack(padx=10, pady=10)

entry_time = customtkinter.CTkEntry(app, width=300, height=35)
entry_time.insert(0, 'Enter the time after which the video will play. (In seconds)')
entry_time.pack(padx=10, pady=10)

pin_entry = customtkinter.CTkEntry(app, width=300, height=35)
pin_entry.insert(0, 'Enter your PIN code to subsequently unlock the program')
pin_entry.pack(padx=10, pady=10)

pin_out = customtkinter.CTkEntry(app, width=300, height=35)
pin_out.insert(0, 'Enter password to unlock')
pin_out.pack(padx=10, pady=10)

exit = customtkinter.CTkButton(master=app, text="Exit", command=exit)
exit.pack(padx=10, pady=10)

app.mainloop()