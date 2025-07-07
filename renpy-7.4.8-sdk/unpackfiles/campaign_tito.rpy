#####################################################################################################################################################
#####################################################################################################################################################
###### TITO SIDE STORY ###########################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################

label campaign_tito:
    window hide
    stop music fadeout 1.0
    stop soundfx fadeout 1.0
    stop mmsound fadeout 1.0
    stop mmsound2 fadeout 1.0
    $ _window_during_transitions = False
    $_game_menu_screen = "save_screen"
    if level_choice == 1:
        $ save_name = "Il Douche's Folly (Easy)"
    elif level_choice == 2:
        $ save_name = "Il Douche's Folly (Normal)"
    else:
        $ save_name = "Il Douche's Folly (Expert)"
    $ store.text_history_enabled = True
    $ mouse_visible = False
    scene black
    with dissolve2
    pause 0.1
    
    jump sc0000208

#####################################################################################################################################################
#sc0000208	-	Wavell retakes Gypta from Graziani
#####################################################################################################################################################
label sc0000208:
    scene black
    with fade
    
    $ mouse_visible = False
    show expression Text(_("At the fortified line outside Zidiparrani, Gypta . . ."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx "se/wind.ogg" fadein 3.0
    play soundfx2 "se/tank_invasion.ogg" fadein 3.0
    play soundfx3 "se/battle4.ogg" fadein 3.0
    play sound3 "se/boom.ogg"
    play sound4 "se/boom2.ogg"
    scene desert_smoke
    with hpunch
    with vpunch
    play music "music/glory.ogg"
    
    "A loud explosion rips through the desert sands and debris is sent scattering everywhere."
    
    show object_desertbritannia at tankpos
    with dissolve
    
    "On the border with Vitalian-held Zidiparrani, Britannian troops pour over the frontier wire, smashing the defenses."
    "{i}Ducky{/i} tanks blast at the walls of the seaside resort, forcing the defenders back towards the sea." 
    "Late last night, the {i}BRAF{/i} bombed and strafed Vitalian airfields as Zidiparrani was shelled from the sea."
    "The surprise attack leaves the Vitalians shaken and confused . . ."
    
    hide object_desertbritannia
    with dissolve
    show vitalia shock
    with dissolve
    play silsound2 "se/poke.ogg"
    
    vitaliasol "W-What? What's happening?"
    "The regulars and {i}Blackskirt{/i} divisions stumble around the trenches, dumbfounded by the early counterattack."
    vitaliasol "Wavell . . . she's finally fighting back . . ."
    "Fear spreads among the ranks as they're outflanked and overrun by the enemy."
    
    play sound5 "se/run.ogg"
    play sound4 "se/dash.ogg"
    hide vitalia
    with easeoutleft
    
    "In a panic, the Vitalian soldiers retreat, abandoning their positions and heading back inland, towards Fort Kaputz."
    vitaliasol shock "Back to Cyracana! Run! Run away!"
    "Desperate reports come in over the wire from other areas, at Bineiwa, the Muttars, Maxtila, Bug Bug and Zovavi."
    "The line that Graziani spent weeks preparing, in anticipation for reinforcements, has buckled under the onslaught."
    "Within minutes, Zidiparrani falls to the enemy . . ."
    
    show wavell determined
    with dissolve
    
    wavell "Today, we're reclaming our lands for the Britannian empire!"
    "Commander Wavell proudly leads the Britannians into battle, reclaiming the border towns for the Gyptan colony."
    wavell "Dummy tanks were set up in the desert to distract and draw away the enemy's attention! Genius!"
    "Thanks to the quiet preparations over the past weeks, the surprise attack goes off without a hitch."
    
    show wavell happy
    with dissolve
    
    wavell "Be rough with the enemy. Use our tanks to the fullest. There is no room in war for delicate machinery."
    "The Vitalians do their best to evade capture, heading back to their bases beyond the old borders with Cyracana."
    "Eager to exploit the collapse of the line, the Britannians pursue eagerly, their tanks rolling over the deserts."
    "Finally, Wavell has struck back at Graziani's forces. Will the Vitalians be able to regain their footing?"
    
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    stop soundfx3 fadeout 3.0
    stop music fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000198

#####################################################################################################################################################
#sc0000198	-	Horthy agrees to join the {i}Axle{/i} / Celebration
#####################################################################################################################################################
label sc0000198:
    scene black
    with fade
    
    $ mouse_visible = False
    show expression Text(_("To the east, aboard a train in the nation of Hang . . ."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx "se/train.ogg" fadein 3.0
    scene train_country_travel
    with fade
    play music "music/zipangu.ogg"
    play sound4 "se/train_whistle.ogg"
    
    "Aboard a private locomotive, Horthy, leader of Hang, sits peacefully and stares out of the window at passing scenery."
    
    show horthy normal
    with dissolve
    
    hor "{i}Sigh{/i} . . . it sure is boring being so very neutral. Safe, sensible, but boring . . ."
    "Completely tired of the lack of action recently, she pouts a little and nuzzles a toy bear against her cheek."
    "The war has ravaged much of the rest of Europa, but this tiny pocket of countryside remains steady."
    "Hang, while friendly and a great trading partner of Germania, has yet to commit itself as an ally to either side."
    
    play sound2 "se/doorslide.ogg"
    
    teleki happy "Although, maybe that's not such a bad thing, my liege."
    
    play sound4 "se/metal_steps.ogg"
    
    "Teleki, her First Minister, enters the carriage and comes towards his leader's compartment."
    teleki "It's true. The war is simply passing the nation by. Although, there have been some benefits to date."
    hor "What do you mean?"
    teleki "Well, the country has become rather more sizeable since the war began . . ."
    "Territorial disputes have been settled, with Horthy claiming land from weakened enemies in Rumanum and Czexa."
    "The size and wealth of Hang has increased exponentially, the more the Germanians have attacked their neighbors."
    
    show horthy determined
    with dissolve
    
    hor "But, don't you think it's boring? Just sitting around, trading, and growing fat?"
    teleki normal "I'm afraid I don't follow, your majesty."
    
    play silsound3 "se/silly9.ogg"
    
    hor "I'm saying, we should join the war, on Hitora's side. Actually do some fighting for once."
    teleki annoyed "What? What nonsense. Where'd you get a crazy idea like that?"
    hor "I thought of it all by myself."
    
    play silsound4 "se/silly8.ogg"
    show horthy shock
    
    teleki normal "Oh, I get it. You're cranky because you haven't had your afternoon nap yet . . ."
    hor "What? No, I'm not."
    teleki happy "I'll get the steward to heat you up some milk, and you can sleep here until we arrive back at the palace."
    
    show horthy determined
    
    hor "I'm not cranky!"
    
    show horthy shock
    
    teleki "Aww, you're so cute when you're tired, m'lady."
    hor "Geez . . . you never take me seriously."
    "Horthy pouts, disappointed that her adorable stature makes others take pity."
    
    show horthy determined
    with dissolve
    
    hor "Anyway, we already signed up to join the {i}Triple Pact{/i} in the coming weeks. I thought you'd support me on this."
    teleki annoyed "Taking land is one thing, but there's no chance I'd ever support that maniacal dictator girl in a war. It's madness."
    
    play silsound5 "se/silly17.ogg"
    show horthy shock
    
    teleki "I don't know what the rest of you all see in her . . . but there's something evil about that Hitora."
    hor "Teleki . . ."
    "Minister Teleki seems to be visibly on edge, shaking a little, desperately betraying his true feelings."
    
    show horthy normal
    
    teleki "Please, m'lady. I'm only looking out for you when I say this. But if we join Germania's war, it will bring us nothing but ruin."
    "Horthy carefully contemplates the situation, observing her First Minister's determination. He really dislikes Hitora."
    
    show horthy happy
    with dissolve
    
    hor "Thank you, for advising me and always being so honest, Teleki. I admire your conviction."
    teleki happy "M'lady."
    hor "I'm not particularly keen on becoming too close to Hitora either . . . regardless, I've already decided."
    teleki annoyed "Eh? Decided what, your highness?"
    
    show horthy moe
    with dissolve
    play silsound3 "se/silly17.ogg"
    play sound2 "se/battlecry.ogg"
    
    hor "No more sitting on the sidelines. We're going to enter the war against the {i}Alliance{/i} on the {i}Axle{/i} side!"
    "Other ministers, guards and soldiers in the carriage begin to cheer loudly at their sovereign's declaration."
    
    stop sound2 fadeout 3.0
    show horthy normal
    with dissolve
    
    teleki "But . . . but!"
    hor "Hmm? But what?"
    teleki normal "Nothing, just {i}'but'{/i}. I don't like it."
    
    play silsound6 "se/silly22.ogg"
    show horthy determined
    
    hor "Geez, you're the only butt here, Teleki."
    "Teleki sighs at the lame joke."
    
    show horthy happy
    with dissolve
    
    hor "Anyway, joining the {i}Axle{/i} is good for Hang. We'll have improved trade with other nations in the pact . . ."
    hor "Our territorial gains will be more solid. They won't just go to Rumanum or Serpana on a whim. The army will expand . . ."
    hor "And . . . it might actually keep Adorofia Hitora off our backs. That's what you want, isn't it?"
    teleki annoyed "You're going to enter into a close alliance in order to keep our distance from them? How does that work?"
    
    show horthy determined
    with dissolve
    
    hor "I know it doesn't make sense on the surface . . ."
    hor "But I've found that if you give Hitora what she wants, even if she's still not satisfied, she soon moves on."
    teleki "And if you don't give her what she wants, she becomes bloodthirsty and reckless?"
    "They're certainly under pressure, caught between a rock and an even harder rock."
    teleki normal "So, what can we do?"
    
    play silsound4 "se/silly6.ogg"
    show horthy happy
    
    hor "The point is, when a bully wants to be your friend, act cute and play along. Then, they'll pick on the other kids instead."
    teleki annoyed "That's so messed up . . ."
    "Still, Horthy makes a salient point. It's not like they have much choice, surrounded by big players in this war."
    "Hang needs to choose a side and start fighting for its future in the new world order."
    
    show horthy moe
    with dissolve
    
    hor "You know, I think I'll have that warm milk after all. It's getting quite cosy in here."
    teleki normal "Yes, m'lady. I'll sort that for you right away."
    "Resting her head against the cushioned seats, Horthy closes her eyes and relaxes."
    "Waiting for a few moments before meeting the steward, Teleki cautiously watches his leader recline."
    teleki annoyed "{size=-6}Damn you, Hitora . . . you'll corrupt all that's good about this world . . .{/size}"
    
    play sound3 "se/metal_steps.ogg"
    play sound2 "se/doorslide.ogg"
    
    "Exiting the carriage, the First Minister sets about his duties, still sore over the direction of his nation."
    "Hang is going to join the {i}Axle{/i} cause, alongside Germania and Vitalia. In time, they may begin to fight."
    "Will Horthy be able to last as a military leader among the other giants? Has she saved her country from doom?"
    hor "Mmmm . . . Teleki, pass the {i}arany galuska{/i} . . ."
    "Or will this alliance only make things worse for the continent?"
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000200
    
#####################################################################################################################################################
#sc0000200	-	Antoness gets rid of Garol / Loses all the money
#####################################################################################################################################################
label sc0000200:
    scene black
    with fade
    
    $ mouse_visible = False
    show expression Text(_("Meanwhile, in the eastern nation of Rumanum . . ."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx "se/room.ogg" fadein 3.0
    scene mansion_room
    with fade
    play music "music/evil.ogg"
    
    "In the newly-occupied Vlasia Palace, {i}Canineducator{/i} Antoness meets with her close confidante Cshima."
    
    show antoness happy at left35
    show sima determined at right35
    with dissolve
    
    anton "King Garol has abdicated in favor of his daughter Michelle, and agreed to go into exile . . ."
    sima "The {i}Furry Guard{/i} has a tight control over the countryside and the cities . . ."
    anton "And I, Antoness, am {i}Canineducator{/i} of all Rumanum!"
    "The small, furry critter marvels at the immense power she holds. Nothing can stand in her way now."
    
    show antoness insane
    with dissolve
    play silsound5 "se/silly17.ogg"
    
    anton "Together, we will form a new regime, right here, in the heart of Rumanum . . . the {i}National Legendary State{/i}."
    "A new extremist government and regime for Rumanum, to restore military glory to the country and enter into new alliances."
    anton "All pacts and agreements signed by Garol are now null and void. Rumanum will chart a new course, as an ally of Germania."
    sima "We can sign new trade deals, join the new {i}Triple Pact{/i} and have Adorofia Hitora teach us about {i}blitzkrieg{/i}."
    "Turning their backs on Serpana and the western {i}Alliance{/i}, the {i}National Legendary State{/i} will grow closer to the {i}Axle{/i} instead."
    "Under the new state, Antoness will remain as {i}Canineducator{/i}, with Cshima as {i}Deputy Canineducator{/i}, leader of the {i}Furry Guard{/i}."
    anton "We will be swift, be just and recognize that, over all ambitions, intrigues and hatred, there is the motherland . . ."
    
    show sima normal
    show antoness normal
    with dissolve
    
    sima "What's going to happen to King Garol now that he's abdicated?" 
    
    show antoness happy
    
    anton "We put him on the royal train last night and sent him out of the country. I even offered protection and guards for the trip."
    "Just to make sure that Garol actually left the nation in one piece . . ."
    anton "Hopefully, we can wipe out the corruption of the royal family now and start over . . ."
    
    show sima happy
    
    sima "We can even use all the funds from the royal treasury to help rebuild this country and reform the economy."
    
    show antoness normal
    show sima normal
    
    anton "Well, not all of them. I promised Garol he could take some treasure with him, you know, to start over."
    
    play silsound2 "se/silly7.ogg"
    show sima shock
    
    sima "Wait . . . you let the king take whatever he wanted from the royal treasury?"
    "Garol, a man known for his absent-minded corruption and deceit, was allowed access to the country's finances before he left."
    
    stop music fadeout 5.0
    
    "This can't be good news."
    anton "Huh? What's wrong? I'm sure he only took enough to get by . . ."
    
    play music "music/drama.ogg"
    play sound3 "se/door3.ogg"
    play sound4 "se/run.ogg"
    play sound2 "se/dash.ogg"
    hide sima
    with easeoutright
    
    "In a panic, Cshima rushes out of the room and through the opulent halls, towards the royal treasury."
    "A few moments later, there's a panicked shriek from down the corridor."
    
    play silsound5 "se/silly12.ogg"
    show antoness shock
    
    sima shock "It's gone! It's all gone! Everything . . ."
    anton "H-Huh? {i}'All gone'?{/i} What do you mean?"
    
    play sound2 "se/walk.ogg"
    show sima shock at right35
    with easeinright
    
    "Slinking back into the room, Cshima has a ghostly expression on his face."
    
    play silsound3 "se/silly1.ogg"
    show antoness moe
    
    sima "We've been robbed blind. The treasury is completely empty . . . all because . . ."
    
    show sima determined
    with dissolve
    
    "Cshima's face darkens as he rounds on Antoness."
    
    play silsound4 "se/poke.ogg"
    
    sima "You dumb dog! Garol took all the gold with him! There's nothing left in the country's coffers."
    
    show antoness angry
    
    anton "Well, I didn't think he'd actually take it all. I thought he'd leave us something at least . . ."
    "A king forced into abdication and exile, known for his bad spending habits, has robbed Rumanum of its finances."
    
    show sima shock
    
    sima "We'll go bankrupt before the year is out . . . all those economic programs . . . gone."
    
    show antoness shock
    
    anton "Don't worry about it. I'm sure we'll work something out. Maybe Garol will return the money?"
    "Like a dog trusting her former master, Antoness still seems to hold some hope for her old sovereign."
    "That's partially why she became {i}Canineducator{/i} - she's part of the old regime, a monarchist, less radical than the {i}Furry Guard{/i}."
    
    play silsound4 "se/silly21.ogg"
    show antoness moe
    show sima determined
    
    sima "You think he's going to return the money? How can you be so naive?!"
    anton "N-Naive?! Who are you calling naive?"
    
    show sima shock
    
    sima "You're a dog! You chase your own tail, for god's sake! Of course you're naive!"
    
    play silsound6 "se/silly11.ogg"
    show antoness angry
    
    anton "Well, this dog is {i}Canineducator{/i} of Rumanum now, so you better get used to it!"
    
    show sima determined
    with dissolve
    
    sima "{size=-6}Hmm, well, we'll see about that . . .{/size}"
    "With King Garol out of the picture, it's now up to Antoness to bring glory to Rumanum and its people . . ."
    "However, the {i}Furry Guard{/i} have other concerns, beginning campaigns of terror and pogroms across the country."
    "Bankrupt, leader of the military and reliant on a vascist political faction, the {i}Red Dog's{/i} troubles are only just beginning . . ."
    
    stop soundfx fadeout 3.0
    stop music fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000197

#####################################################################################################################################################
#sc0000197	-	Churchill and Battenia discuss Grecia / British forces moving in
#####################################################################################################################################################
label sc0000197:
    scene black
    with fade
    
    $ mouse_visible = False
    show expression Text(_("Meanwhile, in the Britannian isles, in the capital city Albion . . ."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx "se/birds.ogg" fadein 3.0
    scene albion_day
    with fade
    play music "music/teatime.ogg"
    
    "After a dangerous few weeks, the threat of invasion has evaporated, leaving Britannia in a safer position."
    "While nightly bombing raids continue, the {i}Alliance{/i} maintains air supremacy and can now focus on other fronts."
    "In the streets of Albion, the First Minister Churchill meets with Lady Battenia at their usual spot on Albion Bridge."
    
    play sound4 "se/walk.ogg"
    show churchill hat determined at left35
    show battenia normal at right35
    with dissolve
    
    ch "Finally . . . the Battle of Britannia is over."
    batt "And it's all thanks to Stuffy's brave airmen in the {i}BRAF{/i}."
    ch "Never was so much owed by so many to so few . . . not to mention, we're having success elsewhere."
    ch "Wavell has launched the counterattack against Vitalia in Gypta. At long last, we're hitting back at them."
    "It's the first good news they've had in a while."
    
    show churchill hat moe4
    show battenia angry
    with dissolve
    
    ch "However, the Vitalian war against Grecia is developing into a drastic situation . . ."
    ch "Mussorinni's forces have converged beyond the borders of Epirus, and are pushing inland to meet with Papagos."
    batt "So, they've finally done it. War has come to the birthplace of western civilization itself . . ."
    "Considering the Britannian royal family has ties to the monarchy in Grecia, it's a country very dear to Britannia."
    "While not quite an official ally yet, Churchill has pledged to come to their side and help defend the nation if attacked."
    "Over the past months, a trade agreement was struck between both nations, allowing Britannia to use the Grecian merchant fleet."
    "Warships sailed deep into Galatian Waters, and exports to Germania were brought to an end."
    
    show churchill hat determined
    with dissolve
    
    ch "We've made further contact with the Grecian government and have offered military support, should they require it."
    
    play silsound3 "se/silly15.ogg"
    show battenia shock
    
    batt "Still . . . the Grecian-Vitalian war must be played very carefully. You need to be cautious Churchill . . ."
    batt "If it becomes a protracted conflict, there's nothing to stop it from leading to another proxy war between Britannia and Germania."
    ch "At this stage, we will simply offer aerial support and supplies, helping to keep Papagos and Metaxas going."
    
    show plane_wellington at tankpos
    with dissolve
    
    ch "The {i}BRAF{/i} are in position, with new aircraft at their bases in Maltana and Kyprosa, ready to strike when ordered."
    "In fact, the new runways put them within striking distance of the oil fields in Rumanum . . ."
    ch "If need be, Rumanum is the true target for our bombers. Those oil fields and fuel depots . . ."
    batt "Both Hitora and Starin are eyeing up Rumanum to fuel their future wars. If need be, we can put an end to it."
    
    hide plane_wellington
    with dissolve
    show battenia normal
    show churchill hat normal
    with dissolve
    
    ch "Still, another front. What is Mussorinni thinking, starting all these wars?"
    "Gypta, Zomali, Grecia . . . without finishing off the Britannians or winning once, the {i}Douché{/i} keeps initiating conflicts."
    
    show churchill hat happy
    
    ch "Let's just consider it a stroke of good fortune that she's overstretching her forces."
    ch "By fighting on many fronts, the {i}Axle{/i} will be distracted, reducing their overall effectiveness in Europa."
    "It's an opportunity that the {i}Alliance{/i} cannot miss."
    ch "That's where we should focus our efforts, Battenia. Vitalia. It is the soft underbelly of the {i}Axle{/i} . . ."
    
    show battenia happy
    with dissolve
    play silsound4 "se/silly20.ogg"
    
    batt "Then let's do our best to break Mussorinni's invasion in Grecia and send her packing!"
    "Battenia gets fired up, excited by the prospect of stopping Adorofia Hitora's war through beating Vitalia."
    "The war in Grecia takes on a new dimension, as Britannia commits itself to supporting Papagos's troops."
    "Things are beginning to heat up in Europa once again . . ."
    
    stop soundfx fadeout 3.0
    stop music fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000201
    
#####################################################################################################################################################
#sc0000201	-	Tito emerges
#####################################################################################################################################################
label sc0000201:   
    scene black
    with fade
    
    $ mouse_visible = False
    show expression Text(_("Meanwhile, in the forests of Serpana . . ."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx "se/birds.ogg" fadein 3.0
    play soundfx2 "se/outdoor_crowd.ogg" fadein 3.0
    scene woodland_clearing
    with fade
    play music "music/evil.ogg"
    
    "Serpana, a country in south-central Europa, is a flashpoint of ethnic hostilities and tension."
    "Deep in the woodland of the countryside, the xommunist and partisan fighters gather . . ."
    "Hidden from sight, forced to retreat into the countryside, the citizens fear impending war."
    
    #Profile Unlock
    $ active_codex_profiles.update({
        "Tito": [profile_tito_name, profile_tito_flag, profile_tito_birthplace, profile_tito_description, profile_tito_type, profile_tito_birthday, profile_tito_zodiac, profile_tito_role, profile_tito_height, profile_tito_blood, profile_tito_drink, profile_tito_food, profile_tito_weight, profile_tito_sprite]
    })
    
    play sound4 "se/walk.ogg"
    play sound6 "se/brush.ogg"
    $ mouse_visible = False
    scene cg_tito
    with dissolve2
    $ mouse_visible = True
    
    "At the helm of the group, their leader, a scrappy girl named Iosipa Tito, gives an impassioned speech . . ."
    tito determined "Comrades, xommunists, my fellow partisans . . ."
    "The crowds watch in awe as their boss rouses their spirits."
    tito "Our country and our movement face an existential threat . . . the war in Europa is coming to our doorstep."
    tito "Under pressure from Hang, Rumanum and Germania, Prince Paulie plans to sign the {i}Triple Pact{/i} . . ."
    "By joining such a pact, Serpana will be forced down the road towards vascism."
    "For a xommunist like Tito, such a thing is unacceptable."
    tito "On our northern borders, Hang and Germania wait, with their tanks, planes and soldiers . . ."
    tito "To the east, our allies in Rumanum have abandoned us, conquered by extremism and fear . . ."
    tito "The western {i}Alliance{/i} won't come to our rescue. Surrounded on all sides, we must make our own plans . . ."
    "Wearing fingerless gloves, she flexes in a fighting pose, a true image of partisan determination."
    "This is where their rebel movement begins . . ."
    tito "The monarchy has abandoned its people. The rest of Europa is at war. Now is our time to act!"
    
    play soundfx3 "se/battlecry.ogg" fadein 2.0 volume 0.4
    play soundfx4 "se/urah.ogg" fadein 2.0 volume 0.4
    
    tito "It is time for us partisans to seize control and form our own country . . ."
    "The rebel soldiers around her cheer in joy."
    sol determined "Better the grave than a slave, better a war than the pact!"
    "It's time for them to fight back. It's time to take back their country and fight off the northern invaders."
    "Tito smiles as her peasant army prepares for civil war."
    
    stop soundfx3 fadeout 2.0
    stop soundfx4 fadeout 2.0
    play silsound4 "se/silly4.ogg"
    
    tito happy "And once we have control, I can finally wear a nice sundress!"
    sol normal "Huh? Are you feeling okay boss?"
    
    stop music fadeout 5.0
    play silsound6 "se/silly3.ogg"
    
    tito shock "What? Isn't that why we're doing this?"
    sol "I don't follow . . ."
    "An awkward silence fills the air."
    
    play music "music/facepalm.ogg"
    play silsound2 "se/silly18.ogg"
    
    tito moe "The rich landowners always have the nicest clothes! I want to wear a cute sundress for once!"
    sol shock "You want to take over the country just so you can wear nicer clothes?!"
    tito "That's the whole point of our movement!"
    sol ". . . eh . . . so that's what it's about . . ."
    tito "We will spill an ocean of blood for the sisterhood and the right of our peoples to wear sundresses!"
    sol ". . . . . . . . ."
    "This revelation might have disheartened the rebels somewhat . . ."
    tito "W-Well, we can also form a democratic and righteous nation . . . but the sundresses come first!"
    "Well, that's what's happening in the woodland of Serpana anyway . . ."
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000219

#####################################################################################################################################################
#sc0000219	-	Simovic plotting / Declares Tito an idiot
#####################################################################################################################################################
label sc0000219:
    play soundfx "se/city.ogg" fadein 3.0
    scene day3
    with fade
    play music "music/horror.ogg"
    play soundfx2 "se/walk.ogg"
    
    "Meanwhile, further north, in the capital Singidun, a devious individual stalks the cobbled streets . . ."
    
    scene city2
    with dissolve
    show simovic determined
    with dissolve
    play silsound3 "se/silly12.ogg"
    stop soundfx2 fadeout 1.0
    
    "Simovic, {i}Chief of the General Staff of the Serpana Royal Army{/i}, is a powerful figure in Serpana's politics."
    "An old soldier, she has seen the fortunes of her country come and go, leaders rise and fall . . ."
    simovic "Peasant rebels . . . xommunists . . . vascists . . . criminals . . . they're all trying to destroy this country."
    "She looks down on the partisan forces with contempt, disgusted by their peasant, socialist tendencies."
    simovic "That Tito is a fool. What does she think she can achieve, hiding out with her band of merry men?"
    "Clutching a bag of shopping, the pensioner-General mutters to herself."
    simovic "I can't let a silly girl like that ruin my plans . . . not when I'm so close."
    "Sniffing haughtily, the elderly woman ruminates secretively, keeping a careful watch on her surroundings."
    
    show simovic happy
    with dissolve
    
    simovic "For years, I've plotted, calculating, waiting for my moment to strike. We're closer now than ever . . ."
    "With access to the high echelons of government, Simovic is privy to top-level discussions and diplomatic intel."
    "The recent pressure from Germania to have the country join the {i}Triple Pact{/i} has caused much controversy."
    
    show simovic normal
    
    simovic "Prince Paulie will betray us as soon as he gets the chance. He's weak. For Serpana's future, we have to act."
    simovic "The coup will be swift and decisive. Neither the xommunists, nor the vascists, will even have time to blink . . ."
    "Seeing herself as a martyr, the lady quietly contemplates the brilliance of her scheming."
    
    show simovic determined
    with dissolve
    
    simovic "Soon . . . the timing isn't right yet. But soon . . ."
    "Until then, the elderly General will simply have to continue her work behind the scenes."
    "A divided and strange land, Serpana is a powderkeg waiting for a strike, ready to blow at the first spark . . ."
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000211
    
#####################################################################################################################################################
#sc0000211	-	Rinni/Badoglio panic as Cyracana is invaded/IEA invaded
#####################################################################################################################################################
label sc0000211:
    scene black
    with fade
    
    $ mouse_visible = False
    show expression Text(_("At the headquarters of the Vitalian leader, in Rhome, Vitalia . . ."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    scene day3
    with fade
    play soundfx "se/sea.ogg" fadein 3.0
    
    "All seemed to be going well for the {i}Douché{/i}. Grecia is being handled by Messe, the deserts are secure . . ."
    "It was just another peaceful day in Vitalia, when . . ."
    
    play silsound3 "se/silly12.ogg"
    play silsound4 "se/silly14.ogg"
    scene mansion3
    show rinni hat moe2 at right35
    show badoglio hat shock at left35
    with hpunch
    with vpunch
    play music "music/pantsu.ogg"
    
    rin "We're on the retreat in Gypta now?! The Britannians! Wavell! Graziani, how could you?!"
    "At the Villa Dorlonia in Rhome, Vitalia, the leader of the grandiose nation, {i}Il Douché{/i} Mussorinni, begins to freak out."
    
    play silsound2 "se/silly9.ogg"
    
    rin "This is bad! This is really bad! Badoglioooooo! What's a {i}Douché{/i} to do?! What's a {i}Douché{/i} to do?!"
    "The Britannians are now on the offensive, counterattacking the Vitalian lines and reclaiming their territory."
    
    show badoglio hat determined
    show rinni hat embarrassed
    with dissolve
    
    rin "What's going on here? I thought Graziani and Yamato won the war for us . . ."
    bad "First the {i}Maletti Group{/i} was bombarded by artillery fire on one of Graziani's fortified camps, around Zidiparrani . . ."
    bad "Hundreds of soldiers were killed and thousands taken prisoner in a complete reversal of fortunes."
    "As this happened, the {i}Ducky{/i} tanks engaged in {i}bewegungskrieg{/i} and overran the Vitalian camps."
    bad "Now, Graziani is on the run and all the gains of the previous autumn have been forfeited . . ."
    
    play silsound3 "se/silly2.ogg"
    play silsound4 "se/silly27.ogg"
    show rinni hat moe3
    show badoglio hat moe
    
    rin "Graziani is such a coward! We Vitalians don't run away, we're far too lazy for that."
    bad "Please don't belittle your own countrymen, {i}Il Douché{/i}."
    
    show object_vitalianprisoners at tankpos
    with dissolve
    
    "{i}Il Douché{/i} is disheartened by regular bad news. The reports coming from the frontline haven't been good."
    "Around dawn this morning, as the Britannian tanks attacked, mass surrenders took place."
    "Many Vitalians across the dunes gave in to their foe, foregoing their morning cappuccinos in the process."
    "{i}Kruiser{/i} tanks arrive under the cloak of sandstorms, mercilessly pursuing the fleeing Vitalians with glee."
    "Huge quantities of supplies have been captured by the Britannians, with many jars of bolognese lost to the enemy."
    
    hide object_vitalianprisoners
    show rinni hat moe1
    show badoglio hat determined
    with dissolve
    play silsound2 "se/silly21.ogg"
    
    bad "Not only has Wavell beaten back Graziani's forces in Gypta . . . now Cyracana is threatened by invasion."
    rin "No way! Cyracana is our sovereign territory! They can't just march in . . ."
    bad "Well, they are, in droves. In Zomali too, our armies are being routed by renewed colonial efforts."
    
    show rinni hat determined
    with dissolve
    
    rin "That Churchill! Where does she get the nerve to attack us?"
    "Distractions in Grecia and elsewhere on the continent have given the Britannians a window within which to attack."
    "This might be the first time in the war that an {i}Axle{/i} power is on the retreat . . ."
    
    play silsound3 "se/silly20.ogg"
    show rinni hat moe3
    show badoglio hat shock
    
    rin "{i}Sigh{/i} . . . I'm getting pretty tired of all this fighting. Let's just quit."
    bad "{i}Il Douché{/i}, you can't say things like that! All those soldiers out there, fighting and dying for you . . ."
    rin "But I'm tired."
    
    stop music fadeout 5.0
    
    bad "It would be a complete waste of their sacrifices if you threw in the towel."
    "Badoglio chides her leader into continuing the war."
    rin "{i}Sigh{/i} . . ."
    
    show rinni hat determined
    show badoglio hat normal
    with dissolve
    play music "music/rinni.ogg"
    
    rin "Fine. Get our armies in Gypta to fall back to the wire and regroup at Fort Kaputz!"
    "With a determined demeanor, Rinni tries to make a bold decision."
    
    show rinni hat shock
    show badoglio hat determined
    
    bad "Fort Kaputz was captured {i}en passant{/i} by Britannian armor as it advanced westwards."
    "But she's instantly rebuffed by Badoglio. It seems the {i}Douché{/i} is too late to save Fort Kaputz."
    
    show rinni hat determined
    with dissolve
    
    rin "Then . . . we should retreat to the port town of Bardia . . ."
    bad "Already lost. Our defenses were too weak. Some Ostralasian sappers blew holes in our lines and broke into the town."
    "Meanwhile, naval and aerial bombardment forced the Vitalia garrisons into surrender."
    
    play silsound6 "se/silly10.ogg"
    show rinni hat moe1
    show badoglio hat normal
    
    rin "Tobrunsk . . . that's where we make our stand! We have to defend Tobrunsk!"
    "Badoglio simply stares at her dear leader."
    
    play silsound2 "se/silly25.ogg"
    show rinni hat moe3
    
    rin "Tobrunsk has already fallen to Britannia, hasn't it?"
    
    show badoglio hat determined
    
    bad "Enemy infantry broke through the southern perimeter of the city with their {i}Ducky{/i} tanks taking the bridgehead."
    "Shocked by the sudden attack, the Vitalian soldiers panicked, uncertain what to do."
    bad "Despite a few energetic counterattacks from the {i}Vitalia Sirte{/i} division, the battle was over by nightfall."
    bad "The harbor suffered little damage and the industrial plants remain intact, but the city is now under enemy control."
    "Over twenty thousand Vitalia soldiers and weapons were taken captive by {i}Alliance{/i} forces following this battle alone."
    
    play silsound5 "se/silly22.ogg"
    show rinni hat shock
    show badoglio hat moe
    
    bad "By this point, hundreds of thousands of our soldiers have been captured by the enemy in total."
    
    play silsound2 "se/silly12.ogg"
    show rinni hat moe2
    
    rin "Those Vitalians . . . they're surrendering even harder than Franzo does!"
    "This Britannian counterattack operation has been a complete disaster for Vitalia."
    
    show rinni hat determined
    show badoglio hat normal
    with dissolve
    play silsound4 "se/silly14.ogg"
    
    rin "This is a disaster! I'm going to have Graziani replaced. We need someone that can stop the Britannians!"
    "Going over Graziani's head, it seems that Mussorinni has lost confidence in her commander."
    
    show badoglio hat shock
    
    bad "There's Epirus and Grecia to consider as well . . ."
    rin ". . . indeed."
    bad "What about Zomali? Our forces are being pushed into a retreat there too."
    rin ". . . I know."
    bad "Your popularity is beginning to tank as well. Maybe we should ask the Germanians for support?"
    
    play silsound3 "se/silly7.ogg"
    show rinni hat moe2
    
    rin "No! I can't afford to get Hitora involved again. I still haven't told her about Commander Yamato's abduction!"
    "Rinni gets flustered over the idea of Germania fighting on these old fronts she opened up."
    rin "Why do we have to finish all these wars anyway? I'm getting a headache just thinking about it."
    
    show badoglio hat normal
    
    bad "Perhaps you would like some gelato to cool your head, {i}Il Douché?{/i}"
    
    show rinni hat moe4
    with dissolve
    
    rin "Well, if you insist. I think I've earned a break."
    "After a very short session of planning strategy, the easily-distracted leader of Vitalia goes to get some ice cream."
    
    scene day3
    with dissolve
    
    "With Vitalia's colonies being overrun by Britannia, will they fight back and make a final stand?"
    "Will they call on Germania? Or is this the end for the {i}Axle{/i} on those exotic shores?"
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000202
    
#####################################################################################################################################################
#sc0000202	-	Hitora planning about Rumanum oil
#####################################################################################################################################################
label sc0000202:
    scene black
    with fade
    
    $ mouse_visible = False
    show expression Text(_("Meanwhile, in Altberlin, Germania . . ."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx2 "se/power2.ogg" fadein 3.0
    play soundfx3 "se/heart.ogg" fadein 3.0
    scene warroom_dark
    show transparent
    show hitora hat powers large fade
    with dissolve
    play music "music/yandere.ogg"
    
    "Standing at her study window, the Füühbar paces back and forth, a dark aura seeping out."
    hit "Those sneaky, sneaky Britannians, building airbases within striking distance of Rumanum!"
    
    play silsound5 "se/silly17.ogg"
    
    hit "It's as if they know about my secret plans . . . my plans for a total war with the Union of Sovia."
    "The oilfields of Rumanum are a valuable prize and Hitora has had her eye on them for some time now."
    "The fuel is needed for tanks, trucks, fighters, bombers, and all the machinery of her planned war."
    hit "They're using Vitalia's war in Grecia to try and cut us off . . . Rinni, you moron. Do you think I don't know what's going on?"
    "While it may lead to delays in her planned invasion of the east, the Füühbar can't have a weak southern front."
    hit "They leave me no choice. We will have to act, swiftly, to stop the Britannians in their tracks."
    hit "Germania will have to clean up Mussorinni's mess yet again . . ."
    "Plotting to fix the situation in the southeast, Hitora comes up with a new plan . . ."
    hit "First, the oilfields. Then, securing the pact. And finally, a new war in Grecia . . ."
    
    stop music fadeout 3.0
    stop soundfx2 fadeout 3.0
    stop soundfx3 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    #Map Data
    $ mapdata = ScreenData("geomap1", "map11", "easternmap")
    
    #Mission Data
    $ active_invasionbeacons_items.update({"bat000048": [bat000048_description, bat000048_title, bat000048_type, bat000048_x, bat000048_y]})
    
    #Mission Assign
    $ log.assign("[bat000048_title]")
    
    #Allegiances Data
    $ tobrunsk_governor = "Jumbo"
    $ tobrunsk_governor_pic = "{image=side jumbo normal}"
    $ tobrunsk_command = command_two
    $ tobrunsk_management = management_two
    $ tobrunsk_influence = influence_three
    $ tobrunsk_alignment = britannia_empire
    $ tobrunsk_hostility = hostility_unfriendly
    $ tobrunsk_martial = [
        "infantry_anzac_gunner_heer6_profile",
        "infantry_anzac_gunner_heer6_profile",
        "panzer_bishopsph_profile",
        "panzer_crusader_profile",
        "airsupport_snotfire_profile"
        ]
    $ active_maptown_items.update({"tobrunsk": [tobrunsk_name, tobrunsk_size, tobrunsk_governor, tobrunsk_governor_pic, tobrunsk_hostility, tobrunsk_alignment, tobrunsk_population, tobrunsk_publicorder, tobrunsk_influence, tobrunsk_command, tobrunsk_management, tobrunsk_farming_worth, tobrunsk_mining_worth, tobrunsk_industry_worth, tobrunsk_trade_worth, tobrunsk_entertainment_worth, tobrunsk_military_worth, tobrunsk_corruption_worth, tobrunsk_unlocktown, tobrunsk_martial, tobrunsk_siege, tobrunsk_company_img, tobrunsk_company_text, .63, .775]})
    
    #Additional Map Data
    $ budast_unlocktown = True
    $ active_maptown_items.update({"budast": [budast_name, budast_size, budast_governor, budast_governor_pic, budast_hostility, budast_alignment, budast_population, budast_publicorder, budast_influence, budast_command, budast_management, budast_farming_worth, budast_mining_worth, budast_industry_worth, budast_trade_worth, budast_entertainment_worth, budast_military_worth, budast_corruption_worth, budast_unlocktown, budast_martial, budast_siege, budast_company_img, budast_company_text, .62, .45]})
    
    #Go To Map
    jump map_begin
    
#####################################################################################################################################################
#bat000048	-	Operation Mozzarella: Battle of Klisura Pass
#####################################################################################################################################################
label bat000048:    
    hide screen mapchoice1
    $ renpy.block_rollback()
    $ _rollback = True
    $ store.text_history_enabled = True
    window hide
    play sound6 "se/march2.ogg"
    stop music fadeout 2.0
    scene black
    with dissolve
    
    $ mouse_visible = False
    show expression Text(_("[bat000048_title]"), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    show expression Text(_("The Klisura Pass, Grecia"), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx "se/tank_invasion.ogg" fadein 3.0
    scene desert_bunker
    show messe determined
    with fade
    play music "music/rinni.ogg"
    
    "The autumnal war in Grecia continues, with much stiff resistance and destructive fighting."
    messe "Keep up the good fight . . . let's show them what we've got."
    "One Vitalian battalion in Epirus captured the Krabapple heights on the Alpaki front, while shrouded in a snowstorm."
    "And the use of artillery and aircraft on this front has forced the Grecians to retreat to defensive positions further inland."
    "In fact, they've done well enough to warrant Vitalia's supreme command diverting troops from Gypta to Grecia."
    cavallero determined "I see things are looking lively here."
    
    show messe at right35
    with ease
    play sound3 "se/walk.ogg"
    show cavallero determined at left35
    with dissolve
    
    "A high-ranking official, Cavallero, joins Messe's corps, inspecting the line as they march."
    cavallero "How goes it Messe? The invasion?"
    "The young boy was recently promoted by Mussorinni to {i}Chief of the Defense Staff{/i}, taking over from Badoglio."
    "He will be helping to lead the campaign in Grecia, working with talented commanders like Messe."
    messe "It's been easygoing so far. This whole thing will be a cinch . . . it's actually all a bit boring."
    cavallero "Well, let's review the situation once more . . ."
    
    show cavallero at right25
    show messe at right1
    with ease
    play sound4 "se/map.ogg"
    show map_tactical8 behind messe at tacticalpos
    with dissolve
    
    cavallero "Vitalian forces invaded Grecia in several columns; the {i}XXV{/i} and {i}XXVI{/i} . . ."
    "Despite protests about lack of materiel, they have invaded with more advanced equipment than their counterparts."
    cavallero "So far, we haven't encountered much resistance at all. As expected. Stupid Grecians."
    messe "Still, we should be on our guard . . ."
    "Due to Bolga's neutrality, the opposing army was able to move many of its divisions across to the border with Epirus."
    "Just because they haven't seen a pushback, that doesn't mean the Grecians aren't waiting for their moment."
    
    play silsound3 "se/silly5.ogg"
    show cavallero normal
    show messe shock
    
    cavallero "There is some bad news though."
    messe "Bad news? What bad news?"
    cavallero "The battles across the border from Epirus will decide this war for now. Other operations are being postponed . . ."
    messe "Postponed?"
    cavallero "The amphibious invasions have been called off because of bad weather. Along with other plans."
    "Even though it seemed like a cool idea to have frogmen leading the march, it's no longer feasible."
    
    hide map_tactical8
    with dissolve
    show messe normal at right35
    show cavallero normal at left35
    with ease
    
    messe "I guess we'll be leading this war then . . ."
    
    show cavallero determined
    
    cavallero "Do your best, Messe. For the glory of Vitalia and {i}Il Douché{/i}."
    "Cavallero puts his trust in the girl, knowing that the war ahead won't always seem so easy."
    
    stop music fadeout 5.0
    play silsound6 "se/poke.ogg"
    show messe determined
    show cavallero shock
    
    messe "Ah! You've got bolognese sauce on your shirt again! That's the third time this campaign."
    cavallero "W-What?"
    
    show messe determined at center
    with ease
    
    "Messe licks her finger and begins rubbing Cavallero's collar, trying to clean it."
    cavallero "P-Please stop it, you're embarrassing me."
    "The girl continues to act the part of a big sister, until the stain slowly vanishes from the fabric."
    messe "Almost . . . almost got it . . ."
    
    play soundfx2 "se/battle4.ogg"
    play sound4 "se/tank_fire.ogg"
    show messe moe
    show cavallero shock
    with hpunch
    with vpunch
    play music "music/glory.ogg"
    
    "Suddenly there's a flurry of fire from entrenched positions on the opposing hillside."
    "Mortar rounds, anti-tank guns and machine gun nests all inflict casualties on the advancing Vitalians."
    
    show messe moe at right35
    with ease
    
    "Before Messe can finish the job, she plucks up her courage and barks orders, loudly, along the line."
    messe "D-Defensive positions! Quickly!"
    "The Vitalian soldiers panic, dashing to and fro, desperately trying to find cover."
    
    show cavallero determined
    show messe determined
    with dissolve
    
    cavallero "Where are they? Where are those Grecian cowards?! Why I oughtta!"
    "Without time to react properly, the commanders also duck low and do their best to command their lines."
    "But the column soon disintegrates, as the desperate men and women dive under nearby bushes for safety."
    cavallero "I don't understand. Mussorinni assured us that the Grecians were lazy and wouldn't fight back . . ."
    messe "What? Of course they're going to defend themselves! What kind of crazy idea is that?"
    
    show cavallero determined at left25
    show messe determined at center
    with ease
    
    "Messe sticks her head above the parapet, scanning the horizon with a small pair of binoculars."
    messe "Metaxas obviously prepared his soldiers. They're dug in deep . . ."
    "Focusing her gaze, the girl notices trenches and nests built on the surrounding hills."
    "The roads are guarded, the forests are crawling with enemies and key targets are well-defended."
    
    play silsound2 "se/silly2.ogg"
    show messe moe
    
    messe "We've found the {i}Alpaki Line!{/i} To battlestations! We're going to attack!"
    
    play sound3 "se/trumpet.ogg"
    play sound5 "se/battlecry.ogg"
    
    "Plunging forward into battle, the Vitalians bravely push their invasion deeper and deeper into Grecia."
    messe "Come on you kebab-eating cowards, show us what you've got!"
    
    stop music fadeout 1.0
    stop soundfx fadeout 1.0
    stop soundfx2 fadeout 1.0
    stop sound5 fadeout 1.0
    scene black
    with pixellate
    
    jump bat000048_begin
    
label bat000048_begin:
###########################################################################
    #bat000048	-	Battle
###########################################################################
    
    #History Block
    $ renpy.block_rollback()
    $ store.text_history_enabled = False
    $ _rollback = False
    $ config.skipping = False
    
    #Enemy Team Set
    $ enemy_team = BaseTeam("Enemy", Solid("#000000", xysize=(50,50)), limit=50)
    $ enemy_team.add_fighter("enemy_grecia_gunner_heer5")
    $ enemy_team.add_fighter("enemy_panzer_l335")
    $ enemy_team.add_fighter("enemy_panzer_crusader")
    
    #Playing For New Side Set - Axle
    $ empty_data("fighter")
    $ load_data(vitalia_fighter_set, "fighter")
    $ yamato_unload()
    $ yamatoforce_enabled = False

    # Selection Screen Set
    $ airsupport_section_unlocked = False
    $ infantry_section_unlocked = False
    $ panzer_section_unlocked = True
    $ antitank_section_unlocked = False
    $ commander_section_unlocked = False
    $ specialgroup_section_unlocked = True
    $ player_team = BaseTeam("Player", Solid("#000000", xysize=(50,50)), limit=50)
    play battlemusic "music/map3.ogg"
    call screen non_battle_party_screen

    # Battle Set
    $ config.skipping = False
    $ yamato_lvlcheck()
    stop battlemusic fadeout 1.0
    scene black
    $ renpy.pause(1.0, hard=True)
    play battlesfx "se/battle4.ogg" volume 0.25
    play battlemusic "music/battle_desert.ogg"
    $ renpy.block_rollback()
    $ fight_end = "bat000048_aftermath"
    $ game = Battleground("Battle Stage   |   Operation Mozzarella", player_team.store[0], enemy_team.store[0], "statuewoman")
    $ battle_terrain = "mountain"
    $ battleground_bg = "background_field"
    $_game_menu_screen = None
    $ config.skipping = False
    $ config.keymap['skip'].remove('K_LCTRL')
    $ config.keymap['skip'].remove('K_RCTRL')
    $ config.keymap['hide_windows'].remove('h')
    $ renpy.clear_keymap_cache()
    call screen battle_screen(bg=battleground_bg, disc="plate_dirt", dec_1=["decoration_cave_front1", 950, 0], dec_2=["decoration_cave_back1", 3, 320]) with battleopening 
    $ renpy.block_rollback()
    
label bat000048_aftermath:
    scene black
    $ renpy.pause(1.0, hard=True)
    
    #Aftermath
    $ battle_count +=1
    $ battlestats_up()
    $_game_menu_screen = "save_screen"
    $ renpy.block_rollback()
    $ cp = max_cp
    $ cp += cp_levelset
    $ max_cp += max_cp_levelset
    
    #Unlocked Player Team Set
    if not skip_battle_selected:
        $ axle_fighter_set.append("panzer_toldi")
        $ load_data([
            "panzer_toldi"
            ], "fighter")
        $ yamato_levels +=1
    $ persistent.skip_battle_sensitive = False
    $ skip_battle_selected = False
    
    #After Battle Continue
    $ _rollback = True
    $ store.text_history_enabled = True
    $ config.keymap['skip'].append('K_LCTRL')
    $ config.keymap['skip'].append('K_RCTRL')
    $ config.keymap['hide_windows'].append('h')
    $ renpy.clear_keymap_cache()
    
    jump bat000048_continue
    
###########################################################################
    #bat000048	-	Battle End
###########################################################################
label bat000048_continue:
    
    play soundfx "se/tank_invasion.ogg" fadein 3.0
    play soundfx2 "se/battle4.ogg" fadein 3.0
    scene desert_bunker
    with pixellate
    play music "music/rinni.ogg"
    
    #Mission Marked Done
    $ log.markdone("bat000048")
    
    "Slowly, the Grecians begin to win and push back on the Vitalian lines, sending them into a retreat."
    "Things were going so well for the Vitalians. After their success in Gypta and Zomali, it felt like a victory was imminent."
    "It seemed as though another deadly conflict would claim a neutral nation for the {i}Axle{/i} side."
    "And yet . . ."
         
    show messe moe
    with dissolve
    play silsound5 "se/silly1.ogg"
    
    messe "{i}Il Douché!{/i} This isn't how it's meant to go at all!"    
    "And yet, the Vitalian offensive has been halted by the Grecian defensive line, almost immediately."    
    "Wave after wave of swarthy, pasta-eating Vitalian soldiers have been flung at the enemy."    
    "But the line has held, much to the chagrin of Mussorinni and her subordinates."
    
    show messe determined
    with dissolve
    
    messe "Pull yourself together Messe! Your soldiers need you to be strong."
    
    show object_klisurapass at tankpos
    with dissolve
    
    "Now some weeks have passed and the attrition is beginning to break, but in the opposite direction . . ."
    "Commander-in-Chief of the Grecian Army, Papagos, leads the counterattack into Epirus, taking advantage of {i}Alliance{/i} aid."
    "Churchill has sent a Britannian expeditionary force to the island of Kaptara to assist the Grecian armies."
    "The {i}BRAF{/i} is also offering air support to help break the Vitalian lines . . ."
    "Many Vitalian commanders simply hoped that the Grecians would not react to an invasion or would let them pass."
    "Now, the Grecian foe marches into Vitalian territory; a complete humiliation for Rinni and her Generals . . ."
    
    hide object_klisurapass
    show messe moe
    with dissolve
    play silsound4 "se/silly4.ogg"
    
    messe "Who am I kidding? This is impossible! We're going to lose here, I just know it."
    "It was to be expected. The army suffered several setbacks before the invasion started."    
    "Out of one hundred light tanks in the {i}Centauro Armored Division{/i}, only ninety were operational in time."    
    "There were meant to be around two thousand lorries for use in the offensive, but just over one hundred arrived."    
    "What's more, Rinni let almost a million troops go home for the harvest before mobilization."
    
    play silsound3 "se/silly12.ogg"
    
    messe "Stupid Mussorinni! Why did you send us out here to die without any support?!"
    "The tide is turning against Vitalia in Grecia and time is running out for the {i}Douché{/i} to prove herself as a brilliant leader."
    "Can they turn the situation around?"
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000205

#####################################################################################################################################################
#sc0000205	-	Germanian troops occupy Rumanum / Bolga
#####################################################################################################################################################
label sc0000205:
    scene black
    with fade
    
    $ mouse_visible = False
    show expression Text(_("Meanwhile, in the woodland of northern Rumanum . . ."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx "se/march3.ogg" fadein 3.0
    play soundfx2 "se/tank_far.ogg" fadein 3.0
    play soundfx3 "se/birds.ogg" fadein 3.0
    scene woodland_day
    with fade
    play music "music/evil.ogg"
    
    "On the border between Rumanum and Germanian Polix, there's much buzz and commotion . . ."
    
    show object_belgaeinvasion at tankpos
    with dissolve
    
    "Germanian soldiers and tanks steam through the forests and plains, taking up strategic positions and making themselves at home."
    "To prevent their enemies from gaining access to the vast oilfields of Rumanum, the {i}Vehrmaxt{/i} are slowly filtering into the country."
    
    hide object_belgaeinvasion
    with dissolve
    play sound4 "se/brush.ogg"
    play sound2 "se/walk.ogg"
    show hitora hat angry
    with dissolve

    hit "Look at it. It's a beautiful sight, isn't it? All that oil . . . and now it's ours."
    "The Füühbar is pleased by the prospect of access to ready oil and a swift expansion of territory."
    ewalda "I think you and I have different definitions of beauty . . ."
    
    play sound6 "se/scamper.ogg"
    play silsound3 "se/poke.ogg"
    
    anton moe "H-Hey! Wait a minute! What are you Germanians doing here?"
    
    stop sound6 fadeout 1.0
    play sound5 "se/brush.ogg"
    show hitora hat happy at left3
    with ease
    show antoness moe at right3
    with dissolve
    
    "Suddenly, Antoness, the little {i}Red Dog{/i}, bursts into the clearing, dashing on all fours like a mongrel."
    anton "What is this? All these soldiers and supplies! What's with all the tanks?!"
    
    play silsound2 "se/silly7.ogg"
    show hitora hat moe2
    
    hit "Oh yeah, about that . . ."
    anton "No way . . . the Füühbar! The Füühbar of Germania is here!"
    "Hitora pulls an awkward expression as the little dog fangirls over her."
    hit "We're just going to be staying here for a while. Hope that's cool and all."
    
    show antoness angry
    with dissolve
    
    anton "Hang on . . . what do you mean you're going to be staying for a while?"
    hit "You know . . . just let our troops camp here, and take control of the oil and grain, and use your train stations for transit . . ."
    "It's pretty much an occupation."
    anton "This is sovereign Rumanum territory. You can't move your soldiers in without my permission. Do you want me to bite you?"
    
    show hitora hat angry
    with dissolve
    
    hit "Bite me? Just try and attack the Füühbar of Germania, pipsqueak. See what happens."
    "Hitora doubles down."
    
    show antoness shock
    with dissolve
    
    anton "I'm s-sorry, my Füühbar. But . . . but this is my country. This is Rumanum."
    hit "Every nation in Europa belongs to Germania. It's high time you learned that."
    anton "And I thought you'd be cool about it! When I sent a letter saying we should have a sleepover, I didn't think you'd bring your armies."
    "Even though Antoness complains, Hitora notices her little bushy tail is beginning to wag."
    "Rumanum and Hang have been in competition recently, trying to vie for Hitora's affections, as she's taken over most of Europa."
    "To be given Germania's protection in the face of Starin's recent expansionism must make her happy on some level."
    "Although it does mean a humiliating occupation is necessary . . ."
    
    show hitora hat moe2
    show antoness normal
    with dissolve
    
    hit "Here. Have this in exchange, to make up for the occupation."
    "The Füühbar hands the little dog a golden envelope."
    anton "Huh? What's this?"
    
    play silsound3 "se/silly19.ogg"
    show antoness moe
    
    hit "It's an invitation to join my new club, the {i}Triple Pact{/i}."
    anton "Eh? Seriously! You mean it?"
    hit "Originally it was only meant to be about Zipangu and Vitalia, but now I'm getting some more members signed up."
    hit "We can trade, swap prisoners, invade our enemies, share intelligence, hold sleepovers, go bowling . . . all kinds of stuff!"
    
    play silsound4 "se/silly12.ogg"
    
    anton "This is . . . all I ever hoped for . . . Rumanum and Germania are going to be friends?"
    
    show antoness happy
    show hitora hat moe4
    with dissolve
    
    hit "We're going to hold a big party in Wien soon to celebrate too. You should come along."
    anton "A party too? I'm in!"
    "Hitora makes plans to take charge over more unwitting, weak countries in Europa. This time without firing a shot."
    ewalda "So you're happy for us to crash here? It's only a couple of divisions anyway . . . for now."
    anton "Of course. Just try not to cause any trouble. We're bankrupt right now, so we can't afford to clean up after you."
    
    play silsound2 "se/poke.ogg"
    show hitora hat moe3
    show antoness moe
    
    hit "What? You're bankrupt?"
    anton "A-Ah! Never mind! You didn't hear that from me."
    "No, they really did just hear that."
    anton "Anyway, I've got to get back to the capital! Big country to run after all, so I'll see you around!"
    
    play sound3 "se/dash.ogg"
    play sound4 "se/scamper.ogg"
    hide antoness
    with dissolve
    
    "Just as quickly as she arrived, the little {i}Red Dog{/i} scampers away again, her paws pounding against the sodden earth."
    
    show hitora hat angry at center
    with ease
    
    ewalda "Well, she gave up on defending her sovereignty rather quickly . . ."
    hit "Everyone in this country is like that. Push a little and they'll hand over their territories, just like that."
    ewalda "Which is why we had to act. Starin would have leaned on Antoness, and she would have buckled . . ."
    "Better a Germanian Rumanum than a Sovian one. That's Hitora's logic, anyway."
    ewalda "I suppose Antoness needs to learn her place in the pecking order, one way or another."
    hit "It's the way things are. But maybe these wannabe's need some positive reinforcement to understand that."
    "Hitora, the alpha wolf, asserts her dominance over the {i}Red Dog{/i} by strategically moving her troops into the country."
    "Rumanum is slowly being overrun by Germanian soldiers, as they take advantage of what they see to be an open invitation."
    "The raw materials and supplies of the east will serve them well in their future wars of aggression . . ."
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    stop soundfx3 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000206
    
#####################################################################################################################################################
#sc0000206	-	Starin surprised by Rumanum and Germanian aggression
#####################################################################################################################################################
label sc0000206:
    scene black
    with fade
    
    $ mouse_visible = False
    show expression Text(_("Elsewhere, deep within the Xremlin walls, in Moskva, Sovia Major . . ."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx "se/cave.ogg" fadein 3.0
    scene starinbase
    with fade
    play music "music/soviagrad.ogg"
    
    "In her secret, evil lair, the great leader Starin of the Union of Sovia confides with her closest commander, Zhukky . . ."
    
    show zhukky hat normal at right35
    show starin hat angry at left35
    with dissolve
    
    star "Zhukky! What is the meaning of these reports? It's really bad! Bad bad bad!"
    zh "Which reports are you talking about, m'lady?"
    
    play silsound5 "se/silly2.ogg"
    show zhukky hat moe1
    
    star "The ones about the {i}Vehrmaxt{/i} marching into Rumanum and seizing the oilfields."
    zh "Ah . . . those reports."
    "The tensions between Sovia and Germania have been building for some time."
    "Day by day, it seems that Rumanum is turning into a satellite of {i}Nappi{/i} Germania."
    star "How could you let this happen on your watch? We were meant to be the ones to take the oil from Antoness."
    
    show zhukky hat angry
    with dissolve
    
    zh "I didn't expect Hitora to be so brazen. After all, she signed that {i}Non-Assault Pact{/i} . . ."
    star "That was well over a year ago. She's obviously trying to push the limits and test our responses . . ."
    "Now, only miles from the Sovian border, Germanian troops are amassing and setting up defensive positions."
    
    show zhukky hat determined
    with dissolve
    
    zh "Details in the reports did suggest that her armies are possibly planning to march south, towards Grecia . . ."
    star "Because of Mussorinni's war? That idiot {i}Douché{/i} can't even handle a bunch of goat herders with fez hats!"
    zh "I thought it might simply be an exercise in protecting the flanks on that sort of advance."
    
    show starin hat normal
    with dissolve
    
    star "Well, I don't like it. Next time, she should consult me about movements like these. If we're meant to be friends . . ."
    "Starin pauses for a moment."
    star "Have we heard back from Joey Lippentrop yet about joining the {i}Triple Pact{/i}?"
    zh "Not yet, m'lady."
    
    play sound4 "se/stomach.ogg"
    show starin hat cry
    show zhukky hat moe1
    with dissolve
    
    star "{i}Sigh{/i} . . . tension like this between our empires always makes me hungry. I want something sweet."
    zh "But, we've only just started our briefing."
    
    play silsound2 "se/silly5.ogg"
    show zhukky hat embarrassed
    
    star "Something sweeeeeeeeeeeet!"
    "Starin begins to throw a temper tantrum."
    
    play silsound5 "se/silly26.ogg"
    show starin hat moe1
    show zhukky hat normal
    
    zh "Then, perhaps we should go have some milkshakes out on {i}Scarlet Square{/i}."
    star "Milkshakes? Now we're talking!"
    
    play silsound3 "se/silly23.ogg"
    show starin hat moe4
    
    zh "We'll continue the briefing too."
    star "Eh? Stingy."
    "The spoiled leader of Sovia tries to forget the bad news of Rumanum's turn, as Zhukky treats her to an early snack."
    "With the oilfields firmly in Hitora's grasp, Starin will have to look elsewhere for drilling and supplies."
    "As the two superpowers continue to expand their empires, they begin to push up against one another's borders."
    "Will their peaceful pact last much longer, at this rate? And if not, who will be the first to strike?"
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000267

#####################################################################################################################################################
#sc0000267	-	Gariboldi arrives to take over from Graziani
#####################################################################################################################################################
label sc0000267:
    play soundfx "se/wind.ogg" fadein 2.0
    play soundfx2 "se/tank_far.ogg" fadein 2.0
    play soundfx3 "se/airbase.ogg" fadein 2.0
    scene desert_smoke
    with fade
    play music "music/desert.ogg"
    
    "On the southern shores, in the western region of Cyracana, the {i}Regio Lasagnotte{/i} regroups."
    
    show object_desertbritannia at tankpos
    with dissolve
    
    "As the Britannians successfully push forward and drive back the {i}Axle{/i} forces, things are looking dire."
    "Zomali and Grecia had drawn Mussorinni's focus, leaving Graziani to try and defend against an empowered Wavell."
    "Fort Kaputz, Bardia, Tobrunsk . . . all exposed major weaknesses in the Vitalian army's ability to wage war."
    "Finding it difficult to cope with the pressure and repeated enemy successes, they can only retreat along the coast."
    
    hide object_desertbritannia
    with dissolve
    
    "Their destination is the small coastal area of Baddaboom. Hopefully regrouping there will give them a shot at success."
    
    play sound3 "se/walk.ogg"
    show graziani determined
    with dissolve
    
    "Responsible for their efforts, unable to hold the line any longer, Marshal Graziani frets over her failures so far."
    graz "The Britannians blindsided us. We couldn't hold the towns or the forts, they were spread out too far . . ."
    "The short girl paces back and forth, grinding her teeth and trying to formulate a plan for a counterattack."
    "But every time, she arrives at the same conclusion. It's impossible."
    
    play silsound6 "se/silly5.ogg"
    show graziani moe
    
    graz "It's all {i}Il Douché's{/i} fault. She sent us on a suicide mission without any of the right equipment."
    graz "The Vitalians are neither equipped nor prepared for a war against an opponent armed with the most modern weapons . . ."
    "The army in particular is at a disadvantage in respect of tanks, anti-tank equipment, artillery, and anti-aircraft defense."
    "A big portion of army's guns are from the booty collected on the collapse of Osta-Hang empire in the last great war."
    
    show graziani determined
    with dissolve
    
    graz "We can't match their tanks when we're still fighting like it's the last war. Not to mention the food . . ."
    "There are no field kitchens, and the rations are insufficient, since Vitalian industry is not equipped to meet their requirements."
    
    play silsound4 "se/silly7.ogg"
    
    graz "I hate it! I want to eat a proper pizza again. Not this schlock they keep piling on my plate every evening."
    "In short, Mussorinni's regime has neglected the armed forces during this whole campaign."
    
    show graziani normal
    with dissolve
    
    graz "Germania . . . only Germania can save us. Not a special operation like Yamato's, but a supporting army, with modern equipment."
    "Their ally, with superior tanks, weapons and tactics, will be able to salvage what's left of this campaign."
    "Graziani glances around the campsite, looking for a tent with a radio operator."
    graz "I need to find a wireless post and get in touch with Altberlin . . ."
    
    play silsound2 "se/poke.ogg"
    show graziani shock
    
    gariboldi_un determined "Not so fast."
    
    show graziani shock at left3
    with ease
    play sound3 "se/walk.ogg"
    show gariboldi determined at right3
    with dissolve
    
    "An old man with a puffy, white moustache, appears before Graziani and her detail."
    gariboldi_un "You won't be sending out any further orders. Not on my watch."
    
    show graziani determined
    
    graz "Eh? Who the heck are you? Get out of my way, old man."
    
    show gariboldi happy
    show graziani shock
    with dissolve
    play silsound5 "se/silly12.ogg"
    
    gariboldi "Ah, where are my manners . . . I'm your replacement. Nice to meet you. The name's Gariboldi."
    "Ivitalo Gariboldi, General and Commander of the Vitalian {i}X Army{/i}, currently serving under Graziani."
    "Although, the two have never met before this moment . . ."
    graz "R-Replacement?"
    
    play silsound2 "se/silly11.ogg"
    
    gariboldi "Commander Graziani, I'm here to relieve you of your . . . your command."
    graz "W-What nonsense! You should be leading our forces along the coastal roads to Baddaboom, not here, acting crazy."
    
    show gariboldi determined
    
    gariboldi "It's no joke. I have the telegram from Mussorinni to prove it."
    
    play sound6 "se/map.ogg"
    
    "Gariboldi produces a printed document, the signature and seal of the {i}Douché's{/i} office clearly marked."
    
    show graziani moe
    with dissolve
    
    "Graziani glances through it quickly before turning away in embarrassment."
    graz "That brat. After everything I've done for her, after my loyalty . . . she wants to blame me for this failure?"
    gariboldi "Well, it is your fault."
    graz "I've only ever been a soldier who's obeyed orders."
    "It seems that's not enough for Mussorinni. She wants Graziani to shoulder the blame and return to Vitalia."
    gariboldi "Resign your commission. Let an old codger, like me, take it from here."
    
    show graziani normal
    with dissolve
    
    "Graziani takes a few moments to process the information."
    "Her replacement is an experienced soldier. The army will be safe under his command."
    "Perhaps, in time, he can reverse their fortunes and do what she couldn't . . ."
    gariboldi "You know it's the right thing to do."
    
    play silsound2 "se/silly10.ogg"
    show graziani determined
    show gariboldi shock
    
    graz "Not yet. I have to save this campaign first."
    
    play sound4 "se/dash.ogg"
    play sound5 "se/run.ogg"
    hide graziani
    with easeoutleft
    
    "The girl boldly dashes away, headed for the wireless post."
    
    show gariboldi shock at center
    with ease
    
    gariboldi "W-What . . . where are you going?!"
    graz determined "I'm going to help {i}Il Douché{/i} win this war! I'm going to contact Altberlin and the {i}Vehrmaxt!{/i}"
    
    show gariboldi determined
    
    gariboldi "No, stop it! Mussorinni doesn't want the Germanians to get involved here."
    "But Graziani continues on, disappearing further down the campsite, making her way towards a small tent on the outskirts."
    "Gariboldi would chase her, but he's old and his knees are weak."
    gariboldi "Damn you, Graziani. This is Vitalia's war . . ."
    "Marshal Graziani has lost her position as {i}Governor-General of Cyracana{/i} and has been replaced by an experienced General."
    "In a desperate last move as commander, she aims to bring Germania into this southern war."
    "Will Hitora commit ground troops to this campaign and help to win back Cyracana for Vitalia?"
    "Or is the entire campaign doomed to failure, as Wavell's troops slowly close in?"
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    stop soundfx3 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000209
   
#####################################################################################################################################################
#sc0000209	-	Horthy/Antoness/Hitora Pelbebere palace party in Wien / Feels like a funeral
#####################################################################################################################################################
label sc0000209:
    scene black
    with fade
    
    $ mouse_visible = False
    show expression Text(_("Meanwhile, at the Pelbebere Palace, Wien, Osta"), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx "se/room.ogg" fadein 3.0
    play soundfx2 "se/court_ambience.ogg" fadein 3.0
    scene palace_room_night
    with fade
    play music "music/facepalm.ogg"
    
    "At an official banquet in the opulent Pelbebere Palace in Wien, prominent figures meet to discuss their accession to an alliance."
    "The {i}Triple Pact{/i} . . . one of the most important treaties that the {i}Axle{/i} powers have ever negotiated."
    "The initial treaty confirmed an alliance between Zipangu, Germania and Vitalia. Now, minor countries are also signing up."
    "Hang, Rumanum, Bolga, Serpana, Czexa . . . there are many representatives here tonight."
    "Delegates from each of the host countries mingle over their supper, although the atmosphere is rather dire."
    
    show horthy normal at left2
    show antoness normal at right2
    show hitora hat angry
    with dissolve
                                                            
    "The Füühbar, seated at the head of the table, frowns over the proceedings."
    hit "Honestly, why is everyone being so miserable? This is like attending a funeral . . ."
    "While the key signatories of the agreement are excited about its prospects, many of the smaller nations are anxious."
    "Browbeaten, bribed and bullied into joining the {i}Axle{/i} alliance, they fret over the future."
    "Prince Paulie of Serpana in particular worries for his people and their reaction to joining this pact . . ."
    
    play silsound3 "se/silly4.ogg"
    show hitora hat moe1
    show horthy shock
    
    hit "That silly old coot! Who does he think he is?! He should be honored to even be recognized by the Füühbar!"
    hor "You should cut him some slack. Some of us are up past our bedtimes . . ."
    hit "He just doesn't appreciate how much work goes into diplomacy. Treaties like this make all of us safer!"
    "Although, it does happen at the expense of their humanity  . . ."
    
    show hitora hat angry
    show horthy normal
    with dissolve
    
    hit "{i}Sigh{/i} . . . I just wish they were a little happier about it. They're making me feel like I'm the bad guy."
    
    play silsound4 "se/silly7.ogg"
    show hitora hat worry
    show horthy shock
    show antoness moe
    
    hor "Huh? I thought we were the bad guys?"
    hit "No way! That's just enemy propaganda!"
    
    show horthy determined
    
    hor "But . . . didn't you start this war? Not to mention all those nasty things you've all been doing recently . . ."
    anton "D-Don't worry. History is written by the victors. Once your war with Britannia ends, the {i}Axle{/i} will be the good guys!"
    "Antoness cheers Hitora on, keen to impress the Germanians. Rumanum is pretty desperate to improve relations."
    
    show antoness happy
    with dissolve
    
    anton "The struggle in Europa will swing one way or the other. And right now, the {i}Axle{/i} alliance are the winners!"
    "It's a bargain they all have chosen to make. An extremely destructive, bloody and disastrous one . . ."
    
    show horthy happy
    show hitora hat normal
    with dissolve
    
    hor "Anyway, enough about this treaty. Let's gossip instead."
    hit "Gossip? About what?"
    
    play silsound5 "se/silly9.ogg"
    show hitora hat worry
    
    hor "How are things going with that Zipanguese guy?"
    hit "Eh?! Not you too?"
    
    show antoness shock
    
    anton "Commander . . . Potato, was it?"
    
    play silsound4 "se/silly21.ogg"
    show hitora hat moe1
    
    hit "C-Commander Yamato!"
    
    show horthy moe
    
    hor "Have you guys kissed yet?"
    hit ". . . that's none of your business. Besides, he's busy fighting for the Vitalians in Zomali."
    "As far as she knows. Rinni still hasn't told her what has happened to him."
    
    show horthy happy
    show hitora hat angry
    with dissolve
    
    hor "So . . . you have kissed him?"
    hit "N-No way! I wouldn't lower myself to kiss a foreigner like him!"
    
    play silsound3 "se/silly20.ogg"
    show antoness happy
    
    anton "So you've thought about it?"
    
    show hitora hat embarrassed
    with dissolve
    
    "Hitora goes silent."
    
    show antoness moe
    with dissolve
    play silsound4 "se/silly14.ogg"
    
    anton "Don't tell me . . . you guys have actually kissed already?"
    
    play silsound2 "se/silly2.ogg"
    show hitora hat moe1
    
    hit "Shut up!"
    "Poor genocidal dictator. Everyone keeps ganging up on her like this . . ."
    
    show horthy determined
    
    hor "You shouldn't drag things out too long. He might grow bored and fall in love with someone else."
    
    show hitora hat angry
    with dissolve
    
    hit "I'm n-not dragging anything out! He's busy. And I'm the Füühbar and the Füühbar is one. I'm fine being on my own!"
    
    show antoness normal
    show horthy normal
    
    hit "If Yamato wants to grope other girls, that's entirely his business."
    hor ". . . . . . . . ."
    anton ". . . . . . . . ."
    hit "What? What is it?"
    
    show antoness happy
    
    anton "When you deny things so strongly like that . . ."
    
    play silsound4 "se/silly19.ogg"
    show horthy moe
    show hitora hat moe1
    
    hor "You really must like him, huh?"
    anton "Of course. Since they've already both been smooching like lovesick puppies . . ."
    
    play silsound2 "se/silly17.ogg"
    
    hit "Drop it or I'll annex both of your countries for real, regardless of the pact!"
    "It really is a touchy subject."
    
    hide hitora
    hide horthy
    hide antoness
    with dissolve
    
    "Across the hall, seated at a smaller table, Prince Paulie grumbles and plots to himself."
    
    show politician determined
    with dissolve
    
    paul "What a humiliation . . . not only have I been forced to sign this embarrassing treaty just to save Serpana . . ."
    
    play silsound2 "se/silly9.ogg"
    
    paul ". . . but they went and sat me at the kid's table! I've never been so humiliated!"
    "Playing with his shrimpfork, the tired monarch glares at the Füühbar, throned at the head table."
    paul "Adorofia Hitora . . . just what kind of dictator are you . . ."
    "With resentment and tension running high, the {i}Triple Pact{/i} is ratified and secured."
    "As the dictator of Germania and the lead nations celebrate, dangerous feelings run beneath the surface."
    "Will this come back to haunt the Füühbar? Maybe, in time . . ."
    
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    stop music fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000210

#####################################################################################################################################################
#sc0000210	-	Messe in Grecia/Waiting on reinforcements
#####################################################################################################################################################
label sc0000210:
    scene black
    with fade
    
    $ mouse_visible = False
    show expression Text(_("Deep within Epirus, at the frontlines . . ."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx "se/tank_invasion.ogg" fadein 3.0
    play soundfx2 "se/battle3.ogg" fadein 3.0
    scene desert_bunker
    with fade
    play music "music/rinni.ogg"
    
    "Following the battle of Klisura Pass, the Grecian advance has finally come to a halt."
    "The enemy are lacking in supplies, and the stingy support of the Britannians has had little effect."
    "However, although Vitalia has ample materiel, the soldiers are tired, worn down from the war of attrition."
    "Weeks of fighting have been a knackering humiliation, and morale is slowly being weakened."
    
    show messe moe
    with dissolve
    play silsound5 "se/silly2.ogg"
    
    messe "{i}Il Douché!{/i} Please hurry! I can't hold out much longer . . ."
    "Messe has been doing her best to hold off the advancing Grecian forces as they plunged into Epirus."
    "Now that the enemy has halted, Rinni has promised to send reinforcements for a new offensive."
    
    show messe determined
    with dissolve
    
    messe "If you don't hurry up and send something, we'll have to wait for the Germanians instead!"
    "With the Füühbar alerted to the disaster in Grecia and weakening on the flanks, the Germanians may soon get properly involved."
    "Before the {i}Vehrmaxt{/i} approaches, the Vitalians want to score a quick victory against Papagos and save Epirus."
    messe "We have to win. We can't let this turn into a complete disaster. Mussorinni . . . don't abandon us . . ."
    
    play silsound4 "se/poke.ogg"
    show messe shock
    
    rin hat moe4 "Did somebody say my name?"
    
    show messe shock at right25
    with ease
    play sound6 "se/walk.ogg"
    play sound2 "se/win.ogg"
    show rinni hat moe4 at center
    show cavallero determined at left25
    with dissolve
    
    "Out of nowhere, {i}Il Douché{/i} Mussorinni appears at the front, with Cavallero in tow."
    messe "No way. {i}Il Douché!{/i} What are you doing here?"
    rin "You wanted some more divisions to help defend Epirus, right? So I brought them myself!"
    
    play soundfx3 "se/march.ogg" fadein 2.0
    show object_vitalianreinforcements at tankpos
    with dissolve
    
    "Messe peers behind her leader and spies a huge column marching through the hills towards their camp."
    rin "Ten extra divisions, with around one hundred and fifty bombers, and two hundred fighter planes!"
    "Alongside the new recruits, violent vascist cadres and top-ranking officials march with them, to help guide the fight."
    
    hide object_vitalianreinforcements
    show messe determined
    show rinni hat determined
    with dissolve
    stop soundfx3 fadeout 2.0
    
    messe "Then that means . . . it's almost time for the offensive!"
    cavallero "Bingo. We're going to send those Grecians back to the stone age!"
    rin "It'll be easy-peasy. Grecia has no war industry and can only count on supplies from Britannia."
    
    show messe normal
    
    messe "But then . . . why are you here, {i}Il Douché?{/i} It's not safe at the front."
    rin "I had to come and see it for myself. After all, we have to score a victory before the Germanians show up."
    messe "But why?"
    rin "We have to prove to Adorofia Hitora that we don't need her help and that we're independent!"
    
    play silsound4 "se/silly6.ogg"
    show cavallero shock
    show messe shock
    show rinni hat moe1
    
    messe "But didn't she already lend you that Zipanguese commander, to fight for you in Gypta and Zomali?"
    messe "Not to mention that Graziani has already sent a direct request to Altberlin, asking for help in Cyracana . . ."
    
    play silsound3 "se/silly5.ogg"
    show rinni hat moe2
    
    rin "Forget about small details like that! I can't have Hitora winning all my battles for me!"
    
    show cavallero determined
    show messe determined
    show rinni hat determined
    with dissolve
    
    rin "If we can do this, Vitalia's reputation will be saved."
    messe "U-Understood."
    cavallero "Let us score a victory, for all Vitalians."
    "One final offensive from the Vitalian side will determine their place in the world order."
    "Can Mussorinni save face against the Grecian onslaught? Or is it already futile?"
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000221
    
#####################################################################################################################################################
#sc0000221	-	Simovic coup / Overthrows Paul
#####################################################################################################################################################
label sc0000221:
    play soundfx "se/battle2.ogg" fadein 3.0
    play soundfx2 "se/battlecry2.ogg" fadein 3.0
    play soundfx3 "se/cheer.ogg" fadein 3.0
    scene day3
    with fade
    play music "music/horror.ogg"
    
    "Trouble in Serpana has finally reached a breaking point . . ."
    "Anger over the signing of the {i}Triple Pact{/i} has led to a {i}coup d'etat{/i} in the capital Singidun."
    "A group of violent officers and soldiers has taken over, infuriated at the government."
    
    scene city2
    with dissolve
    show object_serpanacoup at tankpos
    with dissolve
    
    "In only a few hours, the coup has succeeded in deposing members of Paulie's cabinet."
    "Rebel officers have assumed control of important buildings, taking over bridges, post offices and barracks."
    "Mobs run riot around the city streets, hoisting banners and flags, storming the government headquarters."
    "Despite one small fatal accident, it has been a bloodless coup, with a great amount of popular support."
    
    hide object_serpanacoup
    with dissolve
    play sound5 "se/walk.ogg"
    show simovic happy
    with dissolve
    
    "Simovic has placed herself at the center, helping to lead this rebel government as it takes power."
    simovic "This is it . . . this is our moment. This is the end of Hitora's evil pact and the rebirth of Serpana."
    "The elderly pensioner smirks to herself as the rebellion picks up momentum."
    "A national unity government has been declared under Petey, Prince Paulie's young nephew."
    "Together with this new monarch, Simovic hopes to align her country to Britannia and the {i}Alliance{/i} movement."
    
    show simovic determined
    with dissolve
    
    simovic "Place more guards at the entrance there, round up the last of the ministers and secure their homes."
    simovic "We don't stop until we can guarantee the full capture and control of the government . . ."
    "Pulling the strings behind the operation, Simovic works with the rebel soldiers to establish a new order."
    simovic "Together Petey, we're going to run this country differently . . . without the Füühbar's help . . ."
    
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    stop soundfx3 fadeout 3.0
    scene day3
    with dissolve
    play soundfx4 "se/birds.ogg" fadein 3.0
    
    "Faraway, the newly-deposed monarch is on the run, out in the countryside, fearing for his life."
    
    play sound5 "se/train_whistle.ogg"
    scene countrylane_day
    with dissolve
    show politician determined at left3
    show cvetkovic normal at right3
    with dissolve
    
    "Prince Paulie, with a suitcase packed ready for his holiday, has been caught off guard."
    "Arranging to meet his prime minister at a train station to the south, he grumbles to himself at this turn of fortune."
    paul "The people are rioting, the army's against me, my holiday's going to be cancelled . . . what am I to do?"
    cvetkovic "You could stand down. Disappear into exile, my liege."
    paul "Don't be so impertinent . . . to give up the throne so easily. It would be an utter humiliation."
    "Not to mention, he has the hotel room booked and has already claimed a poolside deckchair with his towel."
    
    play silsound5 "se/silly12.ogg"
    show cvetkovic annoyed
    
    cvetkovic "What else can you do? The government has already been defeated . . . the coup was a success."
    "Prince Paulie bites his bottom lip. It really seems there's no hope for it."
    cvetkovic "Get on a train, find a safe haven and escape the continent. Maybe you can survive the war in one piece."
    paul "Maybe . . . maybe you're right. Exile might be my only option now."
    "With the capital city in the hands of the rebels, there isn't much that Paulie can do to reclaim power."
    "Brought down by the signing of the pact with Germania, his countrymen have rejected him."
    
    scene day3
    with dissolve
    
    "The coup in Singidun was a great success. Petey has been installed with Simovic pulling the strings."
    "Prince Paulie has decided to disappear into exile, easily defeated and overthrown by the mob."
    "Now, Serpana will become an {i}Alliance{/i}-aligned nation, and reject Germanian overtures for friendship."
    ch hat happy "It would seem that Serpana has found its soul once more . . ."
    "This is a great morale-boost for the {i}Alliance{/i} as they continue their fightback against the {i}Axle{/i}."
    "Just how will the Füühbar Adorofia Hitora take this news?"
    
    stop music fadeout 3.0
    stop soundfx4 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000212
    
#####################################################################################################################################################
#sc0000212	-	Hitora/Rommel sent to Cyracana to reclaim territory
#####################################################################################################################################################
label sc0000212:
    play soundfx "se/march3.ogg" fadein 3.0
    play soundfx2 "se/tank_far.ogg" fadein 3.0
    play soundfx3 "se/airbase.ogg" fadein 3.0
    scene armycamp
    with fade
    play music "music/bravery.ogg"
    
    "While Germania concerns itself with securing its southern flanks, Vitalia continues to have trouble in the deserts . . ."
    "Graziani, and now Gariboldi, are at their wits end, pushed out of Benghatza and along the coast towards Tripolita."
    "Morale is at an all-time low and many Vitalian soldiers simply allow themselves to be captured."
    
    show hitora hat angry at left3
    show rommel annoyed at right3
    with dissolve
    
    "It's because of these developments that the Füühbar has called on Erwina Rommel for a private meeting."
    hit "We need to do something about Cyracana. If this situation continues, it might be the end of the desert campaign . . ."
    "The haughty Britannians smirk as they cut through the Vitalian lines like a hot knife through butter."
    "To them, the enemy soldier is not a soldier from within. Their garrison mentality affects their determination to fight."
    hit "Those Britannians . . . always invading other people's sovereign territory like that!"
    
    play silsound5 "se/silly20.ogg"
    show rommel moe1
    show hitora hat worry
    
    rom "Hey, don't you have any self-awareness? Pot calling the kettle black . . ."
    hit "W-When I do it, it's different!"
    rom "Uh huh, and how's that?"
    
    play silsound2 "se/poke.ogg"
    show hitora hat angry
    
    hit "I'm . . . upsizing, I guess? I mean, Germania needs the retail space."
    
    play sound4 "se/map.ogg"
    show rommel normal
    with dissolve
    
    "Reaching into her coat pocket, Hitora pulls out a folded telegram."
    hit "Anyway, Marshal Graziani sent us an urgent message, asking that we send reinforcements to help repel the enemy."
    rom "Graziani did?"
    hit "At least one of the Vitalians is being honest with us. The situation is dire. They need our help."
    rom "Ridiculous. Of course, you rejected the proposal?"
    "After all, this is Vitalia's war. Germania shouldn't draw itself into such a desperate conflict."
    
    play silsound3 "se/poke.ogg"
    show hitora hat moe2
    show rommel moe2
    
    hit "Not exactly . . ."
    rom "Don't tell me you actually accepted the offer?!"
    
    show hitora hat angry
    show rommel moe1
    with dissolve
    
    hit "But this is another chance to humiliate Churchill. Imagine if her troops are beaten on yet another front."
    rom "I don't know about that . . ."
    hit "If we can drive her tanks back across the desert, it'll prevent Britannia knocking Vitalia out of the war."
    rom "Would that be such a bad thing?"
    "Still, probably better to keep allies around rather than lose them, no matter how bad they are at fighting . . ."
    
    play silsound6 "se/silly2.ogg"
    show rommel moe2
    show hitora hat moe1
    
    hit "Fine. If you don't want your own {i}Panzy Armee{/i}, then I'll give the job to someone else."
    rom "Wait a minute! Did you say . . . {i}Panzy Armee?{/i}"
    
    show rommel embarrassed
    show hitora hat normal
    with dissolve
    
    "Hitora sighs manipulatively, and glances into the distance, reminiscing."
    hit "I was going to give it a catchy name, like the {i}Dessous Afrikaa Korps{/i}, with its own logo and everything . . ."
    hit "But . . . if you're not interested in helping out an ally, I'll make someone else a {i}Generalleutnant{/i} . . ."
    
    play silsound5 "se/silly4.ogg"
    show hitora hat worry
    show rommel moe2
    
    rom "Wait! Waitwaitwaitwaitwaitwaitwaitwait!"
    
    show hitora hat moe1
    
    hit "Stop whining!"
    
    play sound4 "se/punch.ogg"
    play sound2 "se/hit.ogg"
    play sound3 "se/bloop.ogg"
    show rommel moe2
    with hpunch
    with vpunch
    
    "Rolling up a newspaper, the Füühbar smacks the foxgirl across the snout."
    rom "Yah! I'm sorry! But I wanna go now! I want my own {i}Dessous Afrikaa Korps{/i}, with the logo and stuff!"
    hit "One second you want to stay in, the next you want to go out. Make up your mind, won't you?!"
    "Rommel, the foxgirl, will be heading to Cyracana to help salvage the Vitalian position and fight off the Britannians."
    "Will she manage to turn the tide with her foxy ways?"
    
    show rommel moe1
    show hitora hat worry
    with dissolve
    play silsound6 "se/silly12.ogg"
    
    rom "By the way, did you hear about Prince Paulie being overthrown in Serpana?"
    hit "What?!! When did this happen?!!"
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    stop soundfx3 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000222
    
#####################################################################################################################################################
#sc0000222	-	Tito in shock
#####################################################################################################################################################
label sc0000222:
    scene black
    with fade
    
    $ mouse_visible = False
    show expression Text(_("Meanwhile, in the dark forests of Serpana . . ."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx "se/birds.ogg" fadein 3.0
    play soundfx2 "se/outdoor_crowd.ogg" fadein 3.0
    scene woodland_cave
    with fade
    play music "music/drama.ogg"
    
    "Following Simovic's coup, many civilians across the country are shocked and confused."
    "It's an unstable moment in the history of their nation."
    "With the unpopular royal dictatorship gone, radio messages and dropped pamphlets have proclaimed Petey as king."
    "From abroad, foreign governments have chimed in, with Churchill declaring that {i}'Serpana has found its soul'{/i}." 
    "Xommunist partisans, western-allied rebels and pro-Germanian vascists now begin to plot their next moves."  
    
    show tito shock
    with dissolve
    play silsound5 "se/silly9.ogg"
    
    tito "Comrades, hold fast! Don't let the vascists distract you. We still have work to do!"
    "Surprised by the sudden turn of events, Tito does her best to maintain order in her camp."
    
    show tito determined
    with dissolve
    
    tito "Though they are not xommunists, we must show our support for the new, anti-Germanian government."
    tito "We should take to the streets, waving our banners and taking part in the new kingdom!"
    "Tito and her gang had no love for the old order, or the way in which Prince Paulie was forced to ally with Hitora."
    "Now that Simovic has taken command and placed Prince Paulie's nephew, Petey, on the throne, things may stabilize."
    
    show tito happy
    with dissolve
    
    tito "Today, we work with these monarchists. Tomorrow, we rise up and take control for ourselves."
    "Xommunism is very much alive in these woods and soon it will be in full swing on the streets."
    "Tito plans demonstrations and marches, displaying herself as an opponent of the old vascists and appeasers."
    "Will this very unstable situation pan out well for the rebels?"
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000213
    
#####################################################################################################################################################
#sc0000213	-	Briefing on Serpana/Bolga
#####################################################################################################################################################
label sc0000213:
    play soundfx "se/room.ogg" fadein 3.0
    play soundfx2 "se/train.ogg" fadein 3.0
    scene train_country_travel
    with fade
    play music "music/yandere.ogg"
    
    "Aboard the {i}Füühbarsonderzug{/i}, news of the coup in Serpana has reached the Füühbar's ears."
    
    play sound4 "se/break.ogg"
    play silsound6 "se/silly1.ogg"
    show hitora hat moe1
    with hpunch
    with vpunch
    
    hit "Dang it! That does it! Those sneaks! Those evil, treacherous losers! They're all dead!" 
    "Hitora takes the coup as a personal insult and is determined to have her vengeance."
    
    play silsound3 "se/silly17.ogg"
    
    hit "I'm going to destroy Serpana, militarily and as a state, with pitiless harshness! Everything will burn!"
    goeb scared "D-Don't you think you should c-calm down and wait to see w-what Simovic's regime is like? They m-might be friendly."
    hit "I am calm! See how calm I am?! I'm not shaking at all!"
    
    play silsound2 "se/silly4.ogg"
    
    "The furious girl holds out her hand, which is flailing around violently from the rage."
    
    show hitora hat angry
    with dissolve
    
    hit "And I won't wait around for fake declarations of loyalty from the new government! They're all traitors."
    gor pout "You're not going to wait around? What are you planning?"
    hit "They're dead meat! I'm going to wipe that stupid country from the face of the earth!"
    "Here we go again. Hitora is impossible to control when she's in one of her moods."
    "Unfortunately, that's often when most of her strategic decisions get made . . ."
    
    stop music fadeout 3.0
    play sound6 "se/knock.ogg"
    show hitora hat normal
    with dissolve
    
    "Suddenly, they're interrupted by a knocking noise at the door."
    gor "Eh? Who is it?"
    
    play silsound5 "se/silly14.ogg"
    play silsound3 "se/silly24.ogg"
    show hitora hat worry
    
    rin hat moe2 "Hitoraaaaaaaaaaaaaaaaaaaaa!!"
    
    play sound6 "se/boom.ogg"
    play sound2 "se/damage.ogg"
    queue sound2 "se/creak.ogg"
    show hitora hat worry
    with hpunch
    with vpunch
    play music "music/pantsu.ogg"
    
    "The door gets broken down with a loud boom as {i}Il Douché{/i} Mussorinni of Vitalia bursts into the room."
    
    play sound5 "se/run.ogg"
    show hitora hat worry at left3
    with ease
    show rinni hat moe2 at right3
    with easeinright
    
    rin "Hitoraaaaaaa! It's bad! It's really bad!"
    hit "R-Rinni? What are you doing here?! How did you get on board? This is a moving train!"
    gor "And did you really need to break the door like that . . ."
    
    play silsound2 "se/silly26.ogg"
    show rinni hat moe1
    show hitora hat moe1
    
    rin "Hey guys . . . I really need your help . . . I don't want it but I neeeeeeeeeeed it!"
    hit "Don't tell me, it's another one of your failed invasions? The war with Grecia in Epirus, right?"
    
    show rinni hat worry
    show hitora hat angry
    with dissolve
    
    rin "I t-thought we could hold them off on our own, but . . . it turns out winning wars is, like, super difficult . . ."
    "As they discuss the situation, some guards fix the shattered door back into its frame."
    hit "So you want Germania to come to the rescue again, huh? You want us to fight for you in Grecia?"
    rin "I . . . well . . ."
    hit "You really want to cause us trouble, again, and have us fixing your mistakes, again?"
    rin ". . . {i}grazie{/i}."
    hit "Nnnnnnnnnnnnnnn . . ."
    
    play silsound4 "se/poke.ogg"
    show hitora hat moe2
    show rinni hat shock
    
    hit "Fine. It actually matches up with my new plans perfectly . . ."
    rin "New plans?"
    
    stop music fadeout 3.0
    hide rinni
    with dissolve
    play sound2 "se/map.ogg"
    play sound3 "se/map2.ogg"
    show hitora at right15
    with ease
    show map_tactical7 at tacticalpos
    with dissolve
    
    "Hitora pulls out a prepared map, laying out a decisive military campaign against Serpana and Grecia."
    
    play music "music/evil.ogg"
    
    rin hat shock "Eh? You came prepared with slides."
    hit "Any sensible dictator makes invasion plans for anywhere. There's no sense in trusting half of what our {i}'allies'{/i} say."
    "And yet a maniacal dictator is meant to be more reliable?"
    
    show hitora hat angry
    with dissolve
    
    hit "If Serpana is so desperate to be independent and break its promises, we'll just have to teach these fools a lesson . . ."
    hit "And if you can't hold onto Epirus without our help, then we'll just have to invade Grecia too!"
    rin "Huh? You're planning on getting Rumanum and Hang involved? Bolga too . . ."
    hit "Well, why else do you think we've been positioning our forces on their borders?"
    rin "To offer guidance and training to our friends and allies?"
    
    play silsound4 "se/silly4.ogg"
    show hitora hat moe1
    
    hit "Peh! It was to protect the oilfields and supplies of goulash from Starin and her friends."
    
    show hitora hat angry
    with dissolve
    
    hit "We will begin with an attack on Serpana from all sides. Germania, Hang, Rumanum, Bolga . . . Vitalia too."
    gor pout "Pressing on the country from each direction, with much stronger and better equipped armies, would force their hand."
    "With all this firepower, the inner circle can't foresee this war lasting much longer than a few weeks."
    hit "Then . . . we will strike south towards Grecia and salvage your pathetic Vitalian operation there."
    
    play silsound5 "se/silly3.ogg"
    
    rin hat moe2 "S-Stop being so mean!"
    hit "I'm a dictator. I can do far worse things than say mean words . . ."
    gor "You need to stop promising her things like this. This girl's campaigns are nothing but trouble."
    
    play sound2 "se/map.ogg"
    play sound3 "se/map2.ogg"
    hide map_tactical7
    with dissolve
    show hitora hat angry at left3
    with ease
    show rinni hat worry at right3
    with easeinright
    
    "The Füühbar rolls away the map and then glares at Rinni, like she had let off a bad smell or something."
    hit ". . . . . . . . ."
    rin "What? Was it something I said?"
    hit "There's a small matter we need to discuss before I commit to saving your stinking little campaign."
    rin "Eh?"
    
    play silsound5 "se/silly10.ogg"
    show rinni hat moe1
    show hitora hat moe1
    
    hit "Where . . . is . . . my . . . bodyguard? Where is he? Where is Commander Yamato Yamamoto?"
    rin "Eh, well, that's . . ."
    hit "I won't help you with Epirus or Grecia unless you tell me."
    "Backed into a corner and in desperate need, Mussorinni weighs up her options."
    
    play silsound4 "se/silly7.ogg"
    show hitora hat worry
    show rinni hat moe2
    
    rin "F-Fine! He's . . . he's fighting for me in Grecia, that's it! He said he'd be waiting for you in Athenia once you intervened!"
    hit "Huh? Yamato said that? So he wants me to intervene as well then . . . he'll be waiting for me in Athenia."
    rin "Yeah, t-that's right, ahaha . . . so you'll do it right? You'll help me out?"
    
    show hitora hat angry
    show rinni hat determined
    with dissolve
    
    hit "Very well. Germania will take on Grecia for you. Besides, it will prevent any future interference in the east . . ."
    rin "The east?"
    hit "Never you mind. Since everyone else is busy, Field Marshal Listte will take responsibility for this campaign."
    
    play sound3 "se/walk.ogg"
    
    listte determined "Of course, my Füühbar."
    "A decorated general in the corner chimes in, ready to help fight the campaign."
    hit "Brauchitsch, Ewalda and others will focus on Serpana. Let's take out these allies of Britannia, and finish them off!"
    ewalda "Yes, my Füühbar!"
    brauchitsch ". . . . . . . . ."
    "Glancing over the maps and the statistics, the generals start to help formulate and refine the prepared proposals for the attack."
    "Serpana's coup has enraged the Füühbar and the Germanian military echelons. For this bold defiance, they will reap fire."
    hit "War isn't a game, after all . . . well, this is a game, but . . . oh, never mind."
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    #STRUCTURE CHANGES
    #SERPANA REMOVE
    $ active_armies_items.pop("insignia-armeepanzergruppeguderian", armeepanzergruppeguderian_name)
    $ active_divisions_items.pop("insignia-infanteriedivision002", infanteriedivision002_name)
    $ active_divisions_items.pop("insignia-infanteriedivision004", infanteriedivision004_name)
    $ active_divisions_items.pop("insignia-infanteriedivision013", infanteriedivision013_name)
    $ active_divisions_items.pop("insignia-infanteriedivision019", infanteriedivision019_name)
    $ active_spezialformations_items.pop("insignia-schutzenbrigade", schutzenbrigade_name)
    
    #SERPANA ADD
    $ active_armies_items.update({
        "insignia-armee011": armee011_name,
        "insignia-armee015": armee015_name,
        "insignia-armee017": armee017_name,
        "insignia-armeepanzergruppe002": armeepanzergruppe002_name,
        "insignia-armeepanzergruppe003": armeepanzergruppe003_name,
        "insignia-armeenorda": armeenorda_name
    })
    
    $ active_korps_items.update({
        "insignia-panzerkorps014": panzerkorps014_name,
        "insignia-armeekorps040": armeekorps040_name,
        "insignia-armeekorps041": armeekorps041_name,
        "insignia-panzerkorps046": panzerkorps046_name,
        "insignia-armeekorps049": armeekorps049_name,
        "insignia-panzerkorps051": panzerkorps051_name,
        "insignia-panzerkorps052": panzerkorps052_name
    })
    
    $ active_divisions_items.update({
        "insignia-infanteriedivision016": infanteriedivision016_name,
        "insignia-infanteriedivision060": infanteriedivision060_name,
        "insignia-infanteriedivision073": infanteriedivision073_name,
        "insignia-infanteriedivision079": infanteriedivision079_name,
        "insignia-infanteriedivision125": infanteriedivision125_name,
        "insignia-infanteriedivision132": infanteriedivision132_name,
        "insignia-infanteriedivision183": infanteriedivision183_name,
        "insignia-infanteriedivision294": infanteriedivision294_name,
        "insignia-infanteriedivision538": infanteriedivision538_name,
        "insignia-panzerdivision005": panzerdivision005_name,
        "insignia-panzerdivision008": panzerdivision008_name,
        "insignia-panzerdivision009": panzerdivision009_name,
        "insignia-panzerdivision011": panzerdivision011_name,
        "insignia-panzerdivision014": panzerdivision014_name,
        "insignia-lightdivision101": lightdivision101_name, 
        "insignia-mountaindivision001": mountaindivision001_name,
        "insignia-mountaindivision004": mountaindivision004_name,
        "insignia-zzdivision001": zzdivision001_name,
        "insignia-zzdivision002": zzdivision002_name,
        "insignia-aufklarungsgruppe121": aufklarungsgruppe121_name,
        "insignia-kampfgeschwader002": kampfgeschwader002_name,
        "insignia-kampfgeschwader003": kampfgeschwader003_name,
        "insignia-kampfgeschwader004": kampfgeschwader004_name,
        "insignia-kampfgeschwader051": kampfgeschwader051_name,
        "insignia-lehrgeschwader001": lehrgeschwader001_name,
        "insignia-lehrgeschwader002": lehrgeschwader002_name,
        "insignia-sturzkampfgeschwader002": sturzkampfgeschwader002_name,
        "insignia-sturzkampfgeschwader003": sturzkampfgeschwader003_name,
        "insignia-sturzkampfgeschwader077": sturzkampfgeschwader077_name,
        "insignia-jagdgeschwader027": jagdgeschwader027_name,
        "insignia-jagdgeschwader054": jagdgeschwader054_name,
        "insignia-jagdgeschwader077": jagdgeschwader077_name,
        "insignia-zerstorergeschwader026": zerstorergeschwader026_name
    })
    
    $ active_spezialformations_items.update({
        "insignia-biggermania": biggermania_name
    })
    
    #Map Data
    $ mapdata = ScreenData("geomap2", "map12", "easternmap")
    
    #Mission Data
    $ active_invasionbeacons_items.pop("bat000048", [bat000048_description, bat000048_title, bat000048_type, bat000048_x, bat000048_y])
    $ active_invasionbeacons_items.update({"bat000049": [bat000049_description, bat000049_title, bat000049_type, bat000049_x, bat000049_y]})
    
    #Mission Assign
    $ log.assign("[bat000049_title]")
    
    #Allegiances Data
    $ bolga_alignment = germania_empire
    $ zomali_alignment = britannia_empire
    $ singidun_governor = "Simovic"
    $ singidun_governor_pic = "{image=side simovic determined}"
    $ singidun_command = command_three
    $ singidun_management = management_three
    $ singidun_influence = influence_two
    $ singidun_hostility = hostility_unfriendly
    $ active_maptown_items.update({"singidun": [singidun_name, singidun_size, singidun_governor, singidun_governor_pic, singidun_hostility, singidun_alignment, singidun_population, singidun_publicorder, singidun_influence, singidun_command, singidun_management, singidun_farming_worth, singidun_mining_worth, singidun_industry_worth, singidun_trade_worth, singidun_entertainment_worth, singidun_military_worth, singidun_corruption_worth, singidun_unlocktown, singidun_martial, singidun_siege, singidun_company_img, singidun_company_text, .62, .5]})
    $ burburra_alignment = zomali_alignment
    $ burburra_publicorder +=290
    $ burburra_governor = "Jumbo"
    $ burburra_governor_pic = "{image=side jumbo normal}"
    $ burburra_command = command_two
    $ burburra_management = management_two
    $ burburra_influence = influence_three
    $ burburra_hostility = hostility_protectorate
    $ burburra_allegiance = allegiance_axle
    $ burburra_martial = [
        "panzer_crusader_profile",
        "panzer_crusader_profile"
        ]
    $ active_maptown_items.update({"burburra": [burburra_name, burburra_size, burburra_governor, burburra_governor_pic, burburra_hostility, burburra_alignment, burburra_population, burburra_publicorder, burburra_influence, burburra_command, burburra_management, burburra_farming_worth, burburra_mining_worth, burburra_industry_worth, burburra_trade_worth, burburra_entertainment_worth, burburra_military_worth, burburra_corruption_worth, burburra_unlocktown, burburra_martial, burburra_siege, burburra_company_img, burburra_company_text, .92, .965]})
    $ benghatza_governor = "Gariboldi"
    $ benghatza_governor_pic = "{image=side gariboldi normal}"
    $ benghatza_command = command_one
    $ benghatza_management = management_two
    $ benghatza_influence = influence_one
    $ active_maptown_items.update({"benghatza": [benghatza_name, benghatza_size, benghatza_governor, benghatza_governor_pic, benghatza_hostility, benghatza_alignment, benghatza_population, benghatza_publicorder, benghatza_influence, benghatza_command, benghatza_management, benghatza_farming_worth, benghatza_mining_worth, benghatza_industry_worth, benghatza_trade_worth, benghatza_entertainment_worth, benghatza_military_worth, benghatza_corruption_worth, benghatza_unlocktown, benghatza_martial, benghatza_siege, benghatza_company_img, benghatza_company_text, .61, .82]})
    $ bolga_hostility = hostility_besties
    $ bolga_allegiance = allegiance_axle
    $ bolga_coa = coa_alliance
    $ active_allegiances_items.update({"bolga": [bolga_motto, bolga_flag, bolga_flag2, bolga_description, bolga_name, bolga_coa, bolga_hostility, bolga_power, bolga_allegiance, bolga_text]})
    $ serdica_hostility = bolga_hostility
    $ serdica_allegiance = bolga_allegiance
    $ active_maptown_items.update({"serdica": [serdica_name, serdica_size, serdica_governor, serdica_governor_pic, serdica_hostility, serdica_alignment, serdica_population, serdica_publicorder, serdica_influence, serdica_command, serdica_management, serdica_farming_worth, serdica_mining_worth, serdica_industry_worth, serdica_trade_worth, serdica_entertainment_worth, serdica_military_worth, serdica_corruption_worth, serdica_unlocktown, serdica_martial, serdica_siege, serdica_company_img, serdica_company_text, .67, .495]})
    
    #Additional Map Data
    $ map_update_title = map_update_title14
    $ map_update_subtitle = map_update_subtitle14
    $ map_update_description = map_update_description14
    $ map_update_happen = True
    
    #Go To Map
    jump map_begin
    
    
#####################################################################################################################################################
#bat000049	-	Operation Groundhog: Battle of Singidun
#####################################################################################################################################################
label bat000049:
    hide screen mapchoice1
    $ renpy.block_rollback()
    $ _rollback = True
    $ store.text_history_enabled = True
    window hide
    play sound6 "se/march2.ogg"
    stop music fadeout 2.0
    scene black
    with dissolve
    
    $ mouse_visible = False
    show expression Text(_("[bat000049_title]"), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    show expression Text(_("In the skies over Singidun, Serpana"), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3     
    $ mouse_visible = True
    
    play soundfx "se/airbattle.ogg" fadein 3.0
    play soundfx2 "se/plane.ogg" fadein 3.0
    scene sky1
    show planes
    show spitfire1
    show cloudsflip
    with fade
    play music "music/fury.ogg"
    
    "In the clouds over Singidun, the capital city of Serpana, the native air force battles it out with {i}Ruftwaffe{/i} fighters."
    "With their own mass-produced {i}Hurrycanes{/i}, the {i}Royal Serpana Air Force (VVKS){/i} bravely defend their home country."
    "Not only do they have the Germanians to deal with, but also the {i}Douché Aeronautica{/i}, Vitalia's air force, and invaders from Bolga."
    "Other groups do their best to offer aerial support to ground troops, taking on mechanized columns."
    "Squadrons strafe at enemies on the ground, sometimes defending the very airbases they took off from moments before."
    simovic determined "As head of the army and the air force, I implore you all . . . fight bravely to defend your homeland!"
    
    play sound4 "se/radio.ogg"
    
    "Simovic's voice crackles over the radio, urging the pilots on to victory."
    "Dangerous dogfights high above the cities and plains will determine the fate of the invasion . . ."
    
    stop sound4 fadeout 1.0
    stop soundfx fadeout 1.0
    stop soundfx2 fadeout 1.0
    scene black
    with fade
    
    $ mouse_visible = False
    show expression Text(_("At the same time, on the ground below . . ."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve    
    pause 0.3
    $ mouse_visible = True
    
    play soundfx3 "se/tank_invasion.ogg" fadein 3.0
    play soundfx4 "se/battle.ogg" fadein 3.0
    play soundfx5 "se/bombers.ogg" fadein 3.0
    scene farm_day
    with fade
    
    "The Germanian ground invasion moves swiftly, with a three-pronged approach on Singidun."
    
    show object_serpanainvasion at tankpos
    with dissolve
    
    "Tanks move from over the border in Hang, Osta, Bolga and Rumanum, blasting their way across the enemy lines."
    "The invaders criss-cross with armored columns, as Vitalia and Hang open up other fronts in the west and the north."
    "With the Serpana forces harrassed by the {i}Ruftwaffe{/i}, few defenders make it beyond the capital to fight back."
    
    hide object_serpanainvasion
    with dissolve
    show speedlines with circleirisout
    
    ewalda "L-Let's destroy the enemy armies and capture the capital!"
    
    stop music fadeout 1.0
    stop soundfx3 fadeout 1.0
    stop soundfx4 fadeout 1.0
    stop soundfx5 fadeout 1.0
    scene black
    with pixellate
    
    jump bat000049_begin
    
label bat000049_begin:
###########################################################################
    #bat000049	-	Battle
###########################################################################
    
    #History Block
    $ renpy.block_rollback()
    $ store.text_history_enabled = False
    $ _rollback = False
    $ config.skipping = False
    
    #Enemy Team Set
    $ enemy_team = BaseTeam("Enemy", Solid("#000000", xysize=(50,50)), limit=50)
    $ enemy_team.add_fighter("enemy_serpana_gunner_heer5")
    $ enemy_team.add_fighter("enemy_panzer_renaultr35serpana")
    $ enemy_team.add_fighter("enemy_serpana_antitank_heer5")
    
    #Playing For New Side Set - Axle
    $ empty_data("fighter")
    $ load_data(axle_fighter_set, "fighter")

    # Selection Screen Set
    $ airsupport_section_unlocked = False
    $ infantry_section_unlocked = True
    $ panzer_section_unlocked = True
    $ antitank_section_unlocked = True
    $ commander_section_unlocked = True
    $ specialgroup_section_unlocked = True
    $ player_team = BaseTeam("Player", Solid("#000000", xysize=(50,50)), limit=50)
    play battlemusic "music/map3.ogg"
    call screen non_battle_party_screen

    # Battle Set
    $ config.skipping = False
    $ yamato_lvlcheck()
    stop battlemusic fadeout 1.0
    scene black
    $ renpy.pause(1.0, hard=True)
    play battlesfx "se/battle4.ogg" volume 0.25
    play battlemusic "music/battle_forest.ogg"
    $ renpy.block_rollback()
    $ fight_end = "bat000049_aftermath"
    $ game = Battleground("Battle Stage   |   Operation Groundhog", player_team.store[0], enemy_team.store[0], "forest")
    $ battle_terrain = "ground"
    $ battleground_bg = "background_bunker"
    $_game_menu_screen = None
    $ config.skipping = False
    $ config.keymap['skip'].remove('K_LCTRL')
    $ config.keymap['skip'].remove('K_RCTRL')
    $ config.keymap['hide_windows'].remove('h')
    $ renpy.clear_keymap_cache()
    call screen battle_screen(bg=battleground_bg, disc="plate_grass", dec_1=["decoration_grass_front3", 950, 0], dec_2=["decoration_grass_back3", 3, 320]) with battleopening 
    $ renpy.block_rollback()
    
label bat000049_aftermath:
    scene black
    $ renpy.pause(1.0, hard=True)
    
    #Aftermath
    $ battle_count +=1
    $ battlestats_up()
    $_game_menu_screen = "save_screen"
    $ renpy.block_rollback()
    $ cp = max_cp
    $ cp += cp_levelset
    $ max_cp += max_cp_levelset
    
    #Unlocked Player Team Set
    if not skip_battle_selected:
        $ axle_fighter_set.append("panzer_zrinyi")
        $ load_data([
            "panzer_zrinyi"
            ], "fighter")
        $ yamato_levels +=1
    $ persistent.skip_battle_sensitive = False
    $ skip_battle_selected = False
    
    #After Battle Continue
    $ _rollback = True
    $ store.text_history_enabled = True
    $ config.keymap['skip'].append('K_LCTRL')
    $ config.keymap['skip'].append('K_RCTRL')
    $ config.keymap['hide_windows'].append('h')
    $ renpy.clear_keymap_cache()
    
    jump bat000049_continue
    
###########################################################################
    #bat000049	-	Battle End
###########################################################################
label bat000049_continue:
    
    play soundfx "se/airbattle.ogg" fadein 3.0
    play soundfx2 "se/plane.ogg" fadein 3.0
    scene sky1
    show planes
    show spitfire1
    show cloudsflip
    with pixellate
    play music "music/defeat.ogg"
    
    #Mission Marked Done
    $ log.markdone("bat000049")
    
    "The Germanian forces overwhelm the defenders. In the clouds over Singidun, the air battles come to a close . . ."
    "The {i}VVKS{/i} battles admirably to try and wrestle control of the skies from the encroaching enemy planes."
    "But, despite their best efforts, it's not possible. Their numbers are too few and their combat experience not enough."
    
    play sound4 "se/radio.ogg"
    
    simovic determined "Y-You . . . you did your best, everyone . . . regroup and continue to defend against the invaders . . ."
    "They're just unable to match the overwhelming superiority of the {i}Douché Aeronautica{/i} or the {i}Ruftwaffe{/i}."
    "Many are simply destroyed on the runways and airstrips across the country, with only four lost in aerial combat overall."
    simovic "Aircraft factories can't keep up with production, and within days, the {i}VVKS{/i} will essentially cease to exist . . ."
    "Serpana has been invaded, and there's little the defenders can do to hold back the {i}Axle{/i} forces . . ."
    
    stop sound4 fadeout 1.0
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000214

#####################################################################################################################################################
#sc0000214	-	Tito escapes as Germanians attack
#####################################################################################################################################################
label sc0000214:
    play soundfx "se/battle4.ogg" fadein 3.0
    play soundfx2 "se/tank_invasion.ogg" fadein 3.0
    scene woodland_cave
    with fade
    play music "music/evil.ogg"
    
    "Meanwhile, to the south of the country, xommunist partisans retreat into the hills as the {i}Vehrmaxt{/i} closes in."
    
    play sound5 "se/run2.ogg"
    show tito shock
    with easeinright
    play silsound4 "se/poke.ogg"
    
    tito "Ahh . . . ahhh! What do we do?! We're all going to die! Retreat! Run away!"
    "Tito leads her forces south, trying to outpace the {i}Panzys{/i} and the divebombers that overrun the cities." 
    
    show tito determined
    with dissolve
    
    tito "G-Get a hold of yourself Tito! Your people need you!"
    "As civilians are forced from their homes, there's mass disorder and panic, and the army is nowhere to be found."
    tito "The government has fallen . . . I have longed for this day for so many years. Yet . . ."
    "Before her precious xommunist ideology can sweep the nation, the vascists must first be repelled."
    "Until she can regroup with her rebel fighters, they can do little but hide out in the countryside."
    "Not to mention, the Sovian pact with Germania means that, politically, they cannot fight back against the {i}Axle{/i}." 
    tito "We'll continue the march. The people will unite in a battle against the occupation, one day . . ."
    "As the Germanians launch a successful invasion of Serpana, many factions are thrown into disarray."
    "How will Tito and her xommunists fare in this new and chaotic world?"
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000217

#####################################################################################################################################################
#sc0000217	-	Rommel arrives in Cyracana / Gariboldi jokes
#####################################################################################################################################################
label sc0000217:
    play soundfx "se/wind.ogg" fadein 3.0
    play soundfx2 "se/airbase.ogg" fadein 3.0
    scene desert_smoke
    with fade
    play music "music/desert.ogg"
    
    #STRUCTURE CHANGES
    #NORD AFRIKAA
    $ active_armies_items.update({
        "insignia-armeepanzergruppe004": armeepanzergruppe004_name,
        "insignia-armeepanzergruppeafrikaa": armeepanzergruppeafrikaa_name
    })
    
    $ active_spezialformations_items.update({
        "insignia-afrikaakorps": afrikaakorps_name
    })
    
    "In the far-western reaches of the wastelands of Cyracana, a last division holds the line against the Britannian army."
    
    play sound5 "se/walk.ogg"
    show gariboldi determined
    with dissolve
    
    "Gariboldi, {i}Governor-General of Cyracana{/i} and commander of Vitalia's desert forces, waits patiently at base camp."
    gariboldi "Come on . . . where are they? My bladder can't hold out for this long . . ."
    "Following Graziani's resignation and return to Rhome, he's had to pick up the slack and try to consolidate their losses."
    
    show object_vitalianretreat at tankpos
    with dissolve
    
    gariboldi "The last of the Vitalian {i}X Army{/i} has been saved by the recent malfunctioning of many Britannian vehicles . . ."
    gariboldi "Worn out from an extremely successful and lengthy counterattack, the enemy are slowing their assault . . ."
    "In addition to this, the campaign in Grecia has drawn Churchill's attention and pulled out the best-equipped units."
    gariboldi "Finally, poor weather and a sustained bombing campaign by the {i}Ruftwaffe{/i} at Benghatza has stalled the {i}Alliance{/i}."
    "This small window of opportunity has allowed Gariboldi the chance to regroup."
    
    hide object_vitalianretreat
    with dissolve
    
    gariboldi "Graziani, this is all your fault . . . ah well, at least the Germanians will fight hard."
    "With the request for Germania's assistance accepted by Hitora's administration, a special army has been shipped to Cyracana."
    "This mysterious new corps will help form the basis of an {i}Axle{/i} resistance against the Britannian invaders."
    "Gariboldi scans the horizon, shielding his eyes from the sun with his palm, watching for the delegation as it arrives."
    
    play soundfx4 "se/scamper.ogg"
    stop music fadeout 3.0
    show gariboldi shock
    
    "Suddenly, dust clouds begin to rise as a silhouette appears in the desert sands ahead."
    "There's the sound of scampering paws and panting, as a four-legged beast comes bounding into view."
    
    stop soundfx4 fadeout 1.0
    play sound3 "se/skid.ogg"
    queue sound3 "se/watershake.ogg"
    
    "Skidding to a halt, the animal shakes herself before standing upright and strolling calmly towards Gariboldi."
    
    play sound5 "se/walk.ogg"
    show gariboldi at left3 
    with ease
    show rommel determined at right3
    with dissolve
    play music "music/rinni.ogg"
    
    rom "He he he! Nothing like a good run to stretch the legs."
    "It's that infamous Germanian foxgirl, the one, the only . . ."
    
    show gariboldi happy
    with dissolve
    
    gariboldi "{i}Generalmajor Erwina Rommel{/i} . . . it is an honor, {i}signora{/i}."
    
    play silsound5 "se/silly4.ogg"
    show rommel moe1
    show gariboldi shock
    
    rom "Hey, it's {i}Generalleutnant{/i} Erwina Rommel now."
    
    show gariboldi normal
    show rommel normal
    with dissolve
    
    "The foxgirl looks around the camp at the state of the Vitalian {i}X Army{/i}, wincing a little."
    rom "Is this everyone?"
    gariboldi "{i}Si, signora{/i}."
    
    show rommel sad
    show gariboldi shock
    
    rom "I guess I've got my work cut out for me."
    
    show gariboldi determined
    
    gariboldi "Such impertinence! Oh, and what small detachment did you bring, hmm?"
    
    show rommel determined
    with dissolve
    
    rom "Well, since you asked . . ."
    
    play soundfx3 "se/rumble.ogg" fadein 2.0
    
    "Turning and glancing yonder, over the baking-hot sands, the foxgirl wags her tail happily and the ground begins to rumble."
    
    play silsound4 "se/silly15.ogg"
    play soundfx4 "se/tank_invasion.ogg" fadein 3.0
    stop soundfx3 fadeout 2.0
    show gariboldi shock
    
    "Gariboldi looks across the deserts, grabbing hold of his cap, as a mirage begins to form in the middle distance."
    
    show object_afrikaakorps at tankpos
    with dissolve
    
    "From over the horizon, a mile-long column of armored vehicles rolls into view, kicking up dust and smoke across the dunes."
    "Standing back, Rommel holds out her arms in a sweeping motion, grinning cheekily as the brigades roll by."
    
    play silsound4 "se/silly17.ogg"
    
    rom "This is the {i}Dessous Afrikaa Korps{/i}. Consider it a little present from the Füühbar . . ."
    "{i}Panzy{/i} tanks, along with {i}Schwerer Panzyspähwagen{/i} and other light vehicles, form the basis for this army."  
    "Painted in their special desert camouflage, the war machines make the resting {i}X Army{/i} gape in astonishment."
    "Bigger, faster and altogether deadlier than their Vitalian counterparts, it's certainly a force to be reckoned with."
    "Intended as a blocking force, this special group will help {i}Il Douché{/i} to win in the fight against Wavell."
    
    hide object_afrikaakorps
    with dissolve
    
    gariboldi "Incredible . . . this is the power of Germanian industrial might."
    rom "He he he! Well, you Vitalians have women and food. We Germanians have guns and steel."
    
    play silsound6 "se/silly1.ogg"
    show gariboldi determined
    show rommel moe2
    
    gariboldi "Maybe Graziani was right to call you . . ."
    "Gariboldi begins to revise his opinion of their helpful ally."
    
    show gariboldi normal
    show rommel normal
    with dissolve
    
    rom "Anyway, your boss Roatta told me I'm to take command of your motorized units in the meantime."
    "That's Maria Roatta, {i}Chief of Staff{/i} of the {i}Regio Lasagnotte{/i}, another position that Graziani recently resigned."
    rom "As soon as we're set up, we'll prepare to move out for an attack."
    gariboldi "What if we don't have any orders to attack?"
    
    play silsound4 "se/silly20.ogg"
    show rommel annoyed
    show gariboldi shock
    
    rom "Simple. In the absence of orders, go find something and kill it."
    "It feels like she's saying that as a wild fox rather than as a soldier."
    gariboldi "B-But, our men need to regroup still! A defensive war at this stage would be better . . ."
    rom "That's {i}'old man'{/i} talk. We need to go on the offensive. Anyway, I would rather be the hammer than the anvil."
    "Rommel doesn't hold back, trying to establish herself as the alpha of the pack."
    
    show rommel determined
    show gariboldi normal
    with dissolve
    
    rom "I've sat on the sidelines ever since we took Franzo. Now it's Rommel's time to shine again!"
    "Taking a deep breath from the arid air, the girl smirks, exposing her sharp fangs, and casting her arm forward."
    
    play silsound6 "se/silly12.ogg"
    show gariboldi shock
    
    rom "It's time to begin {i}Operation Sunnyside Eggs{/i} . . . we're going to take back this country, for the Füühbar and Germania!"
    "We might just see a real fight in these deserts. And now Erwina Rommel is here to show them what's what."
    
    show rommel normal
    
    gariboldi "Hey . . . it's {i}Il Douché's{/i} empire, not Hitora's . . ."
    
    play silsound3 "se/silly16.ogg"
    show rommel moe1
    
    rom "Potato, {i}potato{/i}. They're all dictators in the end."
    "Now with Germanian troops arriving, the reconquest of the {i}Douché's{/i} Cyracana will be a cinch."
    "Well, so long as the Vitalian forces still have the morale to go on, with the Germanians leading them . . ."
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    stop soundfx4 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000223
    
#####################################################################################################################################################
#sc0000223	-	Antoness/Horthy discuss progress in Serpana / Notice bombers
#####################################################################################################################################################
label sc0000223:
    play soundfx3 "se/battle3.ogg" fadein 3.0
    play soundfx4 "se/tank_invasion.ogg" fadein 3.0
    scene woodland_day
    with fade
    play music "music/evil.ogg"
    
    "In the deep woodland of the Serpana countryside, the {i}Vehrmaxt{/i} forces sweep through the treeline."
    
    show object_serpanainvasion at tankpos
    with dissolve
    
    "With the successful invasion and routing of the enemy army, the {i}Axle{/i} are doing what they do best."
    "Victory after victory seems to come to the Germanian army as the ground campaign gets under way."
    
    hide object_serpanainvasion
    with dissolve
    show horthy happy at left3
    show antoness happy at right3
    with dissolve
    
    hor "Wow, this is really something . . . you've outdone yourself this time, Commander Ewalda."
    ewalda "I d-don't know about that. After all, you guys are helping this time around, so it's been a lot smoother."
    hor "Well, that's what allies are for, after all, making things easy for one another."
    "Try telling that to the Vitalians . . ."
    
    show antoness normal
    show horthy normal
    with dissolve
    
    ewalda "By the way, I'm sorry to hear about your minister, Teleki . . ."
    "Horthy's primary minister and close confidant, Teleki, took his own life after hearing of the invasion of Serpana."
    hor "Thank you for the condolences. But it's fine, I've got a shiny new minister now."
    
    show horthy happy
    with dissolve
    
    hor "His name is Dossy, and he loves war and annexing territory almost as much as anyone."
    ewalda "I . . . see."
    "That was a little cold."
    
    show horthy normal
    with dissolve
    
    ewalda "Still, you guys are right. About the fighting. We've honed our tactics from previous campaigns after all."
    
    show object_serpana at tankpos
    with dissolve
    
    "From Germanian bases within Hang, Rumanum and Bolga, the {i}Vehrmaxt{/i} have launched numerous incursions."
    ewalda "Our {i}Panzy{/i} corps fight with devastating speed and efficiency, reminiscent of our battles in Franzo."
    ewalda "Superior {i}Axle{/i} tanks blast their way through the defenses, crushing any opposition from the enemy."
    "The Serpana air force have been destroyed on the ground by a mix of Vitalian and Germanian bombers."
    
    hide object_serpana
    with dissolve
    
    ewalda "It won't be much longer before the country has fallen to this onslaught . . ."
    
    show antoness happy
    show horthy moe
    with dissolve
    
    anton "Well, naturally. We're going to completely crush these losers for going back on our pact."
    hor "We'll show them that we mean business! We're the {i}Axle{/i} after all!"
    "These two are real cheerleaders for the cause. Do they really know what it means going to war like this?"
    hor "I'm going to go find a bayonet or something as a souvenir!"
    
    play sound5 "se/walk.ogg"
    play sound2 "se/brush.ogg"
    hide horthy
    with dissolve
    
    "Horthy skips away to root around in the undergrowth."
    
    show antoness at center
    with ease
    
    ewalda "Geez, it's like she thinks she's on a field trip . . ."
    anton "It's not often we get the chance to do something amazing and exciting like this. Thank you for getting us involved!"
    
    play silsound3 "se/silly12.ogg"
    show antoness shock
    
    ewalda ". . . but you aren't involved, are you? What are Rumanum even contributing to this invasion?"
    anton "O-Our artillery provided support during the opening stages! Even if our forces didn't cross the border . . ."
    "Their involvement has been pretty minimal. Antoness is just desperate to impress the Germanians."
    
    show antoness normal
    with dissolve
    
    ewalda "Still, you think this is exciting?"
    
    show antoness insane
    with dissolve
    play silsound6 "se/silly17.ogg"
    
    anton "Of course. The bloodshed, the crushing of your enemies . . . it's a beautiful sight . . ."
    anton "And it's thanks to the Germanian military mission in Rumanum that we're even here . . . I really mean it."
    "Antoness is a big fan and supporter of the {i}Axle{/i} cause, desperate to make friends with her new allies."
    anton "Maybe at this rate, we'll be able to reclaim our lost territories . . ."
    
    show antoness normal
    with dissolve
    play soundfx "se/bombers.ogg" fadein 3.0
    
    "After a few moments, the two dogs begin to notice a familiar, humming sound from far above."
    ewalda "Hmm . . . what is that noise?"
    
    show antoness shock
    with dissolve
    
    "Craning their necks upwards, Antoness and Ewalda let their jaws drop, as they gape at the spectacle."
    "{i}Ruftwaffe{/i} bombers, high in the sky, flock in such great numbers that they almost blot out the sun."
    ewalda "H-Huh? Are those ours? How many bombers are there up there?"
    anton "I . . . I don't know . . . the payload must be enormous . . ."
    "As Germanian troops filter through the trees, clearing out resisters, the air force seems to be on a mission."
    ewalda "Just where are all those planes going? What is Goring up to now . . ."
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    stop soundfx3 fadeout 3.0
    stop soundfx4 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000224
    
#####################################################################################################################################################
#sc0000224	-	Bombing of Singidun
#####################################################################################################################################################
label sc0000224:
    play soundfx "se/bombers.ogg" fadein 3.0
    play soundfx5 "se/plane.ogg" fadein 3.0
    scene sky1
    show clouds
    with fade
    play music "music/horror.ogg"
    
    "In the skies over the ancient capital of Singidun, {i}Ruftwaffe{/i} bombers gather in formation."
    
    show object_ruftwaffe at tankpos
    with dissolve
    
    "Accompanied by fighters, they're untouched by the weak and ineffectual Serpana air force."
    "Any interference is easily fended off, as the Germanians commit themselves to their mission."
    
    play sound4 "se/radio.ogg"
    
    gor determined "Today, pilots, we will take our revenge. These ungrateful people in Singidun turned their backs on us!"
    "Crackling over the aircraft radios, their chubby boss's voice rings loud and clear."
    
    play silsound6 "se/silly12.ogg"
    
    gor "We won't forgive them for their impudence. We will destroy this city and all who live in it. Bombs away!"
    
    hide object_ruftwaffe
    with dissolve
    
    "With their plan of action in place, the unmatched bombers set their sights on the ground far below."
    
    play soundfx2 "se/cheer.ogg" fadein 3.0
    play soundfx6 "se/airsiren.ogg" fadein 3.0
    scene city2
    with dissolve
    stop soundfx5 fadeout 3.0
    
    "In the streets of Singidun, the frightened citizens scramble for cover."
    "Panic runs rife and civilians trample over one another, desperately seeking safety."
    "Only days ago, these same people marched proudly as a mob, supporting the coup and the government."
    "Now, choked by fear, they can only flee in terror as a powerful enemy descends upon them."
    "It seems for a minute as though the air fleet above may simply pass over . . ."
    
    scene white
    with dissolve
    
    "And then . . . in a moment, the bomb bay doors open and hellfire rains down from above."
    
    stop soundfx6 fadeout 3.0
    play sound6 "se/boom3.ogg"
    play sound2 "se/break2.ogg"
    play soundfx3 "se/bomb.ogg"
    scene city2
    show smoke
    show fire
    show spark
    show bomb
    with hpunch
    with hpunch
    play soundfx5 "se/fire2.ogg" fadein 3.0
    
    "Buildings explode into rubble as giant shells crash amongst the rooftops of the capital city . . ."
    "Incendiary bombs set the lanes and alleys aflame, melting the sidewalks and scarring the landscape."
    "The city streets explode in a maelstrom of debris, smoke and fire . . ."
    "People are caught out, blown apart, and torn limb from limb by the blasts."
    "It is a smokey, bloody and destructive scene."
    "This is a vengeful strike . . . pure revenge for abandoning the {i}Triple Pact{/i}. Perhaps simply a taste of things to come . . ."
    
    stop sound2 fadeout 2.0
    stop sound6 fadeout 2.0
    stop soundfx2 fadeout 3.0
    stop soundfx4 fadeout 3.0
    stop soundfx5 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000225
    
#####################################################################################################################################################
#sc0000225	-	Simovic worried/On the run
#####################################################################################################################################################
label sc0000225:
    play soundfx5 "se/cave.ogg" fadein 3.0
    scene tunnel
    with fade
    
    "Meanwhile, below the city streets, individuals gather in dark and cramped tunnels."
    "Embers flicker from torches hung throughout the dank tunnels, as soldiers and firemen desperately try to keep order."
    
    show simovic shock
    with dissolve
    
    "Far beneath her new government residences, Simovic listens in, wide-eyed in horror."
    simovic "No . . . Hitora . . . she's getting her revenge . . . she'll destroy us all . . ."
    
    show object_singidunbombed at tankpos
    with dissolve
    
    "High in the skies above, Germanian bombers are relentlessly pounding her beloved city."
    simovic "Those evil Germanians actually did it. They invaded, and on my daughter's wedding day too . . ."
    "Within minutes the military barracks, train stations, industrial centers, libraries and civil sectors have all been attacked."
    "Somehow the Germanians are hitting their targets precisely, knocking out key areas in moments."
    simovic "We must have been betrayed. There's no way their intelligence could be this good . . ."
    "The {i}Ruftwaffe's{/i} efforts have completely crippled the Serpana government and any hope of an immediate defense."
    
    hide object_singidunbombed
    show simovic determined
    with dissolve
    
    simovic "We have to try to reform our command and control. We can't be beaten like this . . ."
    "There's a wavering in her voice as she says that."
    simovic "But . . . King Petey is already gone. He fled to Albion in the night. And the others too."
    simovic "Perhaps, I should get my family and go . . . leave the fighting to others."
    "Though Simovic is responsible for the coup, she has no stomach for war."
    "Many of her government ministers are gone too. They know they can't defeat the Germanians."
    sol determined "Simovic, ma'am, please . . . you must get yourself to a more secure shelter. It's not safe here."
    simovic "Forced to hide beneath the city streets, like a rat in a sewer . . . very well."
    
    play sound4 "se/walk.ogg"
    hide simovic
    with dissolve
    
    "Taking the soldier's advice, the leader of Serpana scurries away, hurrying to find an intact bunker."
    "Singidun continues to be pounded mercilessly from the air by the heavy Germanian bombers throughout the day."
    "Even aerial mines are set loose as the {i}Ruftwaffe{/i} test new means of killing from above."
    "The fires rage, as Hitora's pilots wage a war of merciless total destruction against civilians as well as military targets . . ."
    
    stop soundfx fadeout 3.0
    stop soundfx3 fadeout 3.0
    stop soundfx5 fadeout 3.0
    stop music fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000226
    
#####################################################################################################################################################
#sc0000226	-	Messe still waiting for reinforcements
#####################################################################################################################################################
label sc0000226:
    scene black
    with fade
    
    $ mouse_visible = False
    show expression Text(_("Meanwhile, on the border between Epirus and Grecia . . ."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx "se/tank_invasion.ogg"
    play soundfx2 "se/battle4.ogg"
    play sound3 "se/boom.ogg"
    scene desert_bunker
    with hpunch
    with vpunch
    play music "music/glory.ogg"
    
    "War continues to ravage the nation of Grecia, as the Vitalians are pushed back further and further towards Epirus."
    
    show object_klisurapass at tankpos
    with dissolve
    
    "Craters are made in the surrounding hillsides, as bunkers are blown out by shells and anti-aircraft guns."
    "Tanks and trucks tumble over mountain roads, pelted by flying boulders and landslides, disturbed by nearby fighting."
    "It's a dog-eat-dog conflict, with opposing forces battling to hold outposts across the peaks of the region."
    
    hide object_klisurapass
    with dissolve
    show messe moe
    with dissolve
    play silsound5 "se/silly1.ogg"
    
    messe "{i}Il Douché{/i}, where are you?! I need help, now!"
    "Wait a minute . . . Messe is still waiting on reinforcements? I thought we wrapped up this story arc."
    messe "We need more soldiers. The last bunch didn't help at all. Please . . . someone . . . come and save us!"
    "The Vitalians won't be able to hold out much longer. Not the way things are going."
    messe "Fine! Germania! Adorofia Hitora! Ewalda . . . or whoever, please hurry south to Grecia and help salvage this campaign."
    "If something doesn't happen soon, the Grecians are going to completely destroy the Vitalian lines . . ."
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000227

#####################################################################################################################################################
#sc0000227	-	Briefing on Serpana and victory
#####################################################################################################################################################
label sc0000227:
    play soundfx "se/battle3.ogg" fadein 3.0
    play soundfx2 "se/tank_invasion.ogg" fadein 3.0
    scene woodland_day
    with fade
    play music "music/evil.ogg"
    
    "In the center of the Serpana countryside, the Germanian tanks converge for one final push."
    
    show germaniangeneraloberst normal
    with dissolve
    
    "Ewalda, the Pomeranian commander who saw great success in Polix, joins Listte to discuss their next moves."
    ewalda "It's been a very speedy campaign. I haven't even had to stop and refuel my tanks yet."
    listte ". . . . . . . . ."
    
    play silsound5 "se/silly27.ogg"
    
    ewalda "What is it? Have I got something caught in my fur?"
    listte "No, it's just, this is a first for me . . . well, taking Rommel and Antoness into account, I guess it's a third."
    ewalda "Huh? You might have to speak up, I'm a bit deaf! It's a common condition for girls of my stature."
    "For a fierce commander, she certainly is quite adorable."
    listte "Never mind."
    ewalda "Ah. Anyway that's enough chit-chat. So, what's the plan?"
    "The little fluff ball directs them onto more important matters."
    
    show germaniangeneraloberst determined
    with dissolve
    
    listte "With King Petey and Simovic nowhere to be found, our armies can only push onwards until our foe relents . . ."
    listte "We can't do this forever. So we're going to force the enemy's hand and smoke them out of their hiding places."
    ewalda "How do you plan to do that?"
    
    play sound6 "se/map.ogg"
    
    "In the usual fashion, Listte pulls out a large map and points to their location."
    listte "We're here. And the {i}Serpana Supreme Command{/i} are holed up near to the middling city of Vrhbosna."
    listte "This city . . . this is where we're going to come out in full force with our {i}Panzys{/i} and take the place."
    ewalda "I see. Scare the enemy into surrendering, eh?"
    "If they can capture the town, there's a good chance that the enemy representatives will sue for peace."
    "Then the Germanians may be able to push south to Grecia and help Mussorinni with her campaigns there."
    
    show germaniangeneraloberst normal
    with dissolve
    
    listte "The way things are going, this next battle may even be one of the last ones we fight here."
    ewalda "Well, what are we waiting for? Let's smash our way through and end this dumb war."
    listte ". . . well said."
    "The Germanian tanks converge around the city of Vrhbosna, ready to encircle the enemy commanders based nearby."
    "Though it has been a brief campaign, the battle for Serpana already seems to be reaching its conclusion . . ."
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    #Map Data
    $ mapdata = ScreenData("geomap2", "map12", "easternmap")
    
    #Mission Data
    $ active_invasionbeacons_items.pop("bat000049", [bat000049_description, bat000049_title, bat000049_type, bat000049_x, bat000049_y])
    $ active_invasionbeacons_items.update({"bat000056": [bat000056_description, bat000056_title, bat000056_type, bat000056_x, bat000056_y]})
    $ active_invasionbeacons_items.update({"bat000053": [bat000053_description, bat000053_title, bat000053_type, bat000053_x, bat000053_y]})
    
    #Mission Assign
    $ log.assign("[bat000056_title]")
    $ log.assign("[bat000053_title]")
    
    #Allegiances Data
    $ singidun_siege = True
    $ active_maptown_items.update({"singidun": [singidun_name, singidun_size, singidun_governor, singidun_governor_pic, singidun_hostility, singidun_alignment, singidun_population, singidun_publicorder, singidun_influence, singidun_command, singidun_management, singidun_farming_worth, singidun_mining_worth, singidun_industry_worth, singidun_trade_worth, singidun_entertainment_worth, singidun_military_worth, singidun_corruption_worth, singidun_unlocktown, singidun_martial, singidun_siege, singidun_company_img, singidun_company_text, .62, .5]})
    
    #Go To Map
    jump map_begin

#####################################################################################################################################################
#bat000056	-	Operation Sunnyside Eggs: Battle of Cyracana
#####################################################################################################################################################
label bat000056:
    hide screen mapchoice1
    $ renpy.block_rollback()
    $ _rollback = True
    $ store.text_history_enabled = True
    window hide
    play sound6 "se/march2.ogg"
    stop music fadeout 2.0
    scene black
    with dissolve
    
    $ mouse_visible = False
    show expression Text(_("[bat000056_title]"), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    show expression Text(_("Somewhere in the desert, Cyracana"), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx "se/tank_battle.ogg" fadein 3.0
    play soundfx2 "se/wind.ogg" fadein 3.0
    scene desert_tanks
    with fade
    play music "music/glory.ogg"
    
    "Far away, in the southern deserts, Rommel's {i}Afrikaa Korps{/i} battles for control in Cyracana."
    
    show rommel determined
    with dissolve
    
    rom "Forward! Don't give them inch! Remember, sweat saves blood, blood saves lives, but brains saves both!"
    "With a smirk, the newly-named {i}Desert Fox{/i} takes control, sewing panic and disorder amongst all the confusion."
    
    show object_sunflower at tankpos
    with dissolve
    
    "The Britannians, now on the retreat in this area, can only stumble backwards as the Germanians press hard on their flanks."
    "There's nothing holding them back, as they charge forward, breaking the spirit of the enemy armies."
    rom "A risk is a chance you take; if it fails you can recover. A gamble is a chance taken; if it fails, recovery is impossible."
    "One by one, towns and fortresses fall to the {i}Afrikaa Korps{/i} and the balance of power in the region shifts once more."
    "In less than a fortnight, the entire military situation has been turned on its head, with the Britannians on the run."
    
    hide object_sunflower
    with dissolve
    show speedlines behind rommel
    with circleirisout
    
    rom "Forward I say! Let's push the Britannians all the way back to the pyramids!"
    
    stop soundfx fadeout 1.0
    stop soundfx2 fadeout 1.0
    stop music fadeout 1.0
    scene black
    with pixellate
    
    jump bat000056_begin
    
label bat000056_begin:
###########################################################################
    #bat000056	-	Battle
###########################################################################
    
    #History Block
    $ renpy.block_rollback()
    $ store.text_history_enabled = False
    $ _rollback = False
    $ config.skipping = False
    
    #Enemy Team Set
    $ enemy_team = BaseTeam("Enemy", Solid("#000000", xysize=(50,50)), limit=50)
    $ enemy_team.add_fighter("enemy_panzer_covenanter")
    $ enemy_team.add_fighter("enemy_britannia_gunner_heer6")
    $ enemy_team.add_fighter("enemy_panzer_matilda2")
    
    #Playing For New Side Set - Axle
    $ empty_data("fighter")
    $ load_data(afrikaakorps_fighter_set, "fighter")
    
    # Selection Screen Set
    $ airsupport_section_unlocked = False
    $ infantry_section_unlocked = False
    $ panzer_section_unlocked = True
    $ antitank_section_unlocked = True
    $ commander_section_unlocked = True
    $ specialgroup_section_unlocked = True
    $ player_team = BaseTeam("Player", Solid("#000000", xysize=(50,50)), limit=50)
    play battlemusic "music/map3.ogg"
    call screen non_battle_party_screen

    # Battle Set
    $ config.skipping = False
    $ yamato_lvlcheck()
    stop battlemusic fadeout 1.0
    scene black
    $ renpy.pause(1.0, hard=True)
    play battlesfx "se/battle4.ogg" volume 0.25
    play battlemusic "music/battle_desert.ogg"
    $ renpy.block_rollback()
    $ fight_end = "bat000056_aftermath"
    $ game = Battleground("Battle Stage   |   Operation Sunnyside Eggs", player_team.store[0], enemy_team.store[0], "mosque")
    $ battle_terrain = "desert"
    $ battleground_bg = "background_desert"
    $_game_menu_screen = None
    $ config.skipping = False
    $ config.keymap['skip'].remove('K_LCTRL')
    $ config.keymap['skip'].remove('K_RCTRL')
    $ config.keymap['hide_windows'].remove('h')
    $ renpy.clear_keymap_cache()
    call screen battle_screen(bg=battleground_bg, disc="plate_desert", dec_1=["decoration_none_front1", 950, 0], dec_2=["decoration_desert_back3", 3, 320]) with battleopening 
    $ renpy.block_rollback()
    
label bat000056_aftermath:
    scene black
    $ renpy.pause(1.0, hard=True)
    
    #Aftermath
    $ battle_count +=1
    $ battlestats_up()
    $_game_menu_screen = "save_screen"
    $ renpy.block_rollback()
    $ airsupport_section_unlocked = False
    $ infantry_section_unlocked = True
    $ panzer_section_unlocked = True
    $ antitank_section_unlocked = True
    $ commander_section_unlocked = True
    $ specialgroup_section_unlocked = True
    $ cp = max_cp
    $ cp += cp_levelset
    $ max_cp += max_cp_levelset
    
    #Unlocked Player Team Set
    if not skip_battle_selected:
        $ axle_fighter_set += ("antitank_hornisse", "specialgroup_afrikaakorps_marksman_heer5")
        $ afrikaakorps_fighter_set += ("antitank_hornisse", "specialgroup_afrikaakorps_marksman_heer5")
        $ load_data([
            "antitank_hornisse",
            "specialgroup_afrikaakorps_marksman_heer5"
            ], "fighter")
        $ yamato_levels +=1
    $ persistent.skip_battle_sensitive = False
    $ skip_battle_selected = False
    
    #After Battle Continue
    $ _rollback = True
    $ store.text_history_enabled = True
    $ config.keymap['skip'].append('K_LCTRL')
    $ config.keymap['skip'].append('K_RCTRL')
    $ config.keymap['hide_windows'].append('h')
    $ renpy.clear_keymap_cache()
    
    jump bat000056_continue
    
###########################################################################
    #bat000056	-	Battle End
###########################################################################
label bat000056_continue:
    
    play soundfx "se/tank_battle.ogg" fadein 3.0
    play soundfx2 "se/wind.ogg" fadein 3.0
    scene desert_tanks
    with pixellate
    play music "music/glory.ogg"
    
    #Mission Marked Done
    $ log.markdone("bat000056")
    $ active_invasionbeacons_items.pop("bat000056", [bat000056_description, bat000056_title, bat000056_type, bat000056_x, bat000056_y])
    
    "The battle rages fiercely around the opposing forces, as tank shells fly and dust is kicked up from smoldering craters."
    "The Vitalians and Germanians advance up the coastal roads at a breakneck pace, reclaiming much of Cyracana."
    
    show rommel determined
    with dissolve
    
    rom "See, Gariboldi? Easy as anything . . . you just had to want it enough . . ."
    "The furry girl smirks as she watches the disorganized columns of the enemy disappearing into the desert sands."
    "Many Britannian armored vehicles have been left abandoned, broken-down and useless in the fight."
    rom "We've even bagged some celebrity prisoners, like that useless O'Connor girl . . ."
    "It has been an amazing success so far. And Rommel plans to press the advantage before letting her superiors know."
    rom "Keep pressing, advance forward and let's chase these tea slurping chickens back into Gypta!"
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump map_return
    
#####################################################################################################################################################
#bat000053	-	Operation Meat Pie: Battle of Vrhbosna
#####################################################################################################################################################
label bat000053:
    hide screen mapchoice1
    $ renpy.block_rollback()
    $ _rollback = True
    $ store.text_history_enabled = True
    window hide
    play sound6 "se/march2.ogg"
    stop music fadeout 2.0
    scene black
    with dissolve
    
    $ mouse_visible = False
    show expression Text(_("[bat000053_title]"), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    show expression Text(_("Five miles north of Vrhbosna, Serpana"), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3        
    $ mouse_visible = True
    
    play soundfx "se/battle4.ogg" fadein 3.0
    play soundfx2 "se/tank_invasion.ogg" fadein 3.0
    scene city1
    with fade
    play music "music/fury.ogg"
    
    "As the invasion continues, Serpana is criss-crossed by {i}Axle{/i} armored columns, as city after city falls to the invaders."
    
    show object_vrhbosna at tankpos
    with dissolve
    
    "With the {i}Serpana Supreme Command{/i} based in the south-central city of Vrhbosna, tanks quickly descend on it."
    "The main bulk of the defending army is situated south of the capital city, Singidun. But their orders come from right here."
    ewalda "Come on! Let's smoke out whoever is still in control of this country, and end this war!"
    "Battling in cities like this is never an easy affair . . ."
    "The surroundings encourage formations to split down into several smaller units, which are more difficult to control."
    "As well as this, noise is easy to hear but extremely difficult to locate. It makes communication and control very difficult."
    
    hide object_vrhbosna
    with dissolve
    
    ewalda "Not a problem for us. The enemy are already so low in morale, I doubt they'll cause us any trouble . . ."
    "Entering the city of Vrhbosna, the Germanian tanks fire on the buildings, aiming to destroy the last of the resistance . . ."
    
    stop soundfx fadeout 1.0
    stop soundfx2 fadeout 1.0
    stop music fadeout 1.0
    scene black
    with pixellate
    
    jump bat000053_begin
    
label bat000053_begin:
###########################################################################
    #bat000053	-	Battle
###########################################################################
    
    #History Block
    $ renpy.block_rollback()
    $ store.text_history_enabled = False
    $ _rollback = False
    $ config.skipping = False
    
    #Enemy Team Set
    $ enemy_team = BaseTeam("Enemy", Solid("#000000", xysize=(50,50)), limit=50)
    $ enemy_team.add_fighter("enemy_partisan_gunner_heer4")
    $ enemy_team.add_fighter("enemy_panzer_renaultr35serpana")
    $ enemy_team.add_fighter("enemy_partisan_marksman_heer4")
    $ enemy_team.add_fighter("enemy_serpana_gunner_heer5")
    $ enemy_team.add_fighter("enemy_partisan_gunner_heer4")
    
    #Playing For New Side Set - Axle
    $ empty_data("fighter")
    $ load_data(axle_fighter_set, "fighter")
    
    # Selection Screen Set
    $ player_team = BaseTeam("Player", Solid("#000000", xysize=(50,50)), limit=50)
    play battlemusic "music/map3.ogg"
    call screen non_battle_party_screen

    # Battle Set
    $ config.skipping = False
    $ yamato_lvlcheck()
    stop battlemusic fadeout 1.0
    scene black
    $ renpy.pause(1.0, hard=True)
    play battlesfx "se/battle4.ogg" volume 0.25
    play battlemusic "music/battle_land.ogg"
    $ renpy.block_rollback()
    $ fight_end = "bat000053_aftermath"
    $ game = Battleground("Battle Stage   |   Operation Meat Pie", player_team.store[0], enemy_team.store[0], "guardtower")
    $ battle_terrain = "urban"
    $ battleground_bg = "background_urban"
    $_game_menu_screen = None
    $ config.skipping = False
    $ config.keymap['skip'].remove('K_LCTRL')
    $ config.keymap['skip'].remove('K_RCTRL')
    $ config.keymap['hide_windows'].remove('h')
    $ renpy.clear_keymap_cache()
    call screen battle_screen(bg=battleground_bg, disc="plate_metal", dec_1=["decoration_urban_front3", 950, 0], dec_2=["decoration_urban_back3", 3, 320]) with battleopening 
    $ renpy.block_rollback()
    
label bat000053_aftermath:
    scene black
    $ renpy.pause(1.0, hard=True)
    
    #Aftermath
    $ battle_count +=1
    $ battlestats_up()
    $_game_menu_screen = "save_screen"
    $ renpy.block_rollback()
    $ cp = max_cp
    $ cp += cp_levelset
    $ max_cp += max_cp_levelset
    
    #Unlocked Player Team Set
    if not skip_battle_selected:
        $ axle_fighter_set += ("antitank_jagdtiger", "panzer_turan")
        $ load_data([
            "antitank_jagdtiger",
            "panzer_turan"
            ], "fighter")
        $ yamato_levels +=1
    $ persistent.skip_battle_sensitive = False
    $ skip_battle_selected = False
    
    #After Battle Continue
    $ _rollback = True
    $ store.text_history_enabled = True
    $ config.keymap['skip'].append('K_LCTRL')
    $ config.keymap['skip'].append('K_RCTRL')
    $ config.keymap['hide_windows'].append('h')
    $ renpy.clear_keymap_cache()
    
    jump bat000053_continue
    
###########################################################################
    #bat000053	-	Battle End
###########################################################################
label bat000053_continue:
    
    play soundfx "se/battle4.ogg" fadein 3.0
    play soundfx2 "se/tank_invasion.ogg" fadein 3.0
    scene city1
    with pixellate
    play music "music/fury.ogg"
    
    #Mission Marked Done
    $ log.markdone("bat000053")
    
    "Eventually, the city of Vrhbosna falls like all the others, with the {i}Serpana Supreme Command{/i} flushed out of hiding."
    ewalda "Simovic has abandoned you, so has King Petey . . . hurry up and surrender!"
    "Despite their best efforts, the defending forces have been overwhelmed in the past weeks of fighting by a superior force."
    "This is the end of the invasion. An armistice is sure to be signed and the country's fate will be in Adorofia Hitora's hands . . ."
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000228

#####################################################################################################################################################
#sc0000228	-	Tito escapes into the hills
#####################################################################################################################################################
label sc0000228:
    scene black
    with fade
    
    $ mouse_visible = False
    show expression Text(_("Meanwhile, in the dark forests of Serpana . . ."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx "se/march3.ogg" fadein 3.0
    play soundfx2 "se/outdoor_crowd.ogg" fadein 3.0
    play soundfx3 "se/battle2.ogg" fadein 3.0
    scene woodland_cave
    with fade
    play music "music/drama.ogg"
    
    "With the resistance in Serpana now broken up into smaller bands, and the royalist cause fading, the {i}Axle{/i} sweep in."
    "Towns are evacuated, possessions lie trampled in the dirt, livestock run wild and livelihoods are extinguished."
    "There's no coordination between the defending groups, making it easy for the well-trained {i}Vehrmaxt{/i} forces."
    
    play sound4 "se/walk.ogg"
    show tito determined
    with dissolve
    
    "In the hills, the xommunist partisans make their escape, regrouping and retreating."
    tito "Comrades, don't lose hope . . . today we may have failed, but tomorrow will always come."
    "Tito's soldiers do their best to keep their spirits high, but it has been a disheartening march from the capital."
    "Without Sovia's support, they have little choice but to avoid confrontation with the incoming {i}Axle{/i} occupation."
    tito "The resistance will continue to wait for many moons. It will be a difficult struggle . . ."
    
    play silsound3 "se/poke.ogg"
    show tito shock
    
    miha normal "That's just like you, whining again . . ."
    
    play sound4 "se/walk.ogg"
    show tito shock at left3
    with ease
    show mihaila normal at right3
    with dissolve
    
    "An old bearded man, Drago Mihaila, leader of the royalist {i}Cheatniks{/i}, arrives with his band of guerilla fighters."
    tito "Uncle Drago? What are you doing here?"
    miha "The same thing as you. Escaping from the vascists marching south."
    
    show tito determined
    show mihaila determined
    with dissolve
    
    tito "I'm surprised you're not throwing down your arms and joining them . . ."
    miha "How dare you! I'm a patriotic royalist, not a vascist."
    tito "Good. The peoples of Serpana do not want vascism. They do not want a totalitarian regime, they do not want to become slaves."
    
    play silsound5 "se/silly2.ogg"
    show tito shock
    
    miha "You say that, but I know you won't make a move without Starin's say-so. Your partisans may as well be collaborators . . ."
    miha "At least me and my {i}Cheatniks{/i} are still carrying on the fight, building a real resistance."
    "Mihaila puts her down with that quick quip."
    
    show tito determined
    show mihaila happy
    with dissolve
    
    miha "In any case, I was hoping you could let us pass. We'll call a truce. We're all fighting for Serpana after all . . ."
    tito "Well . . . I suppose. There's not much reason for us to fight. You have my word."
    "The two commanders, while at odds ideologically, can see that they have a common enemy."
    "There are more pressing matters than arguing over the ideal philosophy for the nation."
    
    show mihaila normal
    with dissolve
    
    tito "By the way, your soldiers have been attacking us all the way up the mountainside."
    
    play silsound3 "se/poke.ogg"
    show mihaila happy
    
    miha "Haha. Those rascals. Don't mind them, they're just a little confused about who to battle."
    "The {i}Cheatniks{/i} are currently fighting the {i}Vehrmaxt{/i}, although they dislike the xommunists too."
    "While Mihaila has opted for a temporary truce with Tito, he doesn't really have control over his troops."
    
    show tito determined
    show mihaila determined
    with dissolve
    
    tito "It doesn't matter. Those {i}Cheatniks{/i} up there who are now firing on us will have joined us within a year."
    miha "Well, the weapons are mine so if they do, you'll have to supply them yourself . . ."
    "Mihaila puts Tito down with another quip, somewhat expressionless. He seems to be a complicated old man . . ."
    
    show tito normal
    with dissolve
    
    tito "Hey, where'd you get all those guns anyway?"
    miha "Winstefina Churchill. The Britannians have been really generous lately, since the Vitalians invaded Grecia."
    "Britannian funding and weapons are flowing into Serpana to support the brave defenders."
    
    show tito determined
    with dissolve
    
    tito "Churchill, she's a great girl."
    tito "She is our enemy and has always been the enemy of xommunism, but she is an enemy one must respect, an enemy one likes to have."
    
    play silsound5 "se/silly16.ogg"
    show mihaila happy
    
    miha "Whatever. Keep up that kind of language and you'll never get any guns or money."
    
    show mihaila normal
    show tito normal
    with dissolve
    
    miha "By the way, is Tito your only name?"
    tito "It will do for the moment."
    
    play silsound3 "se/poke.ogg"
    show mihaila shock
    
    miha "Wait, is it? Or isn't it?"
    tito "Don't ruin a good quote."
    "It seems like Tito's really starting to care about her image."
    
    show mihaila normal
    with dissolve
    
    "Mihaila lights a pipe and raises his left hand in a wave."
    miha "Anyway, we'll be heading our own way now. Take care in your struggles, Commander Tito."
    tito "And you."
    
    play sound4 "se/walk.ogg"
    hide mihaila
    with dissolve
    show tito at center
    with ease
    
    "Casually puffing on his tobacco, the complicated old fighter strolls away, his men hiking up the hillside behind him."
    tito "Farewell, Mihaila. I hope our paths don't cross again too soon."
    
    show tito determined
    with dissolve
    
    "As the band of {i}Cheatniks{/i} disappears into the treeline, Tito turns her attention to her own comrades."
    "The people struggle through the thick woodland, carrying what they can, pushing forward through the undergrowth."
    tito "Fear not. I will protect you . . . all of you."
    "Determined to fight her corner, Tito doesn't give up, retreating to safety in order to fight another day."
    "The future will be difficult and fraught with danger. But for a free Serpana, she knows it will be worth it."
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    stop soundfx3 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000229
    
#####################################################################################################################################################
#sc0000229	-	Serpana army trying to escape into Epirus/Trapped
#####################################################################################################################################################
label sc0000229:
    play soundfx "se/battle2.ogg" fadein 3.0
    play soundfx2 "se/bombers.ogg" fadein 3.0
    play soundfx3 "se/march.ogg" fadein 3.0
    scene day2
    with fade
    play music "music/evil.ogg"
    
    "Some days later, it's all over. War has come to an end in the middling nation of Serpana . . ."
    
    show object_serpanadefeated at tankpos
    with dissolve
    
    "After only eleven days of bloody fighting, representatives of the former government have signed an armistice."
    "With Simovic on the run, and King Petey missing, those responsible are nowhere to be found."
    "In a pocket to the south of the country, remnants of the defending army throw down their arms."
    "The soldiers had been desperately scrambling for the border with Epirus, trying to escape."
    "Now their {i}Axle{/i} enemies are pushing even further south, towards the border with Grecia."
    "It seems they have unfinished business to attend to, clearing up Mussorinni's messes . . ."
    
    hide object_serpanadefeated
    with dissolve
    stop soundfx3 fadeout 3.0
    scene forest_day
    with dissolve
    play sound4 "se/brush.ogg"
    
    "From amongst the brambles and weeds of a forest clearing, a hunched figure keeps an eye out for patrols."
    
    show simovic shock
    with dissolve
    
    simovic "Ha . . . ha . . . not long to go . . . almost there. Then it's just a very long trip to Albion . . ."
    "Simovic has been waylaid on her escape route out of the defeated nation, and waits for her chance."
    simovic "Petey made his way via Grecia. If I can get to the border and join up with {i}Alliance{/i} troops, I'll have made it . . ."
    "Like all the other governments-in-exile, Serpana's old ministers are hoping to continue the fight from abroad."
    "With Churchill's help, maybe they can bring an end to Hitora's new regime of terror."
    
    show simovic determined
    with dissolve
    
    simovic "What a total disaster . . . that's the last time I ever try to overthrow a government."
    simovic "I mean, it all came too quickly. We weren't prepared to defend our country. The army was split . . ."
    simovic "And fifth columnists and secret vascists sold us out . . ."
    "It is rather remarkable that the army collapsed after less than two weeks of fighting."
    "Polix, Norda . . . even Belgae held out longer than that."
    simovic "Farewell, my beautiful Serpana. I hope the Germanians leave you in one piece."
    
    play sound4 "se/brush.ogg"
    play sound3 "se/run.ogg"
    hide simovic 
    with dissolve
    
    "Abandoning her countrymen to their fate, Simovic dashes through the clearing and towards freedom."
    "There are dark days ahead for this nation. At the mercy of the {i}Axle{/i}, she will be split apart and occupied."
    "Much blood will be shed, many innocents will suffer, and Serpana shall never be the same again . . ."
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000230

#####################################################################################################################################################
#sc0000230	-	Hitora/Horthy/Antoness celebrate
#####################################################################################################################################################
label sc0000230:
    play soundfx "se/birds.ogg" fadein 3.0
    scene mansion1
    with fade
    play music "music/requiem.ogg"
    
    "At {i}Horthy's Magical Kingdom{/i}, residence of Hang's regent Miklosa Horthy, a delegation of {i}Axle{/i} representatives celebrates."
    
    show horthy happy at left2
    show antoness happy at right2
    show hitora hat angry at center
    with dissolve
    play silsound6 "se/silly17.ogg"
    
    hit "We did it! Serpana has fallen to the {i}Vehrmaxt{/i} in only a matter of days . . . those pathetic losers!"
    "After all their battling to secure the divided nation, the {i}Axle{/i} forces are finally gaining control of the region."
    "Serpana is their puppet once more, weakened and divided, with much land going to Hang, Germania, Vitalia and Bolga."
    "A puppet state in the west to be named Xrovat, and a military governorate in the east to be named Cervetiis."
    ewalda "Such a speedy victory. The enemy barely put up a fight. It really was a bizarre campaign . . ."
    hor "And a great team effort."
    
    play silsound4 "se/silly5.ogg"
    show hitora hat worry
    
    anton "Yeah! You couldn't have done it without our help, my Füühbar . . . are you proud of me? Say you're proud of me!"
    
    play silsound6 "se/silly20.ogg"
    show hitora hat angry
    show antoness moe
    
    hit "Yeah, right. Thanks for the landing strips and the artillery! You guys in Rumanum barely lifted a finger to help."
    anton "But . . . but I did it for you! I'm a good girl, my Füühbar! Tell me I'm a good dog. Tell me you're proud of me!"
    
    play silsound4 "se/poke.ogg"
    show hitora hat moe1
    
    hit "Gross! I have enough sycophants in Germania to deal with. I don't need another. You better start to toe the line or else . . ."
    
    play silsound2 "se/silly16.ogg"
    show antoness happy
    show hitora hat worry
    
    anton "Or else . . . what?"
    "As Hitora goes to retort, Antoness pulls a stuffed animal out of her pocket and waves it at the Füühbar."
    
    play silsound5 "se/silly9.ogg"
    
    hit "T-That's . . . Keitel!"
    anton "That's right. I've got your {i}Kuschelig Oberbefehlshaber der Vehrmaxt{/i} and I'm holding him hostage."
    keitel "{i}My Füühbar . . . help . . .{/i}"
    "Hitora even does the little voice to lend some gravitas, or the lack thereof, to the situation."
    hit "Hey! That's my teddy bear! Give it back! It's not for mutts to play with . . ."
    
    play silsound7 "se/silly1.ogg"
    show antoness insane
    
    anton "You'll have to catch me first. Catch me, my Füühbar, and tell me that you love me! Say that Antoness is a good girl!"
    
    play sound3 "se/dash.ogg"
    hide antoness
    with easeoutright
    play sound6 "se/scamper.ogg"
    
    "Before anyone can say anything more, Antoness gets on all fours and scampers away with the bear between her jaws."
    
    play silsound4 "se/poke.ogg"
    show hitora hat moe1
    
    hit "Damn dog! You'll slobber all over him. As soon as I catch you, I'll have you skinned alive!"
    
    play sound5 "se/dash.ogg"
    hide hitora
    with easeoutright
    play sound2 "se/run.ogg"
    
    "Adorofia Hitora dashes after the {i}Red Dog{/i} across the lawns of the estate, trying to get her to return the stolen toy."
    anton insane "Ahahahaha, my Füühbar is playing with me . . . together we'll {i}'play'{/i} all over this continent . . ."
    
    show horthy happy at center
    with ease
    
    hor "Always so full of enthusiasm, for the fight or the chase . . ."
    
    $ mouse_visible = False
    scene cg_horthy
    with dissolve2
    $ mouse_visible = True
    
    "Ewalda turns to Horthy, who smiles gently. There seems to be a calculating mind behind that calm expression."
    hor happy "After all, Serpana's loss is our gain . . ."
    ewalda "That's a rather somber attitude to have. Are you feeling sorry for Simovic, Petey and Prince Paulie?"
    hor "Not particularly. Hang will benefit from its alliance with Germania. We will grow fat from the spoils of our victories."
    hor "Old lands that were lost will be reacquired and we will liberate our former countrymen from the xommunist threat."    
    hor normal "Though, sometimes, I wish it hadn't come to war."
    ewalda "Was there any other option? It's not as though diplomacy would have brought back your southern territories."
    hor happy "You shouldn't dismiss diplomacy so quickly."
    hor "I remember when Czexa was divided, during the accords between Hitora and Britannian First Minister Chambers."
    "Horthy has a slight twinkle in her eye as she thinks back to that simpler time, before this deadly war began."
    
    play silsound3 "se/silly4.ogg"
    
    hor moe "I rode a beautiful white horse at the head of the procession, through the streets of annexed Czexan towns."
    hor "As I passed along the roads, girls embraced one another, fell upon their knees, and wept with joy . . ."
    
    play silsound4 "se/silly20.ogg"
    
    ewalda "T-They were crying?"
    hor happy "Because liberation had come to them at last, without war, without bloodshed . . ."
    hor normal "In any case, war is sometimes a necessary tradeoff. For an eventual peace. And a prosperous Hang . . ."
    ewalda "That's a very political answer."
    hor determined "I do my best to keep out of politics. I am the nation's sovereign . . . but I do what I can to keep the country together."
    hor "Girls like Szálasi and her {i}'Nyilaskeresztes Bugyi Párt'{/i}, though driven underground, appear to be gaining supporters once again."
    "That's the {i}'Arrow-Cross Panties Party'{/i}, an extremist vascist party, akin to Germania's {i}Nappi Party{/i}."
    hor "We have to placate the conservatives and right-wingers in this country. That means allying with Hitora. That means land grabs."
    hor "It means many, many things . . . and it's the path we've both chosen. To follow that girl, come what may . . ."
    "Ewalda absorbs Horthy's words slowly."
    "Together, the rabbit and the Pomeranian watch as the Füühbar chases Antoness around with a big stick . . ."
    
    scene day2
    with dissolve
    
    "As the campaign in Serpana draws to a close, the {i}Axle{/i} celebrates a small victory over a weak enemy."
    "Now, their eyes turn to Grecia. In the south, the Vitalians continue to battle in Epirus against the Grecians."
    "In the east, Starin watches their every move, putting pressure on allies like Rumanum and Bolga."
    "Meanwhile, the Britannians continue to resist in the deserts and at sea, landing troops where they see fit . . ."
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000231

#####################################################################################################################################################
#sc0000231	-	Churchill discusses Rommel
#####################################################################################################################################################
label sc0000231:
    scene black
    with fade
    
    $ mouse_visible = False
    show expression Text(_("Meanwhile, in the desert wastes of Gypta . . ."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx "se/wind.ogg" fadein 3.0
    play soundfx2 "se/outdoor_crowd.ogg" fadein 3.0
    play soundfx3 "se/tank_far.ogg" fadein 3.0
    scene day2
    with fade
    play music "music/teatime.ogg"
    
    "Far to the south, at the headquarters of the {i}Britannian Desert Forces{/i} . . ."
    
    scene pyramid
    show crowd
    with dissolve
    
    "There's a great commotion, as an important celebrity has returned for another visit."
    
    play sound4 "se/cardoor_open.ogg"
    play soundfx5 "se/battlecry2.ogg" fadein 2.0
    play sound6 "se/trumpet.ogg"
    show churchill hat determined large
    with dissolve
    
    "Winstefina Churchill, the pouty leader of Britannia, climbs out of her car and inspects the troops stationed there."
    "Going down the line, she looks over the uniforms, rifles and bayonets, greeting some soldiers as she does so."
    ch "Hmm, very good. Nice and tidy appearances, good postures, heavy woolen clothing and bowl haircuts . . ."
    
    show churchill hat happy large
    with dissolve
    
    ch "I feel confident we can hold this region against those cool Germanians, with their {i}Lugo Bust{/i} uniforms and fashionable ways."
    "After Germania's battles with {i}Franzo Libre{/i} and their bid to secure surrendered territory . . ."
    ". . . Britannia is lucky it managed to hold the {i}Axle{/i} at the border between Cyracana and Gypta."
    ch "Wavell did an admirable job pushing forward and humiliating Mussorinni's soldiers."
    
    show object_afrikaakorps at tankpos
    with dissolve
    
    "But news has reached the region that Erwina Rommel has landed nearby, and is already attacking."
    "Vitalians led by a Zipanguese rogue was one thing. A battle-hardened, tank-busting foxgirl is another."
    "Now, Churchill must rouse the men and women stationed here, to give them the stomach for a new fight."
    
    hide object_afrikaakorps
    show churchill hat moe4 large
    with dissolve
    
    ch "Listen soldiers! You have fought admirably, for your king and your country. But now, there is a new threat . . ."
    ch "Rommel, the dastardly fox, has launched her offensive, attacking with brute force, new armor and fresh tactics."
    "The troops all stand firm, admiring their leader. Ready to fight and die, to beat the {i}Nappi{/i} war machine."
    ch "That's not all. We do not fight alone. All of Europa is under fire. The Germanians are circling . . ."
    ch "With Serpana under siege, Hitora might turn her attention back this way and launch a secondary invasion."
    "From Assyria or from Cyracana, or even from across the Medata Sea . . . who knows what mad plans she has?"
    
    show churchill hat determined large
    with dissolve
    
    ch "It will be your job to hold the enemy forces and maintain peace in the area. I believe in you, so believe in yourselves too."
    ch "After all, it's a Britannian tradition to go fox-hunting. Together, we can stop this menace!"
    "Their shoes are shined, their faces are determined and their wits are keen. This is their colony. Part of their empire."
    "Britannia's forces in the southern deserts are strong and loyal, ready to beat back any attacks."
    
    show churchill hat moe4 large
    with dissolve
    play silsound4 "se/silly14.ogg"
    
    ch "That said . . . we'll be diverting some troops to the front in Grecia too, to be led by Jumbo . . ."
    
    play silsound6 "se/poke.ogg"
    
    allied shock "Huh? You mean we're losing more troops?"
    ch "W-We need the tanks and the soldiers there. Besides, you can all hold off the fox by yourselves, right?"
    allied "Where's Wavell? I feel like Wavell should be here to talk this through . . ."
    "As a new front opens up south of Serpana, the Britannians start to divert resources to fight in Grecia."
    "Though Vitalia is on the retreat here, Rommel may soon find a way to overcome the {i}Alliance{/i} defenses."
    "Will this second front become an issue once again in the weeks to come?"
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    stop soundfx3 fadeout 3.0
    stop soundfx5 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000235

#####################################################################################################################################################
#sc0000235	-	Rommel retaking Cyracana
#####################################################################################################################################################
label sc0000235:
    scene black
    with fade
    
    $ mouse_visible = False
    show expression Text(_("Meanwhile, outside the city walls of Tobrunsk, Cyracana . . ."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx "se/wind.ogg" fadein 3.0
    play soundfx2 "se/tank_far.ogg" fadein 3.0
    play soundfx3 "se/march3.ogg" fadein 3.0
    scene desert_smoke
    with fade
    play music "music/desert.ogg"
    
    "The advance of the {i}Dessous Afrikaa Korps{/i} and their recapture of Cyracana has caused must consternation in the southern deserts."
    "As the enemy forces retreat back towards their colonies, Rommel is merciless in her tactics."
    "The Vitalians are even calling the foxgirl {i}'Rommelita'{/i}, an affectionate nickname, meaning {i}'little Rommel'{/i}."
    "Even the foreign press has dubbed her the {i}'Desert Fox'{/i}, in recognition of her military prowess."
    
    show gariboldi determined at left3
    show rommel normal at right3
    with dissolve
    
    "However, not everyone is happy about the success of the Germanian contingent."
    
    play silsound4 "se/silly16.ogg"
    show rommel moe1
    
    gariboldi "You better not get a big head about this. I'm meant to be in charge here. You're supposed to listen to me."
    "Gariboldi stomps his feet and pouts, annoyed about being overshadowed by the flashy, furry commander."
    rom "What are you talking about?"
    gariboldi "You had orders to halt."
    rom "And? What's your point?"
    gariboldi "You're not meant to be ignoring orders! You're breaking the rules."
    "It's true that Rommel has been bending the rules a little, relying on insubordination and subterfuge to achieve victory."
    
    show rommel determined
    with dissolve
    
    rom "One cannot permit unique opportunities to slip by for the sake of trifles . . ."
    "Not that it matters. The {i}Afrikaa Korps{/i} had to stop short of the border wire in any case."
    
    show gariboldi determined at right25
    show rommel determined at right1
    with ease
    play sound2 "se/map.ogg"
    show map_tactical9 behind gariboldi at tacticalpos
    with dissolve
    
    rom "Fort Kaputz and Fort Zollum have fallen to the {i}Panzys,{/i} but a Britannian renegade named Strafer held the line."
    "Thanks to his daring, the Germanian advance has remained halted at the border with Gypta."
    "It didn't help that Rommel's {i}Panzys{/i} had also run out of fuel, so they had to circle back around for resupplies."
    rom "But never mind that. My aim is to take the war to the Britannians. I'm not going to sit around and dig in, needlessly."
    gariboldi "You're supposed to do as you're told."
    
    play silsound6 "se/silly4.ogg"
    show gariboldi shock
    show rommel moe1
    
    rom "It's fine, isn't it? Adorofia Hitora herself encouraged me to advance, so that's what I'm doing."
    gariboldi "Hey, this is {i}Il Douché's{/i} war, not the Füühbar's . . ."
    "Still, Rommel is behaving as though she has complete freedom of action here."
    
    show rommel determined
    show gariboldi normal
    with dissolve
    
    rom "But anyway, forget about Gypta for the moment. We have to focus on retaking Tobrunsk."
    rom "Despite the rest of Cyracana falling to the {i}Axle{/i}, the port town of Tobrunsk is still under {i}Alliance{/i} control."
    "After many decades of Vitalian control, the place was heavily fortified once taken by Ostralasians, making it impenetrable."
    "Now the city is surrounded on all sides by a perimeter, except at sea, where the {i}Britannian Royal Navy{/i} still has the upper hand."
    gariboldi "But . . . the {i}Vitalia Sirte{/i} division already tried that and failed."
    
    play silsound3 "se/silly9.ogg"
    show gariboldi shock
    show rommel normal
    
    rom "So? Let's try again?"
    gariboldi "T-Try again? Without direct orders? Are you mad?"
    "Rommel is beginning to see the problem with Gariboldi's leadership style."
    
    show rommel annoyed
    show gariboldi determined
    with dissolve
    
    rom "We have to take the city. If we don't, the Britannians will keep their foothold in Cyracana and stab us in the back."
    "The {i}Afrikaa Korps{/i} currently relies on goods and materiel imported from Europa, then transported on roads, cross-country."
    rom "Capturing Tobrunsk would help to reduce the length of supply lines and increase overall capacity."
    rom "Gaining such a strategically important port would also allow for a much easier push across the border into Gypta."
    gariboldi "We're struggling to hold Cyracana, and you want to attack the Britannians in Gypta again?"
    rom "Well, of course. The {i}Zues Canal{/i} is still our aim, just as it was the first time . . . before you Vitalians bungled it."
    "If the {i}Afrikaa Korps{/i} are aiming to take the {i}Zues Canal{/i}, they need a clear shot through Gypta and as few obstacles as possible."
    "Improved supply lines further east along the coast will help in that effort."
    
    hide map_tactical9
    with dissolve
    show gariboldi at left3
    show rommel at right3
    with ease
    
    gariboldi "So you want to take Tobrunsk? Even if we were to attempt such an attack . . . how could we pull it off?"
    
    show rommel normal
    with dissolve
    
    rom "Firstly, we want to prevent a breakout. The port is already surrounded due to our earlier interventions."
    rom "But, thanks to the new {i}Alliance{/i} perimeter, we're currently holding, since our artillery guns are out of range of the port."
    "A system of barbed wire, anti-tank ditches, mines, as well as AA-guns, are in place, ready to defend the city from attack."
    rom "Because of this, the {i}Axle{/i} investment simply controls any roads out of the town, meaning the garrison stays holed up."
    
    play silsound2 "se/poke.ogg"
    show rommel moe2
    
    gariboldi "Yes, I know how a siege works, thank you very much."
    
    show rommel determined
    with dissolve
    
    rom "With all this in place, now we're going to probe the defenses with {i}Panzy{/i} regiments, find weaknesses in the line and push on the soft spots."
    rom "Soon those Ostralasian rats will be hopping away like frightened kangaroos . . ."
    
    play silsound3 "se/silly20.ogg"
    show gariboldi shock
    show rommel moe1
    
    gariboldi "Eh? Hopping rats?"
    rom "Forget it."
    
    show gariboldi determined
    with dissolve
    
    gariboldi "Fine. Try and capture Tobrunsk off the march, if you can. But if this fails, I'm going to take this to the Füühbar."
    rom "Eh? I thought you only answered to {i}Il Douché{/i}?"
    gariboldi "B-Be quiet. Show your elders some respect."
    
    show rommel determined
    with dissolve
    
    "Soon enough, Rommel bursts into a toothy grin and adjusts her goggles."
    rom "Don't worry, old man. I'm not going to fail. We're taking this city, and that's that."
    "With determination, the foxgirl prepares to storm the port town."
    "After her great success in repelling Wavell's troops, she makes her mark on the region, pushing ahead with vigor."
    
    show speedlines behind gariboldi
    with circleirisout
    
    rom "Let's begin the siege!"
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    stop soundfx3 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000233

#####################################################################################################################################################
#sc0000233	-	Discussing Grecia with Badoglio
#####################################################################################################################################################
label sc0000233:
    scene black
    with fade
    
    $ mouse_visible = False
    show expression Text(_("In the east, on the border between Serpana and Grecia . . ."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx "se/tank_far.ogg" fadein 3.0
    play soundfx2 "se/airbase.ogg" fadein 3.0
    scene savanna
    with fade
    play music "music/rinni.ogg"
    
    "Straddling the border between Grecia and Serpana, {i}Axle{/i} forces converge for another campaign."
    "As per Hitora's promise, she can use her newfound control north of here to engage with Rinni's failed invasion."
    "With Simovic's support gone, the resistance inside Serpana has broken down into numerous tiny factions."
    "Xommunists are fighting vascists, anarchists are engaging royalists and ethnic tensions are rising."
    "The rebels are severely weakened, giving {i}Axle{/i} troops an easy time in maintaining control of roads and cities."
    "Now, Germania can focus its attention on Grecia and supporting their Vitalian allies . . ."
    
    show badoglio hat normal at left35
    show germaniangeneraloberst normal at right35
    with dissolve
    
    bad "I appreciate your efforts so far, Field Marshal Listte. We're relying on you Germanians far too much."
    listte "Never mind. I could use the work, anyway."
    bad "Really?"
    
    show germaniangeneraloberst determined
    
    listte "It's a chance to try out some our newer tank models too, so don't mention it."
    
    show badoglio hat happy
    show germaniangeneraloberst shock
    with dissolve
    play silsound5 "se/silly20.ogg"
    
    bad "Then I guess the stereotype of Germanians being gruff, serious and blunt all the time, is an unfounded one."
    listte "Huh? That's what you guys think of us?"
    "Listte seems to get a little self-conscious at that remark."
    
    show badoglio hat determined
    show germaniangeneraloberst determined
    with dissolve
    show badoglio at right25
    show germaniangeneraloberst at right1
    with ease
    play sound4 "se/map.ogg"
    show map_tactical13 behind badoglio at tacticalpos
    with dissolve
    
    "Unfurling a map of the strategic situation, the two strategists begin to consider the tactics of the upcoming battle."
    bad "The Vitalian forces are still caught up in the west, in Epirus, battling back the defending Grecians."
    listte "We'll aim to open up a second front in the east then, sending some {i}Panzys{/i} in from Bolga and Serpana."
    "It should hopefully take the Grecians by surprise and cause some confusion and panic."
    
    show badoglio hat normal
    
    bad "What's that {i}'J-Force'{/i} in the middle of the map?"
    listte "In the time since the initial invasion, Britannian troops, under a tubby commander called Jumbo, have joined in."
    listte "That's the contingent he'll be leading to face us when we arrive."
    "Positioned between the northern borders and Athenia, the Britannian group are awaiting the Germanian attack."
    "It's not like it's a big secret that the {i}Axle{/i} are making their way south anyway . . ."
    
    show badoglio hat determined
    show germaniangeneraloberst normal
    with dissolve
    
    bad "So we'll be facing the Britannians again . . ."
    listte "You guys are getting really good at forcing Churchill's hand on these things."
    "The Britannians also have a foothold on the islands of Kaptara, Maltana and Kyprosa from which to run their operations."
    "Although, it's not as though they've had much time to prepare. Intelligence suggests their supplies are limited, at best."
    listte "The goal is simple. We drive south towards Athenia and hope we can force a collapse in the enemy's position."
    listte "A quick, effective strike and a joint effort should lead to a reversal in fortunes and . . . eventually, victory."
    "Listte can't foresee the campaign lasting longer than a few months. But you never know how fate may turn against you."
    "The Germanians can only rely on their proven tactics to get through this . . ."
    
    hide map_tactical13
    with dissolve
    show badoglio hat normal at left35
    show germaniangeneraloberst determined at right35
    with ease
    
    listte "Mussorinni finally got what she wanted. You Vitalians better be grateful."
    
    play silsound2 "se/silly19.ogg"
    show germaniangeneraloberst shock
    
    bad "Ahh . . . mmm. Yes, we're very sorry for all the trouble."
    listte "There's no need to . . . well, yes, thank you for the apology."
    bad "I wish I could join you. Cavallero will be taking over here soon and continuing the campaign."
    listte "Hmm? And what of you?"
    
    show badoglio hat determined
    with dissolve
    
    bad "I'm to resign from the Vitalian general staff soon. {i}Il Douché{/i} wants me to take the fall for the campaign in Epirus . . ."
    listte "I see . . ."
    "After a disastrous war in Epirus, someone needs to take responsibility for it."
    
    show germaniangeneraloberst determined
    with dissolve
    
    "This is it. After some weeks of hesitation and delay, Germania is joining the battle for Grecia."
    listte "Our forces will soon flood across the southern borders of Serpana and Bolga, attacking the enemy lines."
    "Will they be able to recapture the magic of ancient campaigns as Mussorinni had once hoped?"
    "Will Grecia fall to the might of the {i}Axle{/i}? Or will this battle bog down their troops and turn into a slaughter?"
    "It's time to find out . . ."
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    #STRUCTURE CHANGES
    #GRECIA ADD
    $ active_divisions_items.update({
        "insignia-infanteriedivision050": infanteriedivision050_name,
        "insignia-infanteriedivision072": infanteriedivision072_name,
        "insignia-infanteriedivision073": infanteriedivision073_name,
        "insignia-infanteriedivision125": infanteriedivision125_name,
        "insignia-infanteriedivision164": infanteriedivision164_name,
        "insignia-panzerdivision002": panzerdivision002_name,
        "insignia-panzerdivision009": panzerdivision009_name,
        "insignia-panzerdivision016": panzerdivision016_name,
        "insignia-mountaindivision005": mountaindivision005_name,
        "insignia-mountaindivision006": mountaindivision006_name,
    })
    
    $ active_korps_items.update({
        "insignia-armeekorps018": armeekorps018_name,
        "insignia-armeekorps030": armeekorps030_name,
        "insignia-panzerkorps040": panzerkorps040_name,
        "insignia-armeekorps049": armeekorps049_name,
        "insignia-armeekorps050": armeekorps050_name
    })
    
    #Map Data
    $ mapdata = ScreenData("geomap2", "map13", "easternmap")
    
    #Allegiances Data
    $ active_allegiances_items.pop("serpana", [serpana_motto, serpana_flag, serpana_flag2, serpana_description, serpana_name, serpana_coa, serpana_hostility, serpana_power, serpana_allegiance, serpana_text])
    $ active_allegiances_items.update({"cervetiis": [cervetiis_motto, cervetiis_flag, cervetiis_flag2, cervetiis_description, cervetiis_name, cervetiis_coa, cervetiis_hostility, cervetiis_power, cervetiis_allegiance, cervetiis_text]})
    $ active_allegiances_items.update({"xrovat": [xrovat_motto, xrovat_flag, xrovat_flag2, xrovat_description, xrovat_name, xrovat_coa, xrovat_hostility, xrovat_power, xrovat_allegiance, xrovat_text]})
    $ singidun_siege = False
    $ singidun_governor = "Dankman"
    $ singidun_governor_pic = "{image=side soldier happy}"
    $ singidun_command = command_one
    $ singidun_management = management_two
    $ singidun_influence = influence_one
    $ singidun_publicorder -= 165
    $ singidun_hostility = cervetiis_hostility
    $ singidun_allegiance = cervetiis_allegiance
    $ singidun_alignment = cervetiis_alignment
    $ singidun_martial = [
        "infantry_germania_gunner_heer5_profile",
        "infantry_germania_gunner_heer5_profile",
        "infantry_germania_gunner_heer5_profile",
        "antitank_panzerjager_profile",
        "panzer_panzer4_profile",
        "panzer_stug3_profile",
        "airsupport_shrike_profile"
        ]
    $ active_maptown_items.update({"singidun": [singidun_name, singidun_size, singidun_governor, singidun_governor_pic, singidun_hostility, singidun_alignment, singidun_population, singidun_publicorder, singidun_influence, singidun_command, singidun_management, singidun_farming_worth, singidun_mining_worth, singidun_industry_worth, singidun_trade_worth, singidun_entertainment_worth, singidun_military_worth, singidun_corruption_worth, singidun_unlocktown, singidun_martial, singidun_siege, singidun_company_img, singidun_company_text, .62, .5]})
    
    #Additional Map Data
    $ map_update_title = map_update_title5
    $ map_update_subtitle = map_update_subtitle5
    $ map_update_description = map_update_description5
    $ map_update_happen = True
    
    #Mission Data
    if "bat000056" in active_invasionbeacons_items:
        $ log.markfailure("bat000056")
        $ active_invasionbeacons_items.pop("bat000056", [bat000056_description, bat000056_title, bat000056_type, bat000056_x, bat000056_y])
    $ active_invasionbeacons_items.pop("bat000053", [bat000053_description, bat000053_title, bat000053_type, bat000053_x, bat000053_y])
    $ active_invasionbeacons_items.update({"bat000060": [bat000060_description, bat000060_title, bat000060_type, bat000060_x, bat000060_y]})
    $ active_invasionbeacons_items.update({"bat000055": [bat000055_description, bat000055_title, bat000055_type, bat000055_x, bat000055_y]})
    
    #Mission Assign
    $ log.assign("[bat000060_title]")
    $ log.assign("[bat000055_title]")
    
    #Go To Map
    jump map_begin
    
#####################################################################################################################################################
#bat000060	-	Operation Kangaroo: Siege of Tobrunsk
#####################################################################################################################################################
label bat000060:
    hide screen mapchoice1
    $ renpy.block_rollback()
    $ _rollback = True
    $ store.text_history_enabled = True
    window hide
    play sound6 "se/march2.ogg"
    stop music fadeout 2.0
    scene black
    with dissolve
    
    $ mouse_visible = False
    show expression Text(_("[bat000060_title]"), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    show expression Text(_("Tobrunsk, Cyracana"), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx "se/battle.ogg" fadein 3.0
    play soundfx2 "se/tank_invasion.ogg" fadein 3.0
    scene desert_smoke
    with fade
    play music "music/battle_desert.ogg"
    
    "In the deserts of Cyracana, as dust storms blow and sands shift, the {i}Afrikaa Korps{/i} converges on a single city . . ."
    
    show object_tobrunsk at tankpos
    with dissolve
    
    "The fortified port of Tobrunsk is defended by a series of trenches and bunkers on the outskirts of the settlement."
    "These {i}'boxes'{/i} form a line of defense, surrounded by minefields and barbed wire, manned by Ostralasians."
    
    hide object_tobrunsk
    with dissolve
    $ mouse_visible = False
    scene cg_rommel2_2
    with dissolve2
    $ mouse_visible = True
    play silsound5 "se/silly16.ogg"
    
    rom determined "Take that! And this! And one of those! Try throwing a shrimp on your barby now, you stinking Ostralasians . . ."
    "Probing weaknesses in the line with her {i}Panzys{/i}, Rommel the {i}Desert Fox{/i} pushes at the defenses."
    "Making a small bridgehead, the Germanian forces advance along the perimeter, under the cover of a sandstorm."
    rom "If we can move our artillery forward and take those trenches, we'll be within range to strike the port . . ."
    "Trickling forward, the {i}Axle{/i} tanks are met by Britannian cruiser and infantry tanks, and they exchange fire."
    "Vitalians dig in on the flanks as Germanians push ahead, storming the enemy positions, enduring artillery strikes."
    "Meanwhile, high above, the {i}Ruftwaffe{/i} and the {i}Douché Aeronautica{/i} fly sorties, bombarding the lines."
    "Tobrunsk is under siege . . . will the {i}Alliance{/i} manage to hold out?"
    rom "Ha ha! Tough chance!"
    
    stop music fadeout 1.0
    stop soundfx fadeout 1.0
    stop soundfx2 fadeout 1.0
    scene black
    with pixellate    
    
    jump bat000060_begin
    
label bat000060_begin:
###########################################################################
    #bat000060	-	Battle
###########################################################################
    
    #History Block
    $ renpy.block_rollback()
    $ store.text_history_enabled = False
    $ _rollback = False
    $ config.skipping = False
    
    #Enemy Team Set
    $ enemy_team = BaseTeam("Enemy", Solid("#000000", xysize=(50,50)), limit=50)
    $ enemy_team.add_fighter("enemy_anzac_gunner_heer6")
    $ enemy_team.add_fighter("enemy_panzer_matilda2")
    $ enemy_team.add_fighter("enemy_panzer_crusader")
    $ enemy_team.add_fighter("enemy_britannia_antitank_heer6")
    $ enemy_team.add_fighter("enemy_panzer_archer")
    
    #Playing For New Side Set - Axle
    $ empty_data("fighter")
    $ load_data(afrikaakorps_fighter_set, "fighter")
    
    # Selection Screen Set
    $ airsupport_section_unlocked = False
    $ infantry_section_unlocked = False
    $ panzer_section_unlocked = True
    $ antitank_section_unlocked = True
    $ commander_section_unlocked = True
    $ specialgroup_section_unlocked = True
    $ player_team = BaseTeam("Player", Solid("#000000", xysize=(50,50)), limit=50)
    play battlemusic "music/map3.ogg"
    call screen non_battle_party_screen

    # Battle Set
    $ config.skipping = False
    $ yamato_lvlcheck()
    stop battlemusic fadeout 1.0
    scene black
    $ renpy.pause(1.0, hard=True)
    play battlesfx "se/battle4.ogg" volume 0.25
    play battlemusic "music/battle_desert.ogg"
    $ renpy.block_rollback()
    $ fight_end = "bat000060_aftermath"
    $ game = Battleground("Battle Stage   |   Operation Kangaroo", player_team.store[0], enemy_team.store[0], "deserttower")
    $ battle_terrain = "desert"
    $ battleground_bg = "background_desert"
    $_game_menu_screen = None
    $ config.skipping = False
    $ config.keymap['skip'].remove('K_LCTRL')
    $ config.keymap['skip'].remove('K_RCTRL')
    $ config.keymap['hide_windows'].remove('h')
    $ renpy.clear_keymap_cache()
    call screen battle_screen(bg=battleground_bg, disc="plate_desert", dec_1=["decoration_desert_front3", 950, 0], dec_2=["decoration_desert_back2", 3, 320]) with battleopening 
    $ renpy.block_rollback()
    
label bat000060_aftermath:
    scene black
    $ renpy.pause(1.0, hard=True)
    
    #Aftermath
    $ persistent.skip_battle_sensitive = False
    $ skip_battle_selected = False
    $ battle_count +=1
    $ battlestats_up()
    $_game_menu_screen = "save_screen"
    $ renpy.block_rollback()
    $ airsupport_section_unlocked = False
    $ infantry_section_unlocked = True
    $ panzer_section_unlocked = True
    $ antitank_section_unlocked = True
    $ commander_section_unlocked = True
    $ specialgroup_section_unlocked = True
    $ cp = max_cp
    $ cp += cp_levelset
    $ max_cp += max_cp_levelset
    $ yamato_levels +=1
    
    #After Battle Continue
    $ _rollback = True
    $ store.text_history_enabled = True
    $ config.keymap['skip'].append('K_LCTRL')
    $ config.keymap['skip'].append('K_RCTRL')
    $ config.keymap['hide_windows'].append('h')
    $ renpy.clear_keymap_cache()
    
    jump bat000060_continue
    
###########################################################################
    #bat000060	-	Battle End
###########################################################################
label bat000060_continue:
    
    play soundfx "se/battle3.ogg" fadein 3.0
    play soundfx2 "se/tank_invasion.ogg" fadein 3.0
    scene desert_smoke
    with pixellate
    play music "music/evil.ogg"
    
    #Mission Marked Done
    $ log.markdone("bat000060")
    $ active_invasionbeacons_items.pop("bat000060", [bat000060_description, bat000060_title, bat000060_type, bat000060_x, bat000060_y])
    
    "No matter what Rommel throws at them, the Ostralasians hold their ground and pin down the Germanian infantry."
    
    show object_tobrunsk at tankpos
    with dissolve
    
    "Using anti-tank fire, the {i}Alliance{/i} defenders push back the {i}Panzys{/i}, using field guns and heavy artillery."
    "For the first time in the war, Germanian {i}Panzy{/i} units have actually been stopped in their tracks."
    "As hillocks and defensive positions are gained and lost, raiding parties sally forth to attack and reclaim forward posts."
    "Soon, a stalemate is reached and it seems there will be no decisive engagement to take Tobrunsk . . ."
    
    hide object_tobrunsk
    with dissolve
    show rommel annoyed
    with dissolve
    play silsound4 "se/silly14.ogg"
    
    rom "Grrrrr . . . damn it all, those Ostralasians are just too determined . . . fall back! Fall back!"
    "With her plan having failed, Rommel makes a tactical retreat for the day, repulsed by anti-tank fire."
    "The hot sand whips up into a dust storm, as the Germanians start to pull back along the perimeter."
    rom "There are more pressing concerns along the front. More ammunition is needed, and communications need improving . . ."
    "Though it would be a useful port to possess, the rest of the front in Cyracana needs reinforcing and supplying first."
    "Unless Tobrunsk is evacuated, the fortified port will settle into a routine siege of patrols, raids and small-scale attacks."
    "The push towards Zues is still at the front of Rommel's mind. She won't let one siege upset that . . ."
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump map_return
    
#####################################################################################################################################################
#bat000055	-	Operation Hercules: Battle of Grecia I
#####################################################################################################################################################
label bat000055:
    hide screen mapchoice1
    $ renpy.block_rollback()
    $ _rollback = True
    $ store.text_history_enabled = True
    window hide
    play sound6 "se/march2.ogg"
    stop music fadeout 2.0
    scene black
    with dissolve
    
    $ mouse_visible = False
    show expression Text(_("[bat000055_title]"), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    show expression Text(_("The Xlidi Pass, Grecia"), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx "se/battle3.ogg" fadein 3.0
    play soundfx2 "se/tank_invasion.ogg" fadein 3.0
    scene desert_bunker
    with fade
    play music "music/glory.ogg"
    
    "The Germanians begin their invasion of Grecia from Bolga and southern Serpana, sweeping south."
    
    show object_greciainvasion at tankpos
    with dissolve
    
    "Attacking the exposed flanks of the hastily-assembled Britannian forces, tanks and infantry push towards the Xlidi Pass."
    "A steep and rocky valley, bitterly cold and difficult to defend, the pass is held by Ostralasians and other colonial troops."
    "Artillery and mortar fire harrass Grecians down the line, as heavy weapons are turned on Britannian machine guns."
    "The {i}Alliance{/i} troops engage in counterattacks to retain control of vital points, holding ridges and bunkers in the pass."
    
    hide object_greciainvasion
    with dissolve
    show vasey determined
    with dissolve
    
    "Bloody Vasey, an Ostralasian commander, fights desperately to keep back the advancing {i}Waffen-ZZ{/i} troops."
    vasey "No bloody moving from your bloody positions! That's a bloody order . . ."
    "Bravely holding the line and the surrounding hills, he does his best to keep morale high and ensure the men stay in line."
    
    play silsound3 "se/silly1.ogg"
    
    vasey "And if any bloody Germanian gets between your post and the next, turn your bloody bren around and shoot him up the bum!"
    "As the {i}Waffen-ZZ{/i} infantry push on gaps in the defensive line, a fierce confrontation occurs . . ."
    
    stop music fadeout 1.0
    stop soundfx fadeout 1.0
    stop soundfx2 fadeout 1.0
    scene black
    with pixellate
    
    jump bat000055_begin
    
label bat000055_begin:
###########################################################################
    #bat000055	-	Battle
###########################################################################
    
    #History Block
    $ renpy.block_rollback()
    $ store.text_history_enabled = False
    $ _rollback = False
    $ config.skipping = False
    
    #Enemy Team Set
    $ enemy_team = BaseTeam("Enemy", Solid("#000000", xysize=(50,50)), limit=50)
    $ enemy_team.add_fighter("enemy_germania_gunner_heer5")
    $ enemy_team.add_fighter("enemy_panzer_panzer4")
    $ enemy_team.add_fighter("enemy_germania_marksman_heer5")
    $ enemy_team.add_fighter("enemy_panzer_tiger")
    
    #Playing For New Side Set - Alliance
    $ empty_data("fighter")
    $ alliance_fighter_set += ("infantry_britannia_gunner_heer6", "infantry_britannia_antitank_heer6", "specialgroup_grecia_gunner_heer5")
    $ load_data(alliance_fighter_set, "fighter")
    
    # Selection Screen Set
    $ airsupport_section_unlocked = False
    $ infantry_section_unlocked = True
    $ panzer_section_unlocked = True
    $ antitank_section_unlocked = False
    $ commander_section_unlocked = False
    $ specialgroup_section_unlocked = True
    $ player_team = BaseTeam("Player", Solid("#000000", xysize=(50,50)), limit=50)
    play battlemusic "music/map3.ogg"
    call screen non_battle_party_screen

    # Battle Set
    $ config.skipping = False
    $ yamato_lvlcheck()
    stop battlemusic fadeout 1.0
    scene black
    $ renpy.pause(1.0, hard=True)
    play battlesfx "se/battle4.ogg" volume 0.25
    play battlemusic "music/battle_desert.ogg"
    $ renpy.block_rollback()
    $ fight_end = "bat000055_aftermath"
    $ game = Battleground("Battle Stage   |   Operation Hercules", player_team.store[0], enemy_team.store[0], "hedgehog")
    $ battle_terrain = "mountain"
    $ battleground_bg = "background_bunker"
    $_game_menu_screen = None
    $ config.skipping = False
    $ config.keymap['skip'].remove('K_LCTRL')
    $ config.keymap['skip'].remove('K_RCTRL')
    $ config.keymap['hide_windows'].remove('h')
    $ renpy.clear_keymap_cache()
    call screen battle_screen(bg=battleground_bg, disc="plate_dirt", dec_1=["decoration_forest_front2", 950, 0], dec_2=["decoration_ship_back1", 3, 320]) with battleopening 
    $ renpy.block_rollback()
    
label bat000055_aftermath:
    scene black
    $ renpy.pause(1.0, hard=True)
    
    #Aftermath
    $ battle_count +=1
    $ battlestats_up()
    $_game_menu_screen = "save_screen"
    $ renpy.block_rollback()
    $ cp = max_cp
    $ cp += cp_levelset
    $ max_cp += max_cp_levelset
    
    #Unlocked Player Team Set
    if not skip_battle_selected:
        $ axle_fighter_set.append("panzer_tiger")
        $ alliance_fighter_set += ("infantry_anzac_gunner_heer6", "specialgroup_grecia_marksman_heer5", "panzer_bishopsph")
        $ load_data([
            "infantry_anzac_gunner_heer6",
            "specialgroup_grecia_marksman_heer5",
            "panzer_bishopsph"
            ], "fighter")
        $ yamato_levels +=1
    $ persistent.skip_battle_sensitive = False
    $ skip_battle_selected = False
    
    #After Battle Continue
    $ _rollback = True
    $ store.text_history_enabled = True
    $ config.keymap['skip'].append('K_LCTRL')
    $ config.keymap['skip'].append('K_RCTRL')
    $ config.keymap['hide_windows'].append('h')
    $ renpy.clear_keymap_cache()
    
    jump bat000055_continue
    
###########################################################################
    #bat000055	-	Battle End
###########################################################################
label bat000055_continue:
    
    play soundfx "se/battle3.ogg" fadein 3.0
    play soundfx2 "se/tank_invasion.ogg" fadein 3.0
    scene desert_bunker
    with pixellate
    play music "music/evil.ogg"
    
    #Mission Marked Done
    $ log.markdone("bat000055")
    
    "The battle in the Xlidi Pass fails to hold off the assaulting {i}ZZ{/i} forces, who crash forward into the valley with their tanks."
    
    show object_greciainvasion at tankpos
    with dissolve
    
    "Germanian self-propelled guns attack along the width of the sector, the hulking machines somehow climbing the slopes."
    "Disturbed by the shelling, and unable to go on, many Britannians simply abandon their positions and are taken prisoner."
    
    hide object_greciainvasion
    with dissolve
    show vasey shock
    with dissolve
    play silsound6 "se/poke.ogg"
    
    "Soon, orders come down the line to retreat and head for Thermomalis, to set up a defensive line there."
    vasey "We can't hold them here. The roof is leaking! I repeat, the roof is leaking! We have to evacuate . . ."
    "The {i}Alliance{/i} troops, used to the desert heat, struggle to hold the pass, dug into their speedily-fortified bunkers and trenches."
    "Many have frostbite from the cold, spending the nights in thin uniforms, having arrived fresh off the boat from Gypta."
    
    play soundfx3 "se/march.ogg" fadein 3.0
    show vasey determined
    with dissolve
    
    "As some Britannian tanks intervene to hold off the Germanian guns, {i}Alliance{/i} columns begin their withdrawal to the south."
    vasey "Bloody Germanians and their bloody self-propelled guns causing bloody mayhem in the bloody valley . . . bloody Germanians . . ."
    "The hasty retreat leaves some Grecian positions compromised, but there's little that can be done as the weak flanks collapse."
    "After only a few days, the {i}Axle{/i} invasion of mainland Grecia has proved a triumph, as the {i}Alliance{/i} are on the run . . ."
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    stop soundfx3 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000234
    
#####################################################################################################################################################
#sc0000234	-	Messe grateful for relief
#####################################################################################################################################################
label sc0000234:
    play soundfx "se/tank_invasion.ogg" fadein 3.0
    play soundfx2 "se/battle4.ogg" fadein 3.0
    scene savanna
    with fade
    play music "music/rinni.ogg"
    
    "With the Germanian army's entry into Grecia, the forces of Vitalia in Epirus can start to rest easy."
    "{i}Il Douché's{/i} unsuccessful push for land and a swift victory turned into an unmitigated disaster and stalemate."
    "Now the {i}Vehrmaxt{/i} are here to reinforce the front and clear a path through the enemy lines."
    
    show messe happy
    with dissolve
    play silsound5 "se/poke.ogg"
    
    messe "Ahhh . . . relief . . . I'm so relieved . . . the reinforcements are finally here."
    "Messe sighs gently, happy to push on at last and make some headway in the campaign."
    messe "And it's not even {i}Il Douché{/i} doing the reinforcing. Hehe, you're so unreliable sometimes, {i}Il Douché{/i}."
    "The blue-haired commander smiles sweetly in the sunshine, thinking on the improved situation."
    
    show messe shock
    with dissolve
    
    messe "Still, why is it that Hitora's armies had to show up and not Mussorinni's? This is meant to be Vitalia's fight."
    
    play silsound3 "se/silly16.ogg"
    
    messe "First in Gypta and the Medata Sea, and now here too . . . a-are we really that desperate?"
    "Pretty soon, Messe makes a great realization about the capabilities of her countrymen."
    
    show messe determined
    with dissolve
    
    messe "Now the Germanians are involved . . . things may get more intense than we'd hoped."
    "Perhaps there are dark things on the horizon for this conflict in Grecia . . ."
    "With the war in Grecia heating up, both Germania and Britannia leap to the defense of their allies."
    "The trench warfare of the past months give way to the speedy lightning battles of the western front."
    "Stalemate is broken and Messe's forces can fight the good fight, at long last . . ."
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000236
    
#####################################################################################################################################################
#sc0000236	-	Wavell on the run
#####################################################################################################################################################
label sc0000236:
    scene black
    with fade
    
    $ mouse_visible = False
    show expression Text(_("Eastward, at the headquarters of the Britannian Desert Forces . . ."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx "se/wind.ogg" fadein 3.0
    scene pyramid
    show wavell shock
    with fade
    play music "music/teatime.ogg"
    
    "Behind enemy lines, the leader of the {i}Britannian Desert Forces{/i} receives news of the counterattack."
    
    play silsound5 "se/silly12.ogg"
    
    wavell "Tobrunsk is under siege?! By a cute foxgirl? I don't believe it . . ."
    "The Britannian commander has already experienced the shock of a Vitalian invasion and having to fight back to the west."
    "The war in Grecia has also been a distraction, with high numbers of troops shipped off to Kaptara to help fight."
    "Wavell will be shipping out there herself soon as well, to help Jumbo hold off the {i}Axle{/i} forces."
    wavell "What bad timing. All my tanks were sent to help Jumbo defend those Grecian temples . . ."
    "Now this approach in the form of Rommel and her {i}Dessous Afrikaa Korps{/i} has knocked Wavell off her high horse."
    wavell "Intelligence said that she'd be remaining on the defensive for another few weeks . . . damn."
    "This {i}Axle{/i} reversal of fortune means that, once again, the Britannians are on the run."
    
    show wavell determined
    with dissolve
    
    wavell "Damn. And we'd practically just chased the Vitalians into the sea."
    "Stories of Rommel's daring and extraordinary charisma have already reached the ears of the Britannian forces."
    "Rumors and urban legends surrounding her martial prowess or the mystical powers of her furry tail . . ."
    sol shock "All our triumphs have been undone! What do we do? How can we stop Rommel from destroying us at Tobrunsk?!"
    
    play silsound3 "se/silly3.ogg"
    
    allied shock "What do we do if she tries to tickle us with her foxtail? I don't want to be cursed!"
    britanniangen determined "Our tanks just can't match theirs. How are we supposed to beat something like the {i}Panzy IV{/i}?"
    "Wavell must do her best to dispel the myth of the foxgirl. Her soldiers look to her for encouragement."
    
    show wavell happy
    with dissolve
    
    wavell "There's nothing for it. Tobrunsk must be held. I won't allow the citadel to fall to the likes of Rommel."
    sol determined "But . . . how?"
    wavell "We will pour supplies into the city by air and sea . . . a hundred tons a day if we have to."
    wavell "And soon enough, reinforcements will arrive on the fast merchant convoys. Then we'll see who has the last laugh."
    "On hearing the news of Rommel's arrival, Churchill acted fast and commissioned the speediest ships possible to help send materiel."
    "{i}Hurrycane{/i} fighters, {i}Ducky I's, Krusaders{/i}, and a few dozen cruiser tanks too, will be arriving . . . in the next weeks."
    
    show wavell determined
    with dissolve
    
    wavell "The Britannians have had enough surprises in this war. It may take a while, but we won't be beaten any longer."
    sol "So how are we going to hold off Rommel if all of our supplies are in Grecia or at sea still?"
    wavell "I . . . don't know. I might have to convince Jumbo himself to send back some tanks. I'm needed in Grecia anyway."
    "Wavell bites her lip, frustrated at the situation. She knew that draining resources here was a bad move."
    wavell "This will have to wait until I get back. Until then, we'll just have to distract that sly fox . . ."
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000465
    
#####################################################################################################################################################
#sc0000465	-	Serpana warcrimes
#####################################################################################################################################################
label sc0000465:
    scene black
    with fade
    
    $ mouse_visible = False
    show expression Text(_("Meanwhile, in occupied Serpana . . ."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx "se/wind.ogg" fadein 3.0
    play soundfx2 "se/battle2.ogg" fadein 3.0
    scene day4
    with fade
    play music "music/horror.ogg"
    
    "Across the former territory of Serpana, as the war comes to an end, the occupiers get to work committing atrocities . . ."
    "The {i}Uztazhaz{/i} regime in the new state of Xrovat begins exterminating civilians in massacres."
    "The local population are rounded up and hacked to death, or thrown into ravines and locked inside burning churches . . ."
    "Germanian forces, encountering resistance, retaliate by murdering a hundred hostages for each Germanian killed."
    "Armies from Vitalia and Hang carry out similar summary executions and reprisals, burning villages to ash."
    "Concentration camps are quietly established as enemies of the state are rounded up and taken away . . ."
    "Untold horrors begin to be unleashed on the terrorized civilians of this conquered nation."
    "Only the equally bloody {i}Cheatniks{/i} and Partisans are prepared to do something about it . . ." 
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000203

#####################################################################################################################################################
#sc0000203	-	Mannerheim wonders when the fight will come again
#####################################################################################################################################################
label sc0000203:
    scene black
    with fade
    
    $ mouse_visible = False
    show expression Text(_("Far away, at the former fortifications of the Mannerheim Line, Finbard . . ."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx2 "se/wind.ogg" fadein 3.0
    scene snow_day
    show snow
    with fade
    play music "music/soviagrad.ogg"
    
    "Finbard. An icy world, covered in forests, mountains, lakes and snow. The only solace here is alcohol and dancing."
    
    play sound4 "se/walk.ogg"
    show finbard normal behind snow at right3
    show mannerheim determined behind snow at left3
    with dissolve
    
    "Accompanied by a solitary soldier on duty, Mannerheim looks across the parapet to the newly claimed Sovian territory nearby."
    mann "Look at them . . . bunch of monsters and ingrates . . ."
    "She mutters in contempt, crossing her arms and not breaking eye contact."
    mann "One of these days, the fight will come again . . . and then we'll be ready for you."
    fin "Field Marshal? Who are you talking to? There's nobody else here but us . . ."
    "The young guard looks around in confusion."
    
    play silsound6 "se/silly3.ogg"
    show mannerheim moe
    show finbard shock
    
    mann "Idiot. I was speaking about the Sovians."
    
    show mannerheim normal
    show finbard normal
    with dissolve
    
    mann "Still, it has been quiet recently. I suppose that jumped-up corporal {i}Schnitzelgrubber{/i} has been keeping Starin busy . . ."
    
    show finbard determined
    
    fin "Even if Sovia and Germania have signed a pact, it must be scary having to share a border like that."
    mann "We share a border too y'know . . ."
    "Two world powers with opposed ideologies and competing interests in the region. Everyone is paying close attention to it."
    
    show mannerheim determined
    with dissolve
    
    mann "But I suppose whatever happens between those two is on another scale. Best not to think about it."
    "Mannerheim plays it off cooly. She really doesn't want to show allegiance to either side, despising both."
    "In any case, she would rather worry about Finbard's sovereign borders instead . . ."
    
    show finbard normal
    
    fin "I guess you're right. Besides, Churchill is still in the fight. And if things get bad, maybe even Amerika will show up."
    mann "Don't count your chickens."
    
    show finbard shock
    
    fin "Why? Did something happen to them?"
    
    play silsound2 "se/silly13.ogg"
    show mannerheim moe
    
    mann "It's a turn of phrase, numbskull."
    
    show mannerheim determined
    show finbard normal
    with dissolve
    
    "Sighing, the field marshal stands tall and peers across the barren wastes, towards the enemy lines once again."
    mann "One day, Starin . . . one of these days."
    "In these wild, foreboding plains, the bruised Finbardish armies wait quietly, watching events in Europa closely."
    "Mannerheim, their one shining star, must be the girl to give them hope and lead them forward, with their heads held high."
    "With memories of the {i}Wintertime War{/i} still fresh in their minds from the previous year, the people long for a shot at redemption."
    "Their second chance may be coming soon . . . a chance for vengeance, at last . . ."
    mann "Let's have another cup of cocoa until your shift ends."
    
    show finbard determined
    
    fin "Yes, field marshal!"
    
    stop soundfx2 fadeout 3.0
    stop music fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000237
    
#####################################################################################################################################################
#sc0000237	-	Churchill/Battenia discuss {i}Axle{/i} march into Grecia
#####################################################################################################################################################
label sc0000237:
    play soundfx "se/sea.ogg" fadein 3.0
    scene sea1
    with fade
    play music "music/requiem.ogg"
    show churchill hat determined at left3
    show battenia normal at right3
    with dissolve
    
    "On a Britannian capital ship, just moored off the coast of Kaptara, First Minister Churchill checks in."
    ch "So they've finally done it. The Germanians have come to the rescue and marched on Grecia . . ."
    "The {i}Axle{/i} have invaded across the northern borders and are quickly making their way south."
    "Britannian positions ahead of the central region of the country are being shored up for an attack."
    batt "I hope Jumbo knows what he's doing . . ."
    
    show churchill hat happy
    with dissolve
    
    ch "Jumbo can hold the line. I trust him not to retreat unless it's absolutely necessary."
    "It's vital that the {i}Alliance{/i} front in Grecia remains. It's the only thing standing between Hitora and the capital, Athenia."
    ch "Wavell should be arriving soon too, so we'll have two competent commanders in the region."
    
    play silsound5 "se/silly4.ogg"
    show churchill hat moe3
    show battenia angry
    
    batt "Well, one and a half . . . one, really, if you count them together."
    ch "T-There's no need to be such a cynic."
    batt "I'm just being realistic. I'm not sure we really have enough guns or supplies to sufficiently hold our positions."
    batt "Besides, there are reports that our forces are already starting to retreat to the south."
    ch "W-What?!"
    batt "The navy are preparing transport ships as we speak, to give the troops safe passage to Kaptara and Kyprosa."
    
    play silsound2 "se/poke.ogg"
    show churchill hat moe1
    show battenia shock
    
    ch "What do you know? You're just in the admiralty! You're an old cynical seadog."
    batt "Hey, you were in the admiralty too, you know!"
    ch "Ahh, well, being First Minister prepares you for . . . all the other aspects of a war . . ."
    batt "Liar. You're as unprepared for this war as anybody."
    
    show churchill hat determined
    show battenia normal
    with dissolve
    
    ch "In any case . . . we must make a stand. No matter what our provisions or supply lines are like."
    ch "Grecia must stand. We must strike a blow against Hitora's concept of a fortified, Germanian Europa."
    "Winning here will be as much an ideological victory as a strategic one . . ."
    batt "Well, Wavell has informed Bloody Vasey that he must hold Thermomalis, no matter what, so that may help."
    
    play sound6 "se/power.ogg"
    show churchill hat moe4
    show battenia angry
    with dissolve
    
    ch "Good. After all, if we hold the Grecian mainland, we can attack the {i}Axle's{/i} soft underbelly . . ."
    ch "If we hold the island of Kaptara, we can bomb the oilfields in Rumanum . . ."
    ch "If we control the {i}Medata Sea{/i}, Vitalia cannot act and we deny Hitora a powerful ally . . ."
    "Churchill instinctively believes that this battle may determine the fate of the war."
    "Depending on which way it goes, it could frustrate Germania's expansionist plans and cause confusion."
    "If anything, it would be a sorely needed victory against an evil archenemy and great publicity for the {i}Alliance{/i} cause."
    
    show churchill hat determined
    with dissolve
    
    ch "We have taken a grave and hazardous decision to sustain Grecia . . . let's hope it pays off."
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000238
    
#####################################################################################################################################################
#sc0000238	-	Grecia final briefing
#####################################################################################################################################################
label sc0000238:
    play soundfx "se/room.ogg" fadein 3.0
    scene warroom
    with fade
    play music "music/facepalm.ogg"
    
    "In the halls of the {i}Superimperiumskanzleistag{/i}, a couple of senior figures gather in Hitora's study."
    
    show hitora hat angry at left3
    show rinni hat determined at right3
    with dissolve
    play silsound6 "se/silly17.ogg"
    
    keitel "{i}Excellent news, my Füühbar! It took a lot of fighting but, Epirus has fallen to Axle forces once more!{/i}"
    "With her teddy bear in hand, Hitora talks over the trials and tribulations of the Grecian campaign."
    keitel "{i}Vitalia should be able to maintain control of the region for the foreseeable future, as we push into Grecia.{/i}"
    "The influx of Germanian troops from Serpana and Bolga led to a Grecian evacuation, aided by a Vitalian counterattack."
    "The enemy army has been badly hit, having progressed so far into one of Vitalia's colonies . . ."
    
    play silsound4 "se/silly7.ogg"
    show rinni hat happy
    show hitora hat worry
    
    rin "Yay, I did it! We've seen off the Grecians and Epirus belongs to Vitalia once more. What a great, final victory!"
    hit "Huh? Final victory?"
    rin "Now we can get serious. It won't be long before Athenia too is claimed for the Vitalian empire!"
    
    play silsound3 "se/silly9.ogg"
    show hitora hat angry
    show rinni hat moe2
    
    hit "What are you talking about? We'll be taking Athenia in Germania's name!"
    rin "B-B-But I invaded first! This is meant to be my campaign . . ."
    hit "And look at the mess we've had to clear up! It's only fair that we administer the nation's capital after its defeat."
    "Hitora is evidently annoyed by the spilled blood and wasted materiel spent on this invasion."
    keitel "{i}This miserable spectacle, laid on by our gallant ally, must have produced some hollow laughter from the Grecians.{/i}"
    
    play silsound2 "se/silly2.ogg"
    stop music fadeout 5.0
    
    rin "No fair, stop using your stuffed animals and sock puppets to gang up on me!"
    "Once again, Germania has paid the price for Vitalia's mistakes. Not that it was particularly expensive or difficult this time . . ."
    
    show rinni hat determined
    with dissolve
    play sound2 "se/map.ogg"
    show hitora at right25
    show rinni at right05
    with ease
    show map_tactical21 behind hitora at tacticalpos
    with dissolve
    play music "music/evil.ogg"
    
    keitel "{i}Soon enough, all of Grecia will be in Axle hands . . .{/i}"
    keitel "{i}Willy Jumbo's Britannian troops are still on the retreat now, as our forces push south into Grecia itself.{/i}"
    keitel "{i}But, there's news Wavell has landed further reinforcements at Kyprosa and in Athenia, to defend the area.{/i}"
    rin "Wavell, my old foe from my days fighting in Gypta . . ."
    "Since when did she do any of the fighting?"
    
    show hitora hat moe2
    with dissolve
    
    keitel "{i}Well, since the enemy is on the retreat, I think we should focus our efforts on pursuing them.{/i}"
    hit "Like a cop chase or something . . . how exciting."
    "Slow infantry will be no use for catching up with the enemy, so they'll put the motorized divisions to work, with tanks and bikes."
    
    hide map_tactical21
    with dissolve
    show object_grecianretreat behind hitora at tacticalpos
    with dissolve
    
    keitel "{i}The Britannians are headed for the southern coast, as they're evacuating their troops on ships anchored there.{/i}"
    keitel "{i}A commander known as Bloody Vasey intends for her soldiers to make a bold last stand, in a place known as Thermomalis.{/i}"
    "This ancient coastal region is famous for its ancient battles. To hold this area is to control the road to Athenia."
    rin "If we can take Thermomalis from the Grecians, it will deal a crushing blow to their national psyche."
    hit "The Britannians and their colonial subjects are fierce, but we can hold our own with them."
    
    hide object_grecianretreat
    show rinni hat moe4
    show hitora hat worry
    with dissolve
    show rinni at right3
    show hitora at left3
    with ease
    play silsound6 "se/silly1.ogg"
    
    rin "Then go do it, my amazing Vitalian troops! Win all of Grecia for the glory of Vitalia and your {i}Douché!{/i}"
    hit "Hey! I already told you, this is our operation now. We'll give you whatever leftovers we feel like handing you!"
    "The two petty dictators bicker with one another over their shared responsibilities and spoils." 
    "The extremely successful invasion of Grecia has sent the enemy armies into a full flight from the battlefield."
    "As the {i}Axle{/i} inch closer and closer to the capital city Athenia, they begin to approach the final stages of the campaign . . ."
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    #Map Data
    $ mapdata = ScreenData("geomap2", "map13", "easternmap")
    
    #Mission Data
    if "bat000060" in active_invasionbeacons_items:
        $ log.markfailure("bat000060")
        $ active_invasionbeacons_items.pop("bat000060", [bat000060_description, bat000060_title, bat000060_type, bat000060_x, bat000060_y])
    $ active_invasionbeacons_items.pop("bat000055", [bat000055_description, bat000055_title, bat000055_type, bat000055_x, bat000055_y])
    $ active_invasionbeacons_items.update({"bat000057": [bat000057_description, bat000057_title, bat000057_type, bat000057_x, bat000057_y]})
    
    #Mission Assign
    $ log.assign("[bat000057_title]")
    
    #Allegiances Data
    $ athenia_siege = True
    $ active_maptown_items.update({"athenia": [athenia_name, athenia_size, athenia_governor, athenia_governor_pic, athenia_hostility, athenia_alignment, athenia_population, athenia_publicorder, athenia_influence, athenia_command, athenia_management, athenia_farming_worth, athenia_mining_worth, athenia_industry_worth, athenia_trade_worth, athenia_entertainment_worth, athenia_military_worth, athenia_corruption_worth, athenia_unlocktown, athenia_martial, athenia_siege, athenia_company_img, athenia_company_text, .633, .62]})
    
    #Go To Map
    jump map_begin
    
#####################################################################################################################################################
#bat000057	-	Operation Zeus: Battle of Grecia II
#####################################################################################################################################################
label bat000057:
    hide screen mapchoice1
    $ renpy.block_rollback()
    $ _rollback = True
    $ store.text_history_enabled = True
    window hide
    play sound6 "se/march2.ogg"
    stop music fadeout 2.0
    scene black
    with dissolve
    
    $ mouse_visible = False
    show expression Text(_("[bat000057_title]"), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    show expression Text(_("Thermomalis, Grecia"), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx "se/battle.ogg" fadein 3.0
    play soundfx2 "se/tank_invasion.ogg" fadein 3.0
    scene temple
    with fade
    play music "music/battle_desert.ogg"
    
    "At the ancient pass of Thermomalis, at a temple on the surrounding hillsides, the {i}Alliance{/i} defenders battle on."
    "Freyaborg the Salamander was tasked with guarding the ancient pass, but now a small rearguard force is all that remains."
    
    show vasey determined
    with dissolve
    
    "Once again, the Ostralasian commander, Bloody Vasey, battles bravely to hold the pass and keep back the encroaching enemy."
    
    play silsound5 "se/silly4.ogg"
    
    vasey "Not another bloody pass . . . how many bloody passes do I have to bloody defend from these bloody Germanians?"
    "He really does like swearing after all . . ."
    vasey "Here we bloody well are and here we bloody well stay! Defend this pass, just like all the others and hold fast!"
    "A Germanian battlegroup fires on their position, backed up by an armored {i}Panzy{/i} division." 
    "Once again, colonial troops hold out in a delaying action, giving the rest of the army time to evacuate . . ."
    
    stop soundfx fadeout 1.0
    stop soundfx2 fadeout 1.0
    stop music fadeout 1.0
    scene black
    with pixellate
    
    jump bat000057_begin
    
label bat000057_begin:
###########################################################################
    #bat000057	-	Battle
###########################################################################
    
    #History Block
    $ renpy.block_rollback()
    $ store.text_history_enabled = False
    $ _rollback = False
    $ config.skipping = False
    
    #Enemy Team Set
    $ enemy_team = BaseTeam("Enemy", Solid("#000000", xysize=(50,50)), limit=50)
    $ enemy_team.add_fighter("enemy_vitalia_gunner_heer3")
    $ enemy_team.add_fighter("enemy_panzer_semovente")
    $ enemy_team.add_fighter("enemy_germania_antitank_heer5")
    $ enemy_team.add_fighter("enemy_panzer_panzer3")
    $ enemy_team.add_fighter("enemy_panzer_konigstiger")
    
    #Playing For New Side Set - Alliance
    $ empty_data("fighter")
    $ load_data(alliance_fighter_set, "fighter")
    
    # Selection Screen Set
    $ player_team = BaseTeam("Player", Solid("#000000", xysize=(50,50)), limit=50)
    play battlemusic "music/map3.ogg"
    call screen non_battle_party_screen

    # Battle Set
    $ config.skipping = False
    $ yamato_lvlcheck()
    stop battlemusic fadeout 1.0
    scene black
    $ renpy.pause(1.0, hard=True)
    play battlesfx "se/battle4.ogg" volume 0.25
    play battlemusic "music/battle_snow.ogg"
    $ renpy.block_rollback()
    $ fight_end = "bat000057_aftermath"
    $ game = Battleground("Battle Stage   |   Operation Zeus", player_team.store[0], enemy_team.store[0], "temple")
    $ battle_terrain = "mountain"
    $ battleground_bg = "background_desert"
    $_game_menu_screen = None
    $ config.skipping = False
    $ config.keymap['skip'].remove('K_LCTRL')
    $ config.keymap['skip'].remove('K_RCTRL')
    $ config.keymap['hide_windows'].remove('h')
    $ renpy.clear_keymap_cache()
    call screen battle_screen(bg=battleground_bg, disc="plate_deserturban", dec_1=["decoration_grecia_front1", 950, 0], dec_2=["decoration_grecia_back1", 3, 320]) with battleopening 
    $ renpy.block_rollback()
    
label bat000057_aftermath:
    scene black
    $ renpy.pause(1.0, hard=True)
    
    #Aftermath
    $ battle_count +=1
    $ battlestats_up()
    $_game_menu_screen = "save_screen"
    $ renpy.block_rollback()
    $ cp = max_cp
    $ cp += cp_levelset
    $ max_cp += max_cp_levelset
    
    #Unlocked Player Team Set
    if not skip_battle_selected:
        $ alliance_fighter_set += ("infantry_britannia_frogman_heer5", "infantry_britannia_admiral_heer5")
        $ load_data([
            "infantry_britannia_frogman_heer5",
            "infantry_britannia_admiral_heer5"
            ], "fighter")
        $ yamato_levels +=1
    $ persistent.skip_battle_sensitive = False
    $ skip_battle_selected = False
    
    #After Battle Continue
    $ _rollback = True
    $ store.text_history_enabled = True
    $ config.keymap['skip'].append('K_LCTRL')
    $ config.keymap['skip'].append('K_RCTRL')
    $ config.keymap['hide_windows'].append('h')
    $ renpy.clear_keymap_cache()
    
    jump bat000057_continue
    
###########################################################################
    #bat000057	-	Battle End
###########################################################################
label bat000057_continue:
    
    play soundfx "se/battle.ogg" fadein 3.0
    play soundfx2 "se/tank_invasion.ogg" fadein 3.0
    scene temple
    with pixellate
    play music "music/battle_desert.ogg"
    
    #Mission Marked Done
    $ log.markdone("bat000057")
    
    "The delaying action holds all day long, with the Ostralasians and other troops unleashing a maelstrom of fire."
    "The Germanians are pinned down, losing up to fifteen tanks and taking on many casualties."
    "For hours, they've lobbed grenades, fired from hidden nests and used rifles to take out enemy scouts."
    "But eventually, the order comes through to retreat and evacuate to the south, abandoning the pass."
    
    show vasey shock
    with dissolve
    
    vasey "Not another bloody retreat . . . come on, let's get out of Thermomalis and head for the beaches!"
    "Despite their best plans and efforts to hold on, the {i}Alliance{/i} forces simply can't continue the struggle."
    "Grecia is a lost battle . . . evacuation is their only hope now."
    
    show vasey determined
    with dissolve
    
    vasey "We did our bloody best, damn it! Now let's run before they start to pursue us!"
    
    play sound3 "se/dash.ogg"
    hide vasey
    with easeoutleft
    scene day2
    with dissolve
    show object_thermomalis at tankpos
    with dissolve
    
    "Thermomalis is abandoned. The fact that the Grecians weren't here to defend such an important historical site . . ."
    "Many Grecian army units had already capitulated prior to the battle. It will be extremely damaging to the national psyche."
    "{i}Panzys{/i} give chase to the Britannians, winding their way slowly through the passes and hills on steep roads."
    "News soon comes over from nearby Athenia that, despite some dogfights, little resistance has been met."
    
    hide object_thermomalis
    with dissolve
    
    "With Thermomalis lost and the enemy in a full-on assault southwards, the Battle for Grecia is coming to an end . . ."
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000239

#####################################################################################################################################################
#sc0000239	-	Jumbo and Wavell
#####################################################################################################################################################
label sc0000239:
    play soundfx "se/battle2.ogg" fadein 3.0
    scene desert_bunker
    with fade
    play music "music/evil.ogg"
    
    "{i}Alliance{/i} troops have been forced to retreat, having been overwhelmed by the Germanian onslaught."
    "Britannians, Ostralasians and other fighters of the western empire march over hill and plain, headed for the shore."
    "With the battle in Athenia coming to a close, Jumbo's {i}J-Force{/i} is leading the evacuation."
    
    show jumbo determined
    with dissolve
    
    jumbo "Pointless. How useless we've been! We didn't have nearly enough guns or men for this engagement."
    "The bulky soldier mutters to himself as lines of soldiers make their way southward through the trenches."
    jumbo "Wavell . . . if only you'd given us a little longer . . . maybe we could have turned it around."
    
    play silsound6 "se/silly11.ogg"
    show jumbo shock
    
    wavell determined "Hey, don't blame me!"
    jumbo "H-Huh? Wavell? What are you doing here?"
    
    play sound5 "se/walk.ogg"
    show jumbo shock at right3
    with ease
    show wavell determined at left3
    with dissolve
    
    "Sweating profusely, the commander of the {i}Britannian Desert Forces{/i}, Arabella Wavell, makes her way towards Jumbo."
    wavell "It's not my fault it's been such a disaster. Churchill's the one that wanted to fight this battle."
    
    show jumbo normal
    with dissolve
    
    jumbo "I thought you were meant to be in Gypta, containing the Vitalians?"
    wavell "All my resources were drained away and sent here, to Grecia. I can't fight without any of my tanks."
    wavell "Besides, Freyaborg the Salamander wants me to take away some of her more useless soldiers."
    jumbo "But . . . that doesn't mean you have to be here too."
    
    show wavell normal
    with dissolve
    
    wavell "I want to oversee an orderly retreat. I can't have you losing any of my supplies . . ."
    "As in Franzo, it seems likely that a lot of expensive materiel will simply have to be abandoned on the shoreline."
    "And at this rate, tens of thousands of {i}Alliance{/i} troops will be captured too. Wavell needs to put a dent in that figure."
    wavell "We must continue to cooperate with the Grecians, of course . . . but an early withdrawal is necessary."
    jumbo "Churchill won't be happy about this."
    
    play silsound3 "se/silly18.ogg"
    show wavell determined
    show jumbo shock
    
    wavell "Churchill can go suck on a lemon. We have bigger fish to fry."
    "Northward, the Germanians are liberating thousands of Vitalian soldiers from {i}POW{/i} camps, swelling their numbers."
    "With most defensive lines broken, the Britannians are escaping out to sea or to one of the many Grecian islands."
    "The campaign has been an unmitigated disaster. Now Wavell is in damage-control mode."
    
    show wavell normal
    with dissolve
    
    wavell "With all this distraction, it won't be long before we lose our foothold in the southern deserts."
    "Eager to get back to playing with her tanks in the sand, Wavell tries to hurry along Jumbo's retreat."
    "Once again, it seems like Hitora has Churchill's forces on the run . . ."
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000262

#####################################################################################################################################################
#sc0000262	-	Guderian sensei teaching students about tanks
#####################################################################################################################################################
label sc0000262:
    scene black
    with fade
    
    $ mouse_visible = False
    show expression Text(_("Meanwhile in Altberlin, outside a nearby barracks . . ."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx "se/airbase.ogg" fadein 3.0
    play soundfx2 "se/tank_far.ogg" fadein 3.0
    scene armycamp
    with fade
    play music "music/fun.ogg"
    
    "Far away from the frontlines, at one of Altberlin's many {i}Panzytruppenschule{/i}, lines of eager recruits wait patiently."
    "Today, it is their aim to join this mysterious world and its many designations . . ."
    "{i}Panzywaffe, Panzygrenadierdivisions, Panzydivisions, Panzyjäger-Abteilung, Artillerie-Regiments . . .{/i}" 
    "With the news of the {i}Desert Fox's{/i} triumphs in the field against Britannia, many inspired soldiers have signed up to join."
    "The {i}Panzydivisions{/i} are heaving with new drivers, engineers and troops."
    
    show guderian happy
    with dissolve
    
    "At the head of the line, an enthusiastic instructor greets her new cadets, beaming with pride."
    gud "Okay everyone! Guderian-sensei is going to teach you all about our latest {i}Panzyjäger{/i} tanks!"
    sol shock "Eh? What is she talking about? What's a {i}'sensei'{/i}?"
    "It seems Guderian has picked up a few habits from her former bunkmate . . ."
    
    show guderian at right15
    with ease
    show tank_panzerjager1 behind guderian at tacticalpos
    with dissolve
    
    gud "Before we move onto the newest prototypes, let's start with something easy!"
    "Standing back, Guderian comes near to a slim, open-top model and wraps a knuckle against the large gun."
    gud "This is the {i}47mm Panzyanklopfgerät 36 auf Panzykampfwagen I Ausf. B.{/i}"
    sol shock "That's a real tongue twister . . ."
    "For short, it's known as the {i}Panzyjäger I,{/i} the first of the tank hunters."
    
    show guderian normal
    with dissolve
    
    gud "After it became apparent that the {i}Panzy I{/i} was an ineffective tank, many chassis were left over."
    gud "Simply by removing the turret and adding an anti-tank gun, they were easily converted into tank hunters."
    "The {i}47mm Panzyanklopfgerät{/i}, a leftover from the invasion of Czexa, gives the {i}Panzyjäger I{/i} a deadly advantage in the field."
    "On top, a five-sided 14.5mm-thick shield offers the crew basic frontal protection, although it makes visibility poor."
    
    show guderian determined
    with dissolve
    
    gud "The early models saw service in the Battle of Franzo, knocking out hundreds of enemy tanks, virtually unopposed."
    gud "Since then, they've been an effective fighting force in Gypta, Serpana and Grecia."
    "Even in Afrikaa, the {i}Panzyjäger I{/i} managed to score hits against {i}Ducky II's,{/i} using a tungsten-core armor-piercing shell."
    
    show guderian normal
    
    sol determined "Teacher! What's the difference between a {i}Panzyjäger{/i} and a regular {i}Panzy?{/i}"
    
    show guderian happy
    with dissolve
    
    gud "I'm glad you asked, kid."
    
    play silsound5 "se/silly8.ogg"
    
    sol shock "Hey, I'm older than you . . ."
    
    show guderian determined
    with dissolve
    
    gud "Conventional {i}Panzy{/i} are designed to carry out all the main tasks associated with frontline armored combat."
    gud "These main battle tanks can be involved in numerous tactical operations, and employed against many different targets."
    "Guderian happily explains her thoughts on tanks and their roles in combat, as the class listen on, patiently."
    gud "A {i}tank hunter{/i} or {i}Panzyjäger{/i} is only designed to take on enemy tanks."
    "Resting a hand on the tread of the {i}Panzyjäger I{/i}, the teacher looks pensive as she continues her lecture."
    gud "Taking this consideration into mind, a {i}Panzyjäger{/i} is usually turretless, so it can accomodate a more powerful gun."
    gud "It also means production time is faster, they weigh less, and thicker armor can be incorporated."
    "The {i}Panzyjäger I{/i} - the original tank destroyer."
    
    hide tank_panzerjager1
    with dissolve
    show tank_marder behind guderian at tacticalpos
    show guderian happy
    with dissolve
    
    "Moving onto the new tank prototypes, Guderian beams proudly in front of the class."
    gud "Over here, we have the {i}Marten I{/i}, fresh out of Baukommando Becky's workshop."
    "The name {i}Marten{/i} roughly translates to {i}'weasel'.{/i}"
    gud "It's built on the base of an artillery tractor, hundreds of which fell into our possession following the fall of Franzo."
    gud "As the gun is somewhat big, the compartment superstructure has been removed to create space."
    "It runs at a top speed of 21mph, carrying 8.3 tons, including a {i}75mm Panzyanklopfgerät 40 L/46{/i} . . . phew."
    "The armor is relatively thin, with the shield only intended to protect the crew from pistol fire."
    
    show guderian normal
    with dissolve
    
    gud "Protection is kinda poor, but what else do you expect from an open-top tank?"
    "The {i}Marten I{/i} - the next stage of evolution of the tank destroyer."
    
    hide tank_marder
    with dissolve
    show tank_sturmgeschutz3 behind guderian at tacticalpos
    show guderian determined
    with dissolve
    
    gud "Aha! Now this is a unique tank!"
    "The low profile and sleek design on this next tank leaves a formidable impression on the young recruits."
    gud "The basic model is the {i}Gepanzy Selbstfahrlafette für Sturmi 75mm Kanone Ausführung A{/i} or {i}Sd.Kfz.142{/i}."
    gud "However, this prototype is more casually known as the {i}Sd.Kfz.142/1{/i}, due to the improved {i}StuK 40 L/48{/i} gun."
    "That's still not all that casual . . ."
    gud "It's also known as the {i}Sturmi III{/i}."
    sol normal "Huh . . . this is a {i}Panzyjäger?{/i} I thought it was an assault gun. It's even called a {i}Sturmi{/i} . . ."
    
    show guderian happy
    with dissolve
    
    gud "Wow. Top marks. I was hoping you'd spot it."
    sol shock "Eh? Spot what?"
    gud "The {i}Sturmi III{/i} is indeed an assault gun, intended as an infantry-support tank."
    sol normal "So, it's a trick question? It is an assault gun?"
    
    show guderian determined
    with dissolve
    
    gud "Yes. Usually forming a battalion within the artillery, this tank is often used against field fortifications and soft-skin targets."
    gud "But thanks to continuous modifications and production cost, it is often employed in the field as a {i}Panzyjäger{/i}."
    "It seems the {i}Sturmi{/i} has more than one role in combat."
    
    show guderian happy
    with dissolve
    
    gud "Think of it as a less versatile, more stealthy {i}Panzy III{/i}."
    sol normal "Man . . . I hate trick questions."
    
    hide tank_sturmgeschutz3
    with dissolve
    show guderian at center
    with ease
    
    gud "And finally, over here, we have the {i}88mm Panzyanklopfgerät 43 auf Fahrgestell Panzykampfwagen III/IV (Sf){/i}, known as the {i}Horniness{/i}."
    "What a naming convention . . . in comparison to the {i}Sturmi III{/i}, this model is a genuine {i}Panzyjäger{/i}."
    gud "I could tell you more about this one, but I think it's easier if I show you."
    
    play silsound4 "se/silly6.ogg"
    
    sol shock "How lazy! Stop shirking your teaching responsibilities!"
    "Banging her fist on the chassis of a {i}Horniness{/i}, the crew inside begin fumbling around and preparing the main gun."
    gud "Right! Let's hear this baby purr!"
    
    play sound2 "se/boom2.ogg"
    play sound3 "se/tank_fire.ogg"
    scene armycamp
    show guderian happy
    with hpunch
    with vpunch
    
    "Then, a mighty boom sounds as the cannon explodes in a furious fireball, launching a shell across the training grounds."
    gud "Yeehaw! Watch that kitty fly!"
    sol shock "What's with these mixed metaphors?"
    "The teacher enjoys watching over her students as they come to grips with the power of a {i}Panzyjäger{/i}."
    
    show guderian determined
    with dissolve
    
    gud "Okay everybody. It's time to get you all training. Find yourselves a partner and pair up."
    "One by one, the cadets group together, forming small operational crews."
    
    show guderian normal
    
    sol determined "Teacher! What's this strange, metal {i}'ball thing'{/i} over here?"
    
    show guderian shock at right15
    with ease
    show tank_kugelpanzer behind guderian at tacticalpos
    with dissolve
    play silsound6 "se/silly17.ogg"
    
    "A soldier points to a large spherical object, with a small stabilizer wheel jutting out of its rear."
    gud "Ahh this . . . damn, I thought I told them to put this thing away . . ."
    sol "What is it?"
    
    show guderian normal
    with dissolve
    
    gud "Well, since you've seen it, I'm going to let you recruits in on a special secret. This rolling ball is actually a tank!"
    sol shock "A tank? This thing?"
    "It looks more like a UFO than a tank. It's a Germanian {i}wunderwaffe{/i}."
    
    show guderian determined
    
    gud "This is the {i}Kugelpanzer{/i}, or {i}Rollzeug{/i}, a prototype light scout-vehicle."
    gud "With a small vision slit at the front, it's only capable of mounting a light machine gun in the port beneath."
    gud "The two wheel hemispheres on the side are powered by a single cylinder engine, allowing it to keep pace with infantry."
    "The {i}rolling ball{/i} design of the tank certainly is unique. A strange invention to come out of Germanian industry . . ."
    gud "This model is one of a defective batch. We're sending them to Zipangu to help with their war against Zhina."
    
    hide tank_kugelpanzer
    with dissolve
    show guderian determined at center
    with ease
    
    gud "Right! That's enough questions and tomfoolery. It's time we turned you punks into true {i}otanku{/i}."
    sol determined "Sir! Yes sir!"
    
    play silsound5 "se/silly16.ogg"
    show guderian shock
    
    gud "I'm not a {i}sir{/i} . . . never mind! Crews! Into your training vehicles! Now!"
    
    scene day3
    with dissolve
    
    "Will the {i}Panzytruppenschule{/i} be okay incorporating all these new recruits?"
    
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    stop music fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000373

#####################################################################################################################################################
#sc0000373	-	Antoness purges the coup
#####################################################################################################################################################
label sc0000373:
    scene black
    with fade
    
    $ mouse_visible = False
    show expression Text(_("Meanwhile, in the eastern nation of Rumanum . . ."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx "se/battle2.ogg" fadein 3.0
    play soundfx2 "se/battlecry2.ogg" fadein 3.0
    play soundfx3 "se/airsiren.ogg" volume 0.3 fadein 3.0
    scene day4
    with fade
    play music "music/yandere.ogg"
    
    "A rebellion has broken out in Rumanum, in a coup led by Cshima and the {i}Furry Guard{/i} . . ."
    "Disatisfied with Antoness's rule, the armed rebels have incited peasants to rise up and take down the state."
    "Taking over police stations and government buildings, the rioters open fire on the army and set up strongholds."
    "In a simultaneous widespread pogrom, synagogues are destroyed and innocents are murdered in a brutal fashion."
    "Riots in the towns and cities lead to the looting and destruction of thousands of businesses, shops and homes."
    
    play soundfx4 "se/battle3.ogg" fadein 3.0
    $ mouse_visible = False
    scene cg_antoness
    with dissolve4
    $ mouse_visible = True
    
    "With the army on side, and Hitora's backing, Antoness begins to crack down on Cshima's coup . . ."
    
    play silsound3 "se/silly12.ogg"
    
    anton insane "You dare to rise against me, Cshima? I'm the {i}Canineducator{/i} . . . Rumanum belongs to me!"
    "Uninterested in the pogroms, with her own evil machinations, the {i}Red Dog{/i} sends the army in after the rebels."
    "The strongholds quickly begin to collapse, and within a matter of hours the plotters are on the run."
    
    play silsound6 "se/silly17.ogg"
    
    anton "This is my country . . . mine, mine, mine! Its people are mine, its loot is mine, its terror is mine . . ."
    "Reestablishing control over the nation with an iron grip, the {i}National Legendary State{/i} is abolished."
    "In its place, Antoness forms a new nationalist state, with the {i}Furry Guard{/i} gone and herself as supreme dictator."
    anton "Mine, mine, mine . . . it's all mine and mine alone! I am the {i}Canineducator{/i} . . . I am Antoness!"
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    stop soundfx3 fadeout 3.0
    stop soundfx4 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000431

#####################################################################################################################################################
#sc0000431	-	The Axle discuss Kaptara
#####################################################################################################################################################
label sc0000431:
    play soundfx "se/tank_invasion.ogg" fadein 3.0
    play soundfx2 "se/battle2.ogg" fadein 3.0
    scene temple
    with fade
    play music "music/evil.ogg"
    
    "Following the early disasters of the campaign, the Germanian march into Athenia was a rousing success."
    "As the Grecian and Britannian armies retreated, they left behind a lot of supplies and ammunition for the taking."
    "Trucks filled to the brim with petroleum, oil, sugar, weapons, medical supplies and food rations."
    
    show cavallero determined at right35
    show germaniangeneraloberst determined at left35
    with dissolve
    
    "South of the capital city, Listte and Cavallero observe as the chase is on to cut off the enemy retreat."
    "Airborne assaults aim to take bridges and bring down convoys, as troops march through the foothills."
    cavallero "It won't be long before these Britannians are chased off completely . . ."
    listte "Well . . . maybe not just yet."
    cavallero "What do you mean?"
    listte "The enemy are retreating south and shoring up on the island of Kaptara."
    "Prior to Vitalia's first attempt at an invasion, the {i}Alliance{/i} garrisoned the place, turning it into a stronghold."
    "They've been using it as a naval safe haven, keeping tight control of the Medata Sea and frustrating the {i}Kriegssee{/i}."
    listte "The Füühbar is insisting we should begin preparations for an assault, immediately, to invade and attack."
    
    show cavallero normal
    with dissolve
    
    cavallero "Don't take this the wrong way, but I'm pretty sure {i}Il Douché{/i} is kinda done with this war already."
    listte "That girl . . . she's so ungrateful sometimes. After all we've done to win this battle for you." 
    cavallero "I might be able to twist her arm, and see if she'll send some torpedo boats or a landing force."
    listte "She should be leading the attack. Once again, leaving us to do the dirty work . . ."
    "Well, at least they're committing to something."
    
    play soundfx3 "se/bombers.ogg" fadein 3.0
    play soundfx4 "se/airbattle.ogg" fadein 3.0
    show cavallero determined
    show germaniangeneraloberst normal
    with dissolve
    
    "From above, they notice the sounds of heavy aircraft as the {i}Ruftwaffe{/i} pass overhead, making their way towards the coast."
    "The airborne raids are beginning. Kaptara will be bombarded from the air before an invasion is undertaken."
    "With all of mainland Grecia occupied, the final stages of this interlude are coming to a head . . ."
    
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    stop soundfx3 fadeout 3.0
    stop soundfx4 fadeout 3.0
    stop music fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000242

#####################################################################################################################################################
#sc0000242	-	Freyaborg in Kaptara
#####################################################################################################################################################
label sc0000242:
    play soundfx "se/sea.ogg" fadein 3.0
    scene beach_day
    with fade
    play music "music/teatime.ogg"
    
    "On the rocky shoreline of the island of Kaptara, a slimy creature slithers through the barracks of the defenders."
    "Hopping from rock to rock, a lizard-like soldier inspects the batteries and preparations that have been made." 
    
    play silsound5 "se/silly9.ogg"
    
    freyaborg "Excellent work troops . . . we'll stop those Germanians in their tracks. Then we can have all the flies we want."
    "This is Commander Freyaborg the Salamander, Britannia's last hope to hold out and secure a final victory in Grecia."
    "Churchill gave her command of this island as the {i}Alliance{/i} evacuated from the mainland."
    
    show object_kaptaradefenses at tankpos
    with dissolve
    
    "The scaly lizard is now responsible for maintaining the defenses and ensuring that Kaptara doesn't fall into enemy hands."
    "In her time here so far, she's mostly had to see to the evacuation of trouble-makers and nuisances to the local civilians."
    "Now the hour has come to prepare for the final battle."
    freyaborg "I can see it now. The Germanians will invade with a naval landing, attacking in their boats on the northern coast."
    freyaborg "There may be hundreds . . . no, thousands of landing craft. And tanks too . . . not much air support."
    freyaborg "Therefore, we will base our tactics around this eventuality. We must hold the beaches, no matter what."
    "Despite intelligence pointing to a sizable reliance on the {i}Ruftwaffe{/i}, hinting at an airborne invasion, Freyaborg holds true."
    "Her instinct suggests the {i}Axle{/i} will be invading by sea, and so is making every preparation to this end."
    
    hide object_kaptaradefenses
    with dissolve
    play silsound2 "se/poke.ogg"
    
    allied determined "What about the airfields inland? Shouldn't we be making preparations to defend them?"
    freyaborg "Meh . . . let's just worry about our coastal batteries."
    britanniangen determined "But Commander Freyaborg, intelligence messages suggest paratroopers are going to be sent."
    britanniangen "There's nothing in our intel to suggest a naval landing."
    freyaborg "Meh. Ignore any reports from Albion or HQ about paratroopers. Let's not fall for silly false ends like that."
    "Freyaborg the Salamander dismisses the claims, while flicking her tongue and catching a fly at the same time."
    freyaborg "These Germanians are so easy to read . . . this is going to be a piece of earthworm-infested cake."
    "The final assault is coming, and all that stands between Adorofia Hitora and the total capitulation of Grecia . . . is a salamander."
    "Well, whatever . . ."
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    #Map Data
    $ mapdata = ScreenData("geomap2", "map13", "easternmap")
    
    #Mission Data
    $ active_invasionbeacons_items.pop("bat000057", [bat000057_description, bat000057_title, bat000057_type, bat000057_x, bat000057_y])
    $ active_invasionbeacons_items.update({"bat000058": [bat000058_description, bat000058_title, bat000058_type, bat000058_x, bat000058_y]})
    
    #Mission Assign
    $ log.assign("[bat000058_title]")
    
    #Allegiances Data
    $ iraklion_siege = True
    $ iraklion_publicorder -=98
    $ active_maptown_items.update({"iraklion": [iraklion_name, iraklion_size, iraklion_governor, iraklion_governor_pic, iraklion_hostility, iraklion_alignment, iraklion_population, iraklion_publicorder, iraklion_influence, iraklion_command, iraklion_management, iraklion_farming_worth, iraklion_mining_worth, iraklion_industry_worth, iraklion_trade_worth, iraklion_entertainment_worth, iraklion_military_worth, iraklion_corruption_worth, iraklion_unlocktown, iraklion_martial, iraklion_siege, iraklion_company_img, iraklion_company_text, .645, .67]})
    
    #Go To Map
    jump map_begin
        
    
#####################################################################################################################################################
#bat000058	-	Operation Accordion: Battle of Kaptara
#####################################################################################################################################################
label bat000058:
    hide screen mapchoice1
    $ renpy.block_rollback()
    $ _rollback = True
    $ store.text_history_enabled = True
    window hide
    play sound6 "se/march2.ogg"
    stop music fadeout 2.0
    scene black
    with dissolve
    
    $ mouse_visible = False
    show expression Text(_("[bat000058_title]"), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    show expression Text(_("The island of Kaptara, Grecia"), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3        
    $ mouse_visible = True
    
    play soundfx "se/battle4.ogg" fadein 3.0
    play soundfx2 "se/sea.ogg" fadein 3.0
    play soundfx3 "se/bombers.ogg" fadein 3.0
    play soundfx4 "se/airbattle.ogg" fadein 3.0
    scene beachhead
    with fade
    play music "music/glory.ogg"
    
    "The invasion of Kaptara takes place in the late spring, and the Grecian island soon sees fierce conflict."
    
    show object_kaptara at tankpos
    with dissolve
    
    "{i}Tropfenschirmfänger{/i} paratroopers blot out the sun as they descend in droves out of transport planes."
    "As Germanian paratroopers land on the rocky shores of Kaptara, they immediately encounter opposition."
    "Though the {i}Aberwehr's{/i} intelligence suggested there would be few defenders on landing, this proves to be false."
    "The {i}Alliance{/i} are ready and waiting, using what little firepower they have to hold back the paratroopers."
    
    play silsound5 "se/poke.ogg"
    
    axis determined "Damn you, Kanari! Are you trying to make this a failed invasion or what?"
    "Well . . . actually . . ."
    "AA guns and tanks defend the dusty trenches and bunkers. Pillboxes line the surrounding hills and villages."
    "The main Germanian objectives are three airfields on the island, to be captured within the first day. But it seems impossible."
    "What's more, stores and troops to be landed from convoys have failed to materialize, chased off by Britannian cruisers."
    
    hide object_kaptara
    with dissolve
    
    freyaborg "Give them all you've got girls, don't let up! This island is all that stands between Hitora and victory!"
    "Freyaborg the Salamander desperately adjusts to the situation, caught off-guard by the sudden appearance of paratroopers."
    "{i}Ruftwaffe{/i} heavy bombers bombarded the beaches in the preceding days, wiping out bunkers and heavy artillery."
    "Continued air attacks will mean that daylight support from the {i}Britannian Royal Navy{/i} will soon come to an end."
    freyaborg "We have to hold them here. If the Germanians take this airfield, it's all over for us . . ."
    
    stop music fadeout 1.0
    stop soundfx fadeout 1.0
    stop soundfx2 fadeout 1.0
    stop soundfx3 fadeout 1.0
    stop soundfx4 fadeout 1.0
    scene black
    with pixellate
    
    jump bat000058_begin
    
label bat000058_begin:
###########################################################################
    #bat000058	-	Battle
###########################################################################
    
    #History Block
    $ renpy.block_rollback()
    $ store.text_history_enabled = False
    $ _rollback = False
    $ config.skipping = False
    
    #Enemy Team Set
    $ enemy_team = BaseTeam("Enemy", Solid("#000000", xysize=(50,50)), limit=50)
    $ enemy_team.add_fighter("enemy_germania_gunner_heer7")
    $ enemy_team.add_fighter("enemy_germania_antitank_heer7")
    $ enemy_team.add_fighter("enemy_panzer_stug4")
    
    #Playing For New Side Set - Alliance
    $ empty_data("fighter")
    $ load_data(alliance_fighter_set, "fighter")
    
    # Selection Screen Set
    $ player_team = BaseTeam("Player", Solid("#000000", xysize=(50,50)), limit=50)
    play battlemusic "music/map3.ogg"
    call screen non_battle_party_screen

    # Battle Set
    $ config.skipping = False
    $ yamato_lvlcheck()
    stop battlemusic fadeout 1.0
    scene black
    $ renpy.pause(1.0, hard=True)
    play battlesfx "se/battle4.ogg" volume 0.25
    play battlemusic "music/battle_land.ogg"
    $ renpy.block_rollback()
    $ fight_end = "bat000058_aftermath"
    $ game = Battleground("Battle Stage   |   Operation Accordion", player_team.store[0], enemy_team.store[0], "stalagmite")
    $ battle_terrain = "mountain"
    $ battleground_bg = "background_beach"
    $_game_menu_screen = None
    $ config.skipping = False
    $ config.keymap['skip'].remove('K_LCTRL')
    $ config.keymap['skip'].remove('K_RCTRL')
    $ config.keymap['hide_windows'].remove('h')
    $ renpy.clear_keymap_cache()
    call screen battle_screen(bg=battleground_bg, disc="plate_desert", dec_1=["decoration_none_front1", 950, 0], dec_2=["decoration_desert_back1", 3, 320]) with battleopening 
    $ renpy.block_rollback()
    
label bat000058_aftermath:
    scene black
    $ renpy.pause(1.0, hard=True)
    
    #Aftermath
    $ battle_count +=1
    $ battlestats_up()
    $_game_menu_screen = "save_screen"
    $ renpy.block_rollback()
    $ cp = max_cp
    $ cp += cp_levelset
    $ max_cp += max_cp_levelset
    
    #Unlocked Player Team Set
    if not skip_battle_selected:
        $ alliance_fighter_set.append("panzer_matilda2")
        $ load_data([
            "panzer_matilda2"
            ], "fighter")
        $ yamato_levels +=1
    $ persistent.skip_battle_sensitive = False
    $ skip_battle_selected = False
    
    #After Battle Continue
    $ _rollback = True
    $ store.text_history_enabled = True
    $ config.keymap['skip'].append('K_LCTRL')
    $ config.keymap['skip'].append('K_RCTRL')
    $ config.keymap['hide_windows'].append('h')
    $ renpy.clear_keymap_cache()
    
    jump bat000058_continue
    
###########################################################################
    #bat000058	-	Battle End
###########################################################################
label bat000058_continue:
    
    play soundfx "se/battle4.ogg" fadein 3.0
    play soundfx2 "se/sea.ogg" fadein 3.0
    play soundfx3 "se/bombers.ogg" fadein 3.0
    play soundfx4 "se/airbattle.ogg" fadein 3.0
    scene beachhead
    with pixellate
    play music "music/glory.ogg"
    
    #Mission Marked Done
    $ log.markdone("bat000058")
    $ active_invasionbeacons_items.pop("bat000058", [bat000058_description, bat000058_title, bat000058_type, bat000058_x, bat000058_y])
    
    "The bloody battle for Kaptara comes to a head . . ."
    "Reserve forces land under heavy fire on the airstrip itself, breaking out and meeting up with troops in nearby villages."
    "Pillboxes on nearby cliffs are engulfed in fire as Germanian explosives take out the heavy guns."
    "Sandbags collapse from nests on the hillsides and {i}Tropfenschirmfänger{/i} forces overwhelm the {i}Alliance{/i} trenches."
    freyaborg "It's no good . . . they've taken the airfields! We're going to have to evacuate the island . . ."
    
    play sound3 "se/dash.ogg"
    play sound5 "se/scamper.ogg"
    show object_kaptararetreat at tankpos
    with dissolve
    
    "Darting from rock to rock, the salamander leads her troops to the southern beaches, organizing a hasty retreat."
    "Grecian soldiers and partisans are left to fight alone as the Britannians abandon the island to its fate."
    "Once more, Hitora's Germania has invaded and claimed another nation for her evil empire. But it comes at a cost . . ."
    "Fatalities are high, with thousands of paratroopers lost in the heavy fire, and victory brought at a great price."
    "Kaptara, the last stand of the {i}Alliance{/i} in Grecia, has fallen . . ."
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    stop soundfx3 fadeout 3.0
    stop soundfx4 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000243

#####################################################################################################################################################
#sc0000243	-	Churchill bitter / losing
#####################################################################################################################################################
label sc0000243:
    play soundfx "se/sea.ogg" fadein 3.0
    scene sea1
    with fade
    play music "music/defeat.ogg"
    show churchill hat moe2 at left3
    show battenia normal at right3
    with dissolve
    
    "Out at sea, First Minister Churchill watches the battle as it unfolds on Kaptara's shoreline."
    batt "Well, that about does it . . ."
    
    play silsound5 "se/silly17.ogg"
    
    ch "That's not fair . . . it's not fair! Paratroopers?! Where did they get a crazy idea like that?"
    batt "Freyaborg the Salamander did the best she could under the circumstances . . ."
    "Once again, the Britannians are having to evacuate from a warzone, losing soldiers and supplies in the process."
    "They've shown themselves to be, yet again, incapable of taking on Adorofia Hitora's forces."
    "Now with Kaptara under their control, the Germanians can use the island for an attack on Kyprosa or into Gypta by sea."
    
    show churchill hat moe4
    show battenia angry
    with dissolve
    
    ch "This isn't over. I won't allow this to be over."
    batt "Don't do this to yourself. It'll be like Dunkirch all over again."
    ch "I'm tired of it. Evacuation after evacuation after evacuation. When are we going to fight a real war?!"
    batt "What are you talking about? This is a real war."
    
    play silsound6 "se/silly7.ogg"
    show churchill hat moe3
    show battenia shock
    
    ch "It's days like this, I wonder if the ordinary {i}tommy{/i} has it in him to beat the Germanians . . ."
    
    play silsound4 "se/silly20.ogg"
    show battenia angry
    
    batt "H-Hey! Churchill! That's going too far . . ."
    "Churchill breaks a taboo. In her frustration, she berates the common man and questions the Britannian spirit."
    
    show churchill hat sad
    show battenia normal
    with dissolve
    
    ch "I . . . I know. I'm sorry."
    "The girl's expression changes on that realization."
    batt "{i}Sigh{/i} . . . it was a brutal campaign. But we've lost this one, Churchill. Let it go and move onto the next one."
    "Churchill goes quiet, absorbing the words of her friend. She knows Battenia is right on this one."
    "They should apply a little starch and keep a stiff upper lip, under the circumstances."
    "Scratching the back of her head, the First Minister relents."
    ch "You're right. I'll . . . I'll talk to the soldiers before dinner tonight . . . keep their spirits up."
    "It's a small consolation. All Churchill really has in moments like these is her rhetoric."
    "And some stirring words might just be what the men and women need."
    
    show churchill hat normal
    with dissolve
    
    batt "Come along. We should go below deck. It's a long journey to Gypta from here."
    ch "You go ahead. I'll join you in a moment."
    
    play sound5 "se/metal_steps.ogg"
    hide battenia
    with dissolve
    show churchill hat normal at center
    with ease
    
    "Looking out over the rolling waves, Churchill pulls out a chocolate cigar and begins nibbling on the end of it."
    "It's at times like this, with the sea stretching out ahead of her, that the seafaring girl can relax."
    ch "It wasn't a complete disaster. Was it? No, we did a splendid job, considering everything . . ."
    "By Churchill's estimations, the Germanians may well have suffered over fifteen-thousand casualties, based on intercepts."
    "Also, the Grecian monarchy escaped, the Vitalians were humiliated and Hitora has spread herself thin."
    
    show churchill hat determined
    with dissolve
    
    ch "We played our part, as we promised we would. The Britannian bulldog will continue to fight on . . ."
    "The myth of Britannia's commitment to liberty and freedom continues to persist, having intervened once again."
    "It's not a very effective way to wage war, but it does firmly perpetuate the {i}Alliance{/i} cause."
    ch "Until Roosevelt makes up her mind about getting involved . . . I guess this is it."
    "With Franzo out of the picture, and smaller allies and neutral nations slowly turning, Britannia fights on alone."
    "The sole defender against Adorofia Hitora's tyranny; an empire bankrupting itself to save face."
    
    show churchill hat happy
    with dissolve
    
    ch "It was a hard-fought campaign. Hence we will not say that Grecians fight like heroes, but heroes fight like Grecians."
    ch "Or . . . something cool like that."
    "Now begins a long period of occupation. The enemy will continue to see resistance for a long time to come."
    "Peasants are rising up all across Grecia, fiercely fighting to hold onto their country."
    "Even in the recent battles on Kaptara, locals took to beating enemy soldiers with clubs and sniping from the hillside."
    ch "These people have a remarkable tenacity. May their various gods have mercy on them . . ."
    "In the villages and foothills throughout those ancient lands, in the temples and ruins, the flame of democracy burns on."
    "But for now, the Grecian people will be on their own. Britannia has bigger fish to fry . . ."
    
    show churchill hat normal
    with dissolve
    
    ch "Besides . . . there's always that Zipanguese prisoner . . ."
    "Pondering recent events, Churchill continues to chew on her chocolate cigar."
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    #Map Data
    $ mapdata = ScreenData("geomap2", "map14", "easternmap")
    
    jump sc0000430

#####################################################################################################################################################
#sc0000430	-	Warcrimes in Grecia and Krete
#####################################################################################################################################################
label sc0000430:
    play soundfx "se/birds.ogg" fadein 3.0
    play soundfx2 "se/battle2.ogg" fadein 3.0
    scene day5
    with fade
    play music "music/horror.ogg"
    play sound5 "se/battle/mp40.ogg"
    
    "In the days, weeks and months following the occupation of Grecia and Kaptara, warcrimes begin to mount."
    "Infrastructure and factories are destroyed, and civilians are starved to death in the cities and villages."
    "Former soldiers, once captured, are rounded up and executed in groups. Towns are burned to the ground."
    
    queue sound5 "se/battle/mp40.ogg"
    
    "In fits of cruelty, innocent men, women and children are thrown into open trenches and murdered by firing squads."
    "As resistance fighters across Grecia and her islands fight back, entire villages are massacred in retribution."
    "Many are put onto trains and sent north, to ghettos and camps . . ."
    "Grecia has fallen to the onslaught of Vitalia and Germania, and a puppet government is put in place."
    "Occupied and weakened, a bloody resistance will now begin to free the country from its new masters . . ."
    
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    stop music fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000456

#####################################################################################################################################################
#sc0000456	-	Radish Ali briefly taking over
#####################################################################################################################################################
label sc0000456:
    scene black
    with fade
    
    $ mouse_visible = False
    show expression Text(_("Elsewhere, in the capital city of Vaghdad in Iraji . . ."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx "se/battle3.ogg" fadein 3.0
    scene desert_town
    with fade
    play music "music/drama.ogg"
    
    "Civil war has come to Iraji. A slow motion {i}coup d'état{/i} takes place in the narrow lanes of Vaghdad."
    "With tensions having reached a peak between the Britannian military and the local population, it's finally happened."
    "Paramilitary forces storm the government palace as the disgruntled Iraji soldiers battle other Iraji soldiers."
    "Gunshots ring out across the capital city and armored vehicles pass through the tight alleyways."
    "Civilians run scared, trying to escape to safety while opposing forces battle it out in the streets."
    
    show desertman determined
    with dissolve
    
    "On this special day, hiding around a corner, in a dingy alleyway, a man watches the government palace cautiously."
    "This uprising is the work of a Germanian-funded group of former Iraji politicians and Generals."
    "{i}The Golden Parallelogram{/i}. A secret pro-{i}Axle{/i} organization run by a prior prime minister."
    "This revolutionary, by the name of Radish Ali, has bided his time, forming a small military junta, waiting patiently."
    rashidali "That's it boys . . . easy does it . . . easy . . ."
    "His troops position themselves, outside the government quarters, levelling their rifles and waiting for the enemy."
    "But the palace guards appear to have stood down. There is no real military presence here."
    rashidali "The Britannians aren't even here. All we're doing is murdering our brothers . . ."
    "Pro-{i}Axle{/i} forces fight pro-{i}Alliance{/i} soldiers, but only Iraji subjects are doing the battling."
    
    show desertman normal
    
    rashidali "{i}Sigh{/i} . . . Abdullah, you coward. Come out and face me."
    "Radish Ali kicks at the dirt, bored with the slow progress of their coup."
    revolutionary determined "Commander Radish Ali! Commander!"
    
    play sound5 "se/run.ogg"
    show desertman determined at left3
    with ease
    show desertaxis determined at right3
    with dissolve
    
    "One of the revolutionaries comes to the mob leader's side, having scouted the palace's south buildings."
    revolutionary "Commander, we've searched the offices of Regent Abdullah, but can't find him anywhere."
    rashidali "The fool must be hiding somewhere. Secure the roads out of the capital. We can't let him escape."
    "Unbeknownst to them, Regent Abdullah, who serves as protector for the underage monarch, has already fled the country."
    "After learning of the plot to arrest him in the early hours, he was whisked away to safety aboard a Britannian vessel."
    rashidali "Soon, the city will fall. Then we can start anew, with a patriotic government and control of our oilfields."
    
    show desertaxis shock
    
    revolutionary "Ah! Commander!"
    
    show desertman normal
    
    rashidali "What is it?"
    revolutionary "Look! Over there! The people . . . they're coming out."
    "One by one, civilians appear from out of their shops and homes, beginning to show courage as they walk the streets."
    "In one fell swoop, the old government has fallen and a new, anti-Britannian one has taken power."
    
    play soundfx2 "se/city.ogg" fadein 5.0
    show desertman shock
    with dissolve
    
    ow shock "Radish Ali? Did you do this?"
    wom shock "Eh? The former prime minister? He took control and threw out the corrupt old king?"
    
    show crowd behind desertman
    with dissolve
    
    "Coming forward, the civilians start to form a larger and larger crowd."
    "Radish Ali and his compatriots are surrounded by well-wishers, asking questions and praising the new regime."
    
    play soundfx3 "se/applause.ogg" fadein 5.0
    
    "Soon, the crowds begin to chant his name, praying for his success."
    ow happy "Thank you, Radish Ali, thank you. Praise be to God and the Prophet for bringing you to us."
    om determined "For so long, the Britannians abused their privileges, stealing from my business."
    wom determined "Finally, with you leading us, we Iraji citizens can be free from colonial oppression."
    "The people seem to accept the uprising of {i}The Golden Parallelogram{/i}, congratulating Radish Ali's success."
    
    show desertman determined
    with dissolve
    
    "Taking the words of the crowd to heart, the leader of the revolution is moved."
    rashidali "Then . . . I accept your wishes."
    
    play sound3 "se/walk.ogg"
    play soundfx4 "se/cheer.ogg" fadein 5.0
    show desertman determined at center
    show desertaxis normal at right15
    with ease
    
    "Stepping forward into the bright light of day, the man reveals himself fully, taking in the gazes of the crowd."
    "With his head held high, Radish Ali begins to speak with a great deal of soul and vigor."
    rashidali "This is a glorious day. A day of revolution. A day of justice. A day of new alliances and new government."
    rashidali "The king has fled, the Britannians are running scared . . . today, we take back Iraji for ourselves."
    "The people all stare on in astonishment and wonder, hanging on the swarthy man's every word."
    rashidali "From this day on, I hearby declare that I, Radish Ali, will rule as {i}Chief of the National Defense Government{/i}."
    
    play sound5 "se/battlecry2.ogg" fadein 3.0
    
    "The soldiers of the paramilitary begin to cheer heartily while the Iraji civilians applaud the new mob rule."
    "Iraji has been taken in a revolutionary {i}coup d'état{/i}. A huge blow to Britannia's stability in the region."
    "Is this the end of Britannian colonial rule in Iraji? And how will Churchill respond to this latest defeat?"
    "This diverse and far-reaching war in Europa is firmly becoming a world war . . ."
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    stop soundfx3 fadeout 3.0
    stop soundfx4 fadeout 3.0
    stop sound5 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc0000244

#####################################################################################################################################################
#sc0000244	-	Hitora discussing the aftermath
#####################################################################################################################################################
label sc0000244:
    play soundfx "se/room.ogg" fadein 3.0
    scene warroom_dark
    with fade
    play music "music/evil.ogg"
    
    "Following the Grecian campaign, the Füühbar paces around her study, as her inner circle discusses their victory."
    
    show dunitz bored at left25
    show goring pout at right25
    show joebbels sad at center 
    with dissolve
    
    gor "Well, after all the trouble that Mussorinni and Vitalia have caused, the conflicts they started are finally over."
    "Although, saying that, Zomali has fallen, Cyracana is only just under Rommel's control, and the E.V.A. is on the brink."
    goeb "D-Damn those Vitalians. Always causing trouble . . ."
    gor "They should spend less time invading countries and more time drinking wine."
    borkind determined "It worked out well for Franzo."
    "Borkind makes a dark joke."
    don "Well, they are our allies. Our pacts and our treaties have been honored, and the {i}Axle{/i} are stronger for it."
    "But the Füühbar doesn't agree. She quietly ruminates, barely containing her displeasure."
    
    show joebbels scared
    show goring determined
    show dunitz determined
    with dissolve
    
    hit hat angry "You know, I have ideas for this continent . . . unexpected campaigns like this, they're not good . . ."
    goeb "M-My Füühbar?"
    
    hide joebbels
    hide dunitz
    hide goring
    with dissolve
    play sound6 "se/walk.ogg"
    show hitora hat angry large
    with dissolve
    
    "The dictator turns to face them, her velvety scarlet eyes full of bitter disappointment and rage."
    hit "That fool. I wanted, above all, to ask Rinni to postpone the operation until a more favorable season . . ."
    borkind determined "Postpone? The invasion of Grecia?"
    hit "I wanted to ask her not to undertake any action without previously carrying out a {i}blitzkrieg{/i} operation on Kaptara too."
    hit "I intended to make practical suggestions regarding the employment of a parachute and an airborne division."
    "Both things the Germanians ended up having to do themselves, and to their detriment too."
    "The battle for Kaptara inflicted severe losses on the {i}Tropfenschirmfänger{/i}. Even though they celebrate, it was a pyrrhic victory."
    hit "Damn that Mussorinni . . . because of this nonsense, we've had to delay our plans for an invasion of the Union of Sovia."
    "Vital weeks have been spent battling in the mountains of the south, rather than preparing for her total war in the east."
    hit "And now she wants me to go to Athenia for a flag-raising ceremony. And I'm no closer to finding out where Yamato is . . ."
    don determined "You mean she still hasn't told you what happened to him?"
    hit "No . . . but I'm going to find out, one way or another."
    
    play sound3 "se/walk.ogg"
    hide hitora
    with dissolve
    
    "Heading for the door, the Füühbar strides away, full of anger, ready to confront her ally, {i}Il Douché{/i} . . ."
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    #History Block
    $ renpy.block_rollback()
    $ store.text_history_enabled = False
    $ _rollback = False
    
    #PERSISTENT CAMPAIGN UNLOCKED
    $ tito_campaign_completed = True
    $ achievement.grant("COMPLETE_DOUCHESTORY")
    $ achievement.sync()
    
    #CAMPAIGN CHOICE
    $ config.skipping = False
    play music "music/theme.ogg" fadein 3.0
    call screen campaign_selection() with fade 
    
    return
    
###############################################################################################################
