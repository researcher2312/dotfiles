from libqtile import bar
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration
from qtile_extras.popup.toolkit import PopupGridLayout, PopupText, PopupSlider
from colortools import ColorGradient


widget_defaults = dict(
    font="FiraCode Nerd Font",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

powerline = {"decorations": [PowerLineDecoration(path="arrow_right")]}
powerline_left = {"decorations": [PowerLineDecoration()]}

gradient = ColorGradient("a4aab6", "172126", "80", 9)


class VolumePopup(PopupGridLayout):
    def __init__(self, qtile):
        super().__init__(
            qtile,
            rows=2,
            cols=2,
            height=50,
            width=200,
            close_on_click=False,
            controls=[
                PopupText(col=0, row=0, h_align="center", text="Volume"),
                PopupSlider(col=1, row=0, max_value=100, marker_size=0, name="volume"),
                PopupText(col=0, row=1, h_align="center", text="Brightness"),
                PopupSlider(
                    col=1, row=1, max_value=100, marker_size=0, name="brightness"
                ),
            ],
        )


class SystemConfigurationValues:
    volume = 50
    brightness = 0
    volume_popup = None
    system_bar = None
    popup_visible = False


@lazy.function
def show_popup(qtile):
    if SystemConfigurationValues.popup_visible == False:
        if SystemConfigurationValues.system_bar != None:
            SystemConfigurationValues.system_bar.update_system_values()
        if SystemConfigurationValues.volume_popup != None:
            SystemConfigurationValues.popup_visible = True
            SystemConfigurationValues.volume_popup.show(
                relative_to=3, relative_to_bar=True
            )
            SystemConfigurationValues.volume_popup.update_controls(
                volume=SystemConfigurationValues.volume
            )
    else:
        if SystemConfigurationValues.volume_popup != None:
            SystemConfigurationValues.volume_popup.hide()
            SystemConfigurationValues.popup_visible = False


@lazy.function
def hide_volume(qtile):
    pass


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
            mouse_callbacks={"Button1": show_popup()},
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
            format="\uf4bc   {load_percent}%",
            update_interval=5,
            background=gradient.get_color(),
            **powerline
        )
        self.memory = widget.Memory(
            format="\uf2db   {MemPercent}%",
            update_interval=5,
            background=gradient.get_color(),
            **powerline
        )
        self.battery = widget.Battery(
            format="\uf240    {percent:2.0%}",
            show_short_text=False,
            update_interval=60,
            background=gradient.get_color(),
            **powerline
        )
        self.volume_widget = widget.PulseVolume(
            fmt="\uf028   {}", background=gradient.get_color(), **powerline
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
        super().__init__(widgets, 25, background="#80808080", margin=[5, 5, 1, 5])

    def update_system_values(self):
        SystemConfigurationValues.volume = self.volume_widget.get_volume()

