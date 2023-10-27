from libqtile import bar
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

class Widget:
    def __init__(self):
        widget_defaults = dict(
            font="Fira Code",
            fontsize=12,
            padding=3,
        )
        extension_defaults = widget_defaults.copy()

        powerline = {
                "decorations": [
                    PowerLineDecoration(path="arrow_right")
                ]
            }
        powerline_left = {
                "decorations": [
                    PowerLineDecoration()
                ]
            }

        self.mybar = bar.Bar(
                    [
                        widget.GroupBox(background="dddddd80", **powerline_left),
                        widget.Prompt(),
                        widget.WindowName(background="cccccc80", **powerline),
                        widget.Chord(
                            chords_colors={
                                "launch": ("#ff0000", "#ffffff"),
                            },
                            name_transform=lambda name: name.upper(),
                            **powerline
                        ),
                        widget.Pomodoro(
                            length_long_break=25,
                            length_short_break=5,
                            length_pomodori=20,
                            color_active='F38BA8',
                            color_break='A6E3A1',
                            color_inactive='BAC2DE',
                            background="aaaaaa80",
                            **powerline
                        ),
                        widget.CPU(
                            format='CPU {load_percent}%',
                            update_interval=5,
                            background="88888880",
                            **powerline
                        ),
                        widget.Memory(
                            format='MEM {MemPercent}%',
                            update_interval=5,
                            background = "66666680",
                            **powerline
                        ),
                        widget.Battery(
                            format='BAT {percent:2.0%}',
                            show_short_text = False,
                            update_interval=60,
                            background="44444480",
                            **powerline
                        ),
                        # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                        # widget.StatusNotifier(),
                        widget.PulseVolume(fmt="VLM {}", background="22222288", **powerline),                
                        widget.Clock(format="%d/%m %a %H:%M", background="00000088"),
                    ],
                    25,
                    background="#80808080",
                    border_width=[0, 0, 0, 0],  # Draw top and bottom borders
                    border_color=["000000", "000000", "000000", "000000"]  # Borders are transparent
                )

    def get_widget(self):
        return self.mybar

