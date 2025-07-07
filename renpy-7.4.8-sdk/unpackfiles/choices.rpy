
#######  CHOICES  ########

label choice_yamamotocarchat:
    menu:
        "Talk about geography":
            jump choice_yamamotocarchat_answer1
            
        "Talk about the war in Zhina":
            jump choice_yamamotocarchat_answer2
            
        "Talk about Zipanguese history":
            jump choice_yamamotocarchat_answer3
            
        "I feel better already":
            jump choice_yamamotocarchat_continue
            
label choice_battletutorial:
    menu:
        "Please explain it to me with an in-depth tutorial first":
            jump choice_battletutorial_answer1
            
        "I don't need a tutorial, thanks . . . let's just battle!":
            jump choice_battletutorial_answer2

label choice_newspaper1:
    menu:
        "'The failed Britannian appeasement!'":
            jump choice_newspaper1_answer1
            
        "'Polix, our Enemy in the East!'":
            jump choice_newspaper1_answer2
            
        "'Big Crowds expected for Glorious Rally!'":
            jump choice_newspaper1_answer3
            
        "Continue asking around":
            jump choice_newspaper1_continue
            
label choice_winterwar:
    menu:
        "Fight for Finbard in the Wintertime War":
            jump choice_winterwar_answer1
            
        "Don't get involved":
             jump choice_winterwar_answer2
            
label choice_getdowntoit:
    menu:
        "Tell me more about the current situation":
            jump choice_getdowntoit_answer1
            
        "Actually, I'd like to start training":
            jump choice_getdowntoit_answer2
            
        "On second thought, I quit, I don't want this job":
            jump choice_getdowntoit_answer3
            
label choice_onsenpeek:
    menu:
        "Peek":
            $ hitora_love += 1
            $ churchill_love += 1
            $ cyrano_love += 1
            $ starin_love += 1
            jump choice_onsenpeek_answer1
            
        "Don't peek":
            jump choice_onsenpeek_answer2
            
label choice_dinnertable:
    menu:
        "Sure. The more, the merrier.":
            $ hitora_love -= 1
            jump choice_dinnertable_answer1
            
        "I'm afraid not. It's the Füühbar's dinner table after all.":
            $ hitora_love += 1
            jump choice_dinnertable_answer2
            
label choice_joebbelstent:
    menu:
        "I guess it's okay to spend time together . . .":
            jump choice_joebbelstent_answer1
            
        "I'm not going to humor her . . .":
            jump choice_joebbelstent_answer2
            
label choice_panzertalk:
    menu:
        "Talk about the {i}Panzy I{/i} and {i}Panzy II{/i}":
            jump choice_panzertalk_answer1
            
        "Talk about the {i}Panzy III{/i} and {i}Panzy IV{/i}":
            jump choice_panzertalk_answer2
            
label choice_hitoraapology:
    menu:
        "Apologize now. You need to stick around for the mission.":
            $ hitora_love -= 2
            $ breakpoint_hitora_apology = False
            jump choice_hitoraapology_answer1
            
        "Say nothing. Who cares about the mission?":
            $ hitora_love += 2
            $ breakpoint_hitora_apology = True
            jump choice_hitoraapology_answer2

label choice_swimsuit:
    menu:
        "Daring is best! Go for a bikini!":
            $ hitora_love += 2
            jump choice_swimsuit_answer1
            
        "Modesty is best! Stick with the one-piece!":
            $ churchill_love += 2
            jump choice_swimsuit_answer2
            
        "Bonsai charge is best! {i}Fukuryu{/i} all the way!":
            jump choice_swimsuit_answer3
            
