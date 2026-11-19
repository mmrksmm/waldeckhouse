## Game settings (name, version, transitions, sound)
## Based on the standard Ren'Py template: https://www.renpy.org/doc/html/gui.html
define config.name = _("Waldeck House")
define gui.show_name = True
default preferences.transitions = 2
define config.allow_skipping = False
define gui.about = _p("""
{b}Waldeck House{/b}

A visual novel in seven days.

Script, story, code: mmrksmm

Illustrations and interface: created with AI and refined by hand

{b}Music{/b}

"Greats of Far", "fin", "Jazzy Shop" by Tim Reichert{p}
{a=https://tim-reichert.com}tim-reichert.com{/a}{p}
Licensed under {a=https://creativecommons.org/licenses/by-nc/4.0/}CC BY-NC 4.0{/a}

"To You": Composer - 3N{p}
{a=https://ka-music.itch.io/old-radio-music-pack}Old Radio Music Pack{/a}

Fonts: PT Serif, Playfair Display, Cormorant Garamond, Miama Nueva (SIL Open Font License 1.1)

Engine: Ren'Py

A game about a warmth that is hard to tell from a trap.
""")

define build.name = "cs50"

define config.has_sound = True
define config.has_music = True
define config.has_voice = True

## переходы между экранами заданы в конце screens

define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

default preferences.text_cps = 30
default preferences.afm_time = 15

define config.save_directory = "cs50-1792930708"
define config.window_icon = "gui/window_icon.png"

init python:
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    build.documentation('*.html')
    build.documentation('*.txt')