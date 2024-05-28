from libqtile.config import Screen
from libqtile.log_utils import logger
import subprocess
import json
import re

class Monitor:
    def __init__(self, name, x, y, resolution_x, resolution_y, shift_x, shift_y, primary):
        self.name = name
        self.x = x
        self.y = y
        self.resolution_x = resolution_x
        self.resolution_y = resolution_y
        self.shift_x = shift_x
        self.shift_y = shift_y
        self.primary = primary


class MonitorManager:
    def __init__(self):
        self.monitors = []
        self.parse_monitors()
        self.monitors_count = len(self.monitors)
        self.screens = []

    def parse_monitors(self):
        monitors = []
        output = subprocess.getoutput("xrandr --listmonitors").split('\n')
        monitor_parameters = [re.split("\\+|x|/| ", i) for i in output[1:]]
        for parameters in monitor_parameters:
            (_, _, _, primary, res_x, x, res_y, y, shift_x, shift_y, _, name) = parameters
            primary = '*' in primary
            monitors.append(Monitor(name, x, y, res_x, res_y, shift_x, shift_y, primary))
        self.monitors = monitors

    def save_monitors(self):
        with open("~/monitors.json", "w+t") as file:
            json.dump(file, self.monitors, default=vars)



    def init_screens(self, theme):
        for _ in range(self.monitors_count):
            new_screen = Screen(
                top=theme.get_bar(),
                wallpaper=theme.wallpaper_path,
                wallpaper_mode="fill",
            )
            self.screens.append(new_screen)
        return self.screens