label choice_delicatanken:
    menu:
        "Hitora. She loves cakes.":
            $ hitora_love += 1
            $ churchill_love -= 1
            $ cyrano_love -= 1
            $ starin_love -= 1
            $ choice_delicatanken_answered = True
            jump choice_delicatanken_answer1
            
        "Churchill. She loves tea.":
            $ churchill_love += 1
            $ hitora_love -= 1
            $ cyrano_love -= 1
            $ starin_love -= 1
            $ choice_delicatanken_answered = True
            jump choice_delicatanken_answer2
            
        "Cyrano. She loves cafes.":
            $ cyrano_love += 1
            $ hitora_love -= 1
            $ churchill_love -= 1
            $ starin_love -= 1
            $ choice_delicatanken_answered = True
            jump choice_delicatanken_answer3
            
        "Starin. She loves days out.":
            $ starin_love += 1
            $ hitora_love -= 1
            $ churchill_love -= 1
            $ cyrano_love -= 1
            $ choice_delicatanken_answered = True
            jump choice_delicatanken_answer4
            
label choice_hitoraevan:
    menu:
        ". . . you don't trust me.":
            $ hitora_love -= 2
            jump choice_hitoraevan_answer1
            
        ". . . I'm only one of your goons.":
            $ hitora_love -= 1
            jump choice_hitoraevan_answer2
            
label choice_starinevan:
    menu:
        "That sounds tempting . . .":
            $ starin_love += 2
            $ hitora_love -= 2
            jump choice_starinevan_answer1
            
        "There's no way I'm doing that.":
            $ starin_love -= 2
            $ hitora_love += 2
            jump choice_starinevan_answer2
            
label choice_vitaliaquestions:    
    menu:
        "Where are we?":
            jump vitaliaquestion1
        "What is {i}Il Douché{/i} Mussorinni like?":
            jump vitaliaquestion2
        "What is Vitalia's current military situation?":
            jump vitaliaquestion3
            
label choice_favoritedish:
    menu:
        "Carrozza":
            $ hitora_love -= 1
            $ starin_love -= 1
            $ churchill_love -= 1
            $ cyrano_love -= 1
            jump choice_favoritedish_answer1
            
        "Peanut Butter and Jelly":
            $ churchill_love += 1
            jump choice_favoritedish_answer2
            
        "Fischbrötchen":
            $ hitora_love += 1
            jump choice_favoritedish_answer3
            
        "Reuben Sandwich":
            $ starin_love += 1
            jump choice_favoritedish_answer4
            
        "Jambon-beurre":
            $ cyrano_love += 1
            jump choice_favoritedish_answer5
            
label choice_mapintros:
    menu:
        "Empire of Germania and Polix Republic":
            jump choice_mapintros_answer1
            
        "Franzo Republic and Empire of Britannia":
            jump choice_mapintros_answer3
            
        "Kingdom of Vitalia":
            jump choice_mapintros_answer2
            
        "Union of Sovia":
            jump choice_mapintros_answer4
            
        "Actually, I'd like to start training":
            jump choice_getdowntoit_continue
            
label choice_starinteatime:
    menu:
        "Accept Starin's invitation":
            $ starin_love += 2
            $ choice_starinteatime_answered = True
            jump choice_starinteatime_answer1
            
        "Decline Starin's invitation":
            $ starin_love -= 2
            $ choice_starinteatime_answered = False
            jump choice_starinteatime_answer2
            
label choice_hitoraflick:
    menu:
        "Give her a telling off":
            jump choice_hitoraflick_answer2
            
        "Flick her on the forehead and give her a telling off":
            jump choice_hitoraflick_answer1
            
        "Do nothing":
            jump choice_hitoraflick_answer3
            
label choice_cyranodate:
    menu:
        "Of course, diplomacy is always worth a try":
            $ cyrano_love += 2
            $ choice_cyranodate_answered = True
            jump choice_cyranodate_answer1
            
        "We should focus on the war and future battles":
            $ cyrano_love -= 2
            $ choice_cyranodate_answered = False
            jump choice_cyranodate_answer2
            
label choice_cyranoship:
    menu:
        "All I know is that I'm fighting for a better world . . .":
            $ cyrano_love += 2
            $ choice_cyranodate_answered = True
            jump choice_cyranoship_answer1
            
        "When are you going to realize we're on the same side?":
            $ cyrano_love -= 2
            $ choice_cyranodate_answered = False
            jump choice_cyranoship_answer2
            
