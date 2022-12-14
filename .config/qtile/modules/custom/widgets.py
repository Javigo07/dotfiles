from libqtile import bar, layout
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration,BorderDecoration,PowerLineDecoration
from .colors import colors
from qtile_extras.widget import modify
from . import Groupbox

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

Sep = widget.Sep(
        size_percent=100,
        background=bgwidgets,
        foreground=fgwidgets,
        linewidth=1,
        padding=4)  

def GroupBox():
    return Groupbox.GroupBox(
            rainbow=True,
            invert= True, 
            background=bgwidgets,
            foreground=fgwidgets,
            inactive=colors[0],
            this_current_screen_border=[colors[4],colors[3]],
            this_screen_border=[colors[3],colors[1]],
            rounded=True,
            other_screen_border=[colors[3],colors[1]],
            other_current_screen_border=[colors[1],colors[3]],
            spacing=3,
            borderwidth=3,
            highlight_method='line',
            highlight_color=[colors[1]+'ff',colors[0]+'4D'], 
            )


