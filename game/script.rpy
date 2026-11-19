# main script: seven days, choices through menu, the state of the house is kept in house

define ir = Character("[house.name_shown]", who_color="#e7c9c9")
define wa = Character(_("Frau von Waldeck"), who_color="#e8d3a8")
label start:
    show screen diary_button
    show screen mood
    window auto
    jump day1

label day1:
    $ house.day = 1
    call day_card("Day One", "Arrival") from _call_day_card

    $ house.scene = "Prologue"
    $ bg("tma")
    $ play_music("m_prolog")
    if persistent.loops == 1:
        "I've told this before.{w} To whom, I can't remember."
        "The words settle on my tongue so easily, as though I'd said them more than once."
    elif persistent.loops >= 2:
        "How many times now?{w} The words are the same, and I no longer try to work out who I'm telling."
    "They say a house remembers what the people living in it have forgotten."
    "I'd heard that said many times, by grandmothers, by shopkeepers, by anyone who likes to spin a tale over tea rather than sit in silence."
    "It always struck me as slightly wrong, though I could never say quite why."
    "Now I think I understand.{w} No, I don't."
    "It's only that I've had longer to think about it than anyone ought to have time to think about anything."
    "It isn't the house.{w} A house is just timber, stone and plaster; it has nothing to remember with, even if it wanted to."
    "People remember.{w} People carry someone else's pain as if it were their own, because they once took it in for safekeeping and could never hand it back."
    "And the house simply stands.{w} Stands and waits, patiently, for someone to walk through its doors and decide what is worth remembering and what can finally be left behind."
    "I knew nothing about this house until the day I first walked into it.{w} Nothing but the address and the wages, and, to be honest, I hadn't read the figures very closely."
    "But a house doesn't need you to know anything beforehand in order to take you in."
    "Sometimes it's enough that you have something of your own to run from, and I had plenty to run from then."

    $ house.scene = "The Road"
    $ bg("doroga")
    $ play_sfx("z_kareta")
    "The advertisement used surprisingly few words for how much, as it turned out, it had left unsaid."
    "An address, the wages, and one line about how the ward “requires a special approach”, and that was all."
    "I decided it was a polite way of writing “difficult child” without frightening off whoever might answer."
    "A stammer.{w} A bad temper."
    "Poor health.{w} Children can be any number of things; I'd prepared myself for everything on that long list of possibilities and, frankly, wasn't much worried."
    "Children are children."
    "And in truth, it hardly mattered what I would find when I got there."
    "What I needed was a roof over my head and wages, and for both to be a long way from the city."
    "Far enough that the post would take a week to arrive, or better still, that the letters I could no longer bear to answer would stop coming at all."
    "The coachman had asked me for the address twice already; I think he was hoping I'd change my mind and name somewhere closer to town."
    "The third time he simply fell silent and whipped the horses a little harder than usual, as if he wanted to be rid of me and of the whole conversation."
    "I have one suitcase.{w} I'm not as poor in belongings as that sounds; it's only that nearly everything I owned I left with my landlady in the city, telling her I'd come back for it later."
    "We both knew that wasn't true, but it's easier that way.{w} It's simpler to leave things where they lie than to decide which ones to take and which to give up."
    "The house doesn't appear all at once.{w} First the sound changes; the gravel under the wheels goes dull, as if we've driven into a courtyard"
    "walled in on three sides, and only then does a roof show between the branches, then a chimney, then everything else.{w} The gates sag but aren't rusted, which means they're opened more often than you'd think."
    "It's bigger than I'd imagined from a single line in a letter.{w} And quieter."
    "Far quieter than a house ought to be if someone lives in it all year round.{w} Even the crows here seem to call more softly."

    $ house.scene = "The Porch"
    $ bg("krylco")
    show waldeck neutral at waldeck_in
    with dissolve
    wa "You must be Fräulein Irene.{w} We expected you yesterday."
    "I want to tell her the coach from the city runs every second day and that I left the moment I got her reply,"
    "but I say what one says in these situations instead, because explaining the truth in the first minute of an acquaintance seems unnecessary."
    ir "I apologize for the delay.{w} The road was washed out at the ford."
    wa "Of course.{w} Come in, don't stand in the cold."
    $ bg("prihozhaya")
    show waldeck neutral at waldeck_in
    with dissolve
    "She doesn't smile, as though a smile takes an effort that this moment isn't suited for."
    "Her voice is even and well trained, the voice of someone who has spent a very long time learning to speak calmly about things that can't be spoken of calmly."
    "The hall smells of wax and something else I can't place.{w} Old wood, perhaps, or fabric that hasn't been aired in a long while."
    "Nothing unpleasant.{w} Just the smell of a house where no one has thrown the windows wide open for ages."
    "She takes my cloak and hangs it on a hook beside two other cloaks, clearly older, which no one has worn in a long time.{w} Curious."
    "Though perhaps it's nothing special, old clothes in an old house, that's all."
    wa "The journey must have worn you out.{w} The house is not small, but the part we actually live in is really only two floors."
    wa "The rest is closed up. We don't heat it."
    "She says this offhandedly as she leads me down the corridor, and I count the doors without meaning to: one, two, three, all of them shut, not one ajar even by a finger's width."
    "A sensible arrangement for a widow living with a single child in such a big house."
    ir "It's a lovely house.{w} Have you owned it long?"
    wa "Three generations.{w} My husband was born here."
    wa "I was not. I came here as a bride, and I confess that at first it seemed far too large for one family."
    "She says it with a faint, almost imperceptible irony, the first hint of humor from her all this time."
    wa "Now, perhaps, it's the other way around.{w} Sometimes it seems too small."
    "I don't ask what she means."
    "In my years in other people's houses I've learned to tell apart the things people say so that someone will answer from the things they say simply because silence, at that moment, would be heavier."
    "This is the second kind."

    $ house.scene = "The Dining Room"
    $ bg ('tma')
    pause 0.6
    $ bg("stolovaya")
    pause 0.6
    
    wa "Please, sit.{w} I'm sure you're hungry after the journey."
    "I take the chair she offers, the one nearer the window, and only once I'm settled do I notice that the table is laid for three.{w} I count again. Yes, three."
    "One of the places is clearly a child's, with a smaller cup and a fork that's almost a toy."
    "The daughter hasn't come down yet, I suppose.{w} Or she's being kept apart on purpose until the new person in the house settles in... I've heard of that in families where a child is especially shy, or unwell."
    $ table_cg("neutral")
    ir "Forgive me, will your daughter be joining us?"
    $ table_cg("tense")
    "Her hands over the teapot stop for a moment, then go on pouring, as though the question had never been asked."
    $ table_cg("neutral")
    wa "Lizetta is having her supper early today.{w} She hasn't been well these last few days. Nothing serious."
    wa "You'll meet her upstairs, after tea."
    wa "She's a little shy with new people.{w} Don't be surprised if she doesn't speak at first."
    ir "Of course.{w} Children often react that way to change."
    "Something in her tone takes away my wish to ask more."
    "She didn't answer rudely, quite the opposite; she was polite, almost too smooth, as though the line had been rehearsed and spoken many times, to different people, in this very room, at this very table."
    wa "And here is the bread.{w} Forgive us, it's a modest table."
    wa "I've run the household on my own for a long time, without much help."
    ir "I'm used to a modest table."
    wa "That's good.{w} Governesses spoiled by luxury don't last long with us."
    "She laughs, briefly, only with the corners of her mouth.{w} I decide I should smile too, though I'm not sure whether it was a joke."
    "The bread, incidentally, is good.{w} Still warm, the crust crackling a little."
    "The butter melts quickly, so the kitchen must be close by, and the stove was lit not long ago.{w} I finish a slice faster than I meant to."
    wa "Eat, eat.{w} Supper is a long way off, and after a journey one always wants more."
    "She pours me more tea without asking."
    menu:
        "Drink the tea to the bottom.":
            $ house.pull("warm", "tea", "drank")
            $ award("honey")
            "I drink it down, hot and sweetened with honey.{w} Only afterward do I realize I never told her I like it with honey."
            "But the cup warms my hands so well that I don't want to think about it."
        "Push the cup away until I've found my feet.":
            $ house.pull("cold", "tea", "pushed")
            "I push the cup away: until I'm somebody here, it's better not to accept more than I should.{w} Frau von Waldeck takes no offense and only nods, the way one nods when one knows there will be time."
            "A minute later the cup is back in front of me, full and warm.{w} I didn't see anyone replace it."
    "At the edge of the table, beside the child's place, I notice an unopened envelope.{w} The return address is in a woman's hand, from the city."
    "The sender's surname is the same as the lady of the house.{w} A sister?"
    "A grown daughter I wasn't told about?"
    "Judging by the layer of dust on the envelope, it has lain here for more than a day, and, stranger still, for more than a week."
    "I don't dare pick up someone else's letter; I give it a brief glance and look away when Frau von Waldeck begins to speak again."

    $ house.scene = "The Nursery"
    $ bg("tma")
    pause 0.6
    $ bg("detskaya")
    $ play_music("m_detskaya")
    wa "Be gentle with her at first.{w} She's used to quiet."
    "I expected something gloomy, heavy curtains and half-darkness, but the door opens on a room so flooded with light that I squint for a moment."
    "Lace curtains, a canopied cot, a shelf of toys.{w} The room smells of dust and something faintly sweet."
    "Wax, I think, or dried flowers."
    "By the window, in an armchair, sits a figure in a dress."
    $ show_cg("cg lizetta closed")
    "The light falls straight on her, and for the first second I take her for a child, a little girl, neatly combed, sitting perfectly still as if posing for a portrait."
    wa "Lizetta, dear, this is Fräulein Irene.{w} She will be teaching you."
    "She goes up to the chair and smooths a fold in the figure's dress, with the ordinary, practiced gesture one uses on a living child."
    "I take a step closer and only then do I see.{w} It isn't a child."
    "It's a doll.{w} A porcelain face, glass eyes, carefully set curls, sitting in a child's chair, dressed more carefully than I was ever dressed for a school pageant."
    "The height of a real child, real clothes, even shoes on the small feet, but the face is motionless, glossy, too smooth to be alive.{w} I don't know how many seconds I stand there in silence."
    "Enough, probably, for it to be noticed."
    wa "She isn't very talkative today.{w} But you'll get used to her ways."
    "Her voice is perfectly level, without a single hitch, the line spoken as if not for the first time, and long since no effort at all."
    "I have to decide what to say within the next three seconds, or my face will say something extra for me.{w} And I need this job."
    ir "Hello, Lizetta.{w} I'm pleased to meet you."
    "I bow my head slightly to the doll, a courtesy addressed to a child.{w} The doll, of course, doesn't answer."
    "No one expected it to, but a little pause after my words hangs in the air all the same."
    "Frau von Waldeck seems pleased that I didn't ask any questions.{w} She nods briefly, as if I'd just passed a first examination I hadn't been told existed."
    wa "Good.{w} As for terms, I think it's sensible to agree on a week to begin with."
    wa "So that you can see whether the place suits you, and I can see whether you suit Lizetta."
    wa "Afterward, if all goes well, we'll talk about terms at greater length."
    wa "The driver who brought you usually waits in the village for a week, in case a governess doesn't like us and wants to return at once."
    "Seven days.{w} Strangely, it calms me that this stay has a clear boundary, set by someone other than me,"
    "as though a fixed term makes the place itself a little safer, whatever I find in it."
    wa "Look around while you wait, I won't get in your way."
    $ bg("tma")
    pause 0.6
    $ bg("detskaya")
    "I take a closer look at the room while I have a minute.{w} The wardrobe against the wall is locked; I try the handle and it doesn't give."
    "Well, never mind, who knows what's in there."
    "On the shelf stand tin soldiers, a shabby plush rabbit missing an ear, a stack of books with dog-eared corners."
    "Ordinary children's things, well worn, the only things in the whole room that look as if they'd actually been used."
    "Odd.{w} The doll herself is flawless, while the toys around her are battered as if they'd been picked up a thousand times."
    "Maybe the doll came later, and before her there were the ordinary things of an ordinary childhood, and the doll is something that was added to the room afterward, on top."
    "Or maybe I'm simply thinking too much on my very first day."

    $ bg("tma")
    $ house.scene = "Irene's Room"
    $ bg("komnata_irene")
    show waldeck warm at waldeck_in
    wa "I hope you'll be comfortable here.{w} It's no palace, but it's quiet, and the stove draws well."
    ir "It's very nice, thank you."
    "The room really is small, three steps from the door to the window if you take long ones, but it's clean, and that's already a good deal."
    "The bed is made up with fresh linen, and the pillow's creases seem to have been smoothed out on purpose."
    wa "Supper will be later, I'll come for you.{w} Rest in the meantime."
    hide waldeck
    with dissolve
    $ bg('tma')
    "Alone.{w} For the first time all day truly alone, with no need to keep my face in order."
    "I sit down on the bed and simply sit there for a while, doing nothing, staring at one spot on the faded wallpaper."
    "A doll instead of a child.{w} It happens; I read somewhere that after a loss some families commission a portrait and hang it where it can be seen, talk to it, set flowers in front of it."
    "I suppose a doll is the same thing, only more literal."
    "I'm not going to think about it much just now.{w} I'm paid to give lessons, not to hold opinions on how the lady of the house copes with her grief."
    "God knows I have enough of my own without inventing someone else's."
    "Though, I have to admit, I'm already inventing.{w} I can't help it."
    "My mind works faster than I'd like, especially when I'm tired."

    $ house.scene = "Evening"
    $ bg('tma')
    pause 0.6
    $ bg("komnata_irene")
    $ play_music("m_noch")
    "At supper we talked mostly about the weather, whether it would rain this week, whether the road to the village would freeze,"
    "the most ordinary talk, the kind people use to fill pauses so they needn't sit in silence.{w} Frau von Waldeck ate little and neatly, as though from duty rather than real hunger."
    "My hands want to do something familiar after a whole day of unfamiliar things, so I unpack my suitcase."
    "Dresses, linen, a couple of books, a comb, and that's all I have, not counting what I left with my landlady in the city."
    "I hang my clothes on the single hook behind the door and stack the books on the nightstand, putting on top the one I'm reading, though I doubt I'll find time to read in the next few days."
    $ play_sfx("z_vetka")
    "A branch scrapes the glass at even intervals, one, two, one, two, as if someone were counting out a beat."
    "Silly, but I still listen for a second before blowing out the candle, and only then do I remember"
    $ bg('tma')
    "that outside my window there doesn't seem to be a single tree close enough to reach the glass."
    menu:
        "Blow out the candle and listen.":
            $ house.pull("cold", "night", "dark")
            $ play_sfx("z_svecha")
            "I blow out the candle and lie in the dark, counting along with the branch.{w} One, two, one, two."
            "Whenever I hold my breath, the tapping stops too for a moment, as if waiting."
        "Leave the candle to burn down.":
            $ house.pull("warm", "night", "candle")
            $ play_sfx("z_svecha")
            "My hand stops at the wick: I leave it burning.{w} In a room where someone is counting out a beat, I don't want the dark."
            "The flame leans toward the door, steady and calm, as though someone were standing there warming themselves."
    "I don't dare check."
    "The wind bends the branches strangely, and the sound could come from anywhere in such a big, quiet house; you can hear for a mile what in the city would drown among a thousand other sounds."
    "Besides, it's cold to get up."
    call interlude(1) from _call_interlude
    jump day2

