# utils/theme_manager.py

class ThemeManager:
    def __init__(self):
        self.current_theme = "light"

    def set_theme(self, theme):
        self.current_theme = theme
        print(f"Theme updated to: {theme}")
