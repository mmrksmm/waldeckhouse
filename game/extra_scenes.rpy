# quiet scenes between days: unlocked after the first endings (persistent.loops)

label interlude(n):
    if n == 1 and persistent.loops >= 1:
        call quiet_rehearsal from _call_quiet_rehearsal
        call quiet_blanket from _call_quiet_blanket
    elif n == 2 and persistent.loops >= 1:
        call quiet_dawn from _call_quiet_dawn
    elif n == 3 and persistent.loops >= 2:
        call quiet_rain from _call_quiet_rain
        call quiet_lullaby from _call_quiet_lullaby
    elif n == 4 and persistent.loops >= 2:
        call quiet_flour from _call_quiet_flour
        if persistent.loops >= 3:
            call quiet_braid from _call_quiet_braid
    elif n == 5 and persistent.loops >= 3:
        call quiet_thanks from _call_quiet_thanks
        if persistent.loops >= 4:
            call quiet_firstlight from _call_quiet_firstlight
    elif n == 6 and persistent.loops >= 4:
        call quiet_goodnight from _call_quiet_goodnight
    return

label quiet_end(code):
    $ persistent.seen_scenes.add(code)
    $ house.pull("warm")
    $ award("quiet_1")
    if len(persistent.seen_scenes) >= 10:
        $ award("quiet_all")
    $ bg("tma")
    return

label quiet_rehearsal:
    pause 0.6
    $ bg("komnata_irene")
    $ play_music("m_noch")
    "I lie in the dark and realize that tomorrow I'll have to say good morning to an armchair."
    "I decide to practice.{w} Once, under my breath, to the ceiling."
    ir "Good morning, Lizetta."
    "It sounds like a station announcement.{w} I try again."
    ir "Good morning, Lizetta!"
    "Worse.{w} Far too bright, as though I were trying to sell her something."
    ir "Good morning, Liz...{w} Lizetta."
    "Now that's almost a human voice.{w} Warm, a little sleepy."
    "It's exactly how I'd like to be greeted myself."
    "I smile into the pillow.{w} Someone in this house ought to have said good morning to me first, but there you are: I beat them to it." id quiet_rehearsal_4f3a19b9
    call quiet_end("S1") from _call_quiet_end
    return

label quiet_dawn:
    $ bg("kuhnya")
    $ play_music("m_noch")
    "I wake before light, as always.{w} The house is still asleep, and I tiptoe to the kitchen, not out of caution but from some odd sort of respect."
    "A kettle stands on the stove.{w} Warm."
    "Not hot and not cold, but exactly warm, like a palm that has only just been taken away."
    "Beside it on a saucer stands a single cup.{w} One, for me."
    "I won't try to find out who put it there.{w} Sometimes it's better just to say “thank you” aloud."
    ir "Thank you."
    "I drink in small sips by the dark window.{w} The sky over the garden slowly lightens, and for the first time in a long while I have nowhere to hurry."
    call quiet_end("S2") from _call_quiet_end_1
    return

label quiet_rain:
    $ bg("tma")
    pause 0.6
    $ bg("detskaya")
    $ play_sfx("z_dozhd")
    "The rain won't let up.{w} Before bed I go to the nursery for no good reason, to check whether the window lets in a draft."
    "It does.{w} Only the faintest bit, but Lizetta's chair stands right in it."
    ir "There, there.{w} Don't look at me like that."
    "I take the shawl from my shoulders and tie it around the back of the chair, trying not to think how it looks from outside."
    "From outside it looks like a grown woman wrapping up furniture.{w} Never mind."
    "Here, it seems, that's normal."
    ir "There.{w} Now you're not afraid, and I'm not embarrassed."
    "I stand a little longer, listening to the rain.{w} The shawl smells of me, and the room becomes a little less foreign."
    "On my way up I think that in the morning I'll have to explain where the shawl went.{w} I decide not to."
    call quiet_end("S3") from _call_quiet_end_2
    return

