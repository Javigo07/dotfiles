from modules import *
from typing import List
from libqtile import hook

import os
import subprocess

@hook.subscribe.startup_once
def startup(): 
    subprocess.Popen(['.config/qtile/autostart.sh'])
 
dgroups_key_binder = None
dgroups_app_rules = [] # type: List 
follow_mouse_focus = True
cursor_warp=True
bring_front_click = True
auto_fullscreen = True
auto_minimize = False
focus_on_window_activation = "urgent"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "Qtile"
