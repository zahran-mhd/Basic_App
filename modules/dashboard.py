# modules/dashboard.py
import tkinter as tk

class DashboardPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="🏠 Dashboard", font=("Arial", 18)).pack(pady=30)
        tk.Button(self, text="Go to Plot Viewer",
                  command=lambda: controller.show_page("PlotViewerPage")).pack(pady=10)