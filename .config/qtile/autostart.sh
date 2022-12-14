#!/bin/bash

sleep 0.2s &

~/.local/bin/wal -R &
pipewire &
pipewire-pulse &
openrgb --startminimized &
xcalib /home/javigo07/Samsung.icc &
picom &
ferdium &
flashfocus &
keepassxc &
wired &
sleep 0.2s
pipewire-media-session &
notify-send "WM started" &

