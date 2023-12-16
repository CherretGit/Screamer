import customtkinter
from customtkinter import *
from PIL import Image
import os
import vlc
import time
from threading import Timer


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
assets_path = os.path.join(sys._MEIPASS, 'Assets') if getattr(sys, 'frozen', False) else 'Assets'

app = customtkinter.CTk()
app.title('')
app.iconbitmap(f'{assets_path}/Icon.ico')
app.geometry("600x300")
app.resizable(width=False, height=False)


def select_video():
    file_path = filedialog.askopenfile()
    video_path = file_path.name
    path.delete(0, END)
    path.insert(0, f'{video_path}')

def clear():
    path.delete(0, END)
    entry_time.delete(0, END)
    pin_entry.delete(0, END)


def play():
    vlc_instance = vlc.Instance()
    player = vlc_instance.media_player_new()
    player.set_mrl(f'{video_path}')
    if 'switch_var_fs' not in globals():
        player.set_fullscreen(True)
    elif switch_var_fs == 'on':
        player.set_fullscreen(True)
    elif switch_var_fs == 'off':
        player.set_fullscreen(False)
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
    global video_path
    video_path = (path.get())
    path.delete(0, END)
    entry_time.delete(0, END)
    pin_entry.delete(0, END)
    title.destroy()
    settings_button_enter.destroy()
    select_video_button.destroy()
    play_button.destroy()
    path.destroy()
    entry_time.destroy()
    pin_entry.destroy()
    path_title.destroy()
    entry_time_title.destroy()
    pin_entry_title.destroy()
    clear.destroy()
    stop_timer_window()
    global t
    t = Timer(sleep_time, play)
    t.start()

def stop_timer_window():
    global pin_out_title
    pin_out_title = customtkinter.CTkLabel(app, text='Enter password to stop timer')
    pin_out_title.place(x= 220, y = 10)
    global pin_out
    pin_out = customtkinter.CTkEntry(app, width=200, height=35)
    pin_out.place(x= 200, y = 35)
    global stop_timer
    stop_timer = customtkinter.CTkButton(master=app, text="Stop Timer", height=85, width=100, command=stop)
    stop_timer.place(x= 250, y = 90)

def exit_function():
    os.abort()


def stop():
    pin_out_get = int(pin_out.get())
    if pin == {pin_out_get}:
        t.cancel()
        pin_out_title.destroy()
        pin_out.destroy()
        stop_timer.destroy()
        new_window()



def theme_switcher():
    if switch_var.get() == 'on':
        customtkinter.set_appearance_mode("dark")
    elif switch_var.get() == 'off':
        customtkinter.set_appearance_mode("light")


