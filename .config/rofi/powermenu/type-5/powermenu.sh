#!/usr/bin/env bash

## Author : Aditya Shakya (adi1090x)
## Github : @adi1090x
#
## Rofi   : Power Menu
#
## Available Styles
#
## style-1   style-2   style-3   style-4   style-5

# Current Theme
dir="$HOME/.config/rofi/powermenu/type-5"
theme='style-4'

# CMDs
lastlogin="`last $USER | head -n1 | tr -s ' ' | cut -d' ' -f5,6,7`"
uptime="`uptime -p | sed -e 's/up //g'`"
host="Mistborn"

# Options
yes=''
no=''

# Rofi CMD
rofi_cmd() {
	rofi -dmenu \
		-mesg " Last Login: $lastlogin |  Uptime: $uptime" \
		-theme ${dir}/${theme}.rasi
}

# Pass variables to rofi dmenu
run_rofi() {
	echo -e "Lock\0icon\x1f<span color='#4e5165' font='Mistborn'>s</span>\n" \
	"Reboot\0icon\x1f<span color='#d26939' font='Mistborn'>a</span>\n" \
	"Shutdown\0icon\x1f<span color='#c33027' font='Mistborn'>@</span>\n" \
	"Log out\0icon\x1f<span color='#edb54b' font='Mistborn'>v</span>\n" \
	"Suspend\0icon\x1f<span color='#888ba5' font='Mistborn'>f</span>" \
	| rofi_cmd
}

# Execute Command
run_cmd() {
	if [[ $1 == '--shutdown' ]]; then
		systemctl poweroff
	elif [[ $1 == '--reboot' ]]; then
		systemctl reboot
	elif [[ $1 == '--suspend' ]]; then
		betterlockscreen --suspend
	elif [[ $1 == '--logout' ]]; then
		if [[ "$DESKTOP_SESSION" == 'openbox' ]]; then
			openbox --exit
		elif [[ "$DESKTOP_SESSION" == 'bspwm' ]]; then
			bspc quit
		elif [[ "$DESKTOP_SESSION" == 'i3' ]]; then
			i3-msg exit
		elif [[ "$DESKTOP_SESSION" == 'plasma' ]]; then
			qdbus org.kde.ksmserver /KSMServer logout 0 0 0
		elif [[ "$DESKTOP_SESSION" == 'qtile' ]]; then
			qtile cmd-obj -o cmd -f shutdown
		fi
	fi
}

# Actions
chosen="$(run_rofi)"
echo "Probando: ${chosen}" >> ~/result.txt
case ${chosen} in
    " Shutdown")
		run_cmd --shutdown
        ;;
    " Reboot")
		run_cmd --reboot
        ;;
    "Lock")
		if [[ -x '/usr/bin/betterlockscreen' ]]; then
			betterlockscreen -l
		elif [[ -x '/usr/bin/i3lock' ]]; then
			i3lock
		fi
        ;;
    " Suspend")
		run_cmd --suspend
        ;;
    " Log out")
		run_cmd --logout
        ;;
esac
