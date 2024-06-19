import tkinter as tk
from PIL import Image, ImageTk
import random
from pathlib import Path
from classes import Player, Weapon


class Game:
    def __init__(self) -> None:
        ''' Игрок '''
        self.motion_attack = 'player'
        self.player_image = 'vasua.png'
        self.player_name = 'Вася'
        self.player_hp = 10
        self.player_level = 0
        self.player_xp = 0
        self.player_defence = 1
        self.player_attack = 2
        self.player_weapon = 'базовое оружие'
        ''' Противник '''
        self.enemy_name = 'Ася'
        self.enemy_hp = 10
        self.enemy_level = 0
        self.enemy_xp = 0
        self.enemy_defence = 1
        self.enemy_attack = 2
        self.enemy_weapon = 'базовое оружие'
        ''' Другое '''
        self.img_dir = Path(__file__).parent / 'image'
        self.window = tk.Tk()
        self.window.attributes('-fullscreen', True)
        self.window.bind('<Escape>', lambda _: self.window.destroy())
        self.font_size = min(
            self.window.winfo_screenwidth(),
            self.window.winfo_screenheight()
        ) // 50
        self.window.option_add('*Font', ('Impact', self.font_size))
        self.image_size = self.window.winfo_screenwidth() // 3
        self.player = Player('Вася', 'vasua.png', 1, 100, 0)
        self.enemy = Player('Ася', 'vasua.png', 1, 100, 0)
        self.img_dict = dict()
        self.player_frame = tk.Frame(self.window)
        self.player_frame.pack(side='left')

        self.combat_frame = tk.Frame(self.window)
        self.combat_frame.pack(side='left', expand=True, fill='both', padx='25', pady='20')
        self.combat_masseges = tk.Listbox(self.combat_frame)
        self.combat_masseges.pack(expand=True, fill='both')
        tk.Button(self.combat_frame, text='атака', command=self.attack).pack(expand=True)
        self.enemy_frame = tk.Frame(self.window)
        self.enemy_frame.pack(side='left')
        self.clear_widgets_player()
        self.clear_widgets_enemy()
        self.window.mainloop()


    def attack(self) -> None:
        if self.motion_attack == 'player':
            if self.enemy_hp > 0:
                self.player_hp -= self.enemy_attack
                text = f'{self.enemy_name} атаковал {self.player_name} на {self.enemy_attack}'
                self.combat_masseges.insert(tk.END, text)
                self.motion_attack = 'enemy'
                self.attack()
            else:
                self.combat_masseges.insert(tk.END, f'Победил: {self.enemy_name}')

        elif self.motion_attack == 'enemy':
            if self.player_hp > 0:
                self.enemy_hp -= self.player_attack
                text = f'{self.player_name} атаковал {self.enemy_name} на {self.player_attack}'
                self.combat_masseges.insert(tk.END, text)
                self.motion_attack = 'player'
            else:
                self.combat_masseges.insert(tk.END, f'Победил: {self.player_name}')


        self.clear_widgets_player()
        self.clear_widgets_enemy()

    def clear_widgets_player(self):
        for widget in self.player_frame.winfo_children():
            widget.destroy() 
        image = Image.open(self.img_dir / 'vasua.png')
        image = image.resize((self.image_size, self.image_size))
        self.img_dict[self.player_name] = ImageTk.PhotoImage(image=image)
        tk.Label(self.player_frame, text=self.player_name).pack()
        tk.Label(self.player_frame, text=f'жизни: {self.player_hp}').pack()
        tk.Label(self.player_frame, text=f'уровень: {self.player_level}').pack()
        tk.Label(self.player_frame, text=f'опыт: {self.player_xp}').pack()
        tk.Label(self.player_frame, text=f'атака: {self.player_attack}').pack()
        tk.Label(self.player_frame, text=f'защита: {self.player_defence}').pack()
        tk.Label(self.player_frame, text=f'оружие: {self.player_weapon}').pack()

    def clear_widgets_enemy(self):
        for widget in self.enemy_frame.winfo_children():
            widget.destroy()
        image = Image.open(self.img_dir / 'vasua.png')
        image = image.resize((self.image_size, self.image_size))
        self.img_dict[self.player_name] = ImageTk.PhotoImage(image=image)
        tk.Label(self.enemy_frame, text=self.enemy_name).pack()
        tk.Label(self.enemy_frame, text=f'жизни: {self.enemy_hp}').pack()
        tk.Label(self.enemy_frame, text=f'уровень: {self.enemy_level}').pack()
        tk.Label(self.enemy_frame, text=f'опыт: {self.enemy_xp}').pack()
        tk.Label(self.enemy_frame, text=f'атака: {self.enemy_attack}').pack()
        tk.Label(self.enemy_frame, text=f'защита: {self.enemy_defence}').pack()
        tk.Label(self.enemy_frame, text=f'оружие: {self.enemy_weapon}').pack()
    
Game()
