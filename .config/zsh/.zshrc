#history
HISTSIZE=10000
SAVEHIST=10000
HISTFILE=~/.cache/zsh/history

#autocomplete
autoload -U compinit
zstyle ':completion:*' menu select
zmodload zsh/complist
compinit
_comp_options+=(globdots)

#zap
[ -f "${XDG_DATA_HOME:-$HOME/.local/share}/zap/zap.zsh" ] && source "${XDG_DATA_HOME:-$HOME/.local/share}/zap/zap.zsh"
plug "Aloxaf/fzf-tab"
plug "zsh-users/zsh-autosuggestions"
plug "zap-zsh/supercharge"
plug "zap-zsh/zap-prompt"
plug "zap-zsh/completions"
plug "zsh-users/zsh-syntax-highlighting"

#aliases
alias cat="batcat --color=always"
alias ls="eza --color=always --icons=always --long --git --no-filesize --no-permissions --no-time --no-user"

eval "$(zoxide init zsh)"
