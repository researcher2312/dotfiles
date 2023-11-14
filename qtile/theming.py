import os
from themes import QtileTheme
from widgets import ArrowBar, VolumePopup

class BlueyTheme(QtileTheme):
    def __init__(self, qtile, sysConfig):
        super().__init__(qtile, sysConfig)
        self.status_bar = ArrowBar()
        self.status_popup = VolumePopup(qtile)
        self.wallpaper_path = os.path.expanduser("~/.config/wallpapers/arch_nz.png")
