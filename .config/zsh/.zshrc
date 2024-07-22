# Zinit
ZINIT_HOME="${XDG_DATA_HOME:-${HOME}/.local/share}/zinit/zinit.git"
[ ! -d $ZINIT_HOME ] && mkdir -p "$(dirname $ZINIT_HOME)"
[ ! -d $ZINIT_HOME/.git ] && git clone https://github.com/zdharma-continuum/zinit.git "$ZINIT_HOME"
source "${ZINIT_HOME}/zinit.zsh"

zinit light zsh-users/zsh-syntax-highlighting
zinit light zsh-users/zsh-completions
zinit light zsh-users/zsh-autosuggestions
zinit light Aloxaf/fzf-tab

# Autocomplete
autoload -Uz compinit
compinit -d ~/.local/share/zsh/.zcompdump

# History
HISTSIZE=10000
HISTFILE="$HOME/.local/share/zsh/.zsh_history"
SAVEHIST=$HISTSIZE
HISTDUP=erase
setopt appendhistory
setopt sharehistory
setopt hist_ignore_space
setopt hist_ignore_all_dups
setopt hist_save_no_dups
setopt hist_ignore_dups
setopt hist_find_no_dups

# Aliases
alias vim="nvim"
alias cat="batcat --color=always"
alias ls="eza --color=always --icons=always --long --git --no-filesize --no-permissions --no-time --no-user"
alias cd..="cd .."
alias cd...="cd ../.."
alias cd....="cd ../../.."
alias cd.....="cd ../../../.."
alias cd......="cd ../../../../.."

# Evaluate add-ons
#eval "$(fzf --zsh)"
eval "$(zoxide init --cmd cd zsh)"
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
eval "$(oh-my-posh init zsh --config ~/.config/ohmyposh/config.toml)"

# Run only on first command
[[ "$(pidof zsh)" == *' '* ]] || fastfetch
