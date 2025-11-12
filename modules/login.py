# modules/login.py
import tkinter as tk

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="🔐 Login Page", font=("Arial", 18)).pack(pady=30)

        tk.Label(self, text="Username").pack()
        self.username = tk.Entry(self)
        self.username.pack(pady=5)

        tk.Label(self, text="Password").pack()
        self.password = tk.Entry(self, show="*")
        self.password.pack(pady=5)

        tk.Button(self, text="Login", command=self.login_action).pack(pady=20)

    def login_action(self):
        # Simple placeholder logic
        if self.username.get() == "admin" and self.password.get() == "123":
            self.controller.show_page("DashboardPage")
        else:
            tk.Label(self, text="Invalid credentials!", fg="red").pack()
