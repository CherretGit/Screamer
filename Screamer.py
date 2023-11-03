import customtkinter
from customtkinter import *
import os
import vlc
import time
from threading import Timer


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


app = customtkinter.CTk()
app.title('')
app.iconbitmap('Icon.ico')
app.geometry("1000x800")
app.resizable(width=False, height=False)


def select_video():
    file_path = filedialog.askopenfile()
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
    fullscreen = True
    if switch_var_fullscreen.get() == 'on':
        fullscreen = True
    elif switch_var_fullscreen.get() == 'off':
        fullscreen = False
    vlc_instance = vlc.Instance()
    player = vlc_instance.media_player_new()
    if fullscreen == True:
        player.set_fullscreen(True)
    elif fullscreen == False:
        player.set_fullscreen(False)
    player.set_mrl(f'{video_path}')
    player.play()
    time.sleep(0.1)
    length_min = int(player.get_length())
    length = length_min/1000
    exit_timer = Timer(length, exit_function)
    exit_timer.start()


def timer():
    sleep_time = int(entry_time.get())
    global pincode
    pincode = int(pin_entry.get())
    global pin
    pin = ({pincode})
    path.delete(0, END)
    entry_time.delete(0, END)
    pin_entry.delete(0, END)
    pin_out.delete(0, END)
    select_video.configure(state="disabled")
    play_button.configure(state="disabled")
    clear.configure(state="disabled")
    path.configure(state="disabled")
    entry_time.configure(state="disabled")
    pin_entry.configure(state="disabled")
    switch_fullscreen.configure(state="disabled")
    pin_out.configure(state="normal")
    global t
    t = Timer(sleep_time, play)
    t.start()


def exit_function():
    os.abort()


def stop():
    pin_out_get = int(pin_out.get())
    if pin == {pin_out_get}:
        t.cancel()
        pin_out.delete(0, END)
        select_video.configure(state="normal")
        play_button.configure(state="normal")
        clear.configure(state="normal")
        path.configure(state="normal")
        entry_time.configure(state="normal")
        pin_entry.configure(state="normal")
        switch_fullscreen.configure(state="normal")
        pin_out.configure(state="disabled")


def theme_switcher():
    if switch_var.get() == 'on':
        customtkinter.set_appearance_mode("dark")
    elif switch_var.get() == 'off':
        customtkinter.set_appearance_mode("light")



switch_var = customtkinter.StringVar(value="on")
switch = customtkinter.CTkSwitch(app, text="Dark Mode", command=theme_switcher,variable=switch_var, onvalue="on", offvalue="off")
switch.pack()

switch_var_fullscreen = customtkinter.StringVar(value="on")
switch_fullscreen = customtkinter.CTkSwitch(app, text="Full Screen", variable=switch_var_fullscreen, onvalue="on", offvalue="off")
switch_fullscreen.pack()

select_video = customtkinter.CTkButton(master=app, text="Select File", command=select_video)
select_video.pack(padx=10, pady=10)

play_button = customtkinter.CTkButton(master=app, text="Start Timer", command=timer)
play_button.pack(padx=10, pady=10)

clear = customtkinter.CTkButton(master=app, text="Clear", command=clear)
clear.pack(padx=10, pady=10)

path_title = customtkinter.CTkLabel(app, text='Path to file')
path_title.pack()
path = customtkinter.CTkEntry(app, width=300, height=35)
path.pack(padx=10, pady=10)

entry_time_title = customtkinter.CTkLabel(app, text='Enter the time after which the video will play. (In seconds)')
entry_time_title.pack()
entry_time = customtkinter.CTkEntry(app, width=300, height=35)
entry_time.pack(padx=10, pady=10)

pin_entry_title = customtkinter.CTkLabel(app, text='Enter your PIN code to subsequently unlock the program')
pin_entry_title.pack()
pin_entry = customtkinter.CTkEntry(app, width=300, height=35)
pin_entry.pack(padx=10, pady=10)

pin_out_title = customtkinter.CTkLabel(app, text='Enter password to unlock')
pin_out_title.pack()
pin_out = customtkinter.CTkEntry(app, width=300, height=35, state=DISABLED)
pin_out.pack(padx=10, pady=10)

stop_timer = customtkinter.CTkButton(master=app, text="Stop Timer", command=stop)
stop_timer.pack(padx=10, pady=10)

def rename_window():
    new_name = rename_window_entry.get()
    app.title(new_name)

def reset_window_name():
    rename_window_entry.delete(0, END)
    app.title('')

def rename_window_widgets():
    if switch_var_rename.get() == 'on':
        global rename_window_entry
        global rename_window_button
        global reset_button
        rename_window_entry = customtkinter.CTkEntry(app, width=300, height=35)
        rename_window_entry.pack(padx=10, pady=10)
        rename_window_button = customtkinter.CTkButton(app, text='Rename', command=rename_window)
        rename_window_button.pack(padx=10, pady=10)
        reset_button = customtkinter.CTkButton(app, text='Reset Window Name', command=reset_window_name)
        reset_button.pack(padx=10, pady=10)
    elif switch_var_rename.get() == 'off':
        rename_window_entry.destroy()
        rename_window_button.destroy()
        reset_button.destroy()


switch_var_rename = customtkinter.StringVar(value="off")
switch = customtkinter.CTkSwitch(app, text="Enable rename window", command=rename_window_widgets,variable=switch_var_rename, onvalue="on", offvalue="off")
switch.pack()


app.mainloop()