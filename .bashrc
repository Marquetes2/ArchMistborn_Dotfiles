# ~/.bashrc
[[ $- != *i* ]] && return

alias ls='lsd'
alias cat='bat'
alias vim='nvim'

# Sets the terminal to be alacritty when starting tmux
if [ "$TMUX" ]
then
  if [[ "$TERM" != "alacritty" ]]
  then
    export TERM=alacritty
    bash
  fi
fi 
