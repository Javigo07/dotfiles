from libqtile import bar, widget, layout
from libqtile.config import Screen, Match
from .colors import colors
#from qtile_extras import widget as widgetEx 

layouts = [
    layout.Columns(margin = 5, num_columns=3, border_focus_stack=colors[5], margin_on_single=[6, 8, 6, 8]),
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
    Match(wm_class='Telegram', title='Media viewer'),
    Match(wm_class='leagueclientux.exe'),
    Match(wm_class='osu!.exe')
])

bgwidgets = colors[1]+'66'
bgbar = colors[0]+'80'


widget_defaults = dict(
    font='Iosevka Term Nerd Font Complete',
    fontsize=18,
    padding=-2, 
    foreground=bgwidgets,
)


extension_defaults = widget_defaults.copy()

Sep = widget.Sep(
        size_percent=100,
        background=bgwidgets)  

GroupBoxx = widget.GroupBox(
        background=bgwidgets,
        inactive=colors[0],
        this_current_screen_border=colors[3],
        this_screen_border=colors[0],
        rounded=True,
        other_screen_border='#240b0b',
        other_current_screen_border='#240b0b', 
        spacing=3, 
        borderwidth=2) 

screens = [
   Screen(
        #wallpaper="/home/javigo07/Pictures/Wallpapers/Wallpaper 24.png",
        #wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.TextBox(
                    text='',
                    fontsize=24,
                    background=bgbar,
                    foreground=bgwidgets,
                    padding=-2),
                widget.CurrentLayoutIcon(
                    background=bgwidgets),
                Sep,
                widget.CurrentLayout(
                    background=bgwidgets,
                    padding=0),
                widget.Prompt(),
                widget.TextBox(
                    text='',
                    fontsize=60,
                    background=bgbar,
                    foreground=bgwidgets,
                    padding=-12),  
                widget.Spacer(bar.STRETCH),
                widget.TextBox(text='',
                    fontsize=60,
                    background=bgbar,
                    foreground=bgwidgets,
                    padding=-12), 
                GroupBoxx,
                widget.TextBox(
                    text='',
                    fontsize=60,
                    background=bgbar,
                    foreground=bgwidgets,
                    padding=-12),
                widget.Spacer(
                    bar.STRETCH),
                #widget.Systray(background=bgbar), 
                widget.TextBox(
                    text='',
                    fontsize=60,
                    background=bgbar,
                    foreground=bgwidgets,
                    padding=-12),
                widget.Clock(
                    format='%H:%M:%S',
                    background=bgwidgets),
                widget.TextBox(text='',
                    fontsize=24,
                    background=bgbar,
                    foreground=bgwidgets,
                    padding=-2),
            ],
            28,
            background=bgbar,
            margin=[2, 10, 0, 10]
        ),
        bottom=bar.Bar(
           [  
               widget.TextBox(
                   text='',
                   fontsize=24,
                   background=bgbar,
                   foreground=bgwidgets,
                   padding=-2), 
               #widgetEx.ALSAWidget(background=bgwidgets),
               widget.TextBox(
                   text='',
                   fontsize=60,
                   background=bgbar,
                   foreground=bgwidgets,
                   padding=-12),  
               widget.Spacer(bar.STRETCH), 
               widget.TextBox(
                   text='',
                   fontsize=60,
                   background=bgbar,
                   foreground=bgwidgets,
                   padding=-10),
               widget.WindowName(
                   empty_group_string="None",
                   background=bgwidgets),
               widget.TextBox(text='',
                   fontsize=60,
                   background=bgbar,
                   foreground=bgwidgets,
                   padding=-15),
               widget.Spacer(bar.STRETCH),
               widget.TextBox(
                   text='',
                   fontsize=60,
                   background=bgbar,
                   foreground=bgwidgets,
                   padding=-12),  
               widget.QuickExit(
                   default_text='',
                   background=bgwidgets,
                   fontsize=10), 
               widget.TextBox(
                   text='',
                   fontsize=24,
                   background=bgbar,
                   foreground=bgwidgets,
                   padding=-2),
           ],
           28,
           background=bgbar,
           margin=[0, 100, 2, 100]
        ),
        right=bar.Bar(
            [
           #widget.Bluetooth(background=bgwidgets),
           widget.CPU(background=bgwidgets) ],
            28,
            background=bgbar,
            margin=[10, 2, 10, 0]
            )
    ),
Screen(
        #wallpaper_mode="fill",
        top=bar.Bar(
            [

                widget.TextBox(
                    text='',
                    fontsize=24,
                    background=bgbar,
                    foreground=bgwidgets,
                    padding=-2),
                widget.CurrentLayoutIcon(background=bgwidgets),
                Sep,
                widget.CurrentLayout(background=bgwidgets,
                    padding=0),
                widget.Prompt(),
                widget.TextBox(
                    text='',
                    fontsize=60,
                    background=bgbar,
                    foreground=bgwidgets,
                    padding=-12),  
                widget.Spacer(bar.STRETCH),
                widget.TextBox(
                    text='',
                    fontsize=60,
                    background=bgbar,
                    foreground=bgwidgets,
                    padding=-12), 
                GroupBoxx,
                widget.TextBox(
                    text='',
                    fontsize=60,
                    background=bgbar,
                    foreground=bgwidgets,
                    padding=-12),
                widget.Spacer(bar.STRETCH), 
                widget.TextBox(
                    text='',
                    fontsize=60,
                    background=bgbar,
                    foreground=bgwidgets,
                    padding=-12),
                widget.Clock(
                    format='%H:%M:%S', 
                    background=bgwidgets),
                widget.TextBox(
                    text='', 
                    fontsize=24, 
                    background=bgbar,
                    foreground=bgwidgets,
                    padding=-2),
           ],
            28,
            background=bgbar,
            foreground=bgwidgets,
            margin=[2, 10, 0, 10]
        ),
        bottom=bar.Bar(
           [  
               widget.TextBox(
                   text='',
                   fontsize=24,
                   background=bgbar,
                   foreground=bgwidgets,
                   padding=-2), 
               widget.PulseVolume(background=bgwidgets),
               widget.TextBox(
                   text='',
                   fontsize=60,
                   background=bgbar,
                   foreground=bgwidgets,
                   padding=-12),  
               widget.Spacer(bar.STRETCH), 
               widget.TextBox(
                   text='',
                   fontsize=60,
                   background=bgbar,
                   foreground=bgwidgets,
                   padding=-10),
               widget.WindowName(
                   empty_group_string="None",
                   background=bgwidgets),
               widget.TextBox(
                   text='',
                   fontsize=60,
                   background=bgbar,
                   foreground=bgwidgets,
                   padding=-15),
               widget.Spacer(bar.STRETCH),
               widget.TextBox(
                   text='',
                   fontsize=60,
                   background=bgbar,
                   foreground=bgwidgets,
                   padding=-12),
               widget.Mpris2(
                   background=bgwidgets), 
               widget.TextBox(
                   text='',
                   fontsize=24,
                   background=bgbar,
                   foreground=bgwidgets,
                   padding=-2),
              ],
           28,
           background=bgbar,
           margin=[0, 100, 2, 100]
        ),

        left=bar.Bar(
            [
           #widget.Bluetooth(background=bgwidgets),
           widget.CPU(background=bgwidgets) ],
            28,
            background=bgbar,
            margin=[10, 2, 10, 0]
            )
 ),
      

]