icon_image = CTkImage(Image.open(f'{assets_path}/Settings.png'), size=(30, 30))
print(icon_image)
def settings_enter():
    global return_path
    global return_entry_time
    global return_pin_entry
    return_path = path.get()
    return_entry_time = entry_time.get()
    return_pin_entry = pin_entry.get()
    title.destroy()
    settings_button_enter.destroy()
    select_video_button.destroy()
    play_button.destroy()
    path.destroy()
    entry_time.destroy()
    pin_entry.destroy()
    path_title.destroy()
    entry_time_title.destroy()
    pin_entry_title.destroy()
    clear.destroy()
    global switch_var_fullscreen
    global switch_fullscreen
    global settings_button_exit
    global switch_var
    global switch
    global rename_window_entry
    global rename_window_title
    global rename_window_button
    global reset_button
    global screamer_versinon_title
    rename_window_entry = customtkinter.CTkEntry(app, width=200, height=35)
    rename_window_entry.place(x=150,y=60)
    if 'return_window_name' not in globals():
        pass
    else:
        rename_window_entry.insert(0, return_window_name)
    rename_window_title = customtkinter.CTkLabel(app, text='Enter new name for window')
    rename_window_title.place(x=170,y=30)
    rename_window_button = customtkinter.CTkButton(app, text='Rename', height=35, width=100, command=rename_window)
    rename_window_button.place(x=10,y=60)
    reset_button = customtkinter.CTkButton(app, text='Reset Name', height=35, width=100 , command=reset_window_name)
    reset_button.place(x=10,y=110)
    switch_var_fullscreen = customtkinter.StringVar(value="on")
    switch_fullscreen = customtkinter.CTkSwitch(app, text="Full Screen", variable=switch_var_fullscreen, onvalue="on", offvalue="off")
    switch_fullscreen.place(x=480,y=25)
    screamer_versinon_title = customtkinter.CTkLabel(app, text='Screamer V2.0')
    screamer_versinon_title.place(x=0,y=280)
    if 'switch_var_fs' not in globals():
        pass
    elif switch_var_fs == 'on':
        switch_fullscreen.select()
    elif switch_var_fs == 'off':
        switch_fullscreen.deselect()
    switch_var = customtkinter.StringVar(value="on")
    switch = customtkinter.CTkSwitch(app, text="Dark Mode", command=theme_switcher,variable=switch_var, onvalue="on", offvalue="off")
    switch.place(x=480,y=0)
    if 'switch_var_dark' not in globals():
        pass
    elif switch_var_dark == 'on':
        switch.select()
    elif switch_var_dark == 'off':
        switch.deselect()
    settings_button_exit = customtkinter.CTkButton(app, text = '', width=35, height=35, image=icon_image, fg_color = 'transparent', command=settings_exit)
    settings_button_exit.place(x=0, y=0)


def settings_exit():
    global switch_var_dark
    global switch_var_fs
    global return_window_name
    switch_var_fs = switch_var_fullscreen.get()
    switch_var_dark = switch_var.get()
    settings_button_exit.destroy()
    switch.destroy()
    switch_fullscreen.destroy()
    return_window_name = rename_window_entry.get()
    rename_window_entry.destroy()
    rename_window_title.destroy()
    rename_window_button.destroy()
    reset_button.destroy()
    screamer_versinon_title.destroy()
    new_window()
    path.insert(0, return_path)
    entry_time.insert(0, return_entry_time)
    pin_entry.insert(0, return_pin_entry)

def new_window():
    global title
    title = customtkinter.CTkLabel(app, text='Screamer')
    title.pack()
    global settings_button_enter
    settings_button_enter = customtkinter.CTkButton(app, text = '', width=35, height=35, image=icon_image, fg_color = 'transparent', command=settings_enter)
    settings_button_enter.place(x=0, y=0)
    global select_video_button
    select_video_button = customtkinter.CTkButton(master=app, text="Select File", height=35, width=100,command=select_video)
    select_video_button.place(x = 10, y=100)
    global play_button
    play_button = customtkinter.CTkButton(master=app, text="Start Timer", height=35, width=100, command=timer)
    play_button.place(x = 10, y=170)
    global path_title
    path_title = customtkinter.CTkLabel(app, text='Path to file')
    path_title.place(x = 320, y=70)
    global path
    path = customtkinter.CTkEntry(app, width=400, height=35)
    path.place(x = 150, y=100)
    global entry_time_title
    entry_time_title = customtkinter.CTkLabel(app, text='Enter the time after which the video will play. (In seconds)')
    entry_time_title.place(x = 190, y=140)
    global entry_time
    entry_time = customtkinter.CTkEntry(app, width=400, height=35)
    entry_time.place(x = 150, y=170)
    global pin_entry_title
    pin_entry_title = customtkinter.CTkLabel(app, text='Enter your password')
    pin_entry_title.place(x = 195, y=210)
    global pin_entry
    pin_entry = customtkinter.CTkEntry(app, width=200, height=35)
    pin_entry.place(x = 150, y=240)
    global clear
    clear = customtkinter.CTkButton(master=app, text="Clear", height=35, width=100,command=clear)
    clear.place(x = 10, y=240)


def rename_window():
    new_name = rename_window_entry.get()
    app.title(new_name)

def reset_window_name():
    rename_window_entry.delete(0, END)
    app.title('')



new_window()
app.mainloop()