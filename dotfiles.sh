#!/bin/bash

# Dotfiles folder location
dotfile="Desktop/Dotfiles/"
# Config file locations relative to the home directory
config=( ".bashrc" ".xprofile" )

# For each config file, a symbolic link is created
for value in "${config[@]}"
do
  ln -sf "$dotfile""$value" ~/"$value"
  echo ~/"$dotfile""$value" ~/"$value"
done
