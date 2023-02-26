from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal
import os

wallpaper_path = '~/Pictures/sunflowers.jpg'

screens = [
    Screen(
        top=bar.Bar(
            [   widget.Sep(padding=3, linewidth=0, background="#2f343f"),
                widget.Image(filename='~/.config/qtile/eos-c.png', margin=3, background="#2f343f", mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show combi")}),
                widget.Sep(padding=4, linewidth=0, background="#2f343f"), 
                widget.GroupBox(
                                highlight_method='line',
                                this_screen_border="#5294e2",
                                this_current_screen_border="#5294e2",
                                active="#ffffff",
                                inactive="#848e96",
                                background="#2f343f"),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#2f343f'
                       ),    
                widget.Prompt(),
                widget.Spacer(length=5),
             widget.WindowName(foreground='#ebdbb2',fmt='{}'),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                #widget.CurrentLayoutIcon(scale=0.75),
                widget.CheckUpdates(
                    update_interval=1800,
                    distro="Arch_yay",
                    display_format=" {updates} Updates ",
                    foreground="#ffffff",
                    mouse_callbacks={
                        'Button1':
                        lambda: qtile.cmd_spawn(terminal + ' -e yay -Syu')
                    },
                    background="#2f343f"),
                widget.Sep(),
                widget.CurrentLayout(),
                widget.Backlight(
                    backlight_name = "intel_backlight",
                    fmt = "",
                    padding = 0,
                    margin = 0,
                ),
                widget.KeyboardLayout(
                    background = '2f343f',
                    configured_keyboards = ["latam","us"],
                    display_map = {'latam':'LA', 'us':'US'},
                    fmt = ' kbmap: {} ',
                ),
                widget.Systray(icon_size = 20),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#2f343f'
                       ), 
                volume,
                widget.TextBox(                                                                    
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#2f343f',
                       ),   
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#2f343f'
                       ),    
                widget.Clock(
                        #format=' %Y-%m-%d %a %I:%M %p',
                        format=" \uf073  %a %d, %b. |  %H:%M:%S ",
                        background="#2f343f",
                        foreground='#ebdbb2'),
                widget.TextBox(                                                
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#2f343f',
                       ),   
                widget.Battery(
                    format = ' {percent:2.0%} ',
                    background = '404552',
                    low_percentage = 0.2,
                    low_background = 'FFE15D',
                    low_foreground = '000000',
                ),
                    widget.TextBox(
                    text='  ',
                    mouse_callbacks= {
                        'Button1':
                        lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))
                    },
                    foreground='#e39378'
                )
                
            ],
            24,  # height in px
            background="#404552",  # background color
        ),
        wallpaper=wallpaper_path,
        wallpaper_mode="fill",
    ),
    Screen(
        wallpaper=wallpaper_path,
        wallpaper_mode="fill",
    ),
]
