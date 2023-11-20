import os
from themes import QtileTheme
from widgets import ArrowBar, VolumePopup
from colortools import ColorGradient


class BlueyTheme(QtileTheme):
    def __init__(self):
        super().__init__()
        gradient = ColorGradient(
            ["03045e", "0077b6", "00b4d8", "90e0ef", "caf0f8"], 9, "80"
        )
        self.bar = ArrowBar(gradient)
        self.wallpaper_path = os.path.expanduser("~/.config/wallpapers/arch_nz.png")
        self.name = "Bluey"
