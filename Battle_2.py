import tkinter as tk
import random
from PIL import Image, ImageTk
from pathlib import Path


class Game:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.option_add('*Font', ('Arial', 14))
        self.window.attributes('-fullscreen', True)
        self.window.bind('<Escape>', lambda _: self.window.destroy())
        self.img_dir = Path(__file__).parent / 'image'
        self.player = PLayer()
        self.create_hero_screen()
        self.window.mainloop()

    def create_hero_screen(self) -> None:
        '''Вся инфа про игрока'''
        frame = tk.Frame(self.window)
        frame.pack(anchor='nw')
        frame['bg'] = 'CadetBlue1'
        image = Image.open(self.img_dir / 'vasua.png')
        image_width = self.window.winfo_screenwidth() // 3
        aspect_ratio = image.height / image.width
        image_height = int(image_width * aspect_ratio)
        image = image.resize((image_width, image_height), Image.LANCZOS)
        self.image_tk = ImageTk.PhotoImage(image)
        tk.Label(frame, image=self.image_tk).pack()
        tk.Label(frame, text=self.player.player_name).pack()
        tk.Label(frame, text=self.player.player_hp).pack()
        tk.Label(frame, text=self.player.player_lvl).pack()


class PLayer:
    def __init__(self) -> None:
        self.player_name = 'имя:', 'Вася'
        self.player_hp = 'жизни:', 100
        self.player_lvl = 'уровень:', 0


Game()
