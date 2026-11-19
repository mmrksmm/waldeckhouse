## Sound: music and ambient sounds (rain, wind, carriage, branch)
## Channels and volume: https://www.renpy.org/doc/html/audio.html
## (accessing house through store: https://www.renpy.org/doc/html/python.html)
init python:

    renpy.music.register_channel("ambient", mixer="sfx", loop=True)

    AMBIENT = ("z_dozhd", "z_veter", "z_kareta", "z_vetka")   # звуки, которые играют по кругу
    AMBIENT_LONG = ("z_dozhd",)                              # их не выключаем при смене фона
    AMBIENT_VOLUME = {"z_vetka": 0.3, "z_veter": 0.7, 'z_dozhd': 0.3}

    MUSIC_FILES = {
        "piano": "greatsofarpiano",
        "xylo": "greatsofarxylophone",
        "choir": "greatsofarchoir",
        "child": "fin",
        "jazz": "jazzyshop",
        "radio": "toyou",
    }
    MUSIC_VOLUME = {"choir": 0.55, "radio": 0.8, 'jazz': 0.4}

    # какая мелодия играет под каждую метку из сценария
    CUE_TRACKS = {
        "m_prolog": "piano", "m_dom": "piano", "m_detskaya": "xylo",
        "m_dozhd": "radio", "m_teplo": "jazz", "m_trevoga": "choir",
        "m_final": "child", "m_dream": "child", "m_lullaby": "xylo",
    }

    # ищет файл звука в папке audio с любым из этих расширений
    def find_audio(name):
        for ext in (".ogg", ".mp3", ".opus", ".wav"):
            path = "audio/" + name + ext
            if renpy.loadable(path):
                return path
        return None

    # ночью музыка зависит от настроения дома
    def music_for(cue):
        if cue == "m_noch":
            return {"cold": "radio", "warm": "child"}.get(store.house.lean, "piano")
        return CUE_TRACKS.get(cue)

    def play_music(cue):
        track = music_for(cue)
        if track is None or store.house.cur_track == track:
            return
        store.house.cur_track = track
        path = find_audio(MUSIC_FILES[track])
        if path:
            renpy.music.play(path, channel="music", fadeout=1.2, fadein=1.5, loop=True)
            renpy.music.set_volume(MUSIC_VOLUME.get(track, 1.0), channel="music")

    def play_sfx(name):
        path = find_audio(name)
        if not path:
            return
        if name in AMBIENT:
            store.house.amb = name
            renpy.music.set_volume(AMBIENT_VOLUME.get(name, 1.0), channel="ambient")
            renpy.music.play(path, channel="ambient", fadein=0.5, loop=True)
        else:
            renpy.sound.play(path)

    def stop_ambient():
        renpy.music.stop(channel="ambient", fadeout=1.0)
