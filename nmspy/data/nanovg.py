# Hello games uses nanovg (https://github.com/memononen/nanovg) for a lot of their UI rendering under the
# hood.

# This file exposes a number of functions as hooks so that they can be used directly if needed.

# NOTE: THe API provided by this is currently very WIP. It will likely not work properly at all.
# You have been warned.

import ctypes
from typing import Annotated

from pymhf.core.hooking import static_function_hook
from pymhf.core.memutils import get_addressof
from pymhf.core.structs import Field, partial_struct
from pymhf.extensions.ctypes import c_char_p64


@partial_struct
class NVGpoint(ctypes.Structure):
    x: Annotated[float, Field(ctypes.c_float, 0x0)]
    y: Annotated[float, Field(ctypes.c_float, 0x4)]
    dx: Annotated[float, Field(ctypes.c_float, 0x8)]
    dy: Annotated[float, Field(ctypes.c_float, 0xC)]
    len: Annotated[float, Field(ctypes.c_float, 0x10)]
    dmx: Annotated[float, Field(ctypes.c_float, 0x14)]
    dmy: Annotated[float, Field(ctypes.c_float, 0x18)]
    flags: Annotated[int, Field(ctypes.c_uint8, 0x1C)]


@partial_struct
class NVGpath(ctypes.Structure):
    pass


@partial_struct
class NVGvertex(ctypes.Structure):
    x: Annotated[float, Field(ctypes.c_float, 0x0)]
    y: Annotated[float, Field(ctypes.c_float, 0x4)]
    u: Annotated[float, Field(ctypes.c_float, 0x8)]
    v: Annotated[float, Field(ctypes.c_float, 0xC)]


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

    def set_values(self, r: float, g: float, b: float, a: float):
        self.r = r
        self.g = g
        self.b = b
        self.a = a


@partial_struct
class NVGpaint(ctypes.Structure):
    _total_size_ = 0x50
    xform: Annotated[tuple[float, float, float, float, float, float], Field(ctypes.c_float * 6, 0x0)]
    extent: Annotated[tuple[float, float], Field(ctypes.c_float * 2, 0x18)]
    radius: Annotated[float, Field(ctypes.c_float, 0x20)]
    feather: Annotated[float, Field(ctypes.c_float, 0x24)]
    innerColor: Annotated[NVGcolor, 0x28]
    outerColor: Annotated[NVGcolor, 0x38]
    image: Annotated[int, Field(ctypes.c_int32, 0x48)]
    desaturation: Annotated[float, Field(ctypes.c_float, 0x4C)]

    def clear(self):
        ctypes.memset(get_addressof(self), 0, self._total_size_)


@partial_struct
class NVGcompositeOperationState(ctypes.Structure):
    srcRGB: Annotated[int, Field(ctypes.c_int32, 0x0)]
    dstRGB: Annotated[int, Field(ctypes.c_int32, 0x4)]
    srcAlpha: Annotated[int, Field(ctypes.c_int32, 0x8)]
    dstAlpha: Annotated[int, Field(ctypes.c_int32, 0xC)]


@partial_struct
class NVGstate(ctypes.Structure):
    shapeAntiAlias: Annotated[int, Field(ctypes.c_int32, 0x0)]
    fill: Annotated[NVGpaint, 0x4]
    stroke: Annotated[NVGpaint, 0x54]
    strokeWidth: Annotated[float, Field(ctypes.c_float, 0xA4)]
    miterLimit: Annotated[float, Field(ctypes.c_float, 0xA8)]
    lineJoin: Annotated[int, Field(ctypes.c_int32, 0xAC)]
    lineCap: Annotated[int, Field(ctypes.c_int32, 0xB0)]
    alpha: Annotated[float, Field(ctypes.c_float, 0xB4)]
    xform: Annotated[tuple[float, float, float, float, float, float], Field(ctypes.c_float * 6, 0xB8)]
    fontSize: Annotated[float, Field(ctypes.c_float, 0xF0)]
    letterSpacing: Annotated[float, Field(ctypes.c_float, 0xF4)]
    lineHeight: Annotated[float, Field(ctypes.c_float, 0xF8)]
    fontBlur: Annotated[float, Field(ctypes.c_float, 0xFC)]
    textAlign: Annotated[int, Field(ctypes.c_int32, 0x100)]
    fontId: Annotated[int, Field(ctypes.c_int32, 0x104)]


