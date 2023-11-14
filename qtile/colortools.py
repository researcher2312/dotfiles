class RGB:
    def __init__(self, r: int = 0, g: int = 0, b: int = 0):
        self.red = r
        self.green = g
        self.blue = b

    @classmethod
    def fromstring(self, colorstring):
        red = int(colorstring[:2], 16)
        green = int(colorstring[2:4], 16)
        blue = int(colorstring[4:], 16)
        return RGB(red, green, blue)

    def __add__(self, added):
        return RGB(
            r=self.red + added.red, g=self.green + added.green, b=self.blue + added.blue
        )

    def __sub__(self, substracted):
        return RGB(
            r=self.red - substracted.red,
            g=self.green - substracted.green,
            b=self.blue - substracted.blue,
        )

    def __truediv__(self, division):
        return RGB(
            int(self.red / division),
            int(self.green / division),
            int(self.blue / division),
        )

    def __mul__(self, multiplier):
        return RGB(
            self.red * multiplier, self.green * multiplier, self.blue * multiplier
        )

    def __str__(self):
        return f"{self.red:02x}{self.green:02x}{self.blue:02x}"


class ColorGradient:
    def __init__(self, start_color, end_color, transparency, shades_count):
        self.start_color = RGB.fromstring(start_color)
        self.end_color = RGB.fromstring(end_color)
        self.transparency = transparency
        self.calls = -1
        self.color_difference = (self.end_color - self.start_color) / (shades_count - 1)

    def get_color(self):
        self.calls += 1
        return (
            str(self.start_color + self.color_difference * (self.calls))
            + self.transparency
        )



