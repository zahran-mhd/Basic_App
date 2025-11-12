# modules/settings.py
import tkinter as tk
from utils.theme_manager import ThemeManager

class SettingsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.theme_manager = ThemeManager()

        tk.Label(self, text="⚙️ Settings", font=("Arial", 18)).pack(pady=30)

        self.theme_var = tk.StringVar(value=self.theme_manager.current_theme)
        tk.Radiobutton(self, text="Light Mode", variable=self.theme_var, value="light").pack()
        tk.Radiobutton(self, text="Dark Mode", variable=self.theme_var, value="dark").pack()

        tk.Button(self, text="Apply Theme", command=self.apply_theme).pack(pady=20)
        tk.Button(self, text="Back", command=lambda: controller.show_page("DashboardPage")).pack()

    def apply_theme(self):
        self.theme_manager.set_theme(self.theme_var.get())
        tk.Label(self, text=f"Theme set to {self.theme_var.get()}", fg="green").pack()
