# ~/.bashrc
[[ $- != *i* ]] && return

alias ls='lsd'
alias cat='bat'
alias vim='nvim'

export EDITOR='nvim'

# TMUX
export TERM=alacritty
[ -z "$TMUX"  ] && { tmux attach || exec tmux new-session && exit;}