label choice_hitoraboom:
    menu:
        "Of course . . . don't be ridiculous . . . why wouldn't I . . .":
            $ hitora_love += 1
            jump choice_hitoraboom_answer1
            
        "Of course I am. That genocidal dictator has to go. It's my duty . . .":
            $ hitora_love -= 1
            jump choice_hitoraboom_answer2
            
label choice_rinnizomali:
    menu:
        "Not really. It was all down to the numbers . . .":
            jump choice_rinnizomali_answer1
            
        "Of course. Now stop involving me in your problems . . .":
            jump choice_rinnizomali_answer2
            
label choice_helprinni:
    menu:
        "No way. I refuse to follow these orders.":
            jump choice_helprinni_answer1
            
        "Fine. I will do as I'm commanded and help the Vitalians.":
            jump choice_helprinni_answer2
            
label choice_palaceaskaround:
    menu:
        "Ask around for help, quickly . . .":
            jump choice_palaceaskaround_answer1
            
        "Just bluff your way through it all":
            jump choice_palaceaskaround_answer2
            
label choice_goringtraining:
    menu:
        "Sure. I'll help you with your training.":
            $ hitora_love += 1
            jump choice_goringtraining_answer1
            
        "Sorry. I can't help you.":
            $ hitora_love -= 1
            jump choice_goringtraining_answer2
            
label choice_churchillquestion:
    menu:
        "I'm sorry, I can't do this . . . it wouldn't be right.":
            $ churchill_love -= 2
            jump choice_churchillquestion_answer1
            
        "I understand. Go ahead, ask what you want to ask.":
            $ churchill_love += 2
            jump choice_churchillquestion_answer2
            
label choice_soviaarmydiscussion:
    menu:
        "Sure. I want to know about the Union of Sovia":
            jump choice_soviaarmydiscussion_answer1
            
        "No, that won't be necessary":
            jump choice_soviaarmydiscussion_answer2
            
label choice_moskva:
    menu:
        ". . . there's no way I'm leaving. I still have a mission.":
            $ hitora_love += 1
            $ churchill_love += 1
            $ cyrano_love += 1
            jump choice_moskva_answer1
        
        ". . . okay. I'll go home to Zipangu. I'm ready.":
            jump choice_moskva_answer2
            
        ". . . then, I'll stay here with you, and be your bodyguard.":
            $ starin_love += 2
            jump choice_moskva_answer3
            
label choice_chooseanally:
    menu:
        "Call on your {i}Alliance{/i} allies":
            $ churchill_love += 1
            $ cyrano_love += 1
            $ finalbattle_chosen = "alliance"
            jump choice_chooseanally_answer1
        
        "Call on your {i}Axle{/i} allies":
            $ hitora_love += 1
            $ finalbattle_chosen = "axle"
            jump choice_chooseanally_answer2
            
        "Call on your Sovian allies":
            $ starin_love += 1
            $ finalbattle_chosen = "sovia"
            jump choice_chooseanally_answer3
            
label choice_hitoraembrace:
    menu:
        "Stand your ground and do nothing":
            $ hitora_love -= 2
            $ starin_love += 2
            $ churchill_love += 2
            $ cyrano_love += 2
            jump choice_hitoraembrace_answer1
        
        "Embrace Adorofia Hitora":
            $ hitora_love += 2
            $ starin_love -= 2
            $ churchill_love -= 2
            $ cyrano_love -= 2
            jump choice_hitoraembrace_answer2
            
            
            
########################################################################################################################
#### VOX POP ###########################################################################################################
########################################################################################################################
    
# Voxpop 1 - Hospital in Zipangu
# Voxpop 2 - Arrival in Altberlin
# Voxpop 3 - Transfer Order Imperiumstag
# Voxpop 4 - Iraji Aftermath
# Voxpop 5 - Posters and Art Shop
# Voxpop 6 - Evan Braun
    
screen voxpop_overlay_frame():
    frame:
        background "gui/overlay_frame_back2.png"
        xalign .5
        yalign .5
        xmaximum 1300
        xminimum 1300
        ymaximum 638
        yminimum 638
        yfill False
        xfill False
    vbox:
        xalign .5
        yalign .28
        add "gui/overlay_title_voxpop.png"
            

