# history
HISTSIZE=10000
SAVEHIST=10000
HISTDUP=erase
HISTFILE=~/.cache/zsh/history

# zinit
ZINIT_HOME="${XDG_DATA_HOME:-${HOME}/.local/share}/zinit/zinit.git"
[ ! -d $ZINIT_HOME ] && mkdir -p "$(dirname $ZINIT_HOME)"
[ ! -d $ZINIT_HOME/.git ] && git clone https://github.com/zdharma-continuum/zinit.git "$ZINIT_HOME"
source "${ZINIT_HOME}/zinit.zsh"

zinit light zsh-users/zsh-syntax-highlighting
zinit light zsh-users/zsh-completions
zinit light zsh-users/zsh-autosuggestions
zinit light zap-zsh/zap-prompt
zinit light Aloxaf/fzf-tab

# autocomplete
autoload -Uz compinit
compinit
_comp_options+=(globdots)

# aliases
alias vim="nvim"
alias cat="batcat --color=always"
alias ls="eza --color=always --icons=always --long --git --no-filesize --no-permissions --no-time --no-user"
alias cd..="cd .."
alias cd...="cd ../.."
alias cd....="cd ../../.."
alias cd.....="cd ../../../.."
alias cd......="cd ../../../../.."

# evaluate add-ons
#eval "$(fzf --zsh)"
eval "$(zoxide init --cmd cd zsh)"

# fastfetch
COUNTER=$(pgrep -f zsh | wc -l);
if [ $COUNTER -eq 2 ]; then
    fastfetch
fi
