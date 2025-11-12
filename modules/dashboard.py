# modules/dashboard.py
import tkinter as tk

class DashboardPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="🏠 Dashboard", font=("Arial", 18)).pack(pady=30)