label day2:
    $ house.day = 2
    call day_card("Day Two", "The Lesson") from _call_day_card_1

    $ house.scene = "Morning, Dining Room"
    $ bg("stolovaya")
    pause 0.6
    $ play_music("m_dom")
    "I wake before dawn, a habit that isn't easy to shake.{w} I lie there a while, listening to the house creak somewhere in its walls, as if stretching before the new day."
    "It's light outside, but not quite clear.{w} Fog, maybe, or just that kind of sky."
    if house.mem.get("night") == "dark":
        "I never worked out last night where the tapping came from.{w} From the window this morning I can see: the nearest tree stands by the fence, forty paces away."
        "A branch couldn't have reached the glass from there, not even in a storm."
    else:
        "The candle burned down to the base overnight, and the holder has already been wiped free of wax, clean and neat, as for a guest who was expected.{w} I didn't hear anyone come in."
    $ table_cg("neutral")
    wa "Good morning.{w} Did you sleep well in a new place?"
    ir "Quite well, thank you.{w} It's unusually quiet here."
    wa "Yes.{w} It always is."
    wa "It used to be different, but ever since my husband died, the house seems to have decided there's no point in making noise anymore."
    "She tells me of her husband's death in the same tone one uses for the weather.{w} Not an invitation to talk."
    "I don't know how to react."
    ir "I'm sorry to hear that."
    wa "It was quite a while ago.{w} Lizetta was very small then."
    ir "She must hardly remember her father."
    wa "She doesn't.{w} Though I try to tell her about him often; it matters for children to know where they come from."
    "I nod as though there were some obvious sense in it, though a part of me is already quietly asking why one would tell a doll about a man, a doll that can neither remember nor forget."
    "But I don't ask aloud.{w} I'm not paid for questions."
    wa "Eat, eat, before it gets cold.{w} We have fresh eggs here; the hens are still laying, thank God, though it's turning cold."
    "The eggs are good, truly.{w} You can't find any like them in the city."
    "I butter my bread and try not to hurry, though the habit of eating fast has stayed with me from the days when meals were so often interrupted by something urgent."
    wa "Finish up, no need to rush.{w} You can begin the lesson with Lizetta whenever you're ready."
    wa "She's in no hurry."
    "She smiles as she says it, almost kindly, if not for the way she said “She's in no hurry.”"
    "It isn't how one speaks of a living child waiting for her lesson, but of something that is simply there in the room and will be there however long you draw out breakfast."

    $ house.scene = "Nursery, Lesson"
    $ bg("tma")
    pause 0.6
    $ bg("detskaya")
    show lizetta at lizetta_pos
    $ play_music("m_detskaya")
    with dissolve
    "The first real lesson.{w} I worked out a plan last night, lying awake: we begin with the alphabet, then counting to ten, then, if there's time, a short story before lunch."
    "The only problem is that across from me sits a creature who physically cannot repeat a letter, or smile, or tire of the lesson before its time."
    "Well, then, we'll pretend.{w} It isn't the first time I've pretended to an employer that everything is going to plan."
    call lesson_open(2) from _call_lesson_open
    ir "Well, let's start with the simplest one.{w} This letter is “A.”"
    ir "Watch closely, I'll show you how it's written."
    pause 1.0
    "For the first few minutes I feel ridiculous, talking into the void, showing the slate to an armchair."
    "But I soon notice the absurdity dulls on its own, as long as I don't think about it directly."
    ir "“A” is for alphabet.{w} “B” is for breeze."
    ir "You know, the wind really is strong today. Can you hear it howling in the chimney?"
    pause 0.6
    $ play_sfx("z_veter")
    "I don't expect an answer, of course.{w} I'm only remarking on the coincidence aloud."
    "It's calmer that way."
    "I was taught in exactly this way myself, from this very primer, I think, only a different edition, and suddenly I remember my mother's voice so clearly,"
    "saying the same thing about the letter “A” that I'm saying now, only in a different voice, in a different room, to someone else's child, who will never grow up."
    ir "“C” is for candle, “D” is for door, “E” is for elm...{w} Now you try."
    ir "Just nod, at least, if you recognize the letter."
    ir "“F” is for frost, coming soon, by the way.{w} “G” is for garden, “H” is for home, “I” is for ink, “J” is for jar, “K” is for key, like the one to that cupboard, see?"
    ir "“L” is for lantern, “M” is for mama..."
    pause 1.5
    "I falter on that word for a fraction of a second.{w} It's not that it's hard to say."
    "It simply catches on something, like a splinter."
    ir "“N” is for night, “O” is for oven, “P” is for pillow, “Q” is for quiet, and I think that may be the best letter for this house."
    "I laugh softly, alone, at my own joke.{w} The doll, of course, doesn't laugh."
    "But I don't mind that she doesn't."
    ir "“R” is for roses, your mother said they used to grow in the garden.{w} “S” is for snug, though it's hard to believe here, at first.{w} “T”, “U”, “V”, “X”, let's skip those for now, they're tricky."
    ir "“W” is for wardrobe, that very one, by the way.{w} “Y”, “Z”, and there it is, the whole alphabet in a single morning. Well done for sitting through it."
    pause 2.0
    "Silence.{w} Long, even, by now familiar silence, after two days of it."
    "I put the slate aside."
    ir "Well, shall we try counting to twenty?{w} I promise it will be less dull than it sounds."
    ir "One, two, three..."
    ir "...eighteen, nineteen, twenty.{w} See, it isn't scary at all."

    $ house.scene = "Nursery, A Discovery"
    "I straighten the blanket that has slipped off the cot and bump against the wardrobe on the way, yesterday it was locked, I tried the handle myself.{w} Today it gives without any effort."
    "Inside are neatly folded children's dresses, all one size, all clearly for the doll."
    "Perhaps Frau von Waldeck unlocked it this morning to take out a clean dress for Lizetta, and I simply missed it?{w} A perfectly logical explanation."
    $ show_cg("cg chair2")
    "Behind the wardrobe I discover a second armchair, pushed into the corner and covered with a dusty cloth.{w} I didn't notice it yesterday, because of the wardrobe, probably."
    "It's the same make as Lizetta's chair, only a little smaller and with no upholstery on the seat, bare wood, as if the cushion was taken off it long ago and nobody bothered to put it back."
    "I don't touch the cloth that covers it.{w} I only glance at it sideways and carry on with the lesson as though I'd noticed nothing."
    "On the shelf, under a stack of books, the corner of a sheet of paper sticks out, a child's pencil drawing of a house with two figures on the porch, holding hands.{w} One is obviously an adult."
    "The other is a child, and beside her, a little apart, is a smudged smaller silhouette, as though the artist had started to draw a third figure and changed her mind, half erasing it."
    "Or simply never finished; children often abandon drawings halfway.{w} I don't hurry to invent stories ahead of time."
    "I put the drawing back under the books, exactly as it lay."
    $ bg('tma')
    pause 0.6
    $ house.scene = "Garden, Afternoon"
    $ bg("sad")
    "I have an hour of free time before supper and decide to go out for some air.{w} My room has smelled of wax and dust all day."
    "The garden turns out smaller than you'd expect for such a big house: a few overgrown shrubs, a path covered with wet leaves from last year, and a low stone bench."
    "The air is cold and smells of wet earth and rotting leaves.{w} I sit on the cold stone for longer than one should in this weather, simply because it's easier to breathe in the garden than in the house."
    "In the distance, beyond the fence, I can see the roof of the chapel by the graveyard, the same one I could see from the nursery window, only from another angle.{w} I can guess who is buried there."
    "Frau von Waldeck's husband, surely."
    "On my way back I notice in one of the ground-floor windows, the very one that, according to Frau von Waldeck,"
    "has long been closed and unheated, a faint, uneven glow, as if a candle had flickered there for a second.{w} I stop and look again."
    "The window is already dark."
    "Perhaps it was the reflection of the sunset in the glass.{w} The sky really is red today."
    pause 0.6
    $ bg("prihozhaya")
    pause 0.6
    $ house.scene = "Evening, Dining Room"
    $ bg("stolovaya")
    pause 0.6
    $ table_cg("warm")
    $ play_music("m_dom")
    wa "How did the first lesson go?"
    ir "Quietly.{w} We went through the whole alphabet."
    ir "Lizetta seems to know her letters better than I thought."
    "I say it and hear for myself how natural it sounds, as though I really had taught a child who'd taken something in, and hadn't spent a solid hour talking to porcelain."
    wa "She's a capable girl.{w} She just needs time to trust a person."
    ir "By the way, I found an old drawing in the nursery.{w} A house, two figures on the porch."
    wa "Ah, that one.{w} I came across it myself last week while tidying."
    wa "I kept meaning to show you, and forgot."
    ir "Forgive me, I didn't mean to rummage through your things."
    wa "It's nothing.{w} It's just an old drawing."
    ir "And I also noticed another armchair in the nursery, behind the wardrobe, covered with a cloth."
    $ table_cg("tense")
    wa "Ah, that one..."
    pause 0.6
    $ table_cg("neutral")
    wa "The bread turned out well today, don't you think?{w} The oven has been temperamental lately; I was afraid it would burn."
    "She didn't answer.{w} She simply left the sentence unfinished and began to speak of bread."
    "I don't want to press her.{w} Something in that pause tells me that if I ask again, there will still be no answer."
    wa "You know, the garden used to be quite different.{w} While the gardener looked after it, cornflowers grew there, and jasmine bushes right by the bench."
    wa "He left soon after my husband died, but I haven't abandoned Lizetta's roses."
    "I listen with half an ear.{w} I'm thinking about the second chair under its cloth and how quickly the conversation about it broke off."
    menu:
        "Ask about the cornflowers.":
            $ house.pull("warm", "table", "garden")
            ir "Did the cornflowers grow right by the bench?"
            wa "Right by it.{w} Lizetta loved them more than the roses."
            wa "Strange that I still remember how they smelled."
        "Stand and help her clear the table.":
            $ house.pull("cold", "table", "clear")
            "I get up and reach for the dishes.{w} She doesn't let me take the child's cup, but gently intercepts it: “This one I'll do myself.”"
            "Then she wipes it for a long time with the edge of a napkin, in circles, once, twice, a third time, though the cup has long been clean.{w} I look away first."
    wa "Forgive me, I've been talking too much.{w} You must be tired after the day."
    ir "No, not at all.{w} I like listening."
    $ table_cg("warm")
    wa "Good night, Fräulein.{w} Rest well."
    "I climb the stairs and catch myself thinking that the evening wasn't as heavy as I'd expected after the talk about the chair.{w} On the contrary, it was almost cozy."
    pause 0.6
    $ bg('komnata_irene')
    pause 0.6
    $ bg("tma")
    pause 1.0
    call interlude(2) from _call_interlude_1
    jump day3

