import abc, json, yaml
import json, copy


def to_string(number):
    return f"#{number}"


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
        self.bar_copies = 0
        self.status_popup = None
        if group_names == None:
            self.group_names = "123456789"
        else:
            self.group_names = group_names
        if group_labels == None:
            self.group_labels = "123456789"
        else:
            self.group_labels = group_labels

    def get_bar(self):
        if self.bar_copies > 0:
            return copy.deepcopy(self.bar)
        else:
            self.bar_copies = 1
            return self.bar

    def apply_theme(self, qtile):
        defaults = dict(font="FiraCode Nerd Font", fontsize=12, padding=3, foreground=self.dark_colors["white"])
        qtile.config.widget_defaults = defaults
        qtile.config.extension_defaults = defaults.copy()
        self.generate_alacritty_theme()

    def set_wallpaper(self, wallpaper):
        self.wallpaper_path = wallpaper

    def load_colors(self, path):
        file = open(path)
        data = json.load(file)
        self.light_colors = data["light"]
        self.dark_colors = data["dark"]

    def generate_alacritty_theme(self):
        primary = {}
        normal = {}
        bright = {}
        for key, value in self.dark_colors.items():
            if key.find(' ') == -1:
                bright[key] = to_string(value)
            elif key.find("ground") != -1:
                primary[key] = to_string(value)
        
        for key, value in self.light_colors.items():
            if key.find(' ') == -1 and key.find("ground") == -1:
                normal[key] = to_string(value)
        colors = {"colors": {"primary": primary, "normal": normal, "bright": bright}}
        filename = "/home/researcher/.config/alacritty/" + self.name + ".yml"
        with open(filename, "w") as file:
            yaml.dump(colors, file)

    def apply_alacritty_theme(self):
        with open("../alacritty/alacritty.yml", "rw") as file:
            config = yaml.safe_load(file)
