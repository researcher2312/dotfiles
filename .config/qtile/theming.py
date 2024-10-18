import os
from themes import QtileTheme
from widgets import ArrowBar, VolumePopup, SlashBar
from colortools import ColorGradient
from nerdfonts import Nerdfonts as nfs


class BlueyTheme(QtileTheme):
    def __init__(self):
        theme_path = os.path.expanduser("~/.config/qtile/arch.json")
        wallpaper_path = os.path.expanduser("~/wallpapers/arch_nz.png")
        super().__init__(
            name="Bluey",
            theme=theme_path,
            font="FiraCode Nerd Font",
            wallpaper=wallpaper_path,
            group_names="123456ABC",
            group_labels=[
                nfs["terminal"],
                nfs["browser"],
                nfs["chat"],
                nfs["files"],
                nfs["mail"],
                nfs["code"],
                nfs["A_letter"],
                nfs["B_letter"],
                nfs["C_letter"],
            ],
        )
        gradient = ColorGradient(
            ["02367b", "006ca5", "0096c7", "04bade", "55e2e9"], 10, "80"
        )
        self.bar = ArrowBar(gradient, self.dark_colors)

class EVA(QtileTheme):
    def __init__(self):
        theme_path = os.path.expanduser("~/.config/qtile/nerv.json")
        wallpaper_path = os.path.expanduser("~wallpapers/nerv.png")
        super().__init__(
            name="EVA",
            font="FiraCode Nerd Font",
            group_names="123456789",
            group_labels="一二三四五六七八九",
            theme=theme_path,
            wallpaper=wallpaper_path
        )
        gradient = ColorGradient(
            ["3f6d4e", "8bd450", "1d1a2f", "965fd4", "734f9a"], 5
        )
        self.bar = SlashBar(gradient, self.dark_colors)
