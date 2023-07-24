# MarcosRodrui
# Based on the Configuration of Antonio Sarosi

from libqtile import widget
from .theme import colors
from libqtile.command import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.widget.decorations import PowerLineDecoration
from qtile_extras.widget import UPowerWidget, ALSAWidget
from qtile_extras.popup.toolkit import (
    PopupRelativeLayout,
    PopupImage,
    PopupText
)

def show_power_menu(qtile):
    controls = [
        PopupImage(
            filename="/home/marcosrodrui/.config/qtile/images/atium.webp",
            pos_x=0.15,
            pos_y=0.1,
            width=0.1,
            height=0.52,
            highlight_method="mask",
            highlight="#26a98b",
            mouse_callbacks={
                "Button1": lazy.spawn("reboot")
            }
        ),
        PopupImage(
            filename="/home/marcosrodrui/.config/qtile/images/ettmetal.webp",
            pos_x=0.45,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            highlight_method="mask",
            highlight="#c33027",
            mouse_callbacks={
                "Button1": lazy.spawn("shutdown now")
            }
        ),
        PopupImage(
            filename="/home/marcosrodrui/.config/qtile/images/lerasium.webp",
            pos_x=0.75,
            pos_y=0.1,
            width=0.08,
            height=0.53,
            highlight_method="mask",
            highlight="#edb54b",
            mouse_callbacks={
                "Button1": lazy.spawn("betterlockscreen -l dimblur")
            }
        ),
        PopupText(
            text="Reboot",
            pos_x=0.1,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            font="Hurmit Nerd Font",
            fontsize=20,
            h_align="center"
        ),
        PopupText(
            text="Shutdown",
            pos_x=0.405,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            font="Hurmit Nerd Font",
            fontsize=20,
            h_align="center"
        ),
        PopupText(
            text="Lock",
            pos_x=0.687,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            font="Hurmit Nerd Font",
            fontsize=20,
            h_align="center"
        ),
        PopupText(
            text="There’s always another secret",
            pos_x=0.25,
            pos_y=0.93,
            width=0.5,
            height=0.05,
            font="Mistborn",
            fontsize=17,
            foreground="#195465A0",
            h_align="center"
        ),
    ]

    layout = PopupRelativeLayout(
        qtile,
        width=1000,
        height=200,
        controls=controls,
        background="0a0f1460",
        initial_focus=1,
    )
    layout.show(centered=True)
