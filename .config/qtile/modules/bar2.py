from libqtile import bar, layout
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration,BorderDecoration,PowerLineDecoration
from libqtile.config import Screen, Match
from .custom.colors import colors#,colors1
from .custom.widgets import GroupBox,Sep
from .custom import Expanding
from qtile_extras.widget import modify

decor = {
    "decorations": [],
    "padding": 10,
}
powerline = {
    "decorations": [
        PowerLineDecoration(path='rounded_right',
            use_widget_background=False)
    ]
}

bgwidgets = [colors[0]+'80']
bgbar = '00000040'
bglyphs = colors[0]+'00'
fglyphs = colors[1]+'40'
fgwidgets = ['#000000','#ff0000']

widget_defaults = dict(
    font='Iosevka Term Nerd Font Complete',
    fontsize=18,
    padding=None,
    foreground=fgwidgets,
    font_colour='#ff0000')


extension_defaults = widget_defaults.copy()



screen2= Screen(
        #wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.TextBox(
                    text='',
                    fontsize=24,
                    background=bgwidgets,
                    foreground=bglyphs,
                    padding=-2),
                widget.CurrentLayoutIcon(
                    background=bgwidgets,
                    scale=0.75),
                Sep,
                widget.Spacer(
                    length=4,
                    background=bgwidgets
                    ),
                widget.AGroupBox(
                    background=bgwidgets,
                    padding_x=2,
                    borderwidth=0),
                widget.Prompt(
                    background=bgwidgets),
                Sep,
                widget.GlobalMenu(
                    background=bgwidgets,
                    ),
                widget.TextBox(
                    text='',
                    fontsize=60,
                    background=bgwidgets,
                    foreground=bglyphs,
                    padding=-12),  
                widget.Spacer(bar.STRETCH),
                widget.TextBox(text='',
                    fontsize=60,
                    background=bgwidgets,
                    foreground=bglyphs, 
                    padding=-12),
                GroupBox(),
                widget.TextBox(
                    text='',
                    fontsize=60,
                    background=bgwidgets,
                    foreground=bglyphs,  
                    padding=-12),
                widget.Spacer(bar.STRETCH), 
                widget.TextBox(
                    text='',
                    fontsize=60,
                    background=bgwidgets,
                    foreground=bglyphs,  
                    padding=-12),
                 widget.Spacer(bar.STRETCH),
                 widget.WindowName(
                   empty_group_string="None",
                   background=bgwidgets),
                 widget.Spacer(bar.STRETCH),
                 Expanding.ExpandingClock(
                    format="%H:%M:%S",
                    background=bgwidgets
                    ),
                widget.TextBox(
                    text='', 
                    fontsize=24, 
                    background=bgwidgets,
                    foreground=bglyphs,  
                    padding=-2),
           ],
            28,
            background=bgbar,
            foreground=bgwidgets,
            margin=[2, 10, 0, 10]
        )
        )
 