label day3:
    $ house.day = 3
    call day_card("Day Three", "Rain") from _call_day_card_2

    $ house.scene = "Morning, Dining Room"
    $ bg("stolovaya")
    pause 0.6
    $ play_sfx("z_dozhd")
    $ play_music("m_dozhd")
    "I woke to the patter of drops on the roof, then lay for a while, listening."
    "The rain has been falling since dawn, and it makes the house sound quite different, every board, every beam seems to have begun to creak a little louder."
    $ table_cg("neutral")
    wa "In weather like this it's best not to leave the house.{w} Will you hold the lesson in the nursery, as usual?"
    ir "Yes, of course."
    wa "Good.{w} It's damp in the study today; the fireplace won't draw at all in this weather."
    wa "I think I'll sit with you in the nursery, if I won't be in the way."
    ir "Of course you won't be.{w} I actually feel calmer when you're near."
    wa "You know, rainy days have always been special with us.{w} My husband used to say that in this weather the house stops pretending it doesn't care who lives in it."
    "She says it with a quiet, shy smile, the way one speaks of an old family joke that there's no one left to tell."
    ir "That's beautifully put.{w} He must have been a poet at heart."
    wa "He was an engineer, if you can imagine a worse combination.{w} But yes, something would break through in him now and then."

    $ house.scene = "Nursery, Darning and Arithmetic"
    $ bg("tma")
    pause 0.6
    $ bg("tma")
    pause 0.6
    $ bg("detskaya")
    show lizetta at lizetta_pos
    show waldeck neutral at waldeck_in
    with dissolve
    call lesson_open(3) from _call_lesson_open_1
    ir "Today we'll practice counting, all right?{w} Let's go over what we learned yesterday."
    ir "One, two, three, four, five..."
    ir "...six, seven, eight, nine, ten.{w} Now let's add."
    ir "How much is two plus three?"
    pause 1.0
    ir "Five.{w} Look, I take two fingers on one hand and three on the other, and count them all together."
    ir "See how simple it is."
    ir "Clever girl."
    "I say “clever girl” to a doll who has done absolutely nothing.{w} I don't correct myself."
    "I no longer even notice that I should."
    $ play_sfx("z_polovitsa")
    with vpunch
    "A floorboard creaks on its own, I know for certain I didn't go near the cot, I've been sitting at the little table all along.{w} The house is probably just settling in the rain."
    "I go over and press the board down with my foot.{w} It creaks exactly the same under my weight, with the very same sound."
    "So it's the board."
    ir "Where were we... ah yes, let's try counting in tens.{w} Ten, twenty, thirty..."
    ir "...ninety, one hundred.{w} There, a hundred, we won't go further for now, or both our heads will spin."
    wa "She's quiet today.{w} Usually in the rain she likes to listen to the drops on the glass."
    ir "I'll be glad to read to her by the window, if you like."
    "Frau von Waldeck takes a needle from a little box, and a tiny sleeve; the doll has a seam that's come apart.{w} “If it isn't too much trouble,” she says, and hands it to me."
    $ darn_next = 0
    $ darning_cursor(True)
    $ darn_done = renpy.call_screen("darning", DARN_POINTS)
    $ darning_cursor(False)
    if darn_done:
        $ house.pull("warm", "darning", "done")
        "The stitches lie even, as though my hand had known them before I did.{w} Frau von Waldeck looks at them and is silent the way people are silent from gladness."
    else:
        $ house.pull("cold", "darning", "skipped")
        "I set the sleeve aside: “Forgive me, I'm a poor needlewoman.”{w} She nods and takes up the needle herself, without reproach, with precise movements that aren't learned in a single day."
    show waldeck warm
    with dissolve
    wa "Gret..."
    wa "Forgive me.{w} I meant to say something quite different, and it flew out of my head."
    wa "The rain affects me so, I come undone, I lose thoughts halfway."
    "I don't know what she meant to say, and I don't ask.{w} Who knows what rises to a person's tongue when she gazes out the window in the rain."
    wa "You know, I could hardly sew myself until I moved here.{w} The old housekeeper taught me, a strict woman, but fair."
    ir "Your stitches are very even.{w} One can tell at once you had a good teacher."
    wa "And you?{w} Surely someone taught you everything, too."
    ir "My mother.{w} She was stricter than your housekeeper, I expect."
    wa "I think she would be proud of you now.{w} Not every governess lasts even a week with us, and you carry yourself as though you'd lived here all your life."
    "Something in that remark stings me.{w} Not because it's wrong, but because it's quite the opposite."
    ir "Maybe I simply needed a place like this.{w} A quiet one."
    wa "What are you running from, if it isn't a secret?{w} Though forgive me, you needn't answer."
    ir "From myself, I suppose.{w} It's the most ordinary thing people run from."
    wa "The most ordinary, and the most hopeless.{w} One doesn't run from oneself, Fräulein."
    wa "At best one finds a place where it can be forgotten for a little while."
    ir "You speak as though you know it from experience."
    wa "I do.{w} Only I never went anywhere."
    wa "I simply stopped going beyond the garden."
    "I want to ask, forgotten what, exactly?{w} I don't ask."
    "Some doors are better left untouched until you're invited in."
    "For a few minutes the room holds only the sound of the rain, the scratch of chalk on the slate and the soft whisper of thread.{w} I like this quiet."
    "Just the quiet of two people, each busy with her own task."
    ir "Let's finish with a story today.{w} This one, about the forest, doesn't seem to have been read to the end by anyone."
    ir "“Once upon a time there was a girl who got lost in the forest, and the farther she went, the thicker the trees grew...”"
    ir "I think we'll stop there for today.{w} Otherwise there'll be nothing left to read tomorrow."

    $ house.scene = "Corridor, Afternoon"
    $ bg("tma")
    pause 0.6
    $ bg("koridor")
    "After lunch I have a free hour and decide to wander through the house, just to stretch my legs.{w} That's what I tell myself, anyway."
    "The door at the very end of the corridor is locked, like the others Frau von Waldeck mentioned on the first day."
    "And yet I notice that the floorboards in front of this particular door are a little more worn than in front of the rest."
    "On the wall hangs a portrait of a man of middle age, painted, judging by the clothes, some twenty or thirty years ago.{w} Probably Frau von Waldeck's late husband."
    "He has attentive, slightly weary eyes."
    $ play_sfx("z_chasy")
    "At the end of the corridor an old family clock has stopped at a quarter to three."
    "I reach for the key on its chain and wind it, and for a second I wonder how I even know that it has to be wound to the right."
    $ play_sfx("z_shagi")
    "I hear footsteps downstairs and decide that's enough curiosity for one day."
    menu:
        "Go down to meet the footsteps.":
            $ house.pull("warm", "steps", "met")
            show waldeck warm at waldeck_in
            "Frau von Waldeck stands at the foot of the stairs with a lamp raised to light my steps.{w} “You're cold,” she says, and takes my hands in hers without asking."
            "Her hands are warm, and I don't want to take mine away.{w} Only later does the thought come: I never heard her approach."
            "The footsteps I did hear died away long ago."
        "Wait where I am until the footsteps fade.":
            $ house.pull("cold", "steps", "waited")
            $ play_sfx("z_shagi")
            "I stay where I am and count the steps.{w} They climb to the middle of the staircase and stop there."
            "I can hear someone standing and listening, just as I am listening.{w} For a minute."
            "Then the footsteps go back down just as calmly.{w} I'm not afraid."
            "More embarrassed, as if both of us had been caught doing the same thing."

    $ house.scene = "Evening, Dining Room"
    $ bg ('tma')
    pause 0.6
    $ bg("stolovaya")
    pause 0.6
    $ table_cg("warm")
    $ play_sfx("z_dozhd")
    wa "You must miss the city in weather like this."
    ir "Not particularly.{w} To be honest, I feel calmer away from the city."
    wa "I understand.{w} Sometimes quiet is the only thing that helps."
    "She doesn't say helps with what.{w} We both keep silent."
    "It isn't awkward, more like two tired women who don't need to fill the pause with talk."
    $ bg('tma')
    pause 0.6
    $ bg("komnata_irene")
    $ play_music("m_noch")
    "After supper I go up to my room.{w} Out of idle curiosity I take down a book that was here before me.{w} Between its pages I find an old letter."
    "Evidently one of the previous occupants used the book as a box for papers."

    $ house.scene = "The Letter"
    "“...you write to me again as if she were still here, and I don't know how to answer.{w} Mother, I'm not angry with you, truly I'm not."
    "I simply can't keep coming to a house where the table is still laid for her every evening.{w} It has been three years."
    "I understand you needed something to believe in all this time, but I can't be part of it any longer, I can't sit down across from...”"
    "The letter breaks off, the second page is missing.{w} All that can be made out is the start of the next line: “Your Greta.”"
    "Greta.{w} So the envelope on the dining table is from her.{w} The grown daughter nobody mentioned to me."
    "Three years.{w} All this time, then, I haven't been talking to a shy child but to..."
    "I should say it to myself plainly, without circling, just once: to a doll who is dressed, fed and put to bed as though she were truly alive."
    "For some reason I'm not very surprised.{w} I fold the letter back along its creases and return the book to the shelf, to the place where it stood, spine out."
    "I lie awake a long time, listening to the rain outside that swells and then dies down again."
    "Three years ago something happened in this house, and the girl who wrote these lines, Greta, clearly couldn't bear it."
    "And I lie here, in a stranger's room, and feel not horror but something much closer to recognition."
    $ bg("tma")
    call interlude(3) from _call_interlude_2
    jump day4

