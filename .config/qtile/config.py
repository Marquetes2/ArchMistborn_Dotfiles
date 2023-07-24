
# Qtile Config File
# http://www.qtile.org/

# MarcosRodrui
# Original Configuration by Antonio Sarosi

# from typing import List  # noqa: F401

# from libqtile import bar, layout, widget, hook
# from libqtile.config import Click, Drag, Group, Key, Match, Screen
# from libqtile.lazy import lazy

from libqtile import hook

from settings.keys import mod, keys
from settings.groups import groups
from settings.layouts import layouts, floating_layout
from settings.widgets import widget_defaults, extension_defaults
from settings.screens import screens
from settings.mouse import mouse
from settings.path import qtile_path

from os import path
import subprocess

@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(path.expanduser('~'), '.config', 'qtile','autostart.sh')])


main = None
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = False
bring_front_click = False
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = 'urgent'
wmname = 'LG3D'

# mod = "mod4"
# terminal = "alacritty"

# keys = [
#     # Switch between windows
#     Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
#     Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
#     Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
#     Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
#     Key([mod], "space", lazy.layout.next(),
#         desc="Move window focus to other window"),

#     # Move windows between left/right columns or move up/down in current stack.
#     # Moving out of range in Columns layout will create new column.
#     Key([mod, "shift"], "Left", lazy.layout.shuffle_left(),
#         desc="Move window to the left"),
#     Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),
#         desc="Move window to the right"),
#     Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),
#         desc="Move window down"),
#     Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

#     # Grow windows. If current window is on the edge of screen and direction
#     # will be to screen edge - window would shrink.
#     Key([mod, "mod1"], "Left", lazy.layout.grow_left(),
#         desc="Grow window to the left"),
#     Key([mod, "mod1"], "Right", lazy.layout.grow_right(),
#         desc="Grow window to the right"),
#     Key([mod, "mod1"], "Down", lazy.layout.grow_down(),
#         desc="Grow window down"),
#     Key([mod, "mod1"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
#     Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

#     # Toggle between split and unsplit sides of stack.
#     # Split = all windows displayed
#     # Unsplit = 1 window displayed, like Max layout, but still with
#     # multiple stack panes
#     Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
#         desc="Toggle between split and unsplit sides of stack"),
#     Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

#     # Toggle between different layouts as defined below
#     Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
#     Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

#     Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
#     Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

#     # Moving between Screens
#     Key([mod, "control"], "Right", lazy.to_screen(0)),
#     Key([mod, "control"], "Left", lazy.to_screen(1)),

#     # Moving between Groups
#     #Key([mod, "space"], "Right", lazy.screen.next_group(),
#     #Key([mod, "space"], "Left", lazy.screen.prev_group(),

#     # Menu
#     Key([mod], "m", lazy.spawn("rofi -show drun")),
#     Key([mod, "shift"], "m", lazy.spawn("rofi -show")),

#     # Firefox
#     Key([mod, "shift"], "f", lazy.spawn("firefox")),

#     # Volume
#     Key([], "XF86AudioLowerVolume", lazy.spawn(
#         "pactl set-sink-volume @DEFAULT_SINK@ -5%")),
#     Key([], "XF86AudioRaiseVolume", lazy.spawn(
#         "pactl set-sink-volume @DEFAULT_SINK@ +5%")),
#     Key([], "XF86AudioMute", lazy.spawn(
#         "pactl set-sink-mute @DEFAULT_SINK@ toggle")),

#     # Brightness
#     Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
#     Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
# ]

# groups = [Group(i) for i in ["", "", "", "", "", "", "", "", ""]]

# for i, group in enumerate(groups):
#     actual_key = str(i + 1)
#     keys.extend([
#         # Switch to workspace N
#         Key([mod], actual_key, lazy.group[group.name].toscreen()),
#         # Send window to workspace N
#         Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
#     ])

# layout_conf = {
#     'border_focus': "#F07178",
#     'border_width': 1,
#     'margin': 1
# }

# layouts = [
#     layout.Columns(**layout_conf),
#     layout.Max(),
#     # Try more layouts by unleashing below layouts.
#     # layout.Stack(num_stacks=2),
#     # layout.Bsp(),
#     # layout.Matrix(),
#     # layout.MonadTall(**layout_conf),
#     # layout.MonadWide(),
#     # layout.RatioTile(),
#     # layout.Tile(),
#     # layout.TreeTab(),
#     #layout.VerticalTile(),
#     # layout.Zoomy(),
# ]

# widget_defaults = dict(
#     font='Hack Nerd Font',
#     fontsize=17,
#     padding=4,
# )
# extension_defaults = widget_defaults.copy()

