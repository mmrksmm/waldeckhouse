## Screens: diary, suitcase (achievements), gallery, darning mini-game, timed choice
##
## Sources:
## drag and drop (darning)   https://www.renpy.org/doc/html/drag_drop.html
## achievements              https://www.renpy.org/doc/html/achievement.html
## timed choice: pattern from the Lemma Soft forums
##   https://lemmasoft.renai.us/forums/viewtopic.php?p=379059

init python:

    # координаты точек штопки и начальное место иглы (экран 1920x1080)
    DARN_POINTS = [(510, 498), (750, 549), (930, 467), (1110, 553), (1290, 456), (1440, 499)]
    NEEDLE_START = (777, 537)

    # вызывается, когда иглу отпустили: попали в нужную точку или нет
    def darn_dragged(drags, drop):
        if drop is None:
            return
        point = int(drop.drag_name[1:])
        if point == store.darn_next:
            store.darn_next += 1
            renpy.restart_interaction()
        else:
            drags[0].snap(NEEDLE_START[0], NEEDLE_START[1], 0.2)

    # на время штопки курсор становится точкой
    def darning_cursor(on):
        if on:
            config.mouse["screen"] = [("images/ui/dot_cursor.png", 12, 12)]
        else:
            config.mouse.pop("screen", None)


## ---------- экраны ----------

# дневник Ирэн: чем больше страха было при выборе, тем темнее запись
screen diary():
    tag menu
    modal True
    zorder 120
    default closing = False
    add Solid("#000000cc") at (fade_out if closing else fade_in)
    key "game_menu" action SetScreenVariable("closing", True)
    frame at (fade_out if closing else pop_in):
        background "images/ui/diary_bg.png"
        xalign 0.5
        yalign 0.5
        xsize 1440
        ysize 930
        padding (60, 45)
        vbox:
            spacing 21
            text _("Irene's Diary") font gui.heading_font size 60 color "#3b2a1a"
            viewport:
                scrollbars "vertical"
                mousewheel True
                ysize 675
                vbox:
                    spacing 27
                    for key in MEMORIES:
                        if key in house.mem:
                            $ title, texts = MEMORIES[key]
                            $ ink = min(house.mem_dread.get(key, 0), 8)
                            vbox:
                                spacing 12
                                text __(title) font gui.diary_font size 39 color "#6b4a2a"
                                text (__(texts[house.mem[key]]).replace("{w}", " ")) font gui.diary_font size 36 color ("#2a1c10" if ink < 5 else "#1d120a") outlines [(1, "#2a1c10%02x" % min(150, ink * 18), 0, 0)]
                    if not house.mem:
                        text _("Nothing yet.") color "#6b4a2a"
            hbox:
                xalign 1.0
                spacing 45
                textbutton _("Suitcase") action ShowMenu("achievements") text_color "#3b2a1a" text_hover_color "#a33"
                textbutton _("Close") action SetScreenVariable("closing", True) text_color "#3b2a1a" text_hover_color "#a33"
    if closing:
        timer 0.35 action Return()

screen diary_button():
    zorder 90
    if house.mem or persistent.loops:
        textbutton _("Diary") action ShowMenu("diary") align (0.99, 0.01) text_size 33
        key "K_d" action ShowMenu("diary")

# выбор с таймером: когда время выходит, возвращается значение по умолчанию
screen timed_choice(items, seconds, default_value):
    modal True
    zorder 100
    timer seconds action Return(default_value)
    vbox at pop_in:
        style_prefix "choice"
        xalign 0.5
        yalign 0.45
        spacing 27
        for caption, value in items:
            textbutton __(caption) action Return(value) xalign 0.5
        bar value AnimatedValue(old_value=1.0, value=0.0, range=1.0, delay=seconds) xsize 750 ysize 18 xalign 0.5

