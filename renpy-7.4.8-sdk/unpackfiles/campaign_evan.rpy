#####################################################################################################################################################
#####################################################################################################################################################
###### EVAN SIDE STORY ###########################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################

label campaign_evan:
    window hide
    stop music fadeout 1.0
    stop soundfx fadeout 1.0
    stop mmsound fadeout 1.0
    stop mmsound2 fadeout 1.0
    $ _window_during_transitions = False
    $_game_menu_screen = "save_screen"
    if level_choice == 1:
        $ save_name = "A True Rival (Easy)"
    elif level_choice == 2:
        $ save_name = "A True Rival (Normal)"
    else:
        $ save_name = "A True Rival (Expert)"
    $ store.text_history_enabled = True
    $ mouse_visible = False
    scene black
    with dissolve2
    pause 0.1
    
    jump sc000069
    
#####################################################################################################################################################
#sc000069	-	Evan Braun comes to town
#####################################################################################################################################################    
label sc000069:
    play soundfx "se/city.ogg" fadein 3.0
    scene day2
    with fade
    play music "music/bravery.ogg"
    $ mouse_visible = True
    
    "Some time after our battles in the north, before Germania turns its attention to the west . . ."
    "It's a new day in Altberlin. Germania's successful invasion of Norda and Dania has inspired the people."
    "While the war brought apprehension at first, the continued victories have encouraged them onto a war footing."
    "There's an excited atmosphere, a hustle and bustle to the crowds on the street . . ."
    
    scene altberlin
    with dissolve
    
    me "Today, my schedule is jam-packed."
    "I'm meant to be meeting dignitaries in the north, inspecting research facilities in the south, shadowing potential traitors . . ."
    me "And then, this morning, I have a date with the Füühbar . . ."
    "Okay. Maybe {i}'date'{/i} is a stretch. We're doing a troop inspection together at the local training grounds."
    "Many veterans of Polix and Norda are deserving of medals, which Hitora will have to pin onto their uniforms, one-by-one."
    me "A standard duty but still a rather important ceremonial task."
    "Before that though, I have time to kill, so I wander aimlessly through the streets of the capital city."
    "As I do so, I listen in on the conversations of the populace . . ."
    
    jump voxpop6
    
label voxpop6:    
    $ voxpopmode_enabled = True
    $ voxpopjump = "voxpop_leave6"
    $ voxpopleave_sensitive = always_true
    menu:
        "Family":
             jump voxpop_family1
        "Children":
            jump voxpop_children1
        "Guderian":
             jump voxpop_guderian2
        "Large crowd":
            jump voxpop_crowd1
        "Shopkeeper":
            jump voxpop_shopkeeper2
        "Rich Man":
             jump voxpop_richman1
    
label voxpop_family1: 
    show woman happy
    show oldman happy at right2
    show oldwoman shock at left2
    with dissolve
    
    om "Did you hear? He's coming back!"
    wom "Ehh? His trip to South Amerika is finished already?"
    ow "I heard he travelled through all of United Amerika on a film shoot."
    wom "No, last I heard, he was working for a fashion magazine in Lutetia. Such a cool guy is coming here!"
    "Huh . . . I thought they'd all be talking about the conquest of Norda."
    "It sounds like some kind of film star or celebrity is on their way to Germania."
    
    show woman determined
    show oldman shock
    show oldwoman normal
    
    wom "How do you think the Füühbar will take the news?"
    ow "Of course . . . we shouldn't talk so loudly about it. It would be unseemly."
    "Hmm? Unseemly? I wonder what they mean . . ."
    
    hide woman
    hide oldman
    hide oldwoman
    jump voxpop6
    
label voxpop_children1:
    show youth happy as youth1 at left2
    show desertyouth happy as youth2
    show zipanguyouth happy as youth3 at right2
    with dissolve
    
    "A gang of schoolboys go wandering past."
    youth happy "Big bro Evan is so cool! He once caught a frog and let me keep it!"
    youth happy "Big bro Evan taught me how to ride a bike and ask out the pretty girls in my class!"
    youth happy "Big bro Evan helped me sew my {i}Hitora Scouts{/i} badges on after he helped me win them!"
    "Whoever this {i}'Evan'{/i} person is, they sound like a real character."
    
    hide youth1
    hide youth2
    hide youth3
    jump voxpop6
    
label voxpop_guderian2:
    show guderian normal
    with dissolve
    
    "I bump into Guderian as they're out shopping."
    me "Ahh, hey there roomie . . . what are you doing right now?"
    
    show guderian determined
    
    gud "I'm just shopping for the latest {i}Panzy{/i} gear."
    me "{i}'Panzy gear'?{/i}"
    
    show guderian shock
    
    gud "There's a great store on the high street that specializes in everything to do with tanks."
    gud "You can pick up the latest clothing like goggles and trenchcoats, or actual parts like spare treads or dud shells."
    
    show guderian determined
    
    gud "They have different camo paint too, and shovels, tools, rations, toys, postcards . . . pretty much everything!"
    "This sounds like a pretty cool shop."
    me "I'll have to try it out some time."
    
    show guderian happy
    with dissolve
    
    gud "If you're a regular customer, you get free tea and cakes at the upstairs cafe, {i}'Delica'tank'en'{/i}."
    "That does it, I have to go to this shop now!"
    
    if choice_delicatanken_answered:
        jump choice_delicatanken_continue
    else:
        gud "You should go with someone!"
        me "Hmm? That sounds nice. I guess I'll take . . ."
        $ voxpopmode_enabled = False
        jump choice_delicatanken
    
label choice_delicatanken_answer1:
    me "Adorofia Hitora. She loves cakes after all."
    "I need to maintain my cover and stay in her good books after those failed attempts."
    "And, it wouldn't hurt to improve on our comradery, as close companions . . ."
    gud "Well, good luck convincing them to come along."
    jump choice_delicatanken_continue
    
label choice_delicatanken_answer2:
    me "Winstefina Churchill. She loves tea so we can share a pot."
    "I mean, it's quite unlikely since Germania and Britannia are at war. It would be interesting though."
    "And I need to ask her about what happened in Norda . . ."
    gud "Well, good luck convincing them to come along."
    jump choice_delicatanken_continue

label choice_delicatanken_answer3:
    me "Gallia Cyrano. She loves cafes, so long as there's somewhere to smoke."
    "She's a strange girl, with a love of tanks, and her ties to the {i}Alliance{/i} might prove helpful one day . . ."
    gud "Well, good luck convincing them to come along."
    jump choice_delicatanken_continue

label choice_delicatanken_answer4:
    me "Iosefina Starin. She needs the exercise and likes the sunshine."
    "It's not like Germania and Sovia will be at war any time soon. And I have many questions to ask her . . ."
    gud "Well, good luck convincing them to come along."
    jump choice_delicatanken_continue    
    
label choice_delicatanken_continue:
    show guderian normal
    with dissolve
    
    "I reckon I've taken up enough of Guderian's time."
    me "Well, I hope you enjoy yourself! I've got to get back to . . . whatever it is I'm doing."
    
    show guderian determined
    
    gud "See you later roomie!"
    "Maybe I'll take Guderian to this cafe as well . . ."
    
    hide guderian
    $ voxpopmode_enabled = True
    jump voxpop6
    
label voxpop_crowd1:
    play soundfx4 "se/cheer.ogg" fadein 5.0
    show crowd
    with dissolve
    
    "It seems there's some kind of commotion at the center of town."
    "I try to push my way through, but the throngs of people are so tightly packed together that I simply fall back."
    wom shock "Oh my god! Oh my god! He's here!"
    "Excited guys and girls all seem to be aiming for something, but I can't tell what from this distance."
    me "I'll just leave it be for now . . ."
    
    stop soundfx4 fadeout 3.0
    hide crowd
    jump voxpop6
    
label voxpop_shopkeeper2:
    show fatman determined
    with dissolve
    
    "Passing a nearby coffee shop, the owner stands in the doorway with a scowl on his face."
    sk "Dirty . . . rotten . . . stinking . . ."
    "He doesn't sound happy about something, as he chews on the end of a cigarette."
    
    show fatman normal
    
    me "Excuse me? Can I help you at all? You seem upset about something."
    
    show fatman determined
    
    sk "That damn pretty boy! My wife can't stop talking about him."
    me "Pretty boy?"
    sk "He just flies in to Altberlin from nowhere and still acts like he's king of the hill . . ."
    "Ahh, he must be talking about me. I guess it takes some time to adjust to foreign-born soldiers getting involved."
    "Still, to call me a pretty boy? I don't think it fits all that well."
    
    show fatman shock
    
    me "Well, I mean you no harm. And tell your wife I'm flattered, but she should focus on her husband's needs instead."
    
    play silsound5 "se/silly21.ogg"
    show fatman determined
    
    sk "Huh? Who the heck asked you? It ain't none of your business!"
    me "Eh?"
    sk "Not only is this pretty boy wooing her! Now I got some Zipanguese kid trying to cheer me up! Just my luck . . ."
    
    play sound4 "se/walk.ogg"
    hide fatman
    with dissolve
    
    "Throwing his cigarette butt into the gutter, the shopkeep returns to his duties inside his store."
    me "Well . . . that went well."
    
    jump voxpop6
    
label voxpop_richman1:
    show maid normal at left3
    show politician happy at right3
    with dissolve
    
    richman "Maid! Look over there! It's a foreigner."
    maid "Ahh, yes sir."
    "A rather important-looking man arrives on the scene, with his maid in tow."
    richman "How wonderful it is to live in such a diverse society! Men of every creed, united in pursuit of Germanian purity!"
    
    show maid determined
    
    maid "That doesn't really follow . . . sir."
    "I'm ogled like a dog in a pet store window."
    richman "Look at him. This honorary Germanian. Look at his little face. He thinks he's people too."
    
    play silsound6 "se/silly8.ogg"
    show politician shock
    show maid shock
    
    me "Hey! Who the hell do you think you're talking to?!"
    richman "Ahh . . . you speak Germanian."
    me "Honestly . . ."
    
    play sound4 "se/walk.ogg"
    
    "Embarrassed for everyone involved, I make a quick getaway."
    
    hide politician
    hide maid
    jump voxpop6
    
label voxpop_leave6:
    $ voxpopmode_enabled = False
    
    "Passing by the crowds, I feel the wind beginning to nip at my heels."
    me "I should probably head over to the training grounds now. Hitora will be waiting for me . . ."
    
    play sound4 "se/walk.ogg"
    stop music fadeout 5.0
    
    "I start on my way, trying to outpace the bracing chill as I go."
    
    show evanbraun determined
    with dissolve
    
    evan_un ". . . . . . . . ."
    
    stop soundfx fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc000070

