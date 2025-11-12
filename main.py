# main.py
import tkinter as tk
from modules.login import LoginPage
from modules.dashboard import DashboardPage
from modules.plot_viewer import PlotViewerPage
from modules.settings import SettingsPage

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Agile Tkinter Application")
        self.geometry("1000x600")
        self.resizable(True, True)

        # ===== Main Container =====
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.pages = {}
        self.create_pages()
        self.show_page("LoginPage")

    def create_pages(self):
        """Register all modules here"""
        for PageClass in (LoginPage, DashboardPage, PlotViewerPage, SettingsPage):
            page = PageClass(self.container, self)
            self.pages[PageClass.__name__] = page
            page.grid(row=0, column=0, sticky="nsew")

    def show_page(self, page_name):
        """Switch between module pages"""
        frame = self.pages[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