label quiet_flour:
    $ bg("tma")
    pause 1.2
    $ bg("komnata_irene")
    $ play_music("m_noch")
    "Undressing, I notice in the mirror on the dresser a white smudge on my cheekbone.{w} Flour."
    "I walked around with it on my face all evening, and no one said a word."
    "Not Frau von Waldeck, not Lizetta, and not, of course, the armchair."
    "I laugh aloud, unexpectedly even to myself.{w} Short, muffled, into my palm."
    "I haven't heard how that sounds in a long time."
    "I freeze: the house is so quiet that the laughter seems too loud.{w} But no one scolds."
    ir "Sorry."
    "I don't know who I said it to.{w} The house, I suppose."
    "The house, of course, didn't answer.{w} But it seemed to me that something in the wall ticked approvingly."
    "I don't wipe off the flour right away.{w} I look at myself in the mirror a minute longer, just so, without my usual squint."
    "I think I can be quite pretty, if I don't watch myself."
    call quiet_end("S4") from _call_quiet_end_3
    return

label quiet_thanks:
    "Today is a day I don't want to lose.{w} So before sleeping I do something I never did before: I go through it item by item, like pockets."
    if house.mem.get("dinner") == "bread":
        "Bread passed across the table.{w} Her hand over mine, warm, almost weightless."
    else:
        "A candle that didn't flicker.{w} We both watched it, and both knew we were watching."
    if house.mem.get("stairs") == "looked":
        "The stairs, and her at the bottom, content, as though I'd done something right."
    else:
        "The stairs, and footsteps behind me, half a step behind.{w} Patient."
    if house.mem.get("cookie") == "doll":
        "The saucer on the windowsill.{w} One crumb."
    else:
        "A cookie by the stove, and her face while I ate."
    "I sort through it all and realize I don't want to throw any of it away."
    ir "Thank you for today."
    "I say it into the dark, not specifying to whom.{w} The house, I think, will work out for itself what to take as its own."
    call quiet_end("S5") from _call_quiet_end_4
    return

label quiet_goodnight:
    $ bg("tma")
    pause 0.6
    $ bg("koridor")
    $ play_music("m_noch")
    "I can't sleep.{w} I get up, throw on a wrap and step into the corridor, just to walk through the house like a familiar street."
    "The floorboards no longer creak under my steps.{w} Not because I've learned to walk more softly."
    "They simply know me."
    $ bg("tma")
    pause 0.6
    $ bg("detskaya")
    "I look into the nursery.{w} Lizetta sits in her chair, as always."
    "The moonlight makes her face almost alive, not frighteningly, but like a sleeping child's."
    ir "Good night, Lizetta."
    "I leave the door ajar, leaving a narrow strip of light from the corridor.{w} Just in case."
    $ bg("tma")
    pause 0.6
    $ bg("koridor")
    "At the stairs I stop and lay my palm on the banister.{w} It's warm."
    "Of course, it's only wood, warmed through the day.{w} Of course."
    ir "Good night, house."
    "I go to bed with a feeling I haven't had since, it seems, early childhood: that I don't need protecting from anything, because I'm already under a roof."
    call quiet_end("S6") from _call_quiet_end_5
    return

label quiet_blanket:
    $ bg("komnata_irene")
    $ play_music("m_noch")
    "I've hardly dozed off when there's a soft knock at the door.{w} Not even a knock, but a brush of knuckles, as though the knocker were apologizing in advance."
    show waldeck warm at waldeck_in
    with dissolve
    wa "Not asleep?{w} I won't disturb you."
    "Frau von Waldeck stands on the threshold with a candle and a folded blanket.{w} In her nightgown and knitted shawl she looks shorter and much older than by day."
    wa "The walls let in a chill at night.{w} Nobody tells the governesses, and then they complain of their health."
    ir "Thank you.{w} I'm not cold."
    wa "You are.{w} You're just used to not noticing."
    "She doesn't ask permission; she unfolds the blanket and draws it up to my chin, tucking in the edges with quick, precise movements.{w} It's how one tucks in children, I suppose."
    "Or dolls."
    "I want to object that I'm not five years old.{w} But the blanket smells of dried lavender and of someone else's warmth, and the words won't come."
    wa "There.{w} Now sleep."
    "She lingers in the doorway as though about to say something more.{w} But only adjusts the candle in her hand."
    wa "I'm glad you came."
    "The door closes softly, without a click.{w} I lie in the warmth and don't know what to do with that sentence: tuck it away in a pocket or leave it on the pillow."
    call quiet_end("W1") from _call_quiet_end_6
    return