#####################################################################################################################################################
#sc000070	-	Troop inspection with Hitora (date) / Evan gatecrashes
#####################################################################################################################################################    
label sc000070:
    play soundfx2 "se/march3.ogg"
    scene armycamp
    with fade
    play music "music/rally.ogg"
    
    "As the weather begins to pick up, I meet with the Füühbar's party at the training grounds."
    
    show hitora hat happy at right35
    show joebbels normal at left35
    with dissolve
    
    hit "Ahh, Commander Yamato. There you are. I was thinking I'd have to award these bits of ribbon without you."
    "To demonstrate, Joebbels holds up a polished wooden box full of colorful medals for gallantry and military fortitude."
    "{i}Order Of The Plastic Cross, Vehrmaxt Long Service Award, Wound Badge, Infantry Assault Badge, Meme Medal{/i} . . ."
    "Lots of different awards of different orders. We have a mix of soldiers based here in Altberlin; veterans of many conflicts."
    
    show hitora hat normal
    
    me "Sorry. I got caught up eavesdropping on people."
    
    play silsound5 "se/silly9.ogg"
    show hitora hat moe2
    
    hit "Oh, you don't need to worry about doing that. Just leave that kind of work to the {i}Goosetapo{/i}."
    me "Huh?"
    goeb "D-Don't think too hard about i-it."
    "Wait? Am I being spied on like everyone else? How much do they know?"
    
    show hitora hat happy
    with dissolve
    show joebbels normal at left1
    show hitora hat happy at left3
    with ease
    show axis normal at center
    show desertaxis normal as axis2 at right1
    show camoaxis normal as axis1 at right3
    with dissolve
    
    "We begin to pass down the line of recruits. One by one, the Füühbar stops and compliments the soldiers."
    hit "You must have fought very bravely. Tell me, which battle were you in?"
    
    show axis determined
    
    axis "The invasion of Dania, my Füühbar."
    
    show hitora hat normal
    
    hit "Ahh yes. Such a fierce conflict. I can't imagine the horrors you endured."
    
    show axis normal
    
    axis "Actually, it was pretty bland. I got to eat some pastries and didn't even fire my weapon."
    
    play silsound3 "se/silly1.ogg"
    show hitora hat angry
    show axis shock
    
    hit "Wait a minute. You didn't do any fighting? Why are you being decorated for that?!"
    axis "Ahh! I mean, it was brutal. Yes! Extremely hard! I fought those small, childlike people so bravely my Füühbar!"
    hit "Nice try."
    goeb "N-Next time, try shooting at the e-enemy instead of eating c-cakes."
    "The soldier looks away in embarrassment, having lost their chance at an easy glory."
    
    hide axis
    show hitora hat happy
    with dissolve
    show desertaxis normal as axis2 at right15
    show camoaxis normal as axis1 at right4
    with ease
    
    "Hitora turns to the next individual." 
    hit "How about you? You look like a fine, strapping young soldier."
    
    show desertaxis determined as axis2
    
    axis determined "I fought incognito, in the {i}Wintertime War{/i}, my Füühbar, with the Finbardish volunteer forces."
    hit "Of course. Our friends in the north, desperate to defend their borders. You fought with honor, soldier."
    "Since she came from low birth, Hitora is more than happy to mingle with the common recruits, seeing them as true Germanians."
    "Pinning a brightly colored medal to the girl's uniform, the Füühbar takes a step back, then salutes proudly."
    
    hide hitora
    hide axis1
    hide axis2
    hide joebbels
    with dissolve
    
    "We continue down the line, one by one, awarding ribbons and bits of shiny metal to hardened fighters."
    "It takes time but eventually we finish our duties and leave the soldiers behind us."
    
    show hitora hat angry at right35
    show joebbels normal at left35
    with dissolve
    
    hit "It's incredible. In time, these warriors will be battling in Franzo and Britannia, expanding my empire further west."
    me "Huh? Battling in Franzo and Britannia?"
    "It looks like she's already made up her mind about conquering half the planet . . ."
    me "I think you still need to have some conversations about that with your general staff."
    hit "All that matters is that our nation overcomes its aggressors and wins a future for itself."
    
    stop music fadeout 5.0
    play silsound6 "se/silly7.ogg"
    show hitora hat worry
    show joebbels scared
    
    evan_un evil "Ha ha ha! After all this time, you're still making dumb, girly statements like that?"
    
    play sound4 "se/walk.ogg"
    
    "The voice belongs to a stranger, who begins to approach us across the tarmac."
    
    show hitora hat worry at right2
    show joebbels scared at right4
    with ease
    show evanbraun evil at left25
    with dissolve
    play music "music/winter.ogg"
    
    "The handsome civilian makes his way closer and closer, stopping only a few feet short of our congregation."
    "Wearing a garish shirt and sunglasses, he has his hair slicked up in a stylish manner."
    "His appearance and demeanor reminds me of the bad boy stereotypes you see in those Amerikan movies."
    
    play silsound2 "se/silly12.ogg"
    
    hit "Y-Y-You . . ."
    "Hitora and Joebbels stare, wide-eyed, and gasp in simultaneous shock. I guess they know him."
    hit "H-How . . . did you get past my security detail? Yamato, you're meant to be protecting me!"
    evan_un "You don't think I'd let a little pipsqueak like that stop me, do you?"
    me "Who are you calling a pipsqueak?"
    goeb "F-Füühbar . . . it's h-him."
    "Him? Who is this guy? He's unarmed and doesn't seem that threatening. Why are they both acting so concerned?"
    evan_un "Aww, little Joebbels, you still remember me, after all this time?"
    
    play silsound3 "se/silly4.ogg"
    
    "The Propaganda Minister begins to shake like a leaf, due to her androphobia, unable to say anything more."
    
    show hitora hat angry
    with dissolve
    
    hit "W-What do you think you're doing, showing up to a private ceremony like this?!"
    evan_un "Give me a break. I'm just checking in on my number one gal."
    "{i}'Gal'{/i}? Where does he get off referring to a genocidal dictator like that?"
    me "You should watch your language. You're speaking to the Füühbar of Germania."
    
    show evanbraun determined
    with dissolve
    
    "The guy turns on me, with a menacing glare."
    evan_un "Huh? Who's this wimp? One of your stupid inner circle friends? Oh wait, you don't have friends . . ."
    me "Wimp? Hitora, who is this goon?"
    
    play silsound5 "se/silly17.ogg"
    
    hit "His name . . . his name is Evan Braun . . . and he's a {i}Class-S{/i} jerk!"
    "Evan Braun, huh . . . doesn't ring any bells."
    
    show hitora hat moe1
    with dissolve
    
    hit "W-Why don't you run away again, Evan? That's what you did when I invaded Czexa. You were scared of me then!"
    evan "Come on, babe. I've grown up since all that. I've seen more of the world. And I don't intend to leave you be."
    
    show hitora hat embarrassed
    with dissolve
    
    hit "Just go away! I already decided . . . the Füühbar must be the sole ruler of Germania."
    evan "Did you really think I would just let you rule and live alone? I want to stay with you, right up until the last moment!"
    
    play silsound3 "se/silly9.ogg"
    
    hit "Even if you say something cool like that . . ."
    "Hitora looks away, her cheeks flushed with red. Is she actually getting flustered by this chump?"
    
    show joebbels sad
    with dissolve
    
    goeb "T-That's right! G-G-G-Go away, E-Evan! W-W-We don't w-want you h-h-here . . ."
    "Joebbels plucks up her courage and confronts the rude man."
    
    show hitora hat normal
    show joebbels normal
    with dissolve
    
    "But Adorofia Hitora silences her minister with a wave of her hand."
    hit "Joebbels. It's time."
    goeb "M-My Füühbar."
    
    show joebbels scared
    with dissolve
    
    "Hitora looks at her Propaganda Minister with lonely eyes and gently places a hand on her shoulder."
    goeb "I u-understand."
    me "Time? Time for what?"
    
    show hitora hat angry
    show evanbraun shock
    with dissolve
    play silsound5 "se/poke.ogg"
    
    hit "Fine, Evan. You win. I'll give you a chance."
    evan "Huh? You mean it? You're going to let me back into the circle?"
    "Does he mean the inner circle? So this guy was close to the Füühbar like that, way back when?"
    hit "But this is the last chance you'll get, you hear me?"
    
    show evanbraun evil
    with dissolve
    
    evan "Ha ha, sure thing, my cute little Füühbar. I'll be on my best behavior."
    "I scratch my head, a little dazed by the scenario."
    me "Sorry, I'm confused. Who the heck is this guy?"
    
    hide evanbraun
    with easeoutleft
    show hitora hat happy at right35
    show joebbels scared at left35
    with ease
    
    hit "I'm sorry, Commander Yamato. Thank you for helping with the ceremony today. That'll be all."
    me "Huh? You're dismissing me?"
    goeb "Y-You're excused. P-Please go enjoy t-the afternoon by y-yourself . . ."
    "One second I'm asked to work the day, now I'm being given time off . . . and all because of this Evan guy?"
    me "Then . . . if that'll be all . . ."
    
    play sound5 "se/walk.ogg"
    hide hitora
    hide joebbels
    with dissolve
    
    "Before I can even do some kind of salute, Hitora and Joebbels walk away, back towards Evan Braun."
    hit hat embarrassed "Okay, let's go . . ."
    evan evil "Ha ha, after you, my Füühbar."
    "I watch as the three of them stroll away across the parade grounds, back towards the dictator's motorcade."
    me "Well . . . that was weird . . ."
    "Adorofia Hitora is taking on Evan Braun as her guest. More than that, she's inviting him back into the inner circle?"
    me "Just what is going on here? Who was that chump?"
    
    stop music fadeout 3.0
    stop soundfx2 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc000071