@partial_struct
class NVGpathCache(ctypes.Structure):
    points: Annotated[ctypes._Pointer[NVGpoint], 0x0]
    npoints: Annotated[int, Field(ctypes.c_int32, 0x8)]
    cpoints: Annotated[int, Field(ctypes.c_int32, 0xC)]
    paths: Annotated[ctypes._Pointer[NVGpath], 0x10]
    npaths: Annotated[int, Field(ctypes.c_int32, 0x18)]
    cpaths: Annotated[int, Field(ctypes.c_int32, 0x1C)]
    verts: Annotated[ctypes._Pointer[NVGvertex], 0x20]
    nverts: Annotated[int, Field(ctypes.c_int32, 0x28)]
    cverts: Annotated[int, Field(ctypes.c_int32, 0x2C)]
    bounds: Annotated[tuple[float, float, float, float], Field(ctypes.c_float * 4, 0x30)]


@partial_struct
class NVGcontext(ctypes.Structure):
    commands: Annotated[ctypes._Pointer[ctypes.c_float], 0x90]
    ccommands: Annotated[int, Field(ctypes.c_int32, 0x98)]
    ncommands: Annotated[int, Field(ctypes.c_int32, 0x9C)]
    commandx: Annotated[float, Field(ctypes.c_float, 0xA0)]
    commandy: Annotated[float, Field(ctypes.c_float, 0xA4)]
    states: Annotated[tuple[NVGstate, ...], Field(NVGstate * 0x40, 0xA8)]
    nstates: Annotated[int, Field(ctypes.c_int32, 0x42A8)]
    cache: Annotated[ctypes._Pointer[NVGpathCache], 0x42B0]


# NOTE: Pattern not correct
@static_function_hook("48 8B C4 48 89 58 ? 48 89 68 ? F3 0F 11 50")
def nvgArc(
    ctx: ctypes._Pointer[NVGcontext],
    cx: Annotated[float, ctypes.c_float],
    cy: Annotated[float, ctypes.c_float],
    r: Annotated[float, ctypes.c_float],
    a0: Annotated[float, ctypes.c_float],
    a1: Annotated[float, ctypes.c_float],
    dir: Annotated[float, ctypes.c_int32],
):
    """Adds an arc segment at the corner defined by the last path point, and two specified points."""
    ...


@static_function_hook("48 8B C4 48 89 70 ? 55 57 41 54 41 56 41 57 48 8D A8")
def nvgText(
    ctx: ctypes._Pointer[NVGcontext],
    x: Annotated[float, ctypes.c_float],
    y: Annotated[float, ctypes.c_float],
    string: c_char_p64,
    end: c_char_p64,
):
    """Draws text string at specified location.
    If end is specified only the sub-string up to the end is drawn."""
    ...


@static_function_hook("48 8B C4 48 89 58 ? F3 0F 11 58 ? 4C 89 40 ? 48 89 48")
def nvgTextBreakLines(
    ctx: ctypes._Pointer[NVGcontext],
    string: c_char_p64,
    end: ctypes.c_char_p,
    breakRowWidth: Annotated[float, ctypes.c_float],
    rows: ctypes.c_uint64,  # NVGtextRow *
    maxRows: Annotated[int, ctypes.c_int32],
): ...


@static_function_hook("4C 8B DC 53 56 57 41 54 48 81 EC")
def nvgTextBox(
    ctx: ctypes._Pointer[NVGcontext],
    x: Annotated[float, ctypes.c_float],
    y: Annotated[float, ctypes.c_float],
    breakRowWidth: Annotated[float, ctypes.c_float],
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
    "48 89 5C 24 ? 57 48 81 EC ? ? ? ? 48 63 81 ? ? ? ? 48 8B D9 48 69 F8 ? ? ? ? 0F 10 44 0F"
)
def nvgFill(ctx: ctypes._Pointer[NVGcontext]): ...


