#!/bin/bash

# Dotfiles folder location
dotfile="Desktop/Dotfiles/"
# Config file locations relative to the home directory
config=( ".bashrc" ".xprofile" ".face" ".config/alacritty" ".config/betterlockscreen" ".config/nvim" ".config/picom" ".config/qtile" ".config/ranger" ".config/rofi" ".config/Thunar")

# For each config file, a symbolic link is created
for value in "${config[@]}"
do
  rm -rf ~/"$value"
  ln -sf ~/"$dotfile""$value" ~/"$value"
  echo -e "Created link ~/$dotfile$value \t to ~/$value"
done
