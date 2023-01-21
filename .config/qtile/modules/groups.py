from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy
from libqtile import layout
from .keys import keys
from .settings import mod
from .custom.colors import colors

layouts = [
    #layout.MonadTall(margin=[0,0,20,20], border=colors[1]),
    layout.Columns(margin = [0,0,20,20], num_columns=2, border=colors[1], border_focus_stack=colors[5], margin_on_single=[6, 8, 6, 8]),
    layout.Max(margin = 8),
]


floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='zoom'),
    Match(title='Media viewer'),
    Match(wm_class='leagueclientux.exe'),
    Match(wm_class='osu!.exe')
])


group_names = [("",""), ("二","max"), ("三",""),
        ("四",""), ("五",""), ("六",""),
        ("七",""), ("八", "max")]
teclas = ["w","l","r"]


def match(name):
    if name == group_names[1][0]:
        return [Match(wm_class='Telegram')]
    elif name == group_names[1][0]:
        return [Match(wm_class='Ferdium')]
    elif name == group_names[4][0]:
        return [Match(wm_class='qbittorrent')]
    return [] 

groups = [Group(name, layout=layout, matches=match(name)) for name, layout in group_names]

for i, name in enumerate(group_names):
#  if (i+1) <= 5:
    keys.append(Key([mod], str(i+1), lazy.group[name[0]].toscreen(toggle=True)))
    keys.append(Key([mod, "shift"], str(i+1), lazy.window.togroup(name[0])))
 # else:
  #  keys.append(Key([mod], str(teclas[i-5]), lazy.group[name[0]].toscreen(toggle=True))) 
   # keys.append(Key([mod, "shift"], str(teclas[i-5]), lazy.window.togroup(name[0])))
    