@static_function_hook("48 8B C4 55 48 8D 68 ? 48 81 EC ? ? ? ? F3 0F 10 6D")
def nvgEllipse(
    ctx: ctypes._Pointer[NVGcontext],
    cx: Annotated[float, ctypes.c_float],
    cy: Annotated[float, ctypes.c_float],
    rx: Annotated[float, ctypes.c_float],
    ry: Annotated[float, ctypes.c_float],
): ...


@static_function_hook("48 8B C4 48 83 EC ? 0F 28 E2")
def nvgRect(
    ctx: ctypes._Pointer[NVGcontext],
    x: Annotated[float, ctypes.c_float],
    y: Annotated[float, ctypes.c_float],
    w: Annotated[float, ctypes.c_float],
    h: Annotated[float, ctypes.c_float],
): ...


@static_function_hook("48 89 6C 24 ? 48 89 74 24 ? 48 89 54 24 ? 57 41 56 41 57 48 83 EC ? 45 8B F9")
def NVGRegisterTexture(
    ctx: ctypes._Pointer[NVGcontext],
    lpTkTexture: ctypes.c_uint64,  # cTkTexture *
    liRenderBufferObject: Annotated[int, ctypes.c_uint32],
    liImageFlags: Annotated[int, ctypes.c_int32],
) -> ctypes.c_uint64: ...


@static_function_hook("48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 0F 29 74 24 ? 33 ED")
def nvgBeginFrame(
    ctx: ctypes._Pointer[NVGcontext],
    windowWidth: Annotated[int, ctypes.c_int32],
    windowHeight: Annotated[int, ctypes.c_int32],
    devicePixelRatio: Annotated[float, ctypes.c_float],
): ...


@static_function_hook("40 53 48 83 EC ? 48 8B 41 ? 48 8B D9 48 8B 09")
def nvgEndFrame(ctx: ctypes._Pointer[NVGcontext]): ...


@static_function_hook(
    "48 89 5C 24 ? 57 48 81 EC ? ? ? ? 48 63 81 ? ? ? ? 48 8B D9 48 69 F8 ? ? ? ? 0F 29 B4 24"
)
def nvgStroke(ctx: ctypes._Pointer[NVGcontext]): ...


def nvgRestore(ctx: ctypes._Pointer[NVGcontext]):
    # Actually implement this ourselves since it's simple and hooking will likely be too fragile.
    if ctx:
        _ctx = ctx.contents
        if _ctx.nstates <= 1:
            return
        _ctx.nstates = _ctx.nstates - 1


def nvgBeginPath(ctx: ctypes._Pointer[NVGcontext]):
    if ctx:
        _ctx = ctx.contents
        _ctx.ncommands = 0


def nvgStrokeColor(ctx: ctypes._Pointer[NVGcontext], r: float, g: float, b: float, a: float):
    state = nvg__getState(ctx)
    nvg__setPaintColor(state.contents.stroke, r, g, b, a)


def nvgFillColor(ctx: ctypes._Pointer[NVGcontext], r: float, g: float, b: float, a: float):
    state = nvg__getState(ctx)
    nvg__setPaintColor(state.contents.fill, r, g, b, a)


def nvgStrokeWidth(ctx: ctypes._Pointer[NVGcontext], width: float):
    state = nvg__getState(ctx)
    state.contents.strokeWidth = width


def nvg__clearPathCache(ctx: ctypes._Pointer[NVGcontext]):
    _ctx = ctx.contents
    _ctx.cache.contents.npoints = 0
    _ctx.cache.contents.npaths = 0


def nvg__getState(ctx: ctypes._Pointer[NVGcontext]) -> ctypes._Pointer[NVGstate]:
    return ctypes.pointer(ctx.contents.states[ctx.contents.nstates - 1])


def nvg__setPaintColor(p: NVGpaint, r: float, g: float, b: float, a: float):
    p.clear()
    p.xform[0] = 1.0
    p.xform[1] = 0.0
    p.xform[2] = 0.0
    p.xform[3] = 1.0
    p.xform[4] = 0.0
    p.xform[5] = 0.0
    p.radius = 0.0
    p.feather = 1.0
    p.innerColor.set_values(r, g, b, a)
    p.outerColor.set_values(r, g, b, a)