# screens = [
#     Screen(
#         top=bar.Bar(
#             [
#                 widget.GroupBox(
#                     foreground=["#f1ffff", "#f1ffff"],
#                     background=["#0f101a", "#0f101a"],
#                     font='Hack Nerd Font',
#                     fontsize=19,
#                     margin_y=3,
#                     margin_x=0,
#                     padding_y=8,
#                     padding_x=5,
#                     borderwidth=1,
#                     active=["#f1ffff", "#f1ffff"],
#                     inactive=["#f1ffff", "#f1ffff"],
#                     rounded=False,
#                     highlight_method='block',
#                     urgent_alert_method='block',
#                     urgent_border=["#F07178", "#F07178"],
#                     this_current_screen_border=["#f07178", "#f07178"],
#                     this_screen_border=["#5c5c5c", "#5c5c5c"],
#                     other_current_screen_border=["#0f101a", "#0f101a"],
#                     other_screen_border=["#0f101a", "#0f101a"],
#                     disable_drag=True
#                 ),
#                 widget.WindowName(),
#                 widget.Systray(),
#                 widget.CurrentLayoutIcon(
#                     background=["#F07178", "#F07178"],
#                     foreground=["#0f101a","#0f101a"],
#                     scale=0.65
#                 ),
#                 widget.CurrentLayout(
#                     background=["#F07178", "#F07178"],
#                     foreground=["#0f101a","#0f101a"]
#                 ),
#                 widget.TextBox(
#                     background=["#a151d3","#a151d3"],
#                     foreground=["#0f101a","#0f101a"],
#                     text=''
#                 ),
#                 widget.Clock(
#                     background=["#a151d3","#a151d3"],
#                     foreground=["#0f101a","#0f101a"],
#                     format='%d/%m/%Y - %H:%M '
#                 ),
#             ],
#             24,
#             opacity=0.9
#         ),
#     ),
#     Screen(
#         top=bar.Bar(
#             [
#                 widget.GroupBox(
#                     foreground=["#f1ffff", "#f1ffff"],
#                     background=["#0f101a", "#0f101a"],
#                     font='Hack Nerd Font',
#                     fontsize=19,
#                     margin_y=3,
#                     margin_x=0,
#                     padding_y=8,
#                     padding_x=5,
#                     borderwidth=1,
#                     active=["#f1ffff", "#f1ffff"],
#                     inactive=["#f1ffff", "#f1ffff"],
#                     rounded=False,
#                     highlight_method='block',
#                     urgent_alert_method='block',
#                     urgent_border=["#F07178", "#F07178"],
#                     this_current_screen_border=["#f07178", "#f07178"],
#                     this_screen_border=["#5c5c5c", "#5c5c5c"],
#                     other_current_screen_border=["#0f101a", "#0f101a"],
#                     other_screen_border=["#0f101a", "#0f101a"],
#                     disable_drag=True
#                 ),
#                 widget.WindowName(),
#                 widget.CurrentLayoutIcon(
#                     background=["#F07178", "#F07178"],
#                     foreground=["#0f101a","#0f101a"],
#                     scale=0.65
#                 ),
#                 widget.CurrentLayout(
#                     background=["#F07178", "#F07178"],
#                     foreground=["#0f101a","#0f101a"]
#                 ),
#                 widget.TextBox(
#                     background=["#a151d3","#a151d3"],
#                     foreground=["#0f101a","#0f101a"],
#                     text=''
#                 ),
#                 widget.Clock(
#                     background=["#a151d3","#a151d3"],
#                     foreground=["#0f101a","#0f101a"],
#                     format='%d/%m/%Y - %H:%M '
#                 ),
#             ],
#             24,
#             opacity=0.9
#         ),
#     ),
# ]

# # Drag floating layouts.
# mouse = [
#     Drag([mod], "Button1", lazy.window.set_position_floating(),
#          start=lazy.window.get_position()),
#     Drag([mod], "Button3", lazy.window.set_size_floating(),
#          start=lazy.window.get_size()),
#     Click([mod], "Button2", lazy.window.bring_to_front())
# ]

# dgroups_key_binder = None
# dgroups_app_rules = []  # type: List
# follow_mouse_focus = True
# bring_front_click = False
# cursor_warp = False
# floating_layout = layout.Floating(float_rules=[
#     # Run the utility of `xprop` to see the wm class and name of an X client.
#     *layout.Floating.default_float_rules,
#     Match(wm_class='confirmreset'),  # gitk
#     Match(wm_class='makebranch'),  # gitk
#     Match(wm_class='maketag'),  # gitk
#     Match(wm_class='ssh-askpass'),  # ssh-askpass
#     Match(title='branchdialog'),  # gitk
#     Match(title='pinentry'),  # GPG key password entry
# ])
# auto_fullscreen = True
# focus_on_window_activation = "smart"
# reconfigure_screens = True

# # If things like steam games want to auto-minimize themselves when losing
# # focus, should we respect this or not?
# auto_minimize = True

# # XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# # string besides java UI toolkits; you can see several discussions on the
# # mailing lists, GitHub issues, and other WM documentation that suggest setting
# # this string if your java app doesn't work correctly. We may as well just lie
# # and say that we're a working one by default.
# #
# # We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# # java that happens to be on java's whitelist.
# wmname = "LG3D"