label day4:
    $ house.day = 4
    call day_card("Day Four", "The Photograph") from _call_day_card_3

    $ house.scene = "Morning, Dining Room"
    $ bg("stolovaya")
    pause 0.6
    $ play_music("m_dom")
    "The rain has stopped, and at last I woke to something other than the patter of drops."
    $ table_cg("warm")
    wa "Did you sleep?{w} You went to your room early yesterday."
    ir "Yes, thank you.{w} I was simply tired after the day."
    "I don't mention the letter."
    "I'm not ready to ask questions outright; if I ask now, at breakfast, the answer will come out just as smooth and rehearsed as everything else she says."
    wa "Lizetta also loved being read to in the evening.{w} She fell asleep halfway through the page every time."
    wa "Though of course, in her case that never changes."
    "A strange phrase.{w} As if she herself isn't sure which tense to use for Lizetta, past or present."
    ir "I'll gladly read to her today.{w} We stopped at an interesting place."
    wa "Winter is coming soon; I'll light a better fire in the nursery.{w} Lizetta gets cold faster than she looks."
    "I can't think of an answer right away, so I just break off another piece of bread, buying time."
    ir "Yes, of course.{w} It really is chilly in the nursery in the mornings."
    "I answer as though we were truly talking about a draft.{w} It unsettles me how easily I find a way not to notice the absurdity of someone else's sentence."
    wa "By the way, won't you have another cup?{w} The tea came out well today."
    wa "With mint from the garden, the last of what's left from summer."
    ir "I'd love one.{w} It smells even better than usual."
    if house.mem.get("tea") == "drank":
        "The honey in the cup is already dissolved, just as on the first evening.{w} I still don't remember asking for it."
    else:
        "On the first evening I pushed the cup away.{w} Today I take it first, without waiting to be offered."
        "When that changed, I don't remember."
    "I drink the tea in small sips and listen to her talk about the vegetable patch, how the cucumbers failed this year, but the apple trees gave an unheard-of harvest."

    $ house.scene = "Nursery, The Story"
    $ bg("tma")
    pause 0.6
    $ bg("detskaya")
    show lizetta at lizetta_pos
    with dissolve
    call lesson_open(4) from _call_lesson_open_2
    ir "Well, shall we go on?{w} We stopped where the girl got lost in the forest."
    ir "“She had been walking for a long time, her legs were aching, and it was growing darker all around... and suddenly she saw a little light between the trees.”"
    pause 0.8
    "I pause after the exciting moments, where a child would usually ask something.{w} I wait a second."
    "Then I simply read on by myself."
    ir "“The girl came closer and saw a small cottage, wreathed all over in ivy.{w} The door stood ajar, as though she were expected...”"
    "The sun is unusually bright today.{w} The bands of light lie on the floor in such clear lines that it seems you could touch them."
    "One of them falls right across Lizetta's chair, and in that light the porcelain of her face looks, for a moment, almost warm."
    "I put down the book to straighten the pillow on the cot, and in passing brush against the bottom drawer of the nightstand; it's open wider than usual."
    "Inside, among folded children's handkerchiefs, lies a photograph in a wooden frame, face down.{w} Hesitantly, I turn it over."
    $ show_cg("cg photo")
    "Two girls stand side by side, holding hands, in front of this very house.{w} One face is clear, those very curls, that very oval."
    "The other face seems to be rubbed out, not torn, just worn away to a blurred smudge, carefully, in circles, as if someone had done it not once but over years."
    "Who rubs a face out of a photograph for years?{w} I put the photograph back in the drawer, face down, between the same handkerchiefs."
    $ hide_cg()
    ir "Shall we go on, Lizetta?{w} “Inside the cottage it was warm, and supper stood laid on the table, as though the owners had stepped out only for a moment...”"
    ir "I think we'll stop there.{w} The rest can wait until tomorrow."

    $ house.scene = "Kitchen, Afternoon"
    $ bg('tma')
    pause 0.6
    $ bg("kuhnya")
    show waldeck warm at waldeck_in
    $ play_music("m_teplo")
    with dissolve
    "I go into the kitchen for some water for the nursery, but end up lingering there far longer than I planned."
    wa "Won't you help?{w} An extra pair of hands is never unwelcome, and the cookies for tea won't shape themselves."
    ir "I'm afraid my hands weren't made for this."
    wa "No matter; Lizetta doesn't care whether a cookie is even or crooked, as long as it's sweet."
    "In the end I agreed to help, though at first we spend a little while in awkward silence, until it's broken by a remark of hers."
    wa "You know, you're not at all like the previous governesses."
    ir "How so?"
    wa "They counted the days until they left.{w} And now, it seems, for the first time in a long while, someone in this house isn't counting."
    "I don't know what to answer, because she's right, and I'm only noticing it myself just now."
    "We both laugh, not because the line is really funny, but simply at the flour on her cheek, at how clumsily I hold the dough cutter."
    "For a few minutes I almost forget what house I'm in."
    menu:
        "Take the last cookie to Lizetta.":
            $ house.pull("warm", "cookie", "doll")
            $ bg('tma')
            pause 0.6
            $ bg("detskaya")
            "I carry the saucer upstairs and set it on the windowsill by Lizetta's chair, where, it seems to me, it was always set before.{w} Frau von Waldeck follows and says nothing."
            "Only her eyes grow wet, and very grateful."
        "Eat it myself.":
            $ house.pull("cold", "cookie", "ate")
            "I eat it right there, by the stove.{w} It's still warm, and I'm almost ashamed of how good I feel."
            "Only afterward I notice: Frau von Waldeck never sat down.{w} She stood and watched me eat, with the face of someone who hasn't had the chance to watch that in a long time."

    $ bg ('tma')
    pause 0.6
    $ bg("stolovaya")
    pause 0.6
    $ table_cg("warm")
    wa "How is the story coming along?"
    ir "We got to the place where the girl finds the cottage in the forest.{w} Lizetta was waiting especially for that moment."
    "I say “Lizetta was waiting” without any irony, for the first time since I came here."
    wa "She always loved that part best.{w} The one about the cottage."
    $ table_cg("warm")
    wa "I think she likes you.{w} She's never been so calm with a new person before."
    ir "I think so too."
    "For a while we eat in silence, and the quiet between us sounds almost like a family's."
    "She clears the dishes from the table and lingers at the third place, the child's, as she does every evening.{w} Three days ago that gesture seemed alarming to me."
    "Today I look at it and feel nothing but a soft, familiar picture."
    $ bg("tma")
    call interlude(4) from _call_interlude_3
    jump day5

