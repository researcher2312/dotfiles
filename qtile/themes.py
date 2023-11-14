class QtileTheme:
    def __init__(self):
        self.wallpaper_path = None
        self.rofi_theme_path = None
        self.font_name = None
        self.status_bar = None
        self.status_popup = None

    def apply_theme(qtile):
        qtile.screens.set_wallpaper(self.wallpaper_path)
    
    def set_wallpaper(self, wallpaper):
        self.wallpaper_path = wallpaper
