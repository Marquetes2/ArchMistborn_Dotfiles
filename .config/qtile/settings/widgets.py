# MarcosRodrui
# Based on the Configuration of Antonio Sarosi

from libqtile import widget
from .theme import colors
from libqtile.command import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration
from .power_menu import show_power_menu

def base(fg='text', bg='dark'):
    return{
        'foreground':colors[fg],
        'decorations': [
            RectDecoration(
                line_width=0,
                colour=colors[bg],
                filled = True,
                radius=15, 
                clip=True,
                group=True,
            )
        ]
    }

def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)

def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )

def cpu_info():
    return [
            widget.TextBox(
                **base(bg='color2'),
                text='',
                fontsize=20,
                padding=10
            ),
            widget.CPU(
                **base(bg='color2'),
                format='{freq_current}GHz {load_percent}% ',
            ),
    ]

def memory_info():
    return [
            widget.TextBox(
                **base(bg='color2'),
                text='',
                fontsize=20,
                padding=10
            ),
            widget.Memory(
                **base(bg='color2'),
                format='{MemUsed: .0f}{mm} ',
            ),
    ]

def workspaces(): 
    return [
        widget.GroupBox(
            **base(),
            font='Mistborn',
            fontsize=34,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=3,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True,
        ),
    ]

def systray():
    return [
        widget.Systray(
            padding=0,
        )
    ]

def my_button():
    return [
        widget.Image(
            filename='/home/marcosrodrui/.config/qtile/images/ettmetal.webp', 
            mouse_callbacks={"Button1": lazy.spawn("/home/marcosrodrui/.config/rofi/powermenu/type-5/powermenu.sh")},
        ),
    ]

primary_widgets = [
    widget.Clock(**base(bg='color3'), format=' %d/%m/%Y - %H:%M:%S '),
    widget.Spacer(length=20),
    *cpu_info(),
    widget.Spacer(length=10),
    *memory_info(),
    widget.Spacer(),
    *workspaces(),
    widget.Spacer(),
    *systray(),
    widget.Spacer(length=5),
    *my_button(),
]

secondary_widgets = [
    widget.Spacer(),
    *workspaces(),
    widget.Spacer(),
    widget.Clock(**base(bg='color2'), format=' %d/%m/%Y - %H:%M:%S '),
]

widget_defaults = {
    'font': 'Hurmit Nerd Font',
    'fontsize': 16,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
