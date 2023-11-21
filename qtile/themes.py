import abc, json, yaml
import json


class QtileTheme:
    def __init__(
        self,
        name,
        theme,
        font,
        wallpaper,
        group_names=None,
        group_labels=None,
        rofi=None,
    ):
        self.name = name
        self.font_name = font
        self.wallpaper_path = wallpaper
        self.rofi_theme_path = rofi
        self.light_colors = {}
        self.dark_colors = {}
        self.load_colors(theme)
        self.status_bar = None
        self.status_popup = None
        if group_names == None:
            self.group_names = "123456789"
        else:
            self.group_names = group_names
        if group_labels == None:
            self.group_labels = "123456789"
        else:
            self.group_labels = group_labels

    def apply_theme(self, qtile):
        defaults = dict(font="FiraCode Nerd Font", fontsize=12, padding=3, foreground=self.dark_colors["white"])
        qtile.config.widget_defaults = defaults
        qtile.config.extension_defaults = defaults.copy()

    def set_wallpaper(self, wallpaper):
        self.wallpaper_path = wallpaper

    def load_colors(self, path):
        file = open(path)
        data = json.load(file)
        self.light_colors = data["light"]
        self.dark_colors = data["dark"]
