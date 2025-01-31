import tkinter as tk
from config import *
from tkinter import font
import utils.util_imagenes as util_img

class TransactionForm():
    def __init__(self, panel):
        font_awesome = font.Font(family='FontAwesome', size=10, weight='bold')

        self.header = tk.Frame(panel, bg=COLOR_CUERPO_PRINCIPAL, pady=10)
        self.header.pack(side=tk.TOP, fill='x', expand=False)

        self.center = tk.Frame(panel, bg=COLOR_CUERPO_PRINCIPAL)
        self.center.pack(side=tk.BOTTOM, fill='both', expand=True)

        self.ButtonsFrame = tk.Frame(self.center, bg=COLOR_NEGRO, height=100)
        self.ButtonsFrame.pack(side=tk.TOP, fill='x', expand=False) 
        
        self.InputsFrame = tk.Frame(self.center, bg=COLOR_BARRA_SUPERIOR)
        self.InputsFrame.pack(side=tk.TOP, fill='both', expand=True) 
        

        self.labelTitle = tk.Label(
            self.header,
            text='Transacciones', 
            fg=COLOR_NEGRO, 
            font=("Roboto", 20,),
            bg=COLOR_CUERPO_PRINCIPAL)
        self.labelTitle.pack(side=tk.TOP, fill='both', expand=True)


        # Botones
        self.add_img = util_img.readImage("./img/add.png", (25, 25))
        self.AddBtn = tk.Button(
            self.ButtonsFrame,
            image=self.add_img,
            text='Agregar',
            font=font_awesome, 
            compound='left',
            relief='flat',
            padx=10,
            pady=5,
            bg=COLOR_BARRA_SUPERIOR,
            fg=COLOR_BLANCO
        )

        self.AddBtn.bind("<Enter>", lambda e: self.AddBtn.config(bg=COLOR_MENU_CURSOR_ENCIMA))
        self.AddBtn.bind("<Leave>", lambda e: self.AddBtn.config(bg=COLOR_BARRA_SUPERIOR))

        self.AddBtn.pack(side=tk.LEFT, fill='x')
        self.add_img.image = self.add_img


        