label day5:
    $ house.day = 5
    call day_card("Day Five", "Repetition") from _call_day_card_4

    $ house.scene = "Morning, Dining Room"
    $ bg("stolovaya")
    pause 0.6
    $ play_music("m_dom")
    "I wake without much trouble.{w} Already a habit, somehow of its own accord."
    $ table_cg("neutral")
    wa "Good morning.{w} This bread again..."
    wa "I keep threatening to change the baker, and never do."
    ir "I think it gets better every time."
    "Strange, how quickly this room has become familiar to me.{w} The place of the candle on the table."
    "The creak of the third chair if it's bumped by accident.{w} Even the moment when Frau von Waldeck will reach for the teapot, I know it ahead of time, by a second."
    wa "You know, I thought, if the rain doesn't return this week, we could take Lizetta out into the garden.{w} She likes to be wheeled out to the roses."
    ir "I'd be glad to help.{w} Is the chair heavy?"
    wa "You agree remarkably quickly to anything to do with Lizetta."
    "I want to laugh it off and say something like “it's part of the wages,” but I suddenly realize, unexpectedly, that she's telling the truth."
    ir "I simply like her.{w} That's all."
    wa "And the linen in the cupboards ought to be sorted, moths got in last year.{w} Would you care to help one of these days?"
    ir "Of course I'll help.{w} Only give me notice, because I sometimes lose track of the days here."
    "I say it lightly, but at once I catch myself: I've told the plain truth."
    wa "Ah, we all lose track.{w} Especially in winter, when one day can't be told from another."
    wa "Never mind, you'll get used to it."

    $ house.scene = "Stairs, Between Floors"
    $ bg("tma")
    pause 0.6
    $ bg("koridor")
    "I climb the stairs, and halfway up, for no reason at all, I shift my book from my right hand to my left to take hold of the banister,"
    "and only after I've done it do I realize I made exactly the same movement on exactly the same step yesterday."
    "I count the step, the eighth from the top.{w} I don't like how easily that number comes to mind, as if I'd counted it many times before."
    menu:
        "Turn around and look down.":
            $ house.pull("warm", "stairs", "looked")
            "I turn.{w} Below, at the foot of the stairs, stands Frau von Waldeck, looking up at me with such a calm, contented face, as though I were doing something right."
            "She smiles and raises a hand, either to wave or to straighten my collar, which can't be reached from there."
        "Quicken my pace and not look back.":
            $ house.pull("cold", "stairs", "ran")
            $ play_sfx("z_shagi")
            $ award("half_step")
            "I quicken my pace without turning.{w} Behind me I at once hear other footsteps, softer than mine, exactly in time, lagging half a step behind."
            "When I stop, they stop a little later.{w} I hear no menace in them, only patience."
    "For a second I stand still.{w} Then I simply go on climbing."

    $ house.scene = "Nursery, The Story (continued)"
    $ bg("tma")
    pause 0.6
    $ bg("detskaya")
    show lizetta at lizetta_pos
    with dissolve
    if house.mem.get("cookie") == "doll":
        "The saucer on the windowsill stands in the same place.{w} There's no cookie on it, and one crumb lies on the edge."
        "Frau von Waldeck must have cleared it away.{w} Must have."
    call lesson_open(5) from _call_lesson_open_3
    ir "Well, shall we go on with the cottage in the forest?{w} “The girl finished her supper and felt her eyes growing heavy."
    ir "She lay down on a little bed by the wall and fell asleep...”"
    ir "“...and when she woke, she found that the cottage was not empty after all.{w} At the table where her supper had been, an old woman sat knitting."
    ir "‘Don't be afraid, child,’ said the old woman.{w} ‘This house loves guests who come and stay...’”"
    ir "“‘And if I don't want to stay?’{w} asked the girl."
    ir "The old woman smiled, but did not answer...”"
    pause 1.0
    "What if I...{w} no, nonsense."
    "I'm only tired; almost a week without a single truly free day will tell on anyone."
    "I go over everything strange that has happened these days.{w} Each incident can be explained on its own, but..."
    "Together they form a pattern I don't like.{w} And yet it is so warm here."
    "Here I'm expected at breakfast and people are glad when I agree to help with the housework."
    "The thought that something is wrong with me seems far away today, as though it belonged to someone else."
    ir "I think we'll stop there.{w} The rest can wait until tomorrow."

    $ house.scene = "Garden, A Walk"
    $ bg("tma")
    pause 1.0
    $ bg("sad")
    "There's no rain, and Frau von Waldeck reminds me of her promise from this morning.{w} Together we carry Lizetta's chair out into the garden: she holds the back, I take the legs."
    "The chair turns out to be quite light.{w} The hardest part was carrying it past the closed doors."
    "We set it down by the rosebush, on the only dry spot.{w} The last blooms have almost fallen, but one, the most stubborn, still clings low to the ground."
    wa "She likes to be brought out here.{w} She says you can hear the grass growing."
    "“She says.”{w} I don't correct her, but I don't agree aloud either."
    "Frau von Waldeck cuts the stubborn flower and tucks it into the folds of the doll's dress.{w} Her movements are soft, practiced, the way one does what one has done many times."
    wa "She used to choose herself which rose to cut.{w} It was so long ago that sometimes it seems it never happened."
    "I look at the rose, then at the doll, and suddenly think that from outside we must look like three women in a garden."
    "The thought doesn't frighten me, and that is exactly what is strange."
    "I carry the chair back so carefully, as though someone were sitting in it.{w} Frau von Waldeck silently holds the door for me."

    $ house.scene = "Evening, Dining Room"
    $ bg ('tma')
    pause 0.6
    $ bg("stolovaya")
    $ table_cg("tense")
    $ play_music("m_trevoga")
    wa "You're quiet today, Fräulein."
    ir "I was lost in thought.{w} Forgive me."
    wa "Don't apologize.{w} I spend half my days in my own thoughts."
    wa "This room encourages it, I noticed long ago."
    "I want to ask her outright whether she feels what I feel, whether she ever notices"
    "that the days here wear into one another, but instead I only nod and go on eating."
    menu:
        "Slide the bread dish toward her.":
            $ house.pull("warm", "dinner", "bread")
            "I slide the bread dish toward her, just to do something with my hands.{w} She lays her hand over mine and for a few seconds doesn't take it away."
            "Her hand is warm and very light, as if it weighs almost nothing.{w} “Thank you,” she says."
            "“No one has handed me bread in a long time.”"
        "Watch the candle.":
            $ house.pull("cold", "dinner", "candle")
            "I watch the candle flame, the one thing in the room that ought to tremble.{w} Cold seeps in through a crack in the frame, yet the flame stands straight, as if painted."
            "I don't look away for a long time, and neither does Frau von Waldeck."

    $ house.scene = "Irene's Room, Evening"
    $ bg('tma')
    pause 0.6
    $ bg("komnata_irene")
    $ play_music("m_noch")
    "I go up to my room and sit down to write a letter, though I haven't decided yet to whom, and the first thing I do is pull out the desk drawer for a clean sheet."
    "Among the clean sheets I find a folded piece of paper already covered in my own handwriting.{w} The characteristic slant, the way I always press too hard on the crossbar of my t's."
    "But I don't remember writing this."

    $ house.scene = "The Letter"
    "“...she sat in the same place as always, and I read to her again, and again the candle made it warm, and I was at peace in a way I haven't been for a very long time."
    "I don't want to think about what came before this house.”"
    "The date on the letter is today's, the handwriting even, without a single blot.{w} I haven't left the nursery or my room all day, except for the dining room and the garden."
    "I don't remember ever sitting down at this desk before."
    "I don't even know what to think about it."
    "I put the letter back in the drawer.{w} The clean sheet I originally reached for stays where it was, untouched."
    "I blow out the candle without having written a single line to anyone."
    $ bg("tma")
    call interlude(5) from _call_interlude_4
    jump day6

