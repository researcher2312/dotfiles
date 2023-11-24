import os
from themes import QtileTheme
from widgets import ArrowBar, VolumePopup, SlashBar
from colortools import ColorGradient


class BlueyTheme(QtileTheme):
    def __init__(self):
        theme_path = os.path.expanduser("~/.config/palex/arch_nz-color_palette.json")
        wallpaper_path = os.path.expanduser("~/.config/wallpapers/arch_nz.png")
        super().__init__(
            name="Bluey",
            theme=theme_path,
            font="FiraCode Nerd Font",
            wallpaper=wallpaper_path,
            group_names="123456ABC",
            group_labels=[
                "\uf489",  # terminal
                "\uf269",  # browser
                "\U000f0ede",  # chat
                "\ueaf0",  # files
                "\ueb1c",  # mail
                "\ueae9",  # code
                "\U000f0beb",  # A letter
                "\U000f0bee",  # B letter
                "\U000f0bf1",  # C letter
            ],
        )
        gradient = ColorGradient(
            ["02367b", "006ca5", "0096c7", "04bade", "55e2e9"], 10, "80"
        )
        self.bar = ArrowBar(gradient, self.dark_colors)

class EVA(QtileTheme):
    def __init__(self):
        theme_path = os.path.expanduser("~/.config/palex/nerv_wal-color_palette.json")
        wallpaper_path = os.path.expanduser("~/.config/wallpapers/nerv_wal.jpg")
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
