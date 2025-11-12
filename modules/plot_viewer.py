# modules/plot_viewer.py
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class PlotViewerPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="📈 Plot Viewer", font=("Arial", 18)).pack(pady=20)

        self.figure = Figure(figsize=(5, 3), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.ax.plot([1, 2, 3, 4], [2, 4, 1, 3], label="Sample Data")
        self.ax.legend()

        canvas = FigureCanvasTkAgg(self.figure, master=self)
        canvas.get_tk_widget().pack(fill="both", expand=True)

        tk.Button(self, text="Back to Dashboard",
                  command=lambda: controller.show_page("DashboardPage")).pack(pady=10)
