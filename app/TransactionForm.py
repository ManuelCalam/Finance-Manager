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

        self.ButtonsFrame = tk.Frame(self.center, bg=COLOR_CUERPO_PRINCIPAL, height=100)
        self.ButtonsFrame.pack(side=tk.TOP, fill='x', expand=False) 
        
        self.InputsFrame = tk.Frame(self.center, bg=COLOR_CUERPO_PRINCIPAL)
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
            foreground=COLOR_BLANCO,
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


        # Eliminar
        self.delete_img = util_img.readImage("./img/delete.png", (25, 25))
        self.DeleteBtn = tk.Button(
            self.ButtonsFrame,
            image=self.delete_img,
            text='Eliminar',
            font=font_awesome, 
            compound='left',
            relief='flat',
            padx=10,
            pady=5,
            bg=COLOR_BARRA_SUPERIOR,
            fg=COLOR_BLANCO
        )

        self.DeleteBtn.bind("<Enter>", lambda e: self.DeleteBtn.config(bg=COLOR_MENU_CURSOR_ENCIMA))
        self.DeleteBtn.bind("<Leave>", lambda e: self.DeleteBtn.config(bg=COLOR_BARRA_SUPERIOR))

        self.DeleteBtn.pack(side=tk.LEFT, fill='x')
        self.delete_img.image = self.delete_img


        # Editar
        self.edit_img = util_img.readImage("./img/edit.png", (25, 25))
        self.EditBtn = tk.Button(
            self.ButtonsFrame,
            image=self.edit_img,
            text='Editar',
            font=font_awesome, 
            compound='left',
            relief='flat',
            padx=10,
            pady=5,
            bg=COLOR_BARRA_SUPERIOR,
            fg=COLOR_BLANCO
        )

        self.EditBtn.bind("<Enter>", lambda e: self.EditBtn.config(bg=COLOR_MENU_CURSOR_ENCIMA))
        self.EditBtn.bind("<Leave>", lambda e: self.EditBtn.config(bg=COLOR_BARRA_SUPERIOR))

        self.EditBtn.pack(side=tk.LEFT, fill='x')
        self.edit_img.image = self.edit_img


        

                          



        

