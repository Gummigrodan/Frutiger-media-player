from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import song as sg
import os

list_off_songs = []

def load_songs():
    global list_off_songs
    base_path = "Songs"

    for folder in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder)

        if os.path.isdir(folder_path):
            list_off_songs.append(sg.Song(folder))
    
    return list_off_songs

load_songs()

active_song = list_off_songs[0]

image_label = None
label = None
image_ref = None

def load_resized_image(path):
    img = Image.open(path)
    img = img.resize((200, 200), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)

def play():
    active_song.play_song()

def stop():
    active_song.stop_song()

def uppdatera_active_song():
    global active_song, image_ref, image_label

    active_song = list_off_songs[0]

    image_ref = load_resized_image(active_song.album_cover)
    image_label.config(image=image_ref)
    image_label.image = image_ref

    label.config(text=active_song.name)

def höger():
    global list_off_songs, active_song, image_label

    active_song.stop_song()
    list_off_songs = [list_off_songs[-1]] + list_off_songs[:-1]
    uppdatera_active_song()

def vänster():
    global list_off_songs, active_song, image_label

    active_song.stop_song()
    list_off_songs = list_off_songs[1:] + [list_off_songs[0]]
    uppdatera_active_song()

root = tk.Tk()
root.title("Frutiger Mediaplayer")
root.geometry("500x500+100+100")
root.resizable(False, False)
root.config(background="black")

def create_gui():
    global image_label, label, image_ref, active_song

    
    image_ref = load_resized_image(active_song.album_cover)

    image_label = tk.Label(root, image=image_ref, bg="black")
    image_label.pack(pady=50)


    play_button = tk.Button(root, width=10, height=5, text="Play", command=play)
    play_button.pack(side="left", padx=50, pady=20)

    stop_button = tk.Button(root, width=10, height=5, text="Stop", command=stop)
    stop_button.pack(side="right", padx=50, pady=20)


    left_button = tk.Button(root, width=2, height=2, text="<", command=vänster)
    left_button.pack(side="left")
    
    right_button = tk.Button(root, width=2, height=2, text=">", command=höger)
    right_button.pack(side="right")


    label = tk.Label(root, text=active_song.name, bg=None, fg="white", background="black", font=("Arial", 8))
    label.pack(side="bottom", pady=90)

create_gui()
root.mainloop()