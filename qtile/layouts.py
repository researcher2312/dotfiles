from libqtile import layout

class Layouts:
    def __init__(self):
        self.layouts = [
            layout.Columns(
                border_focus="#b0d1ed",
                border_normal="#020385",
                margin=3,
                border_width=2),
            layout.Max(),
            # Try more layouts by unleashing below layouts.
            # layout.Stack(num_stacks=2),
            # layout.Bsp(),
            # layout.Matrix(),
            # layout.MonadTall(),
            # layout.MonadWide(),
            # layout.RatioTile(),
            # layout.Tile(),
            # layout.TreeTab(),
            # layout.VerticalTile(),
            # layout.Zoomy(),
        ]

    def init_layouts(self):
        return self.layouts