label day6:
    $ house.day = 6
    call day_card("Day Six", "The Name") from _call_day_card_5

    $ house.scene = "Morning, Dining Room"
    $ bg("stolovaya")
    pause 0.6
    "The morning is colder than usual."
    $ table_cg("neutral")
    wa "Good morning.{w} How did you sleep?"
    ir "Well, thank you."
    wa "I think there will be a letter from Greta today.{w} She usually writes around this time of the month."
    "It's the first time I've heard the name spoken aloud; until now it had appeared only in letters."
    "I already know who Greta is, but I want to hear it from her."
    ir "Is she... a relative?"
    wa "My daughter.{w} She has lived in the city for several years now."
    ir "So you have two daughters."
    wa "Yes."
    "She doesn't develop the subject.{w} The silence lasts longer than the earlier pauses at the table."
    ir "You must miss her."
    wa "I do.{w} Though, to be honest, I miss her as she was before she left, not the one who writes me these dry, anxious letters now."
    wa "Forgive me.{w} Not the most suitable subject for breakfast."
    "I want to tell her the subject seems perfectly suitable to me.{w} But instead I only nod and change it myself, asking about today's weather."

    $ house.scene = "Nursery, Lesson"
    $ bg("tma")
    pause 0.6
    $ bg("detskaya")
    show lizetta at lizetta_pos
    with dissolve
    call lesson_open(6) from _call_lesson_open_4
    ir "“The old woman went on knitting and knitting, and with every row the cottage seemed a little smaller and the girl a little larger.{w} ‘What are you knitting?’"
    ir "asked the girl.{w} ‘You, child,’ replied the old woman."
    ir "‘You, so that you'll fit this place more exactly...’”"
    show waldeck warm at waldeck_in
    with dissolve
    wa "Greta, your voice sounds a little different today."
    $ name_choice = renpy.call_screen("timed_choice", [("Look her in the face.", "look"), ("Lower my eyes to the book and keep reading.", "book")], 5.0, "book")
    if name_choice == "look":
        with blink
        $ house.pull("cold", "name", "looked")
        $ play_music("m_trevoga")
        $ house.name_look = True
        $ house.name_state = "cut"
        "I look at her directly, searching for a slip, embarrassment, anything.{w} Nothing."
        "Her face is calm and warm, like that of someone who has said the only right word.{w} It chills me more than any mistake could."
    else:
        $ house.pull("warm", "name", "book")
        $ play_music("m_dream")
        $ house.name_state = "greta"
        "I lower my eyes to the page.{w} The name settles on my shoulders like someone else's cloak, but a warm one, a perfect fit, as though it had been sewn long ago and was waiting for me to come."
    $ award("stranger_name")
    $ drift_history()
    $ renpy.block_rollback()
    ir "Hm?{w} Forgive me, I was just lost in thought."
    $ house.name_state = "normal"
    wa "It's quite all right.{w} You do so much good for her, you know that."
    hide waldeck
    with dissolve
    ir "“The girl did not understand what the old woman meant, but for some reason she wasn't frightened.{w} ‘Stay until morning,’ said the old woman, ‘and then you can decide...’”"
    ir "I think that's enough for today."
    "Wait.{w} What did she say?"
    "I replay it in my head: “Greta, your voice sounds a little different today.”{w} Greta."
    "The only thought in my head was that I hadn't even asked her to repeat it.{w} Hadn't corrected her."
    "Because in that second I didn't want to be Irene."

    $ house.scene = "Corridor, After the Lesson"
    $ bg("tma")
    pause 0.6
    $ bg("koridor")
    "The clock has stopped again.{w} I wound it, after all."
    "With my own hands."
    "The linen we meant to sort lies untouched.{w} Frau von Waldeck didn't remind me, and I didn't ask."
    "I reach for the key on its chain and at the last moment stop my hand.{w} I don't want to mend what's broken in this house, not today at least."
    $ bg("tma")
    pause 0.6
    $ bg("detskaya")
    "On the little table in the nursery lies an envelope addressed to me.{w} The handwriting is the same as on the envelope in the dining room; I recognize it before I read the address."

    $ house.scene = "The Letter"
    "“Fräulein Irene,{w} forgive me for writing to someone I have never seen, but my mother mentioned your name in her last letter, and I can't stay silent."
    "I don't know what you've been told about this house, but I beg you not to linger there longer than necessary."
    "I lived in it long enough to know how easily you stop noticing how much time has passed.{w} Mother will do you no harm, she simply... doesn't let go."
    "And somehow the house helps her in this.{w} Please leave while you can still say the word ‘leaving’ and remember why you are saying it."
    "Greta”"
    "I read it three times in a row.{w} Each time it frightens me a little less, not a little more, and that is exactly what ought to frighten me most."

    $ house.scene = "Evening, Dining Room"
    $ bg ('tma')
    pause 0.6
    $ bg("stolovaya")
    $ table_cg("sad")
    $ play_music("m_trevoga")
    wa "A letter came from Greta, as I said it would."
    ir "Yes.{w} I received it."
    wa "She always worries so about me.{w} City life makes people anxious, I think."
    ir "Perhaps."
    "I want to ask her outright, about the name, about the chair behind the wardrobe, about the three years in the letter, and in the end I ask none of it."
    "I'm not afraid of her answer.{w} Rather, I'm afraid of mine."
    "If she were suddenly to ask me in return why I didn't correct her back then, in the nursery."

    $ house.scene = "Irene's Room, Night"
    $ bg('tma')
    pause 0.6
    $ bg("komnata_irene")
    $ play_music("m_noch")
    "I lie there and go over the whole day again in my mind."
    "Again and again that remark of hers surfaces, tossed off quite casually, the way one speaks of any other everyday thing."
    "I try to catch in memory even a shadow of surprise on her face and find none.{w} As though, in her view, that name had long and wholly belonged to me."
    "But what troubles me more is my own silence in answer to her slip.{w} Have there been times before when someone called me by the wrong name and I corrected them at once?"
    "There have, of course there have."
    "So it isn't that I've forgotten how to correct people.{w} What I first thought was wrong: the truth is that in that room, in that second, I didn't want to be Irene."
    "I wanted, if only for a minute, to be someone else.{w} Someone who is expected."
    "Someone who is recognized.{w} Someone who doesn't have to be explained again to every new person."
    "It was easier than remaining myself."
    $ bg("tma")
    call interlude(6) from _call_interlude_5
    jump day7

