#####################################################################################################################################################
#####################################################################################################################################################
###### MEOW SIDE STORY #############################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################

label campaign_nyanquest:
    window hide
    stop music fadeout 1.0
    stop soundfx fadeout 1.0
    stop mmsound fadeout 1.0
    stop mmsound2 fadeout 1.0
    stop mmsound3 fadeout 1.0
    $ _window_during_transitions = False
    $_game_menu_screen = "save_screen"
    $ save_name = "The Rebel Catgirl"
    $ store.text_history_enabled = True
    $ codex_unlocked = False
    
    $ mouse_visible = False
    scene black
    with dissolve2
    pause 0.1
    play soundfx "se/wind.ogg" fadein 3.0
    
    show expression Text(_("East of Wukou, wartime capital of the Republic of Zhina, during the Great Eastern War . . ."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 3.0
    hide textoverlay with dissolve
    pause 0.3
    show expression Text(_("Following their invasion of northern Zhina, Zipanguese troops push south, taking cities."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 3.0
    hide textoverlay with dissolve
    pause 0.3
    show expression Text(_("Battles rage in the streets and hills, with warlords failing to fight against a common threat."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 3.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    me "1 . . . 2 . . . 3 . . ."
    
    $ mouse_visible = False
    show expression Text(_("Sergeant Yamato Yamamoto, a hero of Shenzhenga, battles his way westwards towards the city."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 3.0
    hide textoverlay with dissolve
    pause 0.3
    show expression Text(_("The Zhinese defenders bravely fight to hold onto the surrounding regions . . ."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 3.0
    hide textoverlay with dissolve
    pause 0.3
    show expression Text(_("Soldiers fight only for themselves. For the honor it will bring to those they protect."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 3.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    me " . . . 4 . . . 5 . . . that should do it . . ."
    "Having cooked the grenade, I throw it over the wall . . ."
    
    play soundfx "se/battle4.ogg"
    play sound3 "se/boom.ogg"
    play sound4 "se/boom2.ogg"
    play sound5 "se/grenade.ogg"
    scene city4
    show smoke
    with hpunch
    with vpunch
    play music "music/glory.ogg"
    
    "I hear an instant bang and feel myself shaking, causing my legs to buckle beneath me."
    "The section of wall beside me seems to move as a layer of dust wafts from out of the brickwork."
    me ". . . ?"
    "Smog permeates the area and dirty clouds of dust coat everything in grey."
    "Adjusting my crouch, I grip my rifle tightly and wait. But there's no scream nor sound of footsteps."
    me "I misjudged . . ."
    "The late afternoon sky blows in a cool autumn wind."
    
    show object_dianxia at tankpos
    with dissolve
    
    "We're fighting in a fort town named Dianxia, on the north shore of the Kiam River in central Zhina."
    me "It's one of the last places the Zipanguese army needs to hold before the march on Wukou can begin."
    "Like every town we've taken before it, the defenders put up a fierce resistance, refusing to give way."
    "Armored cars fire on the crumbling buildings as eagle-eyed snipers wait for their moment."
    "Smoke billows in from nearby craters as the enemy forces push closer."
    "Nearby, my companions strive to maintain our position at the end of this road."
    
    hide object_dianxia
    with dissolve
    
    "Having dug myself in alongside this wall, I thought I heard enemy soldiers talking on the other side."
    "If they'd managed to bunker themselves in the surrounding buildings, we would quickly be encircled."
    me "Must have been my imagination . . ."
    "There's the sound of constant gunfire as flames lap around destroyed vehicles."
    
    play sound5 "se/run.ogg"
    show oriasiangeneral determined behind smoke
    with dissolve
    
    lef "Sergeant Yamamoto, what are you wasting your grenades for?!"
    "The lieutenant shouts to me. We've been under her wing since the naval landings earlier in the summer."
    lef "The enemy are in that direction, so dig in and fire your damn weapon . . ."
    
    play sound4 "se/run.ogg"
    hide oriasiangeneral
    with dissolve
    
    "She chides me before rallying other soldiers around her. The enemy continue to advance on our position."
    
    show speedlines with circleirisout
    
    me "Well, here goes nothing . . ."
    
    stop soundfx fadeout 1.0
    stop music fadeout 1.0
    scene black
    with pixellate
    
    jump bat0000100_begin
    
label bat0000100_begin:
###########################################################################
    #bat0000100	-	Nyan Mission: Bottleneck Battle
###########################################################################
    
    #Nyan Quest CP Reset
    $ cp = 350
    $ max_cp = 350
    
    #History Block
    $ renpy.block_rollback()
    $ store.text_history_enabled = False
    $ _rollback = False
    $ config.skipping = False
    $ q_title = "Operation Duck Stew: Battle of Dianxia"
    
    #Load Skills and Fighter Data
    $ load_data(skills_set, "skill")
    $ load_data(enemy_fighter_set, "fighter")
    
    #Enemy Team Set
    $ enemy_team = BaseTeam("Enemy", Solid("#000000", xysize=(50,50)), limit=50)
    $ enemy_team.add_fighter("enemy_zhina_gunner_heer1")
    $ enemy_team.add_fighter("enemy_zhina_marksman_heer1")
    $ enemy_team.add_fighter("enemy_zhina_gunner_heer1")
    
    #Locked Selector
    $ nyanbattles_selection = False
    $ airsupport_section_unlocked = False
    $ infantry_section_unlocked = False
    $ panzer_section_unlocked = False
    $ antitank_section_unlocked = False
    $ commander_section_unlocked = True
    $ specialgroup_section_unlocked = True
    
    #Player Team Set
    $ load_data([
        "commander_yamato_heer0",
        "specialgroup_zipangu_gunner_heer1",
        "specialgroup_zipangu_marksman_heer1"
        ], "fighter")
    $ yamatoforce_enabled = False
    
    # Selection Screen Set
    $ player_team = BaseTeam("Player", Solid("#000000", xysize=(50,50)), limit=50)
    play battlemusic "music/map3.ogg"
    call screen non_battle_party_screen

    # Battle Set
    $ config.skipping = False
    stop battlemusic fadeout 1.0
    scene black
    $ renpy.pause(1.0, hard=True)
    play battlesfx "se/battle4.ogg" volume 0.25
    play battlemusic "music/battle_snow.ogg"
    $ renpy.block_rollback()
    $ fight_end = "bat0000100_aftermath"
    $ game = Battleground("Battle Stage   |   Bottleneck Battle", player_team.store[0], enemy_team.store[0], "woodenbench")
    $ battle_terrain = "urban"
    $ battleground_bg = "background_urban"
    $_game_menu_screen = None
    $ config.skipping = False
    $ config.keymap['skip'].remove('K_LCTRL')
    $ config.keymap['skip'].remove('K_RCTRL')
    $ config.keymap['hide_windows'].remove('h')
    $ renpy.clear_keymap_cache()
    call screen battle_screen(bg=battleground_bg, disc="plate_dirt", dec_1=["decoration_ship_front1", 950, 0], dec_2=["decoration_rubble_back1", 3, 320]) with battleopening
    $ renpy.block_rollback()
    
label bat0000100_aftermath:
    scene black
    $ renpy.pause(1.0, hard=True)
    
    #Aftermath
    $ persistent.skip_battle_sensitive = False
    $ skip_battle_selected = False
    $ battle_count +=1
    $_game_menu_screen = "save_screen"
    $ renpy.block_rollback()
    $ cp = max_cp
    $ cp += 30
    $ max_cp += 30
    
    #Unlocked Player Team Set
    if not skip_battle_selected:
        $ load_data([
            "panzer_braatovervalwagen"
            ], "fighter")
    $ persistent.skip_battle_sensitive = False
    $ skip_battle_selected = False
    
    #After Battle Continue
    $ _rollback = True
    $ store.text_history_enabled = True
    $ config.keymap['skip'].append('K_LCTRL')
    $ config.keymap['skip'].append('K_RCTRL')
    $ config.keymap['hide_windows'].append('h')
    $ renpy.clear_keymap_cache()
    
    jump bat0000100_continue
    
###########################################################################
    #bat0000100	-	Battle End
###########################################################################
label bat0000100_continue:
    
    play soundfx "se/battle4.ogg" fadein 3.0
    scene city4
    with pixellate
    play music "music/evil.ogg"
    
    "Soon enough, the fort town of Dianxia falls to our onslaught, as the enemy retreat or surrender."
    "The Zipanguese soldiers are battle-hardened, and we have greater firepower on our side."
    
    show oriasiangeneral determined
    with dissolve
    
    lef "Not bad, Sergeant Yamamoto. Keep this up and one day you might make Warrant Officer."
    me "I don't know about that . . ."
    "I've been fortunate to make it this far. And it's not as though the army rank system is exactly flexible . . ."
    "The lieutenant watches as the Zhinese forces retreat. Our troops steadily give chase, maintaining the bottleneck as they do."
    "The main guns continue to mow down the retreating front lines. Casualties are high, and bodies are strewn around the town."
    "Rubbing the back of my neck, I look across at the dimly setting sun."
    lef "Come on, let's fortify our position and find somewhere to camp for the night."
    "The skirmish is over. Slowly, the platoon marches on to scout around the immediate area."
    
    stop soundfx fadeout 3.0
    stop music fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    play soundfx3 "se/battle2.ogg" fadein 3.0
    play soundfx2 "se/fire3.ogg" fadein 3.0
    scene city4_night
    show spark
    with fade
    
    "That night, we camp in the captured fort town, sleeping amongst the rubble in open foxholes."
    me "It's one of the few areas in the city that hasn't been completely shelled into the ground."
    "Sparks kick up from the makeshift firepit, as other soldiers get some rest. Unable to sleep, I stay on watch most nights."
    me "There are always fears that {i}Meowists{/i} will infiltrate the lines and attack you in your sleep."
    "Other squads and platoons set fires nearby, causing shadows to flicker in the streets."
    "Some dark spots are probably soldiers, moving into position or carrying out raids, stealing from the locals."
    "Staring at the darkness for long enough, you begin to lose sight of what's real and what's not."
    me "It's strange to think of what this place used to look like, before the shelling . . ."
    "The brutality of the campaign was stepped up after Pinxin Pass. It was already pretty brutal before then."
    "This isn't a noble war . . . it's a bloody and destructive affair. The bloodshed, the brutal treatment of civilians . . ."
    me ". . . it won't be long until we reach Wukou . . ."
    
    play sound2 "se/walk.ogg"
    show oriasiangeneral normal behind spark
    with dissolve
    
    "The lieutenant approaches out of the darkness and comes up to me."
    lef "Sergeant Yamamoto, you're still up?"
    me "I'm on watch."
    lef "Anything to report?"
    me "Nothing out of the ordinary."
    "We both look on as the other soldiers snore loudly in their sleep. They really must be exhausted."
    
    show oriasiangeneral determined
    with dissolve
    play music "music/evil.ogg"
    
    lef "Good to hear. I wanted to speak with you alone . . ."
    me "Alone, ma'am?"
    lef "Yes, we've been given a special assignment. I need this to remain strictly confidential, between us."
    "A confidential mission?"
    me "What is it?"
    lef "Tell me, what do you know of the enemy army? Who are we fighting right now?"
    me "Who? Well, it's the Zhinese right?"
    lef "The Zhinese are many, split up into different factions with competing interests. Warlords, xommunists, nationalists . . ."
    lef "We're currently battling to destroy the main army of the {i}Kittentang (KTT){/i}, and their temporary capital in Wukou . . ."
    "The {i}Kittentang{/i} . . . the main faction, in control of the Republic of Zhina, or what's left of it."
    me "That's right. And the leader of the {i}Kittentang{/i} is a girl named . . . Nyan Katshex?"
    lef "So you do know. Generalissima Katshex and the {i}KTT{/i} made an alliance with the {i}Meowists{/i} last year."
    "The {i}Meowists{/i} . . . they're the xommunist army, led by a rebel commander named Meow . . ."
    lef "Thanks to this coordination, ambushes like Pinxin Pass are becoming more common. The north is under constant attack now."
    me "What does this have to do with this special assignment?"
    
    show oriasiangeneral normal
    with dissolve
    play silsound6 "se/silly20.ogg"
    
    lef "We need to break up their alliance and cut the head off the snake. The quickest way is to take out Nyan Katshex."
    me "T-Take them out? You mean an assassination?"
    
    play silsound3 "se/silly12.ogg"
    
    lef "Precisely. Nyan Katshex is still in Wukou, commanding the garrison . . . we need you to assassinate her, Yamato."
    me "Eh? Me? Wait a minute . . . you said {i}'assassinate'?{/i}"
    lef "Word of your marksmanship has reached high command. They want the hero of Shenzhenga to take on this mission."
    "She can't be serious. I'm a good shot, but an assassin? I'm not so sure I'm cut out for something like that."
    me "I don't think I can take on this assignment . . ."
    
    show oriasiangeneral determined
    play silsound5 "se/silly5.ogg"
    
    lef "I've already told them that you'll accept. We'll have you sent into Wukou ahead of the rest of the invasion force . . ."
    me "I don't have any say in this?"
    lef "No. Once you've infiltrated the city and you're behind enemy lines, the rest will be up to you."
    "I look around at some of the others. A snoozing soldier drools all over his {i}Nariakira{/i} rifle, the spittle dripping into the chamber."
    "Another careless man hugs a frag grenade close to his chest as he dozes, blissfully unaware."
    me "Well, I guess I am the most reliable marksman around here . . ."
    "I suppose I have no choice . . ."
    me ". . . it would be an honor, ma'am."
    "An assassin . . . I'm going to have to take aim at this Nyan Katshex and eliminate them . . ."
    
    show oriasiangeneral normal
    with dissolve
    
    lef "You're a good soldier, Sergeant Yamamoto. I wish I had a dozen more like you."
    me "Thank you, ma'am."
    lef "In the morning, you'll select some soldiers to go with you. Try to get some rest before then . . ."
    
    play sound2 "se/walk.ogg"
    hide oriasiangeneral
    with dissolve
    stop music fadeout 5.0
    
    "I bow to the lieutenant, who takes off, probably to check on the wounded soldiers in a nearby trench."
    "From across the rooftops, I spy some more flickering shadows in the darkness."
    
    play music "music/drama.ogg"
    play sound2 "se/cock.ogg"
    
    "Cocking my bolt-action rifle, I focus down the sights and see the green of the enemy's uniform."
    "Zhinese soldiers move into position in the building opposite, possibly carrying mortars with them."
    me "Oh no you don't . . ."
    "I mutter to myself as I take aim at their captain. Waiting for the right moment, I rest my finger on the trigger . . ."
    
    play sound3 "se/battle/kar98k.ogg"
    scene city4_night
    show spark
    with flash
    
    "Without another second's hesitation, I fire on the enemy soldiers that hide under the cover of night."
    "One of them slumps into the dusty concrete, dropping the grenade launcher with a clatter."
    
    play sound2 "se/gundrop.ogg"
    
    "The weapon drops off the rooftop and lands in the muddy street below, where other Zipanguese soldiers are taken by surprise."
    
    play silsound3 "se/poke.ogg"
    
    sol shock "What the-"
    
    play sound4 "se/battle/mg34.ogg"
    play sound6 "se/rifle.ogg"
    
    "Other Zipanguese forces take notice and start to fire on the building. I watch as other enemy soldiers begin to scatter."
    
    play sound2 "se/cock.ogg"
    
    "Quickly reloading, I take aim again . . ."
    
    play sound3 "se/battle/kar98k.ogg"
    
    "I fire and another enemy falls to the dirt as the rest escape into the night."
    "It goes quiet. Sitting back, I rest my rifle against my shoulder and breathe."
    me ". . . . . . . . ."
    
    stop soundfx2 fadeout 3.0
    stop soundfx3 fadeout 3.0
    stop music fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    scene black
    with fade
    
    $ mouse_visible = False
    show expression Text(_("Meanwhile, at the Kittentang base in Wukou . . ."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx "se/rain.ogg" fadein 3.0
    play soundfx5 "se/battlecry2.ogg" fadein 3.0
    scene zhina_temple_night
    show heavyrain
    with fade
    play music "music/horror.ogg"
    
    "At a grand temple in the center of Wukou, the Zhinese enemy make their encampment as it begins to rain."
    
    show object_ktttroops at tankpos
    with dissolve
    
    "Elite specially-trained {i}KTT{/i} troops gather in the courtyard, dressed in their best uniforms."
    "As the waterdrops patter against the brickwork, the soldiers stand out from under their tents and canopies."
    "Tonight, they are going to hear from their leader; the one who will lead them to victory."
    
    hide object_ktttroops
    with dissolve
    play sound5 "se/walk.ogg"
    
    "The people murmur as a short girl makes her way through the crowd."
    
    play silsound3 "se/poke.ogg"
    
    zhinasol shock "It's our dear leader, the Red Generalissima, Nyan Katshex . . . she's going to rally the troops!"
    
    $ mouse_visible = False
    scene cg_nyan
    show heavyrain
    with dissolve2
    $ mouse_visible = True
    play silsound6 "se/silly17.ogg"
    
    "Nyan Katshex, leader of the {i}Kittentang (KTT){/i} faction of the Zhinese armed forces, arrives on the scene."
    "Letting a cat-ear hoody slope over her slender shoulders, the girl clears her throat and speaks."
    nyan determined "Sisters. Soldiers. Peasants. Countrymen. The Republic of Zhina needs your help!"
    
    play silsound4 "se/silly20.ogg"
    
    nyan "Our country is under attack by foreign barbarians. All of Zhina rallies to our banners . . . even the dirty xommies."
    "Everyone gathers under the stormy clouds, bearing the rain, if only to hear the girl's words."
    nyan "These Zipanguese fighters are cultureless, self-proclaimed imperialists from the east."
    nyan "If imperialism is not banished, Zhina will perish as a nation. If we do not perish, then imperialism cannot remain . . ."
    zhinasol happy "Such wise words! Inspiring!"
    "The soldiers around her nod approvingly at that prophetic statement."
    nyan "The {i}Meowists{/i} are resisting across the countryside, and fighting to free the cities in the north . . ."
    nyan "Warlords put aside their differences to defeat the common enemy . . . at least, some of them are . . ."
    nyan "Most of Zhina unites behind our cause! It is our duty to defend our nation and hold Wukou against the invaders!"
    
    play sound3 "se/sneeze.ogg"
    scene cg_nyan_focus
    show heavyrain
    with hpunch
    play silsound5 "se/silly1.ogg"
    
    nyan sad "Aaaaaachoooooo!"
    "Nyan Katshex lets out a big sneeze and her eyes get a little teary."
    nyan ". . . we will stop these Zipanguese soldiers in their tracks . . . {i}sniffle{/i} . . ."
    "Their leader wavers a little, obviously tired and cold from the rain."
    sol shock "Please Generalissima, it's way past your bedtime! Take a nap, for the sake of your people!"
    
    play silsound2 "se/silly2.ogg"
    
    nyan angry "No . . . I'm fine. I'm in good health. I eat soup made of white doves and it's a wonderful tonic."
    sol determined "Generalissima . . ."
    nyan determined "We have to face the facts. The city will be encircled and surrounded in a few days time . . ."
    nyan "Our air force and our navy have been wiped out by the Zipanguese onslaught. Only the army remains."
    "It is a dark situation. The thought of Zipangu controlling yet another major city is a chilling one for the Zhinese forces."
    nyan "We have little choice. The army will have to retreat westwards towards the mountains . . ."
    nyan "Until we can evacuate the city, the garrison here will have to fight on and buy us some more time."
    
    play silsound4 "se/silly11.ogg"
    
    nyan "I will stay for as long as I can . . . if the worst comes to it, we will set the city ablaze and leave the enemy nothing!"
    zhinasol determined "Then, until that time comes, we must protect the city, for the Generalissima's sake!"
    
    play silsound4 "se/silly19.ogg"
    
    nyan moe1 "Eh? For me?"
    sol determined "If the Generalissima says we must defend the city, then we will defend it to the death!"
    
    play silsound5 "se/silly9.ogg"
    
    nyan moe2 "You guys . . ."
    "The girl is taken back by the sentiment of her soldiers."
    sol happy "Three cheers for the Generalissima! Hooray! Hooray! Hooray!"
    
    play soundfx6 "se/battlecry.ogg" fadein 3.0
    
    "Everybody begins to rally, crying out words of support for their dear leader. They will fight on to the end."
    zhinasol determined "You can do it Generalissima! We love you!"
    zhinawom determined "The people love you, Generalissima. We fight for you. Fight for all of us!"
    "Nyan Katshex then breaks out into a big smile."
    nyan happy "I won't let you down. I will carry everyone's hopes in my heart, as we plunge into battle . . ."
    sol happy "We believe in you, Generalissima!"
    nyan smirk "The final outcome of a war is often determined by the degree of initiative shown on each side."
    nyan "We become what we do . . . Zhina not only fights for her own independence, but for the liberation of every nation."
    nyan "Remember these things and together we'll break the Zipanguese army here in this city!"
    "With flair and determination, Nyan does a call-and-response with her loyal followers."
    
    show speedlines with circleirisout
    
    nyan "{i}Wǒmen néng zuò dào! Wǒmen zǒu ba! Wǒmen zǒu ba!{/i}"
    crowd "{i}Wǒmen néng zuò dào! Wǒmen zǒu ba! Wǒmen zǒu ba!{/i}"
    "Slowly, the rain begins to let up as the heavens part. Through the wisps of silver cloud, the moon begins to shine."
    "Here, in Wukou, the {i}Kittentang{/i} will make a stand . . ."
    
    stop sound2 fadeout 2.0
    stop soundfx fadeout 3.0
    stop soundfx5 fadeout 3.0
    stop soundfx6 fadeout 3.0
    stop music fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    scene black
    with fade
    
    $ mouse_visible = False
    show expression Text(_("Later that week . . ."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx2 "se/fire3.ogg" fadein 3.0
    play soundfx3 "se/wind.ogg" fadein 3.0
    play soundfx4 "se/walk.ogg" fadein 3.0
    play soundfx5 "se/metal_steps.ogg" fadein 3.0
    play soundfx6 "se/march3.ogg" fadein 3.0
    scene day1
    show spark
    with fade
    play music "music/evil.ogg"
    
    "Several days later, we reach the city gates of Wukou ahead of the rest of the invasion force . . ."
    
    show object_zhinarubble at tankpos
    with dissolve
    
    "Smoldering craters cover the streets from shelling attacks, as charred buildings collapse into rubble."
    "Furniture and possessions are left sprawled on the sidewalks, abandoned by their fleeing owners."
    
    play silsound3 "se/poke.ogg"
    
    tak_un shock "It's like a g-g-ghost town . . . Boss-man, what are we doing here by ourselves?"
    "My hand-picked squad of privates and other soldiers nervously follows behind me, uncertain of our mission."
    
    hide object_zhinarubble
    with dissolve
    
    me "We've been handed a special assignment. All we need to do is reach the city garrison and find their commander."
    "I choose to keep the particular details brief for the moment."
    tak_un "That's it?"
    me "That's all we have to do. Keep your eyes peeled. We're on our own here . . ."
    
    stop soundfx4 fadeout 2.0
    stop soundfx5 fadeout 2.0
    stop soundfx6 fadeout 2.0
    scene city1
    show spark
    with dissolve
    
    "We trek our way through the desolate streets and arrive at a clearing."
    zipangusolwom determined "Quiet . . . they obviously evacuated the city ahead of the encirclement."
    "The squad takes a knee beside a burntout automobile."
    
    play sound5 "se/brush.ogg"
    
    "Holding a pair of binoculars, I quietly survey the area. Ahead down the road, in the distance, I find what I'm looking for."
    me "At the end of this road, beyond that open courtyard, is a guarded bridge . . . five, maybe ten soldiers . . ."
    tak_un determined "A bridge?"
    me "It's a vital target. We need to cross it and make our way westwards, towards a temple converted into barracks."
    "As far as we know, that temple is where Nyan Katshex is holed up with her army."
    
    stop music fadeout 3.0
    
    me "If we approach quietly from this side, work our way through this series of buildings . . . we might just ambush them . . ."
    
    play soundfx2 "se/battle.ogg"
    scene city1
    show spark
    with hpunch
    play music "music/glory.ogg"
    
    "To my right, a soldier is flung backwards as they're hit by gunfire from the office building opposite."
    "Suddenly an attack is unleashed upon us."
    me "A-Ambush!?! Get down! Get to cover!"
    
    play sound4 "se/break.ogg"
    play sound6 "se/collapse.ogg"
    scene city1
    show spark
    with vpunch
    
    "We all hit the deck and try to find shelter behind the destroyed vehicles and broken roadblocks."
    "Enemy forces from the bridge ahead take notice, with some headed towards our position as others retreat away."
    tak_un shock "Another surprise attack! It must be the {i}Meowists{/i} again . . . just like at Pinxin Pass!"
    me "Don't talk nonsense, there aren't any {i}Meowists{/i} here. They're all up north . . ."
    "One young soldier shouts for reinforcements, but we know they won't be coming. We're behind enemy lines here."
    "The gunfire is relentless. We're totally pinned down. At this rate, we might have to fall back."
    zipangusolwom determined "They've got two nests guarding those double doors . . ."
    
    show object_wukou at tankpos
    with dissolve
    
    "Looking out from our hiding spot, I watch as enemy soldiers wheel out heavy machine guns."
    
    play silsound5 "se/silly3.ogg"
    
    sol shock "Are those Hotkiss's?!"
    me "Type 92's . . . they're using our guns . . ."
    
    play soundfx4 "se/battle/m1918bar.ogg"
    
    "The Zhinese troops get their heavy guns working and start firing relentlessly on our position."
    
    play sound2 "se/automatic.ogg"
    
    "Bullets ricochet off of the automobile we're leaning against. One wrong move and they'll blow my head off."
    
    hide object_wukou
    with dissolve
    play sound2 "se/brush.ogg"
    
    "Cautiously moving around, I manage to see down the road to the bridge, which is now lightly-manned . . ."
    me "If we can find a way to take out these guns, we can slip through and make for the bridge . . ."
    tak_un "B-Boss-man, what should we do?!"
    "Looking around at the rubble and the destroyed automobiles, I feel at a loss. We're really trapped here."
    
    play silsound2 "se/poke.ogg"
    
    me "Wait a minute . . . what's that?"
    "Amongst the burning wreckages is some kind of Batavian armored-car, a large machine gun poking out of the back."
    
    show speedlines with circleirisout
    
    me "You two there, quickly, climb aboard that vehicle and make use of the gun! The rest of you, we're going to break out!"
    
    play sound5 "se/cock.ogg"
    
    "Reloading my rifle, I rally the others around me as we take on the heavy guns of the enemy . . ."
    
    stop soundfx2 fadeout 1.0
    stop soundfx3 fadeout 1.0
    stop soundfx4 fadeout 1.0
    stop music fadeout 1.0
    scene black
    with pixellate
    
    jump bat0000101_begin
    
label bat0000101_begin:
###########################################################################
    #bat0000101	-	Nyan Mission: Downtown Battle
###########################################################################
    
    #History Block
    $ renpy.block_rollback()
    $ store.text_history_enabled = False
    $ _rollback = False
    $ config.skipping = False
    $ q_title = "Operation Breakout: Battle of Wukou"
    
    #Enemy Team Set
    $ enemy_team = BaseTeam("Enemy", Solid("#000000", xysize=(50,50)), limit=50)
    $ enemy_team.add_fighter("enemy_panzer_ba10zhina")
    $ enemy_team.add_fighter("enemy_zhina_gunner_heer1")
    $ enemy_team.add_fighter("enemy_zhina_marksman_heer1")
    
    #Locked Selector
    $ panzer_section_unlocked = True
    
    # Selection Screen Set
    $ player_team = BaseTeam("Player", Solid("#000000", xysize=(50,50)), limit=50)
    play battlemusic "music/map3.ogg"
    call screen non_battle_party_screen

    # Battle Set
    $ config.skipping = False
    stop battlemusic fadeout 1.0
    scene black
    $ renpy.pause(1.0, hard=True)
    play battlesfx "se/battle4.ogg" volume 0.25
    play battlemusic "music/battle_land.ogg"
    $ renpy.block_rollback()
    $ fight_end = "bat0000101_aftermath"
    $ game = Battleground("Battle Stage   |   Downtown Battle", player_team.store[0], enemy_team.store[0], "zhinahouse")
    $ battle_terrain = "urban"
    $ battleground_bg = "background_churchill"
    $_game_menu_screen = None
    $ config.skipping = False
    $ config.keymap['skip'].remove('K_LCTRL')
    $ config.keymap['skip'].remove('K_RCTRL')
    $ config.keymap['hide_windows'].remove('h')
    $ renpy.clear_keymap_cache()
    call screen battle_screen(bg=battleground_bg, disc="plate_dirt", dec_1=["decoration_rail_front1", 950, 0], dec_2=["decoration_altberlin_back1", 3, 320]) with battleopening
    $ renpy.block_rollback()
    
label bat0000101_aftermath:
    scene black
    $ renpy.pause(1.0, hard=True)
    
    #Aftermath
    $ persistent.skip_battle_sensitive = False
    $ skip_battle_selected = False
    $ battle_count +=1
    $_game_menu_screen = "save_screen"
    $ renpy.block_rollback()
    $ cp = max_cp
    $ cp += 30
    $ max_cp += 30
    
    #Unlocked Player Team Set
    if not skip_battle_selected:
        $ load_data([
            "panzer_renaultftzipangu"
            ], "fighter")
    $ persistent.skip_battle_sensitive = False
    $ skip_battle_selected = False
    
    #After Battle Continue
    $ _rollback = True
    $ store.text_history_enabled = True
    $ config.keymap['skip'].append('K_LCTRL')
    $ config.keymap['skip'].append('K_RCTRL')
    $ config.keymap['hide_windows'].append('h')
    $ renpy.clear_keymap_cache()
    
    jump bat0000101_continue
    
###########################################################################
    #bat0000101	-	Battle End
###########################################################################
label bat0000101_continue:

    play soundfx "se/battle2.ogg" fadein 3.0
    scene city1
    show spark
    with pixellate
    play music "music/glory.ogg"
    
    "As we take out the Zhinese ground troops and their heavy guns, the road is open for us to make it to the river."
    me "Let's break out and cross that bridge. On the count of three! One . . .  two . . .  three!"
    
    play sound4 "se/metal_steps.ogg"
    play sound2 "se/run.ogg"
    play sound3 "se/run2.ogg"
    play soundfx5 "se/run2.ogg"
    scene day1_tank
    show spark
    with dissolve
    queue sound2 "se/run.ogg"
    play soundfx4 "se/run.ogg"
    
    "The squad get to their feet and begin dashing out from behind the burntout automobiles."
    "Heading for the bridge, now empty of soldiers, we run over the cobblestones and soon reach the other side."
    me "At the end of this road, there's the garrison grounds . . . let's try to get there in one piece!"
    
    stop soundfx fadeout 3.0
    stop soundfx4 fadeout 1.0
    stop soundfx5 fadeout 1.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    scene black
    with fade
    
    $ mouse_visible = False
    show expression Text(_("Two miles away, at the city garrison . . ."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx2 "se/march.ogg" fadein 3.0
    play soundfx3 "se/tank_far.ogg" fadein 3.0
    scene zhina_temple
    with fade
    play music "music/horror.ogg"
    
    "As the {i}Kittentang{/i} forces retreat to the temple grounds, the city is slowly encircled by the pincer of the enemy army."
    "With many civilians now having fled Wukou, the soldiers prepare to leave themselves."
    
    show nyan determined
    with dissolve
    
    nyan "Don't leave the Zipanguese any materiel to wage war. Take anything you can, destroy whatever you can't shift."
    "Nyan Katshex oversees the evacuation of the armed forces, as one platoon after another marches to the west."
    zhinasol shock "Generalissima, enemy forces have taken one of the bridges east of here! We only just made it back."
    
    play silsound4 "se/silly8.ogg"
    show nyan sad
    
    nyan "What? The Zipanguese are already in the city? I thought blowing the dikes would have slowed them . . ."
    zhinasol determined "They took out two of our heavy machine guns, and now they're headed this way. What should we do?"
    
    show nyan determined
    with dissolve
    
    "Staring off into the distance, the Red Generalissima thinks for a moment."
    nyan "Let them come. I'll handle them here . . ."
    
    play sound6 "se/walk.ogg"
    hide nyan
    with dissolve
    
    "Wandering away, Nyan heads towards the main temple building."
    zhinasol shock "G-Generalissima?"
    nyan determined "Hold them off for as long as you can. Then, evacuate with the others and set fire to the temple."
    "As they abandon Wukou to the invaders, the Zhinese defenders plan for their escape . . ."
    
    stop soundfx2 fadeout 3.0
    stop soundfx3 fadeout 3.0
    stop music fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    play soundfx "se/battle2.ogg" fadein 3.0
    scene zhina_lane
    show spark
    with fade
    play music "music/evil.ogg"
    
    "Marching through the lanes of Wukou, we eventually reach the western districts of the city."
    "In the middling distance, we see the tiled roof of a temple standing tall above the surrounding buildings."
    me "Within those walls, Nyan Katshek's garrison stands fast, ready to do or die . . ."
    
    play silsound3 "se/silly9.ogg"
    
    tak_un shock "N-Nyan Katshek? Is that why we're here, Boss-man? We're going to fight Nyan herself?!"
    "Ignoring the others, I pull out the binoculars and observe our target."
    "Guards stand watch on the walls of the temple grounds, and the gates are fastened shut."
    me "Today, we're going to make history . . . let's move slowly and find a way into the garrison." 
    
    play sound6 "se/walk.ogg"
    play sound4 "se/metal_steps.ogg"
    play sound5 "se/run.ogg"
    play sound7 "se/run2.ogg"
    
    "Slowing our advance, we split up and take cover in the surrounding buildings, quietly making our way forward."
    "Following along the temple walls, I find a blind spot we can penetrate."
    me "Soldier, give me a leg-up. We're going over the wall here."
    tak_un determined "Y-Yes sir!"
    
    stop music fadeout 3.0
    play sound2 "se/brush.ogg"
    scene day1
    with dissolve
    
    "I'm given a boost by one of the soldiers and we clamber over, getting white plaster marks on our battle dress."
    
    play sound3 "se/collapse.ogg"
    play sound4 "se/break.ogg"
    scene zhina_temple
    show spark
    with hpunch
    with vpunch
    play soundfx4 "se/battle2.ogg" fadein 3.0
    play soundfx3 "se/fire2.ogg" volume 0.5 fadein 3.0
    play music "music/glory.ogg"
    
    "We hop the wall and are confronted by dozens of soldiers, sabotaging heavy guns and setting fire to warehouses."
    
    show object_templerush at tankpos
    with dissolve
    
    "Small fires burn as explosives tar the ground. Sandbags are piled up by the temple steps, hiding enemy nests."
    "Destroying their leftover supplies, the Zhinese are plotting their escape . . ."
    
    play silsound5 "se/poke.ogg"
    
    zhinasol shock "T-They're here! We have to stop them in their tracks, for the Generalissima!"
    
    play soundfx2 "se/battle4.ogg"
    
    "Rushing our squad as we scale the walls, soon we're engaged in a fierce battle with what's left of the garrison."
    "A deadly battle rages within the temple walls as our imperial forces fire upon the nationalist resisters."
    "Soldiers fight hand to hand, using shovels and the butts of rifles, grappling in the dirt and the dust."
    "The pristine temple grounds are a direct contrast to the blood and smoke of the soldiers below."
    me "It's a battle alright . . ."
    
    hide object_templerush
    with dissolve
    
    "Amongst the confusion, I look across to the main temple building and see a hooded figure watching us . . ."
    nyan determined ". . . . . . . . ."
    
    play silsound6 "se/silly12.ogg"
    
    me "N-Nyan Katshex!"
    
    play sound3 "se/walk.ogg"
    
    "The leader of the {i}Kittentang{/i} then turns and disappears into the building."
    
    play sound2 "se/cock.ogg"
    show speedlines with circleirisout
    
    me "They're trying to delay us here! Fight back and let's finish our mission!"
    
    stop soundfx fadeout 1.0
    stop soundfx2 fadeout 1.0
    stop soundfx3 fadeout 1.0
    stop soundfx4 fadeout 1.0
    stop music fadeout 1.0
    scene black
    with pixellate
    
    jump bat0000102_begin
    
label bat0000102_begin:
###########################################################################
    #bat0000102	-	Nyan Mission: Temple Battle
###########################################################################
    
    #History Block
    $ renpy.block_rollback()
    $ store.text_history_enabled = False
    $ _rollback = False
    $ config.skipping = False
    $ q_title = "Operation Temple: Battle of Wukou"
    
    #Enemy Team Set
    $ enemy_team = BaseTeam("Enemy", Solid("#000000", xysize=(50,50)), limit=50)
    $ enemy_team.add_fighter("enemy_zhina_gunner_heer1")
    $ enemy_team.add_fighter("enemy_meowist_gunner_heer1")
    $ enemy_team.add_fighter("enemy_panzer_l335zhina")
    $ enemy_team.add_fighter("enemy_meowist_marksman_heer1")
    
    # Selection Screen Set
    $ player_team = BaseTeam("Player", Solid("#000000", xysize=(50,50)), limit=50)
    play battlemusic "music/map3.ogg"
    call screen non_battle_party_screen

    # Battle Set
    $ config.skipping = False
    stop battlemusic fadeout 1.0
    scene black
    $ renpy.pause(1.0, hard=True)
    play battlesfx "se/battle4.ogg" volume 0.25
    play battlemusic "music/battle_sea.ogg"
    $ renpy.block_rollback()
    $ fight_end = "bat0000102_aftermath"
    $ game = Battleground("Battle Stage   |   Temple Grounds Battle", player_team.store[0], enemy_team.store[0], "zhinatemple")
    $ battle_terrain = "urban"
    $ battleground_bg = "background_cyrano"
    $_game_menu_screen = None
    $ config.skipping = False
    $ config.keymap['skip'].remove('K_LCTRL')
    $ config.keymap['skip'].remove('K_RCTRL')
    $ config.keymap['hide_windows'].remove('h')
    $ renpy.clear_keymap_cache()
    call screen battle_screen(bg=battleground_bg, disc="plate_urban", dec_1=["decoration_zhina_front1", 950, 0], dec_2=["decoration_zhina_back1", 3, 320]) with battleopening
    $ renpy.block_rollback()
    
label bat0000102_aftermath:
    scene black
    $ renpy.pause(1.0, hard=True)
    
    #Aftermath
    $ persistent.skip_battle_sensitive = False
    $ skip_battle_selected = False
    $ battle_count +=1
    $_game_menu_screen = "save_screen"
    $ renpy.block_rollback()
    $ cp = max_cp
    $ cp += 590
    $ max_cp += 590
    
    #After Battle Continue
    $ _rollback = True
    $ store.text_history_enabled = True
    $ config.keymap['skip'].append('K_LCTRL')
    $ config.keymap['skip'].append('K_RCTRL')
    $ config.keymap['hide_windows'].append('h')
    $ renpy.clear_keymap_cache()
    
    jump bat0000102_continue
    
###########################################################################
    #bat0000102	-	Battle End
###########################################################################
label bat0000102_continue:
    
    play soundfx "se/battle2.ogg" fadein 3.0
    scene zhina_temple
    show spark
    with pixellate
    play sound5 "se/boom2.ogg"
    play music "music/evil.ogg"
    
    "Eventually, our squad manages beat back the attackers and gain a foothold within the temple grounds."
    "One by one, enemy soldiers run away, retreating with the others and leaving the city . . ."
    
    play sound6 "se/walk.ogg"
    play sound4 "se/metal_steps.ogg"
    play sound5 "se/run.ogg"
    play sound7 "se/run2.ogg"
    
    "Our squad makes its way across the open courtyard, ducking behind low walls and crates."
    "Soon, we crouch by our rallying point, safe beneath a footbridge that stretches across a grassy knoll."
    me "Nyan Katshex is in this building ahead . . ."
    tak_un determined "Go ahead, Boss-man. We'll cover you from out here."
    me "Thank you . . . I'm sorry, I never asked your name?"
    
    play silsound3 "se/silly20.ogg"
    
    tak determined "Takeshi, sir."
    me "I-Is that all?"
    tak normal "That's my full name."
    "Takeshi. I'll make sure to remember that."
    
    play sound6 "se/run.ogg"
    
    "As the others continue to hold off the defenders, I break away and enter the temple building itself."
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    play soundfx3 "se/room.ogg" fadein 3.0
    scene zhina_temple_room
    with fade
    play music "music/horror.ogg"
    play sound7 "se/walk.ogg"
    
    "Once inside, I find myself standing in the temple's inner sanctum."
    "Confiscated furniture, paintings and sculptures are scattered amongst the tall pillars and holy imagery."
    me "The entire place is kitted out to the rafters with rare treasures and beautiful artwork . . ."
    "Silk cushions, fur carpets, diamond chandeliers, marble monuments, ornate tables . . ."
    
    show nyan determined
    with dissolve
    
    "Generalissima Nyan Katshex sits on an old and lustrous throne, a delicate small vase balanced in one hand."
    nyan "Decadence . . . pure decadence . . ."
    
    play sound6 "se/cock.ogg"
    
    me "Nyan Katshex . . . my name is Sergeant Yamato Yamamoto, and I'm here to carry out a mission . . ."
    "She looks at me nonchalantly, then back to the small vase in her hand."
    nyan "For many years, my people fought to remove the disease of imperial monarchy from our lands."
    nyan "We overthrew a dynasty, marched and battled for our democracy, and sought to remove the foreign powers."
    nyan "In the name of freedom, a national government rose from the ashes to make Zhina strong again . . ."
    
    play sound6 "se/break.ogg"
    
    "With little care or grace, she throws the vase to the floor and it smashes into a dozen pieces."
    nyan "And yet that same decadence and destruction continues to plague our country."
    nyan "Just as we started to win out against the xommies, when victory was at hand, you morons showed up . . ."
    
    show nyan angry
    play silsound4 "se/silly2.ogg"
    
    nyan "The arrogant, murderous, imperialist warriors from across the sea, here to make us serfs once more!"
    "Spitting on the floor, the Red Generalissima glares at me."
    me "Who are you to talk? You're a butcher, Nyan Katshex. The purges, the murdering, the corruption . . ."
    "It took being kidnapped to force her into an alliance with other Zhinese factions, in order to fight us."
    me "You blew the dikes on the Golden River, flooding the plains and drowning thousands of soldiers and civilians!"
    
    play silsound6 "se/silly12.ogg"
    
    nyan "Don't try to lecture me, you samurai scum. I've heard the reports . . . your soldiers are attacking civilians like savages!"
    nyan "Pillaging, looting, slaughtering . . . for a people so obsessed with honor, don't you have any shame?!"
    "She's not wrong. This war . . . this invasion of Zhina is barbaric . . ."
    nyan "Hmm? Don't you have anything to say?"
    ". . . but I have a duty to carry out this assignment. This dictator must be toppled."
    
    play sound6 "se/cock.ogg"
    stop music fadeout 3.0
    show nyan determined
    with dissolve
    
    "Raising my rifle, I point it at the leader of the {i}Kittentang{/i}."
    nyan "So that's your answer . . . fine. Now you shall see the true power of Zhinese Nyantionalism and the {i}Kittentang{/i}!"
    
    stop soundfx3 fadeout 2.0
    play sound3 "se/battle/purge.ogg"
    play sound4 "se/battle/death.ogg"
    play soundfx2 "se/power2.ogg" fadein 3.0
    show transparent behind nyan
    with dissolve
    play sound7 "se/power.ogg"
    play sound5 "se/flash.ogg"
    show nyan powers large
    with dissolve
    play sound2 "se/battle/pose.ogg"
    play sound6 "se/rumble.ogg"
    play music "music/nyan.ogg"
    scene zhina_temple_room_distort
    show transparent
    show nyan powers large
    with hpunch
    with vpunch
    queue sound5 "se/collapse.ogg"
    
    "Suddenly, a powerful aura bursts forth from the dictator, knocking me backwards."
    
    queue sound3 "se/gundrop.ogg"
    queue sound5 "se/dash.ogg"
    
    "My rifle goes flying from my hands and lands with a clatter on the other side of the hall."
    me "H-Huh? What's going on? W-Why is she glowing?! I've never seen anything like this before . . ."
    nyan "I will never surrender, nor be taken out by the likes of you! Your intentions are not noble. Your invasions are illegal . . ."
    nyan "Millions are dying and suffering, all because of your blind arrogance, lies and hatred. You leave me with no choice . . ."
    
    play sound6 "se/scalp.ogg"
    
    "Scrabbling around on the ground, I pull a sword sticking out of a treasure pile and point it at the short girl's forehead."
    me "Wukou is already surrounded . . . it's your fate to fall here, with the city . . ."
    nyan "Enough talking, let's do this!"
    "As I size up the Zhinese warrior before me, she takes a fighting stance and steadies her hand."
    "Nyan Katshex, the dictator, wants to fight! An experienced veteran in the field . . . let's see what she's made of!"
    
    stop soundfx2 fadeout 1.0
    stop music fadeout 1.0
    scene black
    with pixellate
    
    jump bat0000103_begin
    
label bat0000103_begin:
###########################################################################
    #bat0000103	-	Nyan Mission: Nyan Boss Battle
###########################################################################
    
    #History Block
    $ renpy.block_rollback()
    $ store.text_history_enabled = False
    $ _rollback = False
    $ config.skipping = False
    $ q_title = "Operation Nyan: Battle of Wukou"
    
    #Enemy Team Set
    $ enemy_team = BaseTeam("Enemy", Solid("#000000", xysize=(50,50)), limit=50)
    $ enemy_team.add_fighter("enemy_commander_nyan")
    
    # Selection Screen Set
    $ player_team = BaseTeam("Player", Solid("#000000", xysize=(50,50)), limit=50)
    play battlemusic "music/map3.ogg"
    call screen non_battle_party_screen

    # Battle Set
    $ config.skipping = False
    stop battlemusic fadeout 1.0
    scene black
    $ renpy.pause(1.0, hard=True)
    play battlesfx "se/battle4.ogg" volume 0.25
    play battlemusic "music/nyan.ogg"
    $ renpy.block_rollback()
    $ fight_end = "bat0000103_aftermath"
    $ game = Battleground("Battle Stage   |   Boss Battle", player_team.store[0], enemy_team.store[0], "zhinathrone")
    $ battle_terrain = "urban"
    $ battleground_bg = "background_dark"
    $_game_menu_screen = None
    $ breakpoint_lossokay_nyan = True
    $ config.skipping = False
    $ config.keymap['skip'].remove('K_LCTRL')
    $ config.keymap['skip'].remove('K_RCTRL')
    $ config.keymap['hide_windows'].remove('h')
    $ renpy.clear_keymap_cache()
    call screen battle_screen(bg=battleground_bg, disc="plate_indoors", dec_1=["decoration_zhinatemple_front1", 950, 0], dec_2=["decoration_zhinatemple_back1", 3, 320]) with battleopening
    $ renpy.block_rollback()
    
label bat0000103_aftermath:
    scene black
    $ renpy.pause(1.0, hard=True)
    
    #Aftermath
    if not skip_battle_selected:
        $ achievement.grant("BATTLE_BEATNYAN1")
        $ achievement.sync()
    $ persistent.skip_battle_sensitive = False
    $ skip_battle_selected = False
    $ battle_count +=1
    $_game_menu_screen = "save_screen"
    $ renpy.block_rollback()
    $ cp = max_cp
    $ cp += 30
    $ max_cp += 30
    $ breakpoint_lossokay_nyan = False
    
    #Unload Player Team Set
    $ unload_data([
        "commander_yamato_heer0"
        ], "fighter")
    
    #After Battle Continue
    $ _rollback = True
    $ store.text_history_enabled = True
    $ config.keymap['skip'].append('K_LCTRL')
    $ config.keymap['skip'].append('K_RCTRL')
    $ config.keymap['hide_windows'].append('h')
    $ renpy.clear_keymap_cache()
    
    scene cg_redgeneralissima
    hide cg_redgeneralissima
    
    jump bat0000103_continue
    
###########################################################################
    #bat0000103	-	Battle End
###########################################################################
label bat0000103_continue:
    
    play soundfx2 "se/power2.ogg" fadein 3.0
    scene zhina_temple_room
    show transparent
    show nyan powers large
    with pixellate
    play sound6 "se/break2.ogg"
    play music "music/evil.ogg"
    
    "Battling against one another, it seems we're equally matched as we dance back and forth."
    "The dictator of the {i}Kittentang{/i} refuses to give in, and breaks a sweat trying to hold me off."
    nyan "No . . . I won't lose here . . ."
    "Pulling a pin, she rolls a grenade across the ground. I try to duck for cover but . . ."
    
    play sound2 "se/collapse.ogg"
    play sound4 "se/grenade.ogg"
    scene zhina_temple_room
    show transparent
    show nyan powers large
    with hpunch
    with vpunch
    play sound6 "se/boom2.ogg"
    play sound3 "se/collapse.ogg"
    play sound5 "se/break2.ogg"
    
    "I'm blown back against a wooden pillar. The force of the throw cracks the column in two and I collapse to the ground."
    me "Yaaaaaaaarghhhh . . ."
    "A tearing pain shoots up my arm and I cry out in pain. The ligaments in my shoulder feel torn."
    nyan "I warned you. I told you that you would get hurt."
    "Out of breath, the dictator says that boldly, though she seems weakened as well."
    
    play silsound5 "se/silly4.ogg"
    
    me "M-My shoulder . . . arghhh . . . I think s-something's lodged in there . . ."
    nyan "Shrapnel. If you're not careful you might even lose the use of your arm."
    "She winces as she says that, struggling to keep her footing as she stands over me."
    nyan "Take this chance and run . . . I will spare your life if you go now."
    "Determinedly, the girl seems to be making a genuine offer. If I run, I will live to fight another day."
    "But if I stand down now then Nyan Katshex will escape. I will have failed my mission . . ."
    "It doesn't seem like I have much choice . . ."
    
    play silsound4 "se/poke.ogg"
    
    me "N-Never . . . I will fight on to the end . . ."
    nyan "And here I thought I would show you some mercy."
    me "What kind of soldier would I be if I ran now? You're out of breath too . . . just a little longer and . . ."
    
    stop soundfx2 fadeout 3.0
    play soundfx "se/fire2.ogg" fadein 3.0
    play sound3 "se/boom2.ogg"
    play sound6 "se/break2.ogg"
    scene zhina_temple_room
    show transparent
    show nyan powers large
    show fire
    show spark
    with hpunch
    with vpunch
    show sunraysflip behind smoke
    
    "At that moment, the ceiling collapses in with a mighty crash as fiery rubble rains down from above."
    
    play sound5 "se/walk.ogg"
    
    "A fire starts to spread and the room fills with black smoke, causing Nyan to back away."
    nyan "Too bad you won't have a chance to catch me . . ."
    "Beams start to collapse around us, as the fire rages around the temple, the treasures igniting in flames."
    
    play sound3 "se/boom2.ogg"
    play sound6 "se/break2.ogg"
    show spark
    with hpunch
    with vpunch
    
    "A giant wooden pillar smashes to the ground between us, cutting us off from one another."
    
    play silsound2 "se/silly12.ogg"
    
    nyan "We're setting the city on fire before we go. There won't be anything for you thieves to pillage or plunder!"
    me "No. No, it can't end like this! I have to take you out . . ."
    "Coughing and spluttering, the black smoke gets in my lungs and stings my eyeballs."
    nyan "So long, you failed assassin . . ."
    
    play sound4 "se/walk.ogg"
    hide nyan
    with dissolve
    
    "Falling about, I try to see the Generalissima through the embers, but she's already vanished, escaping out the back."
    
    play silsound2 "se/silly17.ogg"
    
    me "Nyan Katshex . . . get back here!"
    
    play sound5 "se/run.ogg"
    
    tak shock "B-Boss-man! Are you still in here? We have to get out, they enemy have set the place on fire!"
    me "No, we have to stop her . . . {i}cough{/i} . . . we have to stop the Zhinese dictator . . . {i}cough cough{/i} . . ."
    "Struggling to stay conscious in the smoke, the heat from the flames becomes too intense to continue."
    "Stumbling backwards, feeling weak, I take the soldier's advice and slowly limp away from the scene."
    me "Damn it . . ."
    
    stop soundfx fadeout 3.0
    scene black
    with fade
    
    "Passing through the inner sanctum and the vast corridors, we stumble outside into the courtyard."
    
    play soundfx "se/fire2.ogg" fadein 3.0
    play soundfx2 "se/battle2.ogg" fadein 3.0
    scene zhina_temple
    show fire
    show spark
    with fade
    
    "In the bright daylight, I turn to see the temple ablaze and the temple grounds abandoned."
    "Though the sounds of battle continue around the city, only my fellow soldiers are here still, waiting for me."
    
    play sound2 "se/collapse.ogg"
    scene zhina_temple
    show fire
    show spark
    with hpunch
    with vpunch
    play sound3 "se/run.ogg"
    
    "Arriving by the stone steps at the entrance, I collapse to my knees as soldiers come to my side."
    tak shock "B-Boss-man? Are you alright? Can you breathe?"
    "Noticing the blood pouring out of my arm, they go quiet."
    me "I'm fine . . . just a wounded shoulder . . ."
    
    play silsound5 "se/silly20.ogg"
    
    tak determined "I should call for a medic. Or we should find you a doctor or something!"
    me "Who's going to come? We're stranded here alone, remember? In this burning city . . ."
    "Turning back I look at the grand temple behind me, now burning to ashes."
    "In the distance, smoke billows in from other areas. A seeming quiet descends over the captured city."
    "After weeks of fighting, the battle for Wukou is finally over."
    me "Nyan Katshex has escaped once again . . . the dictator of the {i}Kittentang{/i} lives to fight another day."
    "Knowing her reputation for speed, she's probably halfway across Zhina by now."
    "Our troops will continue the chase, but judging by the power she showed in our battle . . ."
    me "It's not the last we'll see of her . . ."
    
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    stop music fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    scene black
    with fade
    
    $ mouse_visible = False
    show expression Text(_("Meanwhile, north of the Dardaria-Sovia border . . ."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
 
    play soundfx4 "se/battle3.ogg" fadein 3.0
    scene field_day_notree
    with fade
    show zhukky hat determined
    with dissolve
    play music "music/soviagrad.ogg"
    play sound2 "se/power.ogg"
    
    "Commander Zhukky watches as her conquered enemies run from the battle."
    zh "That should be the last of them . . . pathetic worms."
    "The Zipanguese forces retreat over the hills and back towards their bases within Dardaria."
    "With a Sovian victory over the invaders, the border towns within Sovia Major will remain safe."
    
    show zhukky hat normal 
    with dissolve
    
    zh "They've been crossing the river less frequently this past month. Perhaps they've finally accepted they can't win . . ."
    "Zipangu and Sovia have been engaging one another in limited confrontations for the past years."
    "Since the Empire of Zipangu arrived in the region, the Sovians have sought control of the northern areas within Dardaria."
    "In retaliation for attempted invasions, Zipanguese soldiers attack Sovian towns from across the river."
    
    play sound6 "se/run.ogg"
    show zhukky hat normal at right3 
    with ease
    show sovian determined at left3 
    with dissolve
    
    sov "Commander Zhukky! Orders from Moskva, ma'am!"
    zh "Hmm?"
    sov "You're to return to the west as soon as possible! You're needed in the capital."
    
    show zhukky hat determined
    with dissolve
    
    zh "Well, I suppose I'm finished here anyway . . ."
    sov "{i}Tak tochno{/i}. A train is waiting for you, commander."
    
    play sound3 "se/walk.ogg"
    hide sovian 
    with dissolve
    show zhukky hat determined at center 
    with ease
    
    zh "I'm going back to Europa then . . . I wonder what Starin has planned this time."
    
    stop soundfx4 fadeout 3.0
    stop music fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    scene black
    with fade
    
    $ mouse_visible = False
    show expression Text(_("Some time later, in the forests of central Zhina . . ."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx "se/brush.ogg" fadein 3.0
    play soundfx2 "se/birds.ogg" fadein 3.0
    play soundfx3 "se/march.ogg" fadein 3.0
    scene woodland_clearing
    with fade
    play music "music/horror.ogg"
    show nyan angry
    with dissolve
    play sound3 "se/slash.ogg"
    
    nyan "What's with all these stinking plants?! I can't cut my way through . . ."
    "Generalissima Nyan Katshek's forces make their way through the undergrowth, retreating into the hills."
    "The dense shrubbery is proving difficult to cut through and it's beginning to frustrate the catgirl."
    
    queue sound3 "se/slash.ogg"
    show nyan angry
    with hpunch
    
    nyan "Grrrr . . . it's not fair . . . it isn't fair . . ."
    "From now on, the Nyantionalists will have to wage a war of resistance from their mountainous fortress in Xhongqing."
    "It will be a long game of {i}cat-and-mouse{/i} with their Zipanguese enemies, and she's certainly the {i}mouse{/i} this time around."
    "With the air force and navy essentially destroyed, they will have to rely on the help of the local {i}Meowists{/i} to support them."
    
    show nyan determined
    with dissolve
    
    nyan "This is going to be a long campaign. The Zipanguese are too powerful . . . we will have to grind them down, slowly."
    "As they progress through the mountains, the future of their cause seems uncertain."
    "The long columns of Zhinese fighters march along the dirt track, disappearing into the dark woods."
    "Staring off into the distance, the girl makes a serious face."
    nyan "Mark my words, Yamato Yamamoto. Before this war is over, I will find you again and defeat you for real . . ."
    
    play sound6 "se/walk.ogg"
    hide nyan
    with dissolve
    
    "Surveying the area once more, Nyan Katshek turns around and marches into the forest after her troops . . ."
    
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    stop soundfx3 fadeout 3.0
    
    stop music fadeout 8.0
    $_game_menu_screen = None
    $ renpy.block_rollback()
    $ store.text_history_enabled = False
    $ _rollback = False
    $ mouse_visible = False
    window hide
    scene theend
    with dissolve5
    $ renpy.pause(1.0, hard=True)
    
    scene white
    with dissolve2
    $ renpy.pause(1.0, hard=True)
    
    scene black
    with dissolve
    $ mouse_visible = True
    $ store.text_history_enabled = True
    
    #PERSISTENT CAMPAIGN UNLOCKED
    $ nyanbattles_selection = True
    $ persistent.nyan_campaign_completed = True
    $ codex_unlocked = True
    
    return

###############################################################################################################

    
