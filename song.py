import pygame.mixer
sounds = pygame.mixer
sounds.init()

class Song:
    def __init__(self, name):
        self.name = name
        self.file = f"Songs/{self.name}/song.wav"
        self.album_cover = f"Songs/{self.name}/cover.png"
    
        self.song_to_play = sounds.Sound(f"{self.file}")
    
    def play_song(self):
        self.song_to_play.play()
    
    def stop_song(self):
        self.song_to_play.stop()