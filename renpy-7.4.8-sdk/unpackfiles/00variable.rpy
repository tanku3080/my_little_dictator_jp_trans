#############################################################################################
#  VOICES ###################################################################################
#############################################################################################

init python:
    import random
    
    #readback_full = False
    
    # keymap overriding to show text_history.
    #def readback_catcher():
        #ui.add(renpy.Keymap(rollback=If(store.text_history_enabled,[ SetVariable("yvalue", 1.0), ShowMenu("text_history")])))
        #ui.add(renpy.Keymap(rollforward=ui.returns(None)))
        
    #def scroll_enabler():
        #if readback_full:
            #global config.rollback_enabled = False
            #global config.overlay_functions.append(readback_catcher)
        #else:
            #global config.rollback_enabled = True
            #global config.overlay_functions.remove(readback_catcher)
    
init:
    default female_xs_battle_voiceset = ["voice/battle/female_xs_attack1.ogg", "voice/battle/female_xs_attack2.ogg", "voice/battle/female_xs_attack3.ogg"]
    default female_sm_battle_voiceset = ["voice/battle/female_sm_attack1.ogg", "voice/battle/female_sm_attack2.ogg", "voice/battle/female_sm_attack3.ogg"]
    default female_md_battle_voiceset = ["voice/battle/female_md_attack1.ogg", "voice/battle/female_md_attack2.ogg", "voice/battle/female_md_attack3.ogg"]
    
    default hitora_battle_voiceset = female_sm_battle_voiceset
    default rinni_battle_voiceset = female_sm_battle_voiceset
    default rommel_battle_voiceset = female_xs_battle_voiceset
    default churchill_battle_voiceset = female_sm_battle_voiceset
    default cyrano_battle_voiceset = female_sm_battle_voiceset
    default nyankatshex_battle_voiceset = female_xs_battle_voiceset
    default monty_battle_voiceset = [None]
    default guderian_battle_voiceset = female_sm_battle_voiceset
    default reinejean_battle_voiceset = female_sm_battle_voiceset
    default leclercia_battle_voiceset = female_sm_battle_voiceset
    default starin_battle_voiceset = female_xs_battle_voiceset
    default zhukky_battle_voiceset = female_md_battle_voiceset
    
    default speaking_char = None

    default allied_long_voiceset = ["voice/allied/allied-voice-long-1.ogg", "voice/allied/allied-voice-long-2.ogg", "voice/allied/allied-voice-long-3.ogg"]
    default allied_medium_voiceset = ["voice/allied/allied-voice-medium-1.ogg", "voice/allied/allied-voice-medium-2.ogg", "voice/allied/allied-voice-medium-3.ogg"]
    default allied_short_voiceset = ["voice/allied/allied-voice-short-1.ogg", "voice/allied/allied-voice-short-2.ogg", "voice/allied/allied-voice-short-3.ogg"]
    
    default antoness_long_voiceset = ["voice/antoness/antoness-voice-long-1.ogg", "voice/antoness/antoness-voice-long-2.ogg", "voice/antoness/antoness-voice-long-3.ogg"]
    default antoness_medium_voiceset = ["voice/antoness/antoness-voice-medium-1.ogg", "voice/antoness/antoness-voice-medium-2.ogg", "voice/antoness/antoness-voice-medium-3.ogg"]
    default antoness_short_voiceset = ["voice/antoness/antoness-voice-short-1.ogg", "voice/antoness/antoness-voice-short-2.ogg", "voice/antoness/antoness-voice-short-3.ogg"]
    
    default axis_long_voiceset = ["voice/axis/axis-voice-long-1.ogg", "voice/axis/axis-voice-long-2.ogg", "voice/axis/axis-voice-long-3.ogg"]
    default axis_medium_voiceset = ["voice/axis/axis-voice-medium-1.ogg", "voice/axis/axis-voice-medium-2.ogg", "voice/axis/axis-voice-medium-3.ogg"]
    default axis_short_voiceset = ["voice/axis/axis-voice-short-1.ogg", "voice/axis/axis-voice-short-2.ogg", "voice/axis/axis-voice-short-3.ogg"]
    
    default badoglio_long_voiceset = ["voice/badoglio/badoglio-voice-long-1.ogg", "voice/badoglio/badoglio-voice-long-2.ogg", "voice/badoglio/badoglio-voice-long-3.ogg"]
    default badoglio_medium_voiceset = ["voice/badoglio/badoglio-voice-medium-1.ogg", "voice/badoglio/badoglio-voice-medium-2.ogg", "voice/badoglio/badoglio-voice-medium-3.ogg"]
    default badoglio_short_voiceset = ["voice/badoglio/badoglio-voice-short-1.ogg", "voice/badoglio/badoglio-voice-short-2.ogg", "voice/badoglio/badoglio-voice-short-3.ogg"]
    
    default battenia_long_voiceset = ["voice/battenia/battenia-voice-long-1.ogg", "voice/battenia/battenia-voice-long-2.ogg", "voice/battenia/battenia-voice-long-3.ogg"]
    default battenia_medium_voiceset = ["voice/battenia/battenia-voice-medium-1.ogg", "voice/battenia/battenia-voice-medium-2.ogg", "voice/battenia/battenia-voice-medium-3.ogg"]
    default battenia_short_voiceset = ["voice/battenia/battenia-voice-short-1.ogg", "voice/battenia/battenia-voice-short-2.ogg", "voice/battenia/battenia-voice-short-3.ogg"]
    
    default churchill_long_voiceset = ["voice/churchill/churchill-voice-long-1.ogg", "voice/churchill/churchill-voice-long-2.ogg", "voice/churchill/churchill-voice-long-3.ogg"]
    default churchill_medium_voiceset = ["voice/churchill/churchill-voice-medium-1.ogg", "voice/churchill/churchill-voice-medium-2.ogg", "voice/churchill/churchill-voice-medium-3.ogg"]
    default churchill_short_voiceset = ["voice/churchill/churchill-voice-short-1.ogg", "voice/churchill/churchill-voice-short-2.ogg", "voice/churchill/churchill-voice-short-3.ogg"]
    
    default cyrano_long_voiceset = ["voice/cyrano/cyrano-voice-long-1.ogg", "voice/cyrano/cyrano-voice-long-2.ogg", "voice/cyrano/cyrano-voice-long-3.ogg"]
    default cyrano_medium_voiceset = ["voice/cyrano/cyrano-voice-medium-1.ogg", "voice/cyrano/cyrano-voice-medium-2.ogg", "voice/cyrano/cyrano-voice-medium-3.ogg"]
    default cyrano_short_voiceset = ["voice/cyrano/cyrano-voice-short-1.ogg", "voice/cyrano/cyrano-voice-short-2.ogg", "voice/cyrano/cyrano-voice-short-3.ogg"]
    
    default dunitz_long_voiceset = ["voice/dunitz/dunitz-voice-long-1.ogg", "voice/dunitz/dunitz-voice-long-2.ogg", "voice/dunitz/dunitz-voice-long-3.ogg"]
    default dunitz_medium_voiceset = ["voice/dunitz/dunitz-voice-medium-1.ogg", "voice/dunitz/dunitz-voice-medium-2.ogg", "voice/dunitz/dunitz-voice-medium-3.ogg"]
    default dunitz_short_voiceset = ["voice/dunitz/dunitz-voice-short-1.ogg", "voice/dunitz/dunitz-voice-short-2.ogg", "voice/dunitz/dunitz-voice-short-3.ogg"]
    
    default fatman_long_voiceset = ["voice/fatman/fatman-voice-long-1.ogg", "voice/fatman/fatman-voice-long-2.ogg", "voice/fatman/fatman-voice-long-3.ogg"]
    default fatman_medium_voiceset = ["voice/fatman/fatman-voice-medium-1.ogg", "voice/fatman/fatman-voice-medium-2.ogg", "voice/fatman/fatman-voice-medium-3.ogg"]
    default fatman_short_voiceset = ["voice/fatman/fatman-voice-short-1.ogg", "voice/fatman/fatman-voice-short-2.ogg", "voice/fatman/fatman-voice-short-3.ogg"]
    
    default gamelin_long_voiceset = ["voice/gamelin/gamelin-voice-long-1.ogg", "voice/gamelin/gamelin-voice-long-2.ogg", "voice/gamelin/gamelin-voice-long-3.ogg"]
    default gamelin_medium_voiceset = ["voice/gamelin/gamelin-voice-medium-1.ogg", "voice/gamelin/gamelin-voice-medium-2.ogg", "voice/gamelin/gamelin-voice-medium-3.ogg"]
    default gamelin_short_voiceset = ["voice/gamelin/gamelin-voice-short-1.ogg", "voice/gamelin/gamelin-voice-short-2.ogg", "voice/gamelin/gamelin-voice-short-3.ogg"]
        
    default general_long_voiceset = ["voice/general/general-voice-long-1.ogg", "voice/general/general-voice-long-2.ogg", "voice/general/general-voice-long-3.ogg"]
    default general_medium_voiceset = ["voice/general/general-voice-medium-1.ogg", "voice/general/general-voice-medium-2.ogg", "voice/general/general-voice-medium-3.ogg"]
    default general_short_voiceset = ["voice/general/general-voice-short-1.ogg", "voice/general/general-voice-short-2.ogg", "voice/general/general-voice-short-3.ogg"]
    
    default goring_long_voiceset = ["voice/goring/goring-voice-long-1.ogg", "voice/goring/goring-voice-long-2.ogg", "voice/goring/goring-voice-long-3.ogg"]
    default goring_medium_voiceset = ["voice/goring/goring-voice-medium-1.ogg", "voice/goring/goring-voice-medium-2.ogg", "voice/goring/goring-voice-medium-3.ogg"]
    default goring_short_voiceset = ["voice/goring/goring-voice-short-1.ogg", "voice/goring/goring-voice-short-2.ogg", "voice/goring/goring-voice-short-3.ogg"]
    
    default graziani_long_voiceset = ["voice/graziani/graziani-voice-long-1.ogg", "voice/graziani/graziani-voice-long-2.ogg", "voice/graziani/graziani-voice-long-3.ogg"]
    default graziani_medium_voiceset = ["voice/graziani/graziani-voice-medium-1.ogg", "voice/graziani/graziani-voice-medium-2.ogg", "voice/graziani/graziani-voice-medium-3.ogg"]
    default graziani_short_voiceset = ["voice/graziani/graziani-voice-short-1.ogg", "voice/graziani/graziani-voice-short-2.ogg", "voice/graziani/graziani-voice-short-3.ogg"]
    
    default guderian_long_voiceset = ["voice/guderian/guderian-voice-long-1.ogg", "voice/guderian/guderian-voice-long-2.ogg", "voice/guderian/guderian-voice-long-3.ogg"]
    default guderian_medium_voiceset = ["voice/guderian/guderian-voice-medium-1.ogg", "voice/guderian/guderian-voice-medium-2.ogg", "voice/guderian/guderian-voice-medium-3.ogg"]
    default guderian_short_voiceset = ["voice/guderian/guderian-voice-short-1.ogg", "voice/guderian/guderian-voice-short-2.ogg", "voice/guderian/guderian-voice-short-3.ogg"]
    
    default hirahita_long_voiceset = ["voice/hirahita/hirahita-voice-long-1.ogg", "voice/hirahita/hirahita-voice-long-2.ogg", "voice/hirahita/hirahita-voice-long-3.ogg"]
    default hirahita_medium_voiceset = ["voice/hirahita/hirahita-voice-medium-1.ogg", "voice/hirahita/hirahita-voice-medium-2.ogg", "voice/hirahita/hirahita-voice-medium-3.ogg"]
    default hirahita_short_voiceset = ["voice/hirahita/hirahita-voice-short-1.ogg", "voice/hirahita/hirahita-voice-short-2.ogg", "voice/hirahita/hirahita-voice-short-3.ogg"]
    
    default hitora_long_voiceset = ["voice/hitora/hitora-voice-long-1.ogg", "voice/hitora/hitora-voice-long-2.ogg", "voice/hitora/hitora-voice-long-3.ogg"]
    default hitora_medium_voiceset = ["voice/hitora/hitora-voice-medium-1.ogg", "voice/hitora/hitora-voice-medium-2.ogg", "voice/hitora/hitora-voice-medium-3.ogg"]
    default hitora_short_voiceset = ["voice/hitora/hitora-voice-short-1.ogg", "voice/hitora/hitora-voice-short-2.ogg", "voice/hitora/hitora-voice-short-3.ogg"]
    
    default horthy_long_voiceset = ["voice/horthy/horthy-voice-long-1.ogg", "voice/horthy/horthy-voice-long-2.ogg", "voice/horthy/horthy-voice-long-3.ogg"]
    default horthy_medium_voiceset = ["voice/horthy/horthy-voice-medium-1.ogg", "voice/horthy/horthy-voice-medium-2.ogg", "voice/horthy/horthy-voice-medium-3.ogg"]
    default horthy_short_voiceset = ["voice/horthy/horthy-voice-short-1.ogg", "voice/horthy/horthy-voice-short-2.ogg", "voice/horthy/horthy-voice-short-3.ogg"]
    
    default hubala_long_voiceset = ["voice/hubala/hubala-voice-long-1.ogg", "voice/hubala/hubala-voice-long-2.ogg", "voice/hubala/hubala-voice-long-3.ogg"]
    default hubala_medium_voiceset = ["voice/hubala/hubala-voice-medium-1.ogg", "voice/hubala/hubala-voice-medium-2.ogg", "voice/hubala/hubala-voice-medium-3.ogg"]
    default hubala_short_voiceset = ["voice/hubala/hubala-voice-short-1.ogg", "voice/hubala/hubala-voice-short-2.ogg", "voice/hubala/hubala-voice-short-3.ogg"]
    
    default joebbels_long_voiceset = ["voice/joebbels/joebbels-voice-long-1.ogg", "voice/joebbels/joebbels-voice-long-2.ogg", "voice/joebbels/joebbels-voice-long-3.ogg"]
    default joebbels_medium_voiceset = ["voice/joebbels/joebbels-voice-medium-1.ogg", "voice/joebbels/joebbels-voice-medium-2.ogg", "voice/joebbels/joebbels-voice-medium-3.ogg"]
    default joebbels_short_voiceset = ["voice/joebbels/joebbels-voice-short-1.ogg", "voice/joebbels/joebbels-voice-short-2.ogg", "voice/joebbels/joebbels-voice-short-3.ogg"]
    
    default man_long_voiceset = ["voice/man/man-voice-long-1.ogg", "voice/man/man-voice-long-2.ogg", "voice/man/man-voice-long-3.ogg"]
    default man_medium_voiceset = ["voice/man/man-voice-medium-1.ogg", "voice/man/man-voice-medium-2.ogg", "voice/man/man-voice-medium-3.ogg"]
    default man_short_voiceset = ["voice/man/man-voice-short-1.ogg", "voice/man/man-voice-short-2.ogg", "voice/man/man-voice-short-3.ogg"]
    
    default mannerheim_long_voiceset = ["voice/mannerheim/mannerheim-voice-long-1.ogg", "voice/mannerheim/mannerheim-voice-long-2.ogg", "voice/mannerheim/mannerheim-voice-long-3.ogg"]
    default mannerheim_medium_voiceset = ["voice/mannerheim/mannerheim-voice-medium-1.ogg", "voice/mannerheim/mannerheim-voice-medium-2.ogg", "voice/mannerheim/mannerheim-voice-medium-3.ogg"]
    default mannerheim_short_voiceset = ["voice/mannerheim/mannerheim-voice-short-1.ogg", "voice/mannerheim/mannerheim-voice-short-2.ogg", "voice/mannerheim/mannerheim-voice-short-3.ogg"]
    
    default manstein_long_voiceset = ["voice/manstein/manstein-voice-long-1.ogg", "voice/manstein/manstein-voice-long-2.ogg", "voice/manstein/manstein-voice-long-3.ogg"]
    default manstein_medium_voiceset = ["voice/manstein/manstein-voice-medium-1.ogg", "voice/manstein/manstein-voice-medium-2.ogg", "voice/manstein/manstein-voice-medium-3.ogg"]
    default manstein_short_voiceset = ["voice/manstein/manstein-voice-short-1.ogg", "voice/manstein/manstein-voice-short-2.ogg", "voice/manstein/manstein-voice-short-3.ogg"]
    
    default nyan_long_voiceset = ["voice/nyan/nyan-voice-long-1.ogg", "voice/nyan/nyan-voice-long-2.ogg", "voice/nyan/nyan-voice-long-3.ogg"]
    default nyan_medium_voiceset = ["voice/nyan/nyan-voice-medium-1.ogg", "voice/nyan/nyan-voice-medium-2.ogg", "voice/nyan/nyan-voice-medium-3.ogg"]
    default nyan_short_voiceset = ["voice/nyan/nyan-voice-short-1.ogg", "voice/nyan/nyan-voice-short-2.ogg", "voice/nyan/nyan-voice-short-3.ogg"]
    
    default messe_long_voiceset = ["voice/messe/messe-voice-long-1.ogg", "voice/messe/messe-voice-long-2.ogg", "voice/messe/messe-voice-long-3.ogg"]
    default messe_medium_voiceset = ["voice/messe/messe-voice-medium-1.ogg", "voice/messe/messe-voice-medium-2.ogg", "voice/messe/messe-voice-medium-3.ogg"]
    default messe_short_voiceset = ["voice/messe/messe-voice-short-1.ogg", "voice/messe/messe-voice-short-2.ogg", "voice/messe/messe-voice-short-3.ogg"]
    
    default molotov_long_voiceset = ["voice/molotov/molotov-voice-long-1.ogg", "voice/molotov/molotov-voice-long-2.ogg", "voice/molotov/molotov-voice-long-3.ogg"]
    default molotov_medium_voiceset = ["voice/molotov/molotov-voice-medium-1.ogg", "voice/molotov/molotov-voice-medium-2.ogg", "voice/molotov/molotov-voice-medium-3.ogg"]
    default molotov_short_voiceset = ["voice/molotov/molotov-voice-short-1.ogg", "voice/molotov/molotov-voice-short-2.ogg", "voice/molotov/molotov-voice-short-3.ogg"]
    
    default monty_long_voiceset = ["voice/monty/monty-voice-long-1.ogg", "voice/monty/monty-voice-long-2.ogg", "voice/monty/monty-voice-long-3.ogg"]
    default monty_medium_voiceset = ["voice/monty/monty-voice-medium-1.ogg", "voice/monty/monty-voice-medium-2.ogg", "voice/monty/monty-voice-medium-3.ogg"]
    default monty_short_voiceset = ["voice/monty/monty-voice-short-1.ogg", "voice/monty/monty-voice-short-2.ogg", "voice/monty/monty-voice-short-3.ogg"]
    
    default oldman_long_voiceset = ["voice/oldman/oldman-voice-long-1.ogg", "voice/oldman/oldman-voice-long-2.ogg", "voice/oldman/oldman-voice-long-3.ogg"]
    default oldman_medium_voiceset = ["voice/oldman/oldman-voice-medium-1.ogg", "voice/oldman/oldman-voice-medium-2.ogg", "voice/oldman/oldman-voice-medium-3.ogg"]
    default oldman_short_voiceset = ["voice/oldman/oldman-voice-short-1.ogg", "voice/oldman/oldman-voice-short-2.ogg", "voice/oldman/oldman-voice-short-3.ogg"]
    
    default oldwoman_long_voiceset = ["voice/oldwoman/oldwoman-voice-long-1.ogg", "voice/oldwoman/oldwoman-voice-long-2.ogg", "voice/oldwoman/oldwoman-voice-long-3.ogg"]
    default oldwoman_medium_voiceset = ["voice/oldwoman/oldwoman-voice-medium-1.ogg", "voice/oldwoman/oldwoman-voice-medium-2.ogg", "voice/oldwoman/oldwoman-voice-medium-3.ogg"]
    default oldwoman_short_voiceset = ["voice/oldwoman/oldwoman-voice-short-1.ogg", "voice/oldwoman/oldwoman-voice-short-2.ogg", "voice/oldwoman/oldwoman-voice-short-3.ogg"]
    
    default politician_long_voiceset = ["voice/politician/politician-voice-long-1.ogg", "voice/politician/politician-voice-long-2.ogg", "voice/politician/politician-voice-long-3.ogg"]
    default politician_medium_voiceset = ["voice/politician/politician-voice-medium-1.ogg", "voice/politician/politician-voice-medium-2.ogg", "voice/politician/politician-voice-medium-3.ogg"]
    default politician_short_voiceset = ["voice/politician/politician-voice-short-1.ogg", "voice/politician/politician-voice-short-2.ogg", "voice/politician/politician-voice-short-3.ogg"]
    
    default rinni_long_voiceset = ["voice/rinni/rinni-voice-long-1.ogg", "voice/rinni/rinni-voice-long-2.ogg", "voice/rinni/rinni-voice-long-3.ogg"]
    default rinni_medium_voiceset = ["voice/rinni/rinni-voice-medium-1.ogg", "voice/rinni/rinni-voice-medium-2.ogg", "voice/rinni/rinni-voice-medium-3.ogg"]
    default rinni_short_voiceset = ["voice/rinni/rinni-voice-short-1.ogg", "voice/rinni/rinni-voice-short-2.ogg", "voice/rinni/rinni-voice-short-3.ogg"]
    
    default roijean_long_voiceset = ["voice/roijean/roijean-voice-long-1.ogg", "voice/roijean/roijean-voice-long-2.ogg", "voice/roijean/roijean-voice-long-3.ogg"]
    default roijean_medium_voiceset = ["voice/roijean/roijean-voice-medium-1.ogg", "voice/roijean/roijean-voice-medium-2.ogg", "voice/roijean/roijean-voice-medium-3.ogg"]
    default roijean_short_voiceset = ["voice/roijean/roijean-voice-short-1.ogg", "voice/roijean/roijean-voice-short-2.ogg", "voice/roijean/roijean-voice-short-3.ogg"]
    
    default rommel_long_voiceset = ["voice/rommel/rommel-voice-long-1.ogg", "voice/rommel/rommel-voice-long-2.ogg", "voice/rommel/rommel-voice-long-3.ogg"]
    default rommel_medium_voiceset = ["voice/rommel/rommel-voice-medium-1.ogg", "voice/rommel/rommel-voice-medium-2.ogg", "voice/rommel/rommel-voice-medium-3.ogg"]
    default rommel_short_voiceset = ["voice/rommel/rommel-voice-short-1.ogg", "voice/rommel/rommel-voice-short-2.ogg", "voice/rommel/rommel-voice-short-3.ogg"]
    
    default roosevelt_long_voiceset = ["voice/roosevelt/roosevelt-voice-long-1.ogg", "voice/roosevelt/roosevelt-voice-long-2.ogg", "voice/roosevelt/roosevelt-voice-long-3.ogg"]
    default roosevelt_medium_voiceset = ["voice/roosevelt/roosevelt-voice-medium-1.ogg", "voice/roosevelt/roosevelt-voice-medium-2.ogg", "voice/roosevelt/roosevelt-voice-medium-3.ogg"]
    default roosevelt_short_voiceset = ["voice/roosevelt/roosevelt-voice-short-1.ogg", "voice/roosevelt/roosevelt-voice-short-2.ogg", "voice/roosevelt/roosevelt-voice-short-3.ogg"]
    
    default smigly_long_voiceset = ["voice/smigly/smigly-voice-long-1.ogg", "voice/smigly/smigly-voice-long-2.ogg", "voice/smigly/smigly-voice-long-3.ogg"]
    default smigly_medium_voiceset = ["voice/smigly/smigly-voice-medium-1.ogg", "voice/smigly/smigly-voice-medium-2.ogg", "voice/smigly/smigly-voice-medium-3.ogg"]
    default smigly_short_voiceset = ["voice/smigly/smigly-voice-short-1.ogg", "voice/smigly/smigly-voice-short-2.ogg", "voice/smigly/smigly-voice-short-3.ogg"]
    
    default soldier_long_voiceset = ["voice/soldier/soldier-voice-long-1.ogg", "voice/soldier/soldier-voice-long-2.ogg", "voice/soldier/soldier-voice-long-3.ogg"]
    default soldier_medium_voiceset = ["voice/soldier/soldier-voice-medium-1.ogg", "voice/soldier/soldier-voice-medium-2.ogg", "voice/soldier/soldier-voice-medium-3.ogg"]
    default soldier_short_voiceset = ["voice/soldier/soldier-voice-short-1.ogg", "voice/soldier/soldier-voice-short-2.ogg", "voice/soldier/soldier-voice-short-3.ogg"]
    
    default sovian_long_voiceset = ["voice/sovian/sovian-voice-long-1.ogg", "voice/sovian/sovian-voice-long-2.ogg", "voice/sovian/sovian-voice-long-3.ogg"]
    default sovian_medium_voiceset = ["voice/sovian/sovian-voice-medium-1.ogg", "voice/sovian/sovian-voice-medium-2.ogg", "voice/sovian/sovian-voice-medium-3.ogg"]
    default sovian_short_voiceset = ["voice/sovian/sovian-voice-short-1.ogg", "voice/sovian/sovian-voice-short-2.ogg", "voice/sovian/sovian-voice-short-3.ogg"]
    
    default starin_long_voiceset = ["voice/starin/starin-voice-long-1.ogg", "voice/starin/starin-voice-long-2.ogg", "voice/starin/starin-voice-long-3.ogg"]
    default starin_medium_voiceset = ["voice/starin/starin-voice-medium-1.ogg", "voice/starin/starin-voice-medium-2.ogg", "voice/starin/starin-voice-medium-3.ogg"]
    default starin_short_voiceset = ["voice/starin/starin-voice-short-1.ogg", "voice/starin/starin-voice-short-2.ogg", "voice/starin/starin-voice-short-3.ogg"]
    
    default stuffy_long_voiceset = ["voice/stuffy/stuffy-voice-long-1.ogg", "voice/stuffy/stuffy-voice-long-2.ogg", "voice/stuffy/stuffy-voice-long-3.ogg"]
    default stuffy_medium_voiceset = ["voice/stuffy/stuffy-voice-medium-1.ogg", "voice/stuffy/stuffy-voice-medium-2.ogg", "voice/stuffy/stuffy-voice-medium-3.ogg"]
    default stuffy_short_voiceset = ["voice/stuffy/stuffy-voice-short-1.ogg", "voice/stuffy/stuffy-voice-short-2.ogg", "voice/stuffy/stuffy-voice-short-3.ogg"]
    
    default tito_long_voiceset = ["voice/tito/tito-voice-long-1.ogg", "voice/tito/tito-voice-long-2.ogg", "voice/tito/tito-voice-long-3.ogg"]
    default tito_medium_voiceset = ["voice/tito/tito-voice-medium-1.ogg", "voice/tito/tito-voice-medium-2.ogg", "voice/tito/tito-voice-medium-3.ogg"]
    default tito_short_voiceset = ["voice/tito/tito-voice-short-1.ogg", "voice/tito/tito-voice-short-2.ogg", "voice/tito/tito-voice-short-3.ogg"]
    
    default dresckow_long_voiceset = ["voice/dresckow/dresckow-voice-long-1.ogg", "voice/dresckow/dresckow-voice-long-2.ogg", "voice/dresckow/dresckow-voice-long-3.ogg"]
    default dresckow_medium_voiceset = ["voice/dresckow/dresckow-voice-medium-1.ogg", "voice/dresckow/dresckow-voice-medium-2.ogg", "voice/dresckow/dresckow-voice-medium-3.ogg"]
    default dresckow_short_voiceset = ["voice/dresckow/dresckow-voice-short-1.ogg", "voice/dresckow/dresckow-voice-short-2.ogg", "voice/dresckow/dresckow-voice-short-3.ogg"]
    
    default vasile_long_voiceset = ["voice/vasile/vasile-voice-1.ogg"]
    default vasile_medium_voiceset = ["voice/vasile/vasile-voice-1.ogg"]
    default vasile_short_voiceset = ["voice/vasile/vasile-voice-1.ogg"]
    
    default woman_long_voiceset = ["voice/woman/woman-voice-long-1.ogg", "voice/woman/woman-voice-long-2.ogg", "voice/woman/woman-voice-long-3.ogg"]
    default woman_medium_voiceset = ["voice/woman/woman-voice-medium-1.ogg", "voice/woman/woman-voice-medium-2.ogg", "voice/woman/woman-voice-medium-3.ogg"]
    default woman_short_voiceset = ["voice/woman/woman-voice-short-1.ogg", "voice/woman/woman-voice-short-2.ogg", "voice/woman/woman-voice-short-3.ogg"]
    
    default youth_long_voiceset = ["voice/youth/youth-voice-long-1.ogg", "voice/youth/youth-voice-long-2.ogg", "voice/youth/youth-voice-long-3.ogg"]
    default youth_medium_voiceset = ["voice/youth/youth-voice-medium-1.ogg", "voice/youth/youth-voice-medium-2.ogg", "voice/youth/youth-voice-medium-3.ogg"]
    default youth_short_voiceset = ["voice/youth/youth-voice-short-1.ogg", "voice/youth/youth-voice-short-2.ogg", "voice/youth/youth-voice-short-3.ogg"]
    
    default zhukky_long_voiceset = ["voice/zhukky/zhukky-voice-long-1.ogg", "voice/zhukky/zhukky-voice-long-2.ogg", "voice/zhukky/zhukky-voice-long-3.ogg"]
    default zhukky_medium_voiceset = ["voice/zhukky/zhukky-voice-medium-1.ogg", "voice/zhukky/zhukky-voice-medium-2.ogg", "voice/zhukky/zhukky-voice-medium-3.ogg"]
    default zhukky_short_voiceset = ["voice/zhukky/zhukky-voice-short-1.ogg", "voice/zhukky/zhukky-voice-short-2.ogg", "voice/zhukky/zhukky-voice-short-3.ogg"]
    
    default hoth_long_voiceset = ["se/bearvoice.ogg"]
    default hoth_medium_voiceset = ["se/bearvoice.ogg"]
    default hoth_short_voiceset = ["se/bearvoice.ogg"]
    
    python:
        from random import randrange
        from functools import partial
        
        def char_chat(char, event_name, *args, **kwargs):
            
            if event_name == "show":
                if _last_say_what == ". . . . . . . . .":
                    pass
                elif char != store.speaking_char:
                    if len(_last_say_what) > 65:
                        b = (globals()[char + "_long_voiceset"])
                    elif len(_last_say_what) > 35 and len(_last_say_what) <= 65:
                        b = (globals()[char + "_medium_voiceset"])
                    else:
                        b = (globals()[char + "_short_voiceset"])
                    renpy.play(random.choice(b), "truevoice")
                    store.speaking_char = char
                else:
                    if len(_last_say_what) > 65:
                        b = (globals()[char + "_long_voiceset"])
                    elif len(_last_say_what) > 35 and len(_last_say_what) <= 65:
                        b = (globals()[char + "_medium_voiceset"])
                    else:
                        b = (globals()[char + "_short_voiceset"])
                    renpy.play(random.choice(b), "truevoice")
            elif event_name == "end" or event_name == "slow_done":
                renpy.sound.stop(channel="truevoice", fadeout=0.5)

#############################################################################################
#  RESEARCH DATA  ##############################################################################
#############################################################################################
init:
    default research_power1_completed = False
    default research_power2_completed = False
    default research_power3_completed = False
    default research_power4_completed = False
    default research_power5_completed = False
    default research_armor1_completed = False
    default research_armor2_completed = False
    default research_armor3_completed = False
    default research_armor4_completed = False
    default research_armor5_completed = False
    default research_accuracy1_completed = False
    default research_accuracy2_completed = False
    default research_accuracy3_completed = False
    default research_accuracy4_completed = False
    default research_charm1_completed = False
    default research_charm2_completed = False
    default research_charm3_completed = False
    default research_charm4_completed = False
    default research_speed1_completed = False
    default research_speed2_completed = False
    default research_speed3_completed = False
    
    default research_power1_current = True
    default research_power2_current = False
    default research_power3_current = False
    default research_power4_current = False
    default research_power5_current = False
    default research_armor1_current = False
    default research_armor2_current = False
    default research_armor3_current = False
    default research_armor4_current = False
    default research_armor5_current = False
    default research_accuracy1_current = False
    default research_accuracy2_current = False
    default research_accuracy3_current = False
    default research_accuracy4_current = False
    default research_charm1_current = False
    default research_charm2_current = False
    default research_charm3_current = False
    default research_charm4_current = False
    default research_speed1_current = False
    default research_speed2_current = False
    default research_speed3_current = False
        
    default research_none_basename = "???????????"
    default research_power1_basename = "Conscription"
    default research_power2_basename = "Allegiance"
    default research_power3_basename = "Discipline"
    default research_power4_basename = "Heavy Guns"
    default research_power5_basename = "Total War"
    default research_armor1_basename = "Thick Armor"
    default research_armor2_basename = "Spare Tracks"
    default research_armor3_basename = "Sloped Armor"
    default research_armor4_basename = "Spaced Armor"
    default research_armor5_basename = "Zimmerit Coating"
    default research_accuracy1_basename = "Bombardment"
    default research_accuracy2_basename = "Strategic Bombing"
    default research_accuracy3_basename = "Radar"
    default research_accuracy4_basename = "Vengeance Weapons"
    default research_charm1_basename = "Nationalization"
    default research_charm2_basename = "Grand Projects"
    default research_charm3_basename = "Propaganda"
    default research_charm4_basename = "Total Control"
    default research_speed1_basename = "Powder Metallurgy"
    default research_speed2_basename = "Assembly Lines"
    default research_speed3_basename = "Wartime Production"
    
    default conscription_description = "Build a massive standing army with mandatory enlistment.\n{color=#F35F5F}+1 Up to Power{/color} across all fighters. Takes {color=#F35F5F}3 Turns{/color} to complete."
    default allegiance_description = "Demand that all soldiers swear an oath of loyalty.\n{color=#F35F5F}+1 Up to Power{/color} across all fighters. Takes {color=#F35F5F}3 Turns{/color} to complete."
    default discipline_description = "Introduce new training and discipline for soldiers.\n{color=#F35F5F}+1 Up to Power{/color} across all fighters. Takes {color=#F35F5F}3 Turns{/color} to complete."
    default heavyguns_description = "Roll out new, powerful, heavy guns across the front.\n{color=#F35F5F}+1 Up to Power{/color} across all fighters. Takes {color=#F35F5F}3 Turns{/color} to complete."
    default totalwar_description = "Prepare the army for a total war.\n{color=#F35F5F}+1 Up to Power{/color} across all fighters. Takes {color=#F35F5F}3 Turns{/color} to complete."
    default thickarmor_description = "Improve and thicken the armor of tanks and vehicles.\n{color=#F35F5F}+1 Up to Armor{/color} across all fighters. Takes {color=#F35F5F}3 Turns{/color} to complete."
    default sparetracks_description = "Include spare tracks, shells and tools on tanks in the field.\n{color=#F35F5F}+1 Up to Armor{/color} across all fighters. Takes {color=#F35F5F}3 Turns{/color} to complete."
    default slopedarmor_description = "Introduce sloped armor on tanks to protect against penetration.\n{color=#F35F5F}+1 Up to Armor{/color} across all fighters. Takes {color=#F35F5F}3 Turns{/color} to complete."
    default spacedarmor_description = "Add armored skirts to make tanks more resistant to anti-tank fire.\n{color=#F35F5F}+1 Up to Armor{/color} across all fighters. Takes {color=#F35F5F}3 Turns{/color} to complete."
    default zimmeritcoating_description = "Paint tanks with a coating of Zimmerit paste to improve the armor.\n{color=#F35F5F}+1 Up to Armor{/color} across all fighters. Takes {color=#F35F5F}3 Turns{/color} to complete."
    default bombardment_description = "Destroy entire areas with a general bombardment.\n{color=#F35F5F}+1 Up to Accuracy{/color} across all fighters. Takes {color=#F35F5F}3 Turns{/color} to complete."
    default strategicbombing_description = "Use concentrated bombing to weaken the enemy.\n{color=#F35F5F}+1 Up to Accuracy{/color} across all fighters. Takes {color=#F35F5F}6 Turns{/color} to complete."
    default radar_description = "Utilize the latest radar technology to gain the upper hand.\n{color=#F35F5F}+1 Up to Accuracy{/color} across all fighters. Takes {color=#F35F5F}3 Turns{/color} to complete."
    default vengeanceweapons_description = "Take revenge with space-age wonder weapons.\n{color=#F35F5F}+1 Up to Accuracy{/color} across all fighters. Takes {color=#F35F5F}3 Turns{/color} to complete."
    default nationalization_description = "Take control of key industries in a managed economy.\n{color=#F35F5F}+1 Up to Critical{/color} across all fighters. Takes {color=#F35F5F}3 Turns{/color} to complete."
    default grandprojects_description = "Rebuild the country with railroads, motorways and new buildings.\n{color=#F35F5F}+1 Up to Critical{/color} across all fighters. Takes {color=#F35F5F}3 Turns{/color} to complete."
    default propaganda_description = "Brainwash the populace with frightening propaganda.\n{color=#F35F5F}+1 Up to Critical{/color} across all fighters. Takes {color=#F35F5F}6 Turns{/color} to complete."
    default totalcontrol_description = "Take full control of all institutions in a one-party state.\n{color=#F35F5F}+1 Up to Critical{/color} across all fighters. Takes {color=#F35F5F}3 Turns{/color} to complete."
    default powdermetallurgy_description = "Improve factory line production with metal powders.\n{color=#F35F5F}+1 Up to Speed{/color} across all fighters. Takes {color=#F35F5F}3 Turns{/color} to complete."
    default assemblylines_description = "Speed up factory line production with assembly lines.\n{color=#F35F5F}+1 Up to Speed{/color} across all fighters. Takes {color=#F35F5F}6 Turns{/color} to complete."
    default wartimeproduction_description = "Devote all national resources to wartime production.\n{color=#F35F5F}+1 Up to Speed{/color} across all fighters. Takes {color=#F35F5F}6 Turns{/color} to complete."
    
    default research_power2_nonename = "?!????!???"
    default research_power3_nonename = "??????!!??"
    default research_power4_nonename = "??!?!????"
    default research_power5_nonename = "?????!??!???"
    default research_armor2_nonename = "?!??????!??"
    default research_armor3_nonename = "????!??????!?"
    default research_armor4_nonename = "??!????!!"
    default research_armor5_nonename = "??!???!??"
    default research_accuracy2_nonename = "?!??!?????!"
    default research_accuracy3_nonename = "??!?????!?"
    default research_accuracy4_nonename = "?!??!??????"
    default research_charm2_nonename = "??!????!???"
    default research_charm3_nonename = "?????!?????"
    default research_charm4_nonename = "???!??!????"
    default research_speed2_nonename = "??????!???"
    default research_speed3_nonename = "??!??!????"
    
    default research_none_name = research_none_basename
    default research_power1_name = research_power1_basename
    default research_power2_name = research_power2_nonename
    default research_power3_name = research_power3_nonename
    default research_power4_name = research_power4_nonename
    default research_power5_name = research_power5_nonename
    default research_armor1_name = research_armor1_basename
    default research_armor2_name = research_armor2_nonename
    default research_armor3_name = research_armor3_nonename
    default research_armor4_name = research_armor4_nonename
    default research_armor5_name = research_armor5_nonename
    default research_accuracy1_name = research_accuracy1_basename
    default research_accuracy2_name = research_accuracy2_nonename
    default research_accuracy3_name = research_accuracy3_nonename
    default research_accuracy4_name = research_accuracy4_nonename
    default research_charm1_name = research_charm1_basename
    default research_charm2_name = research_charm2_nonename
    default research_charm3_name = research_charm3_nonename
    default research_charm4_name = research_charm4_nonename
    default research_speed1_name = research_speed1_basename
    default research_speed2_name = research_speed2_nonename
    default research_speed3_name = research_speed3_nonename
    
    image research_power1_base = im.FactorScale(im.Crop("character/object/object_lutetia.png", (400, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16)
    image research_power2_base = im.FactorScale(im.Crop("character/object/object_banners.png", (400, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16)
    image research_power3_base = im.FactorScale(im.Crop("character/object/object_marching.png", (164, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16)
    image research_power4_base = im.FactorScale(im.Crop("character/object/tank_kv2.png", (300, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16)
    image research_power5_base = im.FactorScale(im.Crop("character/object/object_dianxia.png", (164, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16)
    image research_armor1_base = im.FactorScale(im.Crop("character/object/tank_matildai.png", (164, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16)
    image research_armor2_base = im.FactorScale(im.Crop("character/object/tank_marder.png", (164, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16)
    image research_armor3_base = im.FactorScale(im.Crop("character/object/tank_jagdpanzer.png", (254, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16)
    image research_armor4_base = im.FactorScale(im.Crop("character/object/tank_panzer4.png", (164, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16)
    image research_armor5_base = im.FactorScale(im.Crop("character/object/tank_panzer3.png", (200, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16)
    image research_accuracy1_base = im.FactorScale(im.Crop("character/object/plane_fw200condor.png", (224, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16)
    image research_accuracy2_base = im.FactorScale(im.Crop("character/object/object_serpana.png", (164, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16)
    image research_accuracy3_base = im.FactorScale(im.Crop("character/object/plane_wellington.png", (164, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16)
    image research_accuracy4_base = im.FactorScale(im.Crop("character/object/tank_schwerergustav.png", (164, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16)
    image research_charm1_base = im.FactorScale(im.Crop("character/object/architecture_gallery.png", (200, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16)
    image research_charm2_base = im.FactorScale(im.Crop("character/object/architecture_moskva.png", (164, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16)
    image research_charm3_base = im.FactorScale(im.Crop("character/object/object_bookburning.png", (164, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16)
    image research_charm4_base = im.FactorScale(im.Crop("character/object/object_himmora.png", (300, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16)
    image research_speed1_base = im.FactorScale(im.Crop("character/object/object_dustbowl.png", (500, 450, 400, 323), xalign=0.5, yalign=0.5), 0.32)
    image research_speed2_base = im.FactorScale(im.Crop("character/object/tank_7tp.png", (164, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16)
    image research_speed3_base = im.FactorScale(im.Crop("character/object/ship_arkroyal.png", (300, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16)
    
    image research_power1_researching = im.MatrixColor(im.FactorScale(im.Crop("character/object/object_lutetia.png", (400, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16), im.matrix.desaturate() * im.matrix.tint(1, 0.5, 0.5))
    image research_power2_researching = im.MatrixColor(im.FactorScale(im.Crop("character/object/object_banners.png", (400, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16), im.matrix.desaturate() * im.matrix.tint(1, 0.5, 0.5))
    image research_power3_researching = im.MatrixColor(im.FactorScale(im.Crop("character/object/object_marching.png", (164, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16), im.matrix.desaturate() * im.matrix.tint(1, 0.5, 0.5))
    image research_power4_researching = im.MatrixColor(im.FactorScale(im.Crop("character/object/tank_kv2.png", (300, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16), im.matrix.desaturate() * im.matrix.tint(1, 0.5, 0.5))
    image research_power5_researching = im.MatrixColor(im.FactorScale(im.Crop("character/object/object_dianxia.png", (164, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16), im.matrix.desaturate() * im.matrix.tint(1, 0.5, 0.5))
    image research_armor1_researching = im.MatrixColor(im.FactorScale(im.Crop("character/object/tank_matildai.png", (164, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16), im.matrix.desaturate() * im.matrix.tint(1, 0.5, 0.5))
    image research_armor2_researching = im.MatrixColor(im.FactorScale(im.Crop("character/object/tank_marder.png", (164, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16), im.matrix.desaturate() * im.matrix.tint(1, 0.5, 0.5))
    image research_armor3_researching = im.MatrixColor(im.FactorScale(im.Crop("character/object/tank_jagdpanzer.png", (254, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16), im.matrix.desaturate() * im.matrix.tint(1, 0.5, 0.5))
    image research_armor4_researching = im.MatrixColor(im.FactorScale(im.Crop("character/object/tank_panzer4.png", (200, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16), im.matrix.desaturate() * im.matrix.tint(1, 0.5, 0.5))
    image research_armor5_researching = im.MatrixColor(im.FactorScale(im.Crop("character/object/tank_panzer3.png", (164, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16), im.matrix.desaturate() * im.matrix.tint(1, 0.5, 0.5))
    image research_accuracy1_researching = im.MatrixColor(im.FactorScale(im.Crop("character/object/plane_fw200condor.png", (224, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16), im.matrix.desaturate() * im.matrix.tint(1, 0.5, 0.5))
    image research_accuracy2_researching = im.MatrixColor(im.FactorScale(im.Crop("character/object/object_serpana.png", (164, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16), im.matrix.desaturate() * im.matrix.tint(1, 0.5, 0.5))
    image research_accuracy3_researching = im.MatrixColor(im.FactorScale(im.Crop("character/object/plane_wellington.png", (164, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16), im.matrix.desaturate() * im.matrix.tint(1, 0.5, 0.5))
    image research_accuracy4_researching = im.MatrixColor(im.FactorScale(im.Crop("character/object/tank_schwerergustav.png", (164, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16), im.matrix.desaturate() * im.matrix.tint(1, 0.5, 0.5))
    image research_charm1_researching = im.MatrixColor(im.FactorScale(im.Crop("character/object/architecture_gallery.png", (200, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16), im.matrix.desaturate() * im.matrix.tint(1, 0.5, 0.5))
    image research_charm2_researching = im.MatrixColor(im.FactorScale(im.Crop("character/object/architecture_moskva.png", (164, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16), im.matrix.desaturate() * im.matrix.tint(1, 0.5, 0.5))
    image research_charm3_researching = im.MatrixColor(im.FactorScale(im.Crop("character/object/object_bookburning.png", (164, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16), im.matrix.desaturate() * im.matrix.tint(1, 0.5, 0.5))
    image research_charm4_researching = im.MatrixColor(im.FactorScale(im.Crop("character/object/object_himmora.png", (300, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16), im.matrix.desaturate() * im.matrix.tint(1, 0.5, 0.5))
    image research_speed1_researching = im.MatrixColor(im.FactorScale(im.Crop("character/object/object_dustbowl.png", (164, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16), im.matrix.desaturate() * im.matrix.tint(1, 0.5, 0.5))
    image research_speed2_researching = im.MatrixColor(im.FactorScale(im.Crop("character/object/tank_7tp.png", (164, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16), im.matrix.desaturate() * im.matrix.tint(1, 0.5, 0.5))
    image research_speed3_researching = im.MatrixColor(im.FactorScale(im.Crop("character/object/ship_arkroyal.png", (300, 101, 800, 646), xalign=0.5, yalign=0.5), 0.16), im.matrix.desaturate() * im.matrix.tint(1, 0.5, 0.5))
    
    image research_power1_insensitive = im.MatrixColor(im.FactorScale(im.Crop("gui/gallocked.png", (47, 0, 235, 190), xalign=0.5, yalign=0.5), 0.54), im.matrix.opacity(0.5))
    image research_power2_insensitive = im.MatrixColor(im.FactorScale(im.Crop("gui/gallocked.png", (47, 0, 235, 190), xalign=0.5, yalign=0.5), 0.54), im.matrix.opacity(0.5))
    image research_power3_insensitive = im.MatrixColor(im.FactorScale(im.Crop("gui/gallocked.png", (47, 0, 235, 190), xalign=0.5, yalign=0.5), 0.54), im.matrix.opacity(0.5))
    image research_power4_insensitive = im.MatrixColor(im.FactorScale(im.Crop("gui/gallocked.png", (47, 0, 235, 190), xalign=0.5, yalign=0.5), 0.54), im.matrix.opacity(0.5))
    image research_power5_insensitive = im.MatrixColor(im.FactorScale(im.Crop("gui/gallocked.png", (47, 0, 235, 190), xalign=0.5, yalign=0.5), 0.54), im.matrix.opacity(0.5))
    image research_armor1_insensitive = im.MatrixColor(im.FactorScale(im.Crop("gui/gallocked.png", (47, 0, 235, 190), xalign=0.5, yalign=0.5), 0.54), im.matrix.opacity(0.5))
    image research_armor2_insensitive = im.MatrixColor(im.FactorScale(im.Crop("gui/gallocked.png", (47, 0, 235, 190), xalign=0.5, yalign=0.5), 0.54), im.matrix.opacity(0.5))
    image research_armor3_insensitive = im.MatrixColor(im.FactorScale(im.Crop("gui/gallocked.png", (47, 0, 235, 190), xalign=0.5, yalign=0.5), 0.54), im.matrix.opacity(0.5))
    image research_armor4_insensitive = im.MatrixColor(im.FactorScale(im.Crop("gui/gallocked.png", (47, 0, 235, 190), xalign=0.5, yalign=0.5), 0.54), im.matrix.opacity(0.5))
    image research_armor5_insensitive = im.MatrixColor(im.FactorScale(im.Crop("gui/gallocked.png", (47, 0, 235, 190), xalign=0.5, yalign=0.5), 0.54), im.matrix.opacity(0.5))
    image research_accuracy1_insensitive = im.MatrixColor(im.FactorScale(im.Crop("gui/gallocked.png", (47, 0, 235, 190), xalign=0.5, yalign=0.5), 0.54), im.matrix.opacity(0.5))
    image research_accuracy2_insensitive = im.MatrixColor(im.FactorScale(im.Crop("gui/gallocked.png", (47, 0, 235, 190), xalign=0.5, yalign=0.5), 0.54), im.matrix.opacity(0.5))
    image research_accuracy3_insensitive = im.MatrixColor(im.FactorScale(im.Crop("gui/gallocked.png", (47, 0, 235, 190), xalign=0.5, yalign=0.5), 0.54), im.matrix.opacity(0.5))
    image research_accuracy4_insensitive = im.MatrixColor(im.FactorScale(im.Crop("gui/gallocked.png", (47, 0, 235, 190), xalign=0.5, yalign=0.5), 0.54), im.matrix.opacity(0.5))
    image research_charm1_insensitive = im.MatrixColor(im.FactorScale(im.Crop("gui/gallocked.png", (47, 0, 235, 190), xalign=0.5, yalign=0.5), 0.54), im.matrix.opacity(0.5))
    image research_charm2_insensitive = im.MatrixColor(im.FactorScale(im.Crop("gui/gallocked.png", (47, 0, 235, 190), xalign=0.5, yalign=0.5), 0.54), im.matrix.opacity(0.5))
    image research_charm3_insensitive = im.MatrixColor(im.FactorScale(im.Crop("gui/gallocked.png", (47, 0, 235, 190), xalign=0.5, yalign=0.5), 0.54), im.matrix.opacity(0.5))
    image research_charm4_insensitive = im.MatrixColor(im.FactorScale(im.Crop("gui/gallocked.png", (47, 0, 235, 190), xalign=0.5, yalign=0.5), 0.54), im.matrix.opacity(0.5))
    image research_speed1_insensitive = im.MatrixColor(im.FactorScale(im.Crop("gui/gallocked.png", (47, 0, 235, 190), xalign=0.5, yalign=0.5), 0.54), im.matrix.opacity(0.5))
    image research_speed2_insensitive = im.MatrixColor(im.FactorScale(im.Crop("gui/gallocked.png", (47, 0, 235, 190), xalign=0.5, yalign=0.5), 0.54), im.matrix.opacity(0.5))
    image research_speed3_insensitive = im.MatrixColor(im.FactorScale(im.Crop("gui/gallocked.png", (47, 0, 235, 190), xalign=0.5, yalign=0.5), 0.54), im.matrix.opacity(0.5))
    
    image research_power1_image = ConditionSwitch(
        "research_power1_current == True", "research_power1_researching",
        "True", "research_power1_base")
    
    image research_power2_image = ConditionSwitch(
        "research_power2_current == True", "research_power2_researching",
        "battlestats_attack_up < .75", "research_power2_insensitive",
        "True", "research_power2_base")
        
    image research_power3_image = ConditionSwitch(
        "research_power3_current == True", "research_power3_researching",
        "battlestats_attack_up < 1.5", "research_power3_insensitive",
        "True", "research_power3_base")
    
    image research_power4_image = ConditionSwitch(
        "research_power4_current == True", "research_power4_researching",
        "battlestats_attack_up < 2.25", "research_power4_insensitive",
        "True", "research_power4_base")
    
    image research_power5_image = ConditionSwitch(
        "research_power5_current == True", "research_power5_researching",
        "battlestats_attack_up < 3", "research_power5_insensitive",
        "True", "research_power5_base")
        
    image research_armor1_image = ConditionSwitch(
        "research_armor1_current == True", "research_armor1_researching",
        "True", "research_armor1_base")
    
    image research_armor2_image = ConditionSwitch(
        "research_armor2_current == True", "research_armor2_researching",
        "battlestats_defense_up < .75", "research_armor2_insensitive",
        "True", "research_armor2_base")
        
    image research_armor3_image = ConditionSwitch(
        "research_armor3_current == True", "research_armor3_researching",
        "battlestats_defense_up < 1.5", "research_armor3_insensitive",
        "True", "research_armor3_base")
    
    image research_armor4_image = ConditionSwitch(
        "research_armor4_current == True", "research_armor4_researching",
        "battlestats_defense_up < 2.25", "research_armor4_insensitive",
        "True", "research_armor4_base")
    
    image research_armor5_image = ConditionSwitch(
        "research_armor5_current == True", "research_armor5_researching",
        "battlestats_defense_up < 3", "research_armor5_insensitive",
        "True", "research_armor5_base")
        
    image research_accuracy1_image = ConditionSwitch(
        "research_accuracy1_current == True", "research_accuracy1_researching",
        "True", "research_accuracy1_base")
    
    image research_accuracy2_image = ConditionSwitch(
        "research_accuracy2_current == True", "research_accuracy2_researching",
        "battlestats_accuracy_up < .75", "research_accuracy2_insensitive",
        "True", "research_accuracy2_base")
        
    image research_accuracy3_image = ConditionSwitch(
        "research_accuracy3_current == True", "research_accuracy3_researching",
        "battlestats_accuracy_up < 2.25", "research_accuracy3_insensitive",
        "True", "research_accuracy3_base")
    
    image research_accuracy4_image = ConditionSwitch(
        "research_accuracy4_current == True", "research_accuracy4_researching",
        "battlestats_accuracy_up < 3", "research_accuracy4_insensitive",
        "True", "research_accuracy4_base")
    
    image research_charm1_image = ConditionSwitch(
        "research_charm1_current == True", "research_charm1_researching",
        "True", "research_charm1_base")
        
    image research_charm2_image = ConditionSwitch(
        "research_charm2_current == True", "research_charm2_researching",
        "battlestats_critical_up < .75", "research_charm2_insensitive",
        "True", "research_charm2_base")
    
    image research_charm3_image = ConditionSwitch(
        "research_charm3_current == True", "research_charm3_researching",
        "battlestats_critical_up < 1.5", "research_charm3_insensitive",
        "True", "research_charm3_base")
        
    image research_charm4_image = ConditionSwitch(
        "research_charm4_current == True", "research_charm4_researching",
        "battlestats_critical_up < 3", "research_charm4_insensitive",
        "True", "research_charm4_base")
    
    image research_speed1_image = ConditionSwitch(
        "research_speed1_current == True", "research_speed1_researching",
        "True", "research_speed1_base")
    
    image research_speed2_image = ConditionSwitch(
        "research_speed2_current == True", "research_speed2_researching",
        "battlestats_speed_up < .75", "research_speed2_insensitive",
        "True", "research_speed2_base")
        
    image research_speed3_image = ConditionSwitch(
        "research_speed3_current == True", "research_speed3_researching",
        "battlestats_speed_up < 2.25", "research_speed3_insensitive",
        "True", "research_speed3_base")
    
    default research_power1_number = 3
    default research_power2_number = 6
    default research_power3_number = 9
    default research_power4_number = 12
    default research_power5_number = 15
    default research_armor1_number = 3
    default research_armor2_number = 6
    default research_armor3_number = 9
    default research_armor4_number = 12
    default research_armor5_number = 15
    default research_accuracy1_number = 3
    default research_accuracy2_number = 9
    default research_accuracy3_number = 12
    default research_accuracy4_number = 15
    default research_charm1_number = 3
    default research_charm2_number = 6
    default research_charm3_number = 12
    default research_charm4_number = 15
    default research_speed1_number = 3
    default research_speed2_number = 9
    default research_speed3_number = 15
    
    default active_research_items = {
        research_power1_name: ["research_power1_image", 270, 50, research_power1_completed, research_power1_current, research_power1_number],
        research_power2_name: ["research_power2_image", 270, 280, research_power2_completed, research_power2_current, research_power2_number],
        research_power3_name: ["research_power3_image", 270, 510, research_power3_completed, research_power3_current, research_power3_number],
        research_power4_name: ["research_power4_image", 270, 740, research_power4_completed, research_power4_current, research_power4_number],
        research_power5_name: ["research_power5_image", 270, 970, research_power5_completed, research_power5_current, research_power5_number],
        research_armor1_name: ["research_armor1_image", 520, 50, research_armor1_completed, research_armor1_current, research_armor1_number],
        research_armor2_name: ["research_armor2_image", 520, 280, research_armor2_completed, research_armor2_current, research_armor2_number],
        research_armor3_name: ["research_armor3_image", 520, 510, research_armor3_completed, research_armor3_current, research_armor3_number],
        research_armor4_name: ["research_armor4_image", 440, 970, research_armor4_completed, research_armor4_current, research_armor4_number],
        research_armor5_name: ["research_armor5_image", 600, 970, research_armor5_completed, research_armor5_current, research_armor5_number],
        research_accuracy1_name: ["research_accuracy1_image", 771, 50, research_accuracy1_completed, research_accuracy1_current, research_accuracy1_number],
        research_accuracy2_name: ["research_accuracy2_image", 771, 510, research_accuracy2_completed, research_accuracy2_current, research_accuracy2_number],
        research_accuracy3_name: ["research_accuracy3_image", 771, 740, research_accuracy3_completed, research_accuracy3_current, research_accuracy3_number],
        research_accuracy4_name: ["research_accuracy4_image", 771, 970, research_accuracy4_completed, research_accuracy4_current, research_accuracy4_number],
        research_charm1_name: ["research_charm1_image", 1023, 50, research_charm1_completed, research_charm1_current, research_charm1_number],
        research_charm2_name: ["research_charm2_image", 1023, 280, research_charm2_completed, research_charm2_current, research_charm2_number],
        research_charm3_name: ["research_charm3_image", 1023, 740, research_charm3_completed, research_charm3_current, research_charm3_number],
        research_charm4_name: ["research_charm4_image", 1023, 970, research_charm4_completed, research_charm4_current, research_charm4_number],
        research_speed1_name: ["research_speed1_image", 1276, 50, research_speed1_completed, research_speed1_current, research_speed1_number],
        research_speed2_name: ["research_speed2_image", 1276, 510, research_speed2_completed, research_speed2_current, research_speed2_number],
        research_speed3_name: ["research_speed3_image", 1276, 970, research_speed3_completed, research_speed3_current, research_speed3_number]
    }
    
    default inactive_research_items = {
        "research_power2_insensitive": [research_none_name, 270, 280],
        "research_power3_insensitive": [research_none_name, 270, 510],
        "research_power4_insensitive": [research_none_name, 270, 740],
        "research_power5_insensitive": [research_none_name, 270, 970],
        "research_armor2_insensitive": [research_none_name, 520, 280],
        "research_armor3_insensitive": [research_none_name, 520, 510],
        "research_armor4_insensitive": [research_none_name, 440, 970],
        "research_armor5_insensitive": [research_none_name, 600, 970],
        "research_accuracy2_insensitive": [research_none_name, 771, 510],
        "research_accuracy3_insensitive": [research_none_name, 771, 740],
        "research_accuracy4_insensitive": [research_none_name, 771, 970],
        "research_charm2_insensitive": [research_none_name, 1023, 280],
        "research_charm3_insensitive": [research_none_name, 1023, 740],
        "research_charm4_insensitive": [research_none_name, 1023, 970],
        "research_speed2_insensitive": [research_none_name, 1276, 510],
        "research_speed3_insensitive": [research_none_name, 1276, 970]
    }


#############################################################################################
#  BATTLE DATA  ##############################################################################
#############################################################################################
default gui_text = []
default fighter_store = {}
default skill_store = {}
default available_section = ["infantry", "panzer", "antitank", "commander", "airsupport", "special group"]

default silly_sounds = True

default breakpoint_lossokay_training = False
default breakpoint_lossokay_zhukky = False
default breakpoint_lossokay_churchill = False
default breakpoint_lossokay_airtraining = False
default breakpoint_lossokay_nyan = False
default breakpoint_lossokay_prologue = False
default breakpoint_lossokay_monty = False

default infantry_section_unlocked = True
default panzer_section_unlocked = True
default antitank_section_unlocked = True
default commander_section_unlocked = True
default airsupport_section_unlocked = False
default specialgroup_section_unlocked = False
default nyanbattles_selection = True

default player_team = BaseTeam("Player", Solid("#000000", xysize=(50,50)), limit=50)
default enemy_team = BaseTeam("Enemy", Solid("#000000", xysize=(50,50)), limit=50)
default current_player = None
default current_enemy = None
default player_pos = [80, 230]
default enemy_pos = [1000, -50]
default bar_delay = 1.5

default battle_kodisplay = False
default battlesprite_overlaying = False
default battle_enemyintro = False
default skip_battle_prompt = False
default skip_battle_happen = False
default skip_battle_sensitive = False
default skip_battle_selected = False
default levelup_okay = False
default yamato_levels = 0

default click_to_proceed = False
default novictoryscreen_enabled = False

default cp = 500
default max_cp = 500
default cp_levelset = 50
default max_cp_levelset = 50

default battlescreen_overlaid = False
default battle_terrain = "ground"
default front_definition = "_front"
default fight_end = "bat000001_aftermath"
default yamatoforce_enabled = True
default finalbattle_chosen = "axle"
default battle_count = 0
default escape_delay = False
default escape_pause = False

default infantry_initial_locked_fighters = 21
default panzer_initial_locked_fighters = 44
default antitank_initial_locked_fighters = 10
default commander_initial_locked_fighters = 7
default airsupport_initial_locked_fighters = 9
default specialgroup_initial_locked_fighters = 16

default infantry_locked_fighters = infantry_initial_locked_fighters
default panzer_locked_fighters = panzer_initial_locked_fighters
default antitank_locked_fighters = antitank_initial_locked_fighters
default commander_locked_fighters = commander_initial_locked_fighters
default airsupport_locked_fighters = airsupport_initial_locked_fighters
default specialgroup_locked_fighters = specialgroup_initial_locked_fighters
default overall_locked_fighters = infantry_locked_fighters + panzer_locked_fighters + antitank_locked_fighters  + commander_locked_fighters + airsupport_locked_fighters + specialgroup_locked_fighters

default battlestats_focus = "Power"
default battlestats_attack_up = 0
default battlestats_defense_up = 0
default battlestats_accuracy_up = 0
default battlestats_critical_up = 0
default battlestats_speed_up = 0

default enemy_fighter_set = [
    "enemy_airsupport_dambuster",
    "enemy_airsupport_fopfighter",
    "enemy_airsupport_freccia",
    "enemy_airsupport_griffin",
    "enemy_airsupport_ironsides",
    "enemy_airsupport_petlyakov",
    "enemy_airsupport_rampage",
    "enemy_airsupport_shrike",
    "enemy_airsupport_snotfire",
    "enemy_airsupport_swallow",
    "enemy_airsupport_yakovlev",
    "enemy_antitank_elefant",
    "enemy_antitank_t13",
    "enemy_antitank_jagdpanther",
    "enemy_anzac_gunner_heer6",
    "enemy_batavia_gunner_heer3",
    "enemy_belgae_gunner_heer3",
    "enemy_britannia_gunner_heer2",
    "enemy_britannia_antitank_heer3",
    "enemy_britannia_gunner_heer3",
    "enemy_britannia_marksman_heer3",
    "enemy_britannia_admiral_heer5",
    "enemy_britannia_frogman_heer5",
    "enemy_britannia_pirate_heer6",
    "enemy_britannia_camelcavalry_heer5",
    "enemy_britannia_shark_heer6",
    "enemy_britannia_antitank_heer6",
    "enemy_britannia_gunner_heer6",
    "enemy_britannia_marksman_heer6",
    "enemy_britannia_gunner_heer4",
    "enemy_dania_gunner_heer2",
    "enemy_finbard_gunner_heer7",
    "enemy_finbard_marksman_heer7",
    "enemy_franzo_gunner_heer2",
    "enemy_franzo_gunner_heer3",
    "enemy_franzo_gunner_heer4",
    "enemy_franzo_marksman_heer3",
    "enemy_franzo_marksman_heer4",
    "enemy_germania_antitank_heer1",
    "enemy_germania_antitank_heer5",
    "enemy_germania_antitank_heer7",
    "enemy_germania_gunner_heer1",
    "enemy_germania_gunner_heer5",
    "enemy_germania_gunner_heer7",
    "enemy_germania_marksman_heer5",
    "enemy_grecia_gunner_heer5",
    "enemy_grecia_marksman_heer5",
    "enemy_iraji_gunner_heer6",
    "enemy_commander_churchill",
    "enemy_commander_cyrano",
    "enemy_commander_guderian",
    "enemy_commander_hitora",
    "enemy_commander_nyan",
    "enemy_commander_monty",
    "enemy_commander_negahitora",
    "enemy_commander_roijean",
    "enemy_commander_starin",
    "enemy_commander_zhukky",
    "enemy_meowist_gunner_heer1",
    "enemy_meowist_marksman_heer1",
    "enemy_norda_gunner_heer2",
    "enemy_norda_marksman_heer2",
    "enemy_panzer_47mmapx",
    "enemy_panzer_7tp",
    "enemy_panzer_archer",
    "enemy_panzer_ba10",
    "enemy_panzer_ba10zhina",
    "enemy_panzer_bishopsph",
    "enemy_panzer_bt42",
    "enemy_panzer_charb1",
    "enemy_panzer_charfcm",
    "enemy_panzer_churchill",
    "enemy_panzer_covenanter",
    "enemy_panzer_crusader",
    "enemy_panzer_felthaubits",
    "enemy_panzer_hotchkiss",
    "enemy_panzer_is2",
    "enemy_panzer_konigstiger",
    "enemy_panzer_kv1",
    "enemy_panzer_kv12",
    "enemy_panzer_kv2",
    "enemy_panzer_l335",
    "enemy_panzer_l335zhina",
    "enemy_panzer_matilda1",
    "enemy_panzer_matilda2",
    "enemy_panzer_maus",
    "enemy_panzer_mech",
    "enemy_panzer_odessa",
    "enemy_panzer_panther",
    "enemy_panzer_pantserwagen",
    "enemy_panzer_panzer2",
    "enemy_panzer_panzer3",
    "enemy_panzer_panzer38t",
    "enemy_panzer_panzer4",
    "enemy_panzer_renaultft",
    "enemy_panzer_renaultftzipangu",
    "enemy_panzer_renaultr3540",
    "enemy_panzer_renaultr35serpana",
    "enemy_panzer_semovente",
    "enemy_panzer_somuas35",
    "enemy_panzer_stug4",
    "enemy_panzer_su100",
    "enemy_panzer_t34",
    "enemy_panzer_t35",
    "enemy_panzer_toldi",
    "enemy_panzer_tiger",
    "enemy_panzer_tks",
    "enemy_panzer_ursus",
    "enemy_panzer_valentine",
    "enemy_partisan_gunner_heer4",
    "enemy_partisan_marksman_heer4",
    "enemy_polix_cavalry_heer1",
    "enemy_polix_gunner_heer1",
    "enemy_rumanum_antitank_heer7",
    "enemy_rumanum_cavalry_heer7",
    "enemy_rumanum_gunner_heer7",
    "enemy_serpana_antitank_heer5",
    "enemy_serpana_gunner_heer5",
    "enemy_shifta_gunner_heer4",
    "enemy_sovia_antitank_heer2",
    "enemy_sovia_gunner_heer2",
    "enemy_sovia_marksman_heer2",
    "enemy_sovia_antitank_heer7",
    "enemy_sovia_gunner_heer7",
    "enemy_sovia_marksman_heer7",
    "enemy_sovia_cavalry_heer7",
    "enemy_vitalia_gunner_heer3",
    "enemy_westafrikaa_gunner_heer3",
    "enemy_zhina_gunner_heer1",
    "enemy_zhina_marksman_heer1",
    "enemy_zombie_gunner_heer8" 
    ]

default skills_set = [
    "main1_attack_120mmhowitzer",
    "main1_attack_20k",
    "main1_attack_41m75mm",
    "main1_attack_42m40mm",
    "main1_attack_47model1931",
    "main1_attack_47sa35",
    "main1_attack_47sa37",
    "main1_attack_75modele",
    "main1_attack_ampulomet",
    "main1_attack_beretta38",
    "main1_attack_bofors37",
    "main1_attack_breda20",
    "main1_attack_bredasafat",
    "main1_attack_browningm2",
    "main1_attack_cannoneda47",
    "main1_attack_carcano",
    "main1_attack_d10",
    "main1_attack_d25122mm",
    "main1_attack_dshk",
    "main1_attack_emp",
    "main1_attack_faustpatrone",
    "main1_attack_g7atorpedo",
    "main1_attack_gunto",
    "main1_attack_hs404cannon",
    "main1_attack_kar98k_heer1",
    "main1_attack_kar98k_heer3",
    "main1_attack_kar98k_heer5",
    "main1_attack_kar98k_heer7",
    "main1_attack_karabinek29",
    "main1_attack_kragjorgensen",
    "main1_attack_kt28",
    "main1_attack_kwk30l55",
    "main1_attack_kwk36l56",
    "main1_attack_kwk38l42",
    "main1_attack_kwk38l47",
    "main1_attack_kwk40l48",
    "main1_attack_kwk42l70",
    "main1_attack_kwk43l71",
    "main1_attack_kwk44l55",
    "main1_attack_lanchester",
    "main1_attack_leeenfield",
    "main1_attack_luger",
    "main1_attack_m10thowitzer",
    "main1_attack_m24",
    "main1_attack_madsen",
    "main1_attack_mannlicher",
    "main1_attack_mas36",
    "main1_attack_mavag105mm",
    "main1_attack_megaresister",
    "main1_attack_mg131",
    "main1_attack_mg34",
    "main1_attack_mg81",
    "main1_attack_mgff",
    "main1_attack_mk108cannon",
    "main1_attack_mosinnagant",
    "main1_attack_mp40_heer1",
    "main1_attack_mp40_heer3",
    "main1_attack_mp40_heer5",
    "main1_attack_mp40_heer7",
    "main1_attack_nkmwz38fk",
    "main1_attack_obice7518m34",
    "main1_attack_panzerbuchse",
    "main1_attack_pak36",
    "main1_attack_pak39",
    "main1_attack_pak40",
    "main1_attack_pak43",
    "main1_attack_pak44",
    "main1_attack_pak47",
    "main1_attack_piat",
    "main1_attack_ppsh41",
    "main1_attack_prismblast",
    "main1_attack_purge",
    "main1_attack_puteauxl21",
    "main1_attack_puteauxsa18",
    "main1_attack_qf2pounder",
    "main1_attack_qf17pounder",
    "main1_attack_qf25pounder",
    "main1_attack_qf45howitzer",
    "main1_attack_qf75mm",
    "main1_attack_sa35",
    "main1_attack_shkas",
    "main1_attack_solothurn20mm",
    "main1_attack_szablasabre",
    "main1_attack_thompson_heer1",
    "main1_attack_thompson_heer3",
    "main1_attack_thompson_heer5",
    "main1_attack_thompson_heer7",
    "main1_attack_type100smg",
    "main1_attack_type99arisaka",
    "main1_attack_type24maxim",
    "main1_attack_vickersmg",
    "main1_attack_zhashkasabre",
    "main1_attack_zis5",
    "main2_attack_38mgebauermg",
    "main2_attack_besamg",
    "main2_attack_bombardment",
    "main2_attack_bouncingbomb",
    "main2_attack_breda38", 
    "main2_attack_brenlmg",
    "main2_attack_dive",
    "main2_attack_dp27", 
    "main2_attack_dshk",
    "main2_attack_emp",
    "main2_attack_enemygermanianstrafe", 
    "main2_attack_fistsoffury",
    "main2_attack_granatobronny",
    "main2_attack_grenade",
    "main2_attack_hotchkissm1914",
    "main2_attack_hurricane",
    "main2_attack_kar98k_heer1",
    "main2_attack_kar98k_heer3",
    "main2_attack_kar98k_heer5",
    "main2_attack_kar98k_heer7",
    "main2_attack_katyusha",
    "main2_attack_lewismg",
    "main2_attack_limonka",
    "main2_attack_limpetmine",
    "main2_attack_m1918bar",
    "main2_attack_mg151",
    "main2_attack_mg17",
    "main2_attack_mg34", 
    "main2_attack_mg37",
    "main2_attack_millsbomb",
    "main2_attack_mle1939",
    "main2_attack_molotovcocktail", 
    "main2_attack_pak184",
    "main2_attack_pose",
    "main2_attack_reibelmg",
    "main2_attack_rp3",
    "main2_attack_rrab3",
    "main2_attack_sa35",
    "main2_attack_stielhandgranate", 
    "main2_attack_tellermine",
    "main2_attack_type97grenade",
    "main2_attack_type99arisaka",
    "main2_attack_typelgrenade",
    "main2_attack_veldhandgranaat",
    "special1_attack_brainwash",
    "special1_attack_brains",
    "special1_attack_cyberstrike", 
    "special1_attack_electricstorm",
    "special1_attack_finesthour",
    "special1_attack_fireball",
    "special1_attack_fistsoffury",
    "special1_attack_groundpound",
    "special1_attack_iceburst",
    "special1_attack_polka",
    "special1_attack_quickattack",
    "special1_attack_sandstorm",
    "special1_attack_sovianwinter",
    "special1_attack_strafe", 
    "special1_attack_germanianstrafe", 
    "special1_attack_britanniaanthem",
    "special1_attack_franzoanthem",
    "special1_attack_germaniaanthem",
    "special1_attack_soviaanthem",
    "special1_attack_vitaliaanthem",
    "special1_attack_cutlass",
    "special1_attack_boomerang",
    "special1_attack_chomp",
    "special1_attack_quickmarch",
    "special1_attack_armeemesser",
    "special1_attack_enemygermanianstrafe",
    "special2_attack_baguette",
    "special2_attack_bolognese", 
    "special2_attack_bushido",
    "special2_attack_desertfox", 
    "special2_attack_flamesofwar",
    "special2_attack_frozenwinter",
    "special2_attack_mustardgas",
    "special2_attack_nanoattack",
    "special2_attack_patience",
    "special2_attack_redgeneralissima",
    "special2_attack_samurai",
    "special2_attack_scarletrevolution",
    "special2_attack_shockwave",
    "special2_attack_thousandyearstrike",
    "special2_attack_truebalance",
    "special2_attack_breakthrough",
    "special2_attack_flatten",
    "special2_attack_rundown",
    "special2_attack_smush",
    "special2_attack_snowball",
    "special3_attack_absorb",
    "special3_attack_autumnbreeze",
    "special3_attack_crusade",
    "special3_attack_doppelganger",
    "special3_attack_drain",
    "special3_attack_earthstrike",
    "special3_attack_fissure",
    "special3_attack_northexpedition",
    "special3_attack_leech",
    "special3_attack_powerofrenin",
    "special3_attack_pureevil",
    "special3_attack_rainyseason",
    "special3_attack_summerdance",
    "special3_attack_typhoon",
    "special3_attack_moraleshock",
    "special3_attack_battlecry",
    "special3_attack_clogkick",
    "special3_attack_sprouts",
    "special3_attack_teacup",
    "special3_attack_walkingstick",
    "main1_powerup_megaaccuracy",
    "main1_powerup_megaarmor",
    "main1_powerup_megacharm",
    "main1_powerup_megapower",
    "main1_powerup_megaspeed",
    "main1_powerup_xaccuracy",
    "main1_powerup_xarmor",
    "main1_powerup_xcharm",
    "main1_powerup_xpower",
    "main1_powerup_xspeed",
    "main2_powerup_aimup",
    "main2_powerup_bunkerin",
    "main2_powerup_positivity",
    "main2_powerup_blitz",
    "main2_powerup_stukatablets",
    "heal_maintenance_heer1",
    "heal_maintenance_heer2",
    "heal_maintenance_heer3",
    "heal_maintenance_heer4",
    "heal_maintenance_heer5",
    "heal_maintenance_heer6",
    "heal_maintenance_heer7",
    "heal_maintenance_heer8",
    "heal_medikit_heer1",
    "heal_medikit_heer2",
    "heal_medikit_heer3",
    "heal_medikit_heer4",
    "heal_medikit_heer5",
    "heal_medikit_heer6",
    "heal_medikit_heer7",
    "heal_medikit_heer8",
    "heal_regeneration_churchill",
    "heal_regeneration_nyan",
    "heal_regeneration_starin"
    ]

default axle_fighter_set = [
    "infantry_germania_gunner_heer1",
    "infantry_germania_marksman_heer1",
    "infantry_germania_antitank_heer1",
    "panzer_panzer1",
    "antitank_pak36"
    ]

default alliance_fighter_set = [
    "infantry_franzo_gunner_heer4",
    "infantry_franzo_marksman_heer4",
    "commander_roijean",
    "panzer_renaultft"
    ]

default albion_fighter_set = [
    "infantry_germania_gunner_heer3",
    "infantry_germania_marksman_heer3",
    "infantry_germania_antitank_heer3",
    "panzer_panzer2",
    "panzer_panzer3",
    "panzer_panzer38t",
    "panzer_l335",
    "panzer_bt42",
    "antitank_panzerjager",
    "specialgroup_vitalia_marksman_heer3",
    "specialgroup_vitalia_gunner_heer3",
    "specialgroup_finbard_gunner_heer2",
    "specialgroup_finbard_marksman_heer2",
    "specialgroup_nord_gunner_heer2"
    ]
    
default afrikaakorps_fighter_set = [
    "commander_rommel",
    "specialgroup_afrikaakorps_antitank_heer5",
    "specialgroup_afrikaakorps_gunner_heer5",
    "panzer_l335",
    "panzer_semovente",
    "panzer_panzer1",
    "panzer_panzer2",
    "panzer_panzer3",
    "panzer_panzer38t",
    "panzer_panzer4",
    "panzer_stug3",
    "antitank_panzerjager",
    "antitank_marder"
    ]

default vitalia_fighter_set = [
    "panzer_carroarmato",
    "specialgroup_vitalia_gunner_heer3",
    "specialgroup_vitalia_marksman_heer3"
    ]

default sovia_fighter_set = [
    "infantry_sovia_gunner_heer7",
    "infantry_sovia_marksman_heer7",
    "panzer_t34",
    "panzer_kv1"
    ]

default power_up_status = {
    "name": "Hyper",
    "colour": "#000000",
    "desc": "Player be powerful",
    "boost": {
        "attack": "double"
    },
    "turns_remaining": 4,
    "chance": 0
}

default speed_up_status = {
    "name": "Speedy",
    "colour": "#000000",
    "desc": "Player be speedy",
    "boost": {
        "speed": "triple"
    },
    "turns_remaining": 4,
    "chance": 0
}

default aimup_status = {
    "name": "Aim Up",
    "colour": "#000000",
    "desc": "",
    "boost": {
        "accuracy": "double"
    },
    "turns_remaining": 4,
    "chance": 50
}

default bunkerin_status = {
    "name": "Bunker In",
    "colour": "#000000",
    "desc": "",
    "boost": {
        "defense": "double"
    },
    "turns_remaining": 4,
    "chance": 50
}

default positivity_status = {
    "name": "Positivity",
    "colour": "#000000",
    "desc": "",
    "boost": {
        "critical": "double"
    },
    "turns_remaining": 4,
    "chance": 50
}

default blitz_status = {
    "name": "Blitz",
    "colour": "#000000",
    "desc": "",
    "boost": {
        "attack": "double"
    },
    "turns_remaining": 4,
    "chance": 50
}

default stukatablets_status = {
    "name": "Ztuka Tablets",
    "colour": "#000000",
    "desc": "",
    "boost": {
        "speed": "double"
    },
    "turns_remaining": 4,
    "chance": 50
}

default megaaccuracy_status = {
    "name": "Mega-Accuracy",
    "colour": "#000000",
    "desc": "",
    "boost": {
        "accuracy": "triple"
    },
    "turns_remaining": 6,
    "chance": 45
}

default megaarmor_status = {
    "name": "Mega-Armor",
    "colour": "#000000",
    "desc": "",
    "boost": {
        "defense": "triple"
    },
    "turns_remaining": 6,
    "chance": 45
}

default megacharm_status = {
    "name": "Mega-Critical",
    "colour": "#000000",
    "desc": "",
    "boost": {
        "critical": "triple"
    },
    "turns_remaining": 6,
    "chance": 45
}

default megapower_status = {
    "name": "Mega-Power",
    "colour": "#000000",
    "desc": "",
    "boost": {
        "attack": "triple"
    },
    "turns_remaining": 6,
    "chance": 45
}

default megaspeed_status = {
    "name": "Mega-Speed",
    "colour": "#000000",
    "desc": "",
    "boost": {
        "speed": "triple"
    },
    "turns_remaining": 6,
    "chance": 45
}

default xaccuracy_status = {
    "name": "X-Accuracy",
    "colour": "#000000",
    "desc": "",
    "boost": {
        "accuracy": "quadruple"
    },
    "turns_remaining": 8,
    "chance": 40
}

default xarmor_status = {
    "name": "X-Armor",
    "colour": "#000000",
    "desc": "",
    "boost": {
        "defense": "quadruple"
    },
    "turns_remaining": 8,
    "chance": 40
}

default xcharm_status = {
    "name": "X-Critical",
    "colour": "#000000",
    "desc": "",
    "boost": {
        "critical": "quadruple"
    },
    "turns_remaining": 8,
    "chance": 40
}

default xpower_status = {
    "name": "X-Power",
    "colour": "#000000",
    "desc": "",
    "boost": {
        "attack": "quadruple"
    },
    "turns_remaining": 8,
    "chance": 40
}

default xspeed_status = {
    "name": "X-Speed",
    "colour": "#000000",
    "desc": "",
    "boost": {
        "speed": "quadruple"
    },
    "turns_remaining": 8,
    "chance": 40
}

default burn_status = {
    "name": "Burn",
    "colour": "#000000",
    "desc": "Burn",
    "boost": {
        "effect": "skip"
    },
    "turns_remaining": 2,
    "chance": 10
}

default stun_status = {
    "name": "Stun",
    "colour": "#000000",
    "desc": "Stun",
    "boost": {
        "effect": "skip"
    },
    "turns_remaining": 2,
    "chance": 50
}

default runover_status = {
    "name": "Runover",
    "colour": "#000000",
    "desc": "Runover",
    "boost": {
        "effect": "skip"
    },
    "turns_remaining": 4,
    "chance": 25
}

default breakthrough_status = {
    "name": "Breakthrough",
    "colour": "#000000",
    "desc": "Breakthrough",
    "boost": {
        "effect": "skip",
        "speed": "half",
        "accuracy": "half",
        "critical": "half"
    },
    "turns_remaining": 2,
    "chance": 40
}

default morale_status = {
    "name": "Morale",
    "colour": "#000000",
    "desc": "Morale",
    "boost": {
        "effect": "skip"
    },
    "turns_remaining": 2,
    "chance": 33
}

default perk_firepower_description = "This fighter packs a punch, with powerful attack moves."
default perk_speed_description = "This fighter is speedy, moving quickly into action."
default perk_explosive_description = "This fighter has explosive firepower, using explosions to win."
default perk_spacedarmor_description = "This fighter has strong armor, avoiding enemy fire."
default perk_slopedarmor_description = "This fighter has strong armor and a high defense."
default perk_heal_description = "This fighter can heal quickly."
default perk_stealth_description = "This fighter is stealthy, moving with speed and accuracy."
default perk_lightweight_description = "This fighter is lightweight, easily overwhelmed by bigger opponents."
default perk_bruteforce_description = "This fighter uses brute force to overwhelm its opponents."
default perk_dark_description = "This fighter uses dark mana to destroy its enemies."
default perk_electric_description = "This fighter uses electric mana to zap its enemies."
default perk_flame_description = "This fighter uses flame mana to burn its enemies."
default perk_ice_description = "This fighter uses ice mana to freeze its enemies."
default perk_slash_description = "This fighter attacks sharply, slashing at their opponents."
default perk_wind_description = "This fighter floats on the wind, quick and nimble."
default perk_valkyrie_description = "This fighter follows blindly, attacking forcefully."
default perk_angel_description = "This fighter uses light mana to blind its enemies."
default x_description = ""

#############################################################################################
#  DATA  #####################################################################################
#############################################################################################
init +2 python:
    mapdata = ScreenData("geomap1", "map1", "easternmap")

init python:
    import math
    config.skip_indicator = None
    
    achievement.register("ENDING_BADENDING1")
    achievement.register("ENDING_BADENDING2")
    achievement.register("ENDING_BADENDING3")
    achievement.register("BATTLE_BEATNYAN1")
    achievement.register("COMPLETE_EVANSTORY")
    achievement.register("COMPLETE_DOUCHESTORY")
    achievement.register("BATTLE_BEATZHUKKY1")
    achievement.register("BATTLE_BEATCHURCHILL1")
    achievement.register("BATTLE_BEATREINEJEAN1")
    achievement.register("BATTLE_BEATCYRANO1")
    achievement.register("BATTLE_BEATCHURCHILL2")
    achievement.register("BATTLE_BEATNEGAHITORA1")
    achievement.register("BATTLE_BEATMONTY1")
    achievement.register("BATTLE_BEATGUDERIAN1")
    achievement.register("BATTLE_BEATSTARIN1")
    achievement.register("BATTLE_BEATHITORA1")
    achievement.register("COMPLETE_MUSEUM")
    achievement.register("ENDING_NEUTRAL_ROUTE")
    achievement.register("ENDING_HITORA_ROUTE")
    achievement.register("ENDING_STARIN_ROUTE")
    achievement.register("ENDING_CYRANO_ROUTE")
    achievement.register("ENDING_CHURCHILL_ROUTE")
    
init:
    $ config.keymap['hide_windows'].remove('mouseup_2')
    $ config.keymap['viewport_drag_start'].append('mousedown_2')
    $ config.keymap['viewport_drag_end'].append('mouseup_2')
    
    default level_choice = None
    default level_easy_tooltip = "Begin with increased {color=#F35F5F}Command Points (CP){/color} and receive more {color=#F35F5F}CP{/color} after battles as well. {color=#F35F5F}Skip Battle{/color} is always enabled."
    default level_normal_tooltip = "Begin with average {color=#F35F5F}Command Points (CP){/color} and receive regular {color=#F35F5F}CP{/color} after battles. {color=#F35F5F}Skip Battle{/color} is enabled after losing a battle once."
    default level_hard_tooltip = "Begin with fewer {color=#F35F5F}Command Points (CP){/color} and receive less {color=#F35F5F}CP{/color} after battles as well. {color=#F35F5F}Skip Battle{/color} is always disabled."
    
    default breakpoint_hitora_apology = False
    default breakpoint_alliance_onside = False
    
    default current_campaign = None
    
    default routechoice_axis = False
    default routechoice_allied = False
    default routechoice_sovian = False
    
    default dresckow1chat = True
    
    default save_name = "My Little Dictator"
    
    default resistance_campaign_unlocked = False
    default totalwar_campaign_unlocked = False
    default evan_campaign_unlocked = False
    default tito_campaign_unlocked = False
    default nyan_campaign_unlocked = False
    
    default conquest_campaign_completed = False
    default resistance_campaign_completed = False
    default totalwar_campaign_completed = False
    default evan_campaign_completed = False
    default tito_campaign_completed = False
    default nyan_campaign_completed = False
    
    default choice_delicatanken_answered = False
    default choice_starinteatime_answered = False
    default choice_cyranodate_answered = False
    
    default hitora_love = 0
    default cyrano_love = 0
    default churchill_love = 0
    default starin_love = 0
    
    default campaign_yamato_show = True
    
    default codex_unlocked = False

    default mapcontinue = ""
    default q_description = ""
    default q_title = ""
    default q_type = 0
        
    default disclaimer_text = "{i}My Little Dictator{/i} is the intellectual and commercial property of {i}WarGirl Games{/i}. The fictional story, setting and characters contained within are the intellectual property of the developers.\n\nAll characters, names, businesses, places, products, events and incidents appearing in this work are fictional. Any resemblance to any real persons, living or dead, is purely coincidental. No identification with actual persons (living or deceased), names, businesses, places, products, events or incidents is intended or should be inferred. This game is a fictional work of parody, featuring caricature as well as satire, and contains suggestive content. This game was designed and developed by a global team of creatives of various beliefs, backgrounds and ethnicities.\n\nThe makers of this game do not condone, endorse or encourage engaging in any conduct depicted in this game. This game contains references to warfare and war crimes, violence, genocide, jingoism, imperialism, fascism, communism, dictatorship, racial and ethnic stereotyping, intolerance, propaganda, suicide, alcohol, tobacco, nudity and themes of a sexual nature. As such, player discretion is strongly advised."
    default post_disclaimer_text = "Our story takes place in a world similar to our own yet vastly different.\n\nA world in which the figures of history are cute anime girls . . ."
        
    default fuuhbarmuseum_description = "The Füühbar has decreed the opening of a new museum of culture, right in the heart of Germania. As the armies of the {i}Axle{/i} march across Europa, works of art, world wonders, architecture and other valuables are to be stolen and displayed as exhibits here. Goring in particular hopes to steal as much as she can get her grubby fingers on."
        
    default captured_arch_name = "Arc de Trompette"
    default captured_bank_name = "Bank of Britannia"
    default captured_barmaleyfountain_name = "Barley Fountain"
    default captured_beerhall_name = "Beer hall"
    default captured_woodenbench_name = "Wooden bench"
    default captured_bigben_name = "Albion Clocktower"
    default captured_bollard_name = "Bollard"
    default captured_bones_name = "Dinosaur bones"
    default captured_brandenburggate_name = "Brandybutter Gate"
    default captured_brickhouse_name = "Red brick house"
    default captured_bunker_name = "Bunker"
    default captured_bush_name = "Bush"
    default captured_cafe_name = "Cafe"
    default captured_zhinahouse_name = "Zhina house"
    default captured_zhinatemple_name = "Zhina temple"
    default captured_zhinathrone_name = "Dragon Throne"
    default captured_church_name = "Church"
    default captured_cottage_name = "Cottage"
    default captured_crate_name = "Mystery crate"
    default captured_debris_name = "Debris"
    default captured_deserthouse_name = "Desert house"
    default captured_desertrocks_name = "Desert rocks"
    default captured_desertruins_name = "Desert ruins"
    default captured_deserttower_name = "Watch tower"
    default captured_dragonteeth_name = "Dragon's teeth"
    default captured_eiffel_name = "Tower of Lutetia"
    default captured_factory_name = "Factory"
    default captured_farmhousesnow_name = "Farmhouse"
    default captured_flat_name = "Apartment"
    default captured_forest_name = "Forest"
    default captured_fountainbig_name = "Large fountain"
    default captured_fountainsmall_name = "Small fountain"
    default captured_gear_name = "Gear"
    default captured_guardtower_name = "Guard tower"
    default captured_hangar_name = "Hangar"
    default captured_hedgehog_name = "Czexa hedgehog"
    default captured_hut_name = "Hut"
    default captured_iceberg_name = "Iceberg"
    default captured_kremlin_name = "The Xremlin"
    default captured_lamppost_name = "Lamp post"
    default captured_machinegunnest_name = "Machine gun nest"
    default captured_mansion_name = "Mansion"
    default captured_market_name = "Bazaar"
    default captured_mosque_name = "Mosque"
    default captured_palace_name = "The Reflecting Palace"
    default captured_palmtree_name = "Palm tree"
    default captured_pillbox_name = "Pillbox"
    default captured_postbox_name = "Britannian postbox"
    default captured_pyramid_name = "The Great Pyramid"
    default captured_radiotower_name = "Radio tower"
    default captured_sandbag_name = "Sandbags"
    default captured_shrub_name = "Shrubbery"
    default captured_snowyrocks_name = "Snow-covered rocks"
    default captured_stalagmite_name = "Stalagmite"
    default captured_statueeagle_name = "Eagle statue"
    default captured_statuekaiser_name = "Kaiserin statue"
    default captured_statueman_name = "Supermann statue"
    default captured_statuewoman_name = "Superfrau statue"
    default captured_sweat_name = "Sweat"
    default captured_table_name = "Dining set"
    default captured_temple_name = "Grecian temple"
    default captured_tent_name = "Tent"
    default captured_terrace_name = "Terrace house"
    default captured_theater_name = "Opera house"
    default captured_train_name = "Foch's train carriage"
    default captured_vases_name = "Ming vases"
    default captured_wheat_name = "Wheat"
    default captured_woodland_name = "Woodland"
        
    default captured_arch_description = "Taken from Lutetia, commissioned by the Empress Napoleon after a victory, this archway takes inspiration from Vitalian architecture. It is a symbol of Franzo's past glory and arrogance."
    default captured_bank_description = "An example of a modern bank. Financial institutions like these can create much opportunity and wealth, but also lead to a nation's ruin. The Füühbar is very skeptical of places like these and their employees."
    default captured_barmaleyfountain_description = "This fountain was located in Staringrada and is an important symbol of that campaign. The statue depicts children holding hands and dancing around a crocodile."
    default captured_beerhall_description = "An example of a beer hall. The Füühbar's regime and rhetoric had their foundations in places like these, where she often gave fiery speeches as a young girl."
    default captured_woodenbench_description = "It's a wooden bench. What did you expect?"
    default captured_bigben_description = "This clocktower was constructed in the last century, when the old Palace of Albion was destroyed in a fire. It is the seat of Britannian government and the headquarters of their leader."
    default captured_bollard_description = "A bollard. What did you expect?"
    default captured_bones_description = "Hey, who doesn't love dinosaurs?"
    default captured_brandenburggate_description = "This mighty gate stands at the center of Altberlin and is considered a symbol of unity. The Füühbar has kindly loaned it to the Füühbarmuseum for its exhibition."
    default captured_brickhouse_description = "This red brick house is an example of an ordinary worker's dwelling. Found both within cities and in the countryside, they are relatively unexceptional."
    default captured_bunker_description = "Bunkers are fine places. The Füühbar even has her own personal bunker, right here in Altberlin. Just in case."
    default captured_bush_description = "A fine example of Europa's natural vegetation."
    default captured_cafe_description = "A national pastime in the west is to waste time drinking coffee and lounging around in cafes."
    default captured_zhinahouse_description = "An example of an ordinary dwelling for a Zhinese citizen."
    default captured_zhinatemple_description = "An example of a Zhinese place of worship. The magnificent architecture helps it to stand out from Europa's buildings."
    default captured_zhinathrone_description = "This is the throne of the former imperial family of Zhina. It once sat in the {i}Hall of Supreme Harmony{/i}. Following the fall of the monarchy and revolution, it was claimed by Nyan Katshex as her birthright."
    default captured_church_description = "A place of worship for many across Europa, the Füühbar actually dislikes the Church's tenets, and prefers her own cult of personality."
    default captured_cottage_description = "An example of an ordinary dwelling for Europa's tenant farmers."
    default captured_crate_description = "A mysterious crate. Who knows what could be inside?"
    default captured_debris_description = "I don't know why you picked this up, but I guess it can have its own exhibit . . ."
    default captured_deserthouse_description = "An example of an ordinary dwelling for colonial subjects in the southern deserts."
    default captured_desertrocks_description = "I guess they are a unique color. The orange and yellow tint comes from exposure to sun and sand, bleaching the outer surface of the rock."
    default captured_desertruins_description = "These mysterious ruins are an example of ancient culture. Managing to sneak this out of the country without the locals noticing must have been a feat."
    default captured_deserttower_description = "Fortress towns throughout the southern deserts rely on maintaining a unique vantage over the empty plains. This tower is an example of the architecture found throughout these shores."
    default captured_dragonteeth_description = "These anti-tank defenses are made from reinforced concrete and intended to trap enemy {i}Panzy{/i} into kill zones."
    default captured_eiffel_description = "This tower was constructed late in the last century, in time for the World Fair. Many see it as a symbol of Franzo's modernity and a testament to the industrial might of the western nation."
    default captured_factory_description = "An example of the industrial might of the peoples of Europa. Raw materials, synthetics, consumer goods and military materiel are produced daily by these sturdy factories in each and every nation."
    default captured_farmhousesnow_description = "Longhouses like this are extremely fashionable in the north."
    default captured_flat_description = "A depressing example of inner-city housing, found throughout the towerblocks of Europa. Despised by most, these architectural monstrosities make for easy targets."
    default captured_forest_description = "The forests of Europa are wild and untamed places, full of mighty pines, oaks and beeches."
    default captured_fountainbig_description = "An example of the brilliance of Europa art, architecture and engineering. Tall fountains like these are big tourist traps in the major cities."
    default captured_fountainsmall_description = "An imitation of the brilliance of Europa art, architecture and engineering."
    default captured_gear_description = "A large metal gear, taken from the Albion Clocktower's winding mechanism."
    default captured_guardtower_description = "Wooden guard towers like these are often used at low-security installations or temporary defensive lines, such as in POW camps deep behind enemy lines."
    default captured_hangar_description = "Made from corrugated galvanised iron, hangars like these are in operation across Europa. Large aircraft are maintained and stored in them, and they can be found on airfields."
    default captured_hedgehog_description = "Made from study metal, this anti-tank defense helps to slow an enemy advance. It is most effective in trapping light vehicles from penetrating defensive lines."
    default captured_hut_description = "Temporary wooden huts like these are usually found in barracks, airfields or POW camps. Either used for storage or as living quarters."
    default captured_iceberg_description = "How did you get this back without it melting?"
    default captured_kremlin_description = "The {i}Xremlin{/i} is adjacent to {i}Scarlet Square{/i}, a large public area used for military marches and displays of new weapons."
    default captured_lamppost_description = "An example of a modern lamp post. The vast majority are still lit by gas, but recent innovations in science have led to the first electrical lamp posts being installed across Europa."
    default captured_machinegunnest_description = "An example of a machine gun nest formation."
    default captured_mansion_description = "An example of upper class housing. The decadent bourgeoisie own mansions like these throughout Europa."
    default captured_market_description = "Bazaars are marketplaces common to the southern deserts. Goods of all kinds are bartered and traded on a daily basis."
    default captured_mosque_description = "A place of worship for many on the southern shores. The Füühbar somewhat admires their religion."
    default captured_palace_description = "In this beautiful palace, the treaty that formally ended the last great war was signed. Capturing it holds great significance for Germania."
    default captured_palmtree_description = "Trees like these grow all along the southern shores, preferring the warm climate and arid conditions."
    default captured_pillbox_description = "Pillboxes and cloche, such as these, are fixed fortifications intended primarily as lookout posts. Made of cast iron or concrete, they are a useful first line of defense and allow for engagement with light weapons."
    default captured_postbox_description = "Little red mailboxes like these can be found throughout the Britannian isles."
    default captured_pyramid_description = "In the ancient world, the Gyptans ruled the southern shores in millennia old dynasties. A mysterious people noted for their ingenuity, they have long been a topic of fascination in Europa."
    default captured_radiotower_description = "The wireless radio is a marvel of the modern world, and has proven to be an invaluable tool in both propaganda and military terms."
    default captured_sandbag_description = "A sandbag. Handy, sturdy, useful."
    default captured_shrub_description = "First you must find . . . another shrubbery! Ni! Ni! Ni!"
    default captured_snowyrocks_description = "Some rocks, covered in snow. There's probably some significance to these, but I can't see it."
    default captured_stalagmite_description = "Found in caves, this natural formation is rather fetching."
    default captured_statueeagle_description = "The eagle is a powerful symbol of Germanian might and cunning. Its image can be found in architecture, medals, uniforms and official documents."
    default captured_statuekaiser_description = "The Kaiserin united Germania and created the second Empire. This statue, on loan from the Füühbar, commemorates her power and influence on the world stage."
    default captured_statueman_description = "This statue is an example of the {i}Supermann{/i} ideology of the Füühbar's Germania."
    default captured_statuewoman_description = "This statue is an example of the {i}Superfrau{/i} ideology of the Füühbar's Germania."
    default captured_sweat_description = "Eww . . . why did you bring me bottled sweat? I know it's popular in Zipangu but really . . ."
    default captured_table_description = "The Füühbar said she wanted a new dining set, so here's a table and some chairs."
    default captured_temple_description = "An example of Grecian architecture. This temple was built to honor the ancient gods of Athenia. These days, it's a bit of a ruin."
    default captured_tent_description = "An example of an ordinary footsoldier's living quarters."
    default captured_terrace_description = "Terraced housing like this is common for workers in cities throughout Europa."
    default captured_theater_description = "An example of a modern opera house. The Füühbar values the cultural power of the opera, and has been fascinated by the hypnotic power of music since her first visit to one."
    default captured_train_description = "This train carriage was transported to Germania following the fall of Franzo. It is the same car where Foch forced a Germanian delegation to sign a ceasefire, during the last great war."
    default captured_vases_description = "These valuable vases are an example of ancient Zhinese pottery."
    default captured_wheat_description = "It's some golden wheat. The Füühbar wishes to plant much of it in the east once she has conquered enough land."
    default captured_woodland_description = "An example of the light woodland that can be found throughout both Zhina and Europa. Okay, it's a pretty boring exhibit really."
        
    default active_fuuhbarmuseum_items = {
        "captured_statuekaiser": [captured_statuekaiser_name, captured_statuekaiser_description]  
    }
        
    default museum_arch_unlocked = False
    default museum_bank_unlocked = False
    default museum_barmaleyfountain_unlocked = False
    default museum_beerhall_unlocked = False
    default museum_woodenbench_unlocked = False
    default museum_bigben_unlocked = False
    default museum_bollard_unlocked = False
    default museum_bones_unlocked = False
    default museum_brandenburggate_unlocked = False
    default museum_brickhouse_unlocked = False
    default museum_bunker_unlocked = False
    default museum_bush_unlocked = False
    default museum_cafe_unlocked = False
    default museum_zhinahouse_unlocked = False
    default museum_zhinatemple_unlocked = False
    default museum_zhinathrone_unlocked = False
    default museum_church_unlocked = False
    default museum_cottage_unlocked = False
    default museum_crate_unlocked = False
    default museum_debris_unlocked = False
    default museum_deserthouse_unlocked = False
    default museum_desertrocks_unlocked = False
    default museum_desertruins_unlocked = False
    default museum_deserttower_unlocked = False
    default museum_dragonteeth_unlocked = False
    default museum_eiffel_unlocked = False
    default museum_factory_unlocked = False
    default museum_farmhousesnow_unlocked = False
    default museum_flat_unlocked = False
    default museum_forest_unlocked = False
    default museum_fountainbig_unlocked = False
    default museum_fountainsmall_unlocked = False
    default museum_gear_unlocked = False
    default museum_guardtower_unlocked = False
    default museum_hangar_unlocked = False
    default museum_hedgehog_unlocked = False
    default museum_hut_unlocked = False
    default museum_iceberg_unlocked = False
    default museum_kremlin_unlocked = False
    default museum_lamppost_unlocked = False
    default museum_machinegunnest_unlocked = False
    default museum_mansion_unlocked = False
    default museum_market_unlocked = False
    default museum_mosque_unlocked = False
    default museum_palace_unlocked = False
    default museum_palmtree_unlocked = False
    default museum_pillbox_unlocked = False
    default museum_postbox_unlocked = False
    default museum_pyramid_unlocked = False
    default museum_radiotower_unlocked = False
    default museum_sandbag_unlocked = False
    default museum_shrub_unlocked = False
    default museum_snowyrocks_unlocked = False
    default museum_stalagmite_unlocked = False
    default museum_statueeagle_unlocked = False
    default museum_statuekaiser_unlocked = True
    default museum_statueman_unlocked = False
    default museum_statuewoman_unlocked = False
    default museum_sweat_unlocked = False
    default museum_table_unlocked = False
    default museum_temple_unlocked = False
    default museum_tent_unlocked = False
    default museum_terrace_unlocked = False
    default museum_theater_unlocked = False
    default museum_train_unlocked = False
    default museum_vases_unlocked = False
    default museum_wheat_unlocked = False
    default museum_woodland_unlocked = False
        
    default company_albioncornexchange_name = "Albion Corn Exchange"
    default company_axemann_name = "Axe Mann"
    default company_caveavin_name = "Cave a vin"
    default company_dokuk_name = "Dokuk"
    default company_ducepasta_name = "Douché Pasta"
    default company_freedomburger_name = "Freedom Burger"
    default company_fuuhbarcakes_name = "Füühbarcakes"
    default company_ghoulish_name = "Ghoulish Goulash"
    default company_grupp_name = "Grupp"
    default company_guptatours_name = "Gupta Tours"
    default company_handlarz_name = "Handlarz Majtki"
    default company_iorginaicecream_name = "Iorgina Ice Cream"
    default company_lugobust_name = "Lugo Bust"
    default company_magische_name = "Magische Mädchenschule"
    default company_molkereiwagen_name = "Molkereiwagen"
    default company_motherofnationspelts_name = "Mother of Nations Pelts"
    default company_ottoflugzeugwerke_name = "Auto-Superflugwerke"
    default company_panpanpan_name = "Pan Pan Pan"
    default company_penguinironworks_name = "Penguin Ironworks"
    default company_petwelt_name = "Pet Welt"
    default company_pizzahaus_name = "Pizza Haus"
    default company_sakurawhale_name = "Sakura Whale Candy"
    default company_southernmining_name = "Southern Mining Conglomerate"
    default company_sovianpotato_name = "Sovian Potato Concern"
    default company_tanfa_name = "Tanfa"
    default company_teaempire_name = "Tea Empire"
    default company_toothhurty_name = "Tooth Hurty"
    default company_victorrubber_name = "Victor's Supreme Collective Rubber Concern"
    default company_woodyslogging_name = "Woody's Logging"
    default company_zippilen_name = "Zippilen"
        
    default company_albioncornexchange_description = "A well-established Britannian corn exchange where farmers can sell and trade their produce."
    default company_axemann_description = "A company that produces tools for forestry work."
    default company_caveavin_description = "A wine company based in Franzo, noted for their excellent vineyards and ancient heritage."
    default company_dokuk_description = "A camera company that also manufactures triggers and other intricate metallic parts."
    default company_ducepasta_description = "A Vitalian pasta restaurant chain, sponsored by Benita Mussorinni herself."
    default company_freedomburger_description = "An Amerikan fast food outlet."
    default company_fuuhbarcakes_description = "A popular bakery that creates all kinds of specialist cakes and pastries. Personal provider of cream puffs to the Füühbar herself."
    default company_ghoulish_description = "A chain of family restaurants that specializes in goulash."
    default company_grupp_description = "Armaments manufacturer, responsible for providing much of Germania's artillery and ammunition."
    default company_guptatours_description = "A tour company that specializes in the ruins of the southern deserts."
    default company_handlarz_description = "A chain of backalley illicit shops. Not for the faint of heart . . ."
    default company_iorginaicecream_description = "A Sovian ice cream company, sponsored by Iorgina Zhukky."
    default company_lugobust_description = "A fashion retail chain that holds an exclusive contract with both the Germanian army and the {i}Nappi Party{/i}."
    default company_magische_description = "An exclusive private girls school. The curriculum is a mystery . . ."
    default company_molkereiwagen_description = "An automobile manufacturer. With the Füühbar's encouragement, their aim is to produce affordable cars for ordinary citizens."
    default company_motherofnationspelts_description = "A state-sponsored Sovian pelts and leather company."
    default company_ottoflugzeugwerke_description = "A Germanian aircraft manufacturer."
    default company_panpanpan_description = "A famous bakery based in Franzo, renowned for its cakes and patisseries."
    default company_penguinironworks_description = "A chain of ironworks."
    default company_petwelt_description = "A pet store chain. Provides all kinds of animal-related feed and products."
    default company_pizzahaus_description = "A Vitalian pizza restaurant chain. Not exactly high quality pizza at that . . ."
    default company_sakurawhale_description = "A Zipanguese confectionary company. Don't ask what the secret ingredient is . . ."
    default company_southernmining_description = "A southern mining company."
    default company_sovianpotato_description = "A Sovian company dedicated solely to the production of potatoes."
    default company_tanfa_description = "An Amerikan soft drink concern that produces lemon-flavored soda."
    default company_teaempire_description = "A Britannian chain of tearooms and merchants."
    default company_toothhurty_description = "A nationwide chain of dentistry practices. Not to be taken lightly."
    default company_victorrubber_description = "A company that produces and sells rubber."
    default company_woodyslogging_description = "A logging company."
    default company_zippilen_description = "A company that manufactures {i}lighter-than-air{/i} aircraft."
        
    default innercircle_joebbels_name = "{size=20}[profile_joebbels_name]{/size}\n{i}Propagandaministerium{/i}"
    default innercircle_hess_name = "{size=20}[profile_hess_name]{/size}\n{i}Stallvertreter des Füühbars{/i}"
    default innercircle_borkind_name = "{size=20}[profile_borkind_name]{/size}\n{i}Sekretär des Stallvertreter des Füühbars{/i}"
    default innercircle_funk_name = "{size=20}Walther Funk{/size}\n{i}Imperiumswirtschaftsministerium{/i}"
    default innercircle_ribbentrop_name = "{size=20}Joey Lippentrob{/size}\n{i}Imperiumsminister des Auswärtigen{/i}"
    default innercircle_lammers_name = "{size=20}Hans Lammers{/size}\n{i}Chef der Imperiumskanzlei{/i}"
    default innercircle_linge_name = "{size=20}Linge{/size}\n{i}Valet des Füühbars{/i}"
    default innercircle_himmora_name = "{size=20}Heiny Himmora{/size}\n{i}Chef des Zombieztaffel{/i}"
    default innercircle_kanari_name = "{size=20}Kanari{/size}\n{i}Chef des Aberwehr{/i}"
    default innercircle_ooster_name = "{size=20}Ooster{/size}\n{i}Stellvertretender Chef des Aberwehr{/i}"
        
    default active_innercircle_items = {
        "side joebbels scared": innercircle_joebbels_name,
        "side hess normal": innercircle_hess_name,
        "side borkind determined": innercircle_borkind_name,
        "side oldman determined": innercircle_funk_name,
        "side youth shock": innercircle_ribbentrop_name,
        "side politician normal": innercircle_lammers_name,
        "side germaniangeneral normal": innercircle_linge_name,
        "zinnercircle_blank": innercircle_himmora_name,
        "zinnercircle_blank2": innercircle_kanari_name,
        "zinnercircle_blank3": innercircle_ooster_name
    }
        
    default militarycircle_hitora_name = "{size=20}[profile_hitora_name]{/size}\n{i}Oberster Befehlshaber der Vehrmaxt{/i}"
    default militarycircle_brauchitsch_name = "{size=20}[profile_brauchitsch_name]{/size}\n{i}Oberbefehlshaber des Truppe{/i}"
    default militarycircle_keitel_name = "{size=20}[profile_keitel_name]{/size}\n{i}Oberbefehlshaber der Vehrmaxt{/i}"
    default militarycircle_dunitz_name = "{size=20}[profile_dunitz_name]{/size}\n{i}Oberbefehlshaber des See{/i}"
    default militarycircle_goring_name = "{size=20}[profile_goring_name]{/size}\n{i}Imperiumsmarschall{/i}"
    default militarycircle_blank_name = "{size=20}-{/size}\n{i}Chef des Generalstall{/i}"
    default militarycircle_blank2_name = "{size=20}-{/size}\n{i}Chef des Vehrmaxtführungsstabes{/i}"
    default militarycircle_krancke_name = "{size=20}Theosa Krancke{/size}\n{i}Seegruppenkommandos West{/i}"
    default militarycircle_sperrle_name = "{size=20}Hugo Sperrle{/size}\n{i}General der Flieger{/i}"
        
    default active_militarycircle_items = {
        "militarycircle001_brauchitsch": militarycircle_brauchitsch_name,
        "militarycircle002_keitel": militarycircle_keitel_name,
        "militarycircle003_dunitz": militarycircle_dunitz_name,
        "militarycircle004_goring": militarycircle_goring_name,
        "militarycircle005_blank": militarycircle_blank_name,
        "militarycircle006_blank": militarycircle_blank2_name,
        "militarycircle007_krancke": militarycircle_krancke_name,
        "militarycircle008_sperrle": militarycircle_sperrle_name,
    }
        
    default infanteriedivision001_name = "1. Fußtruppe\nDivision"
    default infanteriedivision002_name = "2. Motorized\nDivision"
    default infanteriedivision003_name = "3. Fußtruppe\nDivision"
    default infanteriedivision004_name = "4. Fußtruppe\nDivision"
    default infanteriedivision005_name = "5. Fußtruppe\nDivision"
    default infanteriedivision006_name = "6. Fußtruppe\nDivision"
    default infanteriedivision007_name = "7. Fußtruppe\nDivision"
    default infanteriedivision008_name = "8. Fußtruppe\nDivision"
    default infanteriedivision009_name = "9. Fußtruppe\nDivision"
    default infanteriedivision010_name = "10. Fußtruppe\nDivision"
    default infanteriedivision011_name = "11. Fußtruppe\nDivision"
    default infanteriedivision012_name = "12. Fußtruppe\nDivision"
    default infanteriedivision013_name = "13. Motorized\nDivision"
    default infanteriedivision014_name = "14. Fußtruppe\nDivision"
    default infanteriedivision015_name = "15. Fußtruppe\nDivision"
    default infanteriedivision016_name = "16. Fußtruppe\nDivision"
    default infanteriedivision017_name = "17. Fußtruppe\nDivision"
    default infanteriedivision018_name = "18. Fußtruppe\nDivision"
    default infanteriedivision019_name = "19. Fußtruppe\nDivision"
    default infanteriedivision020_name = "20. Motorized\nDivision"
    default infanteriedivision021_name = "21. Fußtruppe\nDivision"
    default infanteriedivision022_name = "22. Fußtruppe\nDivision"
    default infanteriedivision023_name = "23. Fußtruppe\nDivision"
    default infanteriedivision024_name = "24. Fußtruppe\nDivision"
    default infanteriedivision025_name = "25. Fußtruppe\nDivision"
    default infanteriedivision026_name = "26. Fußtruppe\nDivision"
    default infanteriedivision027_name = "27. Fußtruppe\nDivision"
    default infanteriedivision028_name = "28. Fänger\nDivision"
    default infanteriedivision029_name = "29. Motorized\nDivision"
    default infanteriedivision030_name = "30. Fußtruppe\nDivision"
    default infanteriedivision031_name = "31. Fußtruppe\nDivision"
    default infanteriedivision032_name = "32. Fußtruppe\nDivision"
    default infanteriedivision033_name = "33. Fußtruppe\nDivision"
    default infanteriedivision034_name = "34. Fußtruppe\nDivision"
    default infanteriedivision035_name = "35. Fußtruppe\nDivision"
    default infanteriedivision036_name = "36. Fußtruppe\nDivision"
    default infanteriedivision037_name = "37. Fußtruppe\nDivision"
    default infanteriedivision038_name = "38. Fußtruppe\nDivision"
    default infanteriedivision039_name = "39. Fußtruppe\nDivision"
    default infanteriedivision040_name = "40. Fußtruppe\nDivision"
    default infanteriedivision041_name = "41. Fußtruppe\nDivision"
    default infanteriedivision042_name = "42. Fänger\nDivision"
    default infanteriedivision043_name = "43. Fußtruppe\nDivision"
    default infanteriedivision044_name = "44. Fußtruppe\nDivision"
    default infanteriedivision045_name = "45. Fußtruppe\nDivision"
    default infanteriedivision046_name = "46. Fußtruppe\nDivision"
    default infanteriedivision047_name = "47. Fußtruppe\nDivision"
    default infanteriedivision048_name = "48. Fußtruppe\nDivision"
    default infanteriedivision049_name = "49. Fußtruppe\nDivision"
    default infanteriedivision050_name = "50. Fußtruppe\nDivision"
    default infanteriedivision051_name = "51. Fußtruppe\nDivision"
    default infanteriedivision052_name = "52. Fußtruppe\nDivision"
    default infanteriedivision053_name = "53. Fußtruppe\nDivision"
    default infanteriedivision054_name = "54. Fußtruppe\nDivision"
    default infanteriedivision055_name = "55. Fußtruppe\nDivision"
    default infanteriedivision056_name = "56. Fußtruppe\nDivision"
    default infanteriedivision057_name = "57. Fußtruppe\nDivision"
    default infanteriedivision058_name = "58. Fußtruppe\nDivision"
    default infanteriedivision059_name = "59. Fußtruppe\nDivision"
    default infanteriedivision060_name = "60. Fußtruppe\nDivision"
    default infanteriedivision061_name = "61. Fußtruppe\nDivision"
    default infanteriedivision062_name = "62. Fußtruppe\nDivision"
    default infanteriedivision063_name = "63. Fußtruppe\nDivision"
    default infanteriedivision064_name = "64. Fußtruppe\nDivision"
    default infanteriedivision065_name = "65. Fußtruppe\nDivision"
    default infanteriedivision066_name = "66. Fußtruppe\nDivision"
    default infanteriedivision067_name = "67. Fußtruppe\nDivision"
    default infanteriedivision068_name = "68. Fußtruppe\nDivision"
    default infanteriedivision069_name = "69. Fußtruppe\nDivision"
    default infanteriedivision070_name = "70. Fußtruppe\nDivision"
    default infanteriedivision071_name = "71. Fußtruppe\nDivision"
    default infanteriedivision072_name = "72. Fußtruppe\nDivision"
    default infanteriedivision073_name = "73. Fußtruppe\nDivision"
    default infanteriedivision074_name = "74. Fußtruppe\nDivision"
    default infanteriedivision075_name = "75. Fußtruppe\nDivision"
    default infanteriedivision076_name = "76. Fußtruppe\nDivision"
    default infanteriedivision077_name = "77. Fußtruppe\nDivision"
    default infanteriedivision078_name = "78. Fußtruppe\nDivision"
    default infanteriedivision079_name = "79. Fußtruppe\nDivision"
    default infanteriedivision080_name = "80. Fußtruppe\nDivision"
    default infanteriedivision081_name = "81. Fußtruppe\nDivision"
    default infanteriedivision082_name = "82. Fußtruppe\nDivision"
    default infanteriedivision083_name = "83. Fußtruppe\nDivision"
    default infanteriedivision084_name = "84. Fußtruppe\nDivision"
    default infanteriedivision085_name = "85. Fußtruppe\nDivision"
    default infanteriedivision086_name = "86. Fußtruppe\nDivision"
    default infanteriedivision087_name = "87. Fußtruppe\nDivision"
    default infanteriedivision088_name = "88. Fußtruppe\nDivision"
    default infanteriedivision089_name = "89. Fußtruppe\nDivision"
    default infanteriedivision090_name = "90. Fußtruppe\nDivision"
    default infanteriedivision091_name = "91. Fußtruppe\nDivision"
    default infanteriedivision092_name = "92. Fußtruppe\nDivision"
    default infanteriedivision093_name = "93. Fußtruppe\nDivision"
    default infanteriedivision094_name = "94. Fußtruppe\nDivision"
    default infanteriedivision095_name = "95. Fußtruppe\nDivision"
    default infanteriedivision096_name = "96. Fußtruppe\nDivision"
    default infanteriedivision097_name = "97. Fußtruppe\nDivision"
    default infanteriedivision098_name = "98. Fußtruppe\nDivision"
    default infanteriedivision099_name = "99. Fußtruppe\nDivision"
    default infanteriedivision111_name = "111. Fußtruppe\nDivision"
    default infanteriedivision121_name = "121. Fußtruppe\nDivision"
    default infanteriedivision122_name = "122. Fußtruppe\nDivision"
    default infanteriedivision123_name = "123. Fußtruppe\nDivision"
    default infanteriedivision125_name = "125. Fußtruppe\nDivision"
    default infanteriedivision126_name = "126. Fußtruppe\nDivision"
    default infanteriedivision131_name = "131. Fußtruppe\nDivision"
    default infanteriedivision132_name = "132. Fußtruppe\nDivision"
    default infanteriedivision134_name = "134. Fußtruppe\nDivision"
    default infanteriedivision137_name = "137. Fußtruppe\nDivision"
    default infanteriedivision161_name = "161. Fußtruppe\nDivision"
    default infanteriedivision162_name = "162. Fußtruppe\nDivision"
    default infanteriedivision163_name = "163. Fußtruppe\nDivision"
    default infanteriedivision164_name = "164. Fußtruppe\nDivision"
    default infanteriedivision167_name = "167. Fußtruppe\nDivision"
    default infanteriedivision168_name = "168. Fußtruppe\nDivision"
    default infanteriedivision170_name = "170. Fußtruppe\nDivision"
    default infanteriedivision181_name = "181. Fußtruppe\nDivision"
    default infanteriedivision183_name = "183. Fußtruppe\nDivision"
    default infanteriedivision196_name = "196. Fußtruppe\nDivision"
    default infanteriedivision197_name = "197. Fußtruppe\nDivision"
    default infanteriedivision198_name = "198. Fußtruppe\nDivision"
    default infanteriedivision205_name = "205. Fußtruppe\nDivision"
    default infanteriedivision206_name = "206. Fußtruppe\nDivision"
    default infanteriedivision207_name = "207. Fußtruppe\nDivision"
    default infanteriedivision208_name = "208. Fußtruppe\nDivision"
    default infanteriedivision211_name = "211. Fußtruppe\nDivision"
    default infanteriedivision213_name = "213. Fußtruppe\nDivision"
    default infanteriedivision214_name = "214. Fußtruppe\nDivision"
    default infanteriedivision215_name = "215. Fußtruppe\nDivision"
    default infanteriedivision217_name = "217. Fußtruppe\nDivision"
    default infanteriedivision218_name = "218. Fußtruppe\nDivision"
    default infanteriedivision221_name = "221. Fußtruppe\nDivision"
    default infanteriedivision225_name = "225. Fußtruppe\nDivision"
    default infanteriedivision227_name = "227. Fußtruppe\nDivision"
    default infanteriedivision228_name = "228. Fußtruppe\nDivision"
    default infanteriedivision239_name = "239. Fußtruppe\nDivision"
    default infanteriedivision246_name = "246. Fußtruppe\nDivision"
    default infanteriedivision251_name = "251. Fußtruppe\nDivision"
    default infanteriedivision252_name = "252. Fußtruppe\nDivision"
    default infanteriedivision253_name = "253. Fußtruppe\nDivision"
    default infanteriedivision254_name = "254. Fußtruppe\nDivision"
    default infanteriedivision255_name = "255. Fußtruppe\nDivision"
    default infanteriedivision256_name = "256. Fußtruppe\nDivision"
    default infanteriedivision257_name = "257. Fußtruppe\nDivision"
    default infanteriedivision258_name = "258. Fußtruppe\nDivision"
    default infanteriedivision262_name = "262. Fußtruppe\nDivision"
    default infanteriedivision263_name = "263. Fußtruppe\nDivision"
    default infanteriedivision267_name = "267. Fußtruppe\nDivision"
    default infanteriedivision268_name = "268. Fußtruppe\nDivision"
    default infanteriedivision269_name = "269. Fußtruppe\nDivision"
    default infanteriedivision281_name = "281. Fußtruppe\nDivision"
    default infanteriedivision285_name = "285. Fußtruppe\nDivision"
    default infanteriedivision290_name = "290. Fußtruppe\nDivision"
    default infanteriedivision291_name = "291. Fußtruppe\nDivision"
    default infanteriedivision292_name = "292. Fußtruppe\nDivision"
    default infanteriedivision293_name = "293. Fußtruppe\nDivision"
    default infanteriedivision294_name = "294. Fußtruppe\nDivision"
    default infanteriedivision295_name = "295. Fußtruppe\nDivision"
    default infanteriedivision296_name = "296. Fußtruppe\nDivision"
    default infanteriedivision297_name = "297. Fußtruppe\nDivision"
    default infanteriedivision298_name = "298. Fußtruppe\nDivision"
    default infanteriedivision299_name = "299. Fußtruppe\nDivision"
    default infanteriedivision526_name = "526. Fußtruppe\nDivision"
    default infanteriedivision538_name = "Division z.b.V. 538."
    default infanteriedivision554_name = "554. Fußtruppe\nDivision"
    default infanteriedivision556_name = "556. Fußtruppe\nDivision"
        
    default panzerdivision001_name = "1. Panzy\nDivision"
    default panzerdivision002_name = "2. Panzy\nDivision"
    default panzerdivision003_name = "3. Panzy\nDivision"
    default panzerdivision004_name = "4. Panzy\nDivision"
    default panzerdivision005_name = "5. Panzy\nDivision"
    default panzerdivision006_name = "6. Panzy\nDivision"
    default panzerdivision007_name = "7. Panzy\nDivision"
    default panzerdivision008_name = "8. Panzy\nDivision"
    default panzerdivision009_name = "9. Panzy\nDivision"
    default panzerdivision010_name = "10. Panzy\nDivision"
    default panzerdivision011_name = "11. Panzy\nDivision"
    default panzerdivision012_name = "12. Panzy\nDivision"
    default panzerdivision013_name = "13. Panzy\nDivision"
    default panzerdivision014_name = "14. Panzy\nDivision"
    default panzerdivision016_name = "16. Panzy\nDivision"
    default panzerdivision017_name = "17. Panzy\nDivision"
    default panzerdivision018_name = "18. Panzy\nDivision"
    default panzerdivision019_name = "19. Panzy\nDivision"
    default panzerdivision020_name = "20. Panzy\nDivision"
        
    default lightdivision001_name = "1. Wenig\nDivision"
    default lightdivision002_name = "2. Wenig\nDivision"
    default lightdivision003_name = "3. Wenig\nDivision"
    default lightdivision004_name = "4. Wenig\nDivision"
    default lightdivision097_name = "97. Wenig\nDivision"
    default lightdivision099_name = "99. Wenig\nDivision"
    default lightdivision100_name = "100. Wenig\nDivision"
    default lightdivision101_name = "101. Wenig\nDivision"
        
    default mountaindivision001_name = "1. Hügelfänger\nDivision"
    default mountaindivision002_name = "2. Hügelfänger\nDivision"
    default mountaindivision003_name = "3. Hügelfänger\nDivision"
    default mountaindivision004_name = "4. Hügelfänger\nDivision"
    default mountaindivision005_name = "5. Hügelfänger\nDivision"
    default mountaindivision006_name = "6. Hügelfänger\nDivision"
    default mountaindivision007_name = "7. Hügelfänger\nDivision"
    default mountaindivision188_name = "188. Hügelfänger\nDivision"
        
    default kavalleriedivision001_name = "1. Horsey\nDivision"
        
    default airdivision001_name = "Ruftflotte 1\nDivision"
    default airdivision002_name = "Ruftflotte 2\nDivision"
    default airdivision003_name = "Ruftflotte 3\nDivision"
    default airdivision004_name = "Ruftflotte 4\nDivision"
    default xfliegerkorps_name = "X. Fliegerkorps"
        
    default fuuhbarbegleitbatallion_name = "Füühbarbegleit\nBatallion"
    default schutzenbrigade_name = "11. Pendelverkehr\nBrigade"
    default biggermania_name = "Biggermania Infantry"
    default afrikaakorps_name = "Dessous Afrikaa Korps"
        
    default kampfgeschwader001_name = "Angehen Schwadron 1"
    default kampfgeschwader002_name = "Angehen Schwadron 2"
    default kampfgeschwader003_name = "Angehen Schwadron 3"
    default kampfgeschwader004_name = "Angehen Schwadron 4"
    default kampfgeschwader026_name = "Angehen Schwadron 26"
    default kampfgeschwader027_name = "Angehen Schwadron 27"
    default kampfgeschwader030_name = "Angehen Schwadron 30"
    default kampfgeschwader040_name = "Angehen Schwadron 40"
    default kampfgeschwader051_name = "Angehen Schwadron 51"
    default kampfgeschwader053_name = "Angehen Schwadron 53"
    default kampfgeschwader054_name = "Angehen Schwadron 54"
    default kampfgeschwader055_name = "Angehen Schwadron 55"
    default kampfgeschwader076_name = "Angehen Schwadron 76"
    default kampfgeschwader077_name = "Angehen Schwadron 77"
        
    default jagdgeschwader002_name = "Fänger Schwadron 2"
    default jagdgeschwader003_name = "Fänger Schwadron 3"
    default jagdgeschwader026_name = "Fänger Schwadron 26"
    default jagdgeschwader027_name = "Fänger Schwadron 27"
    default jagdgeschwader051_name = "Fänger Schwadron 51"
    default jagdgeschwader052_name = "Fänger Schwadron 52"
    default jagdgeschwader053_name = "Fänger Schwadron 53"
    default jagdgeschwader054_name = "Fänger Schwadron 54"
    default jagdgeschwader077_name = "Fänger Schwadron 77"
        
    default sturzkampfgeschwader001_name = "Sturzangehen Schwadron 1"
    default sturzkampfgeschwader002_name = "Sturzangehen Schwadron 2"
    default sturzkampfgeschwader003_name = "Sturzangehen Schwadron 3"
    default sturzkampfgeschwader077_name = "Sturzangehen Schwadron 77"
        
    default lehrgeschwader001_name = "Trainings Schwadron 1"
    default lehrgeschwader002_name = "Trainings Schwadron 2"
        
    default aufklarungsgruppe014_name = "Ausguck Schwadron 14"
    default aufklarungsgruppe022_name = "Ausguck Schwadron 22"
    default aufklarungsgruppe031_name = "Ausguck Schwadron 31"
    default aufklarungsgruppe120_name = "Ausguck Schwadron 120"
    default aufklarungsgruppe121_name = "Ausguck Schwadron 121"
    default aufklarungsgruppe122_name = "Ausguck Schwadron 122"
    default aufklarungsgruppe123_name = "Ausguck Schwadron 123"
    default aufklarungsgruppeobdl_name = "Ausguck Schwadron Ubdl"
        
    default zerstorergeschwader002_name = "Untergang Schwadron 2"
    default zerstorergeschwader026_name = "Untergang Schwadron 26"
    default zerstorergeschwader076_name = "Untergang Schwadron 76"
        
    default zzdivision001_name = "1. ZZ Panzy Division 'Lockpick Hitora'"
    default zzdivision002_name = "2. ZZ Panzy Division 'Das Empire'"
    default zzdivision003_name = "3. ZZ Panzy Division 'Totenkatze'"
    default zzdivision004_name = "4. ZZ Polizei Panzygrenadier Division"
    default zzdivision005_name = "5. ZZ Panzy Division 'Smorgasbord'"
    default zzdivision006_name = "6. ZZ Hügelfänger Division 'Nord'"
    default zzdivision008_name = "8. ZZ Horsey Division 'Flora'"
        
    default hanggyorshadtescorps_name = "Hang Gyorshadtest"
    default czexaexpeditionarygroup_name = "Czexa Field Army Bernolak"
    default rumanum3army_name = "Armata a 3-a Rumanum"
    default rumanum4army_name = "Armata a 4-a Rumanum"
        
    default vitaliainfanteriedivision009_name = "Vitalia 9a Divisione Infantry"
    default vitaliainfanteriedivision052_name = "Vitalia 52a Divisione Infantry"
    default vitaliakavalleriedivision003_name = "Vitalia 3a Divisione Celere"
        
    default heeresgruppea_name = "Truppegruppe A"
    default heeresgruppeb_name = "Truppegruppe B"
    default heeresgruppec_name = "Truppegruppe C"
    default heeresgruppenord_name = "North Army"
    default heeresgruppemitte_name = "Center Army"
    default heeresgruppesud_name = "South Army"
        
    default armee001_name = "1. Armee"
    default armee002_name = "2. Armee"
    default armee003_name = "3. Armee"
    default armee004_name = "4. Armee"
    default armee005_name = "5. Armee"
    default armee006_name = "6. Armee"
    default armee007_name = "7. Armee"
    default armee008_name = "8. Armee"
    default armee009_name = "9. Armee"
    default armee010_name = "10. Armee"
    default armee011_name = "11. Armee"
    default armee012_name = "12. Armee"
    default armee014_name = "14. Armee"
    default armee015_name = "15. Armee"
    default armee016_name = "16. Armee"
    default armee017_name = "17. Armee"
    default armee018_name = "18. Armee"
    default armeenorda_name = "Armee Norda"
    default armeepanzergruppeewalda_name = "Panzygruppe Ewalda"
    default armeepanzergruppeguderian_name = "Panzygruppe Guderian"
    default armeepanzergruppeafrikaa_name = "Panzygruppe Afrikaa"
    default armeepanzergruppe001_name = "Panzygruppe 1"
    default armeepanzergruppe002_name = "Panzygruppe 2"
    default armeepanzergruppe003_name = "Panzygruppe 3"
    default armeepanzergruppe004_name = "Panzygruppe 4"
        
    default armeekorps001_name = "I. Armeekorps"
    default armeekorps002_name = "II. Armeekorps"
    default armeekorps003_name = "III. Armeekorps"
    default panzerkorps003_name = "III. Panzykorps"
    default armeekorps004_name = "IV. Armeekorps"
    default armeekorps005_name = "V. Armeekorps"
    default armeekorps006_name = "VI. Armeekorps"
    default armeekorps007_name = "VII. Armeekorps"
    default armeekorps008_name = "VIII. Armeekorps"
    default armeekorps009_name = "IX. Armeekorps"
    default armeekorps010_name = "X. Armeekorps"
    default armeekorps011_name = "XI. Armeekorps"
    default armeekorps012_name = "XII. Armeekorps"
    default armeekorps013_name = "XIII. Armeekorps"
    default armeekorps014_name = "XIV. Armeekorps"
    default panzerkorps014_name = "XIV. Panzykorps"
    default armeekorps015_name = "XV. Armeekorps"
    default armeekorps016_name = "XVI. Armeekorps"
    default armeekorps017_name = "XVII. Armeekorps"
    default armeekorps018_name = "XVIII. Armeekorps"
    default armeekorps019_name = "XIX. Armeekorps"
    default armeekorps020_name = "XX. Armeekorps"
    default armeekorps021_name = "XXI. Armeekorps"
    default armeekorps021gruppe_name = "XXI. Gruppe"
    default armeekorps022_name = "XXII. Armeekorps"
    default armeekorps023_name = "XXIII. Armeekorps"
    default armeekorps024_name = "XXIV. Armeekorps"
    default panzerkorps024_name = "XXIV. Panzykorps"
    default armeekorps025_name = "XXV. Armeekorps"
    default armeekorps026_name = "XXVI. Armeekorps"
    default armeekorps027_name = "XXVII. Armeekorps"
    default armeekorps028_name = "XXVIII. Armeekorps"
    default armeekorps029_name = "XXIX. Armeekorps"
    default armeekorps030_name = "XXX. Armeekorps"
    default armeekorps032_name = "XXXII. Armeekorps"
    default armeekorps033_name = "Überlegen Kommando z.b.V. XXXIII"
    default armeekorps035_name = "XXXV. Armeekorps"
    default armeekorps037_name = "Überlegen Kommando z.b.V. XXXVII"
    default armeekorps038_name = "XXXVIII. Armeekorps"
    default panzerkorps039_name = "XXXIX. Panzykorps"
    default armeekorps040_name = "XXXX. Armeekorps"
    default panzerkorps040_name = "XXXX. Panzykorps"
    default armeekorps041_name = "XXXXI. Armeekorps"
    default panzerkorps041_name = "XXXXI. Panzykorps"
    default armeekorps042_name = "XXXXII. Armeekorps"
    default armeekorps043_name = "XXXXIII. Armeekorps"
    default armeekorps044_name = "XXXXIV. Armeekorps"
    default armeekorps045_name = "Überlegen Kommando z.b.V. XXXXV"
    default panzerkorps046_name = "XXXXVI. Panzykorps"
    default panzerkorps047_name = "XXXXVII. Panzykorps"
    default panzerkorps048_name = "XXXXVIII. Panzykorps"
    default armeekorps049_name = "XXXXVIII. Hügel-Armeekorps"
    default armeekorps050_name = "L. Armeekorps"
    default armeekorps051_name = "LI. Armeekorps"
    default panzerkorps051_name = "LI. Panzykorps"
    default armeekorps052_name = "LII. Armeekorps"
    default panzerkorps052_name = "LII. Panzykorps"
    default armeekorps053_name = "LIII. Armeekorps"
    default armeekorps054_name = "LIV. Armeekorps"
    default armeekorps055_name = "LV. Armeekorps"
    default panzerkorps056_name = "LVI. Panzykorps"
    default panzerkorps057_name = "LVII. Panzykorps"
        
        
    #STARTING STRUCTURE
    default active_armygroups_items = {
        "insignia-heeresgruppec": heeresgruppec_name,
        "insignia-heeresgruppenord": heeresgruppenord_name,
        "insignia-heeresgruppesud": heeresgruppesud_name      
    }
        
    default active_armies_items = {
        "insignia-armee001": armee001_name,
        "insignia-armee002": armee002_name,
        "insignia-armee003": armee003_name,
        "insignia-armee004": armee004_name,
        "insignia-armee005": armee005_name,
        "insignia-armee007": armee007_name,
        "insignia-armee008": armee008_name,
        "insignia-armee010": armee010_name,
        "insignia-armee014": armee014_name
    }
        
    default active_korps_items = {
        "insignia-armeekorps001": armeekorps001_name,
        "insignia-armeekorps002": armeekorps002_name,
        "insignia-armeekorps003": armeekorps003_name,
        "insignia-armeekorps004": armeekorps004_name,
        "insignia-armeekorps007": armeekorps007_name,
        "insignia-armeekorps008": armeekorps008_name,
        "insignia-armeekorps010": armeekorps010_name,
        "insignia-armeekorps011": armeekorps011_name,
        "insignia-armeekorps013": armeekorps013_name,
        "insignia-armeekorps014": armeekorps014_name,
        "insignia-armeekorps015": armeekorps015_name,
        "insignia-armeekorps016": armeekorps016_name,
        "insignia-armeekorps017": armeekorps017_name,
        "insignia-armeekorps018": armeekorps018_name,
        "insignia-armeekorps019": armeekorps019_name,
        "insignia-armeekorps021": armeekorps021_name,
        "insignia-armeekorps022": armeekorps022_name,
        "insignia-armeekorps026": armeekorps026_name
    }
        
    default active_divisions_items = {
        "insignia-panzerdivision001": panzerdivision001_name,
        "insignia-panzerdivision002": panzerdivision002_name,
        "insignia-panzerdivision003": panzerdivision003_name,
        "insignia-panzerdivision004": panzerdivision004_name,
        "insignia-panzerdivision005": panzerdivision005_name,
        "insignia-panzerdivision010": panzerdivision010_name,
        "insignia-infanteriedivision001": infanteriedivision001_name, 
        "insignia-infanteriedivision002": infanteriedivision002_name,
        "insignia-infanteriedivision003": infanteriedivision003_name,
        "insignia-infanteriedivision004": infanteriedivision004_name,
        "insignia-infanteriedivision007": infanteriedivision007_name,
        "insignia-infanteriedivision008": infanteriedivision008_name,
        "insignia-infanteriedivision010": infanteriedivision010_name,
        "insignia-infanteriedivision011": infanteriedivision011_name,
        "insignia-infanteriedivision012": infanteriedivision012_name,
        "insignia-infanteriedivision013": infanteriedivision013_name,
        "insignia-infanteriedivision014": infanteriedivision014_name,
        "insignia-infanteriedivision017": infanteriedivision017_name,
        "insignia-infanteriedivision018": infanteriedivision018_name,
        "insignia-infanteriedivision019": infanteriedivision019_name,
        "insignia-infanteriedivision020": infanteriedivision020_name,
        "insignia-infanteriedivision021": infanteriedivision021_name,
        "insignia-infanteriedivision023": infanteriedivision023_name,
        "insignia-infanteriedivision024": infanteriedivision024_name,
        "insignia-infanteriedivision027": infanteriedivision027_name,
        "insignia-infanteriedivision028": infanteriedivision028_name,
        "insignia-infanteriedivision029": infanteriedivision029_name,
        "insignia-infanteriedivision030": infanteriedivision030_name,
        "insignia-infanteriedivision031": infanteriedivision031_name,
        "insignia-infanteriedivision032": infanteriedivision032_name,
        "insignia-infanteriedivision044": infanteriedivision044_name,
        "insignia-infanteriedivision045": infanteriedivision045_name,
        "insignia-infanteriedivision046": infanteriedivision046_name,
        "insignia-infanteriedivision050": infanteriedivision050_name,
        "insignia-infanteriedivision061": infanteriedivision061_name,
        "insignia-infanteriedivision062": infanteriedivision062_name,
        "insignia-infanteriedivision068": infanteriedivision068_name,
        "insignia-infanteriedivision073": infanteriedivision073_name,
        "insignia-infanteriedivision206": infanteriedivision206_name,
        "insignia-infanteriedivision207": infanteriedivision207_name,
        "insignia-infanteriedivision208": infanteriedivision208_name,
        "insignia-infanteriedivision213": infanteriedivision213_name,
        "insignia-infanteriedivision217": infanteriedivision217_name,
        "insignia-infanteriedivision218": infanteriedivision218_name,
        "insignia-infanteriedivision221": infanteriedivision221_name,
        "insignia-infanteriedivision228": infanteriedivision228_name,
        "insignia-infanteriedivision239": infanteriedivision239_name,
        "insignia-mountaindivision001": mountaindivision001_name, 
        "insignia-mountaindivision002": mountaindivision002_name, 
        "insignia-mountaindivision003": mountaindivision003_name,
        "insignia-kavalleriedivision001": kavalleriedivision001_name,
        "insignia-lightdivision001": lightdivision001_name,
        "insignia-lightdivision002": lightdivision002_name, 
        "insignia-lightdivision003": lightdivision003_name, 
        "insignia-lightdivision004": lightdivision004_name, 
        "insignia-jagdgeschwader054": jagdgeschwader054_name,
        "insignia-kampfgeschwader001": kampfgeschwader001_name,
        "insignia-kampfgeschwader076": kampfgeschwader076_name,
        "insignia-kampfgeschwader077": kampfgeschwader077_name
    }
            
    default active_spezialformations_items = {
        "insignia-fuuhbarbegleitbatallion": fuuhbarbegleitbatallion_name,
        "insignia-czexaexpeditionarygroup": czexaexpeditionarygroup_name
    } 
        
    default voxpopmode_enabled = False
    default voxpopjump = None
    default voxpopleave_sensitive = None
        
    default always_true = True
    
    default vitaliaq1 = False
    default vitaliaq2 = False
    default vitaliaq3 = False
        
    default command_one = "{image=icon_command}"
    default command_two = "{image=icon_command} {image=icon_command}"
    default command_three = "{image=icon_command} {image=icon_command} {image=icon_command}"
    default command_four = "{image=icon_command} {image=icon_command} {image=icon_command} {image=icon_command}"
    default command_five = "{image=icon_command} {image=icon_command} {image=icon_command} {image=icon_command} {image=icon_command}"
    
    default management_one = "{image=icon_management}"
    default management_two = "{image=icon_management} {image=icon_management}"
    default management_three = "{image=icon_management} {image=icon_management} {image=icon_management}"
    default management_four = "{image=icon_management} {image=icon_management} {image=icon_management} {image=icon_management}"
    default management_five = "{image=icon_management} {image=icon_management} {image=icon_management} {image=icon_management} {image=icon_management}"
    
    default influence_one = "{image=icon_influence}"
    default influence_two = "{image=icon_influence} {image=icon_influence}"
    default influence_three = "{image=icon_influence} {image=icon_influence} {image=icon_influence}"
    default influence_four = "{image=icon_influence} {image=icon_influence} {image=icon_influence} {image=icon_influence}"
    default influence_five = "{image=icon_influence} {image=icon_influence} {image=icon_influence} {image=icon_influence} {image=icon_influence}"
        
    default current_image = 1
    default temp_image = 5
        
    default polix_invasion_success = False
    default finbard_success = False
        
    default map_update_happen = False
    default map_update_title = ""
    default map_update_subtitle = ""
    default map_update_description = ""
        
    default map_update_title1 = "Welcome to the Map Screen"
    default map_update_title2 = "New Territories created"
    default map_update_title3 = "New Territories created"
    default map_update_title4 = "New Territories created"
    default map_update_title5 = "New Territories created"
    default map_update_title6 = "New Territories created"
    default map_update_title7 = "Nation has been occupied"
    default map_update_title8 = "Nation has been occupied"
    default map_update_title9 = "Nation has been occupied"
    default map_update_title10 = "Nation has been occupied"
    default map_update_title11 = "Nation declares new allegiance"
    default map_update_title12 = "Colonies declare new allegiance"
    default map_update_title13 = "Nations declare new allegiance"
    default map_update_title14 = "Colony has been occupied"
    default map_update_title15 = "Nation has been occupied"
    default map_update_title16 = "Colony has been occupied"
    default map_update_title17 = "Territory has been occupied"
    default map_update_title18 = "Territory has been occupied"
    default map_update_title19 = "Territory has been occupied"
        
    default map_update_subtitle1 = "Discover what you can see and do on the map screen!"
    default map_update_subtitle2 = "Polix divided and new territories have appeared on the map!"
    default map_update_subtitle3 = "Franzo occupied and new territories have appeared on the map!"
    default map_update_subtitle4 = "Rumanum divided and new territories have appeared on the map!"
    default map_update_subtitle5 = "Serpana divided and new territories have appeared on the map!"
    default map_update_subtitle6 = "Finbard divided and new territories have appeared on the map!"
    default map_update_subtitle7 = "Dania has been occupied by the Empire of Germania!"
    default map_update_subtitle8 = "Norda has been occupied by the Empire of Germania!"
    default map_update_subtitle9 = "Batavia has been occupied by the Empire of Germania!"
    default map_update_subtitle10 = "Belgae has been occupied by the Empire of Germania!"
    default map_update_subtitle11 = "Belgae has joined the Alliance side!"
    default map_update_subtitle12 = "Brad, Banki and Kamrun have joined the Alliance side!"
    default map_update_subtitle13 = "Many nations have declared new allegiances!"
    default map_update_subtitle14 = "Zomali has been occupied by the Empire of Britannia!"
    default map_update_subtitle15 = "Grecia has been occupied by the Axle side!"
    default map_update_subtitle16 = "Eastern Vitalia Afrikaa has been occupied by the Empire of Britannia!"
    default map_update_subtitle17 = "Sovian Polix has been occupied by the Empire of Germania!"
    default map_update_subtitle18 = "Livonia has been occupied by the Empire of Germania!"
    default map_update_subtitle19 = "Much of the Sovian Front is controlled by the Empire of Germania!"
        
    default map_update_description1 = "Prior to missions, you will be presented with this map screen. There are multiple views to choose from, such as seeing a geographic or political map, or even tertiary maps. There are additional information boxes containing data on main missions and side missions, tracking your progress and success. \n \n You can also view information on current alliances, enemies and controlling powers from across the continent. You can see the status of cities and governors, as well as key players in the campaign, by clicking on the city stars. \n \n Main missions will progress the main storyline with a key battle. Side missions allow players the opportunity to level up, progress research and unlock additional units for battles. If you choose to play the main mission without playing the side missions, those particular missions will be unavailable at the next map screen. When you are ready to begin a mission, simply click on an Invasion Beacon."
    default map_update_description2 = "On occasion, new territories may appear on the map screen. Following the fall of Polix to Germanian and Sovian forces, the former nation has been abolished. Its borders have been redrawn by its occupiers to form two new nations - {i}Germanian-Occupied Polix{/i} and {i}Sovian-Occupied Polix{/i}. \n \n To establish firm control over the resources, arms and populations of the new territories, the armies are conducting brutal {i}'cleanup operations'{/i}, involving forced deportations and executions . . ."
    default map_update_description3 = "Now that Franzo has fallen to Germania, the country has been divided into two new territories - {i}Occupied Franzo{/i} and {i}Vichei Franzo{/i}. Technically neutral, but really an ally of Germania, {i}Vichei Franzo{/i} and its colonies overseas will fight against Britannia and what's left of the {i}Alliance{/i}. \n \n With mainland Europa now under the control of the {i}Axle{/i}, both alliances turn their attention to new theaters, in the deserts and jungles of the southern shores . . . \n \n Elsewhere, Livonia has been occupied by the Union of Sovia and a puppet state has been established."
    default map_update_description4 = "After substantial pressure was placed on its leaders, Rumanum has lost a large amount of land to its neighbors. {i}Vampiria{/i}, a region in the west, is now part of Hang. {i}Tobrudza{/i}, a southern region, is now part of Bolga. And the northern borders are now known as {i}Sovia Moldvaya{/i}, part of the Sovian empire. \n \n To establish firm control over the resources, arms and populations of the new territories, forced deportations and mass movement of civilians is now taking place . . . \n \n Elsewhere, the colony of Zomali has been occupied by the Empire of Vitalia following an invasion. Britannian forces managed to escape across the Rotten Sea . . ."
    default map_update_description5 = "Following the invasion of Serpana, the country's borders have been redrawn from scratch. A lot of land has been divided up amongst Germania, Vitalia and Bolga. What's left of the rump state has become two new puppet regions - {i}Cervetiis{/i}, controlled by Germania, and {i}Xrovat{/i}, run by a violent, vascist regime. \n \n To establish firm control over the resources, arms and populations of the new territories, the armies are conducting brutal {i}'cleanup operations'{/i}, involving forced deportations and executions . . ."
    default map_update_description6 = "Following the Sovian invasion of Finbard, and the {i}Wintertime War{/i}, a new territory has been created out of southern Finbard. The new Sovian territory is known as {i}Sovian Xarelia{/i}, part of the Sovian empire. \n \n To establish firm control over the resources, arms and populations of the new territories, forced deportations and mass movement of civilians is now taking place . . ."
    default map_update_description7 = "Following an invasion, the nation of Dania has surrendered, and has been occupied by the Empire of Germania. Due to the brief period of battle and proximity of the country, the occupation will be relatively lenient. \n \n To establish firm control over the resources, arms and populations of the new territories, a government of occupation has been established . . ."
    default map_update_description8 = "Following an invasion, the nation of Norda has surrendered, and has been occupied by the Empire of Germania. However, the government has escaped abroad and continues to fight for the {i}Alliance{/i} side. Resistance groups have already formed to fight the occupation. \n \n To establish firm control over the resources, arms and populations of the new territories, a government of occupation has been established . . ."
    default map_update_description9 = "Following an invasion, the nation of Batavia has surrendered, and has been occupied by the Empire of Germania. However, the government has escaped abroad and continues to fight for the {i}Alliance{/i} side. Resistance groups have already formed to fight the occupation. \n \n To establish firm control over the resources, arms and populations of the new territories, a government of occupation has been established . . ."
    default map_update_description10 = "Following an invasion, the nation of Belgae has surrendered, and has been occupied by the Empire of Germania. The king himself has surrendered and accepted the occupation. However, a government-in-exile has escaped abroad and continues to fight for the {i}Alliance{/i} side. Resistance groups have already formed to fight the occupation. \n \n To establish firm control over the resources, arms and populations of the new territories, a government of occupation has been established . . ."
    default map_update_description11 = "Following the Germanian invasion on its eastern and northern borders, Belgae has abandoned neutrality and joined the {i}Alliance{/i} side. Now the armies of Franzo and Britannia will march into Belgae to confront the invasion forces . . ."
    default map_update_description12 = "The Empire of Vitalia has invaded the Britannian-controlled colony of Gypta, pushing eastwards along the coast. Many towns have fallen to Vitalian control. \n \n Elsewhere, three colonies have broken away from {i}Vichei Franzo{/i} control, and now fight for Gallia Cyrano's {i}Franzo Libre{/i}. The Afrikaan colonies of Brad, Banki and Kamrun are now allied to the {i}Alliance{/i} side, and will battle against {i}Axle{/i} forces . . ."
    default map_update_description13 = "Hang and Rumanum have officially declared allegiance to Germania and the {i}Axle{/i} side. \n \n Following its war with Vitalian forces on the border with Epirus, Grecia has declared allegiance to the {i}Alliance{/i} side. Because of this, the nation has now seen an increase in the presence of Britannian troops there. \n \n Elsewhere, Franzo Gonko has broken away from {i}Vichei Franzo{/i} control, and now fights for Gallia Cyrano's {i}Franzo Libre{/i}. The Afrikaan colony is now allied to the {i}Alliance{/i} side, and will battle against {i}Axle{/i} forces . . ."
    default map_update_description14 = "Following the previous invasion and occupation of Zomali by the Empire of Vitalia, Britannian forces have reclaimed the colony from {i}Axle{/i} forces. Once again, the Britannian flag will fly in Zomali. \n \n Meanwhile, Britannian forces push back against the Vitalians in Gypta and Cyracana, chasing the enemy all the way into the sea. Similarly, Grecian forces have pushed back against the Vitalian invasion and into Epirus itself. \n \n Elsewhere, Bolga has officially declared allegiance to Germania and the {i}Axle{/i} side . . ."
    default map_update_description15 = "Following an invasion, the nation of Grecia has surrendered, and has been occupied by the empires of Germania, Vitalia and Bolga. However, the government has escaped abroad and continues to fight for the {i}Alliance{/i} side. Resistance groups have already formed to fight the occupation. \n \n To establish firm control over the resources, arms and populations of the new territories, governments of occupation have been established. Meanwhile, the armies are conducting brutal {i}'cleanup operations'{/i}, involving forced deportations and executions . . . \n \n Elsewhere, rebels in Iraji, with {i}Axle{/i} backing, have risen up to fight against the Britannian occupation. In Cyracana and on Gypta's northern coast, Germanian forces have pushed the Britannian forces back into Gypta . . ."
    default map_update_description16 = "Following an invasion, the colony of Eastern Vitalia Afrikaa has been occupied by Britannian forces. \n \n Elsewhere, Assyria has broken away from {i}Vichei Franzo{/i} control, and now fights for Gallia Cyrano's {i}Franzo Libre{/i}. The colony is now allied to the {i}Alliance{/i} side, and will battle against {i}Axle{/i} forces . . ."
    default map_update_description17 = "Following the start of {i}Operation Barbara-Ann{/i}, the territory of Sovian-Occupied Polix has been occupied by the Empire of Germania. Sovian forces have pulled back as Germanian troops push forwards into Sovia Minor . . . \n \n To establish firm control over the resources, arms and populations of the new territories, the armies are conducting brutal {i}'cleanup operations'{/i}, involving forced deportations and executions . . ."
    default map_update_description18 = "Following the start of {i}Operation Barbara-Ann{/i}, the territory of Sovian-Occupied Livonia has been occupied by the Empire of Germania. Sovian forces have pulled back as Germanian troops push forwards into Sovia Minor . . . \n \n To establish firm control over the resources, arms and populations of the new territories, the armies are conducting brutal {i}'cleanup operations'{/i}, involving forced deportations and executions . . . \n \n Elsewhere, Finbard has annexed territory it lost in the {i}Wintertime War{/i}, abolishing the territory of {i}Sovian Xarelia{/i}. Rumanum has annexed territory it lost in treaty negotiations, controlling {i}Sovian Moldvaya{/i}."
    default map_update_description19 = "Following the start of {i}Operation Barbara-Ann{/i}, much of the Sovian Front is now controlled by the Empire of Germania. Sovian forces have pulled back as Germanian troops push forwards into Sovia Major . . . \n \n To establish firm control over the resources, arms and populations of the new territories, the armies are conducting brutal {i}'cleanup operations'{/i}, involving forced deportations and executions . . . \n \n Elsewhere, the Britannians have pushed back against Germania in Gypta and into Cyracana . . ."
    
    default codex_navchoice = "codex1"
        
    default profile_yamato_name = "Yamato Yamamoto"
    default profile_joebbels_name = "Iosefina Joebbels"
    default profile_goring_name = "Hermina Goring"
    default profile_hitora_name = "Adorofia Hitora"
    default profile_cyrano_name = "Gallia Cyrano"
    default profile_churchill_name = "Winstefina Churchill"
    default profile_dunitz_name = "Karol Dunitz"
    default profile_zhukky_name = "Iorgina Zhukky"
    default profile_roijean_name = "Reine Jean"
    default profile_monty_name = "Ben Monty"
    default profile_starin_name = "Iosefina Starin"
    default profile_hirahita_name = "Zhowa Hirahita"
    default profile_roosevelt_name = "Francine Roosevelt"
    default profile_manstein_name = "Erika Manstein"
    default profile_mannerheim_name = "Karla Mannerheim"
    default profile_rinni_name = "Benita Mussorinni"
    default profile_rommel_name = "Erwina Rommel"
    default profile_gamelin_name = "Maurie Gamelin"
    default profile_badoglio_name = "Petra Badoglio"
    default profile_messe_name = "Giovannia Messe"
    default profile_graziani_name = "Rodolphia Graziani"
    default profile_antoness_name = "Iona Antoness"
    default profile_tito_name = "Iosipa Tito"
    default profile_molotov_name = "Vyacheslavia Molotov"
    default profile_vasile_name = "Alexa Vasile"
    default profile_stuffy_name = "Dowdy Stuffy"
    default profile_battenia_name = "Louisa Battenia"
    default profile_guderian_name = "Heinzia Guderian"
    default profile_horthy_name = "Miklosa Horthy"
    default profile_smigly_name = "Edwina Smigly"
    default profile_dresckow_name = "Henri vi Dresckow"
    default profile_nyan_name = "Nyan Katshex"
    default profile_hess_name = "Rudolphia Hess"
    default profile_borkind_name = "Marty Borkind"
    default profile_keitel_name = "Mister Keitel"
    default profile_brauchitsch_name = "Mister Brauchitsch"
        
    default profile_yamato_sprite = "yamato codex"
    default profile_joebbels_sprite = "joebbels codex"
    default profile_goring_sprite = "goring codex"
    default profile_hitora_sprite = "hitora codex"
    default profile_cyrano_sprite = "cyrano codex"
    default profile_churchill_sprite = "churchill codex"
    default profile_dunitz_sprite = "dunitz codex"
    default profile_zhukky_sprite = "zhukky codex"
    default profile_roijean_sprite = "roijean codex"
    default profile_monty_sprite = "monty codex"
    default profile_starin_sprite = "starin codex"
    default profile_hirahita_sprite = "hirahita codex"
    default profile_roosevelt_sprite = "roosevelt codex"
    default profile_manstein_sprite = "manstein codex"
    default profile_mannerheim_sprite = "mannerheim codex"
    default profile_rinni_sprite = "rinni codex"
    default profile_rommel_sprite = "rommel codex"
    default profile_gamelin_sprite = "gamelin codex"
    default profile_badoglio_sprite = "badoglio codex"
    default profile_messe_sprite = "messe codex"
    default profile_graziani_sprite = "graziani codex"
    default profile_antoness_sprite = "antoness codex"
    default profile_tito_sprite = "tito codex"
    default profile_molotov_sprite = "molotov codex"
    default profile_vasile_sprite = "vasile codex"
    default profile_stuffy_sprite = "stuffy codex"
    default profile_battenia_sprite = "battenia codex"
    default profile_guderian_sprite = "guderian codex"
    default profile_horthy_sprite = "horthy codex"
    default profile_smigly_sprite = "smigly codex"
    default profile_dresckow_sprite = "dresckow codex"
    default profile_nyan_sprite = "nyan codex"
        
    default profile_yamato_flag = "yamato codex flag"
    default profile_joebbels_flag = "joebbels codex flag"
    default profile_goring_flag = "goring codex flag"
    default profile_hitora_flag = "hitora codex flag"
    default profile_cyrano_flag = "cyrano codex flag"
    default profile_churchill_flag = "churchill codex flag"
    default profile_dunitz_flag = "dunitz codex flag"
    default profile_zhukky_flag = "zhukky codex flag"
    default profile_roijean_flag = "roijean codex flag"
    default profile_monty_flag = "monty codex flag"
    default profile_starin_flag = "starin codex flag"
    default profile_hirahita_flag = "hirahita codex flag"
    default profile_roosevelt_flag = "roosevelt codex flag"
    default profile_manstein_flag = "manstein codex flag"
    default profile_mannerheim_flag = "mannerheim codex flag"
    default profile_rinni_flag = "rinni codex flag"
    default profile_rommel_flag = "rommel codex flag"
    default profile_gamelin_flag = "gamelin codex flag"
    default profile_badoglio_flag = "badoglio codex flag"
    default profile_messe_flag = "messe codex flag"
    default profile_graziani_flag = "graziani codex flag"
    default profile_antoness_flag = "antoness codex flag"
    default profile_tito_flag = "tito codex flag"
    default profile_molotov_flag = "molotov codex flag"
    default profile_vasile_flag = "vasile codex flag"
    default profile_stuffy_flag = "stuffy codex flag"
    default profile_battenia_flag = "battenia codex flag"
    default profile_guderian_flag = "guderian codex flag"
    default profile_horthy_flag = "horthy codex flag"
    default profile_smigly_flag = "smigly codex flag"
    default profile_dresckow_flag = "dresckow codex flag"
    default profile_nyan_flag = "nyan codex flag"
        
    default profile_yamato_role = "Warrant Officer, Empire of Zipangu"
    default profile_joebbels_role = "Propaganda Minister, Nappi Empire of Germania"
    default profile_goring_role = "Ruftwaffe Commander, Nappi Empire of Germania"
    default profile_hitora_role = "Füühbar, Nappi Empire of Germania"
    default profile_cyrano_role = "General, Republic of Franzo"
    default profile_churchill_role = "First Minister, Empire of Britannia"
    default profile_dunitz_role = "Kriegssee Admiral, Nappi Empire of Germania"
    default profile_zhukky_role = "Marshal, Union of Sovia"
    default profile_roijean_role = " General, Republic of Franzo"
    default profile_monty_role = "General, Empire of Britannia"
    default profile_starin_role = "Dictator, Union of Sovia"
    default profile_hirahita_role = "Nyantei Heika, Empire of Zipangu"
    default profile_roosevelt_role = "President, United Amerika"
    default profile_manstein_role = "General, Empire of Germania"
    default profile_mannerheim_role = "Marshal, Republic of Finbard"
    default profile_rinni_role = "Il Douché, Kingdom of Vitalia"
    default profile_rommel_role = "General, Nappi Empire of Germania"
    default profile_gamelin_role = "General, Republic of Franzo "
    default profile_badoglio_role = "Marshal, Kingdom of Vitalia"
    default profile_messe_role = "General, Kingdom of Vitalia"
    default profile_graziani_role = "General, Kingdom of Vitalia "
    default profile_antoness_role = "Dictator, Nationalist Kingdom of Rumanum"
    default profile_tito_role = "General, Serpana Partisan Army"
    default profile_molotov_role = "Foreign Minister, Union of Sovia"
    default profile_vasile_role = "General, Union of Sovia"
    default profile_stuffy_role = "BRAF Commander, Empire of Britannia"
    default profile_battenia_role = "BRN Admiral, Empire of Britannia"
    default profile_guderian_role = "General, Nappi Empire of Germania "
    default profile_horthy_role = "Sovereign, Kingdom of Hang"
    default profile_smigly_role = "Dictator, Republic of Polix"
    default profile_dresckow_role = " General, Nappi Empire of Germania"
    default profile_nyan_role = "Dictator, Zhinese Kittentang (KTT)"
        
    default profile_yamato_birthplace = "Zipangu"
    default profile_joebbels_birthplace = "Germania"
    default profile_goring_birthplace = "Germania "
    default profile_hitora_birthplace = "Osta"
    default profile_cyrano_birthplace = "Franzo"
    default profile_churchill_birthplace = "Britannia"
    default profile_dunitz_birthplace = " Germania"
    default profile_zhukky_birthplace = "Sovia Major"
    default profile_roijean_birthplace = "Franzo "
    default profile_monty_birthplace = "Britannia "
    default profile_starin_birthplace = "Sovia Minor"
    default profile_hirahita_birthplace = "Zipangu "
    default profile_roosevelt_birthplace = "United Amerika"
    default profile_manstein_birthplace = " Germania "
    default profile_mannerheim_birthplace = "Finbard"
    default profile_rinni_birthplace = "Vitalia"
    default profile_rommel_birthplace = " Germania  "
    default profile_gamelin_birthplace = " Franzo"
    default profile_badoglio_birthplace = "Vitalia "
    default profile_messe_birthplace = " Vitalia"
    default profile_graziani_birthplace = " Vitalia "
    default profile_antoness_birthplace = "Rumanum"
    default profile_tito_birthplace = "Serpana"
    default profile_molotov_birthplace = "Sovia Major "
    default profile_vasile_birthplace = " Sovia Major"
    default profile_stuffy_birthplace = " Britannia"
    default profile_battenia_birthplace = " Britannia "
    default profile_guderian_birthplace = "  Germania "
    default profile_horthy_birthplace = "Hang"
    default profile_smigly_birthplace = "Polix"
    default profile_dresckow_birthplace = "  Germania  "
    default profile_nyan_birthplace = "Zhina"
        
    default profile_yamato_description = "A disillusioned but brave soldier, he fought in the wars against Zhina in the Imperial Army. Having been raised in Zipangu, he has no real knowledge of Europa or the terrain. His uncle is commander-in-chief of the {i}Combo Fleet{/i}, Vice-Admiral Yamamoto. Sent to Germania as a spy for the military, he becomes personal advisor to the dictator Adorofia Hitora. Enjoys reading and fighting. Pretty relatable, huh?"
    default profile_joebbels_description = "A shy girl with a stutter, she works as one of Hitora's loyal ministers. As Germania's Propaganda Minister, she is responsible for organizing rallies, culture and art, and keeping up public morale. She suffers from androphobia and only trusts other women. As such, she has a crush on Hitora and will remove anyone who gets in their way. Devoted, maniacal and sneaky, she is a powerful figure."
    default profile_goring_description = "A boisterous and simple girl with a loud laugh, she works as one of Hitora's loyal ministers. As commander of Germania's air forces, the {i}Ruftwaffe{/i}, she is responsible for ensuring aerial dominance during campaigns. She loves snacking on junk food, collecting valuable artwork and lazing around doing nothing. As the {i}Imperiumsmarschall{/i}, her goal is to eventually become Füühbar too."
    default profile_hitora_description = "The Füühbar of Germania. A bratty, cruel girl, her dream is to conquer all of Europa. After entering politics, she was jailed following a failed putsch. Once released, she gained power using trickery, intimidation and violence. A fiery dictator with a temperamental, bloodthirsty personality, she plunges Europa into the Second Great War. Her hobbies include painting, vegetarianism and cute dogs."
    default profile_cyrano_description = "A tomboyish girl, with an interest in tank warfare and freedom. She believes strongly that Franzo has a unique destiny, as a long-time enemy of Germania. A fierce fighter and a loyal patriot, she hates losing, even in small matters like board games. Enjoys running and going to the theatre (although most of them were closed due to the war). Despite her athletic lifestyle, she still smokes cigarettes - a habit she refuses to give up."
    default profile_churchill_description = "A determined girl, she is a worthy adversary and perhaps the one Hitora fears most. Churchill commands a mighty navy, a plucky air force and an island nation of hooligans. She is considered to be a genius, indulging in oratory, inventing and studying old magick. Despite her relaxed appearance, she can be rather brutal and destructive when she wants to. Likes eating chocolate cigars, drinking tea and dictating orders from the bathtub."
    default profile_dunitz_description = "A voluptuous older woman, she works as one of Hitora's loyal ministers. As Grand Admiral of the Germanian navy, the {i}Kriegssee{/i}, she is responsible for maintaining dominance at sea, sinking enemy destroyers and keeping shipping lanes open. She's slowly approaching {i}christmas cake{/i} status, and has a teasing, coy personality. Likes crosswords, clothes shopping and playing mechanical arcade games."
    default profile_zhukky_description = "Known across Europa as the {i}'ice queen'{/i}, she is a leading general in the Union of Sovia. Behaving like an older sister to the dictator Starin, she is a powerful warrior and dangerous enemy. Described by fans as a 'cool beauty', she enjoys crushing her enemies and has a reputation for being ruthless. Having won many victories against the Empire of Zipangu, she now sets her sights on eastern Europa, keeping the pressure on Germania."
    default profile_roijean_description = "A commander of Franzo. Childhood friends with Cyrano, she is is an ambitious and rebellious fighter. Having risen through the ranks, her aim is to make her country strong and defensible. She is an optimist and a popular figure among her troops. With a severe dislike for Germania, she vows to never surrender and continue to resist if the situation becomes dire. Her hobbies include athletics, reading novels and playing wargames."
    default profile_monty_description = "A wily and unpredictable commander, he longs for an opportunity to really prove himself in warfare. A quick-witted fighter, his primary goal is to catch and defeat enemies like Erwina Rommel, reclaiming Britannian territory with his crews of tanks. He often lacks tact and diplomacy, preferring to speak his mind and use down-to-earth language."
    default profile_starin_description = "The Mother of Nations. A teasing, short girl with a height complex, she controls the vast eastern territories and armies of the Union of Sovia. A tyrant and a bully - despite her sweet looks, she is not to be trusted. She wishes to create a paradise on earth and elevate herself to a godlike status. Her hobbies include purging dissidents, drinking hot chocolate and teasing other dictators."
    default profile_hirahita_description = "Known as {i}Nyantei{/i} to her subjects, and as Empress Hirahita to the outside world, she is the royal leader of Zipangu. An authoritative figure with a strong sense of duty, she has to play military factions against one another to keep the government running. Graceful yet commanding, she remains in Zipangu, still overseeing the war with Zhina."
    default profile_roosevelt_description = "A president far away on the Amerikan continent, providing economic support to the {i}Alliance{/i} side. She spends her time eating fast food, playing baseball, dancing, cracking jokes and enjoying her god-given, god-damn freedoms. Secretly working on some kind of suspicious scientific project. She has a strong distrust of Zipangu and Germania, but doesn't want to commit to doing anything about them."
    default profile_manstein_description = "A former advisor and tactician to Hitora, she opted to leave with other members of the {i}Generalstall{/i} and retire to Argentinia. A sensible, fun-loving, older-sister type who grew bored with her isolation, now she's back in Germania to help plan for upcoming battles. A tactician with a great sense of grand strategy, she likes taking big risks and surprising her enemies."
    default profile_mannerheim_description = "A cold and defiant leader, beloved by the people of Finbard. Her icy temperament reflects the empty wastes of the northern tundra. Whilst outwardly a friendly diplomat, she has a fierce dislike for both the {i}Axle{/i} and the Sovians. Her guerrilla tactics against enemy invaders have earned her a reputation for deception. More than anything, she just wants to be left alone."
    default profile_rinni_description = "Il Douché, the leader of the southern, sunny nation of Vitalia. This lazy and forgetful girl is determined to reignite a classical empire, stretching from Grecia to Gypta and beyond. A bit of a forgetful klutz and usually getting herself into trouble, she is an important ally and member of the {i}Axle{/i} alliance. She likes pizza, pasta, naps, and burdening others with her self-inflicted problems."
    default profile_rommel_description = "The {i}Desert Fox{/i}. A sharp-minded soldier with great skill for tactics and strategy. She loves tanks and everything to do with mechanized warfare. Rommel is a foxgirl, an ancient and mystical creature, so she sometimes leaves hairballs on the carpet. Loyal and honest, she will obey orders if threatened with a rolled-up newspaper, or if given treats."
    default profile_gamelin_description = "Leader of the armies of Franzo, responsible for the construction of its defenses. A huge beefy man with massive biceps, legs like tree trunks, a thick neck and an anger problem. You don't want to get on the wrong side of this commander. A hero of the First Great War, he despises all things Germanian and seeks to crush any opposition to Franzo sovereignty. Enjoys bodybuilding, eating and manual labor."
    default profile_badoglio_description = "Second in command to Mussorinni and a powerful mover within the Vitalian military. She usually has to look out for {i}Il Douché{/i} and keep her from making trouble. With a sensible head on her shoulders, she grows tired of waging war and wishes for a strong and secure Vitalia. However, so long as there are successes, she will do as her {i}Douché{/i} commands her."
    default profile_messe_description = "A sisterly girl with a positive attitude. A talented soldier with a penchant for commanding armored divisions. Decorated following fighting in the First Great War, she has proven herself time and again in battle. With Epirus firmly under Vitalia's control, she has been stationed in the region should any conflict arise. Perhaps one of the only truly skilled Vitalian generals fighting in this war."
    default profile_graziani_description = "A cowardly girl, and Chief of Staff of the {i}Regio Lasagnotte{/i}. Short and plain, but with a fiery, determined attitude, she believes in {i}Il Douché{/i} and in the new empire of Vitalia. However, she's quick to run from danger. She's known throughout Afrikaa as {i}'the butcher'{/i} for her pre-war activities in Cyracana and Eastern Vitalia Afrikaa. Likes snacking, reading comics and lazing around."
    default profile_antoness_description = "The {i}Red Dog{/i}. A rather fierce character, she fights to keep the balance of power in Rumanum. Completely loyal to the {i}Axle{/i} cause and fiercely determined. She fears Sovian aggression and wishes to protect Rumanum's borders from the east. She will do anything to impress Hitora and turn Rumanum into a vascist country. All's fair in love and war . . . but Antoness takes things way too far."
    default profile_tito_description = "A scrappy and confident young xommunist rebel, she fights to keep the invaders and nationalists out of Serpana. Initially in a weak position, her popularity has grown within Serpana as the {i}Axle{/i} occupy their lands. With contacts in the {i}Alliance{/i}, this girl works hard to maintain her dominant position among the partisan groups. Likes sundresses, lemonade and repairing bicycles."
    default profile_molotov_description = "A concerned, plain girl and the foreign minister of the Union of Sovia. A diplomat, she is tactful and a girl of outstanding ability, though often overlooked or ignored. Generally mistrustful of others, she had a hand in the purges and is constantly having to adjust her position to survive. She enjoys taking tea and writing music."
    default profile_vasile_description = "An enthusiastic, airheaded girl that fights for Starin's cause. Never one to question orders, she has a tendency to blurt out nonsensical phrases. While she's more interested in having fun than fighting battles, in the heat of the moment, she can be quite fearsome. Has a reputation for brilliant staff work and outstanding operational planning. Likes butterflies and eating stacks of pancakes."
    default profile_stuffy_description = "One of Churchill's close comrades. A serious fighter and pilot, she commands the {i}Britannian Royal Air Force (BRAF){/i}. Her responsibility is to keep Britannia's skies free of {i}Ruftwaffe{/i} planes, and intercept any of Goring's bombers and fighters. A member of the aristocracy, she believes in maintaining the world order and civility above all else. She has a strong love for Lapsang Souchong tea, and believes in fairies."
    default profile_battenia_description = "An aristocrat and naval commander, she helps command the fleets of Britannia against the {i}Axle{/i} threat. It's her desire to maintain Britannian superiority at sea and protect the colonies of the empire. A favorite of Churchill's, Battenia fights valiantly and should not be taken lightly. Likes playing polo, sailing and buying expensive collector automobiles."
    default profile_guderian_description = "A proud and determined soldier with a brilliant mind. Hardworking and loyal to the {i}Nappi{/i} regime, with a great interest in tank warfare . . . in fact, Guderian thinks of little else. A published author, their theories on tank warfare are widely respected. Working with {i}Panzys{/i}, this commander hopes to show the world the power of Germanian engineering and tactics."
    default profile_horthy_description = "A sleepy young girl that always carries around a giant stuffed teddy bear. She seeks to maintain sovereignty over the nation of Hang and supports the {i}Axle{/i} cause in Europa, due to her fierce anti-xommunism and fear of Starin. Whilst friendly on the surface, she wishes to avoid total Germanian influence and interference in Hang's conservative, authoritarian affairs. Her favorite animals are rabbits."
    default profile_smigly_description = "The dictator of the {i}dictatorship-without-a-dictator{/i}. An idol with a legend similar to that of Hitora. Leader of the Bozo gang, the girl has a strong will and a determination to restore the medieval Polix Empire. She runs her country and her army like a gang, having installed herself as the authoritarian mob boss. Likes pierogi, horseriding and killing time doing nothing."
    default profile_dresckow_description = "A daring soldier in the {i}Generalstall{/i}, he has long been disillusioned with Adorofia Hitora's {i}Nappi{/i} regime. A rather serious, no-nonsense individual. Working behind the scenes to bring down the Füühbar, he is the ringleader of the {i}Black Band{/i} and the mastermind behind Operation Sparkles . . ."
    default profile_nyan_description = "The Red Generalissima. A fierce rebel and a believer in Zhinese nationalism, she desires to lead Zhina to victory against Zipangu. When the imperial dynasty fell, she was a key figure in the republic before becoming dictator. Full of patriotic zeal and the leader of the Kittentang (KTT) Faction, in a temporary alliance with the Meowists. Sometimes likes to dress up and pretend she's a cat."
    
    default profile_yamato_type = "Ground"
    default profile_joebbels_type = "Ground "
    default profile_goring_type = "Wind"
    default profile_hitora_type = "Dark Mana"
    default profile_cyrano_type = "Fire"
    default profile_churchill_type = "Light Mana"
    default profile_dunitz_type = "Water"
    default profile_zhukky_type = "Ice"
    default profile_roijean_type = " Ground"
    default profile_monty_type = "Electric"
    default profile_starin_type = "Dark Mana "
    default profile_hirahita_type = " Light Mana"
    default profile_roosevelt_type = "Light Mana "
    default profile_manstein_type = " Ground "
    default profile_mannerheim_type = "Ice "
    default profile_rinni_type = "Earth"
    default profile_rommel_type = "Wind "
    default profile_gamelin_type = "Fire "
    default profile_badoglio_type = "Earth "
    default profile_messe_type = "  Ground "
    default profile_graziani_type = "Electric"
    default profile_antoness_type = " Ground  "
    default profile_tito_type = "  Ground  "
    default profile_molotov_type = " Ice"
    default profile_vasile_type = " Ice "
    default profile_stuffy_type = " Wind"
    default profile_battenia_type = "Water "
    default profile_guderian_type = " Fire"
    default profile_horthy_type = " Earth"
    default profile_smigly_type = " Ground   "
    default profile_dresckow_type = "   Ground "
    default profile_nyan_type = " Dark Mana"
        
    default profile_yamato_birthday = "September 10"
    default profile_joebbels_birthday = "October 29"
    default profile_goring_birthday = "January 12"
    default profile_hitora_birthday = "April 20"
    default profile_cyrano_birthday = "November 22"
    default profile_churchill_birthday = "November 30"
    default profile_dunitz_birthday = "September 16"
    default profile_zhukky_birthday = "December 1"
    default profile_roijean_birthday = "February 2"
    default profile_monty_birthday = "November 17"
    default profile_starin_birthday = "December 18"
    default profile_hirahita_birthday = "April 29"
    default profile_roosevelt_birthday = "January 30"
    default profile_manstein_birthday = "November 24"
    default profile_mannerheim_birthday = "June 4"
    default profile_rinni_birthday = "July 29"
    default profile_rommel_birthday = "November 15"
    default profile_gamelin_birthday = "September 20"
    default profile_badoglio_birthday = "September 28"
    default profile_messe_birthday = "December 10"
    default profile_graziani_birthday = "August 11"
    default profile_antoness_birthday = "June 15"
    default profile_tito_birthday = "May 7"
    default profile_molotov_birthday = "December 21"
    default profile_vasile_birthday = "September 30"
    default profile_stuffy_birthday = "April 24"
    default profile_battenia_birthday = "June 25"
    default profile_guderian_birthday = "June 17"
    default profile_horthy_birthday = "June 18"
    default profile_smigly_birthday = "March 11"
    default profile_dresckow_birthday = "January 10"
    default profile_nyan_birthday = "October 31"
        
    default profile_yamato_blood = "Type AB"
    default profile_joebbels_blood = "Type A"
    default profile_goring_blood = "Type O"
    default profile_hitora_blood = " Type A"
    default profile_cyrano_blood = " Type O"
    default profile_churchill_blood = " Type AB"
    default profile_dunitz_blood = "Type B"
    default profile_zhukky_blood = " Type B"
    default profile_roijean_blood = "Type B "
    default profile_monty_blood = " Type B "
    default profile_starin_blood = "Type O "
    default profile_hirahita_blood = "Type A "
    default profile_roosevelt_blood = " Type O "
    default profile_manstein_blood = "Type AB "
    default profile_mannerheim_blood = "  Type B "
    default profile_rinni_blood = " Type O  "
    default profile_rommel_blood = " Type AB "
    default profile_gamelin_blood = "  Type O "
    default profile_badoglio_blood = " Type B  "
    default profile_messe_blood = "  Type B  "
    default profile_graziani_blood = "   Type B  "
    default profile_antoness_blood = " Type A "
    default profile_tito_blood = "  Type O  "
    default profile_molotov_blood = "   Type O  "
    default profile_vasile_blood = "   Type B   "
    default profile_stuffy_blood = "    Type B   "
    default profile_battenia_blood = "  Type AB "
    default profile_guderian_blood = " Type O   "
    default profile_horthy_blood = "   Type O "
    default profile_smigly_blood = "   Type O    "
    default profile_dresckow_blood = "    Type B    "
    default profile_nyan_blood = " Type AB  "
        
    default profile_yamato_zodiac = "Virgo"
    default profile_joebbels_zodiac = "Scorpio"
    default profile_goring_zodiac = "Capricorn"
    default profile_hitora_zodiac = "Taurus"
    default profile_cyrano_zodiac = "Sagittarius"
    default profile_churchill_zodiac = "Sagittarius "
    default profile_dunitz_zodiac = " Virgo"
    default profile_zhukky_zodiac = " Sagittarius"
    default profile_roijean_zodiac = "Aquarius"
    default profile_monty_zodiac = " Scorpio"
    default profile_starin_zodiac = " Sagittarius "
    default profile_hirahita_zodiac = "Taurus "
    default profile_roosevelt_zodiac = "Aquarius "
    default profile_manstein_zodiac = "Scorpio "
    default profile_mannerheim_zodiac = "Gemini"
    default profile_rinni_zodiac = "Leo"
    default profile_rommel_zodiac = " Scorpio "
    default profile_gamelin_zodiac = "Virgo "
    default profile_badoglio_zodiac = "Libra"
    default profile_messe_zodiac = " Sagittarius  "
    default profile_graziani_zodiac = "Leo "
    default profile_antoness_zodiac = "Gemini "
    default profile_tito_zodiac = " Taurus"
    default profile_molotov_zodiac = "  Sagittarius "
    default profile_vasile_zodiac = "Libra "
    default profile_stuffy_zodiac = " Taurus "
    default profile_battenia_zodiac = "Cancer"
    default profile_guderian_zodiac = " Gemini"
    default profile_horthy_zodiac = " Gemini "
    default profile_smigly_zodiac = "Pisces"
    default profile_dresckow_zodiac = "Capricorn "
    default profile_nyan_zodiac = "  Scorpio "
        
    default profile_yamato_height = 178
    default profile_joebbels_height = 142
    default profile_goring_height = 166
    default profile_hitora_height = 165
    default profile_cyrano_height = 168
    default profile_churchill_height = 155
    default profile_dunitz_height = 176
    default profile_zhukky_height = 177
    default profile_roijean_height = 154
    default profile_monty_height = 187
    default profile_starin_height = 147
    default profile_hirahita_height = 170
    default profile_roosevelt_height = 182
    default profile_manstein_height = 180
    default profile_mannerheim_height = 169
    default profile_rinni_height = 163
    default profile_rommel_height = 156
    default profile_gamelin_height = 190
    default profile_badoglio_height = 171
    default profile_messe_height = 153
    default profile_graziani_height = 151
    default profile_antoness_height = 143
    default profile_tito_height = 152
    default profile_molotov_height = 157
    default profile_vasile_height = 167
    default profile_stuffy_height = 162
    default profile_battenia_height = 179
    default profile_guderian_height = 158
    default profile_horthy_height = 140
    default profile_smigly_height = 172
    default profile_dresckow_height = 181
    default profile_nyan_height = 144
        
    default profile_yamato_drink = "Umeshu"
    default profile_joebbels_drink = "Milk"
    default profile_goring_drink = "Gravy"
    default profile_hitora_drink = "Kiba"
    default profile_cyrano_drink = "Red Wine"
    default profile_churchill_drink = "Earl Grey"
    default profile_dunitz_drink = "Whisky"
    default profile_zhukky_drink = "Vodka"
    default profile_roijean_drink = "White Wine"
    default profile_monty_drink = "Pale Ale"
    default profile_starin_drink = "Hot Chocolate"
    default profile_hirahita_drink = "Sake"
    default profile_roosevelt_drink = "Milkshake"
    default profile_manstein_drink = "Gluhwein"
    default profile_mannerheim_drink = "Lakka"
    default profile_rinni_drink = "Amaretto"
    default profile_rommel_drink = "Water"
    default profile_gamelin_drink = "Coffee"
    default profile_badoglio_drink = "Bombardino"
    default profile_messe_drink = "Cappuccino"
    default profile_graziani_drink = "Limoncello"
    default profile_antoness_drink = "Rachiu"
    default profile_tito_drink = "Slivovitz"
    default profile_molotov_drink = "Kompot"
    default profile_vasile_drink = "Medovukha"
    default profile_stuffy_drink = "Lapsang Souchong"
    default profile_battenia_drink = "Rum"
    default profile_guderian_drink = "Apfelschorle"
    default profile_horthy_drink = "Pálinka"
    default profile_smigly_drink = "Mead"
    default profile_dresckow_drink = "Beer"
    default profile_nyan_drink = "Oolong"
        
    default profile_yamato_food = "Tonkatsu"
    default profile_joebbels_food = "Cookies"
    default profile_goring_food = "Potato Chips"
    default profile_hitora_food = "Laugenbrezeln"
    default profile_cyrano_food = "Fondue"
    default profile_churchill_food = "Shepherds Pie"
    default profile_dunitz_food = "Sauerbraten"
    default profile_zhukky_food = "Shchi"
    default profile_roijean_food = "Crepes"
    default profile_monty_food = "Fish & Chips"
    default profile_starin_food = "Stroganoff"
    default profile_hirahita_food = "Takoyaki"
    default profile_roosevelt_food = "Apple Pie"
    default profile_manstein_food = "Schnitzel"
    default profile_mannerheim_food = "Cabbage Roll"
    default profile_rinni_food = "Seafood Pizza"
    default profile_rommel_food = "Oxtail Soup"
    default profile_gamelin_food = "Gougere"
    default profile_badoglio_food = "Gnocchi"
    default profile_messe_food = "Risotto"
    default profile_graziani_food = "Buridda"
    default profile_antoness_food = "Pork Greaves"
    default profile_tito_food = "Cevapcici"
    default profile_molotov_food = "Pelmeni"
    default profile_vasile_food = "Shashlyk"
    default profile_stuffy_food = "Lamb Chops"
    default profile_battenia_food = "Steak Pie"
    default profile_guderian_food = "PBJ Sandwich"
    default profile_horthy_food = "Goulash"
    default profile_smigly_food = "Pierogi"
    default profile_dresckow_food = "Rice Pudding"
    default profile_nyan_food = "Duck Stew"
        
    default profile_yamato_weight = 71
    default profile_joebbels_weight = 41
    default profile_goring_weight = 79
    default profile_hitora_weight = 53
    default profile_cyrano_weight = 57
    default profile_churchill_weight = 50
    default profile_dunitz_weight = 67
    default profile_zhukky_weight = 59
    default profile_roijean_weight = 49
    default profile_monty_weight = 75
    default profile_starin_weight = 40
    default profile_hirahita_weight = 54
    default profile_roosevelt_weight = 63
    default profile_manstein_weight = 61
    default profile_mannerheim_weight = 62
    default profile_rinni_weight = 56
    default profile_rommel_weight = 64
    default profile_gamelin_weight = 130
    default profile_badoglio_weight = 65
    default profile_messe_weight = 51
    default profile_graziani_weight = 48
    default profile_antoness_weight = 45
    default profile_tito_weight = 47
    default profile_molotov_weight = 46
    default profile_vasile_weight = 58
    default profile_stuffy_weight = 55
    default profile_battenia_weight = 70
    default profile_guderian_weight = 52
    default profile_horthy_weight = 44
    default profile_smigly_weight = 66
    default profile_dresckow_weight = 86
    default profile_nyan_weight = 42
        
    default profile_name = profile_yamato_name
    default profile_birthplace = profile_yamato_birthplace
    default profile_role = profile_yamato_role
    default profile_description = profile_yamato_description
    default profile_type = profile_yamato_type
    default profile_birthday = profile_yamato_birthday
    default profile_blood = profile_yamato_blood
    default profile_zodiac = profile_yamato_zodiac
    default profile_height = profile_yamato_height
    default profile_drink = profile_yamato_drink
    default profile_weight = profile_yamato_weight
    default profile_sprite = profile_yamato_sprite
    default profile_flag = profile_yamato_flag
    default profile_food = profile_yamato_food
        
    default active_codex_profiles = {
        "Yamato": [profile_yamato_name, profile_yamato_flag, profile_yamato_birthplace, profile_yamato_description, profile_yamato_type, profile_yamato_birthday, profile_yamato_zodiac, profile_yamato_role, profile_yamato_height, profile_yamato_blood, profile_yamato_drink, profile_yamato_food, profile_yamato_weight, profile_yamato_sprite]
    }
        
    default size_small = "S M A L L   C I T Y"
    default size_large = "L A R G E   C I T Y"
    default size_capital = "C A P I T A L   C I T Y"
        
    default wonder_name = ""
    default wonder_location = ""
    default wonder_description = ""
    default wonder_condition = ""
    default wonder_icon = ""
    default wonder_image = ""
        
    default wonder_name_bigben = "The Albion Clocktower and Palace of Albion"
    default wonder_location_bigben = "Albion, Britannia"
    default wonder_description_bigben = "This Wonder was constructed in the last century, when the old {i}Palace of Albion{/i} was destroyed in a fire. It is the seat of Britannian government and the headquarters of their leader. Britannia was ruled by a monarchy for centuries, until a series of events led to devolved powers passing from the king to elected politicians and ministers. These ministers represent certain regions and peoples of Britannia, and operate within a parliamentary system where they vote on policy - an essential factor of Britannian governance. \n \n Following the Germanian invasion of Czexa and the rise in tensions between nations, the Britannian government attempted to appease Germania by signing a treaty of friendship. Despite this, Adorofia Hitora continued taking land and threatening neighboring countries. Now, Britannia goes to war in defense of Polix, allied with Franzo. Intelligence suggests a War Cabinet has been formed and that the Britannians are rebuilding their armies and navies."
    default wonder_condition_bigben = "Capturing this Wonder would mean the capitulation of the Britannian Empire and the inheritance of their domains."
    default wonder_icon_bigben = "gui/map/bigben_big.png"
    default wonder_image_bigben = "albionsmall"
        
    default wonder_name_imperium = "The Imperiumstag, Brandybutter Gate and Altberlin"
    default wonder_location_imperium = "Altberlin, Germania"
    default wonder_description_imperium = "Germania was once comprised of many smaller kingdoms and principalities. After many centuries of civil war and invasion, order broke down in the small states as they started to rely on one another more. Around this time, the {i}Brandybutter Gate{/i} was constructed. Following the rule of Napoleon, and several more wars, Germania was united into one giant empire. The Imperiumstag was burned down during the early years of Adorofia Hitora's rule. Anarchists were blamed and the government voted to give the Füühbar and the army immense power over public life. Taking advantage of this, Hitora slowly started to rebuild the military and the country, investing in public works and persecuting her enemies. \n \n At first, the destroyed Imperiumstag was left to fall apart and rot, but following pressure from the architect Zpeer, Hitora decided to turn the grounds into a new central government building - partly inspired by her visions of Altberlin becoming a central hub for Europa culture. Thus, the {i}Imperiumstag{/i} and the {i}Imperiumskanzlei{/i} became one and the same. Let's hope it doesn't get destroyed again . . ."
    default wonder_condition_imperium = "Capturing this Wonder would mean the capitulation of the Germanian Empire and the inheritance of their domains."
    default wonder_icon_imperium = "gui/map/imperium_big.png"
    default wonder_image_imperium = "imperiumsmall"
        
    default wonder_name_villa = "The Villa Dorlonia"
    default wonder_location_villa = "Rhome, Vitalia"
    default wonder_description_villa = "This Wonder was constructed in the last century, as a private residence, in the neoclassical style. Vitalia is known for its architectural traditions. Colosseums and amphitheatres were built across the country as far back as the First Century, as arenas for gladitorial entertainment. Competitors would battle to the death for the amusement of the patrician class in Ancient Vitalia. This glorious tradition is one of many images we have of the ancient empire, and is a great inspiration to the Vitalian leader, Mussorinni. It is her desire to revive the old traditions and bring about a glorious new age for Vitalia. \n \n The Villa Dorlonia is not very well fortified and is beginning to crumble. The government and military in the capital are very corrupt, spending most days eating pasta and throwing loud parties. It is for this reason that Mussorinni spends a lot of time at her summer retreat on the coast - although she tends to relax on the beach and eat rather than train or make policies."
    default wonder_condition_villa = "Capturing this Wonder would mean the capitulation of Vitalia and the inheritance of their domains."
    default wonder_icon_villa = "gui/map/villa_big.png"  
    default wonder_image_villa = "rinnimansionsmall"
        
    default wonder_name_kremlin = "The Xremlin and Scarlet Square"
    default wonder_location_kremlin = "Moskva, Sovia Major"
    default wonder_description_kremlin = "The {i}Xremlin{/i} is a citadel fortress inside the Sovian capital city Moskva. This Wonder was first constructed several centuries ago, when the Union of Sovia was a tsarist monarchy. Its role and usage has changed many times throughout history, and its layout consists of dozens of palaces, cathedrals, towers and fortifications. \n \n Following the Sovian Revolution, it became a symbolic headquarters for the xommunist regime, with Renin's mausoleum nearby and a necropolis constructed within the {i}Xremlin{/i} walls themselves. It is the seat of Sovian government and the headquarters of Iosefina Starin, their dictator. The {i}Xremlin{/i} is adjacent to {i}Scarlet Square{/i}, a large public area used for military marches and displays of new weapons."
    default wonder_condition_kremlin = "Capturing this Wonder would mean the capitulation of the Sovian Empire and the inheritance of their domains."
    default wonder_icon_kremlin = "gui/map/kremlin_big.png"   
    default wonder_image_kremlin = "starinbasesmall"
        
    default wonder_name_giza = "The Great Pyramid"
    default wonder_location_giza = "Kair, Gypta"
    default wonder_description_giza = "This Wonder was constructed centuries ago, as a tomb for a Gyptan ruler, the Pharaoh. In the ancient world, the Gyptans ruled the southern shores in millennia-old dynasties. A mysterious people noted for their ingenuity, they have long been a topic of fascination in Europa. \n \n In the last century, archaeology teams from all over the continent were dispatched to discover more of the ancient world. When Napoleon declared war on Britannia, she looted many artifacts and treasures from the temples and pyramids of Gypta. This region is now a stronghold for {i}Alliance{/i} desert forces and is a potential front for new wars and conflicts."
    default wonder_condition_giza = "Capturing this Wonder would mean the capitulation of Gypta and the strong grip of the {i}Alliance{/i} in the south."
    default wonder_icon_giza = "gui/map/pyramid_big.png"
    default wonder_image_giza = "pyramidsmall"
        
    default wonder_name_eiffel = "The Tower of Lutetia and Arc de Trompette"
    default wonder_location_eiffel = "Lutetia, Franzo"
    default wonder_description_eiffel = "The {i}Arc de Trompette{/i} was built during the Napoleonic era, to commemorate Franzo's war dead and victory in the field. It is a symbol of pride and liberty to the citizens of Franzo. \n \n The {i}Tower of Lutetia{/i}, a large metallic construction, was built late in the last century, in time for the {i}World Fair{/i}. It has long been thought of as an ugly abomination by the citizens of Lutetia, but it has also gained supporters. Many see it as a symbol of Franzo's modernity and a testament to the industrial might of the western nation."
    default wonder_condition_eiffel = "Capturing this Wonder would mean the capitulation of the Franzo Republic and the inheritance of their domains."
    default wonder_icon_eiffel = "gui/map/eiffel_big.png"
    default wonder_image_eiffel = "lutetiasmall"
        
    default maptown_update = None
        
    default population_small = 40000
    default population_large = 80000
    default population_capital = 120000
        
    default bat000001_title = "Operation Tutorial: Training Grounds"
    default bat000002_title = "Operation Honeybadger: Polix Sabotage"
    default bat000003_title = "Operation White Pixie: Invasion of Polix"
    default bat000004_title = "Operation Cream Puff: Battle of Varsaa"
    default bat000005_title = "Operation Sneaky: Tunnels beneath Varsaa"
    default bat000006_title = "Operation Hot Cocoa: Battle of Finbard"
    default bat000007_title = "Operation Shhhh: Polix Unrest"
    default bat000008_title = "Operation Playdate: Invasion of Dania"
    default bat000009_title = "Operation Crayon: Dania Art Run"
    default bat000010_title = "Operation Big Jubblies: Battle of the Norda Sea"
    default bat000011_title = "Operation Snowball: Battle of Vkam"
    default bat000012_title = "Operation Duck: Battle of the Northern Sea"
    default bat000013_title = "Operation Snow Angel: Battle of Nidaros"
    default bat000014_title = "Operation Marshmallow: Defense of Knarravik"
    default bat000016_title = "Operation Pen: Battle of Hegrastadkleiva Fortress"
    default bat000045_title = "Operation Air Training: Training Airfield"
    default bat000018_title = "Operation Cherry Blossom: Battle of Fort Ebin"
    default bat000019_title = "Operation Red Gnome: Battle of Xrebbeberg"
    default bat000020_title = "Operation Chalk: Batavia Art Run"
    default bat000021_title = "Operation Boots: Battle of Zeetopia"
    default bat000022_title = "Operation Sprouts: Battle of Belgae"
    default bat000023_title = "Operation Lipgloss: Battle of Hardknut"
    default bat000024_title = "Operation Beachball: Battle of the Amerikan Sea"
    default bat000025_title = "Operation Sunny Day: Battle of the Ardennen"
    default bat000026_title = "Operation Donut: Battle of Mintkornetto"
    default bat000027_title = "Operation Creek: Battle of the Mousse River"
    default bat000028_title = "Operation Pastel: Belgae Art Run"
    default bat000029_title = "Operation Moshi Moshi: Battle of Atrecht"
    default bat000030_title = "Operation Gerbil: Siege of Rijsel"
    default bat000031_title = "Operation Spaniel: Siege of Bononia"
    default bat000032_title = "Operation Hamster: Siege of Kales"
    default bat000033_title = "Operation Paddleboard: Battle of Dunkirch"
    default bat000034_title = "Operation Shortcake: Battle of The Weygand Line"
    default bat000035_title = "Operation Garlic: Battle of Lutetia"
    default bat000037_title = "Operation Bikini: Battle of the Medata Sea"
    default bat000038_title = "Operation Mummy: Invasion of Gypta"
    default bat000039_title = "Operation Sarcophagus: Battle of Zidiparrani"
    default bat000040_title = "Operation Jungle: Battle of Tug Oregano"
    default bat000041_title = "Operation Bloomers: Battle of Goofra Fort"
    default bat000042_title = "Operation Cactus: Battle of Palmaa"
    default bat000043_title = "Operation Vulture: Battle of Kabon"
    default bat000044_title = "Operation Pew-Pew: Battle of Britannia"
    default bat000048_title = "Operation Mozzarella: Battle of Klisura Pass"
    default bat000049_title = "Operation Groundhog: Battle of Singidun"
    default bat000053_title = "Operation Meat Pie: Battle of Vrhbosna"
    default bat000055_title = "Operation Hercules: Battle of Grecia I"
    default bat000056_title = "Operation Sunnyside Eggs: Battle of Cyracana"
    default bat000057_title = "Operation Zeus: Battle of Grecia II"
    default bat000058_title = "Operation Accordion: Battle of Kaptara"
    default bat000060_title = "Operation Kangaroo: Siege of Tobrunsk"
    default bat000063_title = "Operation Desert Kitty: Battle of Iraji"
    default bat000065_title = "Operation Import-Exporter: Battle of Assyria"
    default bat000066_title = "Operation Sphinx: Battle of Cyracana"
    default bat000073_title = "Operation Crumpet: Battle of Albion"
    default bat000081_title = "Operation Crane: Air Battle Over Sovia Minor"
    default bat000083_title = "Operation Red Dog: Battle of Rumanum"
    default bat000085_title = "Operation Takebacksies: Finbard Battle"
    default bat000086_title = "Operation Penguin: Battle of Livonia"
    default bat000087_title = "Operation Barbara-Ann: Invasion of Sovia Minor"
    default bat000093_title = "Operation Ox: Battle of Broody"
    default bat000088_title = "Operation Moth: Battle of Minx"
    default bat000089_title = "Operation Wet Summer: Battle of Smolenx"
    default bat000090_title = "Operation Rubble: Battle of Khiava"
    default bat000091_title = "Operation Queen: Battle of Bryanx"
    default bat000092_title = "Operation Bear: Battle of Moskva"
    default bat000094_title = "Operation Wolf: Battle of Altberlin"
        
    default bat000001_summary = "gui/captured/terrain_grass.png"
    default bat000002_summary = "gui/captured/terrain_forest.png"
    default bat000003_summary = "gui/captured/terrain_forest.png"
    default bat000004_summary = "gui/captured/terrain_urban.png"
    default bat000005_summary = "gui/captured/terrain_urban.png"
    default bat000006_summary = "gui/captured/terrain_ice.png"
    default bat000007_summary = "gui/captured/terrain_forest.png"
    default bat000008_summary = "gui/captured/terrain_grass.png"
    default bat000009_summary = "gui/captured/terrain_grass.png"
    default bat000010_summary = "gui/captured/terrain_sea.png"
    default bat000011_summary = "gui/captured/terrain_ice.png"
    default bat000012_summary = "gui/captured/terrain_sea.png"
    default bat000013_summary = "gui/captured/terrain_ice.png"
    default bat000014_summary = "gui/captured/terrain_ice.png"
    default bat000016_summary = "gui/captured/terrain_ice.png"
    default bat000045_summary = "gui/captured/terrain_air.png"
    default bat000018_summary = "gui/captured/terrain_forest.png"
    default bat000019_summary = "gui/captured/terrain_forest.png"
    default bat000020_summary = "gui/captured/terrain_grass.png"
    default bat000021_summary = "gui/captured/terrain_grass.png"
    default bat000022_summary = "gui/captured/terrain_grass.png"
    default bat000023_summary = "gui/captured/terrain_forest.png"
    default bat000024_summary = "gui/captured/terrain_sea.png"
    default bat000025_summary = "gui/captured/terrain_forest.png"
    default bat000026_summary = "gui/captured/terrain_grass.png"
    default bat000027_summary = "gui/captured/terrain_urban.png"
    default bat000028_summary = "gui/captured/terrain_grass.png"
    default bat000029_summary = "gui/captured/terrain_urban.png"
    default bat000030_summary = "gui/captured/terrain_urban.png"
    default bat000031_summary = "gui/captured/terrain_urban.png"
    default bat000032_summary = "gui/captured/terrain_urban.png"
    default bat000033_summary = "gui/captured/terrain_sea.png"
    default bat000034_summary = "gui/captured/terrain_forest.png"
    default bat000035_summary = "gui/captured/terrain_urban.png"
    default bat000037_summary = "gui/captured/terrain_sea.png"
    default bat000038_summary = "gui/captured/terrain_desert.png"
    default bat000039_summary = "gui/captured/terrain_desert.png"
    default bat000040_summary = "gui/captured/terrain_jungle.png"
    default bat000041_summary = "gui/captured/terrain_desert.png"
    default bat000042_summary = "gui/captured/terrain_desert.png"
    default bat000043_summary = "gui/captured/terrain_jungle.png"
    default bat000044_summary = "gui/captured/terrain_air.png"
    default bat000048_summary = "gui/captured/terrain_canyon.png"
    default bat000049_summary = "gui/captured/terrain_grass.png"
    default bat000053_summary = "gui/captured/terrain_urban.png"  
    default bat000055_summary = "gui/captured/terrain_canyon.png"
    default bat000056_summary = "gui/captured/terrain_desert.png"
    default bat000057_summary = "gui/captured/terrain_canyon.png"
    default bat000058_summary = "gui/captured/terrain_canyon.png"
    default bat000060_summary = "gui/captured/terrain_desert.png"
    default bat000063_summary = "gui/captured/terrain_air.png"
    default bat000065_summary = "gui/captured/terrain_desert.png"
    default bat000066_summary = "gui/captured/terrain_desert.png"
    default bat000073_summary = "gui/captured/terrain_urban.png"
    default bat000081_summary = "gui/captured/terrain_air.png"
    default bat000083_summary = "gui/captured/terrain_sea.png"
    default bat000085_summary = "gui/captured/terrain_ice.png"
    default bat000086_summary = "gui/captured/terrain_forest.png"
    default bat000087_summary = "gui/captured/terrain_grass.png"
    default bat000093_summary = "gui/captured/terrain_grass.png"
    default bat000088_summary = "gui/captured/terrain_urban.png"
    default bat000089_summary = "gui/captured/terrain_urban.png"
    default bat000090_summary = "gui/captured/terrain_urban.png"
    default bat000091_summary = "gui/captured/terrain_urban.png"
    default bat000092_summary = "gui/captured/terrain_urban.png"
        
    default bat000001_description = "Get ready for basic training at your local barracks! Play as {color=#FF1A1A}AXLE{/color}."
    default bat000002_description = "An optional mission. Take command of a crack squad of soldiers and create havoc with a false flag operation. Cut communications with the capital city. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000003_description = "Germania's master plan to expand into the east. In collusion with Sovian forces, invade the neighboring nation of Polix. Begin the invasion here. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000004_description = "With the invasion of Polix under way, battle into the conquered capital city of Varsaa. Destroy any resistance and claim the city from its defenders. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000005_description = "Adorofia Hitora has a secret mission for your unit. Accompany the dictator through the old tunnels . . . Play as {color=#FF1A1A}AXLE{/color}."
    default bat000006_description = "An optional mission. This icy northern nation needs help. Travel with the {i}Hang Volunteer Battalion{/i} and defend the Mannerheim Line against the invading Sovian forces. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000007_description = "An optional mission. Resistance members inside the borders of Germanian Polix are causing trouble for the occupying forces. Follow the intelligence and snuff them out. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000008_description = "To secure its borders, Germania must expand northward. Invade the neutral nation of Dania, secure the capital city and destroy any resistance. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000009_description = "An optional mission. With victory comes the spoils of war. Goring wants to rob this nation of her treasures for a museum in Altberlin. Help guard her detachment. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000010_description = "As the Germanian invasion force moves across the seas towards Norda, enemy ships are encountered. Observe with the Kriegssee and defend the transport ships. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000011_description = "An optional mission. King Haakon has escaped the capital city and Germanian paratroopers are in pursuit. Battle the skiing defenders and stop that train. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000012_description = "An optional mission. The Britannian navy are in the area, attempting to blockade the ports of Norda and cut off ore supplies. Board the {i}Pissmarck{/i} and sink enemy ships. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000013_description = "The Britannians are coming to Norda's aid. Troops have landed on the western shores, and are to engage the Germanians in the town of Nidaros. Fight them off. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000014_description = "The northern city of Knarravik has become an epicenter of fighting, as the Britannians bravely hold onto the port town. Take a detachment north and take the city. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000016_description = "Hegrastadkleiva Fortress in central Norda continues to hold out against the Germanian invasion. Finish them off and end the campaign in Norda. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000045_description = "Get ready for basic training at your local airfield! Play as {color=#FF1A1A}AXLE{/color}."
    default bat000018_description = "The invasion of the west has begun. On the first day of hostilities, join paratroopers in an assault against the {i}Alliance{/i} at Fort Ebin, a heavily fortified castle in Belgae. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000019_description = "The invasion of neutral Batavia begins. Germanian forces come up against the fortified {i}Xrebbe Line{/i}, a series of trenches and fortifications. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000020_description = "An optional mission. With victory comes the spoils of war. Goring wants to rob this nation of her treasures for a museum in Altberlin. Help guard her detachment. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000021_description = "The region of Zeetopia continues to hold strong, with Commander-in-Chief Vinkelman defending. Push forward and destroy the last of Batavia's resistance. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000022_description = "The invasion of neutral Belgae begins. The {i}Alliance{/i} sends its forces to defend the north-western borders, drawn out of Franzo. Join the invasion. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000023_description = "Confront the tank brigades of the {i}Alliance{/i} expeditionary forces around Hardknut. Rout their efforts to push back the invasion. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000024_description = "An optional mission. The Britannian navy are lending support to Franzo's navy. Board the {i}Pissmarck{/i} and sink the enemy ships. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000025_description = "It's time to take on Franzo! Invading through the Ardennen Forest, Germanian armies will break through towards the city of Saloon, taking the enemy by surprise. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000026_description = "A Franzo tank division has attacked the village of Mintkornetto, attempting to cut Germanian supply lines. Confront their forces and regain control. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000027_description = "Germanian tanks have been held back at the Mousse River by enemy forces. Break through their lines and ford the river, fighting your way south. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000028_description = "An optional mission. With victory comes the spoils of war. Goring wants to rob this nation of her treasures for a museum in Altberlin. Help guard her detachment. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000029_description = "The citadel of Atrecht has become a crossroads, with enemy armies meeting at this crunch point. Defeat the {i}Alliance{/i} forces and break through. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000030_description = "The Franzo First Army has made its way to the town of Rijsel in the northwest, fighting back the invasion. Use this opportunity to ambush the enemy. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000031_description = "Guderian's {i}Panzys{/i} are moving to secure the town of Bononia, in the northwestern region of Franzo. Push on towards the coast and rout the enemy. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000032_description = "Rommel's forces are pushing on towards the channel ports in order to catch the retreating {i}B.E.E.F{/i}. Push on towards the coast and rout the enemy. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000033_description = "The {i}B.E.E.F.{/i} are cornered, aiming to retreat from Dunkirch. Despite Hitora's orders for Germanian forces to halt and recuperate, some battle towards the coast. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000034_description = "The Franzo forces hold out in their concrete bunkers and trenches, slowly becoming surrounded by Germanian armies. Strike against their fortifications and trap them. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000035_description = "Resistance continues in Lutetia's outer suburbs, as Weygand's forces are surrounded in the east. Battle through the outer suburbs to secure the capital. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000037_description = "Vitalian transport ships are being attacked by {i}Alliance{/i} forces in the Medata Sea. Observe the naval battle and ensure we reach Cyracana on the southern shores. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000038_description = "Vitalia is staging an invasion of Britannian-held Gypta. Join an expeditionary force and help Graziani push into enemy territory, battling across the wire. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000039_description = "The Gyptan coastal resort of Zidiparrani continues to hold out against bombardment and invasion. Fight on against Britannia and capture the seaside town. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000040_description = "Vitalian forces are invading the Britannian colony of Zomali, in the jungles of the east. Help battle the {i}Alliance{/i} defenders and claim this territory. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000041_description = "Intelligence suggests Britannian forces and {i}Franzo Libre{/i} rebels will attack the fort at Goofra. Defend the desert town as part of the Vitalian garrison there. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000042_description = "With the help of the Britannian navy, {i}Franzo Libre{/i} forces are attacking the coastal city of Palmaa, trying to take it from {i}Vichei Franzo{/i}. Observe as a prisoner-of-war. Play as {color=#4D60F0}ALLIANCE{/color}."
    default bat000043_description = "The region of Kabon in Franzo Gonko, central Afrikaa, is being invaded by {i}Franzo Libre{/i}, to take it from {i}Vichei Franzo{/i}. Observe as a prisoner-of-war. Play as {color=#4D60F0}ALLIANCE{/color}."
    default bat000044_description = "Britannia is under siege. Dogfights ensue in the skies over Britannia, to ensure aerial dominance in the region. Fight the {i}Ruftwaffe{/i} with Stuffy's fighters. Play as {color=#4D60F0}ALLIANCE{/color}."
    default bat000073_description = "Having escaped from the Tower of Albion, the Germanian prisoners-of-war encounter resistance from soldiers, as they battle their way to Churchill. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000048_description = "The Vitalian colony has been invaded by a coalition of Britannian and Grecian forces. Hold onto the region and fight as the Vitalians, defending the pass. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000049_description = "A pro-{i}Alliance{/i} coup in Serpana has exposed a weakness on Germania's southern flanks. Now the {i}Axle{/i} will invade, teaching the weak country a lesson. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000056_description = "Cyracana has fallen to Wavell and the {i}Britannian Desert Forces{/i}. Rommel must take command and beat back the enemy forces. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000053_description = "The defenses in Serpana have all but collapsed. Germanian and Vitalian forces pour into the country, as the last of the resistance holds out in the south. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000060_description = "Ostralasian and Britannian forces hold out at the cut-off Vitalian port of Tobrunsk. Rommel's tanks surround the area, readying for an assault. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000055_description = "The pro-{i}Alliance{/i} Grecian forces have retreated from Epirus, as the {i}Axle{/i} sweep south, invading. Ostralasians hold the line, ready to defend the country. Play as {color=#4D60F0}ALLIANCE{/color}."
    default bat000057_description = "The Ostralasians fight to hold the Grecian valley at Thermomalis, as the Germanians continue their blitz of an invasion. Can Vasey hold them off? Play as {color=#4D60F0}ALLIANCE{/color}."
    default bat000058_description = "This Grecian island is being held by a Britannian lizard with an attitude. Defend the isle against paratroopers and hold the airfields. Play as {color=#4D60F0}ALLIANCE{/color}."
    default bat000063_description = "An optional mission. There's been a revolution in Iraji, and the {i}Ruftwaffe{/i} are supporting the rebels. The {i}BRAF{/i} fights for aerial supremacy as they take control. Play as {color=#4D60F0}ALLIANCE{/color}."
    default bat000065_description = "{i}Franzo Libre{/i} has sent fighters into Assyria to overthrow the {i}Axle{/i} and {i}Vichei{/i} forces based there. Can Cyrano take control of this important province? Play as {color=#4D60F0}ALLIANCE{/color}."
    default bat000087_description = "This is it. Adorofia Hitora's invasion of the Union of Sovia. Germanian troops swarm into Sovia Minor, defeating the border forces and establishing a foothold. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000081_description = "The surprise invasion of the Union of Sovia has caught the Sovian air force off-guard. The {i}Ruftwaffe{/i} take advantage, destroying the airfields and their fighters. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000086_description = "On the northern front, Erika Manstein leads Germanian troops forward into Sovian-occupied Livonia, breaking through the defensive lines. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000083_description = "Antoness, the {i}Red Dog{/i}, is proving her loyalty to Hitora by invading Sovian Moldvaya, battling across rivers and plains for control, as the Sovians retreat. Play as {color=#A02FFF}SOVIA{/color}."
    default bat000085_description = "Marshal Mannerheim joins the {i}Axle{/i} invasion and battles southwards into Sovian Xarelia, reopening hostilities put on ice since the {i}Wintertime War{/i}. Play as {color=#A02FFF}SOVIA{/color}."
    default bat000088_description = "Germanian forces are pushing further into Sovia Minor as the war drags on. Fight alongside Sovian forces to retain control of Minx and defeat the invaders. Play as {color=#A02FFF}SOVIA{/color}."
    default bat000093_description = "A giant armored battle is beginning around Broody. Rumor has it that the Germanians have finished development on a new supertank prototype. Play as {color=#A02FFF}SOVIA{/color}."
    default bat000066_description = "Rommel's successes in the deserts have led her into a confrontation with Monty and his new Rat Army. Battle this wily Britannian and escape his clutches. Play as {color=#FF1A1A}AXLE{/color}."
    default bat000089_description = "Germanian forces are pushing further into Sovia Minor as the war drags on. Fight alongside Sovian forces to retain control of Smolenx and defeat the invaders. Play as {color=#A02FFF}SOVIA{/color}."
    default bat000090_description = "Germanian forces are pushing further into Sovia Minor as the war drags on. The Sovians fight to hold open the pocket around Khiava as they retreat. Play as {color=#A02FFF}SOVIA{/color}."
    default bat000091_description = "Commander Zhukky is making a stand against the invading Germanians, coming face-to-face with Guderian's forces before they reach Moskva. Play as {color=#A02FFF}SOVIA{/color}."
    default bat000092_description = "Starin fights on alone, trapped in her capital city. Find her, fight her, end the war and conquer Europa. Good luck, you can do it. Play as {color=#FFFFFF}YAMATO{/color}."
        
    default bat000001_type = 1
    default bat000002_type = 2
    default bat000003_type = 1
    default bat000004_type = 1
    default bat000005_type = 1
    default bat000006_type = 1
    default bat000007_type = 2
    default bat000008_type = 1
    default bat000009_type = 2
    default bat000010_type = 1
    default bat000011_type = 2
    default bat000012_type = 2
    default bat000013_type = 1
    default bat000014_type = 1
    default bat000016_type = 1
    default bat000045_type = 1
    default bat000018_type = 1
    default bat000019_type = 1
    default bat000020_type = 2
    default bat000021_type = 2
    default bat000022_type = 1
    default bat000023_type = 1
    default bat000024_type = 2
    default bat000025_type = 1
    default bat000026_type = 1
    default bat000027_type = 1
    default bat000028_type = 2
    default bat000029_type = 1
    default bat000030_type = 2
    default bat000031_type = 2
    default bat000032_type = 1
    default bat000033_type = 1
    default bat000034_type = 1
    default bat000035_type = 1
    default bat000037_type = 1
    default bat000038_type = 1
    default bat000039_type = 1
    default bat000040_type = 1
    default bat000041_type = 1
    default bat000042_type = 1
    default bat000043_type = 1
    default bat000044_type = 1
    default bat000048_type = 1
    default bat000049_type = 1
    default bat000053_type = 1
    default bat000055_type = 1
    default bat000056_type = 2
    default bat000057_type = 1
    default bat000058_type = 1
    default bat000060_type = 2
    default bat000063_type = 2
    default bat000065_type = 1
    default bat000066_type = 2
    default bat000073_type = 1
    default bat000081_type = 2
    default bat000083_type = 1
    default bat000085_type = 2
    default bat000086_type = 2
    default bat000087_type = 1
    default bat000088_type = 2
    default bat000089_type = 1
    default bat000090_type = 1
    default bat000091_type = 1
    default bat000092_type = 1
    default bat000093_type = 1
    
    default bat000002_x = .55
    default bat000003_x = .56
    default bat000004_x = .6
    default bat000005_x = .6
    default bat000006_x = .78
    default bat000007_x = .54
    default bat000008_x = .45
    default bat000009_x = .425
    default bat000010_x = .32
    default bat000011_x = .38
    default bat000012_x = .19
    default bat000013_x = .29
    default bat000014_x = .25
    default bat000016_x = .27
    default bat000018_x = .28
    default bat000019_x = .37
    default bat000020_x = .37
    default bat000021_x = .28
    default bat000022_x = .35
    default bat000023_x = .33
    default bat000024_x = .1
    default bat000025_x = .34
    default bat000026_x = .255
    default bat000027_x = .3
    default bat000028_x = .28
    default bat000029_x = .31
    default bat000030_x = .255
    default bat000031_x = .2
    default bat000032_x = .23
    default bat000033_x = .24
    default bat000034_x = .31
    default bat000035_x = .23
    default bat000037_x = .5
    default bat000038_x = .66
    default bat000039_x = .68
    default bat000040_x = .89
    default bat000041_x = .62
    default bat000042_x = .03
    default bat000043_x = .21
    default bat000044_x = .1
    default bat000048_x = .59
    default bat000049_x = .59
    default bat000053_x = .59
    default bat000055_x = .62
    default bat000056_x = .63
    default bat000057_x = .62
    default bat000058_x = .63
    default bat000060_x = .65
    default bat000063_x = .92
    default bat000065_x = .85
    default bat000066_x = .66
    default bat000073_x = .14
    default bat000081_x = .76
    default bat000083_x = .74
    default bat000085_x = .85
    default bat000086_x = .65
    default bat000087_x = .68
    default bat000088_x = .74
    default bat000089_x = .79
    default bat000090_x = .83
    default bat000091_x = .87
    default bat000092_x = .88
    default bat000093_x = .73
    
    default bat000002_y = .3
    default bat000003_y = .33
    default bat000004_y = .36
    default bat000005_y = .33
    default bat000006_y = .05
    default bat000007_y = .29
    default bat000008_y = .28
    default bat000009_y = .26
    default bat000010_y = .2
    default bat000011_y = .06
    default bat000012_y = .115
    default bat000013_y = .09
    default bat000014_y = .012
    default bat000016_y = .1
    default bat000018_y = .37
    default bat000019_y = .31
    default bat000020_y = .28
    default bat000021_y = .3
    default bat000022_y = .355
    default bat000023_y = .36
    default bat000024_y = .43
    default bat000025_y = .41
    default bat000026_y = .4
    default bat000027_y = .39
    default bat000028_y = .34
    default bat000029_y = .4
    default bat000030_y = .393
    default bat000031_y = .377
    default bat000032_y = .37
    default bat000033_y = .35
    default bat000034_y = .43
    default bat000035_y = .405
    default bat000037_y = .75
    default bat000038_y = .78
    default bat000039_y = .78
    default bat000040_y = .94
    default bat000041_y = .9
    default bat000042_y = .87
    default bat000043_y = .92
    default bat000044_y = .3
    default bat000048_y = .625
    default bat000049_y = .5
    default bat000053_y = .55
    default bat000055_y = .6
    default bat000056_y = .81
    default bat000057_y = .64
    default bat000058_y = .695
    default bat000060_y = .8
    default bat000063_y = .76
    default bat000065_y = .63
    default bat000066_y = .79
    default bat000073_y = .24
    default bat000081_y = .29
    default bat000083_y = .37
    default bat000085_y = .065
    default bat000086_y = .21
    default bat000087_y = .3
    default bat000088_y = .26
    default bat000089_y = .25
    default bat000090_y = .29
    default bat000091_y = .25
    default bat000092_y = .23
    default bat000093_y = .31
        
    default active_invasionbeacons_items = {
        "bat000002": [bat000002_description, bat000002_title, bat000002_type, bat000002_x, bat000002_y],
        "bat000003": [bat000003_description, bat000003_title, bat000003_type, bat000003_x, bat000003_y]
    }
        
    default maptown_name = ""
    default maptown_size = ""
    default maptown_governor_pic = ""
    default maptown_profileimg = ""
    default maptown_hostility = ""
    default maptown_population = 0
    default maptown_allegiance = ""
    default maptown_alignment = ""
    default maptown_publicorder = 0
    default maptown_influence = 0
    default maptown_command = ""
    default maptown_management = ""
    default maptown_governor = ""
    default maptown_unlocktown = False
    default maptown_martial = []
    default maptown_siege = False
    
    default maptown_entertainment_worth = ""
    default maptown_military_worth = ""
    default maptown_corruption_worth = ""
    default maptown_farming_worth = ""
    default maptown_mining_worth = ""
    default maptown_industry_worth = ""
    default maptown_trade_worth = ""
        
    default status_atpeace = "{color=#92FF83}AT PEACE{/color}"
    default status_atwar = "{color=#FF6F6F}AT WAR{/color}"
    default power_strong = "{color=#92FF83}STRONG{/color}"
    default power_moderate = "{color=#F1F364}MODERATE{/color}"
    default power_weak = "{color=#FF6F6F}WEAK{/color}"
    default hostility_protectorate = "{color=#92FF83}AXLE PROTECTORATE{/color}"
    default hostility_besties = "{color=#92FF83}AXLE BESTIES{/color}"
    default hostility_nemesis = "{color=#FF6F6F}AXLE NEMESIS{/color}"
    default hostility_hostile = "{color=#FFBD4B}AXLE HOSTILE{/color}"
    default hostility_neutral = "{color=#B7E2DE}NEUTRAL{/color}"
    default hostility_friendly = "{color=#92FF83}AXLE FRIENDLY{/color}"
    default hostility_unfriendly = "{color=#F1F364}ALLIANCE FRIENDLY{/color}"
    default hostility_untrusted = "{color=#B7E2DE}UNTRUSTWORTHY{/color}"
    default hostility_none = "NONE"
    default allegiance_axle = "{color=#FF1A1A}AXLE{/color}"
    default allegiance_alliance = "{color=#4D60F0}ALLIANCE{/color}"
    default allegiance_sovian = "{color=#A02FFF}SOVIAN{/color}"
    default allegiance_nonaligned = "{color=#88FF68}NON-ALIGNED{/color}"
    default coa_protectorate = "This nation is an {i}Axle{/i} protectorate. Trade agreements, military cooperation and further assurances exist between these countries. Together, they fight under the {i}Axle{/i} name, to conquer Europa in one common purpose."
    default coa_alliance = "This nation is an {i}Axle{/i} ally. Trade agreements, military cooperation and further assurances exist between these countries. Together, they fight under the {i}Axle{/i} name, to conquer Europa in one common purpose."
    default coa_nemesis = "This nation proves an almighty threat to the continued existence of the {i}Axle{/i}. Hitora believes this enemy must be destroyed at all costs, through warfare and conquest. There is no hope of imposing ideals through occupation - this nation must first be obliterated and rebuilt from the ashes."
    default coa_hostile = "These people are considered enemies of the {i}Axle{/i}. Their claims to their territory, their freedom, and their livelihood are threatened at all times, through warfare and conquest. In time, this nation might be absorbed into the {i}Axle{/i} through occupation."
    default coa_neutral = "This nation is neutral. Both the {i}Axle{/i} and the {i}Alliance{/i} want friendly diplomatic relations to be established. We must know more about these people – where their factories are, their military bases, their armies and their plans. For now, there are matters of greater concern."
    default coa_friendly = "This nation is friendly with the {i}Axle{/i}. Trade agreements, military cooperation and further assurances may be offered. {i}Axle{/i} allies have already made such arrangements. The {i}Axle{/i} continue to extend an olive branch."
    default coa_unfriendly = "This nation is friendly with the {i}Alliance{/i}. Trade agreements, military cooperation and further assurances may be offered. {i}Alliance{/i} allies have already made such arrangements. The {i}Alliance{/i} continue to extend an olive branch."
    default coa_untrusted = "This nation is not to be trusted. It may have a temporary alliance with its former enemies, or claim to be neutral. But such actions are duplicitous. It would be wise to be careful when dealing with this power."
    default coa_germania = coa_alliance
        
    default germania_empire = "{color=#ED2E2E}GERMANIA{/color}"
    default sovia_empire = "{color=#D056C6}SOVIA{/color}"
    default franzo_empire = "{color=#3E45DA}FRANZO{/color}"
    default britannia_empire = "{color=#C7CC38}BRITANNIA{/color}"
    default vitalia_empire = "{color=#FE7523}VITALIA{/color}"
    default hang_empire = "{color=#B1223D}HANG{/color}"
    default grecia_empire = "{color=#4DC795}GRECIA{/color}"
    default trevera_empire = "{color=#79BA62}TREVERA{/color}"
    default serpana_empire = "{color=#6D4E3E}SERPANA{/color}"
    default galatia_empire = "{color=#E0C02D}GALATIA{/color}"
    default bolga_empire = "{color=#ABCC38}BOLGA{/color}"
    default belgae_empire = "{color=#FE7523}BELGAE{/color}"
    default iberia_empire = "{color=#A54545}IBERIA{/color}"
    default batavia_empire = "{color=#D1B349}BATAVIA{/color}"
    default rumanum_empire = "{color=#A12929}RUMANUM{/color}"
    default livonia_empire = "{color=#8FD3B1}LIVONIA{/color}"
    default finbard_empire = "{color=#5940A2}FINBARD{/color}"
    default norda_empire = "{color=#92B5E1}NORDA{/color}"
    default svenda_empire = "{color=#CCD1ED}SVENDA{/color}"
    default dania_empire = "{color=#99D064}DANIA{/color}"
    default polix_empire = "{color=#EFA8EC}POLIX{/color}"
    default swizi_empire = "{color=#CEE79D}SWIZI{/color}"
    default vicheifranzo_empire = "{color=#3E45DA}VICHEI FRANZO{/color}"
    default franzolibre_empire = "{color=#3E45DA}FRANZO LIBRE{/color}"
        
    default afrikaa_alignment = franzo_empire
    default assyria_alignment = franzo_empire
    default batavia_alignment = batavia_empire
    default belgae_alignment = belgae_empire
    default bolga_alignment = bolga_empire
    default borussia_alignment = germania_empire
    default britannia_alignment = britannia_empire
    default cilly_alignment = vitalia_empire
    default xorsa_alignment = franzo_empire
    default cyracana_alignment = vitalia_empire
    default czexa_alignment = germania_empire
    default dania_alignment = dania_empire
    default ogygia_alignment = britannia_empire
    default epirus_alignment = vitalia_empire
    default finbard_alignment = finbard_empire
    default franzo_alignment = franzo_empire
    default galatia_alignment = galatia_empire
    default germania_alignment = germania_empire
    default gibrata_alignment = britannia_empire
    default grecia_alignment = grecia_empire
    default gypta_alignment = britannia_empire
    default hang_alignment = hang_empire
    default iberia_alignment = iberia_empire
    default vitalia_alignment = vitalia_empire
    default iraji_alignment = britannia_empire
    default kaptara_alignment = grecia_empire
    default kyprosa_alignment = britannia_empire
    default livonia_alignment = livonia_empire
    default maltana_alignment = britannia_empire
    default norda_alignment = norda_empire
    default osta_alignment = germania_empire
    default palesta_alignment = britannia_empire
    default polix_alignment = polix_empire
    default polixgermania_alignment = germania_empire
    default polixsovia_alignment = sovia_empire
    default rumanum_alignment = rumanum_empire
    default zardina_alignment = vitalia_empire
    default serpana_alignment = serpana_empire
    default soviamajor_alignment = sovia_empire
    default soviaminor_alignment = sovia_empire
    default svenda_alignment = svenda_empire
    default swizi_alignment = swizi_empire
    default trevera_alignment = germania_empire
    default tripolita_alignment = franzo_empire
    default zomali_alignment = britannia_empire
    default banki_alignment = franzo_empire
    default franzogonko_alignment = franzo_empire
    default britanniannigella_alignment = britannia_empire
    default kamrun_alignment = franzo_empire
    default westafrikaa_alignment = franzo_empire
    default franzooccupied_alignment = germania_empire
    default franzovichei_alignment = germania_empire
    default xrovat_alignment = germania_empire
    default cervetiis_alignment = germania_empire
    default sovxarelia_alignment = sovia_empire
    
    default afrikaa_power = power_moderate
    default afrikaa_hostility = hostility_neutral
    default afrikaa_allegiance = allegiance_alliance
    default afrikaa_coa = coa_hostile 
    default assyria_power = power_weak
    default assyria_hostility = hostility_hostile
    default assyria_allegiance = allegiance_alliance
    default assyria_coa = coa_hostile
    default batavia_power = power_weak
    default batavia_hostility = hostility_neutral
    default batavia_allegiance = allegiance_nonaligned
    default batavia_coa = coa_neutral
    default belgae_power = power_weak
    default belgae_hostility = hostility_neutral
    default belgae_allegiance = allegiance_nonaligned
    default belgae_coa = coa_neutral
    default bolga_power = power_weak
    default bolga_hostility = hostility_neutral
    default bolga_allegiance = allegiance_nonaligned
    default bolga_coa = coa_neutral
    default borussia_power = power_weak
    default borussia_hostility = hostility_protectorate
    default borussia_allegiance = allegiance_axle
    default borussia_coa = coa_protectorate
    default britannia_power = power_strong
    default britannia_hostility = hostility_nemesis
    default britannia_allegiance = allegiance_alliance
    default britannia_coa = coa_nemesis
    default cilly_power = power_weak
    default cilly_hostility = hostility_besties
    default cilly_allegiance = allegiance_axle
    default cilly_coa = coa_alliance
    default xorsa_power = power_weak
    default xorsa_hostility = hostility_neutral
    default xorsa_allegiance = allegiance_alliance
    default xorsa_coa = coa_nemesis
    default cyracana_power = power_moderate
    default cyracana_hostility = hostility_besties
    default cyracana_allegiance = allegiance_axle
    default cyracana_coa = coa_alliance
    default czexa_power = power_weak
    default czexa_hostility = hostility_protectorate
    default czexa_allegiance = allegiance_axle
    default czexa_coa = coa_protectorate 
    default dania_power = power_weak
    default dania_hostility = hostility_neutral
    default dania_allegiance = allegiance_nonaligned
    default dania_coa = coa_neutral
    default ogygia_power = power_weak
    default ogygia_hostility = hostility_neutral
    default ogygia_allegiance = allegiance_alliance
    default ogygia_coa = coa_neutral
    default epirus_power = power_weak
    default epirus_hostility = hostility_friendly
    default epirus_allegiance = allegiance_axle
    default epirus_coa = coa_friendly
    default finbard_power = power_moderate
    default finbard_hostility = hostility_friendly
    default finbard_allegiance = allegiance_nonaligned
    default finbard_coa = coa_friendly
    default franzo_power = power_strong
    default franzo_hostility = hostility_nemesis
    default franzo_allegiance = allegiance_alliance
    default franzo_coa = coa_nemesis
    default galatia_power = power_moderate
    default galatia_hostility = hostility_friendly
    default galatia_allegiance = allegiance_nonaligned
    default galatia_coa = coa_friendly
    default germania_power = power_strong
    default germania_hostility = hostility_none
    default germania_allegiance = allegiance_axle
    default germania_coa = coa_germania
    default gibrata_power = power_weak
    default gibrata_hostility = hostility_hostile
    default gibrata_allegiance = allegiance_alliance
    default gibrata_coa = coa_hostile
    default grecia_power = power_moderate
    default grecia_hostility = hostility_unfriendly
    default grecia_allegiance = allegiance_nonaligned
    default grecia_coa = coa_unfriendly
    default gypta_power = power_moderate
    default gypta_hostility = hostility_hostile
    default gypta_allegiance = allegiance_alliance
    default gypta_coa = coa_hostile
    default hang_power = power_moderate
    default hang_hostility = hostility_friendly
    default hang_allegiance = allegiance_nonaligned
    default hang_coa = coa_friendly
    default iberia_power = power_moderate
    default iberia_hostility = hostility_friendly
    default iberia_allegiance = allegiance_nonaligned
    default iberia_coa = coa_friendly
    default vitalia_power = power_moderate
    default vitalia_hostility = hostility_besties
    default vitalia_allegiance = allegiance_axle
    default vitalia_coa = coa_alliance
    default iraji_power = power_moderate
    default iraji_hostility = hostility_unfriendly
    default iraji_allegiance = allegiance_alliance
    default iraji_coa = coa_unfriendly
    default kaptara_power = power_weak
    default kaptara_hostility = hostility_unfriendly
    default kaptara_allegiance = allegiance_nonaligned
    default kaptara_coa = coa_unfriendly
    default kyprosa_power = power_weak
    default kyprosa_hostility = hostility_unfriendly
    default kyprosa_allegiance = allegiance_alliance
    default kyprosa_coa = coa_unfriendly
    default livonia_power = power_weak
    default livonia_hostility = hostility_neutral
    default livonia_allegiance = allegiance_nonaligned
    default livonia_coa = coa_neutral
    default maltana_power = power_weak
    default maltana_hostility = hostility_hostile
    default maltana_allegiance = allegiance_alliance
    default maltana_coa = coa_hostile
    default zipangu_power = power_strong
    default zipangu_hostility = hostility_friendly
    default zipangu_allegiance = allegiance_nonaligned
    default zipangu_coa = coa_friendly
    default norda_power = power_moderate
    default norda_hostility = hostility_neutral
    default norda_allegiance = allegiance_nonaligned
    default norda_coa = coa_neutral
    default osta_power = power_strong
    default osta_hostility = hostility_protectorate
    default osta_allegiance = allegiance_axle
    default osta_coa = coa_protectorate
    default palesta_power = power_moderate
    default palesta_hostility = hostility_hostile
    default palesta_allegiance = allegiance_alliance
    default palesta_coa = coa_hostile
    default polix_power = power_weak
    default polix_hostility = hostility_hostile
    default polix_allegiance = allegiance_alliance
    default polix_coa = coa_hostile
    default polixgermania_power = power_moderate
    default polixgermania_hostility = hostility_protectorate
    default polixgermania_allegiance = allegiance_axle
    default polixgermania_coa = coa_protectorate
    default polixsovia_power = power_moderate
    default polixsovia_hostility = hostility_neutral
    default polixsovia_allegiance = allegiance_sovian
    default polixsovia_coa = coa_neutral
    default rumanum_power = power_weak
    default rumanum_hostility = hostility_friendly
    default rumanum_allegiance = allegiance_nonaligned
    default rumanum_coa = coa_friendly
    default zardina_power = power_weak
    default zardina_hostility = hostility_besties
    default zardina_allegiance = allegiance_axle
    default zardina_coa = coa_alliance
    default serpana_power = power_weak
    default serpana_hostility = hostility_neutral
    default serpana_allegiance = allegiance_nonaligned
    default serpana_coa = coa_neutral
    default soviamajor_power = power_strong
    default soviamajor_hostility = hostility_untrusted
    default soviamajor_allegiance = allegiance_sovian
    default soviamajor_coa = coa_untrusted
    default soviaminor_power = power_moderate
    default soviaminor_hostility = hostility_untrusted
    default soviaminor_allegiance = allegiance_sovian
    default soviaminor_coa = coa_untrusted
    default svenda_power = power_moderate
    default svenda_hostility = hostility_neutral
    default svenda_allegiance = allegiance_nonaligned
    default svenda_coa = coa_neutral
    default swizi_power = power_weak
    default swizi_hostility = hostility_neutral
    default swizi_allegiance = allegiance_nonaligned
    default swizi_coa = coa_neutral
    default trevera_power = power_weak
    default trevera_hostility = hostility_protectorate
    default trevera_allegiance = allegiance_axle
    default trevera_coa = coa_protectorate
    default tripolita_power = power_weak
    default tripolita_hostility = hostility_hostile
    default tripolita_allegiance = allegiance_alliance
    default tripolita_coa = coa_hostile
    default unitedamerika_power = power_strong
    default unitedamerika_hostility = hostility_unfriendly
    default unitedamerika_allegiance = allegiance_nonaligned
    default unitedamerika_coa = coa_unfriendly
    default zhina_power = power_weak
    default zhina_hostility = hostility_neutral
    default zhina_allegiance = allegiance_nonaligned
    default zhina_coa = coa_unfriendly
    default zomali_power = power_weak
    default zomali_hostility = hostility_unfriendly
    default zomali_allegiance = allegiance_alliance
    default zomali_coa = coa_unfriendly
    default zudanea_power = power_weak
    default zudanea_hostility = hostility_hostile
    default zudanea_allegiance = allegiance_alliance
    default zudanea_coa = coa_hostile
    default niker_power = power_weak
    default niker_hostility = hostility_unfriendly
    default niker_allegiance = allegiance_alliance
    default niker_coa = coa_unfriendly
    default brad_power = power_weak
    default brad_hostility = hostility_unfriendly
    default brad_allegiance = allegiance_alliance
    default brad_coa = coa_unfriendly
    default bradlibre_power = power_weak
    default bradlibre_hostility = hostility_unfriendly
    default bradlibre_allegiance = allegiance_alliance
    default bradlibre_coa = coa_unfriendly
    default eva_power = power_weak
    default eva_hostility = hostility_besties
    default eva_allegiance = allegiance_axle
    default eva_coa = coa_friendly
    default erebiensands_power = power_weak
    default erebiensands_hostility = hostility_neutral
    default erebiensands_allegiance = allegiance_nonaligned
    default erebiensands_coa = coa_neutral
    default banki_power = power_weak
    default banki_hostility = hostility_unfriendly
    default banki_allegiance = allegiance_alliance
    default banki_coa = coa_unfriendly
    default bankilibre_power = power_weak
    default bankilibre_hostility = hostility_unfriendly
    default bankilibre_allegiance = allegiance_alliance
    default bankilibre_coa = coa_unfriendly
    default franzogonko_power = power_weak
    default franzogonko_hostility = hostility_neutral
    default franzogonko_allegiance = allegiance_alliance
    default franzogonko_coa = coa_unfriendly
    default franzogonkolibre_power = power_weak
    default franzogonkolibre_hostility = hostility_unfriendly
    default franzogonkolibre_allegiance = allegiance_alliance
    default franzogonkolibre_coa = coa_unfriendly
    default britanniannigella_power = power_weak
    default britanniannigella_hostility = hostility_unfriendly
    default britanniannigella_allegiance = allegiance_alliance
    default britanniannigella_coa = coa_unfriendly
    default kamrun_power = power_weak
    default kamrun_hostility = hostility_unfriendly
    default kamrun_allegiance = allegiance_alliance
    default kamrun_coa = coa_unfriendly
    default kamrunlibre_power = power_weak
    default kamrunlibre_hostility = hostility_unfriendly
    default kamrunlibre_allegiance = allegiance_alliance
    default kamrunlibre_coa = coa_unfriendly
    default westafrikaa_power = power_weak
    default westafrikaa_hostility = hostility_neutral
    default westafrikaa_allegiance = allegiance_alliance
    default westafrikaa_coa = coa_hostile
    default franzooccupied_power = power_moderate
    default franzooccupied_hostility = hostility_protectorate
    default franzooccupied_allegiance = allegiance_axle
    default franzooccupied_coa = coa_protectorate
    default franzovichei_power = power_moderate
    default franzovichei_hostility = hostility_neutral
    default franzovichei_allegiance = allegiance_axle
    default franzovichei_coa = coa_neutral
    default xrovat_power = power_weak
    default xrovat_hostility = hostility_besties
    default xrovat_allegiance = allegiance_axle
    default xrovat_coa = coa_alliance
    default cervetiis_power = power_weak
    default cervetiis_hostility = hostility_protectorate
    default cervetiis_allegiance = allegiance_axle
    default cervetiis_coa = coa_protectorate
    default sovxarelia_power = power_moderate
    default sovxarelia_hostility = hostility_neutral
    default sovxarelia_allegiance = allegiance_sovian
    default sovxarelia_coa = coa_neutral
        
    #FLAGS
    default afrikaa_flag = "{image=gui/flag_afrikaa.png}"
    default assyria_flag = "{image=gui/flag_assyria.png}"
    default batavia_flag = "{image=gui/flag_batavia.png}"
    default belgae_flag = "{image=gui/flag_belgae.png}"
    default bolga_flag = "{image=gui/flag_bolga.png}"
    default borussia_flag = "{image=gui/flag_borussia.png}"
    default britannia_flag = "{image=gui/flag_britannia.png}"
    default cilly_flag = "{image=gui/flag_vitalia.png}"
    default xorsa_flag = "{image=gui/flag_franzo.png}"
    default cyracana_flag = "{image=gui/flag_cyracana.png}"
    default czexa_flag = "{image=gui/flag_czexa.png}"
    default dania_flag = "{image=gui/flag_dania.png}"
    default ogygia_flag = "{image=gui/flag_ogygia.png}"
    default epirus_flag = "{image=gui/flag_epirus.png}"
    default finbard_flag = "{image=gui/flag_finbard.png}"
    default franzo_flag = "{image=gui/flag_franzo.png}"
    default galatia_flag = "{image=gui/flag_galatia.png}"
    default germania_flag = "{image=gui/flag_germania.png}"
    default gibrata_flag = "{image=gui/flag_gibrata.png}"
    default grecia_flag = "{image=gui/flag_grecia.png}"
    default gypta_flag = "{image=gui/flag_gypta.png}"
    default hang_flag = "{image=gui/flag_hang.png}"
    default iberia_flag = "{image=gui/flag_iberia.png}"
    default vitalia_flag = "{image=gui/flag_vitalia.png}"
    default iraji_flag = "{image=gui/flag_iraji.png}"
    default kaptara_flag = "{image=gui/flag_grecia.png}"
    default kyprosa_flag = "{image=gui/flag_kyprosa.png}"
    default livonia_flag = "{image=gui/flag_livonia.png}"
    default maltana_flag = "{image=gui/flag_britannia.png}"
    default zipangu_flag = "{image=gui/flag_zipangu.png}"
    default norda_flag = "{image=gui/flag_norda.png}"
    default osta_flag = "{image=gui/flag_germania.png}"
    default palesta_flag = "{image=gui/flag_palesta.png}"
    default polix_flag = "{image=gui/flag_polix.png}"
    default polixgermania_flag = "{image=gui/flag_germania.png}"
    default polixsovia_flag = "{image=gui/flag_sovia.png}"
    default rumanum_flag = "{image=gui/flag_rumanum.png}"
    default zardina_flag = "{image=gui/flag_vitalia.png}"
    default serpana_flag = "{image=gui/flag_serpana.png}"
    default soviamajor_flag = "{image=gui/flag_sovia.png}"
    default soviaminor_flag = "{image=gui/flag_sovia.png}"
    default svenda_flag = "{image=gui/flag_svenda.png}"
    default swizi_flag = "{image=gui/flag_swizi.png}"
    default trevera_flag = "{image=gui/flag_germania.png}"
    default tripolita_flag = "{image=gui/flag_tripolita.png}"
    default unitedamerika_flag = "{image=gui/flag_amerika.png}"
    default zhina_flag = "{image=gui/flag_zhina.png}"
    default zomali_flag = "{image=gui/flag_britannia.png}"
    default zudanea_flag = "{image=gui/flag_gypta.png}"
    default niker_flag = "{image=gui/flag_franzo.png}"
    default brad_flag = "{image=gui/flag_franzo.png}"
    default bradlibre_flag = "{image=gui/flag_franzolibre.png}"
    default eva_flag = "{image=gui/flag_vitalia.png}"
    default erebiensands_flag = "{image=gui/flag_erebiensands.png}"
    default banki_flag = "{image=gui/flag_franzo.png}"
    default bankilibre_flag = "{image=gui/flag_franzolibre.png}"
    default franzogonko_flag = "{image=gui/flag_franzo.png}"
    default franzogonkolibre_flag = "{image=gui/flag_franzolibre.png}"
    default britanniannigella_flag = "{image=gui/flag_britannia.png}"
    default kamrun_flag = "{image=gui/flag_franzo.png}"
    default kamrunlibre_flag = "{image=gui/flag_franzolibre.png}"
    default westafrikaa_flag = "{image=gui/flag_franzo.png}"
    default franzooccupied_flag = "{image=gui/flag_germania.png}"
    default franzovichei_flag = "{image=gui/flag_franzo.png}"
    default xrovat_flag = "{image=gui/flag_xrovat.png}"
    default cervetiis_flag = "{image=gui/flag_germania.png}"
    default sovxarelia_flag = "{image=gui/flag_sovia.png}"
        
    default afrikaa_flag2 = "{image=gui/flag_afrikaa2.jpg}"
    default assyria_flag2 = "{image=gui/flag_assyria2.jpg}"
    default batavia_flag2 = "{image=gui/flag_batavia2.jpg}"
    default belgae_flag2 = "{image=gui/flag_belgae2.jpg}"
    default bolga_flag2 = "{image=gui/flag_bolga2.jpg}"
    default borussia_flag2 = "{image=gui/flag_borussia2.jpg}"
    default britannia_flag2 = "{image=gui/flag_britannia2.jpg}"
    default cilly_flag2 = "{image=gui/flag_vitalia2.jpg}"
    default xorsa_flag2 = "{image=gui/flag_franzo2.jpg}"
    default cyracana_flag2 = "{image=gui/flag_cyracana2.jpg}"
    default czexa_flag2 = "{image=gui/flag_czexa2.jpg}"
    default dania_flag2 = "{image=gui/flag_dania2.jpg}"
    default ogygia_flag2 = "{image=gui/flag_ogygia2.jpg}"
    default epirus_flag2 = "{image=gui/flag_epirus2.jpg}"
    default finbard_flag2 = "{image=gui/flag_finbard2.jpg}"
    default franzo_flag2 = "{image=gui/flag_franzo2.jpg}"
    default galatia_flag2 = "{image=gui/flag_galatia2.jpg}"
    default germania_flag2 = "{image=gui/flag_germania2.jpg}"
    default gibrata_flag2 = "{image=gui/flag_gibrata2.jpg}"
    default grecia_flag2 = "{image=gui/flag_grecia2.jpg}"
    default gypta_flag2 = "{image=gui/flag_gypta2.jpg}"
    default hang_flag2 = "{image=gui/flag_hang2.jpg}"
    default iberia_flag2 = "{image=gui/flag_iberia2.jpg}"
    default vitalia_flag2 = "{image=gui/flag_vitalia2.jpg}"
    default iraji_flag2 = "{image=gui/flag_iraji2.jpg}"
    default kaptara_flag2 = "{image=gui/flag_grecia2.jpg}"
    default kyprosa_flag2 = "{image=gui/flag_kyprosa2.jpg}"
    default livonia_flag2 = "{image=gui/flag_livonia2.jpg}"
    default maltana_flag2 = "{image=gui/flag_britannia2.jpg}"
    default zipangu_flag2 = "{image=gui/flag_zipangu2.jpg}"
    default norda_flag2 = "{image=gui/flag_norda2.jpg}"
    default osta_flag2 = "{image=gui/flag_germania2.jpg}"
    default palesta_flag2 = "{image=gui/flag_palesta2.jpg}"
    default polix_flag2 = "{image=gui/flag_polix2.jpg}"
    default polixgermania_flag2 = "{image=gui/flag_germania2.jpg}"
    default polixsovia_flag2 = "{image=gui/flag_sovia2.jpg}"
    default rumanum_flag2 = "{image=gui/flag_rumanum2.jpg}"
    default zardina_flag2 = "{image=gui/flag_vitalia2.jpg}"
    default serpana_flag2 = "{image=gui/flag_serpana2.jpg}"
    default soviamajor_flag2 = "{image=gui/flag_sovia2.jpg}"
    default soviaminor_flag2 = "{image=gui/flag_sovia2.jpg}"
    default svenda_flag2 = "{image=gui/flag_svenda2.jpg}"
    default swizi_flag2 = "{image=gui/flag_swizi2.jpg}"
    default trevera_flag2 = "{image=gui/flag_germania2.jpg}"
    default tripolita_flag2 = "{image=gui/flag_tripolita2.jpg}"
    default unitedamerika_flag2 = "{image=gui/flag_amerika2.jpg}"
    default zhina_flag2 = "{image=gui/flag_zhina2.jpg}"
    default zomali_flag2 = "{image=gui/flag_britannia2.jpg}"
    default zudanea_flag2 = "{image=gui/flag_gypta2.jpg}"
    default niker_flag2 = "{image=gui/flag_franzo2.jpg}"
    default brad_flag2 = "{image=gui/flag_franzo2.jpg}"
    default bradlibre_flag2 = "{image=gui/flag_franzolibre2.jpg}"
    default eva_flag2 = "{image=gui/flag_vitalia2.jpg}"
    default erebiensands_flag2 = "{image=gui/flag_erebiensands2.jpg}"
    default banki_flag2 = "{image=gui/flag_franzo2.jpg}"
    default bankilibre_flag2 = "{image=gui/flag_franzolibre2.jpg}"
    default franzogonko_flag2 = "{image=gui/flag_franzo2.jpg}"
    default franzogonkolibre_flag2 = "{image=gui/flag_franzolibre2.jpg}"
    default britanniannigella_flag2 = "{image=gui/flag_britannia2.jpg}"
    default kamrun_flag2 = "{image=gui/flag_franzo2.jpg}"
    default kamrunlibre_flag2 = "{image=gui/flag_franzolibre2.jpg}"
    default westafrikaa_flag2 = "{image=gui/flag_franzo2.jpg}"
    default franzooccupied_flag2 = "{image=gui/flag_germania2.jpg}"
    default franzovichei_flag2 = "{image=gui/flag_franzo2.jpg}"
    default xrovat_flag2 = "{image=gui/flag_xrovat2.jpg}"
    default cervetiis_flag2 = "{image=gui/flag_germania2.jpg}"
    default sovxarelia_flag2 = "{image=gui/flag_sovia2.jpg}"
        
    default afrikaa_description = "Shares borders with Tripolita, Niker and West Afrikaa."
    default assyria_description = "Shares borders with Galatia, Iraji and Palesta."
    default batavia_description = "Shares borders with Dania, Germania and Belgae."
    default belgae_description = "Shares borders with Batavia, Germania, Trevera and Franzo."
    default bolga_description = "Shares borders with Rumanum, Serpana, Grecia and Galatia."
    default borussia_description = "Shares borders with Polix and Livonia."
    default britannia_description = "An island nation in the Northern Sea."
    default cilly_description = "An island nation in the Iberian Sea."
    default xorsa_description = "An island nation in the Iberian Sea."
    default cyracana_description = "Shares borders with Tripolita, Brad, Zudanea and Gypta."
    default czexa_description = "Shares borders with Germania, Osta, Polix, Rumanum and Hang."
    default dania_description = "Shares borders with Batavia and Germania."
    default ogygia_description = "An island nation in the Norda Sea."
    default epirus_description = "Shares borders with Serpana and Grecia."
    default finbard_description = "Shares borders with Svenda, Sovia Minor and Sovia Major."
    default franzo_description = "Shares borders with Belgae, Trevera, Swizi, Vitalia and Iberia."
    default galatia_description = "Shares borders with Grecia, Bolga and Assyria."
    default germania_description = "Shares borders with Dania, Batavia, Belgae, Trevera, Swizi, Osta, Czexa and Polix."
    default gibrata_description = "Shares borders with Iberia."
    default grecia_description = "Shares borders with Epirus, Serpana, Bolga and Galatia."
    default gypta_description = "Shares borders with Cyracana, Zudanea and Palesta."
    default hang_description = "Shares borders with Osta, Serpana, Rumanum and Czexa."
    default iberia_description = "Shares borders with Franzo and Gibrata."
    default vitalia_description = "Shares borders with Franzo, Swizi, Osta and Serpana."
    default iraji_description = "Shares borders with Erebien Sands, Assyria, Galatia and Palesta."
    default kaptara_description = "An island nation in the Medata Sea."
    default kyprosa_description = "An island nation in the Medata Sea."
    default livonia_description = "Shares borders with Sovia Minor, Polix and Borussia."
    default maltana_description = "An island nation in the Medata Sea."
    default zipangu_description = "A country in the Far East, on the continent of Oriasia."
    default norda_description = "Shares borders with Svenda."
    default osta_description = "Shares borders with Germania, Swizi, Vitalia, Hang, Czexa and Serpana."
    default palesta_description = "Shares borders with Assyria, Iraji and Gypta."
    default polix_description = "Shares borders with Germania, Czexa, Rumanum, Sovia Minor, Livonia and Borussia."
    default polixgermania_description = "Shares borders with Germania, Czexa, Eastern Polix and Borussia."
    default polixsovia_description = "Shares borders with Western Polix, Rumanum, Sovia Minor, Livonia and Borussia."
    default rumanum_description = "Shares borders with Sovia Minor, Polix, Czexa, Hang, Serpana and Bolga."
    default zardina_description = "An island nation in the Iberian Sea."
    default serpana_description = "Shares borders with Osta, Vitalia, Epirus, Grecia, Bolga, Rumanum and Hang."
    default soviamajor_description = "Shares borders with Sovia Minor and Finbard."
    default soviaminor_description = "Shares borders with Livonia, Polix, Rumanum, Finbard and Sovia Major."
    default svenda_description = "Shares borders with Norda and Finbard."
    default swizi_description = "Shares borders with Trevera, Franzo, Vitalia, Osta and Germania."
    default trevera_description = "Shares borders with Germania, Belgae, Franzo, and Swizi."
    default tripolita_description = "Shares borders with Cyracana, Brad, Niker and Afrikaa Minor."
    default unitedamerika_description = "A country in the west over the Amerikan Sea, on the continent of Amerika."
    default zhina_description = "A country in the Far East, on the continent of Oriasia."
    default zomali_description = "Shares borders with Eastern Vitalia Afrikaa."
    default zudanea_description = "Shares borders with Gypta, Cyracana, Brad and Eastern Vitalia Afrikaa."
    default niker_description = "Shares borders with Brad, Tripolita, West Afrikaa, Britannian Nigella and others."
    default brad_description = "Shares borders with Niker, Banki, Kamrun, Britannian Nigella, Tripolita and others."
    default eva_description = "Shares borders with Zudanea and Zomali."
    default erebiensands_description = "Shares borders with Gypta, Palesta and Iraji."
    default banki_description = "Shares borders with Kamrun, Brad and Franzo Gonko."
    default franzogonko_description = "Shares borders with Kamrun and Banki."
    default britanniannigella_description = "Shares borders with Kamrun, Brad, Niker and West Afrikaa."
    default kamrun_description = "Shares borders with Brad, Banki, Franzo Gonko and Britannian Nigella."
    default westafrikaa_description = "Shares borders with Afrikaa Minor, Niker and Britannian Nigella."
    default franzooccupied_description = "Shares borders with Belgae, Trevera, Swizi and Vichei Franzo."
    default franzovichei_description = "Shares borders with Occupied Franzo, Swizi, Vitalia and Iberia."
    default xrovat_description = "Shares borders with Cervetiis, Vitalia, Germania and Hang."
    default cervetiis_description = "Shares borders with Xrovat, Hang, Bolga and Vitalia."
    default sovxarelia_description = "Shares borders with Finbard, Sovia Major and Sovia Minor."
        
    default afrikaa_name = "Protectorate of Afrikaa Minor"
    default assyria_name = "Protectorate of Assyria"
    default batavia_name = "Merchant Kingdom of Batavia"
    default belgae_name = "Kingdom of Belgae"
    default bolga_name = "Kingdom of Bolga"
    default borussia_name = "Protectorate of Borussia"
    default britannia_name = "Empire of Britannia"
    default cilly_name = "Protectorate of Cilly"
    default xorsa_name = "Protectorate of Xorsa"
    default cyracana_name = "Protectorate of Cyracana"
    default czexa_name = "Occupied Czexa"
    default dania_name = "Kingdom of Dania"
    default ogygia_name = "Free Ogygia"
    default epirus_name = "Protectorate of Epirus"
    default finbard_name = "Republic of Finbard"
    default franzo_name = "Franzo Thirteenth Republic"
    default galatia_name = "Republic of Galatia"
    default germania_name = "Nappi Empire of Germania"
    default gibrata_name = "Protectorate City of Gibrata"
    default grecia_name = "Kingdom of Grecia"
    default gypta_name = "Mandate of Gypta"
    default hang_name = "Kingdom of Hang"
    default iberia_name = "Nationalist Kingdom of Iberia"
    default vitalia_name = "Empire of Vitalia"
    default iraji_name = "Mandate of Iraji"
    default kaptara_name = "Protectorate of Kaptara"
    default kyprosa_name = "Protectorate of Kyprosa"
    default livonia_name = "Free States of Livonia"
    default maltana_name = "Protectorate of Maltana"
    default zipangu_name = "Empire of Zipangu"
    default norda_name = "Kingdom of Norda"
    default osta_name = "Protectorate of Osta"
    default palesta_name = "Mandate of Palesta"
    default polix_name = "Republic of Polix"
    default polixgermania_name = "Germanian Occupied Western Polix"
    default polixsovia_name = "Sovian Occupied Eastern Polix"
    default rumanum_name = "Nationalist Kingdom of Rumanum"
    default zardina_name = "Protectorate of Zardina"
    default serpana_name = "Kingdom of Serpana"
    default sovia_name = "Xommunist Union of Sovia"
    default soviamajor_name = "Xommunist Union of Sovia Major"
    default soviaminor_name = "Xommunist Union of Sovia Minor"
    default svenda_name = "Kingdom of Svenda"
    default swizi_name = "Hermit Kingdom of Swizi"
    default trevera_name = "Kingdom of Trevera"
    default tripolita_name = "Protectorate of Tripolita"
    default unitedamerika_name = "United Amerika"
    default zhina_name = "Republic of Zhina"
    default zomali_name = "Colony of Zomali"
    default zudanea_name = "Mandate of Zudanea"
    default niker_name = "Colony of Niker"
    default brad_name = "Colony of Brad"
    default eva_name = "Eastern Vitalia Afrikaa"
    default erebiensands_name = "Erebien Sands"
    default banki_name = "Colony of Banki"
    default franzogonko_name = "Colony of Franzo Gonko"
    default britanniannigella_name = "Colony of Britannian Nigella"
    default kamrun_name = "Colony of Kamrun"
    default westafrikaa_name = "Colony of West Afrikaa"
    default franzooccupied_name = "Occupied Franzo"
    default franzovichei_name = "Vichei Franzo"
    default xrovat_name = "Independent Xrovat"
    default cervetiis_name = "Occupied Cervetiis"
    default sovxarelia_name = "Sovian Occupied Xarelia"
        
    default afrikaa_text = "Afrikaa"
    default assyria_text = "Assyria"
    default batavia_text = "Batavia"
    default belgae_text = "Belgae"
    default bolga_text = "Bolga"
    default borussia_text = "Borussia"
    default britannia_text = "Britannia"
    default cilly_text = "Cilly"
    default xorsa_text = "Xorsa"
    default cyracana_text = "Cyracana"
    default czexa_text = "Czexa"
    default dania_text = "Dania"
    default ogygia_text = "Ogygia"
    default epirus_text = "Epirus"
    default finbard_text = "Finbard"
    default franzo_text = "Franzo"
    default galatia_text = "Galatia"
    default germania_text = "Germania"
    default gibrata_text = "Gibrata"
    default grecia_text = "Grecia"
    default gypta_text = "Gypta"
    default hang_text = "Hang"
    default iberia_text = "Iberia"
    default vitalia_text = "Vitalia"
    default iraji_text = "Iraji"
    default kaptara_text = "Kaptara"
    default kyprosa_text = "Kyprosa"
    default livonia_text = "Livonia"
    default maltana_text = "Maltana"
    default zipangu_text = "Zipangu"
    default norda_text = "Norda"
    default osta_text = "Osta"
    default palesta_text = "Palesta"
    default polix_text = "Polix"
    default polixgermania_text = "Ger. Polix"
    default polixsovia_text = "Sov. Polix"
    default rumanum_text = "Rumanum"
    default zardina_text = "Zardina"
    default serpana_text = "Serpana"
    default sovia_text = "Union of Sovia"
    default soviamajor_text = "Sovia Major"
    default soviaminor_text = "Sovia Minor"
    default svenda_text = "Svenda"
    default swizi_text = "Swizi"
    default trevera_text = "Trevera"
    default tripolita_text = "Tripolita"
    default unitedamerika_text = "United Amerika"
    default zhina_text = "Zhina"
    default zomali_text = "Zomali"
    default zudanea_text = "Zudanea"
    default niker_text = "Niker"
    default brad_text = "Brad"
    default eva_text = "E. V. A."
    default erebiensands_text = "Erebien Sands"
    default banki_text = "Banki"
    default franzogonko_text = "Franzo Gonko"
    default britanniannigella_text = "Brit. Nigella"
    default kamrun_text = "Kamrun"
    default westafrikaa_text = "West Afrikaa"
    default franzooccupied_text = "Occ. Franzo"
    default franzovichei_text = "Vichei Franzo"
    default xrovat_text = "Xrovat"
    default cervetiis_text = "Cervetiis"
    default sovxarelia_text = "Sov. Xarelia"
    default bradlibre_text = "Brad Lib."
    default kamrunlibre_text = "Kamrun Lib."
    default bankilibre_text = "Banki Lib."
    default franzogonkolibre_text = "F. Gonko Lib."
        
    default afrikaa_motto = "GOD, COUNTRY, SURRENDER"
    default assyria_motto = "UNITY, FREEDOM, SURRENDER"
    default batavia_motto = "I WILL MAINTAIN MY PROFIT MARGINS"
    default belgae_motto = "UNITY GIVES STRENGTH"
    default bolga_motto = "UNITY MAKES STRENGTH"
    default borussia_motto = "TO EACH HER OWN"
    default britannia_motto = "KEEP CALM AND DRINK TEA"
    default cilly_motto = "TOGETHER BY PASTA AND RELIGION"
    default xorsa_motto = "LIBERTY, EQUALITY, SURRENDER"
    default cyracana_motto = "TOGETHER BY PASTA AND RELIGION"
    default czexa_motto = "TRUTH PREVAILS ANY DAY NOW"
    default dania_motto = "GOD HELP US"
    default ogygia_motto = "LUCK AND CHARM"
    default epirus_motto = "GIVE ME HONOR"
    default finbard_motto = "THROUGH THE SNOWS"
    default franzo_motto = "LIBERTY, EQUALITY, SURRENDER"
    default galatia_motto = "SOVEREIGNTY BELONGS TO THE RECLINERS"
    default germania_motto = "ONE TYRANNY, ONE EMPIRE, ONE BEAUTY"
    default gibrata_motto = " CONQUERED BY NO MEANIES"
    default grecia_motto = "KEBABS OR DEATH"
    default gypta_motto = "RULE BRITANNIA"
    default hang_motto = "GOD BLESS THE HANGRY"
    default iberia_motto = "ONE, GREAT AND FREE"
    default vitalia_motto = "TOGETHER BY PASTA AND RELIGION"
    default iraji_motto = "GOD IS COOL"
    default kaptara_motto = "KEBABS OR DEATH"
    default kyprosa_motto = "RULE BRITANNIA"
    default livonia_motto = "FATHERLAND AND FREEDOM"
    default maltana_motto = "CONSTANT VIRTUE"
    default zipangu_motto = "A NEW ORDER"
    default norda_motto = "ALL FOR NORDA"
    default osta_motto = "ONE TYRANNY, ONE EMPIRE, ONE BEAUTY"
    default palesta_motto = "RULE BRITANNIA"
    default polix_motto = "FOR OUR FREEDOM AND YOURS"
    default polixgermania_motto = "ONE TYRANNY, ONE EMPIRE, ONE BEAUTY"
    default polixsovia_motto = "GIRLS OF THE WORLD UNITE"
    default rumanum_motto = "HOLE IN ONE"
    default zardina_motto = "SUN, SAND, SEA"
    default serpana_motto = "HOLD FAST"
    default sovia_motto = "GIRLS OF THE WORLD UNITE"
    default soviamajor_motto = "GIRLS OF THE WORLD UNITE"
    default soviaminor_motto = "GIRLS OF THE WORLD UNITE"
    default svenda_motto = "ROLL WITH THE TIMES"
    default swizi_motto = "ONE FOR ALL, ALL FOR ONE"
    default trevera_motto = "ONE TYRANNY, ONE EMPIRE, ONE BEAUTY"
    default tripolita_motto = "FREEDOM, ORDER, JUSTICE"
    default unitedamerika_motto = "IN DESU WE TRUST"
    default zhina_motto = "THE FIRST PEOPLE"
    default zomali_motto = "RULE BRITANNIA"
    default zudanea_motto = "RULE BRITANNIA"
    default niker_motto = "LIBERTY, EQUALITY, SURRENDER"
    default brad_motto = "LIBERTY, EQUALITY, SURRENDER"
    default eva_motto = "TOGETHER BY PASTA AND RELIGION"
    default erebiensands_motto = "SAND, SEA AND OIL"
    default banki_motto = "LIBERTY, EQUALITY, SURRENDER"
    default franzogonko_motto = "LIBERTY, EQUALITY, SURRENDER"
    default britanniannigella_motto = "RULE BRITANNIA"
    default kamrun_motto = "LIBERTY, EQUALITY, SURRENDER"
    default westafrikaa_motto = "LIBERTY, EQUALITY, SURRENDER"
    default franzooccupied_motto = "ONE TYRANNY, ONE EMPIRE, ONE BEAUTY"
    default franzovichei_motto = "LIBERTY, EQUALITY, SURRENDER"
    default xrovat_motto = "TERROR IS THE WAY"
    default cervetiis_motto = "ONE TYRANNY, ONE EMPIRE, ONE BEAUTY"
    default sovxarelia_motto = "GIRLS OF THE WORLD UNITE"
        
    default active_allegiances_items = {
        "afrikaa": [afrikaa_motto, afrikaa_flag, afrikaa_flag2, afrikaa_description, afrikaa_name, afrikaa_coa, afrikaa_hostility, afrikaa_power, afrikaa_allegiance, afrikaa_text],
        "assyria": [assyria_motto, assyria_flag, assyria_flag2, assyria_description, assyria_name, assyria_coa, assyria_hostility, assyria_power, assyria_allegiance, assyria_text],
        "banki": [banki_motto, banki_flag, banki_flag2, banki_description, banki_name, banki_coa, banki_hostility, banki_power, banki_allegiance, banki_text],
        "batavia": [batavia_motto, batavia_flag, batavia_flag2, batavia_description, batavia_name, batavia_coa, batavia_hostility, batavia_power, batavia_allegiance, batavia_text],
        "belgae": [belgae_motto, belgae_flag, belgae_flag2, belgae_description, belgae_name, belgae_coa, belgae_hostility, belgae_power, belgae_allegiance, belgae_text],
        "bolga": [bolga_motto, bolga_flag, bolga_flag2, bolga_description, bolga_name, bolga_coa, bolga_hostility, bolga_power, bolga_allegiance, bolga_text],
        "borussia": [borussia_motto, borussia_flag, borussia_flag2, borussia_description, borussia_name, borussia_coa, borussia_hostility, borussia_power, borussia_allegiance, borussia_text],
        "brad": [brad_motto, brad_flag, brad_flag2, brad_description, brad_name, brad_coa, brad_hostility, brad_power, brad_allegiance, brad_text],
        "britannia": [britannia_motto, britannia_flag, britannia_flag2, britannia_description, britannia_name, britannia_coa, britannia_hostility, britannia_power, britannia_allegiance, britannia_text],
        "britanniannigella": [britanniannigella_motto, britanniannigella_flag, britanniannigella_flag2, britanniannigella_description, britanniannigella_name, britanniannigella_coa, britanniannigella_hostility, britanniannigella_power, britanniannigella_allegiance, britanniannigella_text],
        "cilly": [cilly_motto, cilly_flag, cilly_flag2, cilly_description, cilly_name, cilly_coa, cilly_hostility, cilly_power, cilly_allegiance, cilly_text],
        "cyracana": [cyracana_motto, cyracana_flag, cyracana_flag2, cyracana_description, cyracana_name, cyracana_coa, cyracana_hostility, cyracana_power, cyracana_allegiance, cyracana_text],
        "czexa": [czexa_motto, czexa_flag, czexa_flag2, czexa_description, czexa_name, czexa_coa, czexa_hostility, czexa_power, czexa_allegiance, czexa_text],
        "dania": [dania_motto, dania_flag, dania_flag2, dania_description, dania_name, dania_coa, dania_hostility, dania_power, dania_allegiance, dania_text],
        "ogygia": [ogygia_motto, ogygia_flag, ogygia_flag2, ogygia_description, ogygia_name, ogygia_coa, ogygia_hostility, ogygia_power, ogygia_allegiance, ogygia_text],
        "epirus": [epirus_motto, epirus_flag, epirus_flag2, epirus_description, epirus_name, epirus_coa, epirus_hostility, epirus_power, epirus_allegiance, epirus_text],
        "erebiensands": [erebiensands_motto, erebiensands_flag, erebiensands_flag2, erebiensands_description, erebiensands_name, erebiensands_coa, erebiensands_hostility, erebiensands_power, erebiensands_allegiance, erebiensands_text],
        "eva": [eva_motto, eva_flag, eva_flag2, eva_description, eva_name, eva_coa, eva_hostility, eva_power, eva_allegiance, eva_text],
        "finbard": [finbard_motto, finbard_flag, finbard_flag2, finbard_description, finbard_name, finbard_coa, finbard_hostility, finbard_power, finbard_allegiance, finbard_text],
        "franzo": [franzo_motto, franzo_flag, franzo_flag2, franzo_description, franzo_name, franzo_coa, franzo_hostility, franzo_power, franzo_allegiance, franzo_text],
        "franzogonko": [franzogonko_motto, franzogonko_flag, franzogonko_flag2, franzogonko_description, franzogonko_name, franzogonko_coa, franzogonko_hostility, franzogonko_power, franzogonko_allegiance, franzogonko_text],
        "galatia": [galatia_motto, galatia_flag, galatia_flag2, galatia_description, galatia_name, galatia_coa, galatia_hostility, galatia_power, galatia_allegiance, galatia_text],
        "germania": [germania_motto, germania_flag, germania_flag2, germania_description, germania_name, germania_coa, germania_hostility, germania_power, germania_allegiance, germania_text],
        "gibrata": [gibrata_motto, gibrata_flag, gibrata_flag2, gibrata_description, gibrata_name, gibrata_coa, gibrata_hostility, gibrata_power, gibrata_allegiance, gibrata_text],
        "grecia": [grecia_motto, grecia_flag, grecia_flag2, grecia_description, grecia_name, grecia_coa, grecia_hostility, grecia_power, grecia_allegiance, grecia_text],
        "gypta": [gypta_motto, gypta_flag, gypta_flag2, gypta_description, gypta_name, gypta_coa, gypta_hostility, gypta_power, gypta_allegiance, gypta_text],
        "hang": [hang_motto, hang_flag, hang_flag2, hang_description, hang_name, hang_coa, hang_hostility, hang_power, hang_allegiance, hang_text],
        "iberia": [iberia_motto, iberia_flag, iberia_flag2, iberia_description, iberia_name, iberia_coa, iberia_hostility, iberia_power, iberia_allegiance, iberia_text],
        "iraji": [iraji_motto, iraji_flag, iraji_flag2, iraji_description, iraji_name, iraji_coa, iraji_hostility, iraji_power, iraji_allegiance, iraji_text],
        "kamrun": [kamrun_motto, kamrun_flag, kamrun_flag2, kamrun_description, kamrun_name, kamrun_coa, kamrun_hostility, kamrun_power, kamrun_allegiance, kamrun_text],
        "kaptara": [kaptara_motto, kaptara_flag, kaptara_flag2, kaptara_description, kaptara_name, kaptara_coa, kaptara_hostility, kaptara_power, kaptara_allegiance, kaptara_text],
        "kyprosa": [kyprosa_motto, kyprosa_flag, kyprosa_flag2, kyprosa_description, kyprosa_name, kyprosa_coa, kyprosa_hostility, kyprosa_power, kyprosa_allegiance, kyprosa_text],
        "livonia": [livonia_motto, livonia_flag, livonia_flag2, livonia_description, livonia_name, livonia_coa, livonia_hostility, livonia_power, livonia_allegiance, livonia_text],
        "maltana": [maltana_motto, maltana_flag, maltana_flag2, maltana_description, maltana_name, maltana_coa, maltana_hostility, maltana_power, maltana_allegiance, maltana_text],
        "niker": [niker_motto, niker_flag, niker_flag2, niker_description, niker_name, niker_coa, niker_hostility, niker_power, niker_allegiance, niker_text],
        "norda": [norda_motto, norda_flag, norda_flag2, norda_description, norda_name, norda_coa, norda_hostility, norda_power, norda_allegiance, norda_text],
        "osta": [osta_motto, osta_flag, osta_flag2, osta_description, osta_name, osta_coa, osta_hostility, osta_power, osta_allegiance, osta_text],
        "palesta": [palesta_motto, palesta_flag, palesta_flag2, palesta_description, palesta_name, palesta_coa, palesta_hostility, palesta_power, palesta_allegiance, palesta_text],
        "polix": [polix_motto, polix_flag, polix_flag2, polix_description, polix_name, polix_coa, polix_hostility, polix_power, polix_allegiance, polix_text],
        "rumanum": [rumanum_motto, rumanum_flag, rumanum_flag2, rumanum_description, rumanum_name, rumanum_coa, rumanum_hostility, rumanum_power, rumanum_allegiance, rumanum_text],
        "serpana": [serpana_motto, serpana_flag, serpana_flag2, serpana_description, serpana_name, serpana_coa, serpana_hostility, serpana_power, serpana_allegiance, serpana_text],
        "soviamajor": [soviamajor_motto, soviamajor_flag, soviamajor_flag2, soviamajor_description, soviamajor_name, soviamajor_coa, soviamajor_hostility, soviamajor_power, soviamajor_allegiance, soviamajor_text],
        "soviaminor": [soviaminor_motto, soviaminor_flag, soviaminor_flag2, soviaminor_description, soviaminor_name, soviaminor_coa, soviaminor_hostility, soviaminor_power, soviaminor_allegiance, soviaminor_text],
        "svenda": [svenda_motto, svenda_flag, svenda_flag2, svenda_description, svenda_name, svenda_coa, svenda_hostility, svenda_power, svenda_allegiance, svenda_text],
        "swizi": [swizi_motto, swizi_flag, swizi_flag2, swizi_description, swizi_name, swizi_coa, swizi_hostility, swizi_power, swizi_allegiance, swizi_text],
        "trevera": [trevera_motto, trevera_flag, trevera_flag2, trevera_description, trevera_name, trevera_coa, trevera_hostility, trevera_power, trevera_allegiance, trevera_text],
        "tripolita": [tripolita_motto, tripolita_flag, tripolita_flag2, tripolita_description, tripolita_name, tripolita_coa, tripolita_hostility, tripolita_power, tripolita_allegiance, tripolita_text],
        "unitedamerika": [unitedamerika_motto, unitedamerika_flag, unitedamerika_flag2, unitedamerika_description, unitedamerika_name, unitedamerika_coa, unitedamerika_hostility, unitedamerika_power, unitedamerika_allegiance, unitedamerika_text],
        "vitalia": [vitalia_motto, vitalia_flag, vitalia_flag2, vitalia_description, vitalia_name, vitalia_coa, vitalia_hostility, vitalia_power, vitalia_allegiance, vitalia_text],
        "westafrikaa": [westafrikaa_motto, westafrikaa_flag, westafrikaa_flag2, westafrikaa_description, westafrikaa_name, westafrikaa_coa, westafrikaa_hostility, westafrikaa_power, westafrikaa_allegiance, westafrikaa_text],
        "xorsa": [xorsa_motto, xorsa_flag, xorsa_flag2, xorsa_description, xorsa_name, xorsa_coa, xorsa_hostility, xorsa_power, xorsa_allegiance, xorsa_text],
        "zardina": [zardina_motto, zardina_flag, zardina_flag2, zardina_description, zardina_name, zardina_coa, zardina_hostility, zardina_power, zardina_allegiance, zardina_text],
        "zhina": [zhina_motto, zhina_flag, zhina_flag2, zhina_description, zhina_name, zhina_coa, zhina_hostility, zhina_power, zhina_allegiance, zhina_text],
        "zomali": [zomali_motto, zomali_flag, zomali_flag2, zomali_description, zomali_name, zomali_coa, zomali_hostility, zomali_power, zomali_allegiance, zomali_text],
        "zipangu": [zipangu_motto, zipangu_flag, zipangu_flag2, zipangu_description, zipangu_name, zipangu_coa, zipangu_hostility, zipangu_power, zipangu_allegiance, zipangu_text],
        "zudanea": [zudanea_motto, zudanea_flag, zudanea_flag2, zudanea_description, zudanea_name, zudanea_coa, zudanea_hostility, zudanea_power, zudanea_allegiance, zudanea_text]
    }
    
    default allegiances_motto = germania_motto
    default allegiances_flag2 = germania_flag2
    default allegiances_description = germania_description
    default allegiances_power = power_strong
    default allegiances_allegiance = allegiance_axle
    default allegiances_hostility = hostility_none
    default allegiances_coa = coa_germania
    default allegiances_name = germania_name
        
    default farmtype_farming_worth = "Boom"
    default farmtype_mining_worth = "Bust"
    default farmtype_industry_worth = "Bust"
    default farmtype_trade_worth = "Stable"
    default farmtype_entertainment_worth = "Bust"
    default farmtype_military_worth = "Boom"
    default farmtype_corruption_worth = "Bust"
        
    default minetype_farming_worth = "Bust"
    default minetype_mining_worth = "Boom"
    default minetype_industry_worth = "Bust"
    default minetype_trade_worth = "Stable"
    default minetype_entertainment_worth = "Bust"
    default minetype_military_worth = "Boom"
    default minetype_corruption_worth = "Bust"
        
    default industrytype_farming_worth = "Bust"
    default industrytype_mining_worth = "Bust"
    default industrytype_industry_worth = "Boom"
    default industrytype_trade_worth = "Stable"
    default industrytype_entertainment_worth = "Bust"
    default industrytype_military_worth = "Stable"
    default industrytype_corruption_worth = "Bust"
        
    default tradetype_farming_worth = "Bust"
    default tradetype_mining_worth = "Bust"
    default tradetype_industry_worth = "Bust"
    default tradetype_trade_worth = "Boom"
    default tradetype_entertainment_worth = "Stable"
    default tradetype_military_worth = "Stable"
    default tradetype_corruption_worth = "Stable"
        
    default capitaltype_farming_worth = "Stable"
    default capitaltype_mining_worth = "Stable"
    default capitaltype_industry_worth = "Boom"
    default capitaltype_trade_worth = "Boom"
    default capitaltype_entertainment_worth = "Boom"
    default capitaltype_military_worth = "Boom"
    default capitaltype_corruption_worth = "Boom"
        
    default taiga_name = "Taiga, Franzo"
    default taiga_size = size_small
    default taiga_governor = "Gamelin"
    default taiga_governor_pic = "{image=side gamelin normal}"
    default taiga_command = command_five
    default taiga_management = management_one
    default taiga_influence = influence_three
    default taiga_population = int(renpy.random.uniform(1, 9) * population_large)
    default taiga_publicorder = 20
    default taiga_hostility = franzo_hostility
    default taiga_allegiance = franzo_allegiance
    default taiga_alignment = franzo_alignment
    default taiga_farming_worth = tradetype_farming_worth
    default taiga_mining_worth = tradetype_mining_worth
    default taiga_industry_worth = tradetype_industry_worth
    default taiga_trade_worth = tradetype_trade_worth
    default taiga_entertainment_worth = tradetype_entertainment_worth
    default taiga_military_worth = tradetype_military_worth
    default taiga_corruption_worth = tradetype_corruption_worth
    default taiga_tooltip = False
    default taiga_siege = False
    default taiga_martial = [
        "other_franzo_gunner_heer3_profile",
        "other_franzo_gunner_heer3_profile",
        "panzer_47mmapx_profile",
        "panzer_renaultr3540_profile",
        "panzer_renaultft_profile",
        "airsupport_snotfire_profile"
        ]
    default taiga_unlocktown = False
    default taiga_company_img = [
        "company_freedomburger",
        "company_panpanpan",
        "company_caveavin"
        ]
    default taiga_company_text = {
        company_freedomburger_name: company_freedomburger_description, 
        company_panpanpan_name: company_panpanpan_description, 
        company_caveavin_name: company_caveavin_description
        }
        
    default athenia_name = "Athenia, Grecia"
    default athenia_size = size_capital
    default athenia_governor = "Papagos"
    default athenia_governor_pic = "{image=side man normal}"
    default athenia_command = command_one
    default athenia_management = management_three
    default athenia_influence = influence_one
    default athenia_population = int(renpy.random.uniform(1, 9) * population_capital)
    default athenia_publicorder = 100
    default athenia_hostility = grecia_hostility
    default athenia_allegiance = grecia_allegiance
    default athenia_alignment = grecia_alignment
    default athenia_farming_worth = capitaltype_farming_worth
    default athenia_mining_worth = capitaltype_mining_worth
    default athenia_industry_worth = capitaltype_industry_worth
    default athenia_trade_worth = capitaltype_trade_worth
    default athenia_entertainment_worth = capitaltype_entertainment_worth
    default athenia_military_worth = capitaltype_military_worth
    default athenia_corruption_worth = capitaltype_corruption_worth
    default athenia_tooltip = False
    default athenia_siege = False
    default athenia_martial = [
        "specialgroup_grecia_gunner_heer5_profile",
        "specialgroup_grecia_gunner_heer5_profile",
        "panzer_matilda1_profile",
        "panzer_hotchkiss_profile"
        ]
    default athenia_unlocktown = False
    default athenia_company_img = [
        "company_teaempire",
        "company_southernmining",
        "company_pizzahaus"
        ]
    default athenia_company_text = {
        company_teaempire_name: company_teaempire_description, 
        company_southernmining_name: company_southernmining_description, 
        company_pizzahaus_name: company_pizzahaus_description
        }
        
    default iraklion_name = "Iraklion, Kaptara"
    default iraklion_size = size_large
    default iraklion_governor = "Metaxas"
    default iraklion_governor_pic = "{image=side metaxas normal}"
    default iraklion_command = command_three
    default iraklion_management = management_one
    default iraklion_influence = influence_one
    default iraklion_population = int(renpy.random.uniform(1, 9) * population_large)
    default iraklion_publicorder = 40
    default iraklion_hostility = grecia_hostility
    default iraklion_allegiance = grecia_allegiance
    default iraklion_alignment = grecia_alignment
    default iraklion_farming_worth = tradetype_farming_worth
    default iraklion_mining_worth = tradetype_mining_worth
    default iraklion_industry_worth = tradetype_industry_worth
    default iraklion_trade_worth = tradetype_trade_worth
    default iraklion_entertainment_worth = tradetype_entertainment_worth
    default iraklion_military_worth = tradetype_military_worth
    default iraklion_corruption_worth = tradetype_corruption_worth
    default iraklion_tooltip = False
    default iraklion_siege = False
    default iraklion_martial = [
        "specialgroup_grecia_gunner_heer5_profile",
        "specialgroup_grecia_marksman_heer5_profile",
        "panzer_47mmapx_profile",
        "panzer_matilda1_profile"
        ]
    default iraklion_unlocktown = False
    default iraklion_company_img = [
        "company_guptatours",
        "company_woodyslogging",
        "company_sakurawhale"
        ]
    default iraklion_company_text = {
        company_guptatours_name: company_guptatours_description, 
        company_woodyslogging_name: company_woodyslogging_description, 
        company_sakurawhale_name: company_sakurawhale_description
        }
        
    default zaarkrauten_name = "Zaarkrauten, Trevera"
    default zaarkrauten_size = size_small
    default zaarkrauten_governor = "Bürcgkella"
    default zaarkrauten_governor_pic = "{image=side woman normal}"
    default zaarkrauten_command = command_one
    default zaarkrauten_management = management_one
    default zaarkrauten_influence = influence_one
    default zaarkrauten_population = int(renpy.random.uniform(1, 9) * population_large)
    default zaarkrauten_publicorder = 70
    default zaarkrauten_hostility = trevera_hostility
    default zaarkrauten_allegiance = trevera_allegiance
    default zaarkrauten_alignment = trevera_alignment
    default zaarkrauten_farming_worth = tradetype_farming_worth
    default zaarkrauten_mining_worth = tradetype_mining_worth
    default zaarkrauten_industry_worth = tradetype_industry_worth
    default zaarkrauten_trade_worth = tradetype_trade_worth
    default zaarkrauten_entertainment_worth = tradetype_entertainment_worth
    default zaarkrauten_military_worth = tradetype_military_worth
    default zaarkrauten_corruption_worth = tradetype_corruption_worth
    default zaarkrauten_tooltip = False
    default zaarkrauten_siege = False
    default zaarkrauten_martial = [
        "infantry_germania_gunner_heer1_profile",
        "infantry_germania_gunner_heer1_profile",
        "panzer_hotchkiss_profile"
        ]
    default zaarkrauten_unlocktown = True
    default zaarkrauten_company_img = [
        "company_panpanpan",
        "company_fuuhbarcakes",
        "company_axemann"
        ]
    default zaarkrauten_company_text = {
        company_panpanpan_name: company_panpanpan_description, 
        company_fuuhbarcakes_name: company_fuuhbarcakes_description, 
        company_axemann_name: company_axemann_description
        }
        
    default singidun_name = "Singidun, Serpana"
    default singidun_size = size_capital
    default singidun_governor = "Paulie"
    default singidun_governor_pic = "{image=side politician determined}"
    default singidun_command = command_one
    default singidun_management = management_two
    default singidun_influence = influence_two
    default singidun_population = int(renpy.random.uniform(1, 9) * population_capital)
    default singidun_publicorder = 65
    default singidun_hostility = serpana_hostility
    default singidun_allegiance = serpana_allegiance
    default singidun_alignment = serpana_alignment
    default singidun_farming_worth = capitaltype_farming_worth
    default singidun_mining_worth = capitaltype_mining_worth
    default singidun_industry_worth = capitaltype_industry_worth
    default singidun_trade_worth = capitaltype_trade_worth
    default singidun_entertainment_worth = capitaltype_entertainment_worth
    default singidun_military_worth = capitaltype_military_worth
    default singidun_corruption_worth = capitaltype_corruption_worth
    default singidun_tooltip = False
    default singidun_siege = False
    default singidun_martial = [
            "other_serpana_gunner_heer5_profile",
            "other_serpana_antitank_heer5_profile"
            ]
    default singidun_unlocktown = False
    default singidun_company_img = [
            "company_woodyslogging",
            "company_penguinironworks",
            "company_victorrubber"
            ]
    default singidun_company_text = {
            company_woodyslogging_name: company_woodyslogging_description, 
            company_penguinironworks_name: company_penguinironworks_description, 
            company_victorrubber_name: company_victorrubber_description
            }
        
    default ancyra_name = "Ancyra, Galatia"
    default ancyra_size = size_capital
    default ancyra_governor = "Inonu"
    default ancyra_governor_pic = "{image=side oriasiangeneral normal}"
    default ancyra_command = command_one
    default ancyra_management = management_four
    default ancyra_influence = influence_two
    default ancyra_population = int(renpy.random.uniform(1, 9) * population_capital)
    default ancyra_publicorder = 55
    default ancyra_hostility = galatia_hostility
    default ancyra_allegiance =galatia_allegiance
    default ancyra_alignment =galatia_alignment
    default ancyra_farming_worth = capitaltype_farming_worth
    default ancyra_mining_worth = capitaltype_mining_worth
    default ancyra_industry_worth = capitaltype_industry_worth
    default ancyra_trade_worth = capitaltype_trade_worth
    default ancyra_entertainment_worth = capitaltype_entertainment_worth
    default ancyra_military_worth = capitaltype_military_worth
    default ancyra_corruption_worth = capitaltype_corruption_worth
    default ancyra_tooltip = False
    default ancyra_siege = False
    default ancyra_martial = [
        "panzer_47mmapx_profile",
        "panzer_archer_profile"
        ]
    default ancyra_unlocktown = False
    default ancyra_company_img = [
        "company_southernmining",
        "company_dokuk",
        "company_molkereiwagen"
        ]
    default ancyra_company_text = {
        company_southernmining_name: company_southernmining_description, 
        company_dokuk_name: company_dokuk_description, 
        company_molkereiwagen_name: company_molkereiwagen_description
        }
        
    default zuri_name = "Zuri, Swizi"
    default zuri_size = size_capital
    default zuri_governor = "Guisan"
    default zuri_governor_pic = "{image=side desertgeneral normal}"
    default zuri_command = command_one
    default zuri_management = management_four
    default zuri_influence = influence_two
    default zuri_population = int(renpy.random.uniform(1, 9) * population_capital)
    default zuri_publicorder = 55
    default zuri_hostility = swizi_hostility
    default zuri_allegiance = swizi_allegiance
    default zuri_alignment = swizi_alignment
    default zuri_farming_worth = capitaltype_farming_worth
    default zuri_mining_worth = capitaltype_mining_worth
    default zuri_industry_worth = capitaltype_industry_worth
    default zuri_trade_worth = capitaltype_trade_worth
    default zuri_entertainment_worth = capitaltype_entertainment_worth
    default zuri_military_worth = capitaltype_military_worth
    default zuri_corruption_worth = capitaltype_corruption_worth
    default zuri_tooltip = False
    default zuri_siege = False
    default zuri_martial = [
        "other_norda_gunner_heer2_profile"
        ]
    default zuri_unlocktown = False
    default zuri_company_img = [
        "company_albioncornexchange",
        "company_grupp",
        "company_zippilen"
        ]
    default zuri_company_text = {
        company_albioncornexchange_name: company_albioncornexchange_description, 
        company_grupp_name: company_grupp_description, 
        company_zippilen_name: company_zippilen_description
        }
        
    default serdica_name = "Serdica, Bolga"
    default serdica_size = size_capital
    default serdica_governor = "Boris"
    default serdica_governor_pic = "{image=side youth normal}"
    default serdica_command = command_one
    default serdica_management = management_two
    default serdica_influence = influence_one
    default serdica_population = int(renpy.random.uniform(1, 9) * population_capital)
    default serdica_publicorder = 35
    default serdica_hostility = bolga_hostility
    default serdica_allegiance = bolga_allegiance
    default serdica_alignment = bolga_alignment
    default serdica_farming_worth = capitaltype_farming_worth
    default serdica_mining_worth = capitaltype_mining_worth
    default serdica_industry_worth = capitaltype_industry_worth
    default serdica_trade_worth = capitaltype_trade_worth
    default serdica_entertainment_worth = capitaltype_entertainment_worth
    default serdica_military_worth = capitaltype_military_worth
    default serdica_corruption_worth = capitaltype_corruption_worth
    default serdica_tooltip = False
    default serdica_siege = False
    default serdica_martial = [
        "specialgroup_rumanum_gunner_heer7_profile",
        "specialgroup_rumanum_gunner_heer7_profile"
        ]
    default serdica_unlocktown = False
    default serdica_company_img = [
        "company_woodyslogging",
        "company_victorrubber",
        "company_axemann"
        ]
    default serdica_company_text = {
        company_woodyslogging_name: company_woodyslogging_description, 
        company_victorrubber_name: company_victorrubber_description, 
        company_axemann_name: company_axemann_description
        }
        
    default spruit_name = "Spruit, Belgae"
    default spruit_size = size_capital
    default spruit_governor = "Leopold"
    default spruit_governor_pic = im.Sepia("character/side/leopold_th.png")
    default spruit_command = command_one
    default spruit_management = management_two
    default spruit_influence = influence_two
    default spruit_population = int(renpy.random.uniform(1, 9) * population_capital)
    default spruit_publicorder = 100
    default spruit_hostility = belgae_hostility
    default spruit_allegiance = belgae_allegiance
    default spruit_alignment = belgae_alignment
    default spruit_farming_worth = capitaltype_farming_worth
    default spruit_mining_worth = capitaltype_mining_worth
    default spruit_industry_worth = capitaltype_industry_worth
    default spruit_trade_worth = capitaltype_trade_worth
    default spruit_entertainment_worth = capitaltype_entertainment_worth
    default spruit_military_worth = capitaltype_military_worth
    default spruit_corruption_worth = capitaltype_corruption_worth
    default spruit_tooltip = False
    default spruit_siege = False
    default spruit_martial = [
        "other_franzo_gunner_heer3_profile",
        "other_franzo_gunner_heer3_profile",
        "other_britannia_gunner_heer3_profile",
        "antitank_t13_profile"
        ]
    default spruit_unlocktown = False
    default spruit_company_img = [
        "company_panpanpan",
        "company_freedomburger",
        "company_toothhurty"
        ]
    default spruit_company_text = {
        company_panpanpan_name: company_panpanpan_description, 
        company_freedomburger_name: company_freedomburger_description, 
        company_toothhurty_name: company_toothhurty_description
        }
        
    default mayra_name = "Mayra, Iberia"
    default mayra_size = size_capital
    default mayra_governor = "Franco"
    default mayra_governor_pic = "{image=side basicgeneral happy}"
    default mayra_command = command_three
    default mayra_management = management_two
    default mayra_influence = influence_four
    default mayra_population = int(renpy.random.uniform(1, 9) * population_capital)
    default mayra_publicorder = 40
    default mayra_hostility = iberia_hostility
    default mayra_allegiance = iberia_allegiance
    default mayra_alignment = iberia_alignment
    default mayra_farming_worth = capitaltype_farming_worth
    default mayra_mining_worth = capitaltype_mining_worth
    default mayra_industry_worth = capitaltype_industry_worth
    default mayra_trade_worth = capitaltype_trade_worth
    default mayra_entertainment_worth = capitaltype_entertainment_worth
    default mayra_military_worth = capitaltype_military_worth
    default mayra_corruption_worth = capitaltype_corruption_worth
    default mayra_tooltip = False
    default mayra_siege = False
    default mayra_martial = [
        "panzer_panzer1_profile",
        "panzer_panzer1_profile",
        "airsupport_shrike_profile"
        ]
    default mayra_unlocktown = True
    default mayra_company_img = [
        "company_zippilen",
        "company_ottoflugzeugwerke",
        "company_panpanpan"
        ]
    default mayra_company_text = {
        company_zippilen_name: company_zippilen_description, 
        company_ottoflugzeugwerke_name: company_ottoflugzeugwerke_description, 
        company_panpanpan_name: company_panpanpan_description
        }
    
    default amstel_name = "Amstel, Batavia"
    default amstel_size = size_capital
    default amstel_governor = "Jan de Geer"
    default amstel_governor_pic = "{image=side politician normal}"
    default amstel_command = command_one
    default amstel_management = management_three
    default amstel_influence = influence_one
    default amstel_population = int(renpy.random.uniform(1, 9) * population_capital)
    default amstel_publicorder = 30
    default amstel_hostility = batavia_hostility
    default amstel_allegiance = batavia_allegiance
    default amstel_alignment = batavia_alignment
    default amstel_farming_worth = capitaltype_farming_worth
    default amstel_mining_worth = capitaltype_mining_worth
    default amstel_industry_worth = capitaltype_industry_worth
    default amstel_trade_worth = capitaltype_trade_worth
    default amstel_entertainment_worth = capitaltype_entertainment_worth
    default amstel_military_worth = capitaltype_military_worth
    default amstel_corruption_worth = capitaltype_corruption_worth
    default amstel_tooltip = False
    default amstel_siege = False
    default amstel_martial = [
        "other_batavia_gunner_heer3_profile",
        "antitank_pak36_profile",
        "panzer_47mmapx_profile",
        "panzer_matilda1_profile"
        ]
    default amstel_unlocktown = False
    default amstel_company_img = [
        "company_dokuk",
        "company_albioncornexchange",
        "company_fuuhbarcakes"
        ]
    default amstel_company_text = {
        company_dokuk_name: company_dokuk_description, 
        company_albioncornexchange_name: company_albioncornexchange_description, 
        company_petwelt_name: company_petwelt_description
        }
        
    default rotte_name = "Rotte, Batavia"
    default rotte_size = size_large
    default rotte_governor = "Winkel"
    default rotte_governor_pic = "{image=side official normal}"
    default rotte_command = command_three
    default rotte_management = management_one
    default rotte_influence = influence_one
    default rotte_population = int(renpy.random.uniform(1, 9) * population_large)
    default rotte_publicorder = 30
    default rotte_hostility = batavia_hostility
    default rotte_allegiance = batavia_allegiance
    default rotte_alignment = batavia_alignment
    default rotte_farming_worth = tradetype_farming_worth
    default rotte_mining_worth = tradetype_mining_worth
    default rotte_industry_worth = tradetype_industry_worth
    default rotte_trade_worth = tradetype_trade_worth
    default rotte_entertainment_worth = tradetype_entertainment_worth
    default rotte_military_worth = tradetype_military_worth
    default rotte_corruption_worth = tradetype_corruption_worth
    default rotte_tooltip = False
    default rotte_siege = False
    default rotte_martial = [
        "other_batavia_gunner_heer3_profile",
        "antitank_pak36_profile",
        "panzer_charb1_profile",
        "panzer_matilda2_profile"
        ]
    default rotte_unlocktown = False
    default rotte_company_img = [
        "company_panpanpan",
        "company_magische",
        "company_teaempire"
        ]
    default rotte_company_text = {
        company_panpanpan_name: company_panpanpan_description, 
        company_magische_name: company_magische_description, 
        company_teaempire_name: company_teaempire_description
        }
        
    default bucharex_name = "Bucharex, Rumanum"
    default bucharex_size = size_capital
    default bucharex_governor = "Kalinesgu"
    default bucharex_governor_pic = "{image=side kalinesgu normal}"
    default bucharex_command = command_one
    default bucharex_management = management_three
    default bucharex_influence = influence_three
    default bucharex_population = int(renpy.random.uniform(1, 9) * population_capital)
    default bucharex_publicorder = 33
    default bucharex_hostility = rumanum_hostility
    default bucharex_allegiance = rumanum_allegiance
    default bucharex_alignment = rumanum_alignment
    default bucharex_farming_worth = capitaltype_farming_worth
    default bucharex_mining_worth = capitaltype_mining_worth
    default bucharex_industry_worth = capitaltype_industry_worth
    default bucharex_trade_worth = capitaltype_trade_worth
    default bucharex_entertainment_worth = capitaltype_entertainment_worth
    default bucharex_military_worth = capitaltype_military_worth
    default bucharex_corruption_worth = capitaltype_corruption_worth
    default bucharex_tooltip = False
    default bucharex_siege = False
    default bucharex_martial = [
        "specialgroup_rumanum_gunner_heer7_profile",
        "specialgroup_rumanum_antitank_heer7_profile",
        "specialgroup_rumanum_cavalry_heer7_profile",
        "panzer_toldi_profile"
        ]
    default bucharex_unlocktown = False
    default bucharex_company_img = [
        "company_ghoulish",
        "company_axemann",
        "company_woodyslogging"
        ]
    default bucharex_company_text = {
        company_ghoulish_name: company_ghoulish_description, 
        company_axemann_name: company_axemann_description, 
        company_woodyslogging_name: company_woodyslogging_description
        }
    
    default rija_name = "Rija, Livonia"
    default rija_size = size_capital
    default rija_governor = "Smetona"
    default rija_governor_pic = "{image=side oriasiangeneral normal}"
    default rija_command = command_one
    default rija_management = management_one
    default rija_influence = influence_two
    default rija_population = int(renpy.random.uniform(1, 9) * population_capital)
    default rija_publicorder = 75
    default rija_hostility = livonia_hostility
    default rija_allegiance = livonia_allegiance
    default rija_alignment = livonia_alignment
    default rija_farming_worth = capitaltype_farming_worth
    default rija_mining_worth = capitaltype_mining_worth
    default rija_industry_worth = capitaltype_industry_worth
    default rija_trade_worth = capitaltype_trade_worth
    default rija_entertainment_worth = capitaltype_entertainment_worth
    default rija_military_worth = capitaltype_military_worth
    default rija_corruption_worth = capitaltype_corruption_worth
    default rija_tooltip = False
    default rija_siege = False
    default rija_martial = [
        "infantry_sovia_gunner_heer7_profile",
        "infantry_sovia_gunner_heer7_profile"
        ]
    default rija_unlocktown = False
    default rija_company_img = [
        "company_handlarz",
        "company_woodyslogging",
        "company_sakurawhale"
        ]
    default rija_company_text = {
        company_handlarz_name: company_handlarz_description, 
        company_woodyslogging_name: company_woodyslogging_description, 
        company_sakurawhale_name: company_sakurawhale_description
        }
        
    default helsin_name = "Helsin, Finbard"
    default helsin_size = size_capital
    default helsin_governor = "Mannerheim"
    default helsin_governor_pic = "{image=side mannerheim moe}"
    default helsin_command = command_four
    default helsin_management = management_three
    default helsin_influence = influence_four
    default helsin_population = int(renpy.random.uniform(1, 9) * population_capital)
    default helsin_publicorder = 100
    default helsin_hostility = finbard_hostility
    default helsin_allegiance = finbard_allegiance
    default helsin_alignment = finbard_alignment
    default helsin_farming_worth = capitaltype_farming_worth
    default helsin_mining_worth = capitaltype_mining_worth
    default helsin_industry_worth = capitaltype_industry_worth
    default helsin_trade_worth = capitaltype_trade_worth
    default helsin_entertainment_worth = capitaltype_entertainment_worth
    default helsin_military_worth = capitaltype_military_worth
    default helsin_corruption_worth = capitaltype_corruption_worth
    default helsin_tooltip = False
    default helsin_siege = False
    default helsin_martial = [
        "specialgroup_finbard_gunner_heer2_profile",
        "specialgroup_finbard_marksman_heer2_profile",
        "panzer_bt42_profile"
        ]
    default helsin_unlocktown = False
    default helsin_company_img = [
        "company_penguinironworks",
        "company_victorrubber",
        "company_handlarz"
        ]
    default helsin_company_text = {
        company_penguinironworks_name: company_penguinironworks_description, 
        company_victorrubber_name: company_victorrubber_description, 
        company_handlarz_name: company_handlarz_description
        }
    
    default oxloa_name = "Oxloa, Norda"
    default oxloa_size = size_capital
    default oxloa_governor = "Haakon"
    default oxloa_governor_pic = "{image=side haakon normal}"
    default oxloa_command = command_one
    default oxloa_management = management_three
    default oxloa_influence = influence_two
    default oxloa_population = int(renpy.random.uniform(1, 9) * population_capital)
    default oxloa_publicorder = 80
    default oxloa_hostility = norda_hostility
    default oxloa_allegiance = norda_allegiance
    default oxloa_alignment = norda_alignment
    default oxloa_farming_worth = capitaltype_farming_worth
    default oxloa_mining_worth = capitaltype_mining_worth
    default oxloa_industry_worth = capitaltype_industry_worth
    default oxloa_trade_worth = capitaltype_trade_worth
    default oxloa_entertainment_worth = capitaltype_entertainment_worth
    default oxloa_military_worth = capitaltype_military_worth
    default oxloa_corruption_worth = capitaltype_corruption_worth
    default oxloa_tooltip = False
    default oxloa_siege = False
    default oxloa_martial = [
        "other_norda_gunner_heer2_profile",
        "other_norda_marksman_heer2_profile",
        "panzer_charb1_profile"
        ]
    default oxloa_unlocktown = False
    default oxloa_company_img = [
        "company_penguinironworks",
        "company_tanfa",
        "company_teaempire"
        ]
    default oxloa_company_text = {
        company_penguinironworks_name: company_penguinironworks_description, 
        company_tanfa_name: company_tanfa_description, 
        company_teaempire_name: company_teaempire_description
        }
    
    default syndrome_name = "Syndrome, Svenda"
    default syndrome_size = size_capital
    default syndrome_governor = "Hansson"
    default syndrome_governor_pic = "{image=side man normal}"
    default syndrome_command = command_two
    default syndrome_management = management_five
    default syndrome_influence = influence_three
    default syndrome_population = int(renpy.random.uniform(1, 9) * population_capital)
    default syndrome_publicorder = 70
    default syndrome_hostility = svenda_hostility
    default syndrome_allegiance = svenda_allegiance
    default syndrome_alignment = svenda_alignment
    default syndrome_farming_worth = capitaltype_farming_worth
    default syndrome_mining_worth = capitaltype_mining_worth
    default syndrome_industry_worth = capitaltype_industry_worth
    default syndrome_trade_worth = capitaltype_trade_worth
    default syndrome_entertainment_worth = capitaltype_entertainment_worth
    default syndrome_military_worth = capitaltype_military_worth
    default syndrome_corruption_worth = capitaltype_corruption_worth
    default syndrome_tooltip = False
    default syndrome_siege = False
    default syndrome_martial = [
        "other_norda_gunner_heer2_profile",
        "panzer_47mmapx_profile"
        ]
    default syndrome_unlocktown = False
    default syndrome_company_img = [
        "company_penguinironworks",
        "company_lugobust",
        "company_magische"
        ]
    default syndrome_company_text = {
        company_penguinironworks_name: company_penguinironworks_description, 
        company_lugobust_name: company_lugobust_description, 
        company_magische_name: company_magische_description
        }
        
    default hafn_name = "Hafn, Dania"
    default hafn_size = size_capital
    default hafn_governor = "Christian"
    default hafn_governor_pic = "{image=side christian normal}"
    default hafn_command = command_one
    default hafn_management = management_three
    default hafn_influence = influence_three
    default hafn_population = int(renpy.random.uniform(1, 9) * population_small)
    default hafn_publicorder = 50
    default hafn_hostility = dania_hostility
    default hafn_allegiance = dania_allegiance
    default hafn_alignment = dania_alignment
    default hafn_farming_worth = capitaltype_farming_worth
    default hafn_mining_worth = capitaltype_mining_worth
    default hafn_industry_worth = capitaltype_industry_worth
    default hafn_trade_worth = capitaltype_trade_worth
    default hafn_entertainment_worth = capitaltype_entertainment_worth
    default hafn_military_worth = capitaltype_military_worth
    default hafn_corruption_worth = capitaltype_corruption_worth
    default hafn_tooltip = False
    default hafn_siege = False
    default hafn_martial = [
        "other_dania_gunner_heer2_profile"
        ]
    default hafn_unlocktown = False
    default hafn_company_img = [
        "company_penguinironworks",
        "company_petwelt",
        "company_axemann"
        ]
    default hafn_company_text = {
        company_penguinironworks_name: company_penguinironworks_description, 
        company_petwelt_name: company_petwelt_description, 
        company_axemann_name: company_axemann_description
        }
    
    default balstoge_name = "Balstoge, Polix"
    default balstoge_size = size_large
    default balstoge_governor = "Stachie"
    default balstoge_governor_pic = "{image=side stachie happy}"
    default balstoge_command = command_two
    default balstoge_management = management_one
    default balstoge_influence = influence_two
    default balstoge_population = int(renpy.random.uniform(1, 9) * population_large)
    default balstoge_publicorder = 10
    default balstoge_hostility = polix_hostility
    default balstoge_allegiance = polix_allegiance
    default balstoge_alignment = polix_alignment
    default balstoge_farming_worth = farmtype_farming_worth
    default balstoge_mining_worth = farmtype_mining_worth
    default balstoge_industry_worth = farmtype_industry_worth
    default balstoge_trade_worth = farmtype_trade_worth
    default balstoge_entertainment_worth = farmtype_entertainment_worth
    default balstoge_military_worth = farmtype_military_worth
    default balstoge_corruption_worth = farmtype_corruption_worth
    default balstoge_tooltip = False
    default balstoge_siege = False
    default balstoge_martial = [
        "other_polix_gunner_heer1_profile",
        "other_polix_cavalry_heer1_profile"
        ]
    default balstoge_unlocktown = False
    default balstoge_company_img = [
        "company_victorrubber",
        "company_freedomburger",
        "company_woodyslogging"
        ]
    default balstoge_company_text = {
        company_victorrubber_name: company_victorrubber_description, 
        company_freedomburger_name: company_freedomburger_description, 
        company_woodyslogging_name: company_woodyslogging_description
        }
    
    default varsaa_name = "Varsaa, Polix"
    default varsaa_size = size_capital
    default varsaa_governor = "Smigly"
    default varsaa_governor_pic = "{image=side smigly determined}"
    default varsaa_command = command_three
    default varsaa_management = management_three
    default varsaa_influence = influence_four
    default varsaa_population = int(renpy.random.uniform(1, 9) * population_capital)
    default varsaa_publicorder = -20
    default varsaa_hostility = polix_hostility
    default varsaa_allegiance = polix_allegiance
    default varsaa_alignment = polix_alignment
    default varsaa_farming_worth = capitaltype_farming_worth
    default varsaa_mining_worth = capitaltype_mining_worth
    default varsaa_industry_worth = capitaltype_industry_worth
    default varsaa_trade_worth = capitaltype_trade_worth
    default varsaa_entertainment_worth = capitaltype_entertainment_worth
    default varsaa_military_worth = capitaltype_military_worth
    default varsaa_corruption_worth = capitaltype_corruption_worth
    default varsaa_tooltip = False
    default varsaa_siege = False
    default varsaa_martial = [
        "commander_smigly_profile",
        "other_polix_gunner_heer1_profile",
        "other_polix_cavalry_heer1_profile",
        "panzer_tks_profile",
        "panzer_ursus_profile"
        ]
    default varsaa_unlocktown = False
    default varsaa_company_img = [
        "company_handlarz",
        "company_petwelt",
        "company_toothhurty"
        ]
    default varsaa_company_text = {
        company_handlarz_name: company_handlarz_description, 
        company_petwelt_name: company_petwelt_description, 
        company_toothhurty_name: company_toothhurty_description
        }
    
    default lutetia_name = "Lutetia, Franzo"
    default lutetia_size = size_capital
    default lutetia_governor = "Leynaud"
    default lutetia_governor_pic = "{image=side reynaud normal}"
    default lutetia_command = command_one
    default lutetia_management = management_two
    default lutetia_influence = influence_three
    default lutetia_population = int(renpy.random.uniform(1, 9) * population_capital)
    default lutetia_publicorder = 100
    default lutetia_hostility = franzo_hostility
    default lutetia_allegiance = franzo_allegiance
    default lutetia_alignment = franzo_alignment
    default lutetia_farming_worth = capitaltype_farming_worth
    default lutetia_mining_worth = capitaltype_mining_worth
    default lutetia_industry_worth = capitaltype_industry_worth
    default lutetia_trade_worth = capitaltype_trade_worth
    default lutetia_entertainment_worth = capitaltype_entertainment_worth
    default lutetia_military_worth = capitaltype_military_worth
    default lutetia_corruption_worth = capitaltype_corruption_worth
    default lutetia_tooltip = False
    default lutetia_siege = False
    default lutetia_martial = [
        "other_franzo_gunner_heer3_profile",
        "panzer_charfcm_profile",
        "panzer_renaultr3540_profile",
        "panzer_charb1_profile",
        "airsupport_snotfire_profile"
        ]
    default lutetia_unlocktown = False
    default lutetia_company_img = [
        "company_caveavin",
        "company_panpanpan",
        "company_petwelt"
        ]
    default lutetia_company_text = {
        company_caveavin_name: company_caveavin_description, 
        company_panpanpan_name: company_panpanpan_description, 
        company_petwelt_name: company_petwelt_description
        }
    
    default nanzig_name = "Nanzig, Franzo"
    default nanzig_size = size_small
    default nanzig_governor = "Billotte"
    default nanzig_governor_pic = "{image=side billotte normal}"
    default nanzig_command = command_four
    default nanzig_management = management_two
    default nanzig_influence = influence_two
    default nanzig_population = int(renpy.random.uniform(1, 9) * population_small)
    default nanzig_publicorder = 70
    default nanzig_hostility = franzo_hostility
    default nanzig_allegiance = franzo_allegiance
    default nanzig_alignment = franzo_alignment
    default nanzig_farming_worth = minetype_farming_worth
    default nanzig_mining_worth = minetype_mining_worth
    default nanzig_industry_worth = minetype_industry_worth
    default nanzig_trade_worth = minetype_trade_worth
    default nanzig_entertainment_worth = minetype_entertainment_worth
    default nanzig_military_worth = minetype_military_worth
    default nanzig_corruption_worth = minetype_corruption_worth
    default nanzig_tooltip = False
    default nanzig_siege = False
    default nanzig_martial = [
        "other_franzo_gunner_heer3_profile",
        "other_franzo_gunner_heer3_profile"
        ]
    default nanzig_unlocktown = False
    default nanzig_company_img = [
        "company_zippilen",
        "company_axemann",
        "company_caveavin"
        ]
    default nanzig_company_text = {
        company_zippilen_name: company_zippilen_description, 
        company_axemann_name: company_axemann_description, 
        company_caveavin_name: company_caveavin_description
        }
    
    default vichei_name = "Vichei, Franzo"
    default vichei_size = size_small
    default vichei_governor = "Petain"
    default vichei_governor_pic = "{image=side billotte normal}"
    default vichei_command = command_one
    default vichei_management = management_one
    default vichei_influence = influence_five
    default vichei_population = int(renpy.random.uniform(1, 9) * population_small)
    default vichei_publicorder = -230
    default vichei_hostility = hostility_friendly
    default vichei_allegiance = allegiance_axle
    default vichei_alignment = vicheifranzo_empire
    default vichei_farming_worth = farmtype_farming_worth
    default vichei_mining_worth = farmtype_mining_worth
    default vichei_industry_worth = farmtype_industry_worth
    default vichei_trade_worth = farmtype_trade_worth
    default vichei_entertainment_worth = farmtype_entertainment_worth
    default vichei_military_worth = farmtype_military_worth
    default vichei_corruption_worth = farmtype_corruption_worth
    default vichei_tooltip = False
    default vichei_siege = False
    default vichei_martial = [
        "other_franzo_gunner_heer3_profile",
        "other_franzo_gunner_heer3_profile",
        "panzer_renaultr3540_profile"
        ]
    default vichei_unlocktown = False
    default vichei_company_img = [
        "company_magische",
        "company_woodyslogging",
        "company_panpanpan"
        ]
    default vichei_company_text = {
        company_magische_name: company_magische_description, 
        company_woodyslogging_name: company_woodyslogging_description, 
        company_panpanpan_name: company_panpanpan_description
        }
    
    default ruin_name = "Ruin, Franzo"
    default ruin_size = size_large
    default ruin_governor = "Darlan"
    default ruin_governor_pic = "{image=side oriasiangeneral normal}"
    default ruin_command = command_three
    default ruin_management = management_four
    default ruin_influence = influence_one
    default ruin_population = int(renpy.random.uniform(1, 9) * population_large)
    default ruin_publicorder = 90
    default ruin_hostility = franzo_hostility
    default ruin_allegiance = franzo_allegiance
    default ruin_alignment = franzo_alignment
    default ruin_farming_worth = tradetype_farming_worth
    default ruin_mining_worth = tradetype_mining_worth
    default ruin_industry_worth = tradetype_industry_worth
    default ruin_trade_worth = tradetype_trade_worth
    default ruin_entertainment_worth = tradetype_entertainment_worth
    default ruin_military_worth = tradetype_military_worth
    default ruin_corruption_worth = tradetype_corruption_worth
    default ruin_tooltip = False
    default ruin_siege = False
    default ruin_martial = [
        "other_franzo_gunner_heer3_profile"
        ]
    default ruin_unlocktown = False
    default ruin_company_img = [
        "company_panpanpan",
        "company_caveavin",
        "company_lugobust"
        ]
    default ruin_company_text = {
        company_panpanpan_name: company_panpanpan_description, 
        company_caveavin_name: company_caveavin_description, 
        company_lugobust_name: company_lugobust_description
        }
        
    default palmaa_name = "Palmaa, West Afrikaa"
    default palmaa_size = size_large
    default palmaa_governor = "Boisson"
    default palmaa_governor_pic = "{image=side politician normal}"
    default palmaa_command = command_two
    default palmaa_management = management_four
    default palmaa_influence = influence_three
    default palmaa_population = int(renpy.random.uniform(1, 9) * population_large)
    default palmaa_publicorder = 40
    default palmaa_hostility = westafrikaa_hostility
    default palmaa_allegiance = westafrikaa_allegiance
    default palmaa_alignment = vicheifranzo_empire
    default palmaa_farming_worth = tradetype_farming_worth
    default palmaa_mining_worth = tradetype_mining_worth
    default palmaa_industry_worth = tradetype_industry_worth
    default palmaa_trade_worth = tradetype_trade_worth
    default palmaa_entertainment_worth = tradetype_entertainment_worth
    default palmaa_military_worth = tradetype_military_worth
    default palmaa_corruption_worth = tradetype_corruption_worth
    default palmaa_tooltip = False
    default palmaa_siege = False
    default palmaa_martial = [
        "other_franzo_gunner_heer3_profile",
        "panzer_renaultft_profile"
        ]
    default palmaa_unlocktown = False
    default palmaa_company_img = [
        "company_panpanpan",
        "company_southernmining",
        "company_toothhurty"
        ]
    default palmaa_company_text = {
        company_panpanpan_name: company_panpanpan_description, 
        company_southernmining_name: company_southernmining_description, 
        company_toothhurty_name: company_toothhurty_description
        }
    
    default freeville_name = "Freeville, Franzo Gonko"
    default freeville_size = size_small
    default freeville_governor = "Boisson"
    default freeville_governor_pic = "{image=side politician normal}"
    default freeville_command = command_two
    default freeville_management = management_four
    default freeville_influence = influence_three
    default freeville_population = int(renpy.random.uniform(1, 9) * population_small)
    default freeville_publicorder = 30
    default freeville_hostility = franzogonko_hostility
    default freeville_allegiance = franzogonko_allegiance
    default freeville_alignment = vicheifranzo_empire
    default freeville_farming_worth = minetype_farming_worth
    default freeville_mining_worth = minetype_mining_worth
    default freeville_industry_worth = minetype_industry_worth
    default freeville_trade_worth = minetype_trade_worth
    default freeville_entertainment_worth = minetype_entertainment_worth
    default freeville_military_worth = minetype_military_worth
    default freeville_corruption_worth = minetype_corruption_worth
    default freeville_tooltip = False
    default freeville_siege = False
    default freeville_martial = [
        "other_franzo_gunner_heer3_profile",
        "other_franzo_gunner_heer3_profile"
        ]
    default freeville_unlocktown = False
    default freeville_company_img = [
        "company_southernmining",
        "company_caveavin",
        "company_freedomburger"
        ]
    default freeville_company_text = {
        company_southernmining_name: company_southernmining_description, 
        company_caveavin_name: company_caveavin_description, 
        company_freedomburger_name: company_freedomburger_description
        }
        
    default damasca_name = "Damasca, Assyria"
    default damasca_size = size_large
    default damasca_governor = "Weygand"
    default damasca_governor_pic = "{image=side weygand normal}"
    default damasca_command = command_three
    default damasca_management = management_one
    default damasca_influence = influence_four
    default damasca_population = int(renpy.random.uniform(1, 9) * population_large)
    default damasca_publicorder = 100
    default damasca_hostility = assyria_hostility
    default damasca_allegiance = assyria_allegiance
    default damasca_alignment = assyria_alignment
    default damasca_farming_worth = farmtype_farming_worth
    default damasca_mining_worth = farmtype_mining_worth
    default damasca_industry_worth = farmtype_industry_worth
    default damasca_trade_worth = farmtype_trade_worth
    default damasca_entertainment_worth = farmtype_entertainment_worth
    default damasca_military_worth = farmtype_military_worth
    default damasca_corruption_worth = farmtype_corruption_worth
    default damasca_tooltip = False
    default damasca_siege = False
    default damasca_martial = [
        "infantry_franzo_gunner_heer4_profile",
        "panzer_renaultft_profile"
        ]
    default damasca_unlocktown = False
    default damasca_company_img = [
        "company_southernmining",
        "company_panpanpan",
        "company_guptatours"
        ]
    default damasca_company_text = {
        company_southernmining_name: company_southernmining_description, 
        company_panpanpan_name: company_panpanpan_description, 
        company_guptatours_name: company_guptatours_description
        }
    
    default rome_name = "Rhome, Vitalia"
    default rome_size = size_capital
    default rome_governor = "Mussorinni"
    default rome_governor_pic = "{image=side rinni hat determined}"
    default rome_command = command_four
    default rome_management = management_three
    default rome_influence = influence_five
    default rome_population = int(renpy.random.uniform(1, 9) * population_capital)
    default rome_publicorder = 100
    default rome_hostility = vitalia_hostility
    default rome_allegiance = vitalia_allegiance
    default rome_alignment = vitalia_alignment
    default rome_farming_worth = capitaltype_farming_worth
    default rome_mining_worth = capitaltype_mining_worth
    default rome_industry_worth = capitaltype_industry_worth
    default rome_trade_worth = capitaltype_trade_worth
    default rome_entertainment_worth = capitaltype_entertainment_worth
    default rome_military_worth = capitaltype_military_worth
    default rome_corruption_worth = capitaltype_corruption_worth
    default rome_tooltip = False
    default rome_siege = False
    default rome_martial = [
        "commander_rinni_profile",
        "specialgroup_vitalia_gunner_heer3_profile",
        "specialgroup_vitalia_gunner_heer3_profile",
        "specialgroup_vitalia_gunner_heer3_profile",
        "specialgroup_vitalia_marksman_heer3_profile",
        "panzer_carroarmato_profile"
        ]
    default rome_unlocktown = False
    default rome_company_img = [
        "company_ducepasta",
        "company_pizzahaus",
        "company_caveavin"
        ]
    default rome_company_text = {
        company_ducepasta_name: company_ducepasta_description, 
        company_pizzahaus_name: company_pizzahaus_description, 
        company_caveavin_name: company_caveavin_description
        }
        
    default benghatza_name = "Benghatza, Cyracana"
    default benghatza_size = size_large
    default benghatza_governor = "Balbo"
    default benghatza_governor_pic = "{image=side desertgeneral normal}"
    default benghatza_command = command_one
    default benghatza_management = management_two
    default benghatza_influence = influence_two
    default benghatza_population = int(renpy.random.uniform(1, 9) * population_large)
    default benghatza_publicorder = 80
    default benghatza_hostility = cyracana_hostility
    default benghatza_allegiance = cyracana_allegiance
    default benghatza_alignment = cyracana_alignment
    default benghatza_farming_worth = minetype_farming_worth
    default benghatza_mining_worth = minetype_mining_worth
    default benghatza_industry_worth = minetype_industry_worth
    default benghatza_trade_worth = minetype_trade_worth
    default benghatza_entertainment_worth = minetype_entertainment_worth
    default benghatza_military_worth = minetype_military_worth
    default benghatza_corruption_worth = minetype_corruption_worth
    default benghatza_tooltip = False
    default benghatza_siege = False
    default benghatza_martial = [
        "specialgroup_vitalia_gunner_heer3_profile",
        "panzer_l335_profile"
        ]
    default benghatza_unlocktown = False
    default benghatza_company_img = [
        "company_southernmining",
        "company_ducepasta",
        "company_tanfa"
        ]
    default benghatza_company_text = {
        company_southernmining_name: company_southernmining_description, 
        company_ducepasta_name: company_ducepasta_description, 
        company_tanfa_name: company_tanfa_description
        }
        
    default bulaggna_name = "Bulaggna, Vitalia"
    default bulaggna_size = size_large
    default bulaggna_governor = "Badoglio"
    default bulaggna_governor_pic = "{image=side badoglio hat determined}"
    default bulaggna_command = command_four
    default bulaggna_management = management_four
    default bulaggna_influence = influence_three
    default bulaggna_population = int(renpy.random.uniform(1, 9) * population_large)
    default bulaggna_publicorder = 20
    default bulaggna_hostility = vitalia_hostility
    default bulaggna_allegiance = vitalia_allegiance
    default bulaggna_alignment = vitalia_alignment
    default bulaggna_farming_worth = farmtype_farming_worth
    default bulaggna_mining_worth = farmtype_mining_worth
    default bulaggna_industry_worth = farmtype_industry_worth
    default bulaggna_trade_worth = farmtype_trade_worth
    default bulaggna_entertainment_worth = farmtype_entertainment_worth
    default bulaggna_military_worth = farmtype_military_worth
    default bulaggna_corruption_worth = farmtype_corruption_worth
    default bulaggna_tooltip = False
    default bulaggna_siege = False
    default bulaggna_martial = [
        "specialgroup_vitalia_gunner_heer3_profile",
        "specialgroup_vitalia_gunner_heer3_profile",
        "specialgroup_vitalia_gunner_heer3_profile",
        "panzer_l335_profile"
        ]
    default bulaggna_unlocktown = False
    default bulaggna_company_img = [
        "company_ducepasta",
        "company_woodyslogging",
        "company_freedomburger"
        ]
    default bulaggna_company_text = {
        company_ducepasta_name: company_ducepasta_description, 
        company_woodyslogging_name: company_woodyslogging_description, 
        company_freedomburger_name: company_freedomburger_description
        }
        
    default torino_name = "Torino, Cilly"
    default torino_size = size_small
    default torino_governor = "Guzzoni"
    default torino_governor_pic = "{image=side soldier normal}"
    default torino_command = command_two
    default torino_management = management_two
    default torino_influence = influence_one
    default torino_population = int(renpy.random.uniform(1, 9) * population_small)
    default torino_publicorder = -10
    default torino_hostility = cilly_hostility
    default torino_allegiance = cilly_allegiance
    default torino_alignment = cilly_alignment
    default torino_farming_worth = minetype_farming_worth
    default torino_mining_worth = minetype_mining_worth
    default torino_industry_worth = minetype_industry_worth
    default torino_trade_worth = minetype_trade_worth
    default torino_entertainment_worth = minetype_entertainment_worth
    default torino_military_worth = minetype_military_worth
    default torino_corruption_worth = minetype_corruption_worth
    default torino_tooltip = False
    default torino_siege = False
    default torino_martial = [
        "specialgroup_vitalia_gunner_heer3_profile",
        "specialgroup_vitalia_gunner_heer3_profile",
        "panzer_semovente_profile",
        "airsupport_freccia_profile"
        ]
    default torino_unlocktown = False
    default torino_company_img = [
        "company_panpanpan",
        "company_pizzahaus",
        "company_zippilen"
        ]
    default torino_company_text = {
        company_panpanpan_name: company_panpanpan_description, 
        company_pizzahaus_name: company_pizzahaus_description, 
        company_zippilen_name: company_zippilen_description
        }
    
    default salernum_name = "Salernum, Vitalia"
    default salernum_size = size_small
    default salernum_governor = "Cavallero"
    default salernum_governor_pic = "{image=side cavallero normal}"
    default salernum_command = command_three
    default salernum_management = management_one
    default salernum_influence = influence_three
    default salernum_population = int(renpy.random.uniform(1, 9) * population_small)
    default salernum_publicorder = 20
    default salernum_hostility = vitalia_hostility
    default salernum_allegiance = vitalia_allegiance
    default salernum_alignment = vitalia_alignment
    default salernum_farming_worth = minetype_farming_worth
    default salernum_mining_worth = minetype_mining_worth
    default salernum_industry_worth = minetype_industry_worth
    default salernum_trade_worth = minetype_trade_worth
    default salernum_entertainment_worth = minetype_entertainment_worth
    default salernum_military_worth = minetype_military_worth
    default salernum_corruption_worth = minetype_corruption_worth
    default salernum_tooltip = False
    default salernum_siege = False
    default salernum_martial = [
        "specialgroup_vitalia_gunner_heer3_profile",
        "airsupport_freccia_profile",
        "airsupport_freccia_profile"
        ]
    default salernum_unlocktown = False
    default salernum_company_img = [
        "company_lugobust",
        "company_ducepasta",
        "company_fuuhbarcakes"
        ]
    default salernum_company_text = {
        company_lugobust_name: company_lugobust_description, 
        company_ducepasta_name: company_ducepasta_description, 
        company_fuuhbarcakes_name: company_fuuhbarcakes_description
        }
    
    default koufra_name = "Goofra, Cyracana"
    default koufra_size = size_small
    default koufra_governor = "Gariboldi"
    default koufra_governor_pic = "{image=side gariboldi normal}"
    default koufra_command = command_one
    default koufra_management = management_two
    default koufra_influence = influence_one
    default koufra_population = int(renpy.random.uniform(1, 9) * population_small)
    default koufra_publicorder = 20
    default koufra_hostility = cyracana_hostility
    default koufra_allegiance = cyracana_allegiance
    default koufra_alignment = cyracana_alignment
    default koufra_farming_worth = tradetype_farming_worth
    default koufra_mining_worth = tradetype_mining_worth
    default koufra_industry_worth = tradetype_industry_worth
    default koufra_trade_worth = tradetype_trade_worth
    default koufra_entertainment_worth = tradetype_entertainment_worth
    default koufra_military_worth = tradetype_military_worth
    default koufra_corruption_worth = tradetype_corruption_worth
    default koufra_tooltip = False
    default koufra_siege = False
    default koufra_martial = [
        "specialgroup_vitalia_gunner_heer3_profile"
        ]
    default koufra_unlocktown = False
    default koufra_company_img = [
        "company_handlarz",
        "company_southernmining",
        "company_ducepasta"
        ]
    default koufra_company_text = {
        company_handlarz_name: company_handlarz_description, 
        company_southernmining_name: company_southernmining_description, 
        company_ducepasta_name: company_ducepasta_description
        }
        
    default tobrunsk_name = "Tobrunsk, Cyracana"
    default tobrunsk_size = size_large
    default tobrunsk_governor = "Graziani"
    default tobrunsk_governor_pic = "{image=side graziani determined}"
    default tobrunsk_command = command_three
    default tobrunsk_management = management_three
    default tobrunsk_influence = influence_three
    default tobrunsk_population = int(renpy.random.uniform(1, 9) * population_large)
    default tobrunsk_publicorder = 20
    default tobrunsk_hostility = cyracana_hostility
    default tobrunsk_allegiance = cyracana_allegiance
    default tobrunsk_alignment = cyracana_alignment
    default tobrunsk_farming_worth = tradetype_farming_worth
    default tobrunsk_mining_worth = tradetype_mining_worth
    default tobrunsk_industry_worth = tradetype_industry_worth
    default tobrunsk_trade_worth = tradetype_trade_worth
    default tobrunsk_entertainment_worth = tradetype_entertainment_worth
    default tobrunsk_military_worth = tradetype_military_worth
    default tobrunsk_corruption_worth = tradetype_corruption_worth
    default tobrunsk_tooltip = False
    default tobrunsk_siege = False
    default tobrunsk_martial = [
        "specialgroup_vitalia_gunner_heer3_profile",
        "airsupport_freccia_profile"
        ]
    default tobrunsk_unlocktown = False
    default tobrunsk_company_img = [
        "company_guptatours",
        "company_ghoulish",
        "company_pizzahaus"
        ]
    default tobrunsk_company_text = {
        company_guptatours_name: company_guptatours_description, 
        company_ghoulish_name: company_ghoulish_description, 
        company_pizzahaus_name: company_pizzahaus_description
        }
        
    default albion_name = "Albion, Britannia"
    default albion_size = size_capital
    default albion_governor = "Churchill"
    default albion_governor_pic = "{image=side churchill hat determined}"
    default albion_command = command_four
    default albion_management = management_five
    default albion_influence = influence_five
    default albion_population = int(renpy.random.uniform(1, 9) * population_capital)
    default albion_publicorder = 100
    default albion_hostility = britannia_hostility
    default albion_allegiance = britannia_allegiance
    default albion_alignment = britannia_alignment
    default albion_farming_worth = capitaltype_farming_worth
    default albion_mining_worth = capitaltype_mining_worth
    default albion_industry_worth = capitaltype_industry_worth
    default albion_trade_worth = capitaltype_trade_worth
    default albion_entertainment_worth = capitaltype_entertainment_worth
    default albion_military_worth = capitaltype_military_worth
    default albion_corruption_worth = capitaltype_corruption_worth
    default albion_tooltip = False
    default albion_siege = False
    default albion_martial = [
        "commander_churchill_profile",
        "other_britannia_gunner_heer3_profile",
        "other_britannia_gunner_heer3_profile",
        "panzer_churchill_profile",
        "panzer_matilda2_profile",
        "panzer_valentine_profile",
        "airsupport_snotfire_profile",
        "airsupport_fopfighter_profile",
        "airsupport_dambuster_profile"
        ]
    default albion_unlocktown = False
    default albion_company_img = [
        "company_albioncornexchange",
        "company_sakurawhale",
        "company_teaempire"
        ]
    default albion_company_text = {
        company_albioncornexchange_name: company_albioncornexchange_description, 
        company_sakurawhale_name: company_sakurawhale_description, 
        company_teaempire_name: company_teaempire_description
        }
        
    default dovertown_name = "Dovertown, Britannia"
    default dovertown_size = size_small
    default dovertown_governor = "Stuffy"
    default dovertown_governor_pic = "{image=side stuffy determined}"
    default dovertown_command = command_three
    default dovertown_management = management_three
    default dovertown_influence = influence_two
    default dovertown_population = int(renpy.random.uniform(1, 9) * population_small)
    default dovertown_publicorder = 70
    default dovertown_hostility = britannia_hostility
    default dovertown_allegiance = britannia_allegiance
    default dovertown_alignment = britannia_alignment
    default dovertown_farming_worth = farmtype_farming_worth
    default dovertown_mining_worth = farmtype_mining_worth
    default dovertown_industry_worth = farmtype_industry_worth
    default dovertown_trade_worth = farmtype_trade_worth
    default dovertown_entertainment_worth = farmtype_entertainment_worth
    default dovertown_military_worth = farmtype_military_worth
    default dovertown_corruption_worth = farmtype_corruption_worth
    default dovertown_tooltip = False
    default dovertown_siege = False
    default dovertown_martial = [
        "other_britannia_gunner_heer3_profile",
        "panzer_archer_profile",
        "airsupport_snotfire_profile",
        "airsupport_fopfighter_profile",
        "airsupport_dambuster_profile"
        ]
    default dovertown_unlocktown = False
    default dovertown_company_img = [
        "company_albioncornexchange",
        "company_dokuk",
        "company_axemann"
        ]
    default dovertown_company_text = {
        company_albioncornexchange_name: company_albioncornexchange_description, 
        company_dokuk_name: company_dokuk_description, 
        company_axemann_name: company_axemann_description
        }
    
    default castel_name = "Castel Gibrata, Gibrata"
    default castel_size = size_small
    default castel_governor = "Gort"
    default castel_governor_pic = "{image=side gort normal}"
    default castel_command = command_two
    default castel_management = management_two
    default castel_influence = influence_one
    default castel_population = int(renpy.random.uniform(1, 9) * population_small)
    default castel_publicorder = 40
    default castel_hostility = gibrata_hostility
    default castel_allegiance = gibrata_allegiance
    default castel_alignment = gibrata_alignment
    default castel_farming_worth = tradetype_farming_worth
    default castel_mining_worth = tradetype_mining_worth
    default castel_industry_worth = tradetype_industry_worth
    default castel_trade_worth = tradetype_trade_worth
    default castel_entertainment_worth = tradetype_entertainment_worth
    default castel_military_worth = tradetype_military_worth
    default castel_corruption_worth = tradetype_corruption_worth
    default castel_tooltip = False
    default castel_siege = False
    default castel_martial = [
        "infantry_britannia_gunner_heer6_profile",
        "infantry_britannia_gunner_heer6_profile",
        "infantry_britannia_frogman_heer5_profile",
        "panzer_bishopsph_profile",
        "airsupport_snotfire_profile"
        ]
    default castel_unlocktown = False
    default castel_company_img = [
        "company_panpanpan",
        "company_teaempire",
        "company_pizzahaus"
        ]
    default castel_company_text = {
        company_panpanpan_name: company_panpanpan_description, 
        company_teaempire_name: company_teaempire_description, 
        company_pizzahaus_name: company_pizzahaus_description
        }
    
    default kair_name = "Kair, Gypta"
    default kair_size = size_large
    default kair_governor = "Wavell"
    default kair_governor_pic = "{image=side wavell normal}"
    default kair_command = command_four
    default kair_management = management_three
    default kair_influence = influence_two
    default kair_population = int(renpy.random.uniform(1, 9) * population_large)
    default kair_publicorder = 30
    default kair_hostility = gypta_hostility
    default kair_allegiance = gypta_allegiance
    default kair_alignment = gypta_alignment
    default kair_farming_worth = farmtype_farming_worth
    default kair_mining_worth = farmtype_mining_worth
    default kair_industry_worth = farmtype_industry_worth
    default kair_trade_worth = farmtype_trade_worth
    default kair_entertainment_worth = farmtype_entertainment_worth
    default kair_military_worth = farmtype_military_worth
    default kair_corruption_worth = farmtype_corruption_worth
    default kair_tooltip = False
    default kair_siege = False
    default kair_martial = [
        "infantry_britannia_gunner_heer6_profile",
        "panzer_covenanter_profile",
        "panzer_crusader_profile",
        "airsupport_fopfighter_profile"
        ]
    default kair_unlocktown = False
    default kair_company_img = [
        "company_guptatours",
        "company_teaempire",
        "company_pizzahaus"
        ]
    default kair_company_text = {
        company_guptatours_name: company_guptatours_description, 
        company_teaempire_name: company_teaempire_description, 
        company_pizzahaus_name: company_pizzahaus_description
        }
        
    default burburra_name = "Burburra, Zomali"
    default burburra_size = size_large
    default burburra_governor = "Jumbo"
    default burburra_governor_pic = "{image=side jumbo normal}"
    default burburra_command = command_two
    default burburra_management = management_two
    default burburra_influence = influence_three
    default burburra_population = int(renpy.random.uniform(1, 9) * population_large)
    default burburra_publicorder = 60
    default burburra_hostility = zomali_hostility
    default burburra_allegiance = zomali_allegiance
    default burburra_alignment = zomali_alignment
    default burburra_farming_worth = tradetype_farming_worth
    default burburra_mining_worth = tradetype_mining_worth
    default burburra_industry_worth = tradetype_industry_worth
    default burburra_trade_worth = tradetype_trade_worth
    default burburra_entertainment_worth = tradetype_entertainment_worth
    default burburra_military_worth = tradetype_military_worth
    default burburra_corruption_worth = tradetype_corruption_worth
    default burburra_tooltip = False
    default burburra_siege = False
    default burburra_martial = [
        "panzer_crusader_profile",
        "panzer_crusader_profile"
        ]
    default burburra_unlocktown = False
    default burburra_company_img = [
        "company_guptatours",
        "company_freedomburger",
        "company_teaempire"
        ]
    default burburra_company_text = {
        company_guptatours_name: company_guptatours_description, 
        company_freedomburger_name: company_freedomburger_description, 
        company_teaempire_name: company_teaempire_description
        }
        
    default aelia_name = "Aelia, Palesta"
    default aelia_size = size_large
    default aelia_governor = "Jumbo"
    default aelia_governor_pic = "{image=side jumbo normal}"
    default aelia_command = command_two
    default aelia_management = management_two
    default aelia_influence = influence_three
    default aelia_population = int(renpy.random.uniform(1, 9) * population_large)
    default aelia_publicorder = 40
    default aelia_hostility = palesta_hostility
    default aelia_allegiance = palesta_allegiance
    default aelia_alignment = palesta_alignment
    default aelia_farming_worth = tradetype_farming_worth
    default aelia_mining_worth = tradetype_mining_worth
    default aelia_industry_worth = tradetype_industry_worth
    default aelia_trade_worth = tradetype_trade_worth
    default aelia_entertainment_worth = tradetype_entertainment_worth
    default aelia_military_worth = tradetype_military_worth
    default aelia_corruption_worth = tradetype_corruption_worth
    default aelia_tooltip = False
    default aelia_siege = False
    default aelia_martial = [
        "infantry_britannia_gunner_heer6_profile",
        "infantry_britannia_gunner_heer6_profile",
        "panzer_valentine_profile",
        "airsupport_snotfire_profile"
        ]
    default aelia_unlocktown = False
    default aelia_company_img = [
        "company_guptatours",
        "company_panpanpan",
        "company_caveavin"
        ]
    default aelia_company_text = {
        company_guptatours_name: company_guptatours_description, 
        company_panpanpan_name: company_panpanpan_description, 
        company_caveavin_name: company_caveavin_description
        }
        
    default eideann_name = "Eideann, Britannia"
    default eideann_size = size_large
    default eideann_governor = "Battenia"
    default eideann_governor_pic = "{image=side battenia normal}"
    default eideann_command = command_four
    default eideann_management = management_three
    default eideann_influence = influence_four
    default eideann_population = int(renpy.random.uniform(1, 9) * population_large)
    default eideann_publicorder = 100
    default eideann_hostility = britannia_hostility
    default eideann_allegiance = britannia_allegiance
    default eideann_alignment = britannia_alignment
    default eideann_farming_worth = minetype_farming_worth
    default eideann_mining_worth = minetype_mining_worth
    default eideann_industry_worth = minetype_industry_worth
    default eideann_trade_worth = minetype_trade_worth
    default eideann_entertainment_worth = minetype_entertainment_worth
    default eideann_military_worth = minetype_military_worth
    default eideann_corruption_worth = minetype_corruption_worth
    default eideann_tooltip = False
    default eideann_siege = False
    default eideann_martial = [
        "other_britannia_gunner_heer3_profile",
        "other_britannia_gunner_heer3_profile",
        "panzer_47mmapx_profile",
        "panzer_crusader_profile",
        "panzer_churchill_profile",
        "airsupport_snotfire_profile",
        "airsupport_fopfighter_profile"
        ]
    default eideann_unlocktown = False
    default eideann_company_img = [
        "company_albioncornexchange",
        "company_teaempire",
        "company_freedomburger"
        ]
    default eideann_company_text = {
        company_albioncornexchange_name: company_albioncornexchange_description, 
        company_teaempire_name: company_teaempire_description, 
        company_freedomburger_name: company_freedomburger_description
        }
        
    default vaghdad_name = "Vaghdad, Iraji"
    default vaghdad_size = size_small
    default vaghdad_governor = "Ilah"
    default vaghdad_governor_pic = "{image=side desertgeneral normal}"
    default vaghdad_command = command_two
    default vaghdad_management = management_one
    default vaghdad_influence = influence_one
    default vaghdad_population = int(renpy.random.uniform(1, 9) * population_small)
    default vaghdad_publicorder = 10
    default vaghdad_hostility = iraji_hostility
    default vaghdad_allegiance = iraji_allegiance
    default vaghdad_alignment = iraji_alignment
    default vaghdad_farming_worth = farmtype_farming_worth
    default vaghdad_mining_worth = farmtype_mining_worth
    default vaghdad_industry_worth = farmtype_industry_worth
    default vaghdad_trade_worth = farmtype_trade_worth
    default vaghdad_entertainment_worth = farmtype_entertainment_worth
    default vaghdad_military_worth = farmtype_military_worth
    default vaghdad_corruption_worth = farmtype_corruption_worth
    default vaghdad_tooltip = False
    default vaghdad_siege = False
    default vaghdad_martial = [
        "infantry_britannia_gunner_heer6_profile",
        "panzer_bishopsph_profile"
        ]
    default vaghdad_unlocktown = False
    default vaghdad_company_img = [
        "company_guptatours",
        "company_albioncornexchange",
        "company_handlarz"
        ]
    default vaghdad_company_text = {
        company_guptatours_name: company_guptatours_description, 
        company_albioncornexchange_name: company_albioncornexchange_description, 
        company_handlarz_name: company_handlarz_description
        }
        
    default altberlin_name = "Altberlin, Germania"
    default altberlin_size = size_capital
    default altberlin_governor = "Hitora"
    default altberlin_governor_pic = "{image=side hitora hat angry}"
    default altberlin_command = command_two
    default altberlin_management = management_three
    default altberlin_influence = influence_five
    default altberlin_hostility = germania_hostility
    default altberlin_allegiance = germania_allegiance
    default altberlin_alignment = germania_alignment
    default altberlin_population = int(renpy.random.uniform(1, 9) * population_capital)
    default altberlin_publicorder = 100
    default altberlin_farming_worth = capitaltype_farming_worth
    default altberlin_mining_worth = capitaltype_mining_worth
    default altberlin_industry_worth = capitaltype_industry_worth
    default altberlin_trade_worth = capitaltype_trade_worth
    default altberlin_entertainment_worth = capitaltype_entertainment_worth
    default altberlin_military_worth = capitaltype_military_worth
    default altberlin_corruption_worth = capitaltype_corruption_worth
    default altberlin_tooltip = False
    default altberlin_siege = False
    default altberlin_martial = [
        "commander_hitora_profile",
        "infantry_germania_gunner_heer1_profile",
        "infantry_germania_gunner_heer1_profile",
        "infantry_germania_antitank_heer1_profile",
        "panzer_panzer1_profile",
        "panzer_panzer2_profile",
        "panzer_panzer3_profile",
        "airsupport_shrike_profile"
        ]
    default altberlin_unlocktown = True
    default altberlin_company_img = [
        "company_fuuhbarcakes",
        "company_lugobust",
        "company_grupp"
        ]
    default altberlin_company_text = {
        company_fuuhbarcakes_name: company_fuuhbarcakes_description, 
        company_lugobust_name: company_lugobust_description, 
        company_grupp_name: company_grupp_description
        }
            
    default altendresden_name = "Altendresden, Germania"
    default altendresden_size = size_large
    default altendresden_governor = "Joebbels"
    default altendresden_governor_pic = "{image=side joebbels normal}"
    default altendresden_command = command_one
    default altendresden_management = management_five
    default altendresden_influence = influence_four
    default altendresden_population = int(renpy.random.uniform(1, 9) * population_large)
    default altendresden_publicorder = 90
    default altendresden_hostility = germania_hostility
    default altendresden_allegiance = germania_allegiance
    default altendresden_alignment = germania_alignment
    default altendresden_farming_worth = industrytype_farming_worth
    default altendresden_mining_worth = industrytype_mining_worth
    default altendresden_industry_worth = industrytype_industry_worth
    default altendresden_trade_worth = industrytype_trade_worth
    default altendresden_entertainment_worth = industrytype_entertainment_worth
    default altendresden_military_worth = industrytype_military_worth
    default altendresden_corruption_worth = industrytype_corruption_worth
    default altendresden_tooltip = False
    default altendresden_siege = False
    default altendresden_martial = [
        "infantry_germania_gunner_heer1_profile",
        "infantry_germania_gunner_heer1_profile",
        "antitank_pak36_profile",
        "panzer_panzer4_profile",
        "airsupport_shrike_profile",
        "airsupport_ironsides_profile"
        ]
    default altendresden_unlocktown = True
    default altendresden_company_img = [
        "company_grupp",
        "company_tanfa",
        "company_molkereiwagen"
        ]
    default altendresden_company_text = {
        company_grupp_name: company_grupp_description, 
        company_tanfa_name: company_tanfa_description, 
        company_molkereiwagen_name: company_molkereiwagen_description
        }
        
    default treva_name = "Treva, Germania"
    default treva_size = size_small
    default treva_governor = "Dunitz"
    default treva_governor_pic = "{image=side dunitz determined}"
    default treva_command = command_four
    default treva_management = management_three
    default treva_influence = influence_three
    default treva_population = int(renpy.random.uniform(1, 9) * population_small)
    default treva_publicorder = 60
    default treva_hostility = germania_hostility
    default treva_allegiance = germania_allegiance
    default treva_alignment = germania_alignment
    default treva_farming_worth = farmtype_farming_worth
    default treva_mining_worth = farmtype_mining_worth
    default treva_industry_worth = farmtype_industry_worth
    default treva_trade_worth = farmtype_trade_worth
    default treva_entertainment_worth = farmtype_entertainment_worth
    default treva_military_worth = farmtype_military_worth
    default treva_corruption_worth = farmtype_corruption_worth
    default treva_tooltip = False
    default treva_siege = False
    default treva_martial = [
        "infantry_germania_gunner_heer1_profile",
        "infantry_germania_gunner_heer1_profile",
        "antitank_jagdpanzer_profile",
        "antitank_jagdpanther_profile",
        "panzer_panzer2_profile",
        "airsupport_shrike_profile"
        ]
    default treva_unlocktown = True
    default treva_company_img = [
        "company_zippilen",
        "company_ottoflugzeugwerke",
        "company_petwelt"
        ]
    default treva_company_text = {
        company_zippilen_name: company_zippilen_description, 
        company_ottoflugzeugwerke_name: company_ottoflugzeugwerke_description, 
        company_petwelt_name: company_petwelt_description
        }
        
    default wien_name = "Wien, Osta"
    default wien_size = size_large
    default wien_governor = "Frick"
    default wien_governor_pic = "{image=side official normal}"
    default wien_command = " "
    default wien_management = management_five
    default wien_influence = influence_three
    default wien_population = int(renpy.random.uniform(1, 9) * population_large)
    default wien_publicorder = 90
    default wien_hostility = osta_hostility
    default wien_allegiance = osta_allegiance
    default wien_alignment = osta_alignment
    default wien_farming_worth = minetype_farming_worth
    default wien_mining_worth = minetype_mining_worth
    default wien_industry_worth = minetype_industry_worth
    default wien_trade_worth = minetype_trade_worth
    default wien_entertainment_worth = minetype_entertainment_worth
    default wien_military_worth = minetype_military_worth
    default wien_corruption_worth = minetype_corruption_worth
    default wien_tooltip = False
    default wien_siege = False
    default wien_martial = [
        "infantry_germania_gunner_heer1_profile",
        "infantry_germania_gunner_heer1_profile",
        "infantry_germania_gunner_heer1_profile"
        ]
    default wien_unlocktown = True
    default wien_company_img = [
        "company_zippilen",
        "company_sakurawhale",
        "company_dokuk"
        ]
    default wien_company_text = {
        company_zippilen_name: company_zippilen_description, 
        company_sakurawhale_name: company_sakurawhale_description, 
        company_dokuk_name: company_dokuk_description
        }
    
    default budast_name = "Budast, Hang"
    default budast_size = size_large
    default budast_governor = "Horthy"
    default budast_governor_pic = "{image=side horthy happy}"
    default budast_command = command_three
    default budast_management = management_four
    default budast_influence = influence_three
    default budast_population = int(renpy.random.uniform(1, 9) * population_large)
    default budast_publicorder = 50
    default budast_hostility = hang_hostility
    default budast_allegiance = hang_allegiance
    default budast_alignment = hang_alignment
    default budast_farming_worth = tradetype_farming_worth
    default budast_mining_worth = tradetype_mining_worth
    default budast_industry_worth = tradetype_industry_worth
    default budast_trade_worth = tradetype_trade_worth
    default budast_entertainment_worth = tradetype_entertainment_worth
    default budast_military_worth = tradetype_military_worth
    default budast_corruption_worth = tradetype_corruption_worth
    default budast_tooltip = False
    default budast_siege = False
    default budast_martial = [
        "infantry_germania_gunner_heer1_profile",
        "panzer_zrinyi_profile"
        ]
    default budast_unlocktown = False
    default budast_company_img = [
        "company_ghoulish",
        "company_tanfa",
        "company_pizzahaus"
        ]
    default budast_company_text = {
        company_ghoulish_name: company_ghoulish_description, 
        company_tanfa_name: company_tanfa_description, 
        company_pizzahaus_name: company_pizzahaus_description
        }
        
    default bratiburg_name = "Bratiburg, Czexa"
    default bratiburg_size = size_large
    default bratiburg_governor = "Diso"
    default bratiburg_governor_pic = im.Sepia("character/side/diso_th.png")
    default bratiburg_command = " "
    default bratiburg_management = management_one
    default bratiburg_influence = influence_two
    default bratiburg_population = int(renpy.random.uniform(1, 9) * population_large)
    default bratiburg_publicorder = -20
    default bratiburg_hostility = czexa_hostility
    default bratiburg_allegiance = czexa_allegiance
    default bratiburg_alignment = czexa_alignment
    default bratiburg_farming_worth = farmtype_farming_worth
    default bratiburg_mining_worth = farmtype_mining_worth
    default bratiburg_industry_worth = farmtype_industry_worth
    default bratiburg_trade_worth = farmtype_trade_worth
    default bratiburg_entertainment_worth = farmtype_entertainment_worth
    default bratiburg_military_worth = farmtype_military_worth
    default bratiburg_corruption_worth = farmtype_corruption_worth
    default bratiburg_tooltip = False
    default bratiburg_siege = False
    default bratiburg_martial = [
        "infantry_germania_gunner_heer1_profile",
        "infantry_germania_gunner_heer1_profile",
        "panzer_panzer38t_profile"
        ]
    default bratiburg_unlocktown = True
    default bratiburg_company_img = [
        "company_pizzahaus",
        "company_magische",
        "company_dokuk"
        ]
    default bratiburg_company_text = {
        company_pizzahaus_name: company_pizzahaus_description, 
        company_magische_name: company_magische_description, 
        company_dokuk_name: company_dokuk_description
        }
        
    default konig_name = "Konig, Borussia"
    default konig_size = size_small
    default konig_governor = "Goring"
    default konig_governor_pic = "{image=side goring happy}"
    default konig_command = command_four
    default konig_management = management_two
    default konig_influence = influence_four
    default konig_population = int(renpy.random.uniform(1, 9) * population_small)
    default konig_publicorder = 20
    default konig_hostility = borussia_hostility
    default konig_allegiance = borussia_allegiance
    default konig_alignment = borussia_alignment
    default konig_farming_worth = industrytype_farming_worth
    default konig_mining_worth = industrytype_mining_worth
    default konig_industry_worth = industrytype_industry_worth
    default konig_trade_worth = industrytype_trade_worth
    default konig_entertainment_worth = industrytype_entertainment_worth
    default konig_military_worth = industrytype_military_worth
    default konig_corruption_worth = industrytype_corruption_worth
    default konig_tooltip = False
    default konig_siege = False
    default konig_martial = [
        "infantry_germania_gunner_heer1_profile",
        "infantry_germania_gunner_heer1_profile",
        "panzer_panzer4_profile",
        "airsupport_shrike_profile",
        "airsupport_shrike_profile",
        "airsupport_ironsides_profile",
        "airsupport_griffin_profile"
        ]
    default konig_unlocktown = True
    default konig_company_img = [
        "company_grupp",
        "company_lugobust",
        "company_fuuhbarcakes"
        ]
    default konig_company_text = {
        company_grupp_name: company_grupp_description, 
        company_lugobust_name: company_lugobust_description, 
        company_fuuhbarcakes_name: company_fuuhbarcakes_description
        }
    
    default moskva_name = "Moskva, Sovia Major"
    default moskva_size = size_capital
    default moskva_governor = "Starin"
    default moskva_governor_pic = "{image=side starin hat insane}"
    default moskva_command = command_five
    default moskva_management = management_four
    default moskva_influence = influence_five
    default moskva_population = int(renpy.random.uniform(1, 9) * population_capital)
    default moskva_publicorder = 100
    default moskva_hostility = soviamajor_hostility
    default moskva_allegiance = soviamajor_allegiance
    default moskva_alignment = soviamajor_alignment
    default moskva_farming_worth = capitaltype_farming_worth
    default moskva_mining_worth = capitaltype_mining_worth
    default moskva_industry_worth = capitaltype_industry_worth
    default moskva_trade_worth = capitaltype_trade_worth
    default moskva_entertainment_worth = capitaltype_entertainment_worth
    default moskva_military_worth = capitaltype_military_worth
    default moskva_corruption_worth = capitaltype_corruption_worth
    default moskva_tooltip = False
    default moskva_siege = False
    default moskva_martial = [
        "commander_starin_profile",
        "infantry_sovia_gunner_heer7_profile",
        "infantry_sovia_gunner_heer7_profile",
        "infantry_sovia_gunner_heer7_profile",
        "infantry_sovia_marksman_heer7_profile",
        "panzer_t34_profile",
        "panzer_t35_profile",
        "panzer_is2_profile"
        ]
    default moskva_unlocktown = False
    default moskva_company_img = [
        "company_motherofnationspelts",
        "company_iorginaicecream",
        "company_sovianpotato"
        ]
    default moskva_company_text = {
        company_motherofnationspelts_name: company_motherofnationspelts_description, 
        company_iorginaicecream_name: company_iorginaicecream_description, 
        company_sovianpotato_name: company_sovianpotato_description
        }
    
    default kharkova_name = "Kharkova, Sovia Minor"
    default kharkova_size = size_large
    default kharkova_governor = "Zhukky"
    default kharkova_governor_pic = "{image=side zhukky hat determined}"
    default kharkova_command = command_five
    default kharkova_management = management_four
    default kharkova_influence = influence_three
    default kharkova_population = int(renpy.random.uniform(1, 9) * population_large)
    default kharkova_publicorder = 90
    default kharkova_hostility = soviaminor_hostility
    default kharkova_allegiance = soviaminor_allegiance
    default kharkova_alignment = soviaminor_alignment
    default kharkova_farming_worth = industrytype_farming_worth
    default kharkova_mining_worth = industrytype_mining_worth
    default kharkova_industry_worth = industrytype_industry_worth
    default kharkova_trade_worth = industrytype_trade_worth
    default kharkova_entertainment_worth = industrytype_entertainment_worth
    default kharkova_military_worth = industrytype_military_worth
    default kharkova_corruption_worth = industrytype_corruption_worth
    default kharkova_tooltip = False
    default kharkova_siege = False
    default kharkova_martial = [
        "commander_zhukky_profile",
        "infantry_sovia_gunner_heer7_profile",
        "infantry_sovia_gunner_heer7_profile",
        "panzer_kv1_profile",
        "panzer_kv2_profile",
        "airsupport_yakovlev_profile",
        "airsupport_petlyakov_profile"
        ]
    default kharkova_unlocktown = False
    default kharkova_company_img = [
        "company_victorrubber",
        "company_sovianpotato",
        "company_axemann"
        ]
    default kharkova_company_text = {
        company_victorrubber_name: company_victorrubber_description, 
        company_sovianpotato_name: company_sovianpotato_description, 
        company_axemann_name: company_axemann_description
        }
    
    default minx_name = "Minx, Sovia Minor"
    default minx_size = size_small
    default minx_governor = "Konev"
    default minx_governor_pic = "{image=side soviangeneral normal}"
    default minx_command = command_three
    default minx_management = management_two
    default minx_influence = influence_two
    default minx_population = int(renpy.random.uniform(1, 9) * population_small)
    default minx_publicorder = 50
    default minx_hostility = soviaminor_hostility
    default minx_allegiance = soviaminor_allegiance
    default minx_alignment = soviaminor_alignment
    default minx_farming_worth = minetype_farming_worth
    default minx_mining_worth = minetype_mining_worth
    default minx_industry_worth = minetype_industry_worth
    default minx_trade_worth = minetype_trade_worth
    default minx_entertainment_worth = minetype_entertainment_worth
    default minx_military_worth = minetype_military_worth
    default minx_corruption_worth = minetype_corruption_worth
    default minx_tooltip = False
    default minx_siege = False
    default minx_martial = [
        "infantry_sovia_gunner_heer7_profile",
        "infantry_sovia_gunner_heer7_profile",
        "panzer_ba10_profile",
        "panzer_t34_profile",
        "panzer_kv2_profile",
        "airsupport_yakovlev_profile"
        ]
    default minx_unlocktown = False
    default minx_company_img = [
        "company_iorginaicecream",
        "company_victorrubber",
        "company_motherofnationspelts"
        ]
    default minx_company_text = {
        company_iorginaicecream_name: company_iorginaicecream_description, 
        company_victorrubber_name: company_victorrubber_description, 
        company_motherofnationspelts_name: company_motherofnationspelts_description
        }
        
    default reningrada_name = "Reningrada, Sovia Minor"
    default reningrada_size = size_large
    default reningrada_governor = "Govorov"
    default reningrada_governor_pic = "{image=side sovian normal}"
    default reningrada_command = command_one
    default reningrada_management = management_three
    default reningrada_influence = influence_three
    default reningrada_population = int(renpy.random.uniform(1, 9) * population_large)
    default reningrada_publicorder = 40
    default reningrada_hostility = soviaminor_hostility
    default reningrada_allegiance = soviaminor_allegiance
    default reningrada_alignment = soviaminor_alignment
    default reningrada_farming_worth = tradetype_farming_worth
    default reningrada_mining_worth = tradetype_mining_worth
    default reningrada_industry_worth = tradetype_industry_worth
    default reningrada_trade_worth = tradetype_trade_worth
    default reningrada_entertainment_worth = tradetype_entertainment_worth
    default reningrada_military_worth = tradetype_military_worth
    default reningrada_corruption_worth = tradetype_corruption_worth
    default reningrada_tooltip = False
    default reningrada_siege = False
    default reningrada_martial = [
        "infantry_sovia_gunner_heer7_profile",
        "infantry_sovia_marksman_heer7_profile",
        "panzer_t34_profile",
        "airsupport_yakovlev_profile"
        ]
    default reningrada_unlocktown = False
    default reningrada_company_img = [
        "company_ghoulish",
        "company_sovianpotato",
        "company_iorginaicecream"
        ]
    default reningrada_company_text = {
        company_ghoulish_name: company_ghoulish_description, 
        company_sovianpotato_name: company_sovianpotato_description, 
        company_iorginaicecream_name: company_iorginaicecream_description
        }
        
    default staringrada_name = "Staringrada, Sovia Minor"
    default staringrada_size = size_large
    default staringrada_governor = "Vasile"
    default staringrada_governor_pic = "{image=side vasile normal}"
    default staringrada_command = command_two
    default staringrada_management = management_three
    default staringrada_influence = influence_three
    default staringrada_population = int(renpy.random.uniform(1, 9) * population_large)
    default staringrada_publicorder = 50
    default staringrada_hostility = soviaminor_hostility
    default staringrada_allegiance = soviaminor_allegiance
    default staringrada_alignment = soviaminor_alignment
    default staringrada_farming_worth = industrytype_farming_worth
    default staringrada_mining_worth = industrytype_mining_worth
    default staringrada_industry_worth = industrytype_industry_worth
    default staringrada_trade_worth = industrytype_trade_worth
    default staringrada_entertainment_worth = industrytype_entertainment_worth
    default staringrada_military_worth = industrytype_military_worth 
    default staringrada_corruption_worth = industrytype_corruption_worth
    default staringrada_tooltip = False
    default staringrada_siege = False
    default staringrada_martial = [
        "infantry_sovia_gunner_heer7_profile",
        "infantry_sovia_gunner_heer7_profile",
        "panzer_su100_profile",
        "airsupport_yakovlev_profile"
        ]
    default staringrada_unlocktown = False
    default staringrada_company_img = [
        "company_iorginaicecream",
        "company_victorrubber",
        "company_motherofnationspelts"
        ]
    default staringrada_company_text = {
        company_iorginaicecream_name: company_iorginaicecream_description, 
        company_victorrubber_name: company_victorrubber_description, 
        company_motherofnationspelts_name: company_motherofnationspelts_description
        }
        
    default smolenx_name = "Smolenx, Sovia Minor"
    default smolenx_size = size_small
    default smolenx_governor = "Dimashenka"
    default smolenx_governor_pic = "{image=side dimashenka normal}"
    default smolenx_command = command_three
    default smolenx_management = management_one
    default smolenx_influence = influence_three
    default smolenx_population = int(renpy.random.uniform(1, 9) * population_small)
    default smolenx_publicorder = 50
    default smolenx_hostility = soviaminor_hostility
    default smolenx_allegiance = soviaminor_allegiance
    default smolenx_alignment = soviaminor_alignment
    default smolenx_farming_worth = farmtype_farming_worth
    default smolenx_mining_worth = farmtype_mining_worth
    default smolenx_industry_worth = farmtype_industry_worth
    default smolenx_trade_worth = farmtype_trade_worth
    default smolenx_entertainment_worth = farmtype_entertainment_worth
    default smolenx_military_worth = farmtype_military_worth 
    default smolenx_corruption_worth = farmtype_corruption_worth
    default smolenx_tooltip = False
    default smolenx_siege = False
    default smolenx_martial = [
        "infantry_sovia_gunner_heer7_profile",
        "infantry_sovia_gunner_heer7_profile",
        "infantry_sovia_gunner_heer7_profile",
        "infantry_sovia_gunner_heer7_profile",
        "airsupport_yakovlev_profile"
        ]
    default smolenx_unlocktown = False
    default smolenx_company_img = [
        "company_petwelt",
        "company_axemann",
        "company_sovianpotato"
        ]
    default smolenx_company_text = {
        company_petwelt_name: company_petwelt_description, 
        company_axemann_name: company_axemann_description, 
        company_sovianpotato_name: company_sovianpotato_description
        }
    
    default khiava_name = "Khiava, Sovia Minor"
    default khiava_size = size_small
    default khiava_governor = "Molotov"
    default khiava_governor_pic = "{image=side molotov normal}"
    default khiava_command = command_two
    default khiava_management = management_one
    default khiava_influence = influence_one
    default khiava_population = int(renpy.random.uniform(1, 9) * population_small)
    default khiava_publicorder = -10
    default khiava_hostility = soviaminor_hostility
    default khiava_allegiance = soviaminor_allegiance
    default khiava_alignment = soviaminor_alignment
    default khiava_farming_worth = farmtype_farming_worth
    default khiava_mining_worth = farmtype_mining_worth
    default khiava_industry_worth = farmtype_industry_worth
    default khiava_trade_worth = farmtype_trade_worth
    default khiava_entertainment_worth = farmtype_entertainment_worth
    default khiava_military_worth = farmtype_military_worth 
    default khiava_corruption_worth = farmtype_corruption_worth
    default khiava_tooltip = False
    default khiava_siege = False
    default khiava_martial = [
            "infantry_sovia_gunner_heer7_profile",
            "panzer_kv1_profile",
            "panzer_t35_profile",
            "airsupport_yakovlev_profile",
            "airsupport_yakovlev_profile"
            ]
    default khiava_unlocktown = False
    default khiava_company_img = [
            "company_sovianpotato",
            "company_ghoulish",
            "company_iorginaicecream"
            ]
    default khiava_company_text = {
            company_sovianpotato_name: company_sovianpotato_description, 
            company_ghoulish_name: company_ghoulish_description, 
            company_iorginaicecream_name: company_iorginaicecream_description
            }
    
    default economic_areas = {
        "gui/map/icon_farming.png": "Farming",
        "gui/map/icon_mining.png": "Mining",
        "gui/map/icon_industry.png": "Industry",
        "gui/map/icon_trade.png": "Trade",
        "gui/map/icon_military.png": "Military",
        "gui/map/icon_entertainment.png": "Entertainment",
        "gui/map/icon_corruption.png": "Corruption",
    }
        
    default active_mapwonders_items = {
        "pyramid": [wonder_name_giza,  wonder_location_giza, wonder_description_giza, wonder_condition_giza, wonder_icon_giza, wonder_image_giza, .78, .89],
        "villa": [wonder_name_villa,  wonder_location_villa, wonder_description_villa, wonder_condition_villa, wonder_icon_villa, wonder_image_villa, .46, .56],
        "imperium": [wonder_name_imperium,  wonder_location_imperium, wonder_description_imperium, wonder_condition_imperium, wonder_icon_imperium, wonder_image_imperium, .44, .42],
        "eiffel": [wonder_name_eiffel,  wonder_location_eiffel, wonder_description_eiffel, wonder_condition_eiffel, wonder_icon_eiffel, wonder_image_eiffel, .19, .425],
        "bigben": [wonder_name_bigben,  wonder_location_bigben, wonder_description_bigben, wonder_condition_bigben, wonder_icon_bigben, wonder_image_bigben, .15, .175],
        "kremlin": [wonder_name_kremlin,  wonder_location_kremlin, wonder_description_kremlin, wonder_condition_kremlin, wonder_icon_kremlin, wonder_image_kremlin, .865, .16]
    }
        
    default active_maptown_items = {
        "altberlin": [
            altberlin_name,
            altberlin_size,                                         
            altberlin_governor, 
            altberlin_governor_pic, 
            altberlin_hostility, 
            altberlin_alignment, 
            altberlin_population, 
            altberlin_publicorder, 
            altberlin_influence,
            altberlin_command,
            altberlin_management, 
            altberlin_farming_worth,
            altberlin_mining_worth,
            altberlin_industry_worth,
            altberlin_trade_worth,
            altberlin_entertainment_worth,
            altberlin_military_worth,
            altberlin_corruption_worth,
            altberlin_unlocktown, 
            altberlin_martial, 
            altberlin_siege,
            altberlin_company_img,
            altberlin_company_text,
            .505,
            .35
        ],
        "taiga": [
            taiga_name,
            taiga_size, 
            taiga_governor, 
            taiga_governor_pic, 
            taiga_hostility, 
            taiga_alignment, 
            taiga_population, 
            taiga_publicorder, 
            taiga_influence,
            taiga_command,
            taiga_management, 
            taiga_farming_worth,
            taiga_mining_worth,
            taiga_industry_worth,
            taiga_trade_worth,
            taiga_entertainment_worth,
            taiga_military_worth,
            taiga_corruption_worth,
            taiga_unlocktown, 
            taiga_martial, 
            taiga_siege,
            taiga_company_img,
            taiga_company_text,
            .3,
            .46
        ],
        "athenia": [
            athenia_name,
            athenia_size, 
            athenia_governor, 
            athenia_governor_pic, 
            athenia_hostility, 
            athenia_alignment, 
            athenia_population, 
            athenia_publicorder, 
            athenia_influence,
            athenia_command,
            athenia_management, 
            athenia_farming_worth,
            athenia_mining_worth,
            athenia_industry_worth,
            athenia_trade_worth,
            athenia_entertainment_worth,
            athenia_military_worth,
            athenia_corruption_worth,
            athenia_unlocktown, 
            athenia_martial, 
            athenia_siege,
            athenia_company_img,
            athenia_company_text,
            .633,
            .62
        ],
        "iraklion": [
            iraklion_name,
            iraklion_size, 
            iraklion_governor, 
            iraklion_governor_pic, 
            iraklion_hostility, 
            iraklion_alignment, 
            iraklion_population, 
            iraklion_publicorder, 
            iraklion_influence,
            iraklion_command,
            iraklion_management, 
            iraklion_farming_worth,
            iraklion_mining_worth,
            iraklion_industry_worth,
            iraklion_trade_worth,
            iraklion_entertainment_worth,
            iraklion_military_worth,
            iraklion_corruption_worth,
            iraklion_unlocktown, 
            iraklion_martial, 
            iraklion_siege,
            iraklion_company_img,
            iraklion_company_text,
            .645,
            .67
        ],
        "zaarkrauten": [
            zaarkrauten_name,
            zaarkrauten_size, 
            zaarkrauten_governor, 
            zaarkrauten_governor_pic, 
            zaarkrauten_hostility, 
            zaarkrauten_alignment, 
            zaarkrauten_population, 
            zaarkrauten_publicorder, 
            zaarkrauten_influence,
            zaarkrauten_command,
            zaarkrauten_management, 
            zaarkrauten_farming_worth,
            zaarkrauten_mining_worth,
            zaarkrauten_industry_worth,
            zaarkrauten_trade_worth,
            zaarkrauten_entertainment_worth,
            zaarkrauten_military_worth,
            zaarkrauten_corruption_worth,
            zaarkrauten_unlocktown, 
            zaarkrauten_martial, 
            zaarkrauten_siege,
            zaarkrauten_company_img,
            zaarkrauten_company_text,
            .39,
            .42
        ],
        "singidun": [
            singidun_name,
            singidun_size, 
            singidun_governor, 
            singidun_governor_pic, 
            singidun_hostility, 
            singidun_alignment, 
            singidun_population, 
            singidun_publicorder, 
            singidun_influence,
            singidun_command,
            singidun_management, 
            singidun_farming_worth,
            singidun_mining_worth,
            singidun_industry_worth,
            singidun_trade_worth,
            singidun_entertainment_worth,
            singidun_military_worth,
            singidun_corruption_worth,
            singidun_unlocktown, 
            singidun_martial, 
            singidun_siege,
            singidun_company_img,
            singidun_company_text,
            .62,
            .5
        ],
        "ancyra": [
            ancyra_name,
            ancyra_size, 
            ancyra_governor, 
            ancyra_governor_pic, 
            ancyra_hostility, 
            ancyra_alignment, 
            ancyra_population, 
            ancyra_publicorder, 
            ancyra_influence,
            ancyra_command,
            ancyra_management, 
            ancyra_farming_worth,
            ancyra_mining_worth,
            ancyra_industry_worth,
            ancyra_trade_worth,
            ancyra_entertainment_worth,
            ancyra_military_worth,
            ancyra_corruption_worth,
            ancyra_unlocktown, 
            ancyra_martial, 
            ancyra_siege,
            ancyra_company_img,
            ancyra_company_text,
            .8,
            .52
        ],
        "zuri": [
            zuri_name,
            zuri_size, 
            zuri_governor, 
            zuri_governor_pic, 
            zuri_hostility, 
            zuri_alignment, 
            zuri_population, 
            zuri_publicorder, 
            zuri_influence,
            zuri_command,
            zuri_management, 
            zuri_farming_worth,
            zuri_mining_worth,
            zuri_industry_worth,
            zuri_trade_worth,
            zuri_entertainment_worth,
            zuri_military_worth,
            zuri_corruption_worth,
            zuri_unlocktown, 
            zuri_martial, 
            zuri_siege,
            zuri_company_img,
            zuri_company_text,
            .36,
            .5
        ],
        "serdica": [
            serdica_name,
            serdica_size, 
            serdica_governor, 
            serdica_governor_pic, 
            serdica_hostility, 
            serdica_alignment, 
            serdica_population, 
            serdica_publicorder, 
            serdica_influence,
            serdica_command,
            serdica_management, 
            serdica_farming_worth,
            serdica_mining_worth,
            serdica_industry_worth,
            serdica_trade_worth,
            serdica_entertainment_worth,
            serdica_military_worth,
            serdica_corruption_worth,
            serdica_unlocktown, 
            serdica_martial, 
            serdica_siege,
            serdica_company_img,
            serdica_company_text,
            .67,
            .495
        ],
        "spruit": [
            spruit_name,
            spruit_size, 
            spruit_governor, 
            spruit_governor_pic, 
            spruit_hostility, 
            spruit_alignment, 
            spruit_population, 
            spruit_publicorder, 
            spruit_influence,
            spruit_command,
            spruit_management, 
            spruit_farming_worth,
            spruit_mining_worth,
            spruit_industry_worth,
            spruit_trade_worth,
            spruit_entertainment_worth,
            spruit_military_worth,
            spruit_corruption_worth,
            spruit_unlocktown, 
            spruit_martial, 
            spruit_siege,
            spruit_company_img,
            spruit_company_text,
            .33,
            .385
        ],
        "mayra": [
            mayra_name,
            mayra_size, 
            mayra_governor, 
            mayra_governor_pic, 
            mayra_hostility, 
            mayra_alignment, 
            mayra_population, 
            mayra_publicorder, 
            mayra_influence,
            mayra_command,
            mayra_management, 
            mayra_farming_worth,
            mayra_mining_worth,
            mayra_industry_worth,
            mayra_trade_worth,
            mayra_entertainment_worth,
            mayra_military_worth,
            mayra_corruption_worth,
            mayra_unlocktown, 
            mayra_martial, 
            mayra_siege,
            mayra_company_img,
            mayra_company_text,
            .14,
            .56
        ],
        "amstel": [
            amstel_name,
            amstel_size, 
            amstel_governor, 
            amstel_governor_pic, 
            amstel_hostility, 
            amstel_alignment, 
            amstel_population, 
            amstel_publicorder, 
            amstel_influence,
            amstel_command,
            amstel_management, 
            amstel_farming_worth,
            amstel_mining_worth,
            amstel_industry_worth,
            amstel_trade_worth,
            amstel_entertainment_worth,
            amstel_military_worth,
            amstel_corruption_worth,
            amstel_unlocktown, 
            amstel_martial, 
            amstel_siege,
            amstel_company_img,
            amstel_company_text,
            .3,
            .28
        ],
        "altendresden": [
            altendresden_name,
            altendresden_size, 
            altendresden_governor, 
            altendresden_governor_pic, 
            altendresden_hostility, 
            altendresden_alignment, 
            altendresden_population, 
            altendresden_publicorder, 
            altendresden_influence,
            altendresden_command,
            altendresden_management, 
            altendresden_farming_worth,
            altendresden_mining_worth,
            altendresden_industry_worth,
            altendresden_trade_worth,
            altendresden_entertainment_worth,
            altendresden_military_worth,
            altendresden_corruption_worth,
            altendresden_unlocktown, 
            altendresden_martial, 
            altendresden_siege,
            altendresden_company_img,
            altendresden_company_text,
            .48,
            .4
        ],
        "rotte": [
            rotte_name,
            rotte_size, 
            rotte_governor, 
            rotte_governor_pic, 
            rotte_hostility, 
            rotte_alignment, 
            rotte_population, 
            rotte_publicorder, 
            rotte_influence,
            rotte_command,
            rotte_management, 
            rotte_farming_worth,
            rotte_mining_worth,
            rotte_industry_worth,
            rotte_trade_worth,
            rotte_entertainment_worth,
            rotte_military_worth,
            rotte_corruption_worth,
            rotte_unlocktown, 
            rotte_martial, 
            rotte_siege,
            rotte_company_img,
            rotte_company_text,
            .32,
            .33
        ],
        "bucharex": [
            bucharex_name,
            bucharex_size, 
            bucharex_governor, 
            bucharex_governor_pic, 
            bucharex_hostility, 
            bucharex_alignment, 
            bucharex_population, 
            bucharex_publicorder, 
            bucharex_influence,
            bucharex_command,
            bucharex_management, 
            bucharex_farming_worth,
            bucharex_mining_worth,
            bucharex_industry_worth,
            bucharex_trade_worth,
            bucharex_entertainment_worth,
            bucharex_military_worth,
            bucharex_corruption_worth,
            bucharex_unlocktown, 
            bucharex_martial, 
            bucharex_siege,
            bucharex_company_img,
            bucharex_company_text,
            .7,
            .38
        ],
        "rija": [
            rija_name,
            rija_size, 
            rija_governor, 
            rija_governor_pic, 
            rija_hostility, 
            rija_alignment, 
            rija_population, 
            rija_publicorder, 
            rija_influence,
            rija_command,
            rija_management, 
            rija_farming_worth,
            rija_mining_worth,
            rija_industry_worth,
            rija_trade_worth,
            rija_entertainment_worth,
            rija_military_worth,
            rija_corruption_worth,
            rija_unlocktown, 
            rija_martial, 
            rija_siege,
            rija_company_img,
            rija_company_text,
            .635,
            .14
        ],        
        "helsin": [
            helsin_name,
            helsin_size, 
            helsin_governor, 
            helsin_governor_pic, 
            helsin_hostility, 
            helsin_alignment, 
            helsin_population, 
            helsin_publicorder, 
            helsin_influence,
            helsin_command,
            helsin_management, 
            helsin_farming_worth,
            helsin_mining_worth,
            helsin_industry_worth,
            helsin_trade_worth,
            helsin_entertainment_worth,
            helsin_military_worth,
            helsin_corruption_worth,
            helsin_unlocktown, 
            helsin_martial, 
            helsin_siege,
            helsin_company_img,
            helsin_company_text,
            .74,
            .05
        ],
        "oxloa": [
            oxloa_name,
            oxloa_size, 
            oxloa_governor, 
            oxloa_governor_pic, 
            oxloa_hostility, 
            oxloa_alignment, 
            oxloa_population, 
            oxloa_publicorder, 
            oxloa_influence,
            oxloa_command,
            oxloa_management, 
            oxloa_farming_worth,
            oxloa_mining_worth,
            oxloa_industry_worth,
            oxloa_trade_worth,
            oxloa_entertainment_worth,
            oxloa_military_worth,
            oxloa_corruption_worth,
            oxloa_unlocktown, 
            oxloa_martial, 
            oxloa_siege,
            oxloa_company_img,
            oxloa_company_text,
            .38,
            .1
        ],
        "syndrome": [
            syndrome_name,
            syndrome_size, 
            syndrome_governor, 
            syndrome_governor_pic, 
            syndrome_hostility, 
            syndrome_alignment, 
            syndrome_population, 
            syndrome_publicorder, 
            syndrome_influence,
            syndrome_command,
            syndrome_management, 
            syndrome_farming_worth,
            syndrome_mining_worth,
            syndrome_industry_worth,
            syndrome_trade_worth,
            syndrome_entertainment_worth,
            syndrome_military_worth,
            syndrome_corruption_worth,
            syndrome_unlocktown, 
            syndrome_martial, 
            syndrome_siege,
            syndrome_company_img,
            syndrome_company_text,
            .48,
            .025
        ],
        "hafn": [
            hafn_name,
            hafn_size, 
            hafn_governor, 
            hafn_governor_pic, 
            hafn_hostility, 
            hafn_alignment, 
            hafn_population, 
            hafn_publicorder, 
            hafn_influence,
            hafn_command,
            hafn_management, 
            hafn_farming_worth,
            hafn_mining_worth,
            hafn_industry_worth,
            hafn_trade_worth,
            hafn_entertainment_worth,
            hafn_military_worth,
            hafn_corruption_worth,
            hafn_unlocktown, 
            hafn_martial, 
            hafn_siege,
            hafn_company_img,
            hafn_company_text,
            .405,
            .245
        ],
        "balstoge": [
            balstoge_name,
            balstoge_size, 
            balstoge_governor, 
            balstoge_governor_pic, 
            balstoge_hostility, 
            balstoge_alignment, 
            balstoge_population, 
            balstoge_publicorder, 
            balstoge_influence,
            balstoge_command,
            balstoge_management, 
            balstoge_farming_worth,
            balstoge_mining_worth,
            balstoge_industry_worth,
            balstoge_trade_worth,
            balstoge_entertainment_worth,
            balstoge_military_worth,
            balstoge_corruption_worth,
            balstoge_unlocktown, 
            balstoge_martial, 
            balstoge_siege,
            balstoge_company_img,
            balstoge_company_text,
            .65,
            .26
        ],
        "varsaa": [
            varsaa_name,
            varsaa_size, 
            varsaa_governor, 
            varsaa_governor_pic, 
            varsaa_hostility, 
            varsaa_alignment, 
            varsaa_population, 
            varsaa_publicorder, 
            varsaa_influence,
            varsaa_command,
            varsaa_management, 
            varsaa_farming_worth,
            varsaa_mining_worth,
            varsaa_industry_worth,
            varsaa_trade_worth,
            varsaa_entertainment_worth,
            varsaa_military_worth,
            varsaa_corruption_worth,
            varsaa_unlocktown, 
            varsaa_martial, 
            varsaa_siege,
            varsaa_company_img,
            varsaa_company_text,
            .62,
            .36
        ],
        "lutetia": [
            lutetia_name,
            lutetia_size, 
            lutetia_governor, 
            lutetia_governor_pic, 
            lutetia_hostility, 
            lutetia_alignment, 
            lutetia_population, 
            lutetia_publicorder, 
            lutetia_influence,
            lutetia_command,
            lutetia_management, 
            lutetia_farming_worth,
            lutetia_mining_worth,
            lutetia_industry_worth,
            lutetia_trade_worth,
            lutetia_entertainment_worth,
            lutetia_military_worth,
            lutetia_corruption_worth,
            lutetia_unlocktown, 
            lutetia_martial, 
            lutetia_siege,
            lutetia_company_img,
            lutetia_company_text,
            .239,
            .43
        ],
        "nanzig": [
            nanzig_name,
            nanzig_size, 
            nanzig_governor, 
            nanzig_governor_pic, 
            nanzig_hostility, 
            nanzig_alignment, 
            nanzig_population, 
            nanzig_publicorder, 
            nanzig_influence,
            nanzig_command,
            nanzig_management, 
            nanzig_farming_worth,
            nanzig_mining_worth,
            nanzig_industry_worth,
            nanzig_trade_worth,
            nanzig_entertainment_worth,
            nanzig_military_worth,
            nanzig_corruption_worth,
            nanzig_unlocktown, 
            nanzig_martial, 
            nanzig_siege,
            nanzig_company_img,
            nanzig_company_text,
            .29,
            .41
        ],
        "vichei": [
            vichei_name,
            vichei_size, 
            vichei_governor, 
            vichei_governor_pic, 
            vichei_hostility, 
            vichei_alignment, 
            vichei_population, 
            vichei_publicorder, 
            vichei_influence,
            vichei_command,
            vichei_management, 
            vichei_farming_worth,
            vichei_mining_worth,
            vichei_industry_worth,
            vichei_trade_worth,
            vichei_entertainment_worth,
            vichei_military_worth,
            vichei_corruption_worth,
            vichei_unlocktown, 
            vichei_martial, 
            vichei_siege,
            vichei_company_img,
            vichei_company_text,
            .25,
            .51
        ],
        "ruin": [
            ruin_name,
            ruin_size, 
            ruin_governor, 
            ruin_governor_pic, 
            ruin_hostility, 
            ruin_alignment, 
            ruin_population, 
            ruin_publicorder, 
            ruin_influence,
            ruin_command,
            ruin_management, 
            ruin_farming_worth,
            ruin_mining_worth,
            ruin_industry_worth,
            ruin_trade_worth,
            ruin_entertainment_worth,
            ruin_military_worth,
            ruin_corruption_worth,
            ruin_unlocktown, 
            ruin_martial, 
            ruin_siege,
            ruin_company_img,
            ruin_company_text,
            .185,
            .4
        ],
        "palmaa": [
            palmaa_name,
            palmaa_size, 
            palmaa_governor, 
            palmaa_governor_pic, 
            palmaa_hostility, 
            palmaa_alignment, 
            palmaa_population, 
            palmaa_publicorder, 
            palmaa_influence,
            palmaa_command,
            palmaa_management, 
            palmaa_farming_worth,
            palmaa_mining_worth,
            palmaa_industry_worth,
            palmaa_trade_worth,
            palmaa_entertainment_worth,
            palmaa_military_worth,
            palmaa_corruption_worth,
            palmaa_unlocktown, 
            palmaa_martial, 
            palmaa_siege,
            palmaa_company_img,
            palmaa_company_text,
            .036,
            .82
        ],
        "freeville": [
            freeville_name,
            freeville_size, 
            freeville_governor, 
            freeville_governor_pic, 
            freeville_hostility, 
            freeville_alignment, 
            freeville_population, 
            freeville_publicorder, 
            freeville_influence,
            freeville_command,
            freeville_management, 
            freeville_farming_worth,
            freeville_mining_worth,
            freeville_industry_worth,
            freeville_trade_worth,
            freeville_entertainment_worth,
            freeville_military_worth,
            freeville_corruption_worth,
            freeville_unlocktown, 
            freeville_martial, 
            freeville_siege,
            freeville_company_img,
            freeville_company_text,
            .21,
            .94
        ],
        "damasca": [
            damasca_name,
            damasca_size, 
            damasca_governor, 
            damasca_governor_pic, 
            damasca_hostility, 
            damasca_alignment, 
            damasca_population, 
            damasca_publicorder, 
            damasca_influence,
            damasca_command,
            damasca_management, 
            damasca_farming_worth,
            damasca_mining_worth,
            damasca_industry_worth,
            damasca_trade_worth,
            damasca_entertainment_worth,
            damasca_military_worth,
            damasca_corruption_worth,
            damasca_unlocktown, 
            damasca_martial, 
            damasca_siege,
            damasca_company_img,
            damasca_company_text,
            .89,
            .61
        ],
        "rome": [
            rome_name,
            rome_size, 
            rome_governor, 
            rome_governor_pic, 
            rome_hostility, 
            rome_alignment, 
            rome_population, 
            rome_publicorder, 
            rome_influence,
            rome_command,
            rome_management, 
            rome_farming_worth,
            rome_mining_worth,
            rome_industry_worth,
            rome_trade_worth,
            rome_entertainment_worth,
            rome_military_worth,
            rome_corruption_worth,
            rome_unlocktown, 
            rome_martial, 
            rome_siege,
            rome_company_img,
            rome_company_text,
            .42,
            .59
        ],
        "benghatza": [
            benghatza_name,
            benghatza_size, 
            benghatza_governor, 
            benghatza_governor_pic, 
            benghatza_hostility, 
            benghatza_alignment, 
            benghatza_population, 
            benghatza_publicorder, 
            benghatza_influence,
            benghatza_command,
            benghatza_management, 
            benghatza_farming_worth,
            benghatza_mining_worth,
            benghatza_industry_worth,
            benghatza_trade_worth,
            benghatza_entertainment_worth,
            benghatza_military_worth,
            benghatza_corruption_worth,
            benghatza_unlocktown, 
            benghatza_martial, 
            benghatza_siege,
            benghatza_company_img,
            benghatza_company_text,
            .61,
            .82
        ],
        "bulaggna": [
            bulaggna_name,
            bulaggna_size, 
            bulaggna_governor, 
            bulaggna_governor_pic, 
            bulaggna_hostility, 
            bulaggna_alignment, 
            bulaggna_population, 
            bulaggna_publicorder, 
            bulaggna_influence,
            bulaggna_command,
            bulaggna_management, 
            bulaggna_farming_worth,
            bulaggna_mining_worth,
            bulaggna_industry_worth,
            bulaggna_trade_worth,
            bulaggna_entertainment_worth,
            bulaggna_military_worth,
            bulaggna_corruption_worth,
            bulaggna_unlocktown, 
            bulaggna_martial, 
            bulaggna_siege,
            bulaggna_company_img,
            bulaggna_company_text,
            .475,
            .64
        ],
        "torino": [
            torino_name,
            torino_size, 
            torino_governor, 
            torino_governor_pic, 
            torino_hostility, 
            torino_alignment, 
            torino_population, 
            torino_publicorder, 
            torino_influence,
            torino_command,
            torino_management, 
            torino_farming_worth,
            torino_mining_worth,
            torino_industry_worth,
            torino_trade_worth,
            torino_entertainment_worth,
            torino_military_worth,
            torino_corruption_worth,
            torino_unlocktown, 
            torino_martial, 
            torino_siege,
            torino_company_img,
            torino_company_text,
            .41,
            .71
        ],
        "salernum": [
            salernum_name,
            salernum_size, 
            salernum_governor, 
            salernum_governor_pic, 
            salernum_hostility, 
            salernum_alignment, 
            salernum_population, 
            salernum_publicorder, 
            salernum_influence,
            salernum_command,
            salernum_management, 
            salernum_farming_worth,
            salernum_mining_worth,
            salernum_industry_worth,
            salernum_trade_worth,
            salernum_entertainment_worth,
            salernum_military_worth,
            salernum_corruption_worth,
            salernum_unlocktown, 
            salernum_martial, 
            salernum_siege,
            salernum_company_img,
            salernum_company_text,
            .415,
            .66
        ],
        "koufra": [
            koufra_name,
            koufra_size, 
            koufra_governor, 
            koufra_governor_pic, 
            koufra_hostility, 
            koufra_alignment, 
            koufra_population, 
            koufra_publicorder, 
            koufra_influence,
            koufra_command,
            koufra_management, 
            koufra_farming_worth,
            koufra_mining_worth,
            koufra_industry_worth,
            koufra_trade_worth,
            koufra_entertainment_worth,
            koufra_military_worth,
            koufra_corruption_worth,
            koufra_unlocktown, 
            koufra_martial, 
            koufra_siege,
            koufra_company_img,
            koufra_company_text,
            .64,
            .905
        ],
        "tobrunsk": [
            tobrunsk_name,
            tobrunsk_size, 
            tobrunsk_governor, 
            tobrunsk_governor_pic, 
            tobrunsk_hostility, 
            tobrunsk_alignment, 
            tobrunsk_population, 
            tobrunsk_publicorder, 
            tobrunsk_influence,
            tobrunsk_command,
            tobrunsk_management, 
            tobrunsk_farming_worth,
            tobrunsk_mining_worth,
            tobrunsk_industry_worth,
            tobrunsk_trade_worth,
            tobrunsk_entertainment_worth,
            tobrunsk_military_worth,
            tobrunsk_corruption_worth,
            tobrunsk_unlocktown, 
            tobrunsk_martial, 
            tobrunsk_siege,
            tobrunsk_company_img,
            tobrunsk_company_text,
            .63,
            .775
        ],
        "albion": [
            albion_name,
            albion_size, 
            albion_governor, 
            albion_governor_pic, 
            albion_hostility, 
            albion_alignment, 
            albion_population, 
            albion_publicorder, 
            albion_influence,
            albion_command,
            albion_management, 
            albion_farming_worth,
            albion_mining_worth,
            albion_industry_worth,
            albion_trade_worth,
            albion_entertainment_worth,
            albion_military_worth,
            albion_corruption_worth,
            albion_unlocktown, 
            albion_martial, 
            albion_siege,
            albion_company_img,
            albion_company_text,
            .13,
            .27
        ],
        "dovertown": [
            dovertown_name,
            dovertown_size, 
            dovertown_governor, 
            dovertown_governor_pic, 
            dovertown_hostility, 
            dovertown_alignment, 
            dovertown_population, 
            dovertown_publicorder, 
            dovertown_influence,
            dovertown_command,
            dovertown_management, 
            dovertown_farming_worth,
            dovertown_mining_worth,
            dovertown_industry_worth,
            dovertown_trade_worth,
            dovertown_entertainment_worth,
            dovertown_military_worth,
            dovertown_corruption_worth,
            dovertown_unlocktown, 
            dovertown_martial, 
            dovertown_siege,
            dovertown_company_img,
            dovertown_company_text,
            .085,
            .34
        ],
        "castel": [
            castel_name,
            castel_size, 
            castel_governor, 
            castel_governor_pic, 
            castel_hostility, 
            castel_alignment, 
            castel_population, 
            castel_publicorder, 
            castel_influence,
            castel_command,
            castel_management, 
            castel_farming_worth,
            castel_mining_worth,
            castel_industry_worth,
            castel_trade_worth,
            castel_entertainment_worth,
            castel_military_worth,
            castel_corruption_worth,
            castel_unlocktown, 
            castel_martial, 
            castel_siege,
            castel_company_img,
            castel_company_text,
            .098,
            .65
        ],
        "kair": [
            kair_name,
            kair_size, 
            kair_governor, 
            kair_governor_pic, 
            kair_hostility, 
            kair_alignment, 
            kair_population, 
            kair_publicorder, 
            kair_influence,
            kair_command,
            kair_management, 
            kair_farming_worth,
            kair_mining_worth,
            kair_industry_worth,
            kair_trade_worth,
            kair_entertainment_worth,
            kair_military_worth,
            kair_corruption_worth,
            kair_unlocktown, 
            kair_martial, 
            kair_siege,
            kair_company_img,
            kair_company_text,
            .76,
            .81
        ],
        "burburra": [
            burburra_name,
            burburra_size, 
            burburra_governor, 
            burburra_governor_pic, 
            burburra_hostility, 
            burburra_alignment, 
            burburra_population, 
            burburra_publicorder, 
            burburra_influence,
            burburra_command,
            burburra_management, 
            burburra_farming_worth,
            burburra_mining_worth,
            burburra_industry_worth,
            burburra_trade_worth,
            burburra_entertainment_worth,
            burburra_military_worth,
            burburra_corruption_worth,
            burburra_unlocktown, 
            burburra_martial, 
            burburra_siege,
            burburra_company_img,
            burburra_company_text,
            .92,
            .965
        ],
        "aelia": [
            aelia_name,
            aelia_size, 
            aelia_governor, 
            aelia_governor_pic, 
            aelia_hostility, 
            aelia_alignment, 
            aelia_population, 
            aelia_publicorder, 
            aelia_influence,
            aelia_command,
            aelia_management, 
            aelia_farming_worth,
            aelia_mining_worth,
            aelia_industry_worth,
            aelia_trade_worth,
            aelia_entertainment_worth,
            aelia_military_worth,
            aelia_corruption_worth,
            aelia_unlocktown, 
            aelia_martial, 
            aelia_siege,
            aelia_company_img,
            aelia_company_text,
            .84,
            .68
        ],
        "eideann": [
            eideann_name,
            eideann_size, 
            eideann_governor, 
            eideann_governor_pic, 
            eideann_hostility, 
            eideann_alignment, 
            eideann_population, 
            eideann_publicorder, 
            eideann_influence,
            eideann_command,
            eideann_management, 
            eideann_farming_worth,
            eideann_mining_worth,
            eideann_industry_worth,
            eideann_trade_worth,
            eideann_entertainment_worth,
            eideann_military_worth,
            eideann_corruption_worth,
            eideann_unlocktown, 
            eideann_martial, 
            eideann_siege,
            eideann_company_img,
            eideann_company_text,
            .23,
            .19
        ],
        "vaghdad": [
            vaghdad_name,
            vaghdad_size, 
            vaghdad_governor, 
            vaghdad_governor_pic, 
            vaghdad_hostility, 
            vaghdad_alignment, 
            vaghdad_population, 
            vaghdad_publicorder, 
            vaghdad_influence,
            vaghdad_command,
            vaghdad_management, 
            vaghdad_farming_worth,
            vaghdad_mining_worth,
            vaghdad_industry_worth,
            vaghdad_trade_worth,
            vaghdad_entertainment_worth,
            vaghdad_military_worth,
            vaghdad_corruption_worth,
            vaghdad_unlocktown, 
            vaghdad_martial, 
            vaghdad_siege,
            vaghdad_company_img,
            vaghdad_company_text,
            .93,
            .79
        ],
        "treva": [
            treva_name,
            treva_size, 
            treva_governor, 
            treva_governor_pic, 
            treva_hostility, 
            treva_alignment, 
            treva_population, 
            treva_publicorder, 
            treva_influence,
            treva_command,
            treva_management, 
            treva_farming_worth,
            treva_mining_worth,
            treva_industry_worth,
            treva_trade_worth,
            treva_entertainment_worth,
            treva_military_worth,
            treva_corruption_worth,
            treva_unlocktown, 
            treva_martial, 
            treva_siege,
            treva_company_img,
            treva_company_text,
            .42,
            .33
        ],
        "wien": [
            wien_name,
            wien_size, 
            wien_governor, 
            wien_governor_pic, 
            wien_hostility, 
            wien_alignment, 
            wien_population, 
            wien_publicorder, 
            wien_influence,
            wien_command,
            wien_management, 
            wien_farming_worth,
            wien_mining_worth,
            wien_industry_worth,
            wien_trade_worth,
            wien_entertainment_worth,
            wien_military_worth,
            wien_corruption_worth,
            wien_unlocktown, 
            wien_martial, 
            wien_siege,
            wien_company_img,
            wien_company_text,
            .41,
            .47
        ],
        "budast": [
            budast_name,
            budast_size, 
            budast_governor, 
            budast_governor_pic, 
            budast_hostility, 
            budast_alignment, 
            budast_population, 
            budast_publicorder, 
            budast_influence,
            budast_command,
            budast_management, 
            budast_farming_worth,
            budast_mining_worth,
            budast_industry_worth,
            budast_trade_worth,
            budast_entertainment_worth,
            budast_military_worth,
            budast_corruption_worth,
            budast_unlocktown, 
            budast_martial, 
            budast_siege,
            budast_company_img,
            budast_company_text,
            .62,
            .45
        ],
        "bratiburg": [
            bratiburg_name,
            bratiburg_size, 
            bratiburg_governor, 
            bratiburg_governor_pic, 
            bratiburg_hostility, 
            bratiburg_alignment, 
            bratiburg_population, 
            bratiburg_publicorder, 
            bratiburg_influence,
            bratiburg_command,
            bratiburg_management, 
            bratiburg_farming_worth,
            bratiburg_mining_worth,
            bratiburg_industry_worth,
            bratiburg_trade_worth,
            bratiburg_entertainment_worth,
            bratiburg_military_worth,
            bratiburg_corruption_worth,
            bratiburg_unlocktown, 
            bratiburg_martial, 
            bratiburg_siege,
            bratiburg_company_img,
            bratiburg_company_text,
            .63,
            .42
        ],
        "konig": [
            konig_name,
            konig_size, 
            konig_governor, 
            konig_governor_pic, 
            konig_hostility, 
            konig_alignment, 
            konig_population, 
            konig_publicorder, 
            konig_influence,
            konig_command,
            konig_management, 
            konig_farming_worth,
            konig_mining_worth,
            konig_industry_worth,
            konig_trade_worth,
            konig_entertainment_worth,
            konig_military_worth,
            konig_corruption_worth,
            konig_unlocktown, 
            konig_martial, 
            konig_siege,
            konig_company_img,
            konig_company_text,
            .575,
            .23
        ],
        "moskva": [
            moskva_name,
            moskva_size, 
            moskva_governor, 
            moskva_governor_pic, 
            moskva_hostility, 
            moskva_alignment, 
            moskva_population, 
            moskva_publicorder, 
            moskva_influence,
            moskva_command,
            moskva_management, 
            moskva_farming_worth,
            moskva_mining_worth,
            moskva_industry_worth,
            moskva_trade_worth,
            moskva_entertainment_worth,
            moskva_military_worth,
            moskva_corruption_worth,
            moskva_unlocktown, 
            moskva_martial, 
            moskva_siege,
            moskva_company_img,
            moskva_company_text,
            .88,
            .21
        ],
        "kharkova": [
            kharkova_name,
            kharkova_size, 
            kharkova_governor, 
            kharkova_governor_pic, 
            kharkova_hostility, 
            kharkova_alignment, 
            kharkova_population, 
            kharkova_publicorder, 
            kharkova_influence,
            kharkova_command,
            kharkova_management, 
            kharkova_farming_worth,
            kharkova_mining_worth,
            kharkova_industry_worth,
            kharkova_trade_worth,
            kharkova_entertainment_worth,
            kharkova_military_worth,
            kharkova_corruption_worth,
            kharkova_unlocktown, 
            kharkova_martial, 
            kharkova_siege,
            kharkova_company_img,
            kharkova_company_text,
            .89,
            .33
        ],
        "minx": [
            minx_name,
            minx_size, 
            minx_governor, 
            minx_governor_pic, 
            minx_hostility, 
            minx_alignment, 
            minx_population, 
            minx_publicorder, 
            minx_influence,
            minx_command,
            minx_management, 
            minx_farming_worth,
            minx_mining_worth,
            minx_industry_worth,
            minx_trade_worth,
            minx_entertainment_worth,
            minx_military_worth,
            minx_corruption_worth,
            minx_unlocktown, 
            minx_martial, 
            minx_siege,
            minx_company_img,
            minx_company_text,
            .71,
            .27
        ],
        "reningrada": [
            reningrada_name,
            reningrada_size, 
            reningrada_governor, 
            reningrada_governor_pic, 
            reningrada_hostility, 
            reningrada_alignment, 
            reningrada_population, 
            reningrada_publicorder, 
            reningrada_influence,
            reningrada_command,
            reningrada_management, 
            reningrada_farming_worth,
            reningrada_mining_worth,
            reningrada_industry_worth,
            reningrada_trade_worth,
            reningrada_entertainment_worth,
            reningrada_military_worth,
            reningrada_corruption_worth,
            reningrada_unlocktown, 
            reningrada_martial, 
            reningrada_siege,
            reningrada_company_img,
            reningrada_company_text,
            .735,
            .12
        ],
        "staringrada": [
            staringrada_name,
            staringrada_size, 
            staringrada_governor, 
            staringrada_governor_pic, 
            staringrada_hostility, 
            staringrada_alignment, 
            staringrada_population, 
            staringrada_publicorder, 
            staringrada_influence,
            staringrada_command,
            staringrada_management, 
            staringrada_farming_worth,
            staringrada_mining_worth,
            staringrada_industry_worth,
            staringrada_trade_worth,
            staringrada_entertainment_worth,
            staringrada_military_worth,
            staringrada_corruption_worth,
            staringrada_unlocktown, 
            staringrada_martial, 
            staringrada_siege,
            staringrada_company_img,
            staringrada_company_text,
            .99,
            .32
        ],
        "smolenx": [
            smolenx_name,
            smolenx_size, 
            smolenx_governor, 
            smolenx_governor_pic, 
            smolenx_hostility, 
            smolenx_alignment, 
            smolenx_population, 
            smolenx_publicorder, 
            smolenx_influence,
            smolenx_command,
            smolenx_management, 
            smolenx_farming_worth,
            smolenx_mining_worth,
            smolenx_industry_worth,
            smolenx_trade_worth,
            smolenx_entertainment_worth,
            smolenx_military_worth,
            smolenx_corruption_worth,
            smolenx_unlocktown, 
            smolenx_martial, 
            smolenx_siege,
            smolenx_company_img,
            smolenx_company_text,
            .77,
            .23
        ],
        "khiava": [
            khiava_name,
            khiava_size, 
            khiava_governor, 
            khiava_governor_pic, 
            khiava_hostility, 
            khiava_alignment, 
            khiava_population, 
            khiava_publicorder, 
            khiava_influence,
            khiava_command,
            khiava_management, 
            khiava_farming_worth,
            khiava_mining_worth,
            khiava_industry_worth,
            khiava_trade_worth,
            khiava_entertainment_worth,
            khiava_military_worth,
            khiava_corruption_worth,
            khiava_unlocktown, 
            khiava_martial, 
            khiava_siege,
            khiava_company_img,
            khiava_company_text,
            .8,
            .31
        ]
    }
    
        
#############################################################################################
#############################################################################################
#############################################################################################

default active_divisions_grid_x = 7
default active_divisions_grid_y = int(len(active_divisions_items) / active_divisions_grid_x) + 1
default active_divisions_grid_num = active_divisions_grid_x * active_divisions_grid_y

default active_korps_grid_x = 7
default active_korps_grid_y = int(len(active_korps_items) / active_korps_grid_x) + 1
default active_korps_grid_num = active_korps_grid_x * active_korps_grid_y

default active_spezialformations_grid_x = 7
default active_spezialformations_grid_y = int(len(active_spezialformations_items) / active_spezialformations_grid_x) + 1
default active_spezialformations_grid_num = active_spezialformations_grid_x * active_spezialformations_grid_y

default active_armygroups_grid_x = 7
default active_armygroups_grid_y = int(len(active_armygroups_items) / active_armygroups_grid_x) + 1
default active_armygroups_grid_num = active_armygroups_grid_x * active_armygroups_grid_y

default active_armies_grid_x = 7
default active_armies_grid_y = int(len(active_armies_items) / active_armies_grid_x) + 1
default active_armies_grid_num = active_armies_grid_x * active_armies_grid_y

default active_innercircle_grid_x = 4
default active_innercircle_grid_y = int(len(active_innercircle_items) / active_innercircle_grid_x) + 1
default active_innercircle_grid_num = active_innercircle_grid_x * active_innercircle_grid_y

default active_militarycircle_grid_x = 4
default active_militarycircle_grid_y = int(len(active_militarycircle_items) / active_militarycircle_grid_x)
default active_militarycircle_grid_num = active_militarycircle_grid_x * active_militarycircle_grid_y

default active_fuuhbarmuseum_grid_x = 3
default active_fuuhbarmuseum_grid_y = int(len(active_fuuhbarmuseum_items) / active_fuuhbarmuseum_grid_x) + 1
default active_fuuhbarmuseum_grid_num = active_fuuhbarmuseum_grid_x * active_fuuhbarmuseum_grid_y

default active_allegiances_grid_x = 9
default active_allegiances_grid_y = int(len(active_allegiances_items) / active_allegiances_grid_x) + 1
default active_allegiances_grid_num = active_allegiances_grid_x * active_allegiances_grid_y

init -1 python:
    def command_update():
        global active_armygroups_grid_x
        global active_armygroups_grid_y
        global active_armygroups_grid_num
        global active_armygroups_items
        
        global active_armies_grid_x
        global active_armies_grid_y
        global active_armies_grid_num
        global active_armies_items
        
        global active_korps_grid_x
        global active_korps_grid_y
        global active_korps_grid_num
        global active_korps_items
        
        global active_divisions_grid_x
        global active_divisions_grid_y
        global active_divisions_grid_num
        global active_divisions_items
        
        global active_spezialformations_grid_x
        global active_spezialformations_grid_y
        global active_spezialformations_grid_num
        global active_spezialformations_items
        
        global active_innercircle_grid_x
        global active_innercircle_grid_y
        global active_innercircle_grid_num
        global active_innercircle_items
        
        if len(active_armygroups_items) % 7 == 0:
            active_armygroups_grid_y = int(len(active_armygroups_items) / active_armygroups_grid_x)
        else:
            active_armygroups_grid_y = int(len(active_armygroups_items) / active_armygroups_grid_x) + 1
            
        if len(active_armies_items) % 7 == 0:
            active_armies_grid_y = int(len(active_armies_items) / active_armies_grid_x)
        else:
            active_armies_grid_y = int(len(active_armies_items) / active_armies_grid_x) + 1
            
        if len(active_korps_items) % 7 == 0:
            active_korps_grid_y = int(len(active_korps_items) / active_korps_grid_x)
        else:
            active_korps_grid_y = int(len(active_korps_items) / active_korps_grid_x) + 1
            
        if len(active_divisions_items) % 7 == 0:
            active_divisions_grid_y = int(len(active_divisions_items) / active_divisions_grid_x)
        else:
            active_divisions_grid_y = int(len(active_divisions_items) / active_divisions_grid_x) + 1
            
        if len(active_spezialformations_items) % 7 == 0:
            active_spezialformations_grid_y = int(len(active_spezialformations_items) / active_spezialformations_grid_x)
        else:
            active_spezialformations_grid_y = int(len(active_spezialformations_items) / active_spezialformations_grid_x) + 1
            
        if len(active_innercircle_items) % 4 == 0:
            active_innercircle_grid_y = int(len(active_innercircle_items) / active_innercircle_grid_x)
        else:
            active_innercircle_grid_y = int(len(active_innercircle_items) / active_innercircle_grid_x) + 1
        
        active_armygroups_grid_num = active_armygroups_grid_x * active_armygroups_grid_y    
        active_armies_grid_num = active_armies_grid_x * active_armies_grid_y
        active_korps_grid_num = active_korps_grid_x * active_korps_grid_y
        active_divisions_grid_num = active_divisions_grid_x * active_divisions_grid_y
        active_spezialformations_grid_num = active_spezialformations_grid_x * active_spezialformations_grid_y
        active_innercircle_grid_num = active_innercircle_grid_x * active_innercircle_grid_y
            
    def museum_update():
        global active_fuuhbarmuseum_grid_x
        global active_fuuhbarmuseum_grid_y
        global active_fuuhbarmuseum_grid_num
        global active_fuuhbarmuseum_items
        
        if len(active_fuuhbarmuseum_items) % 3 == 0:
            active_fuuhbarmuseum_grid_y = int(len(active_fuuhbarmuseum_items) / active_fuuhbarmuseum_grid_x)
        else:
            active_fuuhbarmuseum_grid_y = int(len(active_fuuhbarmuseum_items) / active_fuuhbarmuseum_grid_x) + 1
            
        active_fuuhbarmuseum_grid_num = active_fuuhbarmuseum_grid_x * active_fuuhbarmuseum_grid_y
        
    def escape_skipvariables_update():
        config.keymap['skip'].append('K_LCTRL')
        config.keymap['skip'].append('K_RCTRL')
        config.keymap['hide_windows'].append('h')
        renpy.clear_keymap_cache()
        
    def escape_rollback():
        renpy.rollback(force=True, checkpoints=1)
        
    def silly_sounds_enabled():
        if silly_sounds:
            renpy.music.set_volume(1, delay=0, channel=u'silsound2')
            renpy.music.set_volume(1, delay=0, channel=u'silsound3')
            renpy.music.set_volume(1, delay=0, channel=u'silsound4')
            renpy.music.set_volume(1, delay=0, channel=u'silsound5')
            renpy.music.set_volume(1, delay=0, channel=u'silsound6')
            renpy.music.set_volume(1, delay=0, channel=u'silsound7')
            renpy.music.set_volume(1, delay=0, channel=u'silsound8')
        else:
            renpy.music.set_volume(0, delay=0, channel=u'silsound2')
            renpy.music.set_volume(0, delay=0, channel=u'silsound3')
            renpy.music.set_volume(0, delay=0, channel=u'silsound4')
            renpy.music.set_volume(0, delay=0, channel=u'silsound5')
            renpy.music.set_volume(0, delay=0, channel=u'silsound6')
            renpy.music.set_volume(0, delay=0, channel=u'silsound7')
            renpy.music.set_volume(0, delay=0, channel=u'silsound8')
        
    
#############################################################################################
#############################################################################################
#############################################################################################
