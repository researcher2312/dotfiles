import abc
from widgets import SystemConfigurationValues
import json

class QtileTheme:
    def __init__(self, qtile, sysConfig):
        self.qtile_handle = qtile
        self.wallpaper_path = None
        self.rofi_theme_path = None
        self.font_name = None
        self.status_bar = None
        self.status_popup = None
        self.light_colors = {}
        self.dark_colors = {}
        self.sysConfig = sysConfig

    def apply_theme(self):
        self.sysConfig.wallpaper = self.wallpaper_path
        self.sysConfig.volume_popup = self.status_popup
        self.sysConfig.system_bar = self.status_bar

    def set_wallpaper(self, wallpaper):
        self.wallpaper_path = wallpaper

    def load_colors(self, path):
        file = open(path)
        data = json.load(file)
        self.light_colors = data["light"]
        self.dark_colors = data["dark"]
