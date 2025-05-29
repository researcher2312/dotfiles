use std "path add"
path add "/home/linuxbrew/.linuxbrew/bin"

zoxide init nushell --cmd cd | save -f ~/.zoxide.nu
oh-my-posh init nu --config ~/.config/ohmyposh/config.toml
