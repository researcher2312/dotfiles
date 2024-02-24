from math import modf


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
            int(self.red * multiplier),
            int(self.green * multiplier),
            int(self.blue * multiplier),
        )

    def __str__(self):
        return f"{self.red:02x}{self.green:02x}{self.blue:02x}"


class ColorGradient:
    def __init__(self, input_colors, shades_count, transparency="ff"):
        new_colors = []
        [new_colors.append(RGB.fromstring(color)) for color in input_colors]
        self.transparency = transparency
        self.calls = -1
        distance = (len(input_colors) - 1) / (shades_count - 1)
        self.colors = []
        for i in range(0, shades_count - 1):
            frac_color, int_color = modf(i * distance)
            starting_color = new_colors[int(int_color)]
            ending_color = new_colors[int(int_color) + 1]
            self.colors.append(
                starting_color + (ending_color - starting_color) * frac_color
            )
        self.colors.append(new_colors[-1])

    def get_color(self):
        self.calls += 1
        return str(self.colors[self.calls]) + self.transparency
