xrandr --output DP-1 --off --output DP-2 --off --output DP-3 --off --output HDMI-1 --mode 1920x1080 --pos 1920x0 --rotate normal --output DVI-D-1 --primary --mode 1920x1080 --pos 0x0 --rotate normal
[[ -f ~/.Xresources ]] && xrdb -merge -I$HOME ~/.Xresources
ln -s ~/.config/keepassxc/KeepassCache/keepassxc ~/.cache/keepassxc
ln -s ~/.config/wal/walcache ~/.cache/wal
ln -s ~/.config/wal/walcache/colors-rofi-dark.rasi ~/.config/rofi/config-wal.rasi
qtile start -b x11  -c /home/javigo07/.config/qtile/config.py

