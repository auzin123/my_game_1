import tkinter as tk
from PIL import Image, ImageTk
import random
from pathlib import Path



class Game:
    def __init__(self) -> None:
        self.player_name = 'Вася'
        self.player_hp = 100
        self.player_level = 0
        self.player_xp = 0
        self.player_defence = 1
        self.player_attack = 10
        self.player_weapon = 'Копьё'
        self.img_dir = Path(__file__).parent / 'img'
        self.window = tk.Tk()
        self.window.attributes('-fullscreen', True)
        self.window.bind('<Escape>', lambda _: self.window.destroy())
        self.font_size = min(
            self.window.winfo_screenwidth(),
            self.window.winfo_screenheight()
        ) // 50
        self.window.option_add('*Font', ('Impact', self.font_size))

        self.image_size = self.window.winfo_screenwidth() // 3

        self.player_frame = tk.Frame(self.window)
        self.player_frame.pack(side='left')
        self.clear()
        self.window.mainloop()

    def attack(self) -> None:
        self.player_hp -= 10
        self.clear()

    def clear(self):
        for widget in self.player_frame.winfo_children():
            widget.destroy()
        tk.Label(self.player_frame, text=self.player_name).pack()
        tk.Label(self.player_frame, text=f'жизни: {self.player_hp}').pack()
        tk.Label(self.player_frame, text=f'уровень: {self.player_level}').pack()
        tk.Label(self.player_frame, text=f'опыт: {self.player_xp}').pack()
        tk.Label(self.player_frame, text=f'атака: {self.player_attack}').pack()
        tk.Label(self.player_frame, text=f'защита: {self.player_defence}').pack()
        tk.Label(self.player_frame, text=f'оружие: {self.player_weapon}').pack()
        self.combat_frame = tk.Frame(self.window)
        self.combat_frame.pack(side='left')
        tk.Button(self.combat_frame, text='атака', command=self.attack).pack()
        self.enemy_frame = tk.Frame(self.window)
        self.enemy_frame.pack(side='left')


Game()
