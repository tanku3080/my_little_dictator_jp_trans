
#######  ENDINGS  ########

label bad_ending1:
    play soundfx "se/cave.ogg" fadein 3.0    
    scene tunnel
    with fade
    play music "music/horror.ogg"
    play sound6 "se/prison_door.ogg"
    
    "Some time later . . . who knows when . . . I wake up on the concrete floor of a dark cell."
    me "Oww . . . my head."
    "Rubbing the wound on my forehead, I try to sit up."
    gestapo determined "Finally awake, are we?"
    "Through a pair of iron bars, a cocky young officer smirks at me, brandishing a pair of leather gloves."
    me "W-Who are you guys? What's going on?"
    
    play silsound2 "se/silly12.ogg"
    
    gestapo "Us? We're the {i}Goosetapo{/i}. And we're the last people that will see you alive, Commander Yamato."
    "The {i}Goosetapo{/i} are Germania's secret police force, responsible for spying on, and interrogating, suspect citizens."
    me "What is this? You have to let me go. I didn't do anything!"
    gestapo "You insulted the Füühbar and disobeyed orders. That's pretty treasonous behavior."
    "Just because I turned down a request, she threw me in prison to be tortured?"
    me "I apologize, I didn't mean . . . I just want to go home."
    gestapo "Don't you get it yet? This is it for you. Nobody turns down Adorofia Hitora and lives."
    me "W-What?"
    
    play silsound3 "se/silly17.ogg"
    
    gestapo "You'll be shot at dawn. That's the end of the matter. Bet you feel stupid now."
    
    play sound4 "se/metal_steps.ogg"
    
    "The young {i}Goosetapo{/i} officer turns around and begins to walk away."
    gestapo "Oh, and it's going to be liver and sausage for your final dinner."
    
    play sound6 "se/prison_door.ogg"
    
    "With a loud slam, he goes through a heavy metal door and I'm left in silence."
    me "Well . . . that's the end of me . . ."
    
    stop soundfx fadeout 3.0
    stop music fadeout 3.0
    scene black
    with fade
    
    $ achievement.grant("ENDING_BADENDING1")
    $ achievement.sync()
    
    jump game_over

label bad_ending2:
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    stop soundfx3 fadeout 3.0
    stop soundfx4 fadeout 3.0
    stop sound2 fadeout 3.0
    stop sound3 fadeout 3.0
    stop sound4 fadeout 3.0
    stop sound5 fadeout 3.0
    scene black
    with fade
    
    "But as time passes, I find I can't keep up the farce."
    "The inner circle, Altberlin, the tactics, the meetings, the politics, the lying and the deceit . . ."
    "We fight battle after battle, bombing cities full of civilians and destroying peaceful nations."
    "Tanks, planes and soldiers flood across borders, incinerating towns, deporting dissidents, stealing resources . . ."
    "The Füühbar's lust for power knows no bounds."
    me "I can't go on like this. If I stay here, I'll be forced to chew on a cyanide capsule before the end . . ."
    "This is the Germanian empire I started to fight for . . . the one for which I was summoned to spy on."
    "I didn't realize the extent of its evil. And now I've had a hand in it. But no longer."
    "Not being able to stand the shame of it . . . not being able to stomach the fight or the duplicity."
    "In a cowardly manner, I resign my post and buy a one-way ticket back to Zipangu."
    "Sneaking aboard a ferry bound for Edooh, I feel the weight slipping from my shoulders as we steam across the oceans."
    "Perhaps my homeland will survive this global conquest yet . . ."
    
    $ achievement.grant("ENDING_BADENDING2")
    $ achievement.sync()
    
    jump game_over
    
label bad_ending3:
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    stop soundfx3 fadeout 3.0
    stop soundfx4 fadeout 3.0
    stop sound2 fadeout 3.0
    stop sound3 fadeout 3.0
    stop sound4 fadeout 3.0
    stop sound5 fadeout 3.0
    scene black
    with fade
    
    "Unable to fulfill my original duty and my mission, I leave for Zipangu."
    "Whatever happens to Sovia, to Germania or to the dictators . . . who cares. It's not my responsibility any more."
    "I soon learn about the attack on Amerika and the new world war about to begin."
    "Climbing aboard a train bound for the east, I feel the weight slipping from my shoulders."
    "Perhaps my homeland will survive this global conquest yet . . ."
    
    $ achievement.grant("ENDING_BADENDING3")
    $ achievement.sync()
    
    jump game_over
    
