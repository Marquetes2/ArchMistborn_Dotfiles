# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Aux function
snapclient_alias() {
  if [ $(ps -aux | grep snapclient | wc -l) -eq 1 ]; then snapclient --host 192.168.1.101 > /dev/null &; disown ; fi; ncmpcpp -c ~/.config/ncmpcpp/config.server
}

# Bash Configuration
[[ $- != *i* ]] && return

alias ls='lsd'
alias cat='bat'
alias vim='nvim'
alias vimgodot='nvim --listen ./godothost'
alias ytaudio="yt-dlp -f 'ba' -x --audio-quality 0 --no-playlist"
alias ytplaylist="yt-dlp -f 'ba' -x --audio-quality 0"
alias zoro_bind="sshfs zoro@192.168.1.101:/home/zoro/ ~/zoro"
alias zoro_unbind="fusermount3 -u ~/zoro"
alias one_bind="sshfs zoro@192.168.1.101:/ ~/OneServer"
alias one_unbind="fusermount3 -u ~/OneServer"
alias zoro_connect="ssh zoro@192.168.1.101"
alias one_music="snapclient_alias"
alias one_music_stop="killall snapclient"
alias ncmpcpp="ncmpcpp -c ~/.config/ncmpcpp/config.local"
alias notes='cd ~/Notes && vim -c "Neorg workspace notes"'

export EDITOR='nvim'

# TMUX
export TERM=alacritty
#[ -z "$TMUX"  ] && { tmux attach || exec tmux new-session && exit;}

# History in cache directory
HISTFILE=~/.cache/zsh/history
HISTSIZE=1000
SAVEHIST=1000

# Auto Complition
autoload -U compinit
zstyle ':completion:*' menu select
zmodload zsh/complist
setopt extendedglob
_comp_options+=(globdots)

# Lines configured by zsh-newuser-install
unsetopt beep
bindkey -v

# Plugins
source ~/.config/zsh/plugins/powerlevel10k/powerlevel10k.zsh-theme
source ~/.config/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source ~/.config/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source ~/.config/zsh/plugins/zsh-completions/zsh-completions.plugin.zsh

## Autosuggest
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE="fg=13"

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
