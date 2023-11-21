import os
from themes import QtileTheme
from widgets import ArrowBar, VolumePopup
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
                "A",
                "B",
                "C",
            ],
        )
        gradient = ColorGradient(
            ["02367b", "006ca5", "0096c7", "04bade", "55e2e9"], 10, "80"
        )
        self.bar = ArrowBar(gradient, self.light_colors)
