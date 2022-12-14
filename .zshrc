# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi


#
# Executes commands at the start of an interactive session.
#
# Authors:
#   Sorin Ionescu <sorin.ionescu@gmail.com>
#
# Plugins
zstyle ':prezto:load' pmodule \
    'terminal' \
    'history' \
    'fast-syntax-highlighting' \
    'autosuggestions' \
    'spectrum' \
    'utility' \
    'completion' \
    'auto-notify' \
    'prompt' \
    

source .zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
source .zsh/zsh-auto-notify/auto-notify.plugin.zsh
source .zsh/fast-syntax-highlighting/fast-syntax-highlighting.plugin.zsh
source /usr/share/fzf/key-bindings.zsh

export FZF_CTRL_A_OPTS='--height 30 --multi --layout=reverse --preview "if file {} | grep -i 'text'; then 
  bat --color=always --style=grid --line-range :600 {}; fi"'

export PATH="/home/javigo07/.local/bin:$PATH"
export GIT_DISCOVERY_ACROSS_FILESYSTEM=1

# Source Prezto.
if [[ -s "${ZDOTDIR:-$HOME}/.zprezto/init.zsh" ]]; then
  source "${ZDOTDIR:-$HOME}/.zprezto/init.zsh"
fi

# Customize to your needs...
alias cat=bat 
alias progress="tail -f /var/log/emerge-fetch.log"
alias sudo=doas
alias "shutdown now"="loginctl poweroff"
alias reboot="loginctl reboot"
alias osu="WINEPREFIX=/home/javigo07/Games/osu /opt/wine-osu/bin/wine"
alias mkernel="doas make nconfig ;doas make -j13 ;doas make install ;doas make modules_install ;doas emerge -1 @module-rebuild ;doas grub-mkconfig -o /boot/grub/grub.cfg"

export EDITOR=nvim 

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
export YTFZF_EXTMENU='rofi -dmenu -fuzzy -width 1000'export YTFZF_ENABLE_FZF_DEFUALT_OPTS=0

# Autostart
[[ -e ~/.ssh/github ]] && {
  { eval `ssh-agent`; ssh-add -q ~/.ssh/github; } &>/dev/null
}