# штопка: иглу нужно перетащить по точкам по порядку, можно пропустить
# картинки лежат в images/ui/ (darn_bg, darn_needle, darn_point, darn_point_done, darn_stitch_1 ... darn_stitch_5)
screen darning(points):
    modal True
    zorder 100
    fixed at screen_fade:
        add "images/ui/darn_bg.png"

        # уже сделанные стежки
        for k in range(1, darn_next):
            add ("images/ui/darn_stitch_%d.png" % k)

        draggroup:
            for n in range(len(points)):
                $ px, py = points[n]
                drag:
                    drag_name ("p%d" % n)
                    droppable True
                    draggable False
                    xpos (px - 48)
                    ypos (py - 48)
                    add ("images/ui/darn_point_done.png" if n < darn_next else "images/ui/darn_point.png")
            drag:
                drag_name "needle"
                draggable True
                droppable False
                drag_raise True
                xpos NEEDLE_START[0]
                ypos NEEDLE_START[1]
                dragged darn_dragged
                add "images/ui/darn_needle.png"

        if darn_next >= len(points):
            timer 1.1 action Return(True)

        textbutton _("Skip") action Return(False) align (0.99, 0.01) text_color "#d9a3b8" text_hover_color "#fff1f6"

# пульс (страх) или свечение (тепло) поверх сцены
screen mood():
    zorder -5
    if house.dread >= 4 and house.lean != "warm":
        add Solid("#000000") at heartbeat(min(0.03 + 0.008 * house.dread, 0.12))
    elif house.warmth >= 4 and house.lean != "cold":
        add Solid("#ff9fbf") at glow(min(0.02 + 0.008 * house.warmth, 0.10))

screen cg_gallery():
    tag menu
    use game_menu(_("Gallery")):
        vbox:
            spacing 16
            text (__("Unlocked: %d / %d") % (len(persistent.cg_seen), len(CG_LIST))) size 28
            vpgrid:
                cols 3
                spacing 24
                ysize 640
                mousewheel True
                scrollbars "vertical"
                for name, title in CG_LIST:
                    if name in persistent.cg_seen:
                        button:
                            action Show("cg_view", img=name)
                            hover_background Solid("#f2b6cb33")
                            padding (6, 6)
                            vbox:
                                add Transform(name, zoom=0.2)
                                text __(title) size 22 font gui.interface_text_font
                    else:
                        frame:
                            background Solid("#1c1218")
                            xysize (396, 258)
                            text "???" align (0.5, 0.5)

# просмотр CG на весь экран, закрывается кликом
screen cg_view(img):
    modal True
    zorder 200
    add Solid("#000000")
    add img
    button:
        xfill True
        yfill True
        action Hide("cg_view")

# достижения ("чемодан")
screen achievements():
    tag menu
    modal True
    zorder 120
    default closing = False
    add Solid("#000000cc") at (fade_out if closing else fade_in)
    key "game_menu" action SetScreenVariable("closing", True)
    frame at (fade_out if closing else pop_in):
        background "images/ui/ach_bg.png"
        xalign 0.5
        yalign 0.5
        xsize 1440
        ysize 960
        padding (60, 37)
        vbox:
            spacing 21
            yoffset 30
            text "Suitcase" font gui.heading_font size 60 color "#f2b6cb"
            $ seen_n = len(persistent.seen_scenes)
            grid 4 2:
                xalign 0.5
                spacing 30
                for key, title in ACH.items():
                    $ got = achievement.has(key)
                    $ icon_path = "images/ach_%s.png" % key
                    frame:
                        background None
                        xsize 289
                        ysize 277
                        padding (9, 6)
                        vbox:
                            xalign 0.5
                            yalign 0.0
                            spacing 6
                            fixed:
                                xsize 271
                                ysize 165
                                if got:
                                    add icon_path xalign 0.5 yalign 0.5
                                else:
                                    add icon_path xalign 0.5 yalign 0.5 at locked_icon
                            text (title if got else "???") size 36 xalign 0.5 text_align 0.5 color ("#fff1f6" if got else "#6e5866") font gui.interface_text_font
            fixed:
                xfill True
                ysize 45
                text _("Quiet scenes: [seen_n] / 10") size 33 color "#b79aa8" yalign 0.5
                textbutton _("Close") action SetScreenVariable("closing", True) xalign 1.0 yalign 0.5 text_color "#f2b6cb" text_hover_color "#fff"
    if closing:
        timer 0.35 action Return()