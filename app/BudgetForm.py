import tkinter as tk
from tkinter import ttk
from config import *
from tkcalendar import dateentry
class BudgetForm():
    def __init__(self, panel):
        self.header = tk.Frame(panel, bg=COLOR_CUERPO_PRINCIPAL, pady=10)
        self.header.pack(side=tk.TOP, fill='x', expand='false')

        self.center = tk.Frame(panel, bg=COLOR_CUERPO_PRINCIPAL)
        self.center.pack(side=tk.BOTTOM, fill='both', expand=True)

        self.labelTitle = tk.Label(
            self.header,
            text='Presupuestos', 
            fg=COLOR_NEGRO, 
            font=("Roboto", 20),
            bg=COLOR_CUERPO_PRINCIPAL)
        self.labelTitle.pack(side=tk.TOP, fill='both', expand=True)


        # Inputs y Labels
        self.TypeLabel = tk.Label(
            self.center,
            text='Tipo', 
            font=('Roboto', 12),
            foreground=COLOR_NEGRO,
            background=COLOR_CUERPO_PRINCIPAL
        )
        self.TypeLabel.place(x=30, y=15)

        self.TypeComboBox = ttk.Combobox(
            self.center,
            state='readonly',
            values=['Ingreso', 'Pago'],
            font=('Roboto', 12),
            foreground=COLOR_GRIS,
            width=20,
        )
        self.TypeComboBox.place(x=30, y=40)


        self.AmountLabel = tk.Label(
            self.center,
            text='Monto',
            background=COLOR_CUERPO_PRINCIPAL,
            foreground=COLOR_NEGRO,
            font=('Roboto', 12)
        )
        self.AmountLabel.place(x=300, y=15)

        self.AmountTextField = tk.Entry(
            self.center,
            background=COLOR_CUERPO_PRINCIPAL,
            font=('Roboto', 12),
            foreground=COLOR_GRIS,
            width=20,
        )
        self.AmountTextField.place(x=300, y=40)
        
        
        # self.DateInput = dateentry(
        #     self.center
        # )
        # self.DateInput.place(x=30, y=70)


