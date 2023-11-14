import abc
from widgets import SystemConfigurationValues

class QtileTheme:
    def __init__(self, qtile, sysConfig):
        self.qtile_handle = qtile
        self.wallpaper_path = None
        self.rofi_theme_path = None
        self.font_name = None
        self.status_bar = None
        self.status_popup = None
        self.colors = []
        self.sysConfig = sysConfig

    def apply_theme(self):
        #self.qtile_handle.screens[0].set_wallpaper(self.wallpaper_path)
        self.sysConfig.volume_popup = self.status_popup
        self.sysConfig.system_bar = self.status_bar

    def set_wallpaper(self, wallpaper):
        self.wallpaper_path = wallpaper
