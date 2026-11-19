## Core mechanics: the mood of the house, player choices, diary, varying lines
##
## Sources (Ren'Py documentation):
## achievements          https://www.renpy.org/doc/html/achievement.html
## persistent data       https://www.renpy.org/doc/html/persistent.html
## background tinting    https://www.renpy.org/doc/html/matrixcolor.html
## config callbacks      https://www.renpy.org/doc/html/config.html
## store in functions    https://www.renpy.org/doc/html/python.html
##
## The "mood of the house" logic (warmth/dread), random lines without repeats
## and the name change in the dialogue history were written with the help of
## an AI assistant (Claude), since I could not find a similar example.

default house = House()
default darn_next = 0
default darn_done = False
default recalled = set()

default persistent.loops = 0
default persistent.seen_variants = {}
default persistent.seen_scenes = set()
default persistent.cg_seen = set()
default persistent.last_lean = "mixed"

define slowfade = Fade(1.0, 0.6, 1.2)
define blink = Fade(0.12, 0.0, 0.5)
define soft = Dissolve(0.5)


init python:

    # Состояние дома. warmth растёт от тёплых выборов, dread от холодных.
    # От их разницы зависят цвет фонов, ночная музыка и подпись в конце.
    class House(object):
        def __init__(self):
            self.warmth = 0
            self.dread = 0
            self.greets = 0            # сколько раз Ирэн поздоровалась с Лизеттой
            self.mem = {}              # выборы игрока для дневника: {ключ: вариант}
            self.mem_dread = {}        # сколько было страха в момент выбора (для чернил)
            self.name_state = "normal"
            self.name_look = False
            self.day = 1
            self.scene = ""
            self.cur_bg = None
            self.cur_cg = None
            self.cur_track = None
            self.amb = None

        # kind = "warm" или "cold"; key и value записываются в дневник
        def pull(self, kind, key=None, value=None):
            if kind == "warm":
                self.warmth += 1
            else:
                self.dread += 1
            if key is not None:
                self.mem[key] = value
                self.mem_dread[key] = self.dread
            retint()

        @property
        def lean(self):
            d = self.warmth - self.dread
            if d >= 3:
                return "warm"
            if d <= -3:
                return "cold"
            return "mixed"

        @property
        def name_shown(self):
            return __({"normal": _("Irene"), "cut": _("Ire—"), "greta": _("Greta")}[self.name_state])

        # тёплый цвет фона, если тепла больше, и холодно-синий, если страха
        def tint(self):
            d = self.warmth - self.dread
            k = min(abs(d), 10) / 10.0
            if d >= 0:
                color = (255, int(255 - 9 * k), int(255 - 28 * k))
                saturation = 1.0 + 0.04 * k
            else:
                color = (int(255 - 22 * k), int(255 - 10 * k), 255)
                saturation = 1.0 - 0.12 * k
            return TintMatrix(color) * SaturationMatrix(saturation)


    # выборы игрока, которые попадают в дневник и в воспоминания на 7 день
    MEMORIES = {
        "tea": (_("The Cup"), {
            "drank": _("Honey I never asked for.{w} She knew how I like it before I knew it myself."),
            "pushed": _("A cup that returned to its place while I wasn't looking.{w} I refused once. Then I stopped.")}),
        "night": (_("The First Night"), {
            "dark": _("A branch that wasn't there, and a breath she was waiting for.{w} Someone listened to me as closely as I listened."),
            "candle": _("A candlestick wiped clean of wax while I slept.{w} I was looked after here before I'd had time to think I needed it.")}),
        "table": (_("The Second Evening"), {
            "garden": _("Cornflowers right by the bench.{w} She remembers how they smelled. One doesn't remember such things from books."),
            "clear": _("A child's cup she wiped in circles.{w} A clean cup doesn't need that kind of patience.")}),
        "darning": (_("The Darning"), {
            "done": _("The stitches lay even, as if my hand had known them in advance.{w} I don't remember choosing the pattern."),
            "skipped": _("I never took up the needle.{w} She wasn't offended, only took the sleeve herself, and didn't ask why either.")}),
        "steps": (_("Footsteps in the Corridor"), {
            "met": _("My hands in her warm hands on the stairs.{w} I didn't hear her approach, and I didn't pull away."),
            "waited": _("Footsteps that stopped halfway up the staircase and listened along with me.{w} There were two of us: me, and whoever was listening.")}),
        "cookie": (_("The Cookie"), {
            "doll": _("A saucer on the windowsill with a single crumb left on it.{w} I didn't ask who took it."),
            "ate": _("Her face while I ate the cookie.{w} It's how one looks at something one hasn't seen in a long time.")}),
        "stairs": (_("The Stairs"), {
            "looked": _("Her face at the foot of the stairs.{w} It's how one looks at a child who has walked alone for the first time."),
            "ran": _("Footsteps half a step behind.{w} They weren't chasing me, they were seeing me along.")}),
        "dinner": (_("The Fifth Evening"), {
            "bread": _("Her hand over mine, warm and almost weightless.{w} No one had handed her bread in a long time."),
            "candle": _("A flame that didn't stir in the draft.{w} We both watched it and both knew we were watching.")}),
        "name": (_("My Own Name"), {
            "looked": _("A face without a trace of a slip.{w} She wasn't mistaken. To her I was simply Greta."),
            "book": _("A warm name that wasn't mine.{w} I didn't correct it. I allowed it.")}),
        }

    # достижения
    ACH = {
        "honey": _("Honey"),
        "half_step": _("Half a Step"),
        "stranger_name": _("Someone Else's Name"),
        "warm_house": _("One of the House"),
        "cold_house": _("The Fear Is Real"),
        "full_circle": _("Full Circle"),
        "quiet_1": _("A Quiet Minute"),
        "quiet_all": _("Everything She Doesn't Say"),
    }
    for key in ACH:
        achievement.register(key)

    def award(key):
        if not achievement.has(key):
            achievement.grant(key)
            renpy.notify(__("Achievement: ") + __(ACH[key]))

    ## --- фоны и CG ---

    # перекрашивает текущий фон под настроение
    def retint():
        h = store.house
        if h.cur_bg and h.cur_bg != "tma":
            renpy.show("bg " + h.cur_bg, at_list=[house_tint(h.tint())])
            if h.cur_cg:
                renpy.show(h.cur_cg, at_list=[cg_tint(h.tint())])
            renpy.with_statement(Dissolve(1.6))

    # "tma" — чёрный экран между сценами
    def bg(key):
        h = store.house
        h.cur_bg = key
        h.cur_cg = None
        renpy.scene()
        if key == "tma":
            stop_ambient()
            renpy.show("black")
            renpy.with_statement(slowfade, always=True)
            return
        if h.amb and h.amb not in AMBIENT_LONG:
            stop_ambient()
            h.amb = None
        effects = [house_tint(h.tint())]
        if key == "doroga":
            effects.append(carriage_ride)
        renpy.show("bg " + key, at_list=effects)
        renpy.with_statement(soft, always=True)

    CG_LIST = [("cg table neutral", "Waldeck at the Table"), ("cg table warm", "Waldeck at the Table: Warmth"),
               ("cg table tense", "Waldeck at the Table: Tension"), ("cg table sad", "Waldeck at the Table: Sorrow"),
               ("cg lizetta closed", "Lizetta in the Chair"), ("cg lizetta open", "Lizetta?"),
               ("cg photo", "The Photograph"), ("cg chair2", "The Second Chair")]

    EYES_OPEN_AT = 3    # после скольких финалов у Лизетты открываются глаза

    def show_cg(name, trans=None):
        h = store.house
        h.cur_cg = name
        persistent.cg_seen.add(name)
        renpy.show(name, at_list=[cg_tint(h.tint())])
        renpy.with_statement(trans or soft, always=True)

    def hide_cg(trans=None):
        store.house.cur_cg = None
        renpy.hide("cg")
        renpy.with_statement(trans or soft, always=True)

    def table_cg(mood):
        show_cg("cg table " + mood)


    ## --- главное меню и тексты, которые меняются от финалов ---

    def main_menu_title():
        return "Greta" if persistent.loops >= 2 else "Irene"

    def main_menu_art():
        if persistent.loops > EYES_OPEN_AT:
            return "menu lizetta open"
        if persistent.loops >= 1:
            return "menu lizetta closed"
        return "menu first"

    def menu_start_label():
        if persistent.loops == 0:
            return __("Begin")
        if persistent.loops == 1:
            return __("Return")
        return __("Stay")

    def quit_text():
        h = getattr(store, "house", None)
        in_game = h is not None and bool(h.mem)
        if persistent.loops >= 1 and not in_game:
                return _("You will come back, won't you?")
        lean = h.lean if in_game else persistent.last_lean
        return {"warm": _("She will leave the light on. Quit?"), "cold": _("The house will wait. Quit?")}.get(lean, _("The house will wait. Quit the game?"))

    def refresh_layout_texts():
        layout.QUIT = quit_text()
        layout.MAIN_MENU = _("Return to the main menu? Unsaved progress will be forgotten, but the house will remember anyway.")

    # подпись сохранения: день и название сцены
    DAY_TITLES = ["", "Day One", "Day Two", "Day Three", "Day Four",
                  "Day Five", "Day Six", "Day Seven"]

    def save_caption(d):
        h = store.house
        d["day"] = DAY_TITLES[min(h.day, 7)]
        d["scene"] = h.scene.split(" — ")[0]

    def slot_caption(slot):
        day = FileJson(slot, "day")
        if day is None:
            return FileJson(slot, "caption", empty="")   # старые сохранения
        return __(day) + " — " + __(FileJson(slot, "scene", empty=""))

    # после 6 дня в истории диалогов все "Ирэн" превращаются в "Грета"
    def drift_history():
        for entry in store._history_list:
            if entry.who == __("Irene"):
                entry.who = __("Greta")


    ## --- фразы, которые меняются от прохождения к прохождению ---

    POOLS = {
        # приветствие кукле
        "greet_1": ["Curious: I'm beginning to tell when a room is \"too quiet\" and when it's \"quiet in a good way.\"",
                    "Lizetta, of course, doesn't answer. But now I have someone to say \"good morning\" to. That's already a lot.",
                    "I speak a little more softly than needed, the way people do when they don't want to wake someone sleeping."],
        "greet_2": ["I like how it sounds, \"good morning,\" aloud, to someone. In the city I forgot how it's done.",
                    "The morning sun settles in her lap. I must remember to move the chair a little to the left by tomorrow.",
                    "I catch myself smiling and I'm not ashamed. Here no one counts how often I smile."],
        "greet_3": ["Honestly, I already miss these mornings, the ones that haven't happened yet.",
                    "Lizetta, if you can hear me after all: I'm happy with you. It's the simplest thing I can say, and the hardest.",
                    "Here I am expected. I don't know by whom or why, but expected, and it warms me more than tea."],
        # если Ирэн молчит
        "silent_1": ["The habit of not talking to furniture holds, but I can already hear how it looks from outside.",
                     "I stay silent. But in my head I said \"good morning\" all the same. Thoughts needn't count.",
                     "I set everything out in silence. The silence here, I have to admit, knows how to listen."],
        "silent_2": ["The silence in this room has stopped seeming empty. It's like a pause in a conversation that is about to resume.",
                     "I set the book down so as not to brush the hem of her dress. I say nothing aloud, but my hands have already said it all.",
                     "I'm stubborn. But my stubbornness, it seems, has a smile on now."],
        "silent_3": ["You can be silent and still be near. I learned that here.",
                     "I don't say good morning, but I linger at the door a second longer than usual. Let her know I've come.",
                     "If anyone asked, I'd say I don't like this house. And I wouldn't blush at how untrue that is."],
        # шёпот дома на заставке каждого дня
        "whisper1": ["The house hasn't yet decided how to treat you.", "Come in. You needn't take off your shoes.", "Someone has always just left the room."],
        "whisper2": ["Don't count the stairs.", "Morning here begins before you wake.", "Everything you bring into the house, it remembers."],
        "whisper3": ["Rain is the house sighing.", "Better to speak softly today.", "In the rain all the clocks run slower."],
        "whisper4": ["Warmth is also a way of remembering.", "Flour washes off. Habits don't.", "A cookie is never crooked if someone is waiting for it."],
        "whisper5": ["You've seen this before.", "To repeat is to love: the same word, the same gesture.", "The stairs are the same. You are, almost."],
        "whisper6": ["A name is a warm thing you can wear.", "Not everything said to you is meant for you.", "Today the house is listening especially closely."],
        "whisper7": ["The door is open. The house asks for nothing.", "You can leave. It won't take offense. It will wait.", "The last day is also just a day."],
    }

    # выбирает случайную фразу, не повторяя уже показанные (пока не кончатся все)
    def pick(key):
        pool = POOLS[key]
        seen = persistent.seen_variants.setdefault(key, [])
        fresh = [i for i in range(len(pool)) if i not in seen]
        if not fresh:
            del seen[:]
            fresh = list(range(len(pool)))
        i = renpy.random.choice(fresh)
        seen.append(i)
        return __(pool[i])