#####################################################################################################################################################
#sc000071	-	Rommel and Guderian talk Evan / Avoid direct answers
#####################################################################################################################################################    
label sc000071:
    play sound5 "se/door2.ogg"
    play soundfx "se/room.ogg" fadein 3.0
    scene yamato_room
    with fade
    play music "music/chill.ogg"
    
    "Some time later, I wander over towards the barracks, bored and tired."
    "Returning to my lodgings to mull over today's events, I find the room already occupied."
    
    play silsound4 "se/silly4.ogg"
    
    gud determined "No way, the {i}Panzy III{/i} can't handle the strain on its suspension. We need to improve the {i}Panzy IV{/i} before that can happen."
    
    show rommel determined at right35
    show guderian determined at left35
    with dissolve
    
    "Guderian sits on the end of their bed with Rommel, both turning to me in mid-conversation."
    rom "Ahh, Commander Yamato. How are you?"
    me "I'm holding up well. What are you both chatting about?"
    
    show rommel normal
    show guderian normal
    with dissolve
    
    gud "Just some unimportant tank stuff. You wouldn't be interested."
    me "Well, if it's not important, maybe you can help me out?"
    "I place my kit-bag down on the floor and sit on my bunk, opposite the tank nuts."
    
    play silsound3 "se/poke.ogg"
    show rommel sad
    show guderian shock
    
    me "What do you know about Evan Braun? The guy just showed up today at the training grounds . . ."
    "They both make painful expressions after hearing that name."
    me "Do you know something I don't know?"
    
    show rommel normal
    show guderian normal
    with dissolve
    
    "With a collective sigh, they both avoid eye contact and stare off into the middle-distance."
    gud "Evan Braun is . . . well . . . Evan Braun is . . ."
    rom "Nnn. Yeah. He's . . . how to say it . . . Evan Braun."
    "They both nod at that as though it's a revelation."
    me "That's not really an answer. Who is that guy? Where did he come from?"
    
    show rommel sad
    with dissolve
    
    rom "Well, he's from Germania originally. And he has two dogs, both terriers."
    gud "Y-Yeah. And he likes sports, and clothes, and girls, and the movies. He's a model and a film star."
    me "So he's some kind of celebrity hunk? I see. What else?"
    gud "Nnnn. That's about it really . . ."
    "They're holding back, not letting on about anything too important."
    me "Come on, tell me more. I want to know who this guy is. How does he know the Füühbar?"
    
    show guderian determined
    with dissolve
    play silsound6 "se/silly6.ogg"
    
    gud "We're sorry Yamato. We really can't tell you anything more about him. Not without permission."
    me "What? Why not? And on whose permission?"
    rom "It's not our place to say. You should really ask the Füühbar."
    "The Füühbar? So Hitora told them not to say anything? No, she wouldn't waste her time doing that."
    "But . . . that guy did seem to really . . . cause a distraction earlier."
    "So is that it? He's related to the Füühbar in some way."
    me "I thought he was just some civilian punk, trying to cause problems during a medal ceremony."
    "It did surprise me that the {i}Goosetapo{/i} didn't sweep in and take him away, as well . . ."
    
    show guderian normal
    show rommel normal
    with dissolve
    
    gud "Sorry, Commander Yamato. Maybe we can talk about it some other time . . . just, not now . . ."
    me "That's okay. I guess the dictator is lucky to have loyal friends like you guys."
    rom "{size=-6}Please don't call us {i}'friends'{/i} . . . I'd never plot anything, but still . . .{/size}"
    "Anyway, it's bugging me. I might have to do some investigating of my own."
    "Who is this Evan Braun character? What does he want with the Füühbar? What was with that swooning yet hostile atmosphere?"
    me "I'm going to get to the bottom of this . . ."
    
    play sound4 "se/door2.ogg"
    
    "Standing up, I make my way to the door and head out to do some snooping."
    rom "Poor Commander Yamato . . . poor Hitora too."
    gud "It is what it is. Let's not involve ourselves in any gossip this time around."
    
    stop soundfx fadeout 3.0
    stop music fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc000072

#####################################################################################################################################################
#sc000072	-	Yamato sees Hitora+Evan date / Annoyed
#####################################################################################################################################################    
label sc000072:
    play soundfx "se/city.ogg" fadein 3.0
    scene day3
    with fade
    play music "music/facepalm.ogg"
    
    "As I try to get to the bottom of the {i}'Evan Braun mystery'{/i}, I decide to do a stakeout."
    "The more I can pick up from ordinary citizens and those around me, the better I can piece together the puzzle."
    
    play sound4 "se/walk.ogg"
    scene altberlin
    with dissolve
    
    "Walking through the streets of Altberlin on a sunny day, I take in the atmosphere of the city."
    "As always, banners are forcibly flying, fluttering red flags are hung, and the populace seems motivated to do its best."
    "Even though the country has been at war for a few months, support for the Germanian cause continues to remain strong."
    "But there's a new element to it . . ."
    
    play silsound2 "se/silly4.ogg"
    
    wom shock "Did you hear? He's released a new set of saucy shirtless photographs from a shoot he recently did."
    man happy "Damn, that guy really is bold. He's daring in his latest film too. What a cool rebel!"
    ow determined "I don't like to admit it . . . but a handsome devil like that . . . he gets the blood pumping."
    "The fascination over Evan Braun is reaching fever-pitch. T-shirts and mugs are being sold alongside action figures."
    "His face adorns compilation albums, magazine spreads and signed posters. The moviehouses are packed with adoring fans."
    me "It's ridiculous. This country should be focusing on the battles to come, not on some pretty playboy."
    "There's something fishy about the whole thing, and I need to find out what it's all about."
    
    stop music fadeout 3.0
    
    hit hat embarrassed "{size=-6}Stop it . . .{/size}"
    
    play soundfx3 "se/heart.ogg" fadein 3.0
    
    "Then I hear a gentle and familiar voice from nearby."
    
    play sound3 "se/walk.ogg"
    show hitora hat embarrassed at right35
    show evanbraun evil at left35
    with dissolve
    play music "music/winter.ogg"
    
    "Adorofia Hitora and Evan Braun appear, strolling along a nearby street, side by side, alone."
    evan "What's the matter? My joke wasn't that dirty."
    hit "It's embarrassing . . . that's why."
    "The Füühbar tries to bat away his teasing words, yet her face is flushed crimson."
    "Her cheeks are beet-red, her eyelashes are fluttering . . . I've never seen her look so discombobulated."
    evan "Ha ha, when did you become so docile? You never used to be so bothered by my attentions . . ."
    hit "Well . . . that was different. I wasn't {i}Oberster Befehlshaber der Vehrmaxt{/i} then . . ."
    "My heart begins pacing, watching the uncomfortable scene unfold. Why am I invested in something like this?"
    me "{size=-6}(I guess I didn't realize that murderous dictator could behave in such a feminine way . . .){/size}"
    "Heads turn as civilians gossip, fascinated by the Füühbar's sudden flagrant display."
    "After all, she's walking side by side with a celebrity hunk, in broad daylight. It's a juicy sight in these repressed times."
    me "{size=-6}(Adorofia Hitora, what do you think you're doing, spending time with that guy?){/size}"
    "Admittedly, it's making me a little jealous. He's making her behave in a way that I've never managed to make a girl do . . ."
    
    show evanbraun determined
    
    evan "Anyway, come on. I want to try on some tight shirts and then leave without paying for them."
    hit "If you want someone to pay for them, I don't mind . . ."
    
    play silsound4 "se/silly16.ogg"
    show evanbraun evil
    
    evan "Nah, I like winding up the shop staff. Besides, you're going to be paying for lunch, right?"
    hit "Fine . . . it can come out of my expenses."
    "What a jerk! I can't believe he's forcing my target to treat him to food. Then again, she can afford it . . . but still."
    
    play silsound5 "se/silly17.ogg"
    
    evan "Ha ha! That's my girl! Let's enjoy our date, just the two of us . . ."
    "D-Date? Did he say this was a date?!"
    
    stop soundfx3 fadeout 3.0
    play sound3 "se/walk.ogg"
    hide hitora
    hide evanbraun
    with dissolve
    
    "The couple soon disappear out of earshot, into the bustling crowds and I lose sight of them."
    "My heart rate begins to slow down and I try to calm myself, taking a slow breath."
    me "I don't know why . . . but that really annoyed me."
    "The two of them were on a date. They're dating . . . I can't understand it."
    me "Why does Hitora put up with his behavior? It's not like her to be so complacent . . ."
    "This whole turn of events is getting stranger and stranger."
    "Not to mention, it's putting my mission at risk. I should be sticking close to Hitora, not hiding like this . . ."
    "That Evan Braun . . . just who is he? Besides being the world's biggest jerk."
    me "I need to get to the bottom of this, and fast, before the Füühbar spends all her expenses on hotdogs and leather jackets."
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc000073

#####################################################################################################################################################
#sc000073	-	Joebbels+Goring+Everyone knows but you
#####################################################################################################################################################    
label sc000073:
    play soundfx2 "se/birds.ogg" fadein 3.0
    scene day2
    with fade
    play music "music/relax.ogg"
    
    "The mystery of Evan Braun's presence remains a frustration. Who is he? What does Hitora think of him?"
    me "Are they old friends? Childhood sweethearts? Does he have dirt on her? Is he trying to boost his celebrity profile?"
    "I just can't figure out their relationship. And I can sense I'm being pushed out at the same time . . ."
    "In the meantime, I try to busy myself with some work, reading frontline reports to take my mind off recent events."
    
    stop soundfx2 fadeout 3.0
    play soundfx "se/room.ogg" fadein 3.0
    scene corridor
    with dissolve
    play sound5 "se/walk.ogg"
    play sound4 "se/map.ogg"
    
    "Wandering the {i}Imperiumstag{/i}, I write up memos on recent engagements and study intelligence reports."
    me "Hmm . . . there's been a buildup around Saloon in Franzo recently . . . probably reworking the {i}Magnifique Line{/i} again."
    "From down the corridor, I notice two friends shooting the breeze."
    
    show joebbels sad at left35
    show goring pout at right35
    with dissolve
    
    goeb "I-It's so frustrating . . . I c-can't hold b-back anymore . . ."
    gor "Come on Joebbels, the Füühbar made us promise. It'll all be worth it in the end."
    "It seems like they're deep in conversation."
    
    play silsound5 "se/poke.ogg"
    show goring confused
    show joebbels scared
    with hpunch
    
    me "Hey guys, how's it going?"
    gor "Ahh, Commander Yamato! Don't creep up on people like that!"
    goeb "S-Sneaky barbarian . . ."
    "But I was standing right in front of them . . ."
    
    show joebbels normal
    show goring determined
    with dissolve
    
    me "What were you both talking about?"
    gor "Nothing in particular."
    "Goring pulls a stern expression."
    me "What is it?"
    goeb "N-Nothing."
    "Joebbels's face, likewise, is an enigma, as her eyes dart to and fro."
    me "Anyway, if you're not busy, I wanted to talk to you both."
    
    show goring pout
    
    gor "You're not going to ask for the twenty marks you loaned me, are you? Because they're gone. You're not getting them back."
    "Greedy girl. That's the last time I lend her any money for the vending machine."
    me "Actually, I wanted to ask you both about Evan Braun."
    
    play silsound3 "se/silly8.ogg"
    show joebbels scared
    show goring determined
    
    goeb "D-Danger. D-D-Danger."
    me "Huh?"
    gor "Sorry Yamato, we can't tell you anything. Boss's orders."
    "Boss? She must mean Hitora."
    me "Why not? Why is everyone being so cautious around that guy?"
    goeb ". . . . . . . . ."
    gor ". . . . . . . . ."
    "Silence. It doesn't look like I'll be getting a straight answer out of these two, either."
    me "Fine. Forget I asked."
    "So much for my detective skills."
    goeb "Y . . . Y . . ."
    me "Hmm? What is it?"
    
    show goring pout
    
    goeb "Y-You know . . . s-sometimes to s-solve a case . . . you h-have to g-go back to the s-start."
    "The start . . . could she mean that I have to return to the training grounds? Or maybe ask Evan Braun himself?"
    "Or . . . there's always checking in on the Füühbar and finding out first-hand too. Ask the victim, as it were."
    me "Go back to the start, huh . . ."
    
    play silsound2 "se/silly9.ogg"
    show goring confused
    
    gor "Joebbels, you've already said too much."
    goeb "I k-know . . ."
    gor "Sorry Yamato, we really have to go now."
    goeb "G-Good luck . . . Y-Yamato."
    "Rather sweetly, the little Propaganda Minister cheers me on in my quest. Although, it would be easier if she just told me."
    
    play sound6 "se/walk.ogg"
    hide joebbels
    hide goring
    with dissolve
    
    "Joebbels and Goring then scamper away before I can ask anything further."
    me "This problem with Evan Braun is a real headscratcher."
    "Nobody seems to be at liberty to speak about it. I know this country doesn't have freedom of speech, but still."
    me "Maybe it's time I asked the Füühbar herself . . ."
    
    stop soundfx fadeout 3.0
    stop music fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc000074

