from chromia.utils import clip_rgb, limit


class Color:
    """The main color class."""

    _hsl = None

    def __init__(self, color=None, **kwargs):
        """Accepts any color."""
        if isinstance(color, Color):
            self.web = color.web
        else:
            self.web = color if color else "black"

        for k, v in kwargs.items():
            setattr(self, k, v)

    def __getattr__(self, name):
        if name.startswith("get_"):
            raise AttributeError(f"'{name}' not found")

    def __setattr__(self, key, value):
        if key not in ("_hsl", "equality"):
            fc = getattr(self, "set_" + key)
            fc(value)
        else:
            self.__dict__[key] = value