label day7:
    $ house.day = 7
    $ drift_history()
    call day_card("Day Seven", "Departure") from _call_day_card_6

    $ house.scene = "Morning, Irene's Room"
    $ bg("komnata_irene")
    "The contract was for a week's trial.{w} This morning a cart is to come for me and take me back to the ford, if I decide I don't want to stay any longer."
    "I've been standing over my suitcase for a good five minutes without putting anything into it."
    "I reread Greta's letter once more.{w} The line about how you “stop noticing how much time has passed”, I understand it far better now."
    "She's right.{w} The days here truly are so alike that this morning, for a second, I couldn't remember whether it was the sixth day or the third."
    "I could leave.{w} The cart will come, I'll climb in, return to the city, find another post."
    "I'm not afraid of staying.{w} What frightens me far more is going back to where I came from, where I'd have to be a person with a past that has to be remembered whole."
    "Here I don't have to remember that I failed to watch my brother on the shore, on that August day three years ago.{w} Here it's enough to read a story aloud and pour tea into a small cup."
    "Three years.{w} Exactly as long as a place has been laid every evening in this house for someone who doesn't sit at the table."
    "I put a dress and a book into the suitcase.{w} My hands stop there again."

    $ house.scene = "At the Window, Waiting"
    "I go to the window and stand there a while, looking at the road, which is still empty.{w} It's strange to remember how it looked to me on the first day."
    if persistent.loops == 0:
        $ play_music("m_lullaby")
        $ recalled = set()
        $ memory_pick = ""
        while memory_pick != "done":
            python:
                items = [(__(MEMORIES[key][0]), key) for key in MEMORIES if key in house.mem and key not in recalled]
                if len(recalled) >= 2:
                    items.append((__("Enough."), "done"))
            $ narrator(__("I go over everything that happened."), interact=False)
            $ memory_pick = renpy.display_menu(items)
            if memory_pick == "done":
                "Enough.{w} All of it has already fallen into a pattern."
                "The only question is what I will do with it."
            else:
                $ recalled.add(memory_pick)
                $ narrator(MEMORIES[memory_pick][1][house.mem[memory_pick]])
    "From below comes the sound of wheels on gravel.{w} The cart has come sooner than I managed to decide."
    "I go down."

    $ house.scene = "Dining Room, Noon"
    $ bg ('tma')
    pause 0.6
    $ bg("stolovaya")
    $ table_cg("neutral")
    wa "The cart has come.{w} It's your decision, Fräulein."
    ir "I've been thinking about it all morning."
    $ table_cg("sad")
    wa "I won't try to persuade you.{w} This is not the cheeriest place for a young woman."
    ir "May I ask you something before I decide?"
    wa "Ask."
    ir "Yesterday, in the nursery.{w} You called me by another name."
    $ table_cg("tense")
    wa "Did I?{w} I don't remember that."
    "She says it without any lie in her voice, as if she truly doesn't remember.{w} It frightens me more than a direct admission would have."
    ir "It doesn't matter.{w} I must have misheard."
    "We both know I didn't.{w} But we both decide not to pursue it."
    $ play_sfx("z_loshadi")
    wa "The driver will wait.{w} I pay him separately for it."
    ir "So I'm not the first to hesitate so long on the threshold."
    wa "Not the first.{w} But perhaps the first in a long while who hesitates not out of pity for me."
    ir "Allow me to go upstairs for a few more minutes."
    wa "Of course.{w} I'll wait here, along with the driver."

    $ house.scene = "Nursery, Finale"
    $ bg("tma")
    pause 0.6
    $ bg("detskaya")
    $ show_cg("cg lizetta closed")
    $ play_music("m_final")
    "I approach the armchair for the last time, or perhaps not the last, I still haven't decided, and sit down beside it, as I've done every day this past week."
    "I glance toward the second chair behind the wardrobe, still covered with its cloth.{w} I don't lift the cloth."
    "I only look for a couple of minutes before turning away."
    "The room looks exactly as it did on the first day.{w} Only the light is different now, soft, even, midday light, in which everything is perfectly clear."
    menu:
        "Take the doll's hand.":
            $ house.pull("warm", "hand", "held")
            "I take the porcelain palm in mine.{w} It isn't cold, as porcelain should be; it's warmed by the sun, or by me, or by something else."
            "I don't want to find out by what."
        "Rest my hand beside hers, without touching.":
            $ house.pull("cold", "hand", "near")
            "I lay my hand on the armrest next to hers, not touching.{w} Between our fingers there is just enough space to disturb nothing, and still it seems occupied by someone."
    ir "You know, Lizetta, I never did finish that story for you."
    if house.greets >= 3:
        "My hand finds the fold before I can think.{w} I've greeted this chair so many times that my hand has learned how to treat it."
    else:
        "My hand reaches for the fold and I can't stop it in time.{w} Though I tried, all these days."
    "I smooth the fold in the doll's dress, with the same gesture Frau von Waldeck has used since the very first day."
    ir "Remember how the old woman knitted, and the girl didn't understand why?{w} Maybe I don't have to understand why, either."
    ir "You won't miss me, will you, if I leave after all?"
    "Silence.{w} A foolish question, but I need to hear how it sounds aloud."
    ir "You know, it seems only yesterday I was called by a name that wasn't mine for the first time, and I didn't correct it.{w} Perhaps I should have."
    ir "Perhaps it isn't too late."
    if house.name_look:
        "I was looking her in the face and saw that it wasn't a slip.{w} That is what's frightening."
    else:
        "I never even raised my eyes.{w} The name was so warm that I said nothing."
    "I don't know whether she ever truly heard me.{w} Was anything in this house real?"
    "Or is it all something I built up in my own head, because I needed there to be something here worth lingering for beyond the allotted time?"
    "To tell the truth, I'm no longer sure it matters so much that I know."
    if house.lean == "warm":
        "I feel good here.{w} So good that it frightens me a little, and still I don't want to leave."
    elif house.lean == "cold":
        "I'm afraid here.{w} And somehow that is exactly why I can't leave: at least what's frightening stays put and waits."
    else:
        "I feel both good and afraid here.{w} One doesn't cancel the other, and I no longer try to choose."
    "I open the book at the marked page and begin to read aloud, quietly, calmly, without a note of the irony with which my first day in this house began."
    ir "“...and then the girl understood that the cottage in the forest had not been empty all those years, but only waiting for someone to want to live in it again...”"
    window hide
    if persistent.loops >= EYES_OPEN_AT:
        pause 4.0
        $ show_cg("cg lizetta open", Dissolve(3.5))
        pause 4.0
    else:
        pause 1.5
    $ persistent.loops += 1
    $ persistent.last_lean = house.lean
    $ config.allow_skipping = True
    if house.lean == "warm":
        $ award("warm_house")
    elif house.lean == "cold":
        $ award("cold_house")
    if persistent.loops >= 2:
        $ award("full_circle")
    $ renpy.save_persistent()
    $ bg("tma")
    $ s_big = 84
    $ end_title = __("The End")
    show text "{size=[s_big]}[end_title]{/size}" at card_in
    pause 4.0
    hide text
    $ renpy.with_statement(Dissolve(1.5), always=True)
    return