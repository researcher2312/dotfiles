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


def show_popup(qtile):
    test_popup = PopupGridLayout(
        qtile,
        rows=1,
        cols=3,
        height=50,
        width=300,
        background="00000080",
        hide_on_timeout=2,
        close_on_click=False,
        controls=[
            PopupText(col=0, h_align="center", text="kolumna 0"),
            PopupText(col=1, h_align="center", text="kolumna 1"),
            PopupText(col=2, h_align="center", text="kolumna 2"),
        ],
    )
    test_popup.show(relative_to=3, relative_to_bar=True, y=5, x=-5)


arrow_bar = bar.Bar(
    [
        widget.GroupBox(background=gradient.get_color(), **powerline_left),
        widget.Prompt(),
        widget.WindowName(background=gradient.get_color(), **powerline),
        widget.Chord(
            chords_colors={
                "launch": ("#ff0000", "#ffffff"),
            },
            name_transform=lambda name: name.upper(),
            **powerline
        ),
        widget.TextBox(
            text="Launch popup",
            mouse_callbacks={"Button1": lazy.function(show_popup)},
            background=gradient.get_color(),
            **powerline
        ),
        widget.Pomodoro(
            length_long_break=25,
            length_short_break=5,
            length_pomodori=20,
            color_active="F38BA8",
            color_break="A6E3A1",
            color_inactive="BAC2DE",
            background=gradient.get_color(),
            **powerline
        ),
        widget.CPU(
            format="CPU {load_percent}%",
            update_interval=5,
            background=gradient.get_color(),
            **powerline
        ),
        widget.Memory(
            format="MEM {MemPercent}%",
            update_interval=5,
            background=gradient.get_color(),
            **powerline
        ),
        widget.Battery(
            format="BAT {percent:2.0%}",
            show_short_text=False,
            update_interval=60,
            background=gradient.get_color(),
            **powerline
        ),
        # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
        # widget.StatusNotifier(),
        widget.Volume(fmt="VLM {}", background=gradient.get_color(), **powerline),
        widget.Clock(format="%d/%m %a %H:%M", background=gradient.get_color()),
    ],
    25,
    background="#80808080",
    border_width=[0, 0, 0, 0],  # Draw top and bottom borders
    border_color=["000000", "000000", "000000", "000000"],  # Borders are transparent
)