#####################################################################################################################################################
#sc000074	-	Rinni and Vitalians talk about Evan
#####################################################################################################################################################    
label sc000074:
    scene black
    with fade
    
    $ mouse_visible = False
    show expression Text(_("Meanwhile, in the central nation of Vitalia . . ."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx2 "se/sea.ogg" fadein 3.0
    scene day3
    with fade
    play music "music/rinni.ogg"
    
    "Faraway, at the Villa Dorlonia in Rhome, the leader of Vitalia meets with her top general . . ."
    mussorin hat determined "Finally, it's Vitalia's time in the spotlight!"
    "Benita Mussorinni, otherwise known as Rinni, ponders the state of Europa."
    bad hat normal "I wonder where Graziani is with our snacks . . ."
    "Marshal Petra Badoglio stands by her side, keeping an eye on the entrance to the villa for any sign of Marshal Graziani."
    mussorin hat moe4 "Hey, Badoglio, have you heard the latest gossip?"
    bad hat determined "No, {i}Il Douché{/i}."
    mussorin hat moe3 ". . . . . . . . ."
    bad hat determined ". . . . . . . . ."
    mussorin hat moe3 ". . . . . . . . ."
    "An awkward silence fills the gap."
    bad "Did you want me to ask you about it, {i}Il Douché{/i}?"
    
    play silsound4 "se/silly27.ogg"
    
    mussorin hat moe2 "Yes! I really can't wait to tell someone. It's super amazing extraordinary news. I might burst if I don't get it out!"
    bad hat normal ". . . . . . . . ."
    
    play silsound3 "se/silly24.ogg"
    
    mussorin "Badoglioooooo!"
    bad hat determined "Very well. What is the latest gossip, {i}Il Douché{/i}?"
    "For now, the Marshal will indulge her leader."
    mussorin hat determined "Evan Braun has come back to Altberlin!"
    bad hat normal "Who?"
    mussorin hat embarrassed "Geez, don't you know anything? He's that famous movie star and model."
    bad "I'm a little out-of-date on my celebrity knowledge, {i}Il Douché{/i}."
    "When you're a busy Marshal, cleaning up after your {i}Douché{/i} every day, there's not much time to read up on pop culture."
    mussorin hat moe3 "You're so old-fashioned sometimes. It's embarrassing."
    bad "Yes, {i}Il Douché{/i}. I'll work on it."
    "Rinni taps her foot on the ground impatiently as she tries to get her gossip out."
    mussorin hat determined "Anyway, he came back to Altberlin. You know, he's the one that Hitora used to . . ."
    bad hat shock "Ahh, I know him! So he's the one that did all those things?"
    mussorin "Precisely."
    "They both pull concerned faces."
    bad hat determined "I feel sorry for the Füühbar, having to deal with a man like that."
    
    play silsound2 "se/silly18.ogg"
    
    mussorin hat moe4 "Eh? But I think he's kinda dreamy-looking. A big sweaty Germanian hunk."
    bad hat shock "Why does he have to be sweaty?!"
    mussorin "Don't you think he has some good qualities?"
    bad "Good qualities?"
    "Badoglio ponders that question."
    mussorin "What's your type, Badoglio? What kind of guy do you go for? Or maybe, it's a girl?"
    bad hat determined ". . . . . . . . ."
    "It seems she's refusing to answer."
    
    play silsound4 "se/silly20.ogg"
    
    mussorin hat moe3 "Boring."
    bad "I still feel sorry for Adorofia Hitora, even if she is a ruthless dictator. Evan Braun isn't a nice person."
    "She obviously doesn't think very highly of the man."
    mussorin hat normal "Well, what can we do about it?"
    bad hat normal "Nothing much, I suppose."
    
    play sound3 "se/walk.ogg"
    
    graz normal "What are you both talking about?"
    "Rodolphia Graziani, {i}Commander-in-Chief of the Royal Army General Staff{/i}, returns, carrying a bundle of snacks in her arms."
    mussorin hat moe4 "Ah! Graziani! You're back!"
    graz determined "I'm sorry {i}Il Douché{/i}. I couldn't find any peanut butter brittle. All they had were these gooey peanut bars."
    "Holding her arms up, she shows off the brightly colored wrapping on all the products she bought."
    bad "What about my crinkle-cut potato chips?"
    graz moe "No, sorry. They were all out."
    mussorin hat moe3 "Well, what did you pick up?"
    graz normal "They had . . . barbina, bigoli, capellini, pinci, fusilli, spaghetti, cavatappi, ditalini, penne, fiori, gigli . . ."
    
    play silsound2 "se/silly5.ogg"
    
    mussorin hat moe2 "Gah! Those are all just different kinds of pasta! Where's all the junk food?"
    bad hat determined "Maybe the store is rationing things like that now?"
    "Mussorinni throws her arms up in the air, in standard dramatic fashion."
    mussorin "This is unacceptable! {i}Il Douché{/i} without snacks is like a fish without a bicycle!"
    bad hat normal "That doesn't really work . . ."
    "The leader of Vitalia faces her own troubles, as Evan Braun becomes the focus of Europa's hot gossip."
    
    stop music fadeout 3.0
    stop soundfx2 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc000076

#####################################################################################################################################################
#sc000076	-	Confront Hitora / She avoids giving answers
#####################################################################################################################################################    
label sc000076:
    play soundfx "se/city.ogg" fadein 3.0
    scene altberlin
    with fade
    play music "music/waltz.ogg"
    
    "As I wander the streets of Altberlin, I keep my gaze low and my hands in my pockets."
    "The events of the past week have confused me to no end. It's been very odd."
    me "Who is this Evan Braun? Why is he here? Why won't anybody give me concrete answers?"
    "There's definitely something fishy going on."
    "After all, how can I take out my target if she's constantly surrounded by celebrity intrigue?"
    me "{i}Detective Yamato is on the case!{/i} Just kidding . . ."
    
    stop soundfx fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    play sound4 "se/knock.ogg"
    scene black
    with fade
    queue sound4 "se/door3.ogg"
    play soundfx3 "se/room.ogg" fadein 3.0
    scene warroom
    with fade
    
    "Some time later, with a light knock on the door, I step into Hitora's office in the {i}Imperiumstag{/i}."
    me "My Füühbar. Can I speak with you?"
    
    show hitora hat normal
    with dissolve
    
    "I find Adorofia Hitora by herself, idly gazing out of the window."
    "A magazine lies at her feet, half-read, the page opened to a self-help section regarding men."
    hit "Ahh Commander Yamato. What is it?"
    
    show hitora hat worry
    
    me "Evan Braun's not in here, is he?"
    
    show hitora hat embarrassed
    with dissolve
    
    hit "No, not anymore. He went back to his hotel for the day."
    "So he was here earlier . . ."
    
    show hitora hat normal
    with dissolve
    
    me "My Füühbar . . ."
    "I begin my question but abruptly cut it short."
    hit "Hmm? What's wrong? Did you want to ask me something?"
    me "I just realized . . . I can't really ask that of you."
    hit "It's about Evan isn't it?"
    me "Yeah . . ."
    "I sit down on the arm of a plush, leather chair and compose my thoughts."
    me "I want to know who he is to you. I've asked everyone else but can't seem to get a straight answer."
    "Twiddling my thumbs, I absentmindedly gaze off into the distance."
    me "He's taking up all your time, it's put the inner circle on edge, all the townsfolk are talking about it . . ."
    me "I don't know. I feel like I'm being kept out of the loop."
    "Hitora keeps a straight face as I list off my concerns."
    me "You're not going to tell me either, are you?"
    hit ". . . No."
    me "Why not?"
    
    show hitora hat angry
    with dissolve
    
    hit "It's important that Evan Braun is given our full attention. That's all I have to say about it."
    me "{i}'Full attention'{/i}? What do you mean by that? Why is this guy taking up so much of your time?"
    "They're out on dates and doing public events, while the rest of the team are being distant . . ."
    hit "I'm the Füühbar. It's my duty to act in the best interests of our nation. This is one of those times."
    "{i}'Best interests of our nation'{/i}? What kind of lame excuse is that?"
    hit "This is something that has to happen. Please Commander Yamato, just let it be."
    me "I don't understand. Why can't you just tell me what's going on? I'm . . . meant to be your bodyguard, aren't I?"
    "This is frustrating beyond measure."
    
    play silsound4 "se/silly9.ogg"
    show hitora hat worry
    
    me "This prettyboy with an attitude just shows up and I'm suddenly pushed out of the frame?"
    
    show hitora hat angry
    with dissolve
    
    hit "Are you sure you're not just jealous?"
    me "J-Jealous? Me? Ha! What's there to get jealous about . . ."
    "I can't be jealous . . . I'm only concerned about my mission, that's all . . ."
    
    stop music fadeout 3.0
    
    hit "I won't tell you anything more. You'll just have to believe in me."
    me "So then, what you're saying is . . ."
    
    jump choice_hitoraevan
    
label choice_hitoraevan_answer1:
    play music "music/winter.ogg"
    show hitora hat worry
    
    me ". . . you don't trust me."
    
    show hitora hat moe1
    
    hit "Stop being so dramatic. I just want you to trust me on this."
    me "But you can't trust me enough to just tell me?"
    "That's it, isn't it? After everything I've done for these guys . . ."
    "I mean, sure, I'm betraying them with the resistance and everything, but still . . . it's frustrating."
    
    jump choice_hitoraevan_continue
    
label choice_hitoraevan_answer2:
    play music "music/winter.ogg"
    show hitora hat worry
    
    me ". . . I'm only one of your goons."
    hit "Why are you saying stuff like that? You know it's not true."
    me "Then why can't you just say it? Tell me. Tell me what Evan Braun means to you."
    me "Why are you spending so much time with him? Is he blackmailing you or something?"
    hit "It's not like that . . ."
    me "Then what is it? Why has he got everyone so spooked?"
    
    show hitora hat embarrassed
    with dissolve
    
    hit "It's . . . complicated."
    "If this keeps up, I'll just go and ask that prettyboy rebel myself."
    
    jump choice_hitoraevan_continue
    
label choice_hitoraevan_continue:
    show hitora hat normal
    with dissolve
    
    "An awkward silence fills the air between us."
    hit "I'm sorry Yamato, I have to go. There's an event this evening I need to prepare for."
    
    show hitora hat worry
    
    me "Yeah. Just go."
    "I shouldn't act out like this. I might jeopardize my mission if I say too much. But . . ." 
    ". . . but, it's bothering me too much . . ."
    
    show hitora hat normal
    
    hit "I need you to promise me something."
    me "Promise?"
    
    show hitora hat angry
    with dissolve
    play silsound3 "se/silly27.ogg"
    
    hit "I want you to promise that you'll leave Evan Braun alone. I don't want you going near him."
    me "What? What kind of promise is that?"
    hit "Promise me, Commander Yamato. As my loyal bodyguard."
    "I get to my feet in frustration and confront the dictator, face to face."
    me "Adorofia Hitora, if he's blackmailing you in some way, I'm going to go teach him a lesson . . ."
    hit "I can't have you doing that."
    me "Well, what else am I going to do? Nobody will tell me what the heck is going on."
    
    play silsound6 "se/silly6.ogg"
    show hitora hat moe1
    
    hit "Promise me. Swear you won't go after Evan Braun. Swear on your Füühbar's life."
    me "No . . . I'm not going to make a promise like that."
    "This situation is crazy enough without swearing like that. What's with this conspiracy?"
    
    show hitora hat angry
    with dissolve
    play silsound5 "se/silly11.ogg"
    
    hit "Then you leave me no choice. You will take a week's leave. Go on sabbatical and leave Altberlin for a few days."
    me "At a crucial time like this? I can't take a holiday."
    hit "You don't have a say in the matter. This is a directive from your Füühbar. You're going on leave."
    "Huh? I'm being sent away? Wait, it's not so that Evan Braun guy can get settled in, is it?"
    "Don't tell me he's some kind of brilliant advisor or bodyguard, here to take my place? So he's after my job then?"
    "My mission is going to be compromised . . . my place here."
    me "You can't do this to me! You need me, here, helping to win this war! We haven't even started on Franzo . . ."
    hit "We'll survive without you for a few days. And when you come back, everything will be clear."
    "Hitora gives me that ultimatum, as the sun outside begins to retreat behind the clouds."
    
    show hitora hat normal
    with dissolve
    
    hit "I have to go. You'll understand why I'm doing this, one day . . ."
    "I fail to say anything in response, but give a meek nod in farewell."
    
    play sound4 "se/walk.ogg"
    hide hitora
    with dissolve
    
    "With that, the Füühbar heads out into the corridor, off to who knows where."
    me "Evan Braun . . . Adorofia Hitora . . . my mission . . . what does it all mean?"
    "And why does everyone in this city seem to know about this weird situation but me?"
    "Something's not right about this {i}'Evan Braun'{/i} guy, I know it."
    me "But, if I'm being sent away, maybe it's my chance to find out . . ."
    "If Hitora won't be honest about it, I'll have to do some investigating elsewhere . . ."
    "With a new determination, I make my plans and head out to go pack my things."
    
    stop soundfx3 fadeout 3.0
    stop music fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc000075

#####################################################################################################################################################
#sc000075	-	Meanwhile in Amerika #2 - Norda / Evan
#####################################################################################################################################################    
label sc000075:
    scene black
    with fade
    
    $ mouse_visible = False
    show expression Text(_("Meanwhile, in the lands of United Amerika . . . "), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx "se/room.ogg" fadein 3.0
    scene whitehouse
    with fade
    play music "music/freedomfries.ogg"
    show agent normal at left3
    show roosevelt annoyed at right3
    with dissolve
    
    agent "Ms President! We've received intel that Evan Braun, an old flame from Hitora's past, is back on the scene."
    fdr "What are you recapping for? This isn't a soap opera, you know . . ."
    agent "This is important Ms President. This could tip the balance of power in Europa."
    
    play silsound4 "se/joke.ogg"
    show roosevelt happy
    
    fdr "Very well. Be sincere. Be brief. Be seated. {i}Badum-tish!{/i}"
    agent "That pun was terrible."
    
    play silsound3 "se/silly20.ogg"
    show roosevelt bored
    
    fdr "Just get on with it Larry."
    agent "I believe we can make use of this Evan Braun situation and steer Germania back in the right direction."
    fdr "I thought I made it clear before. We're non-interventionists. Let's just kick back and have some {i}brewski's{/i} instead."
    "The secret agent looks at his leader with a disappointed expression."
    
    play silsound2 "se/silly28.ogg"
    show roosevelt moe1
    
    fdr "Fine. Brief me in."
    
    show roosevelt normal
    with dissolve
    
    agent "If this Evan Braun character can win back Hitora's heart, we might be able to work something behind the scenes."
    agent "He spent a lot of time here in Amerika. We have direct contacts, in the fashion and film industries, who can help."
    
    play silsound4 "se/silly18.ogg"
    show roosevelt moe2
    
    fdr "Wait. Evan Braun . . . as in {i}that{/i} Evan Braun? The famous celebrity?"
    agent "Precisely."
    
    show roosevelt normal
    with dissolve
    
    fdr "So . . . he's the one that did all of that stuff with Adorofia Hitora in the past?"
    agent "Yes. We have a full brief if you're interested."
    
    play silsound2 "se/silly22.ogg"
    show roosevelt moe1
    
    fdr "Ugh! I don't want to read anything. Can't you explain it to me in baseball form?"
    agent "That sounds unnecessarily convoluted and painful."
    
    show roosevelt happy
    with dissolve
    
    fdr "The only thing we have to fear is reading complicated documents!"
    agent "You might want to work on that quote. It's not very inspiring . . ."
    
    show roosevelt normal
    with dissolve
    
    "Getting more serious, Roosevelt skims over the dossier before placing it on her desk."
    fdr "Still, someone like him has that much influence over the Füühbar of Germania?"
    fdr "I guess she really is just a foolish young woman after all . . ."
    agent "A young woman that annexes other countries and has one of the largest standing armies on the planet."
    
    show roosevelt annoyed
    
    fdr "And when you see a rattlesnake poised to strike, you do not wait until she has struck to crush her."
    agent "Ms President . . ."
    "Could it be that Roosevelt is going to get serious for once? Has the war, at last, come to United Amerika?"
    
    play silsound4 "se/silly18.ogg"
    show roosevelt moe2
    
    fdr "Ahh! I forgot! I'm meant to be attending a big dance at a charity auction this evening!"
    agent "Eh? You forgot that was on your schedule?"
    
    show roosevelt evil
    with dissolve
    
    fdr "I love a good dance. The big band, the food, the cute guys and gals. And all the silly dance moves too!"
    fdr "{i}The Lindy Hop{/i}, {i}West Coast Swing{/i}, {i}Jitterbug{/i} . . . Ahaha! {i}Jitterbug{/i}! What does that even mean anyway?"
    agent "Wait a minute, what about Evan Braun?"
    
    show roosevelt happy
    
    fdr "Ahh, Larry. It sure is fun to be in the same decade with you. Come on. Let's go dancing!"
    
    play sound4 "se/dash.ogg"
    hide roosevelt 
    with easeoutright
    
    "With that, Roosevelt bounds out of the room, ready to dance."
    
    show agent normal at center 
    with ease
    
    agent "And to think, she used to be in a wheelchair . . ."
    fdr happy "Are you coming Larry?"
    agent "Yes . . . Ms President."
    "And so, Amerika puts off fighting for another day."
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc000077

#####################################################################################################################################################
#sc000077	-	Meet with Mannerheim, suggests asking biggest gossip
#####################################################################################################################################################    
label sc000077:
    play soundfx2 "se/wind.ogg" fadein 3.0
    scene sky_snow
    with fade
    play music "music/soviagrad.ogg"
    
    "In my desperation to find out the truth about Evan Braun, I make way north."
    "Passing through the glens and frozen tundra, I arrive in Helsin, Finbard, at Mannerheim's encampment."
    
    play sound2 "se/walk.ogg"
    
    "Escorted by guards, we approach a single train cart, resting on the tracks near to a defensive line in the south."
    "This is Mannerheim's carriage. From here, she plans her potential assaults, plots the enemy position and devises her schemes."
    
    stop music fadeout 3.0
    play sound4 "se/metal_steps.ogg"
    
    "Coming up the metal steps, I clear my throat and enter through the heavy metal door."
    
    stop soundfx2 fadeout 3.0
    play sound4 "se/doorslide.ogg"
    scene black
    with fade
    play soundfx "se/room.ogg" fadein 3.0
    
    mann determined "Hmm? Who is it? I'm very busy right now . . ."
    
    play music "music/bravery.ogg" fadein 3.0
    $ mouse_visible = False
    scene cg_mannerheim
    with dissolve2
    $ mouse_visible = True
    
    mann determined "Commander Yamato Yamamoto of Zipangu? This is a surprise."
    me "It has been a while since we last met."
    "For a few seconds, I simply stand in a stunned silence."
    mann normal "What is it?"
    me "Ahh . . . nothing. It's just, I've never seen you with your glasses on."
    mann "I'm only partially shortsighted. So I can do without them most of the time."
    "The serious girl turns away from her maps for a moment to face me, adjusting her spectacles as they rest on the bridge of her nose."
    me "We haven't spoken much since the {i}Wintertime War{/i}. How are things faring?"
    mann "Enough small talk. What are you doing here?"
    "She's a very direct girl."
    me "You always struck me as straightforward and calculating. I was hoping you might be able to give me an honest answer."
    mann determined "An honest answer? About what?"
    me "What can you tell me about Evan Braun?"
    
    play silsound3 "se/silly21.ogg"
    
    "The Marshal of Finbard pulls a disconcerted face."
    mann moe "Ahh. You're opening a can of worms there."
    me "Please. Nobody else I know on this continent is being honest with me. I can't work out why he holds such sway over Hitora."
    mann "That girl. All she does is make people worry . . ."
    "With a sigh, Mannerheim puts her hands in her pockets and looks through the carriage windows, to the south."
    "Dark clouds on the horizon bring a cold wind from the east, as they pass over the ridges and and snow dunes."
    mann determined "I'm afraid I can't help you with your quest for information. Beyond some basic answers anyway, which I assume you have."
    me "He likes dogs and movies. I found out that much."
    mann happy "Heh! You really aren't much of a detective, are you?"
    
    play silsound4 "se/silly17.ogg"
    
    me "At least portions of my homeland haven't been annexed."
    "The Marshal of Finbard looks at me with a glare."
    me "Sorry, that was a bit harsh."
    mann determined "It's okay. I'm made of sterner stuff. Besides, the reality of the situation is far crueller than anything you can say."
    "The Finbardish really did lose everything in the {i}Wintertime War{/i}. Betrayed, abandoned and forced into a bitter peace."
    me "I was told that Germania has always been a friend to Finbard . . ."
    
    play silsound3 "se/silly26.ogg"
    
    mann moe "Don't remind me. That jumped-up corporal even crashed my birthday . . . she couldn't wait to give us guns and men."
    me "Still, do you really trust Iosefina Starin to keep her word?"
    "Mannerheim avoids eye contact and rests a hand on one of the maps strewn across the table."
    mann "What kind of cruel fate is this? Forced to choose between two genocidal girls without a shred of decency between them."
    me "I know the feeling . . . well, sort of . . ."
    "The Marshal smiles for a moment before letting the expression slip away."
    mann normal "Like I said, I can't help you with your quest. But . . ."
    "She hesitates."
    mann ". . . but perhaps there's someone who would be willing to help you. The biggest gossip in all of Europa."
    me "Really? That would be great. Where do I find this person?"
    "Mannerheim turns and points to the south, across the border, to the lands of Sovia Major."
    me "Wait, you don't mean . . ."
    mann determined "Who better to give you an honest answer than Adorofia Hitora's sworn archenemy and part-time friend?"
    "Does Iosefina Starin really hold the key to this Evan Braun mystery? That crazy girl?"
    "I guess there's only one way for me to find out."
    me "Thank you Mannerheim. I promise when the time comes, I'll return the favor."
    mann "Be careful Commander Yamato. Don't make promises you can't keep."
    "The Marshal of Finbard turns away from me and back to her maps, promptly ending our meeting."
    "I look out the window, in the direction of Moskva, the cold breeze blowing against the glass."
    me "Let's end this wild goose chase already . . ."
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc000079

#####################################################################################################################################################
#sc000079	-	Meet with Starin, gossips about Evan / Hitora
#####################################################################################################################################################    
label sc000079:
    scene black
    with fade
    
    $ mouse_visible = False
    show expression Text(_("Meanwhile, Yamato continues his journey into the east . . ."), size=30, yalign=0.5, font="font/hussar.otf", color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=None) as textoverlay with dissolve
    pause 2.0
    hide textoverlay with dissolve
    pause 0.3
    $ mouse_visible = True
    
    play soundfx "se/cave.ogg" fadein 3.0
    scene starinbase
    with fade
    play music "music/facepalm.ogg"
    
    "My quest to discover the true nature of Evan Braun has led me here, to the underground lair of Iosefina Starin."
    "Having trekked across the snowscapes of northern Europa, I passed into the mountains and caves of Moskva."
    "There were half a dozen booby traps, a labyrinth, trials and tribulations, and locked doors to pass through."
    me "Man, what was with those riddles at the end? And that crazy old man on the rope bridge over the lava . . ."
    "But finally, I'm here."
    
    play sound5 "se/walk.ogg"
    
    "As I head further into the dark chamber, I overhear an excited conversation."
    
    show starin fur moe2 at left35
    show zhukky hat embarrassed at right35
    with dissolve
    play silsound4 "se/silly8.ogg"
    
    star "Zhukky! I want another mug of hot cocoa!"
    zh "But m'lady, you've already had twelve today. And you've only just had your breakfast."
    "I stumble across a domestic dispute between the leader of Sovia and her top commander."
    
    play silsound4 "se/silly19.ogg"
    show starin fur moe1
    show zhukky hat moe1
    
    star "But {i}Starinbucks{/i} have a new blend! {i}The Triple Cinnamon Orangemint Almondmilk Cocoacream Americhococanalatte!{/i}"
    
    show starin fur moe4
    show zhukky hat determined
    
    zh "No. Too much caffeine is bad for your system."
    
    play silsound2 "se/silly13.ogg"
    show starin fur cry
    
    star "Zhukky! You meanie! Don't make me purge you too!"
    "They really do act like sisters. Maybe they are related? I mean, it wouldn't be the weirdest thing going on around here."
    
    play sound5 "se/walk.ogg"
    show starin fur normal
    show zhukky hat normal
    with dissolve
    
    "Stepping out from the shadows, I make myself known."
    me "Iosefina Starin, Iorgina Zhukky, I need your help."
    star "Eh? Commander Yamato Yamamoto? What are you doing here? Have you come to die?"
    me "I've come to ask you a personal question. You're my last hope . . ."
    
    show zhukky hat angry
    
    zh "Do you want me to turn him into an ice block, m'lady?"
    
    show starin fur angry
    show zhukky hat determined
    
    star "Bad Zhukky! We can't turn away Commander Yamato when he needs our help. Plus he's a real cutie!"
    zh "Forgive me m'lady. But he does work for the Füühbar of Germania."
    
    show starin fur happy
    with dissolve
    
    star "Mmm, that's true. Then again, it's not like our countries are at war so we don't need to hurt him . . . yet."
    "That {i}'yet'{/i} is somewhat ominous."
    
    show starin fur moe1
    show zhukky hat normal
    with dissolve
    
    "Turning to me with a sweet smile, the leader of the Union of Sovia gives me her full attention."
    star "Go ahead, cutie-pie!"
    me "I want you to tell me about Evan Braun. I want to know who he is and what he means for Germania."
    
    show starin fur normal
    with dissolve
    
    star "Eh? Evan Braun? I haven't heard that name in a while . . ."
    zh "Indeed."
    
    play silsound5 "se/silly8.ogg"
    show starin fur moe4
    show zhukky hat moe1
    
    star "Don't tell me! He came back to Altberlin?"
    me "He arrived earlier in the week. Ever since, everyone's been acting strange and won't tell me what's going on."
    me "Even Hitora won't talk to me about it . . ."
    
    stop music fadeout 5.0
    show starin fur normal
    show zhukky hat determined
    with dissolve
    
    "I try not to let the sadness ring in my voice, but my low tone gives it away somewhat."
    star "Hmm. Well, that's to be expected . . ."
    
    show starin fur insane
    show zhukky hat angry
    with dissolve
    play silsound3 "se/silly17.ogg"
    
    star ". . . after all, Evan Braun is Adorofia Hitora's one true love."
    
    play sound4 "se/heart.ogg"
    
    "My heart begins to beat rapidly upon hearing those words. I don't know why . . . maybe it's the stress."
    
    play music "music/history.ogg" fadein 3.0
    
    me "Eh? What did you say? I don't think I heard it properly . . ."
    star "Of course you did. Evan Braun is Hitora's boyfriend. Or, he was, about two years ago."
    "Hitora's boyfriend? Her one true love? That's who this guy is?"
    
    show starin fur normal
    with dissolve
    
    star "They used to be inseparable. They really were the original power couple."
    "A sinking feeling in my gut begins to hang, feeling heavy, as I listen to this new information."
    star "I remember when they first appeared together, at an olympic tournament . . ."
    
    scene black
    with dissolve
    
    star fur normal "It was a few years ago now. I can still see them clearly . . ."
    
    play soundfx4 "se/cheer.ogg" fadein 5.0
    scene flashback2
    with dissolve
    
    "From the stands of the {i}Olympiadastadion{/i} in Altberlin, the crowds go wild for the couple in the royal box."
    "The dictator of Germania, Adorofia Hitora, and her close associate, Evan Braun, inspire awe and confidence."
    evan evil "How are you liking the games, my Füühbar?"
    hit hat happy "Oh Evan! It's marvellous! All these people, cheering on our athletes. We truly are a great nation again."
    evan "And it's because of us, babe. It's all because of us."
    "The commentators in the press box have a field day, writing about the young, hot couple, watching over the spectacle."
    hit "Oh Evan! I'll cherish you forever and always!"
    "The two lovebirds hold hands quietly as the events begin below."
    
    play silsound6 "se/poke.ogg"
    
    hit hat angry "Hey wait a minute . . . what's that Amerikan sprinter doing? Somebody stop her!"
    
    stop soundfx4 fadeout 3.0
    scene black
    with dissolve
    scene starinbase
    show starin fur normal at left35
    show zhukky hat normal at right35
    with fade
    
    star "They were never officially an item. She's the Füühbar after all. But they really were perfect for one another."
    me "But . . . what happened? Why aren't her and Evan together anymore?"
    
    show starin fur angry
    
    star "I don't know the answer to that. But I know it drove Adorofia Hitora to annex Czexa."
    "Huh? That's what started this whole situation in Europa, with the {i}Alliance{/i} and Germania? Hitora got dumped?"
    star "If he's back in Altberlin, it can only mean trouble. They didn't end things very well. It's been rocky ever since."
    
    show zhukky hat angry
    
    zh "It's likely he's stringing her along so he can hurt her again. He's got a reputation as a womanizer, you see."
    zh "Or maybe it's related to her power or the war in some way . . . it's uncertain."
    me "And I'm only just hearing about this now . . . man, I could have helped her . . ."
    "It would have been easier to stay in her good books then."
    
    show starin fur normal
    with dissolve
    
    star "You never know. He could be serious this time. Maybe flying all over the world and becoming a star didn't fulfill him."
    "But, that must mean that . . . if he's back . . . and Hitora is spending all this time in his company . . ."
    me "So . . . he's going to claim her heart again . . ."
    
    stop music fadeout 3.0
    show starin fur moe1
    show zhukky hat normal
    with dissolve
    play silsound4 "se/silly9.ogg"
    
    star "Aww, don't worry Yamato! You can always bunk up with me and Zhukky. We'll take care of you!"
    me "Eh?"
    
    play music "music/facepalm.ogg"
    show zhukky hat determined
    
    zh "It's comfortable here. M'lady will take care of your every need."
    star "You can forget all about Hitora. We can have hot cocoa and purge dissidents every day."
    me "Well . . ."
    
    jump choice_starinevan
    
label choice_starinevan_answer1:
    me "That sounds tempting . . ."
    "A quiet life in the mountains of Moskva, relaxing with these white-haired Sovian goons."
    "Yeah right . . . did you forget that Starin is completely crazy?"
    
    play silsound2 "se/silly10.ogg"
    show starin fur moe4
    show zhukky hat moe1
    
    me "Although, I'm going to have to decline. Sorry."
    
    show starin fur angry
    
    star "Huh? Why?"
    
    jump choice_starinevan_continue
    
label choice_starinevan_answer2:
    play silsound2 "se/silly10.ogg"
    show starin fur moe4
    show zhukky hat moe1
    
    me "There's no way I'm doing that. I have to decline."
    
    show starin fur angry
    
    star "Huh? Why not?"
    
    jump choice_starinevan_continue
    
label choice_starinevan_continue:
    me "It's true that things are difficult right now. The Füühbar didn't trust me enough to tell me about her past."
    "That's fine. I'm new here, and in some small way, she was probably just trying to protect herself."
    me "But, I'm not going to abandon her now when she needs a bodyguard more than ever."
    "And I still have a mission to carry out . . . some day . . ."
    
    play silsound4 "se/silly20.ogg"
    show zhukky hat bored
    
    zh "Ahh, he chose {i}'the friendzone route'{/i}."
    me "No, I haven't chosen any route. Not yet, at least. And not intentionally . . ."
    star "Oh, you really are indecisive! You big foreign dummy!"
    
    show zhukky hat normal
    show starin fur normal
    with dissolve
    
    "With a sigh, Starin pulls a bored expression."
    star "Well, never mind. You seem to have made up your mind."
    me "Thank you for telling me all this. I really appreciate it."
    
    show zhukky hat angry
    
    zh "Go on. Go back to Altberlin and finish this thing."
    
    show starin fur moe1
    
    star "And if it all blows up in your face, the offer still stands. Zhukky will keep a mug in the cupboard with your name on it."
    
    show zhukky hat bored
    
    zh "Yes, I'll do that apparently."
    "I never thought I'd be getting support like this from a girl that once threatened to crush my head."
    me "I need to confront Evan Braun and catch him out. I'll have that guy tell me himself what Hitora means to him."
    "Despite everything she said, I'm going to have to disobey a direct order."
    "With a new found determination, I begin the long journey back to Altberlin."
    
    play sound3 "se/walk.ogg"
    stop soundfx fadeout 3.0
    stop music fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc000080

#####################################################################################################################################################
#sc000080	-	Confront Evan / Get ignored / Consider leaving
#####################################################################################################################################################    
label sc000080:
    play soundfx "se/city.ogg" fadein 3.0
    scene day2
    with fade
    play music "music/chill.ogg"
    
    "After many hours on the road between Moskva and Altberlin, I arrive in the Germanian city."
    
    scene altberlin
    with dissolve
    
    "I had a lot of time to think as I flew, drove and went by train. Over the days, I've formulated a new plan."
    me "I'll have to catch Evan Braun in the act, womanizing, lying . . . trying to weasel his way in . . ."
    "It'll be difficult getting him away from the Füühbar. In order to achieve it, I've had to be rather underhanded."
    "Recruiting Joebbels to help me out, a letter was sent to Evan Braun, calling him out on business."
    "Even if the Propaganda Minister is loyal to Hitora, she'd rather see the back of Evan again . . ."
    
    play sound5 "se/brush.ogg"
    
    "Hiding out of sight behind a corner, I wait patiently for the prettyboy to appear."
    
    play sound4 "se/walk.ogg"
    
    "Then, I hear the sound of footsteps falling on concrete, and that dashing villain arrives."
    
    show evanbraun happy
    with dissolve
    
    evan "Hello? I got your letter, Ms Liefenstahr. I'm ready for the gravure photoshoot."
    "I knew he'd take the bait. What an arrogant piece of . . ."
    evan "Are you hiding? Come on, don't play hard to get. I've heard what you're like on shoots like this."
    evan "Come give your favorite model a kiss on the cheek. You saucy girl, you. You know you love it."
    "What a creep . . ."
    
    play sound2 "se/walk.ogg"
    show evanbraun normal
    
    "Emerging out of my alcove, I confront Evan Braun head on."
    evan "Huh? You're that Zipanguese wimp. What's going on? Where's Reni Liefenstahr?"
    
    play silsound4 "se/poke.ogg"
    show evanbraun shock
    
    me "She's not going to be coming. I tricked you with that letter."
    
    show evanbraun determined
    with dissolve
    
    evan "Huh? So that's what this is about. I thought it was weird . . . for an ex to call me up like that."
    me "An ex? That famous movie director is an ex-girlfriend?"
    
    stop music fadeout 5.0
    
    evan "Yeah, wiseguy. I was planning on fooling around with an ex of mine. You got me. Big deal."
    "I knew it. This guy really doesn't consider women's feelings . . ."
    evan "Anyway, what were you planning to do? Catch me out? Get me to confess to something? Huh?"
    "Building up my courage, I take a breath and speak proudly, from the heart."
    
    play sound3 "se/clash.ogg"
    show speedlines with circleirisout
    show evanbraun shock
    play music "music/drama.ogg"
    
    me "Evan Braun, I want you to stop seeing Hitora. In fact, I demand it. You're ruining my plans . . ."
    
    hide speedlines
    with dissolve
    
    evan "W-What? What are you talking about, you dumb foreigner?"
    me "You're a bully, an unfaithful coward, meanspirited and disloyal. You don't deserve to be at Hitora's side."
    "I land accusation after accusation, levelling everything I've heard from everyone around the continent."
    me "You don't have the right to be spending so much time with the Füühbar. As her bodyguard, I demand you stop."
    
    show evanbraun determined
    with dissolve
    
    evan "You must be joking."
    me "It's the honorable thing to do."
    "I appeal to whatever is left of his noble side."
    
    show evanbraun evil
    with dissolve
    play silsound4 "se/silly17.ogg"
    
    evan "Why would I do something like that? After all, the Füühbar is in love with me."
    me "L-Love? What kind of nonsense is that? Don't screw with me, you playboy!"
    evan "But it's true. The Füühbar has always been in love with me. Right from the start . . ."
    
    show evanbraun determined
    with dissolve
    
    "Suddenly, Evan seems to grow pensive. His mood sours as he begins to recall the past."
    evan "I used to believe in her, you know. Like all the rest of you. I thought she would save this continent . . . save me."
    evan "We started out as friends. Hitora used to be really close to her half-nephew, Gerri. I often saw them together . . ."
    "Hitora has a half-nephew? Why haven't I heard about this? Wait . . . so she's an aunt too?!"
    evan "After Gerri, Hitora started relying on me to fill the gap in her heart. We would spend every day together, becoming closer . . ."
    evan "She so often told me she was madly in love with me. That I was her world . . ."
    evan "But what does that mean when I didn't hear a good word from her in weeks or months?"
    "He obviously didn't appreciate her nasty, selfish personality . . . her temperament could use some work, I guess."
    evan "A few times . . . I even tried to take my life . . . just to get her to notice me for longer than a day . . ."
    "The words drop bitterly from Evan's lips as he recounts his past."
    evan "Then she decided that war was the answer. She wanted to kill people and take over the world."
    
    show evanbraun evil
    with dissolve
    
    evan "Well, I didn't fancy dying in her stupid little war. I wanted to make movies and be in fashion; to be hot, young and famous."
    "This guy. He let his vanity get in the way of his . . . well, somewhat morally-dubious duty to his country."
    
    show evanbraun happy
    
    evan "So, I got on a plane and decided to have my own life."
    evan "It was incredible. Acting, travelling, living it up like a king. Everything I could ever want out of life."
    evan "The chicks, the dudes, the fame, the fortune . . ."
    
    show evanbraun normal
    with dissolve
    
    evan "But still. I always thought about this place and the life we had. About how I couldn't return . . ."
    
    show evanbraun determined
    with dissolve
    
    evan "I thought that maybe she liked me a little, but that she only really loved herself. She loved war more than me."
    "There's a twinge of bitterness in Evan's voice as he talks about his past."
    
    show evanbraun evil
    with dissolve
    play silsound6 "se/silly12.ogg"
    
    evan "Well, turns out I was wrong. It broke her heart. That dumb girl thought the world of me. Haha."
    evan "She called and wrote and telegrammed, desperate, begging me to get in touch, to come back."
    "Hitora really missed him? A guy like this? Maybe . . . does she really love him?"
    evan "I racked my brains for weeks, trying to figure out why, after I left without even saying goodbye."
    
    show evanbraun happy
    with dissolve
    
    evan "Then I realized, in that moment . . . that I could destroy her in an instant. I was her world and she'd do anything for me."
    evan "Every time she annexed a piece of land or invaded a country, she was sending signals. Trying to get me back."
    "This arrogant idiot. He really thinks so highly of himself."
    
    show evanbraun determined
    with dissolve
    
    evan "Anyway, I worked across the world in movies. I travelled and met lots of cute girls. I did everything I wanted to."
    evan "But eventually I stopped getting the auditions and the roles. I couldn't figure out why. And then it hit me."
    evan "With all these refugees leaving Europa thanks to Hitora, the Amerikan film industry had lots of new, cheap talent."
    "New stars from all across Europa who fled the Germanian invasions have become big hits in Amerikan movies."
    evan "Nobody wanted a washed-up Germanian star anymore. Eventually, I got bored of the models and long holidays too."
    evan "So I came back to Altberlin, to restart my career and to make Hitora mine again."
    
    play silsound6 "se/silly4.ogg"
    show evanbraun shock
    
    me "Coward! You abandoned her as soon as you thought you'd have to do any fighting."
    me "Now that Germania's winning the war, you decide to come back? Why? So you can make movies for her?"
    "He only wants her now she's a successful dictator and can get him the roles."
    
    show evanbraun evil
    with dissolve
    
    evan "Of course. That's obvious. But Hitora can't help herself. Evan Braun, her first love, is back in town."
    "This guy's a dirtbag. I knew there was something wrong with him, from the start."
    
    show evanbraun determined
    with dissolve
    
    evan "I'm gonna tell you something important, kid, so listen up."
    evan "Chicks love it when you treat them like dirt. I could break Hitora's heart a thousand times and she'd always take me back."
    
    show evanbraun normal
    with dissolve
    
    me "And what? This makes you happy? To trick a dictator into loving you?"
    evan "Happy? No, happy isn't the right word. At this particular moment I'm certainly not happy."
    
    show evanbraun determined
    with dissolve
    
    evan "I'm twenty-three years old and going nowhere. My career's going to end soon and I'll be needing someone to take care of me."
    evan "Do you think that would make you happy?"
    me "You're just stringing her along. You'll get bored and abandon her again. You don't care about her at all!"
    evan "Well, what's a foreign wimp like you going to do about it? Huh? You gonna tell on me? That's rich."
    "I make a fist and grit my teeth. This guy . . . how dare he laugh at me! I should teach this bully a lesson."
    
    show evanbraun evil
    with dissolve
    
    evan "Gonna hit me, huh? That wouldn't be befitting of an officer now, would it? Do it and you'll be demoted, I guarantee it."
    "He's right. I can't attack a civilian. It wouldn't be right . . . even if he really deserves a good smack."
    evan "Face it, kid. Hitora doesn't care. You're just some patsy she took along for a ride. She doesn't need some runt like you."
    
    show evanbraun determined
    with dissolve
    
    evan "Only Evan Braun, her one true love, can make her happy. Don't you want that? Hitora's happiness?"
    "This bastard."
    evan "I get it . . . we're both guys, after all. We think the same. We want the same things."
    me "We are not the same . . ."
    "He wants to play with her feelings, while all I'm trying to do is the noble thing by blowing her up. We're ten times different."
    evan "Do us all a favor. Get on a plane and go back home to Zipangu. It's what's best for you and for Hitora."
    
    show evanbraun evil
    with dissolve
    
    "He slaps me on the shoulder, as if he's my friend. Then with a wink and a menacing expression, he takes off."
    
    play sound3 "se/walk.ogg"
    hide evanbraun
    with dissolve
    
    "Unable to say or do anything, I watch as Evan Braun disappears into the crowd."
    "A gaggle of fans soon swarm him and follow in a big pack, chanting his name for all to hear."
    me "This . . . can't be happening."
    "Does Adorofia Hitora really love that guy? After the way he treated her?"
    "But what can I do? She asked me to trust her . . . but is this the end of my time here? The end of my mission?"
    me "What can I do? What can I . . ."
    "Someone, please give me a sign. I need a plan . . . an offensive strategy."
    "But once again, I'm left helpless, unable to move decisively. Evan Braun just may have won . . ."
    
    stop soundfx fadeout 3.0
    stop music fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc000081
    
#####################################################################################################################################################
#sc000081	-	Rally where Hitora blows off Evan / Ruins reputation
#####################################################################################################################################################    
label sc000081:
    play soundfx2 "se/birds.ogg" fadein 3.0
    scene day1
    with fade
    play music "music/evil.ogg"
    
    "The days and weeks pass by very slowly . . ."
    "Try as I might, I'm cut out, blocked off, and prevented from seeing the Füühbar. No time or audience is given."
    me "Rumors continue to circulate in the press about Hitora's relationship with Evan."
    "People gossip, celebrity tabloids publish photographs with speculative captions, and the radio waves are buzzing."
    "Every time I read or hear about it, my chest hurts somewhat."
    "It feels as though I've lost my place here. Both as an assassin and a member of the inner circle . . ."
    me "Perhaps I should just go back home to Edooh . . ."
    "I've fought well. Maybe that's enough to grant me safe passage and a small plot of land in the country."
    me "But . . . if I don't stay, I'll be letting down my nation, my uncle, my friends, my sense of duty."
    "One day, Adorofia Hitora makes an announcement. There's to be a grand event held in Altberlin."
    "No further details are given and before I know it, the event itself swiftly arrives."
    "The tabloids believe it's going to be a public ceremony . . . maybe even an engagement announcement."
    
    stop soundfx2 fadeout 3.0
    play soundfx "se/cheer.ogg" fadein 3.0
    scene imperium
    show crowd
    with dissolve
    
    "The crowds gather outside the {i}Superimperiumskanzleistag{/i}, proudly waving miniature flags and cheering."
    "A stage has been quickly constructed, merchandise produced and loudspeakers propped up by the marble pillars."
    "There's a lot of energy as hundreds wait patiently for this surprise speech."
    
    $ mouse_visible = False
    scene cg_hitora1_1
    with dissolve4
    $ mouse_visible = True
    
    "At the top of the sweeping, stone steps, the Füühbar greets the populace, with a fiery determination." 
    hit hat happy "People of Germania! Thank you! Thank you one and all for your continuous adulation!"
    "By her side as her official guest, Evan Braun grins, enjoying the power trip and surveying the crowds."
    evan evil "Heh heh heh . . ."
    "That guy. That playboy."
    hit "I know it's rather short notice, but I absolutely had to hold a rally today. There's something important to discuss . . ."
    "There's some mumbling in the crowd as the people wonder what this event could all be about."
    me "This speech . . . it couldn't be related to all of that . . . could it?"
    "I keep my eyes wide open, on tenterhooks, feeling the tension build."
    hit "There has been a lot of speculation, in the international news, among fan club members and citizens . . ."
    hit "I am here today to address those rumors, once and for all."
    "With a gentle smile, Hitora breathes deeply and then takes on a softer tone."
    
    stop soundfx fadeout 5.0
    stop music fadeout 5.0
    play soundfx2 "se/heart.ogg" fadein 5.0
    
    hit "You see . . . I have a confession to make."
    "A slight panic sets in upon hearing those words."
    me "A confession . . . so this is it . . . she's finally going to make it clear. Her desires. Her relationship."
    "I listen on eagerly, yet part of me struggles to pay attention. My heart swells, my throat closes up . . ."
    hit hat normal "Yes . . . my confession. A confession that everyone here needs to know . . ."
    "The crowd is silent. The mood is palpable. The entire city waits, hanging, hoping, eager."
    "Breathing deeply, I clench my fists and wait for it . . . today, my fate, my relationship with Hitora is decided . . ."
    hit "You see . . ."
    
    play silsound3 "se/silly12.ogg"
    play silsound5 "se/silly11.ogg"
    play sound4 "se/break.ogg"
    stop soundfx2 fadeout 1.0
    show speedlines 
    with circleirisout
    
    hit hat angry "Those rumors are all . . . completely, one-hundred percent false!!!"
    "E-Eh? False? The rumors . . . the rumors about Evan Braun and Hitora . . . aren't true?"
    
    play music "music/savetheday.ogg"
    hide speedlines
    with dissolve
    
    evan shock "W-What? H-Hitora . . . what are you talking about?"
    hit "I do not love Evan Braun. I never did and never will. Nor should any girl who values decency, honor or love."
    hit "He's a cheater, a compulsive liar, a creepy sneak, a slut, a player, a self-obsessed narcissist and a coward."
    "So that's what this is all about . . . she's calling him out on his past behavior."
    hit "Vain and pathetic, Evan Braun makes girls swoon with his lies. No person should be won over by such a weak man."
    hit "Much like our enemies in the past, he imposes selfish doctrines. When others are weak, he takes advantage."
    
    play soundfx "se/cheer.ogg" fadein 3.0
    
    hit hat happy "But Germania . . . and myself . . . we are stronger than we once were. We are better than that."
    "Upon hearing that, the crowds begin to slowly cheer again, enjoying the real-life soap opera playing out on stage."
    evan "B-But . . . but, my Füühbar . . . you can't mean what you're saying?"
    hit hat angry "I mean all of it, one-hundred percent! I don't love you . . . I love war, I love conquest, I love vengeance. But not you."
    evan "Baby, remember, it's me, your lover, Evan. You can't just give up on us! Think about everything we have."
    hit "That's not all. There's someone else here who would like to say something."
    
    play sound2 "se/walk.ogg"
    
    "Joebbels steps up to the microphone and cautiously makes a brief announcement."
    
    play silsound5 "se/silly5.ogg"
    
    goeb evil "F-From this point forward, t-the {i}Propagandaministerium{/i} hereby bans any a-and all of Evan Braun's f-films."
    evan determined "Hey! You can't do this to me. I need those Germanian ticket sales!"
    hit hat angry "Boo-hoo, sucks to be you, loverboy. Once I take over the world, I'll ban your movies everywhere."
    evan "How can you do this? I thought we were going to get back together!"
    
    play silsound4 "se/silly7.ogg"
    
    hit hat moe2 "Hmm? Did I string {i}you{/i} along this time? My bad."
    evan "Y-You tricked me! You made me think . . ."
    hit hat angry "Made you think what? That you could take advantage and propel yourself to glory?"
    hit "I've grown a lot since that childish pretend-romance we had. So I'm going to let you in on a little secret."
    hit "Glory can only be won through hard work and merciless cruelty. You're too much of a coward to have either."
    
    play sound3 "se/battlecry.ogg"
    
    "A mighty cheer goes up from the crowd. I guess they didn't like Evan much either, deep down . . ."
    hit "Evan Braun, not only are your movies banned, but I'm hereby banishing you too. Now get out of my country!"
    evan shock "B-B-But . . . you can't do this!"
    hit "Oh? I can't? Silly me. And here I was, thinking I was an all-powerful dictator. Guards!"
    "Loyal soldiers gradually come forward, ready to escort the jilted ex-boyfriend from the stage."
    hit "Consider yourself lucky. I could also have you shot or sent to the front to sweep minefields!"
    evan determined "So it's like that? Huh?"
    "Slowly coming to realize the situation, Evan looks a little smaller . . . somewhat crestfallen."
    evan "Fine. Forget about it. I'm too good for this place anyway. You can have your stupid wars."
    
    play sound6 "se/run.ogg"
    
    "Swallowing his pride, the playboy takes his leave, swaggering from the stage and disappearing into the crowd."
    "In the end, he really didn't have a leg to stand on."
    hit "Let that be a lesson for any man out there. Don't cross a girl with a standing army and a personality-cult."
    
    play silsound2 "se/silly17.ogg"
    
    hit "The next fool to try it will end up in a much worse place . . ."
    
    play soundfx3 "se/applause.ogg" fadein 3.0
    
    "A few people in the crowd nervously chuckle, and others tear up, before applauding forcefully."
    me "What a bizarre place . . ."
    "The Füühbar gave up on Evan Braun, once and for all. Not only that, she humiliated him, very publicly."
    "I imagine this will be in the papers and on the radio for a long time to come."
    "Soon, I join in on the applause, clapping along. I guess I won't be abandoning my mission here soon . . ."
    
    stop sound3 fadeout 1.0
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    stop soundfx3 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    jump sc000082

#####################################################################################################################################################
#sc000082	-	Hitora and Yamato make up / Ask for more trust
#####################################################################################################################################################    
label sc000082:
    play soundfx3 "se/room.ogg" fadein 3.0
    scene warroom
    with fade
    play music "music/facepalm.ogg"
    
    "Some time later, Hitora and I debrief in her office in the {i}Superimperiumskanzleistag{/i}."
    "We talk over the events of the past few days, the implementation of the top-secret {i}Operation Honeytrap{/i} and more."
    
    show hitora hat worry
    with dissolve
    play silsound4 "se/silly8.ogg"
    
    hit "Eh? You went all the way to Finbard and Moskva over this?"
    me "I was lost, my Füühbar. I needed answers. I needed to know what was going on."
    "There was a reason to keep me in the dark. I understand that much. My curiosity got the better of me."
    "{i}Operation Honeytrap{/i} was Adorofia Hitora's secret plan to entrap Evan Braun and humiliate him as revenge for his past."
    "Only a few members of the inner circle were in on the scheme. But to make it seem real, I had to play the jilted friend."
    
    show hitora hat angry
    with dissolve
    
    hit "Well, I'm sure Iosefina Starin gave you everything you wanted."
    me "I apologize. I didn't know what to do."
    hit "{i}Sigh{/i} . . . I told you to trust me. Just as I trust you to protect me."
    "Funny thing, that . . ."
    me "I guess I didn't like your methods. They confused me . . . they worried me a little."
    "Those final words stop the dictator in her tracks for a moment."
    hit "You . . . really mean that?"
    "I look away, a bit embarrassed, and give a silent nod."
    
    show hitora hat normal
    with dissolve
    
    me "So, what's going to happen to Evan Braun? Have you banished him to the frontline? Forced labor?"
    hit "He's taking a flight back to United Amerika."
    me "What? You're going to let him go? Just like that?"
    
    show hitora hat angry
    with dissolve
    
    hit "I already got what I wanted. Anything else at this point . . . well, it would make me feel lousy."
    "Maybe she does still have a soft spot for that arrogant hunk . . ."
    me "Well, we know there isn't a woman in Germania who would be with him after that speech of yours."
    "Joebbels is going to ban all his films and photographs, so there's no chance of him getting more fans." 
    me "Once he's off this continent, you can focus entirely on this war of yours . . ."
    hit "By the way, how are our plans for war going?"
    me "Well, they're still being worked on, I think. It's good that you've left it to the {i}Generalstall{/i} this time."
    
    play silsound6 "se/silly2.ogg"
    
    hit "That's no good. Keitel can't shirk his responsibilities like that!"
    me "You know, that teddy bear can't actually do anything unless you're the one controlling him."
    
    show hitora hat moe2
    with dissolve
    
    hit "Well, I guess we've all been distracted lately . . ."
    "The Füühbar gives me an all-knowing glance and smiles when she says that. Is she teasing me?"
    me "I need a vacation . . ."
    hit "You've already had your time off. Now we need to win this war. Help me do that and I'll buy your plane tickets myself."
    "Relaxing on a beach or an island . . . perhaps that's all the motivation I need to carry out my mission."
    
    show hitora hat angry
    with dissolve
    
    hit "Ooh! I like the idea of a holiday now. Let's hurry up and smash those xommunists and capitalist pigs!"
    "With this whole escapade behind us, the dictator turns to focus her efforts on future battles once again."
    "Hitora is expecting a victory against the western nations that declared war on Germania. It's her duty to make it a reality."
    "Honestly. What have I got myself into here?"
    
    stop music fadeout 3.0
    stop soundfx3 fadeout 3.0
    scene black
    with fade
    
    ". . . . . . . . ."
    
    #History Block
    $ renpy.block_rollback()
    $ store.text_history_enabled = False
    $ _rollback = False
    
    #PERSISTENT CAMPAIGN UNLOCKED
    $ evan_campaign_completed = True
    $ achievement.grant("COMPLETE_EVANSTORY")
    $ achievement.sync()
    
    #CAMPAIGN CHOICE
    $ config.skipping = False
    play music "music/theme.ogg" fadein 3.0
    call screen campaign_selection() with fade 
    
    return
    
###############################################################################################################
