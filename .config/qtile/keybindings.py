import os
from libqtile.config import Click, Drag, Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal


class CustomKeys:
    def __init__(self):
        self.mod = "mod4"
        mod = self.mod
        terminal = 'wezterm'
        wifi_path = os.path.expanduser("~/.config/rofi/rofi-wifi-menu.sh")
        self.keys = [
            # A list of available commands that can be bound to keys can be found
            # at https://docs.qtile.org/en/latest/manual/config/lazy.html
            # Switch between windows
            Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
            Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
            Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
            Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
            Key(
                [mod],
                "space",
                lazy.layout.next(),
                desc="Move window focus to other window",
            ),
            # Move windows between left/right columns or move up/down in current stack.
            # Moving out of range in Columns layout will create new column.
            Key(
                [mod, "shift"],
                "h",
                lazy.layout.shuffle_left(),
                desc="Move window to the left",
            ),
            Key(
                [mod, "shift"],
                "l",
                lazy.layout.shuffle_right(),
                desc="Move window to the right",
            ),
            Key(
                [mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"
            ),
            Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
            # Grow windows. If current window is on the edge of screen and direction
            # will be to screen edge - window would shrink.
            Key(
                [mod, "control"],
                "h",
                lazy.layout.grow_left(),
                desc="Grow window to the left",
            ),
            Key(
                [mod, "control"],
                "l",
                lazy.layout.grow_right(),
                desc="Grow window to the right",
            ),
            Key(
                [mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"
            ),
            Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
            Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
            # Toggle between split and unsplit sides of stack.
            # Split = all windows displayed
            # Unsplit = 1 window displayed, like Max layout, but still with
            # multiple stack panes
            Key(
                [mod, "shift"],
                "Return",
                lazy.layout.toggle_split(),
                desc="Toggle between split and unsplit sides of stack",
            ),
            Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
            Key(["mod1"], "Tab", lazy.screen.toggle_group(), desc="Toggle last group"),
            # Toggle between different layouts as defined below
            Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
            Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
            Key(
                [mod],
                "f",
                lazy.window.toggle_fullscreen(),
                desc="Toggle fullscreen on the focused window",
            ),
            Key(
                [mod],
                "t",
                lazy.window.toggle_floating(),
                desc="Toggle floating on the focused window",
            ),
            Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
            Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
            Key(
                [mod],
                "r",
                lazy.spawncmd(),
                desc="Spawn a command using a prompt widget",
            ),
            Key([mod], "p", lazy.spawn("rofi -show drun"), desc="Launch a program"),
            Key([mod], "i", lazy.spawn(wifi_path), desc="Launch network selector"),
            Key(
                [mod],
                "k",
                lazy.spawn("rofi -show calc -modi calc -no-show-match -no-sort"),
                desc="Launch calculator",
            ),
            Key(
                [mod],
                "s",
                lazy.spawn("systemctl suspend"),
                desc="suspend system",
            ),
            Key(
                [],
                "XF86AudioRaiseVolume",
                lazy.widget["pulsevolume"].increase_vol(),
                desc="Raise Volume",
            ),
            Key(
                [],
                "XF86AudioLowerVolume",
                lazy.widget["pulsevolume"].decrease_vol(),
                desc="Lower Volume",
            ),
            Key([], "XF86AudioMute", lazy.widget["pulsevolume"].mute(), desc="Mute"),
            # Key([], "XF86MonBrightnessUp", pass, desc="Brightness up"),
            # Key([], "XF86MonBrightnessDown", pass, desc="Brightness down"),
        ]

        self.mouse = [
            Drag(
                [mod],
                "Button1",
                lazy.window.set_position_floating(),
                start=lazy.window.get_position(),
            ),
            Drag(
                [mod],
                "Button3",
                lazy.window.set_size_floating(),
                start=lazy.window.get_size(),
            ),
            Click([mod], "Button2", lazy.window.bring_to_front()),
        ]
