from libqtile import bar
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration
from qtile_extras.popup.toolkit import PopupGridLayout, PopupText
from themes import ColorGradient


widget_defaults = dict(
    font="Fira Code",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

powerline = {"decorations": [PowerLineDecoration(path="arrow_right")]}
powerline_left = {"decorations": [PowerLineDecoration()]}

gradient = ColorGradient("ff0000", "00ff00", "80", 9)


class VolumePopup(PopupGridLayout):
    def __init__(self, qtile):
        super().__init__(
            qtile,
            rows=1,
            cols=2,
            close_on_click=False,
            controls=[
                PopupText(name="text", col=0, h_align="center", text="kolumna 0"),
                PopupText(col=1, h_align="center", text="kolumna 1"),
            ],
        )


class SystemConfigurationValues:
    volume = 50
    brightness = 0
    volume_popup = None
    system_bar = None


@lazy.function
def show_volume(qtile):
    if SystemConfigurationValues.system_bar != None:
        SystemConfigurationValues.system_bar.update_system_values()
    if SystemConfigurationValues.volume_popup != None:
        SystemConfigurationValues.volume_popup.show(centered=True)
        SystemConfigurationValues.volume_popup.update_controls(
            text=str(SystemConfigurationValues.volume)
        )


@lazy.function
def hide_volume(qtile):
    if SystemConfigurationValues.volume_popup != None:
        SystemConfigurationValues.volume_popup.hide()


class ArrowBar(bar.Bar):
    def __init__(self):
        self.group_box = widget.GroupBox(
            background=gradient.get_color(), **powerline_left
        )
        self.prompt = widget.Prompt()
        self.window_name = widget.WindowName(
            background=gradient.get_color(), **powerline
        )
        self.chords = widget.Chord(
            chords_colors={
                "launch": ("#ff0000", "#ffffff"),
            },
            name_transform=lambda name: name.upper(),
            **powerline
        )
        self.launch_popup_text = widget.TextBox(
            text="Launch popup",
            mouse_callbacks={"Button1": show_volume(), "Button3": hide_volume()},
            background=gradient.get_color(),
            **powerline
        )
        self.pomodoro = widget.Pomodoro(
            length_long_break=25,
            length_short_break=5,
            length_pomodori=20,
            color_active="F38BA8",
            color_break="A6E3A1",
            color_inactive="BAC2DE",
            background=gradient.get_color(),
            **powerline
        )
        self.cpu = widget.CPU(
            format="CPU {load_percent}%",
            update_interval=5,
            background=gradient.get_color(),
            **powerline
        )
        self.memory = widget.Memory(
            format="MEM {MemPercent}%",
            update_interval=5,
            background=gradient.get_color(),
            **powerline
        )
        
        self.battery = widget.Battery(
            format="BAT {percent:2.0%}",
            show_short_text=False,
            update_interval=60,
            background=gradient.get_color(),
            **powerline
        )
        self.volume_widget = widget.PulseVolume(
            fmt="VLM {}", background=gradient.get_color(), **powerline
        )

        self.clock = widget.Clock(
            format="%d/%m %a %H:%M", background=gradient.get_color()
        )
        widgets = [
            self.group_box,
            self.prompt,
            self.window_name,
            self.chords,
            self.launch_popup_text,
            self.pomodoro,
            self.cpu,
            self.memory,
            self.battery,
            self.volume_widget,
            self.clock,
        ]
        super().__init__(widgets, 25, background="#80808080")

    def update_system_values(self):
        SystemConfigurationValues.volume = self.volume_widget.get_volume()
