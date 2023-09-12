#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")

        self.current_file = None
        self.paused = False

        pygame.mixer.init()

        self.create_widgets()

    def create_widgets(self):
        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_music)
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.open_button = tk.Button(self.root, text="Open", command=self.open_file)

        self.play_button.pack(pady=10)
        self.pause_button.pack(pady=10)
        self.stop_button.pack(pady=10)
        self.open_button.pack(pady=10)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("C:\music", "*.mp3")])

        if file_path:
            self.current_file = file_path

    def play_music(self):
        if self.current_file:
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load(self.current_file)
                pygame.mixer.music.play()
            elif self.paused:
                pygame.mixer.music.unpause()
                self.paused = False

    def pause_music(self):
        if pygame.mixer.music.get_busy() and not self.paused:
            pygame.mixer.music.pause()
            self.paused = True

    def stop_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()


# In[ ]:





# In[ ]:




