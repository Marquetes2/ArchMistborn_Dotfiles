# MarcosRodrui
# Based on the Configuration of Antonio Sarosi

# Qtile keybindings

from libqtile.config import Key, KeyChord
from libqtile.command import lazy
from .power_menu import show_power_menu

mod = "mod4"

@lazy.function
def float_to_front(qtile):
    for window in qtile.currentGroup.windows:
        if window.floating:
            window.cmd_bring_to_front()


keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),

    # Colums Layout - Grow windows
    ([mod, "mod1"], "h", lazy.layout.grow_left().when(when_floating=False)),
    ([mod, "mod1"], "l", lazy.layout.grow_right().when(when_floating=False)),
    ([mod, "mod1"], "j", lazy.layout.grow_down().when(when_floating=False)),
    ([mod, "mod1"], "k", lazy.layout.grow_up().when(when_floating=False)),
    ([mod], "n", lazy.layout.normalize()),

    # Move windows up or down
    ([mod, "shift"], "h", lazy.layout.shuffle_left()),
    ([mod, "shift"], "l", lazy.layout.shuffle_right()),
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),

    # Kill window
    ([mod], "w", lazy.window.kill()),

    # Manage bar
    ([mod], "b", lazy.spawn("qtile shell -c 'hide_show_bar()'")),

    # Power options
    ([mod], "Escape", lazy.spawn("/home/marcosrodrui/.config/rofi/powermenu/type-5/powermenu.sh")),
    ([mod, "shift"], "Escape", lazy.function(show_power_menu)),

    # Switch focus of monitors
    ([mod, "control"], "l", lazy.to_screen(0)),
    ([mod, "control"], "h", lazy.to_screen(1)),
    # ([mod, "control"], "l", lazy.to_screen(1)),
    # ([mod, "control"], "h", lazy.to_screen(0)),
    #([mod, "control"], "l", lazy.next_screen()),
    #([mod, "control"], "h", lazy.prev_screen()),

    # Floating and Fullscreen
    ([mod], "s", lazy.window.enable_floating()),
    ([mod], "t", lazy.window.disable_floating()),
    ([mod], "f", lazy.window.toggle_fullscreen()),

    ([mod, "shift", "mod1"], "h", lazy.window.resize_floating(-50, 0)),
    ([mod, "shift", "mod1"], "l", lazy.window.resize_floating(50, 0)),
    ([mod, "shift", "mod1"], "j", lazy.window.resize_floating(0, 50)),
    ([mod, "shift", "mod1"], "k", lazy.window.resize_floating(0, -50)),

    ([mod, "mod1", "control"], "h", lazy.window.move_floating(-50, 0)),
    ([mod, "mod1", "control"], "l", lazy.window.move_floating(50, 0)),
    ([mod, "mod1", "control"], "j", lazy.window.move_floating(0, 50)),
    ([mod, "mod1", "control"], "k", lazy.window.move_floating(0, -50)),

    ([mod], "p", lazy.function(float_to_front)),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),
    ([mod, "control"], "q", lazy.shutdown()),
    ([mod], "r", lazy.spawncmd()),

    # ------------ App Configs ------------

    # Menu
    ([mod], "m", lazy.spawn("/home/marcosrodrui/.config/rofi/launchers/type-7/launcher.sh")),

    # Window Nav
    ([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Gaming Hub
    ([mod], "g", lazy.spawn("rofi -modi games -show games -theme games")),

    # Browser
    ([mod, "shift"], "f", lazy.spawn("firefox")),

    # File Explorer
    ([mod], "e", lazy.spawn("thunar")),

    # Terminal
    ([mod], "Return", lazy.spawn("alacritty")),
    ([mod, "shift"], "Return", lazy.spawn("cool-retro-term")),

    # Redshift
    ([mod], "p", lazy.spawn("redshift -P -O 4200")),
    ([mod, "shift"], "p", lazy.spawn("redshift -x")),

    # Screenshot
    ([mod], "Print", lazy.spawn("bash -c 'scrot ~/Desktop/Capturas/%Y-%m-%d-%H:%M:%S.png'")),
    ([mod, "mod1"], "Print", lazy.spawn("bash -c 'scrot /tmp/copy_to_clipboard.png -s && \\cat /tmp/copy_to_clipboard.png | xclip -selection clipboard -target image/png -i && rm /tmp/copy_to_clipboard.png'")),
    ([mod, "shift"], "Print", lazy.spawn("bash -c '")),

    # Shutdown
    ([mod, "mod1"], "F4", lazy.spawn("neoshutdown")),

    # ------------ Hardware Configs ------------

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]