init 1 python:
    # музыка в главном меню зависит от числа финалов
    menu_track = {0: "piano", 1: "xylo"}.get(persistent.loops, "radio")
    menu_file = find_audio(MUSIC_FILES[menu_track])
    if menu_file:
        config.main_menu_music = menu_file

    # пропуск текста открывается после первого финала
    config.allow_skipping = persistent.loops > 0

    config.window_title = ["Waldeck House", "The House", "My House"][min(persistent.loops, 2)]

    # свой курсор (до 32x32)
    config.mouse = {"default": [("images/cursor.png", 0, 0)]}

    # тексты подтверждений обновляются при каждом действии, подписи слотов — при сохранении
    config.interact_callbacks.append(refresh_layout_texts)
    config.save_json_callbacks.append(save_caption)


label day_card(title, sub):
    $ whisper = pick("whisper%d" % house.day)
    $ title = __(title)
    $ sub = __(sub)
    $ s_big = 84
    $ s_small = 39
    scene black
    $ renpy.with_statement(slowfade, always=True)
    show text "{size=[s_big]}[title]{/size}\n{i}[sub]{/i}\n\n{size=[s_small]}[whisper]{/size}" at card_in
    pause 3.8
    hide text
    $ renpy.with_statement(Dissolve(1.5), always=True)
    pause 0.8
    return