label quiet_lullaby:
    $ bg("tma")
    pause 1.2
    $ bg("detskaya")
    $ play_sfx("z_dozhd")
    $ play_music("m_lullaby")
    "The rain beats so insistently that I go back to the nursery without knowing why.{w} A lamp is already burning there."
    show waldeck warm at waldeck_in
    with dissolve
    "Frau von Waldeck sits on a low stool by Lizetta's chair.{w} In the folds of the chair lies my shawl."
    "She hasn't taken it off."
    wa "She was always afraid of rain."
    "She says “always” and “was” as though those words don't get in each other's way."
    wa "I used to sing her a little song.{w} Quite simple, only four notes."
    wa "Will you sit beside us?"
    "I sit on the floor by the chair.{w} Frau von Waldeck hums softly, without words, evenly, a little flat on the third note."
    "The melody goes round and round.{w} After a few rounds I realize I'm humming along: I didn't have to learn anything, as if I'd known it a long time."
    wa "You have a good ear."
    ir "It's more the rain's.{w} It keeps time very precisely."
    "She smiles, and there is nothing frightening in that smile.{w} Only weariness and gratitude at not having to sing alone."
    "As I leave, I look back.{w} She's still sitting by the chair, holding her palm over the armrest, beside my shawl, not touching."
    call quiet_end("W2") from _call_quiet_end_7
    return

label quiet_braid:
    "I'm brushing my hair before bed when Frau von Waldeck appears in the doorway with a comb in her hand."
    $ bg("komnata_irene")
    pause 0.6
    show waldeck warm at waldeck_in
    with dissolve
    wa "May I?"
    ir "I can do it myself, thank you."
    wa "I know.{w} But for many years I've had no one to braid for."
    wa "My hands miss it."
    "It sounds so simple and so honest that refusing is impossible.{w} I sit on the edge of the bed with my back to her."
    "The comb moves through my hair slowly, with a light pressure, from the nape to the very ends.{w} Each time the same, like counting."
    wa "You have heavy hair.{w} Heavy and stubborn."
    wa "Like..."
    "Her hand stops for a second at the back of my neck.{w} I don't turn around."
    wa "Like mine in my youth.{w} There."
    "The braid comes out tight and even.{w} Frau von Waldeck fastens it with a ribbon I never owned."
    wa "Don't undo it in the morning, if you don't wish to.{w} Let the day know that you're here."
    hide waldeck
    with dissolve
    pause 0.6
    "When the door closes, I touch the braid with my fingers.{w} The ribbon is silk and warm, as if it had only just been taken from someone's shoulder."
    call quiet_end("W3") from _call_quiet_end_8
    return

label quiet_firstlight:
    $ bg("komnata_irene")
    $ play_music("m_noch")
    "It's not a knock that wakes me, but light: the room suddenly brightens, not from the window, but from a candle at my bedhead."
    show waldeck warm at waldeck_in
    with dissolve
    wa "Come.{w} I want to show you something before it's too late."
    $ bg("tma")
    pause 1.0
    $ bg("sad")
    $ play_music("m_dom")
    "We go out into the garden in cloaks over our nightgowns, barefoot on the wet grass.{w} She insists it has to be this way."
    show waldeck warm at waldeck_in
    with dissolve
    wa "There.{w} Do you see?"
    wa "The night hasn't left yet, but the day has already decided to begin.{w} Only for a little while."
    wa "Ten minutes or so."
    pause 1.0
    "The sky above the fence turns the color of cooling tea.{w} The birds try out their voices, one by one, timidly, like guests who don't know who should go first."
    wa "I come here every morning.{w} Sometimes I think that if I didn't, the light would change its mind."
    pause 1.2
    ir "It won't change its mind."
    wa "You say that so surely.{w} It's pleasant to hear."
    pause 2.0
    "We stand side by side in silence.{w} She smells of lavender and warm wool."
    "I suddenly catch myself not wanting these ten minutes to end."
    pause 1.2
    wa "Thank you for standing with me."
    "I want to say that it's I who should be thanking her.{w} But words, here, seem unnecessary."
    call quiet_end("W4") from _call_quiet_end_9
    return