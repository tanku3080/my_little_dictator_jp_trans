
###################################

# MAP TRANSITION

label map_transition:
    return
    
###################################

# MAIN MISSION DEFAULT MAPS
# (Important for season changes and turns)

label map_begin:
    scene black
    window hide None
    play music ["music/map.ogg", "music/map2.ogg", "music/map3.ogg", "music/map4.ogg"]
    play sound6 "se/morse.ogg"
    $ store.text_history_enabled = False
    $ _rollback = False
    $ renpy.block_rollback()
    $ config.skipping = False
    call screen mapchoice1(mapdata) with pixellate

###################################
    
# SIDE MISSION DEFAULT MAPS
# (No season/turn changes, for returning after side missions)

label map_return:
    scene black
    window hide None
    play music ["music/map.ogg", "music/map2.ogg", "music/map3.ogg", "music/map4.ogg"]
    play sound6 "se/morse.ogg"
    $ store.text_history_enabled = False
    $ _rollback = False
    $ renpy.block_rollback()
    $ config.skipping = False
    call screen mapchoice1(mapdata) with pixellate
    
###################################

# GAMEOVER TRIGGER
        
label gameover_trigger:
    $ renpy.block_rollback()
    
    if breakpoint_lossokay_training:
        #"It's Okay To Lose Trigger - Training Battle."
        jump bat000001_aftermath
        
    elif breakpoint_lossokay_zhukky:
        #"It's Okay To Lose Trigger - Zhukky Battle."
        $ skip_battle_selected = True
        jump bat000005_aftermath    
        
    elif breakpoint_lossokay_churchill:
        #"It's Okay To Lose Trigger - Churchill First Battle."
        $ skip_battle_selected = True
        jump bat000015_aftermath
        
    elif breakpoint_lossokay_airtraining:
        #"It's Okay To Lose Trigger - Air Training Battle."
        jump bat000045_aftermath
        
    elif breakpoint_lossokay_monty:
        #"It's Okay To Lose Trigger - Monty Battle."
        $ skip_battle_selected = True
        jump bat000066_aftermath
        
    elif breakpoint_lossokay_nyan:
        #"It's Okay To Lose Trigger - Nyan Battle."
        $ skip_battle_selected = True
        jump bat0000103_aftermath    
        
    elif breakpoint_lossokay_prologue:
        #"It's Okay To Lose Trigger - Prologue Battle."
        jump bat000000_aftermath
        
    else:
        #"It's Not Okay To Lose Trigger - Any Other Battle."
        $ persistent.skip_battle_sensitive = True
        $ config.keymap['skip'].append('K_LCTRL')
        $ config.keymap['skip'].append('K_RCTRL')
        $ config.keymap['hide_windows'].append('h')
        $ renpy.clear_keymap_cache()
        
        scene black
        jump game_over
        
###################################
        
# GAMEOVER

label game_over:
    $ renpy.block_rollback()
    $ store.text_history_enabled = False
    $ _rollback = False
    $ config.skipping = False
    $ mouse_visible = False
    $_game_menu_screen = None
    $ renpy.pause(1.0, hard=True)
    play sound3 "se/gameover.ogg"
    call screen game_over_screen
    scene black
    $ renpy.pause(1.0, hard=True)
    $ mouse_visible = True
    $_game_menu_screen = "save_screen"
    return

screen game_over_screen():
    modal True
    add "gameover_anim"
    timer 5.0 action [Return(), With(pixellate)]
    
###################################


