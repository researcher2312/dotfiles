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


class VolumePopup(PopupGridLayout):
    def __init__(self, qtile):
        self.is_visible = False
        super().__init__(
            qtile,
            rows=2,
            cols=2,
            height=50,
            width=200,
            close_on_click=False,
            controls=[
                PopupText(col=0, row=0, h_align="center", text="Volume"),
                PopupSlider(
                    col=1,
                    row=0,
                    max_value=100,
                    marker_size=0,
                    bar_size=10,
                    name="volume",
                ),
                PopupText(col=0, row=1, h_align="center", text="Brightness"),
                PopupSlider(
                    col=1,
                    row=1,
                    max_value=100,
                    marker_size=0,
                    bar_size=10,
                    name="brightness",
                ),
            ],
        )

#class SystemConfigurationValues:
#    volume = 50
#    brightness = 0
#    volume_popup = None
#    system_bar = None
#    popup_visible = False


@lazy.function
def show_popup(qtile):
    bar = qtile.screens[0].top
    if bar.popup == None:
        bar.popup = VolumePopup(qtile)
    popup = bar.popup
    if popup.is_visible:
        popup.is_visible = False
        popup.hide()
    else:
        popup.is_visible = True
        popup.show(relative_to=3, relative_to_bar=True, x=-3, y=5)
        popup.popup.win.keep_above(True)
        popup.popup.win.move_to_top()
        popup.update_controls(volume=bar.get_volume())

class ArrowBar(bar.Bar):
    def __init__(self, gradient):
        self.popup = None
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
            fmt="{}",
            emoji=True,
            emoji_list=["󰸈", "󰕿", "󰖀", "󰕾"],
            fontsize=18,
            background=gradient.get_color(),
            **powerline
        )
        #self.volume_popup = widget.PulseVolumeExtra(mode="popup")
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
            #self.volume_popup,
            self.clock,
        ]
        super().__init__(widgets, 25, background="#80808080", margin=[5, 5, 1, 5])

    def get_volume(self):
        return self.volume_widget.get_volume()
