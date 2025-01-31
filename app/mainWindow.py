import tkinter as tk
from tkinter import font
from config import *;
import utils.util_imagenes as util_img
import utils.util_window as util_window
from app.TransactionForm import TransactionForm
from app.BudgetForm import BudgetForm
from app.Funds import Funds

class mainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.windowConfig()
        self.frames()
        self.buttons()

    def windowConfig(self):
        self.title("Finance Manager")
        util_window.centerWindow(self)

    def frames(self):
        self.header = tk.Frame(bg=COLOR_BARRA_SUPERIOR, height=50)
        self.header.pack(side=tk.TOP, fill='both')
        
        self.aside = tk.Frame(bg=COLOR_MENU_LATERAL, width=150)
        self.aside.pack(side=tk.LEFT, fill='both', expand=False)

        self.center = tk.Frame(bg=COLOR_CUERPO_PRINCIPAL)
        self.center.pack(side=tk.RIGHT, fill='both', expand=True)

    def buttons(self):
        font_awesome = font.Font(family='FontAwesome', size=10, weight='bold')
        width = 20
        height = 2

        # Transacciones
        self.transaction_img = util_img.readImage("./img/transactions.png", (40, 40))
        self.Transaction = tk.Button(
            self.aside, 
            image=self.transaction_img,
            bg=COLOR_MENU_LATERAL, 
            text="Transacciones", 
            font=font_awesome, 
            compound='left',
            relief='flat',
            padx=10,
            pady=5,
            fg=COLOR_BLANCO,
            command=self.openTransactionsForm)
        self.Transaction.bind("<Enter>", lambda e: self.Transaction.config(bg=COLOR_MENU_CURSOR_ENCIMA))
        self.Transaction.bind("<Leave>", lambda e: self.Transaction.config(bg=COLOR_MENU_LATERAL))

        self.Transaction.pack(side=tk.TOP, fill="x")        
        self.Transaction.image = self.transaction_img

        # Presupuestos
        self.BudgetImg = util_img.readImage("./img/budget.png", (40, 40))
        self.Budget = tk.Button(
            self.aside, 
            image=self.BudgetImg,
            bg=COLOR_MENU_LATERAL, 
            text="Presupuestos", 
            font=font_awesome, 
            compound='left',
            relief='flat',
            padx=10,
            pady=5,
            fg=COLOR_BLANCO,
            command=self.openBudgetForm)
        self.Budget.bind("<Enter>", lambda e: self.Budget.config(bg=COLOR_MENU_CURSOR_ENCIMA))
        self.Budget.bind("<Leave>", lambda e: self.Budget.config(bg=COLOR_MENU_LATERAL))

        self.Budget.pack(side=tk.TOP, fill="x")        
        self.Budget.image = self.BudgetImg

        # Fondos
        self.FundsImg = util_img.readImage("./img/funds.png", (40, 40))
        self.Funds = tk.Button(
            self.aside, 
            image=self.FundsImg,
            bg=COLOR_MENU_LATERAL, 
            text="Fondos", 
            font=font_awesome, 
            compound='left',
            relief='flat',
            padx=10,
            pady=5,
            fg=COLOR_BLANCO,    
            command=self.openFunds)
        self.Funds.bind("<Enter>", lambda e: self.Funds.config(bg=COLOR_MENU_CURSOR_ENCIMA))
        self.Funds.bind("<Leave>", lambda e: self.Funds.config(bg=COLOR_MENU_LATERAL))

        self.Funds.pack(side=tk.TOP, fill="x")        
        self.Funds.image = self.FundsImg

    def openTransactionsForm(self):
        self.clearPanel(self.center)
        TransactionForm(self.center)

    def openBudgetForm(self):
        self.clearPanel(self.center)
        BudgetForm(self.center)

    def openFunds(self):
        self.clearPanel(self.center)
        Funds(self.center)

    def clearPanel(self, panel):
        for widget in panel.winfo_children():
            widget.destroy()

        