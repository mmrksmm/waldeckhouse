## Animations (ATL transforms)
## ATL: https://www.renpy.org/doc/html/atl.html
## Background tinting (matrixcolor): https://www.renpy.org/doc/html/matrixcolor.html
transform house_tint(m):
    matrixcolor m

transform cg_tint(m):
    matrixcolor m

transform locked_icon:
    matrixcolor SaturationMatrix(0.0) * BrightnessMatrix(-0.4)

transform lizetta_pos:
    xalign 0.14
    yalign 1.0

# фрау фон Вальдек слегка "дышит"
transform waldeck_idle:
    xalign 0.86
    yalign 1.0
    block:
        ease 2.6 yoffset -10
        ease 2.6 yoffset 0
        repeat

# выходит в кадр справа
transform waldeck_in:
    xalign 0.86
    yalign 1.0
    alpha 0.0
    xoffset 105
    parallel:
        easein 0.8 alpha 1.0
    parallel:
        easein 0.8 xoffset 0
    waldeck_idle

# пульс, когда страшно: сила зависит от house.dread
transform heartbeat(a):
    alpha 0.0
    block:
        ease 0.35 alpha a
        ease 0.45 alpha (a * 0.4)
        ease 0.35 alpha a
        ease 1.2 alpha 0.0
        pause 1.8
        repeat

# тёплое свечение: сила зависит от house.warmth
transform glow(a):
    alpha 0.0
    block:
        ease 3.5 alpha a
        ease 3.5 alpha 0.0
        repeat

transform card_in:
    xalign 0.5
    yalign 0.5
    alpha 0.0
    linear 1.2 alpha 1.0

transform black_in:
    alpha 0.0
    ease 0.8 alpha 1.0

# экраны выплывают снизу и плавно исчезают
transform pop_in:
    on show:
        alpha 0.0
        yoffset 36
        parallel:
            ease 0.45 alpha 1.0
        parallel:
            ease 0.45 yoffset 0
    on replace:
        alpha 0.0
        yoffset 36
        parallel:
            ease 0.45 alpha 1.0
        parallel:
            ease 0.45 yoffset 0
    on hide:
        ease 0.3 alpha 0.0
    on replaced:
        ease 0.3 alpha 0.0

# затемнение под экранами
transform fade_in:
    on show:
        alpha 0.0
        ease 0.45 alpha 1.0
    on replace:
        alpha 0.0
        ease 0.45 alpha 1.0
    on hide:
        ease 0.3 alpha 0.0
    on replaced:
        ease 0.3 alpha 0.0

# окна игрового меню
transform menu_fade:
    on show:
        alpha 0.0
        ease 0.35 alpha 1.0
    on replace:
        alpha 0.0
        ease 0.35 alpha 1.0
    on hide:
        ease 0.25 alpha 0.0
    on replaced:
        ease 0.25 alpha 0.0

# дорога в карете: фон покачивается и слегка трясётся
transform carriage_ride:
    zoom 1.08
    xalign 0.5
    yalign 0.5
    parallel:
        block:
            ease 3.6 xoffset 33
            ease 3.6 xoffset -33
            repeat
    parallel:
        block:
            pause 1.4
            linear 0.06 yoffset 9
            linear 0.12 yoffset 0
            pause 2.2
            linear 0.05 yoffset -7
            linear 0.10 yoffset 0
            pause 0.9
            linear 0.05 yoffset 6
            linear 0.09 yoffset 0
            pause 2.6
            repeat

# закрытие дневника и чемодана: плавно исчезают
transform fade_out:
    alpha 1.0
    ease 0.35 alpha 0.0

# начало игры: главное меню плавно уходит в чёрный, потом запускается игра
screen start_fade():
    zorder 500
    modal True
    add Solid("#000000") at black_in
    timer 0.9 action [Hide("start_fade"), Start()]

# выход в главное меню через затемнение
screen exit_fade():
    zorder 500
    modal True
    add Solid("#000000") at black_in
    timer 0.9 action [Hide("exit_fade"), MainMenu(confirm=False)]

# мини-игры появляются и исчезают плавно (on hide работает и для call screen)
transform screen_fade:
    on show:
        alpha 0.0
        linear 0.6 alpha 1.0
    on hide:
        linear 0.9 alpha 0.0
