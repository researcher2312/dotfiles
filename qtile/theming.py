from themes import theme
from widgets import ArrowBar

class DefaultTheme(QtileTheme):
    def __init__(self):
        self.status_bar = ArrowBar()
        self.status_popup
