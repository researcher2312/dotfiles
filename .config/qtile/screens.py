from libqtile.config import Screen
from libqtile.log_utils import logger
from platform import uname
import subprocess
import json
import re


class Monitor:
    def __init__(
        self, name, x, y, resolution_x, resolution_y, shift_x, shift_y, primary
    ):
        self.name = name
        self.x = x
        self.y = y
        self.resolution_x = resolution_x
        self.resolution_y = resolution_y
        self.shift_x = shift_x
        self.shift_y = shift_y
        self.primary = primary

    def __eq__(self, other):
        return (
            self.name == other.name
            and self.resulution_x == other.resolution_x
            and self.resolution_y == other.resolution_y
        )

    def __str__(self):
        return (
            f"{self.name} screen, {self.resolution_x}x{self.resolution_y} "
            f"on [{self.shift_x}, {self.shift_y}], primary: {self.primary}"
        )


class MonitorSetup:
    def __init__(self, name):
        self.monitors = []
        self.name = name

    def parse_current_monitors(self):
        monitors = []
        output = subprocess.getoutput("xrandr --listmonitors").split("\n")
        monitor_parameters = [re.split("\\+|x|/| ", i) for i in output[1:]]
        for parameters in monitor_parameters:
            (_, _, _, primary, res_x, x, res_y, y, shift_x, shift_y, _, name) = (
                parameters
            )
            primary = "*" in primary
            monitors.append(
                Monitor(name, x, y, res_x, res_y, shift_x, shift_y, primary)
            )
        self.monitors = monitors

    def has_same_monitors(self, other):
        if len(self.monitors) != len(other.monitors):
            return False
        for monitor in self.monitors:
            if monitor not in other.monitors:
                return False
        return True

    def __str__(self):
        result = f"{self.name}:\n"
        for monitor in self.monitors:
            result += str(monitor) + '\n'
        return result


class MonitorManager:
    def __init__(self):
        self.all_monitor_setups = []
        self.current_monitor_setup = MonitorSetup(uname()[1])
        self.current_monitor_setup.parse_current_monitors()
        if not self.load_saved_setup():
            self.all_monitor_setups.append(self.current_monitor_setup)
            

    def load_saved_setup(self):
        for setup in self.all_monitor_setups:
            if self.current_monitor_setup.has_same_monitors(setup):
                self.current_monitor_setup = setup
                return True
        return False
                
    def save_setups(self):
        with open("monitors.json", "w+t") as file:
            json.dump(self.all_monitor_setups, file, default=vars)

    def load_setups(self):
        with open("monitors.json", "wt") as file:
            json.load(self.all_monitor_setups, file, default=vars)

    def init_screens(self, theme):
        for _ in range(self.monitors_count):
            new_screen = Screen(
                top=theme.get_bar(),
                wallpaper=theme.wallpaper_path,
                wallpaper_mode="fill",
            )
            self.screens.append(new_screen)
        return self.screens
