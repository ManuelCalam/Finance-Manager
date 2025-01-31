import tkinter as tk
from config import *

class Funds():
    def __init__(self, panel):
        self.header = tk.Frame(panel, bg=COLOR_CUERPO_PRINCIPAL, pady=10)
        self.header.pack(side=tk.TOP, fill='x', expand='false')

        self.center = tk.Frame(panel, bg=COLOR_CUERPO_PRINCIPAL)
        self.center.pack(side=tk.BOTTOM, fill='both', expand=True)

        self.labelTitle = tk.Label(
            self.header,
            text='Fondos', 
            fg=COLOR_NEGRO, 
            font=("Roboto", 20,),
            bg=COLOR_CUERPO_PRINCIPAL)
        self.labelTitle.pack(side=tk.TOP, fill='both', expand=True)