# d — номер дня: меняется только текст, сам выбор всегда одинаковый
label lesson_open(d):
    menu:
        "Say good morning to Lizetta":
            $ house.pull("warm")
            $ house.greets += 1
            ir "Good morning, Lizetta."
            if d == 2:
                "I speak softly, tenderly, and I'm embarrassed myself at how easily it came.{w} For a second even the draft in the room falls still."
            elif d <= 4:
                "It seems to me the chair is turned toward me a little more than yesterday.{w} Of course, it's only the light from the window."
                "But I like to think it isn't."
            else:
                "The words come on their own, and what answers is a warm silence, the kind you get when you've been expected.{w} I no longer check whether I'm waiting for a reply."
            if persistent.loops >= 1:
                $ narrator(pick("greet_%d" % min(persistent.loops, 3)))
        "Lay out the books in silence":
            $ house.pull("cold")
            if d == 2:
                "I lay out the books and slate briskly, without looking at the chair.{w} I feel it looking at the back of my neck."
                "Of course, it has nothing to look with."
            elif d <= 4:
                "I don't say good morning.{w} But, bumping the leg of the chair, I catch myself muttering “sorry.”"
                "I hope no one heard."
            else:
                "I try to begin in silence, and notice that I place the slate so she can see it.{w} My hand did it before I decided."
            if persistent.loops >= 1:
                $ narrator(pick("silent_%d" % min(persistent.loops, 3)))
    return

# выбор языка при самом первом запуске
default persistent.lang_chosen = False

label splashscreen:
    if not persistent.lang_chosen:
        scene black
        menu:
            "English":
                $ renpy.change_language(None)
            "Русский":
                $ renpy.change_language("russian")
        $ persistent.lang_chosen = True
    return
