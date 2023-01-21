from libqtile.config import Key
from libqtile.lazy import lazy

from .settings import mod, terminal
from .traverse import left,right
mod = "mod4"

@lazy.function
def test(qtile):
    lazy.window.toggle_fullscreen(),
    #lazy.next_layout()

keys = [
    # Switch between windows
    Key([mod], "a", lazy.function(left), desc="Move focus to left"),
    Key([mod], "i", lazy.function(right), desc="Move focus to right"),
    Key([mod], "e", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "o", lazy.layout.up(), desc="Move focus up"),
    Key([mod, "shift"], "space", lazy.window.toggle_floating(), desc="Focus floatin"),
   
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "a", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "i", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "e", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "o", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "a", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "i", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "e", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "o", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "d", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.reload_config(), desc="Restart Qtile"),
    Key(["mod1"], "p", lazy.spawn("flameshot gui"), desc="Restart Qtile"),
    Key([mod, "control"], "apostrophe", lazy.shutdown(), desc="Shutdown Qtile"),
    #Key([mod], "r", lazy.spawncmd(),
     #   desc="Spawn a command using a prompt widget"),
    Key([mod], "space", lazy.spawn("rofi -show drun"),
        desc="Show rofi -show drun uwur window"),
    Key([mod], "t", lazy.window.toggle_fullscreen(),
        desc="Fullscreen"),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"))
]
