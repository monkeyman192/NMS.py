# Hello games uses nanovg (https://github.com/memononen/nanovg) for a lot of their UI rendering under the
# hood.

# This file exposes a number of functions as hooks so that they can be used directly if needed.

import ctypes

from pymhf.core.hooking import static_function_hook


class NVGcontext(ctypes.Structure):
    pass


class NVGcolor(ctypes.Structure):
    _fields_ = [
        ("r", ctypes.c_float),
        ("g", ctypes.c_float),
        ("b", ctypes.c_float),
        ("a", ctypes.c_float),
    ]
    r: float
    g: float
    b: float
    a: float


class NVGpaint(ctypes.Structure):
    _fields_ = [
        ("xform", ctypes.c_float * 6),
        ("extent", ctypes.c_float * 2),
        ("radius", ctypes.c_float),
        ("feather", ctypes.c_float),
        ("innerColor", NVGcolor),
        ("outerColor", NVGcolor),
        ("image", ctypes.c_int32),
        ("desaturation", ctypes.c_float),
    ]


@static_function_hook("48 8B C4 48 89 58 ? 48 89 68 ? F3 0F 11 50")
def nvgArc(
    ctx: ctypes._Pointer[NVGcontext],
    cx: ctypes.c_float,
    cy: ctypes.c_float,
    r: ctypes.c_float,
    a0: ctypes.c_float,
    a1: ctypes.c_float,
    dir: ctypes.c_int32,
):
    """Adds an arc segment at the corner defined by the last path point, and two specified points."""
    ...


@static_function_hook(
    "48 8B C4 48 89 58 ? 48 89 70 ? 55 57 41 54 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 0F 29 70 ? 48 8B F9 0F 29 78"
)
def nvgText(
    ctx: ctypes._Pointer[NVGcontext],
    x: ctypes.c_float,
    y: ctypes.c_float,
    string: ctypes.c_char_p,
    end: ctypes.c_char_p,
):
    """Draws text string at specified location.
    If end is specified only the sub-string up to the end is drawn."""
    ...


@static_function_hook("4C 8B DC 53 56 57 41 54 48 81 EC")
def nvgTextBox(
    ctx: ctypes._Pointer[NVGcontext],
    x: ctypes.c_float,
    y: ctypes.c_float,
    breakRowWidth: ctypes.c_float,
    string: ctypes.c_char_p,
    end: ctypes.c_char_p,
):
    """
    Draws multi-line text string at specified location wrapped at the specified width.
    If end is specified only the sub-string up to the end is drawn.
    White space is stripped at the beginning of the rows, the text is split at word boundaries or when
    new-line characters are encountered.
    Words longer than the max width are slit at nearest character (i.e. no hyphenation).
    """
    ...


@static_function_hook(
    "48 89 5C 24 ? 48 89 74 24 ? 57 48 81 EC ? ? ? ? 48 63 81 ? ? ? ? 48 8B D9 48 69 F8"
)
def nvgFill(ctx: ctypes._Pointer[NVGcontext]): ...


@static_function_hook("48 8B C4 48 83 EC ? 0F 28 E2")
def nvgRect(
    ctx: ctypes._Pointer[NVGcontext],
    x: ctypes.c_float,
    y: ctypes.c_float,
    w: ctypes.c_float,
    h: ctypes.c_float,
): ...
