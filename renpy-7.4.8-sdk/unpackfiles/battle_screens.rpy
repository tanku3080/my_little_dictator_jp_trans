screen battle_screen(bg, disc, dec_1=None, dec_2=None):
    on "show":
        action Show("get_ready")
    on "hide":
        action With(pixellate)
        
    tag battle_screen
    zorder 10
    
    key "K_ESCAPE" action [Play("mmsound", "se/researchui.ogg"), Show("escape_battle_prompt")]
    key "h" action NullAction()
    
    default path_ui = "battle/ui/"
    default second_label = "normal"
    default second_menu = None
    if level_choice == 1:
        default player_actions = [
            [ "Attack", SetScreenVariable("second_label", "attack") ],
            [ "Skills", SetScreenVariable("second_label", "medic") ],
            [ "Party", Show("battle_party_screen", mid_game=True) ],
            [ "Skip Battle", [Play("mmsound", "se/researchui.ogg"), SetVariable("skip_battle_prompt", True)] ]
        ]
    elif level_choice == 3:
        default player_actions = [
            [ "Attack", SetScreenVariable("second_label", "attack") ],
            [ "Skills", SetScreenVariable("second_label", "medic") ],
            [ "Party", Show("battle_party_screen", mid_game=True) ],
            [ "Skip Battle", [SensitiveIf(level_choice == 1), NullAction()] ]
        ]
    else:
        default player_actions = [
            [ "Attack", SetScreenVariable("second_label", "attack") ],
            [ "Skills", SetScreenVariable("second_label", "medic") ],
            [ "Party", Show("battle_party_screen", mid_game=True) ],
            [ "Skip Battle", [SensitiveIf(persistent.skip_battle_sensitive), Play("mmsound", "se/researchui.ogg"), SetVariable("skip_battle_prompt", True)] ]
        ]
    
    use battleground_back
    add disc xpos 3 ypos 490
    add disc xpos 950 ypos 170

    if dec_1:
        add dec_1[0] xpos dec_1[1] ypos dec_1[2]
    if dec_2:
        add dec_2[0] xpos dec_2[1] ypos dec_2[2]

    add "back/effects/storm_darkness.png"
    
    add game
    
    if second_label == "normal":
        add path_ui + "window.png" xalign 0.0 yalign 1.0
        if gui_text:
            text gui_text[0] style "battle_text" size 32 xmaximum 880 xpos 32 ypos 895

        if game.player_turn():
            grid 2 2:
                xpos 970
                ypos 870
                spacing 0

                for name, act in player_actions:
                    button:
                        xysize (472, 102)
                        idle_background path_ui + "attack_main_button_idle.png"
                        hover_background path_ui + "attack_main_button_hover.png"
                        insensitive_background "attack_main_button_insensitive"
                        hover_sound "se/hover.ogg"
                        activate_sound "se/click.ogg"
                        focus_mask True
                        text name xalign 0.5 yalign 0.69
                        action act
                        at nav_eff

    elif second_label == "attack" or second_label == "medic":
        add path_ui + "window_2.png" xalign 0.0 yalign 1.0

        if second_label == "attack":
            $ second_menu = game.player.attack_store
        else:
            $ second_menu = game.player.heal_store

        $ total = 0
        $ row = 1 if divmod(len(second_menu), 3)[0] == 0 else 2

        imagebutton:
            action SetScreenVariable("second_label", "normal")
            idle "yesno_no_idle"
            hover "yesno_no_hover"
            focus_mask True 
            hover_sound "se/hover.ogg" 
            activate_sound "se/click.ogg"
            xalign 0.988
            ypos 927

        grid 3 row:
            xpos 6
            ypos 871
            spacing 0
            for id, skill in second_menu.iteritems():
                fixed:
                    xysize (589, 101)
                    button:
                        xysize (429, 101)
                        idle_background path_ui + "attack_button_idle.png"
                        hover_background path_ui + "attack_button_hover.png"
                        insensitive_background "attack_button_insensitive"
                        hover_sound "se/hover.ogg"
                        activate_sound "se/click.ogg"
                        focus_mask True
                        text skill.name xalign 0.5 yalign 0.69 text_align 0.5
                        sensitive (skill.pp > 0)
                        if skill.base_hp < 0:
                            tooltip skill.desc + " {color=#FFC490}(Base DMG / " + str(int(abs(skill.base_hp * 1.3))) + "){/color}"
                        else:
                            tooltip skill.desc
                        action [ SetScreenVariable("second_label", "normal"), SetScreenVariable("second_menu", None), Function(game.chosen_skill, skill=skill) ]
                        
                    fixed:
                        xysize (156, 101)
                        xpos 433
                        ypos 5
                        vbox:
                            yalign 0.5
                            hbox:
                                vbox:
                                    xalign 1.0 yalign 1.0
                                    add return_skilltype(skill.skilltype)
                            hbox:
                                vbox:
                                    xalign 1.0 yalign 1.0
                                    text "[skill.pp]":
                                        size 22
                                vbox:
                                    xalign 1.0 yalign 1.0
                                    text "/[skill.max_pp]":
                                        size 18
                                vbox:
                                    xalign 1.0 yalign 1.0
                                    text "PP":
                                        size 15

                $ total += 1

            for i in range(total, 3*row):
                null height 1

    # Fighter HUD
    frame:
        xysize (941, 221)
        background path_ui + "display_box.png"
        xpos 970
        ypos 585
        add game.player.map_icon
        text game.player.name size 36 xpos 215 ypos 65
        text "Lv. [game.player.level]" size 22 xalign 0.90 ypos 72
        bar:
            left_bar bar_colour(path_ui, game.player.hp, game.player.max_hp)
            right_bar path_ui + "hp_bar_empty.png"
            thumb None
            thumb_shadow None
            thumb_offset 0
            left_gutter 0
            right_gutter 0
            value AnimatedValue(value=game.player.hp, range=game.player.max_hp, delay=bar_delay)
            range game.player.max_hp
            xysize (598, 20)
            xpos 270
            ypos 152
        if yamatoforce_enabled:
            add "battle/ui/yamatoforce_overlay.png" xpos 0 ypos 0

    frame:
        xysize (941, 221)
        background path_ui + "display_box.png"
        xpos 15
        ypos 25
        add game.enemy.map_icon
        if game.enemy:
            text game.enemy.name size 36 xpos 215 ypos 65
            text "Lv. [game.enemy.level]" size 22 xalign 0.90 ypos 72
            bar:
                left_bar bar_colour(path_ui, game.enemy.hp, game.enemy.max_hp)
                right_bar path_ui + "hp_bar_empty.png"
                thumb None
                thumb_shadow None
                thumb_offset 0
                left_gutter 0
                right_gutter 0
                value AnimatedValue(value=game.enemy.hp, range=game.enemy.max_hp, delay=bar_delay)
                range game.enemy.max_hp
                xysize (598, 20)
                xpos 270
                ypos 152
                
    add At(Solid("#000000"), getready_loadin_trans) xalign 0.5 yalign 0.5

    $ tooltip = GetTooltip()
    
    if tooltip:
        frame:
            style_group "tooltip_box"
            vbox:
                xalign 0.5
                yalign 0.5
                text "[tooltip]"
                
    if skip_battle_prompt:
        add Solid("#000000") alpha 0.6
        add "gear2" xalign 0.63 yalign 0.655
        add "gear" xalign 0.37 yalign 0.655
        frame:
            style_group "yesno"
            vbox:
                xalign 0.5
                yalign 0.93
                hbox:
                    label "Are you sure you want to skip this battle?":
                        xalign 0.5
                null height 18
                hbox:
                    xalign 0.5
                    imagebutton auto "gui/yesno_yes_%s.png" action [SetVariable("skip_battle_prompt", False), SetVariable("skip_battle_selected", True), SetVariable("persistent.skip_battle_sensitive", False), Function(game.can_run_away)] hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True
                    null width 60
                    imagebutton auto "gui/yesno_no_%s.png" action SetVariable("skip_battle_prompt", False) hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True
        vbox:
            xalign .5
            yalign .408
            add "gui/overlay_title_systemaction.png"
            
screen escape_battle_prompt():
    zorder 103
    modal True
    
    key "h" action NullAction()
    
    add Solid("#000000") alpha 0.6
    add "gear2" xalign 0.63 yalign 0.655
    add "gear" xalign 0.37 yalign 0.655
    frame:
        style_group "yesno"
        vbox:
            xalign 0.5
            yalign 0.93
            hbox:
                label "Are you sure you want to restart the battle?":
                    xalign 0.5
            null height 18
            hbox:
                xalign 0.5
                imagebutton auto "gui/yesno_yes_%s.png" action [SetVariable("mouse_visible", False), Stop("battlemusic", fadeout=1.0), Stop("battlesfx", fadeout=1.0), Hide("escape_battle_prompt"), Show("escape_battle_delay"), With(pixellate)] hover_sound "se/hover.ogg" activate_sound "se/fightui.ogg" focus_mask True
                null width 60
                imagebutton auto "gui/yesno_no_%s.png" action Hide("escape_battle_prompt") hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True    
    vbox:
        xalign .5
        yalign .408
        add "gui/overlay_title_restartbattle.png"
            
screen escape_battle_delay():
    zorder 104
    modal True
    add Solid("#000000")
    add "dis_chibi_random" xalign 0.25 yalign 0.49 zoom 0.55
    add "battle_reload_icon" xalign 0.48 yalign 0.5
    text "Restarting battle . . ." xalign 0.68 yalign 0.51 size 36 slow True slow_cps 45
    if escape_delay:
        timer 2.0 action [SetVariable("mouse_visible", True), SetVariable("escape_delay", False), Function(escape_skipvariables_update), Function(escape_rollback)]
    
    on "show":
        action SetVariable("escape_delay", True)
    
screen choose_fighter():
    zorder 10
    modal True

    frame:
        background Solid("#000000")
        xalign 0.5
        yalign 0.5
        vbox:
            spacing 10
            xalign 0.5
            yalign 0.5
            for i in player_team.store:
                textbutton _(i.name):
                    text_color "#ffffff"
                    action SetVariable("current_player", i), Return()

screen battle_party_screen(mid_game=False):
    modal True
    zorder 150
    
    key "h" action NullAction()

    default path_ui = "battle/ui/"
    if current_player.hp > 0:
        default chosen_player = current_player
    else:
        default chosen_player = None

    add path_ui + "party_window.jpg"

    viewport:
        id "party_screen_port"
        child_size (1350, 2660)
        area (68, 135, 1320, 900)
        mousewheel True
        vbox:
            spacing 10

            for fighter in player_team.store:
                button:
                    xysize (1261, 185)
                    if chosen_player == fighter:
                        background "party_member_display_hover"
                    elif current_player == fighter:
                        background "party_member_display_selected_idle"
                    else:
                        background "party_member_display"

                    add fighter.image xpos 13 ypos 28
                    text fighter.name style "battle_text" size 36 xpos 180 ypos 38
                    text "Lv. [fighter.level]" style "battle_text" size 22 xpos 750 ypos 46

                    grid 2 5:
                        xpos 935
                        ypos 17
                        spacing -1
                        hbox:
                            add "battleicon_power"
                            text "Power" size 13
                            null width 10
                    
                        fixed:
                            text str(int(fighter.attack)) size 13 xalign 0.5 text_align 0.5
                            xsize 70
                            yminimum 20
                            ymaximum 20
                            
                        hbox:
                            add "battleicon_armor"
                            text "Armor" size 13
                            null width 10

                        fixed:
                            text str(int(fighter.defense)) size 13 xalign 0.5 text_align 0.5
                            xsize 70
                            yminimum 20
                            ymaximum 20
                        
                        hbox:
                            add "battleicon_accuracy"
                            text "Accuracy" size 13
                            null width 10

                        fixed:
                            text str(int(fighter.accuracy)) size 13 xalign 0.5 text_align 0.5
                            xsize 70
                            yminimum 20
                            ymaximum 20
                        
                        hbox:
                            add "battleicon_charm"
                            text "Critical" size 13
                            null width 10

                        fixed:
                            text str(int(fighter.critical)) size 13 xalign 0.5 text_align 0.5
                            xsize 70
                            yminimum 20
                            ymaximum 20

                        hbox:
                            add "battleicon_speed"
                            text "Speed" size 13
                            null width 10

                        fixed:
                            text str(int(fighter.speed)) size 13 xalign 0.5 text_align 0.5
                            xsize 70
                            yminimum 20
                            ymaximum 20

                    if chosen_player == fighter:
                        imagebutton:
                            idle path_ui + "yesno_no_idle.png"
                            hover path_ui + "yesno_no_hover.png"
                            action SetScreenVariable("chosen_player", None)
                            xalign 0.9875
                            yalign 0.49
                            hover_sound "se/hover.ogg"
                            activate_sound "se/unequip.ogg"
                    else:
                        imagebutton:
                            idle path_ui + "yesno_switch_idle.png"
                            hover path_ui + "yesno_switch_hover.png"
                            action SetScreenVariable("chosen_player", fighter)
                            xalign 0.9875
                            yalign 0.49
                            hover_sound "se/hover.ogg"
                            activate_sound "se/equip.ogg"
                    bar:
                        left_bar bar_colour(path_ui, fighter.hp, fighter.max_hp)
                        right_bar path_ui + "hp_bar_empty.png"
                        thumb None
                        thumb_shadow None
                        thumb_offset 0
                        left_gutter 0
                        right_gutter 0
                        value fighter.hp
                        range fighter.max_hp
                        xysize (598, 20)
                        xpos 270
                        ypos 128

    vbar:
        base_bar Frame(path_ui + "overlay_vscrollbar_back.png")
        thumb path_ui + "overlay_scrollbar_button.png"
        unscrollable "hide"
        top_gutter 10
        bottom_gutter 10
        thumb_offset -15
        xysize (30, 925)
        value YScrollValue("party_screen_port")
        xpos 1360
        ypos 120

    vbox:
        xpos 1462
        ypos 14
        spacing 1
        button:
            xysize (442, 140)
            idle_background "party_choose_button_idle"
            hover_background "party_choose_button_hover"
            insensitive_background "party_choose_button_insensitive"
            hover_sound "se/hover.ogg"
            activate_sound "se/fightui.ogg"
            text "Choose" size 48 xalign 0.5 yalign 0.65
            sensitive chosen_player is not None and chosen_player is not current_player
            action ChangeFighter(fighter=chosen_player, shown=mid_game), If(mid_game, false=Return())
            at nav_eff

        button:
            xysize (442, 106)
            idle_background "party_cancel_button_idle"
            hover_background "party_cancel_button_hover"
            insensitive_background "party_cancel_button_insensitive"
            hover_sound "se/hover.ogg"
            activate_sound "se/click.ogg"
            text "Cancel" size 36 xalign 0.5 yalign 0.7
            sensitive store.current_player != None and store.current_player.hp > 0
            action If(mid_game, true=Hide("battle_party_screen"), false=Return())
            at nav_eff
            
    vbox:
        xysize (444, 644)
        xpos 1481
        ypos 380
        for fighter in player_team.store:
            if chosen_player == fighter:
                vbox:
                    hbox:
                        add fighter.image xpos 10 ypos 11
                        vbox:
                            style_group "update_stat" xalign 0.5 yalign 0 yfill False xfill False
                            frame:
                                style_group "description_box_dark"
                                xysize (252, 50)
                                xpos 20
                                vbox:
                                    frame:
                                        style_group "main_stats"
                                        xysize (242, 44)
                                        top_padding 13
                                        text fighter.name xalign 0.5 yalign 0.73 size 17
                                    frame:
                                        style_group "main_stats"
                                        xysize (242, 43)
                                        top_padding 12
                                        if not fighter.unit == "panzer":
                                            text fighter.unit.upper() + " TYPE" xalign 0.5 yalign 0.5 size 14 color "#FF9915"
                                        else:
                                            text "PANZY TYPE" xalign 0.5 yalign 0.5 size 14 color "#FF9915"
                                    hbox:
                                        frame:
                                            style_group "main_stats"
                                            xysize (90, 43)
                                            top_padding 11
                                            text "Terrain" xalign 0.5 yalign 0.75 size 14
                                        frame:
                                            style_group "battle_stats"
                                            xysize (152, 42)
                                            top_padding 11
                                            text str(fighter.terrain).capitalize() xalign 0.5 yalign 0.7 size 14
                                    
                    hbox:
                        vbox:
                            frame:
                                style_group "description_box_central"
                                xysize (409, 181)
                                yalign 0.5
                                vbox:
                                    frame:
                                        style_group "main_stats"
                                        xysize (398, 25)
                                        top_padding 11
                                        text "Primary Weapon" xalign 0.5 yalign 0.75 size 14
                                    frame:
                                        style_group "battle_stats"
                                        xysize (398, 30)
                                        top_padding 11
                                        text fighter.primary_weapon xalign 0.5 yalign 0.7 size 16
                                    frame:
                                        style_group "main_stats"
                                        xysize (398, 25)
                                        top_padding 11
                                        text "Secondary Weapon" xalign 0.5 yalign 0.75 size 14
                                    frame:
                                        style_group "battle_stats"
                                        xysize (398, 30)
                                        top_padding 11
                                        text fighter.secondary_weapon xalign 0.5 yalign 0.7 size 16
                                    frame:
                                        style_group "main_stats"
                                        xysize (398, 25)
                                        top_padding 11
                                        text "Description" xalign 0.5 yalign 0.75 size 14
                                    frame:
                                        style_group "battle_stats"
                                        xysize (398, 150)
                                        top_padding 10
                                        xpadding 12
                                        text fighter.description xalign 0.5 yalign 0.5 size 14 text_align 0.5 line_spacing 7

        if chosen_player == None and current_player:
            vbox:
                hbox:
                    if current_player.hp <= 0:
                        add "mia_profile" xpos 10 ypos 11
                    else:
                        add current_player.image xpos 10 ypos 11
                        
                    vbox:
                        style_group "update_stat" xalign 0.5 yalign 0 yfill False xfill False
                        frame:
                            style_group "description_box_dark"
                            xysize (252, 50)
                            xpos 20
                            vbox:
                                frame:
                                    style_group "main_stats"
                                    xysize (242, 44)
                                    top_padding 13
                                    text current_player.name xalign 0.5 yalign 0.73 size 17
                                frame:
                                    style_group "main_stats"
                                    xysize (242, 43)
                                    top_padding 12
                                    if not current_player.unit == "panzer":
                                        text current_player.unit.upper() + " TYPE" xalign 0.5 yalign 0.5 size 14 color "#FF9915"
                                    else:
                                        text "PANZY TYPE" xalign 0.5 yalign 0.5 size 14 color "#FF9915"
                                hbox:
                                    frame:
                                        style_group "main_stats"
                                        xysize (90, 43)
                                        top_padding 11
                                        text "Terrain" xalign 0.5 yalign 0.75 size 14
                                    frame:
                                        style_group "battle_stats"
                                        xysize (152, 42)
                                        top_padding 11
                                        text str(current_player.terrain).capitalize() xalign 0.5 yalign 0.7 size 14

                hbox:
                    vbox:
                        frame:
                            style_group "description_box_central"
                            xysize (409, 181)
                            yalign 0.5
                            vbox:
                                frame:
                                    style_group "main_stats"
                                    xysize (398, 25)
                                    top_padding 11
                                    text "Primary Weapon" xalign 0.5 yalign 0.75 size 14
                                frame:
                                    style_group "battle_stats"
                                    xysize (398, 30)
                                    top_padding 11
                                    text current_player.primary_weapon xalign 0.5 yalign 0.7 size 16
                                frame:
                                    style_group "main_stats"
                                    xysize (398, 25)
                                    top_padding 11
                                    text "Secondary Weapon" xalign 0.5 yalign 0.75 size 14
                                frame:
                                    style_group "battle_stats"
                                    xysize (398, 30)
                                    top_padding 11
                                    text current_player.secondary_weapon xalign 0.5 yalign 0.7 size 16
                                frame:
                                    style_group "main_stats"
                                    xysize (398, 25)
                                    top_padding 11
                                    text "Description" xalign 0.5 yalign 0.75 size 14
                                frame:
                                    style_group "battle_stats"
                                    xysize (398, 150)
                                    top_padding 10
                                    xpadding 12
                                    text current_player.description xalign 0.5 yalign 0.5 size 14 text_align 0.5 line_spacing 7

                
            
    fixed:
        xysize (360, 250)
        xpos 1504
        ypos 888
        if current_player and current_player.hp <= 0:
            text "[current_player.name]\n has been knocked out." style "battle_text" size 26 text_align 0.5 xalign 0.5 yalign 0.5
        elif current_player and current_player.hp > 0:
            text "[current_player.name]\n is fighting." style "battle_text"size 26 text_align 0.5 xalign 0.5 yalign 0.5

screen non_battle_party_screen():
    modal True
    
    key "h" action NullAction()
    
    on "hide":
        action With(battleclose)
        
    default path_ui = "battle/ui/"
    if airsupport_section_unlocked:
        default available_troops = show_section("airsupport")
    elif not nyanbattles_selection:
        default available_troops = show_section("commander")
    elif not infantry_section_unlocked:
        default available_troops = show_section("panzer")
    else:
        default available_troops = show_section("infantry")
    
    add path_ui + "party_selection_window.jpg"

    $ no_of_troops = len(available_troops)
    if available_troops == show_section("infantry"):
        $ current_locked_fighters = infantry_locked_fighters - no_of_troops
    elif available_troops == show_section("panzer"):
        $ current_locked_fighters = panzer_locked_fighters - no_of_troops
    elif available_troops == show_section("antitank"):
        $ current_locked_fighters = antitank_locked_fighters - no_of_troops
    elif available_troops == show_section("commander"):
        $ current_locked_fighters = commander_locked_fighters - no_of_troops
    elif available_troops == show_section("airsupport"):
        $ current_locked_fighters = airsupport_locked_fighters - no_of_troops
    elif available_troops == show_section("special group"):
        $ current_locked_fighters = specialgroup_locked_fighters - no_of_troops
    else:
        $ current_locked_fighters = overall_locked_fighters - no_of_troops
    $ overall_battlecards = no_of_troops + current_locked_fighters
    
    $ battlecards_grid_x = 8
    $ battlecards_grid_y = 6 #int((len(fighter_store) + current_locked_fighters) / battlecards_grid_x) #- 10  #+ 1
    $ battlecards_grid_num = battlecards_grid_x * battlecards_grid_y
    #$ fighter_row = len(fighter_store) / 8 if len(fighter_store) / 8 > 5 else 5
    
    viewport:
        id "non_battle_selection"
        child_size (1350, 9700)
        area (50, 124, 1365, 520)
        mousewheel True
        draggable True

        grid battlecards_grid_x battlecards_grid_y:
            spacing 2
            for i, fighter in sorted(available_troops.iteritems()):
                fixed:
                    xysize (163, 239)
                    if len(player_team.store) >= 8 or (len(player_team.store) >= 8 and fighter["cost"] > store.cp) or store.cp <= 0:
                        add "empty_card_insensitive"
                        add fighter["image"] xalign 0.5 yalign 0.27 alpha 0.3
                        text "{alpha=0.3}" + str(fighter["cost"]) + " CP" + "{/alpha}" style "party_text" xalign 0.9 yalign 0.035
                        fixed:
                            xpos 16
                            ypos 166
                            xysize (132, 27)
                            text "{alpha=0.3}" + str(fighter["name"]) + "{/alpha}" style "party_text" xalign 0.5 yalign 0.5
                        fixed:
                            xpos 66
                            ypos 200
                            xysize (30, 30)
                            text "{alpha=0.3}" + str(fighter["level"]) + "{/alpha}" style "party_text" size 17 xalign 0.5 yalign 0.5
                        imagebutton:
                            idle path_ui + "yesno_info_small_idle.png"
                            hover path_ui + "yesno_info_small_hover.png"
                            insensitive "yesno_info_small_insensitive"
                            action None
                            xpos 2
                            ypos 187
                        imagebutton:
                            idle path_ui + "yesno_add_small_idle.png"
                            hover path_ui + "yesno_add_small_hover.png"
                            insensitive "yesno_add_small_insensitive"
                            action None
                            xpos 111
                            ypos 187

                    elif not len(player_team.store) >= 8 or fighter["cost"] > store.cp:
                        add path_ui + "fighter_card.png"
                        add fighter["image"] xalign 0.5 yalign 0.27
                        text str(fighter["cost"]) + " CP" style "party_text" xalign 0.9 yalign 0.035
                        fixed:
                            xpos 16
                            ypos 166
                            xysize (132, 27)
                            text str(fighter["name"]) style "party_text" xalign 0.5 yalign 0.5
                        fixed:
                            xpos 66
                            ypos 200
                            xysize (30, 30)
                            text str(fighter["level"]) style "party_text" size 17 xalign 0.5 yalign 0.5
                        imagebutton:
                            idle path_ui + "yesno_info_small_idle.png"
                            hover path_ui + "yesno_info_small_hover.png"
                            insensitive "yesno_info_small_insensitive"
                            action Show(
                                "fighter_information", 
                                fullname=fighter["fullname"], 
                                description=fighter["description"], 
                                profile=fighter["image"],
                                attack=fighter["attack"],
                                defense=fighter["defense"],
                                accuracy=fighter["accuracy"],
                                speed=fighter["speed"],
                                critical=fighter["critical"],
                                level=fighter["level"],
                                cost=fighter["cost"],
                                unit=fighter["unit"],
                                terrain=fighter["terrain"],
                                primary_weapon=fighter["primary_weapon"],
                                secondary_weapon=fighter["secondary_weapon"],
                                map_icon=fighter["map_icon"],
                                motto=fighter["motto"],
                                perks=fighter["perks"]
                                )
                            hover_sound "se/hover.ogg"
                            activate_sound "se/info.ogg"
                            xpos 2
                            ypos 187
                        imagebutton:
                            idle path_ui + "yesno_add_small_idle.png"
                            hover path_ui + "yesno_add_small_hover.png"
                            insensitive "yesno_add_small_insensitive"
                            action AddToParty(i, fighter["cost"])
                            hover_sound "se/hover.ogg"
                            activate_sound "se/equip.ogg"                       
                            xpos 111
                            ypos 187
        
            for i in range(0, current_locked_fighters):
                fixed:
                    xysize (163, 239)
                    if len(player_team.store) >= 8 or (len(player_team.store) >= 8 and fighter["cost"] > store.cp) or store.cp <= 0:
                        add "empty_card_insensitive"
                        if available_troops == show_section("infantry"):
                            add "basic_infantry_profile_insensitive" xalign 0.5 yalign 0.27
                        elif available_troops == show_section("panzer"):
                            add "basic_panzer_profile_insensitive" xalign 0.5 yalign 0.27
                        elif available_troops == show_section("antitank"):
                            add "basic_antitank_profile_insensitive" xalign 0.5 yalign 0.27
                        elif available_troops == show_section("commander"):
                            add "basic_commander_profile_insensitive" xalign 0.5 yalign 0.27
                        elif available_troops == show_section("airsupport"):
                            add "basic_airsupport_profile_insensitive" xalign 0.5 yalign 0.27
                        elif available_troops == show_section("special group"):
                            add "basic_specialgroup_profile_insensitive" xalign 0.5 yalign 0.27
                        else:
                            add None
                        text "{alpha=0.3}?? CP{/alpha}" style "party_text" xalign 0.9 yalign 0.035
                        fixed:
                            xpos 16
                            ypos 167 
                            xysize (132, 27)
                            text "{alpha=0.3}???????????{/alpha}" style "party_text" xalign 0.5 yalign 0.5
                        fixed:
                            xpos 67
                            ypos 199
                            xysize (30, 33)
                            text "{alpha=0.3}?{/alpha}" style "party_text" size 18 xalign 0.5 yalign 0.5
                        imagebutton:
                            idle "yesno_info_small_insensitive"
                            action None
                            xpos 2
                            ypos 187
                        imagebutton:
                            idle "yesno_add_small_insensitive"
                            action None
                            xpos 111
                            ypos 187
                    elif not len(player_team.store) >= 8 or fighter["cost"] > store.cp:
                        add "empty_card_faded"
                        if available_troops == show_section("infantry"):
                            add "basic_infantry_profile" xalign 0.5 yalign 0.27
                        elif available_troops == show_section("panzer"):
                            add "basic_panzer_profile" xalign 0.5 yalign 0.27
                        elif available_troops == show_section("antitank"):
                            add "basic_antitank_profile" xalign 0.5 yalign 0.27
                        elif available_troops == show_section("commander"):
                            add "basic_commander_profile" xalign 0.5 yalign 0.27
                        elif available_troops == show_section("airsupport"):
                            add "basic_airsupport_profile" xalign 0.5 yalign 0.27
                        elif available_troops == show_section("special group"):
                            add "basic_specialgroup_profile" xalign 0.5 yalign 0.27
                        else:
                            add None
                        text "??" + " CP" style "party_text" xalign 0.9 yalign 0.035
                        fixed:
                            xpos 16
                            ypos 167     
                            xysize (132, 27)
                            text "???????????" style "party_text" xalign 0.5 yalign 0.5
                        fixed:
                            xpos 67
                            ypos 199
                            xysize (30, 33)
                            text "?" style "party_text" size 18 xalign 0.5 yalign 0.5
                        imagebutton:
                            idle "yesno_info_small_faded"
                            action None
                            xpos 2
                            ypos 187
                        imagebutton:
                            idle "yesno_add_small_faded"
                            action None
                            xpos 111    
                            ypos 187
                    
                    
            for i in range(0, battlecards_grid_num - overall_battlecards):
                add path_ui + "empty_card.png"

    vbar:
        base_bar Frame(path_ui + "overlay_vscrollbar_back.png")   
        thumb path_ui + "overlay_scrollbar_button.png"
        hover_thumb path_ui + "overlay_scrollbar_button_hover.png"
        unscrollable "hide"
        top_gutter 10
        bottom_gutter 10
        thumb_offset -10
        xysize (30, 510)
        value YScrollValue("non_battle_selection")
        xpos 1370
        ypos 120
    
    hbox:    
        xpos 158
        ypos 285
        if len(player_team.store) >= 8 or (len(player_team.store) >= 8 and store.cp <= 0):
            fixed:
                xysize (1100, 170)
                add "black" alpha 0.7
                text "Party Queue is full!" xalign 0.5 yalign 0.55
        elif store.cp <= 0:
            fixed:
                xysize (1100, 170)
                add "black" alpha 0.7
                text "No more Command Points to spend!" xalign 0.5 yalign 0.55
            
            
    hbox:
        xpos 65
        ypos 795
        spacing .5
        for fighter in player_team.store:
            fixed:
                xysize (163, 239)
                add path_ui + "fighter_card.png"
                add fighter.image xalign 0.5 yalign 0.27
                text str(fighter.cost) + " CP" style "party_text" xalign 0.9 yalign 0.035
                fixed:
                    xpos 16
                    ypos 166
                    xysize (132, 27)
                    text str(fighter.name) style "party_text" xalign 0.5 yalign 0.5
                fixed:
                    xpos 66
                    ypos 200
                    xysize (30, 30)
                    text str(fighter.level) style "party_text" size 17 xalign 0.5 yalign 0.5
                imagebutton:
                    idle path_ui + "yesno_info_small_idle.png"
                    hover path_ui + "yesno_info_small_hover.png"
                    action Show(
                        "fighter_information", 
                        fullname=fighter.fullname,
                        description=fighter.description,
                        profile=fighter.image,
                        attack=fighter.attack,
                        defense=fighter.defense,
                        accuracy=fighter.accuracy,
                        speed=fighter.speed,
                        critical=fighter.critical,
                        level=fighter.level,
                        cost=fighter.cost,
                        unit=fighter.unit,
                        terrain=fighter.terrain,
                        primary_weapon=fighter.primary_weapon,
                        secondary_weapon=fighter.secondary_weapon,
                        map_icon=fighter.map_icon,
                        motto=fighter.motto,
                        perks=fighter.perks
                        )
                    xpos 2
                    ypos 187
                    hover_sound "se/hover.ogg"
                    activate_sound "se/info.ogg"
                imagebutton:
                    idle path_ui + "yesno_no_small_idle.png"
                    hover path_ui + "yesno_no_small_hover.png"
                    action RemoveFromParty(fighter)
                    xpos 111
                    ypos 187
                    hover_sound "se/hover.ogg"
                    activate_sound "se/unequip.ogg"
                    
    text "[cp]{size=48}/[max_cp]{/size}{size=24} C P{/size}" size 72 style "cp_text" xalign 0.975 ypos 1

    vbox:
        xpos 1462
        ypos 120
        button:
            xysize (442, 140)
            idle_background "party_choose_button_idle"
            hover_background "party_choose_button_hover"
            insensitive_background "party_choose_button_insensitive"
            activate_sound "se/fightui.ogg"
            text "Fight!" size 48 xalign 0.5 yalign 0.63
            action [If(player_team.store, true=Return(), false=NullAction()), SensitiveIf(player_team.store), Stop("music")]
            at nav_eff
    vbox:
        xpos 1469
        ypos 289
        spacing -1
        button:
            style_group "availablesection"
            text "Infantry" size 28 xalign 0.5 yalign 0.63
            action [SetScreenVariable("available_troops", show_section("infantry")), SensitiveIf(infantry_section_unlocked)]
            at nav_eff
        button:
            style_group "availablesection"
            text "Panzy" size 28 xalign 0.5 yalign 0.63
            action [SetScreenVariable("available_troops", show_section("panzer")), SensitiveIf(panzer_section_unlocked)]
            at nav_eff
        button:
            style_group "availablesection"
            text "Antitank" size 28 xalign 0.5 yalign 0.63
            action [SetScreenVariable("available_troops", show_section("antitank")), SensitiveIf(antitank_section_unlocked)]
            at nav_eff
        button:
            style_group "availablesection"
            text "Commander" size 28 xalign 0.5 yalign 0.63
            action [SetScreenVariable("available_troops", show_section("commander")), SensitiveIf(commander_section_unlocked)]
            at nav_eff
        button:
            style_group "availablesection"
            text "Air Support" size 28 xalign 0.5 yalign 0.63
            action [SetScreenVariable("available_troops", show_section("airsupport")), SensitiveIf(airsupport_section_unlocked)]
            at nav_eff
        button:
            style_group "availablesection"
            text "Special Group" size 28 xalign 0.5 yalign 0.63
            action [SetScreenVariable("available_troops", show_section("special group")), SensitiveIf(specialgroup_section_unlocked)]
            at nav_eff
    

    hbox:
        xpos 1495
        ypos 952
        text "Select a battle stat to research across battles..." size 12.5
    hbox:
        xpos 1470
        ypos 974
        spacing 5
        imagebutton auto "battlestats_power_%s" action [SensitiveIf(nyanbattles_selection), SetVariable("battlestats_focus", "Power"), Function(battlestats_research_check), Show("research_prompt1")] hover_sound "se/hover.ogg" activate_sound "se/researchui.ogg" focus_mask True
        imagebutton auto "battlestats_armor_%s" action [SensitiveIf(nyanbattles_selection), SetVariable("battlestats_focus", "Armor"), Function(battlestats_research_check), Show("research_prompt2")] hover_sound "se/hover.ogg" activate_sound "se/researchui.ogg" focus_mask True
        imagebutton auto "battlestats_accuracy_%s" action [SensitiveIf(nyanbattles_selection), SetVariable("battlestats_focus", "Accuracy"), Function(battlestats_research_check), Show("research_prompt4")] hover_sound "se/hover.ogg" activate_sound "se/researchui.ogg" focus_mask True
        imagebutton auto "battlestats_charm_%s" action [SensitiveIf(nyanbattles_selection), SetVariable("battlestats_focus", "Critical"), Function(battlestats_research_check), Show("research_prompt3")] hover_sound "se/hover.ogg" activate_sound "se/researchui.ogg" focus_mask True
        imagebutton auto "battlestats_speed_%s" action [SensitiveIf(nyanbattles_selection), SetVariable("battlestats_focus", "Speed"), Function(battlestats_research_check), Show("research_prompt5")] hover_sound "se/hover.ogg" activate_sound "se/researchui.ogg" focus_mask True
        
    hbox:
        xpos 16
        ypos 16
        imagebutton idle path_ui + "yesno_info_small_idle.png" hover path_ui + "yesno_info_small_hover.png" insensitive "yesno_info_small_insensitive" action Show("battleinfo_prompt") hover_sound "se/hover.ogg" activate_sound "se/info.ogg" focus_mask True
        
screen battleinfo_prompt():
    add Solid("#000000") alpha 0.6
    add "gear2" xalign 0.63 yalign 0.655
    add "gear" xalign 0.37 yalign 0.655
    frame:
        style_group "yesno"
        vbox:
            xalign 0.5
            yalign 0.93
            hbox:
                label "[q_title]":
                    xalign 0.5
            null height 18
            hbox:
                xalign 0.5
                imagebutton auto "gui/yesno_yes_%s.png" action Hide("battleinfo_prompt") hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True at quick_eff
    vbox:
        xalign .5
        yalign .408
        add "gui/overlay_title_battleinformation.png"    
    
screen research_prompt():
    add Solid("#000000") alpha 0.6
    add "gear2" xalign 0.63 yalign 0.655
    add "gear" xalign 0.37 yalign 0.655
    frame:
        style_group "yesno"
        vbox:
            xalign 0.5
            yalign 0.65
            label "You are now researching [battlestats_focus]!":
                xalign 0.5
    vbox:
        xalign 0.5
        yalign 0.65
        button:
            style_group "researchsection"
            text "View Research Tree" size 21 xalign 0.5 yalign 0.6
            action [Hide("research_prompt1"), Hide("research_prompt2"), Hide("research_prompt3"), Hide("research_prompt4"), Hide("research_prompt5"), Show("research_information")]
            activate_sound "se/info.ogg"
            at nav_eff
    vbox:
        xalign 0.7745
        yalign 0.348
        imagebutton idle "yesno_no_small_idle" hover "yesno_no_small_hover" action [Hide("research_prompt1"), Hide("research_prompt2"), Hide("research_prompt3"), Hide("research_prompt4"), Hide("research_prompt5")] focus_mask True hover_sound "se/hover.ogg" activate_sound "se/click.ogg" at mapicon_eff            
    vbox:
        xalign .5
        yalign .408
        add "gui/overlay_title_research.png"    
                
screen research_prompt1():
    modal True
    use research_prompt
    
screen research_prompt2():
    modal True
    use research_prompt
    
screen research_prompt3():
    modal True
    use research_prompt
    
screen research_prompt4():
    modal True
    use research_prompt
    
screen research_prompt5():
    modal True
    use research_prompt
    
screen research_information():
    modal True
    
    add Solid("#000000") alpha 0.6
    add "gear2" xalign 0.78 yalign 0.93
    add "gear" xalign 0.68 yalign 0.93
    add "gear" xalign 0.22 yalign 0.93
    add "gear2" xalign 0.32 yalign 0.93
    frame:
        style_group "overlayboxlarge"
        xalign .5
        yalign .5
        xmaximum 1569
        xminimum 1569
        ymaximum 910
        yminimum 910
        yfill False
        xfill False
        frame:
            style_group "governor2"
            xminimum 1500
            xmaximum 1500
            yminimum 670
            ymaximum 670
            bottom_padding 1
            top_padding 1
            yalign 0.85
            xalign 0.51
            vbox:
                xalign 0.5
                yalign 0.5
                yfill False
                xfill False
                viewport:
                    scrollbars "vertical"
                    xmaximum 1480
                    xminimum 1480
                    ymaximum 626
                    yminimum 626
                    viewport_yminimum 653
                    viewport_yoffset -13
                    yalign 0.5
                    side_yalign .5
                    side_ymaximum 600
                    side_spacing -30
                    draggable True
                    mousewheel True
                    vbox:
                        xalign 0.5
                        yalign 0.1
                        style_group "update_stat"
                        yfill False
                        xfill False
                        frame:
                            style_group "governor2"
                            xminimum 1450
                            xmaximum 1450
                            yminimum 40
                            ymaximum 40
                            top_padding 20
                            hbox:
                                style_group "governor"
                                xalign 0.5
                                yalign 0.5
                                vbox:
                                    text "{size=30}You are currently researching [battlestats_focus]!{/size}"
                        frame:
                            style_group "governor2"
                            xminimum 1450
                            xmaximum 1450
                            yminimum 1194
                            ymaximum 1194
                            vbox:
                                add "gui/research_branch.png"
                                xalign 0.5
                                yalign 0.5
                                
                            for key, value in sorted(active_research_items.items()):
                                frame:
                                    style_group "research"
                                    xpos value[1]
                                    ypos value[2]
                                    vbox:
                                        frame:
                                            style_group "research_upper"
                                            imagebutton idle value[0] action NullAction() hover_sound "se/hover.ogg":
                                                xalign 0.5 
                                                tooltip key + "_description"
                                        frame:
                                            style_group "research_lower"
                                            text key
                                if value[3] == True:
                                    vbox:
                                        add "gui/tick.png"
                                        xpos value[1] + 34
                                        ypos value[2] + 75
                                
                                if value[4] == True:
                                    vbox:
                                        frame:
                                            style_group "research_counter"
                                            if "power" in value[0]:
                                                text str(int(value[5] - (battlestats_attack_up * 4)))
                                            elif "armor" in value[0]:
                                                text str(int(value[5] - (battlestats_defense_up * 4)))
                                            elif "accuracy" in value[0]:
                                                text str(int(value[5] - (battlestats_accuracy_up * 4)))
                                            elif "charm" in value[0]:
                                                text str(int(value[5] - (battlestats_critical_up * 4)))
                                            else:
                                                text str(int(value[5] - (battlestats_speed_up * 4)))
                                        xpos value[1] + 30
                                        ypos value[2] + 16
                                    vbox:
                                        add "gui/researching.png"
                                        xpos value[1] + 30
                                        ypos value[2] + 75
    frame:
        background "gui/overlay_frame_back1.png"
        xalign .5
        yalign .5
        xmaximum 1569
        xminimum 1569
        ymaximum 910
        yminimum 910
        yfill False
        xfill False
    vbox:
        xalign .5
        yalign .15
        add "gui/overlay_title_research.png"
    hbox:
        style_group "bonus"
        xalign .9
        yalign .095
        imagebutton idle "yesno_no_small_idle" hover "yesno_no_small_hover" action Hide("research_information") focus_mask True hover_sound "se/hover.ogg" activate_sound "se/click.ogg" at mapicon_eff
        
    $ tooltip = GetTooltip()
    
    if tooltip and not "?" in tooltip:
        frame:
            style_group "tooltip3_box"
            vbox:
                xalign 0.5
                yalign 0.5
                text str(eval(tooltip.lower().replace(" ", "")))
        
screen fighter_information(fullname, description, profile, attack, defense, accuracy, speed, critical, level, cost, unit, terrain, primary_weapon, secondary_weapon, map_icon, motto, perks):
    modal True
    add Solid("#000000") alpha 0.6
    add "gear2" xalign 0.685 yalign 0.785
    add "gear" xalign 0.315 yalign 0.785
    frame:
        style_group "overlayboxsmall"
        xalign .5
        yalign .5
        xmaximum 1300
        xminimum 1300
        ymaximum 638
        yminimum 638
        yfill False
        xfill False
        frame:
            style_group "description_box_central"
            xminimum 1231
            xmaximum 1231
            yminimum 399
            ymaximum 399
            bottom_padding 1
            top_padding 1
            yalign 0.85
            xalign 0.51
            vbox:
                xalign 0.5 yalign 0.5 yfill False xfill False
                viewport:
                    scrollbars "vertical"
                    xmaximum 1211
                    xminimum 1211
                    ymaximum 350
                    yminimum 350
                    viewport_yminimum 379
                    viewport_ymaximum 379
                    yalign 0.5
                    viewport_yoffset -14
                    side_yalign .5
                    side_ymaximum 350
                    side_spacing -30
                    draggable True
                    mousewheel True
                    hbox:
                        vbox:
                            style_group "update_stat" xalign 0.5 yalign 0 yfill False xfill False
                            frame:
                                style_group "description_box_dark"
                                xysize (756, 80)
                                text fullname xalign 0.5 yalign 0.75 size 26
                            frame:
                                style_group "description_box_dark"
                                xysize (756, 30)
                                xpadding 20
                                top_padding 15
                                bottom_padding -1
                                if not unit == "panzer":
                                    text unit.upper() + " TYPE" xalign 0.5 yalign 0.7 size 18 color "#FF9915" kerning 2
                                else:
                                    text "PANZY TYPE" xalign 0.5 yalign 0.7 size 18 color "#FF9915" kerning 2
                            frame:
                                style_group "description_box_central"
                                xysize (756, 162)
                                yalign 0.5
                                vbox:
                                    hbox:
                                        frame:
                                            style_group "main_stats"
                                            xysize (221, 50)
                                            xpadding 20
                                            top_padding 15
                                            text "Command" xalign 0.5 yalign 0.7 size 20
                                        frame:
                                            style_group "battle_stats"
                                            xysize (150, 50)
                                            xpadding 20
                                            top_padding 15
                                            text str(cost) + " CP" xalign 0.5 yalign 0.7 size 20
                                        frame:
                                            style_group "main_stats"
                                            xysize (221, 50)
                                            xpadding 20
                                            top_padding 15
                                            text "Critical" xalign 0.5 yalign 0.7 size 20
                                        frame:
                                            style_group "battle_stats"
                                            xysize (151, 50)
                                            xpadding 20
                                            top_padding 15
                                            text str(int(critical)) xalign 0.5 yalign 0.7 size 20
                                    hbox:
                                        frame:
                                            style_group "main_stats"
                                            xysize (221, 50)
                                            xpadding 20
                                            top_padding 15
                                            text "Power" xalign 0.5 yalign 0.7 size 20
                                        frame:
                                            style_group "battle_stats"
                                            xysize (150, 50)
                                            xpadding 20
                                            top_padding 15
                                            text str(int(attack)) xalign 0.5 yalign 0.7 size 20
                                        frame:
                                            style_group "main_stats"
                                            xysize (221, 50)
                                            xpadding 20
                                            top_padding 15
                                            text "Armor" xalign 0.5 yalign 0.7 size 20
                                        frame:
                                            style_group "battle_stats"
                                            xysize (151, 50)
                                            xpadding 20
                                            top_padding 15
                                            text str(int(defense)) xalign 0.5 yalign 0.7 size 20
                                    hbox:
                                        frame:
                                            style_group "main_stats"
                                            xysize (221, 50)
                                            xpadding 20
                                            top_padding 15
                                            text "Accuracy" xalign 0.5 yalign 0.7 size 20
                                        frame:
                                            style_group "battle_stats"
                                            xysize (150, 50)
                                            xpadding 20
                                            top_padding 15
                                            text str(int(accuracy)) xalign 0.5 yalign 0.7 size 20
                                        frame:
                                            style_group "main_stats"
                                            xysize (221, 50)
                                            xpadding 20
                                            top_padding 15
                                            text "Speed" xalign 0.5 yalign 0.7 size 20
                                        frame:
                                            style_group "battle_stats"
                                            xysize (151, 50)
                                            xpadding 20
                                            top_padding 15
                                            text str(int(speed)) xalign 0.5 yalign 0.7 size 20
                            frame:
                                style_group "description_box_central"
                                xysize (756, 112)
                                yalign 0.5
                                vbox:
                                    hbox:
                                        frame:
                                            style_group "main_stats"
                                            xysize (300, 50)
                                            xpadding 20
                                            top_padding 15
                                            text "Primary Weapon" xalign 0.5 yalign 0.7 size 20
                                        frame:
                                            style_group "battle_stats"
                                            xysize (443, 50)
                                            xpadding 20
                                            top_padding 15
                                            text primary_weapon xalign 0.5 yalign 0.7 size 20
                                    hbox:
                                        frame:
                                            style_group "main_stats"
                                            xysize (300, 50)
                                            xpadding 20
                                            top_padding 15
                                            text "Secondary Weapon" xalign 0.5 yalign 0.7 size 20
                                        frame:
                                            style_group "battle_stats"
                                            xysize (443, 50)
                                            xpadding 20
                                            top_padding 15
                                            text secondary_weapon xalign 0.5 yalign 0.7 size 20
                            frame:
                                style_group "description_box_central"
                                xysize (756, 140)
                                xpadding 30
                                top_padding 20
                                text description xalign 0.5 yalign 0.5 size 18 text_align 0.5
                            frame:
                                style_group "description_box_central"
                                xysize (756, 115)
                                yalign 0.5
                                vbox:
                                    hbox:
                                        frame:
                                            style_group "main_stats"
                                            xysize (186, 103)
                                            imagebutton idle return_perks(perks[0]) xalign 0.5 yalign 0.5 action NullAction() tooltip str(eval(perks[0] + "_description")) hover_sound "se/hover.ogg"
                                        frame:
                                            style_group "main_stats"
                                            xysize (186, 103)
                                            imagebutton idle return_perks(perks[1]) xalign 0.5 yalign 0.5 action NullAction() tooltip str(eval(perks[1] + "_description")) hover_sound "se/hover.ogg"
                                        frame:
                                            style_group "main_stats"
                                            xysize (186, 103)
                                            imagebutton idle return_perks(perks[2]) xalign 0.5 yalign 0.5 action NullAction() tooltip str(eval(perks[2] + "_description")) hover_sound "se/hover.ogg"
                                        frame:
                                            style_group "main_stats"
                                            xysize (186, 103)
                                            imagebutton idle return_perks(perks[3]) xalign 0.5 yalign 0.5 action NullAction() tooltip str(eval(perks[3] + "_description")) hover_sound "se/hover.ogg"
                            
                        vbox:
                            style_group "update_stat" xalign 0.5 yalign 0 yfill False xfill False
                            frame:
                                style_group "description_box_central"
                                xysize (425, 395)
                                add profile zoom 3.0 nearest True xalign 0.5 yalign 0.5
                            frame:
                                style_group "description_box_dark"
                                xysize (425, 55)
                                xpadding 10
                                top_padding 17
                                text "{i}'" + motto + "'{/i}" xalign 0.5 yalign 0.8 size 17
                            frame:
                                style_group "description_box_central"
                                xysize (425, 227)
                                vbox:
                                    hbox:
                                        vbox:
                                            frame:
                                                style_group "main_stats"
                                                xysize (204, 54)
                                                top_padding 13
                                                text "Exp. Level" xalign 0.5 yalign 0.7 size 20
                                            frame:
                                                style_group "battle_stats"
                                                xysize (204, 54)
                                                xpadding 20
                                                top_padding 15
                                                text "[level]" xalign 0.5 yalign 0.7 size 20
                                            frame:
                                                style_group "main_stats"
                                                xysize (204, 54)
                                                top_padding 13
                                                text "Terrain" xalign 0.5 yalign 0.7 size 20
                                            frame:
                                                style_group "battle_stats"
                                                xysize (204, 54)
                                                xpadding 20
                                                top_padding 15
                                                text terrain.capitalize() xalign 0.5 yalign 0.7 size 20
                                        frame:
                                            style_group "main_stats"
                                            xysize (210, 216)
                                            add map_icon xalign 0.5 yalign 0.5    

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
        add "gui/overlay_title_fighterinformation.png"
    hbox:
        style_group "bonus"
        xalign .828
        yalign .226
        imagebutton idle "yesno_no_small_idle" hover "yesno_no_small_hover" action Hide("fighter_information") focus_mask True hover_sound "se/hover.ogg" activate_sound "se/click.ogg" at mapicon_eff
        
    $ tooltip = GetTooltip()
    
    if tooltip and not "x_description" in tooltip:
        frame:
            style_group "tooltip3_box"
            vbox:
                xalign 0.5
                yalign 0.5
                text "[tooltip]"
    
    
screen victoryscreen_right():
    vbox:
        xalign 0.5
        yalign -0.1
        for x in [1, 3, 8]:
            if (battle_count % 10) == x:
                add "character/hitora/campaign_hitora.png" at victoryscreen_slideinleft_hitora_eff
        for x in [2, 5, 4, 0]:
            if (battle_count % 10) == x:
                add "character/churchill/campaign_churchill.png" at victoryscreen_slideinleft_churchill_eff
        for x in [7, 6, 9]:
            if (battle_count % 10) == x:
                add "character/rinni/campaign_rinni.png" at victoryscreen_slideinleft_rinni_eff
        
        
screen victoryscreen_left():
    vbox:
        xalign 0.5
        yalign -0.1
        for x in [1, 4, 7]:
            if (battle_count % 10) == x:
                add "character/campaign_yamato.png" at victoryscreen_slideinright_yamato_eff
        for x in [2, 6, 8, 0]:
            if (battle_count % 10) == x:
                add "character/cyrano/campaign_cyrano.png" at victoryscreen_slideinright_cyrano_eff
        for x in [3, 5, 9]:
            if (battle_count % 10) == x:
                add "character/starin/campaign_starin.png" at victoryscreen_slideinright_starin_eff
        

screen victory_screen(won):
    #tag battle_screen
    modal True
    zorder 12
    
    add "black" alpha 0.95
    add "gear2" xalign 0.635 yalign 0.775
    add "gear" xalign 0.37 yalign 0.775
    frame:
        style_group "victoryscreen"
        xalign .5
        yalign .5
        xmaximum 1165
        xminimum 1165
        ymaximum 598
        yminimum 598
        yfill False
        xfill False

        vbox:
            xalign 0.51
            yalign 0.328
            text game.name:
                size 20
            
        vbox:
            xalign 0.51
            yalign 0.712
            grid 4 1:
                spacing 26
                vbox:
                    vbox:
                        xmaximum 170
                        xminimum 170
                        ymaximum 170
                        yminimum 170
                        add "captured_" + game.capture
                    vbox:
                        xmaximum 170
                        xminimum 170
                        ymaximum 40
                        yminimum 40
                        null height 15
                        text "Captured"
                vbox:
                    vbox:
                        xmaximum 170
                        xminimum 170
                        ymaximum 170
                        yminimum 170
                        add "critical_ticker"
                    vbox:
                        xmaximum 170
                        xminimum 170
                        ymaximum 40
                        yminimum 40
                        null height 15
                        text "Critical Hits"
                vbox:
                    vbox:
                        xmaximum 170
                        xminimum 170
                        ymaximum 170
                        yminimum 170
                        add "missed_ticker"
                    vbox:
                        xmaximum 170
                        xminimum 170
                        ymaximum 40
                        yminimum 40
                        null height 15
                        text "Misfires"
                vbox:
                    vbox:
                        xmaximum 170
                        xminimum 170
                        ymaximum 170
                        yminimum 170
                        add "totaldamage_ticker"
                    vbox:
                        xmaximum 170
                        xminimum 170
                        ymaximum 40
                        yminimum 40
                        null height 15
                        text "Total Damage"
    
    button:
        style_group "availablesection"
        text "Continue" size 28 xalign 0.5 yalign 0.63
        action [ Stop("victorymusic", fadeout=3.0), Hide("victory_screen"), With(pixellate), Stop("tickersound"), Jump(fight_end) ]
        activate_sound "se/fightui.ogg"
        xalign 0.5
        yalign 0.775
        
    frame:
        background Frame(im.Sepia("gui/outer_frame.png"), 200, 200)
        xminimum 1922
        yminimum 1082
            
    use victoryscreen_right
    use victoryscreen_left
    if not abs(int(game.player_counter["total_damage"])) <= 0:
        timer 0.01 action Play("tickersound", "se/ticker.ogg")
        timer (0.00066 * abs(int(game.player_counter["total_damage"]))) action Stop("tickersound")
 
        

    

        
init:
    python:
        def critical_countdown(st, at, length=0.0):
            remaining = length + (st * 150)
            if remaining < abs(int(game.player_counter["critical"])):
                return Text("%.0f" % remaining, color="#ffffff", size=45, kerning=-2, xalign=0.5, yalign=0.6), 0.01
            else:
                return Text(str(abs(int(game.player_counter["critical"]))), color="#ffffff", size=45, kerning=-2, xalign=0.5, yalign=0.6), None
                
        def missed_countdown(st, at, length=0.0):
            remaining = length + (st * 150)
            if remaining < abs(int(game.player_counter["missed"])):
                return Text("%.0f" % remaining, color="#ffffff", size=45, kerning=-2, xalign=0.5, yalign=0.6), 0.01
            else:
                return Text(str(abs(int(game.player_counter["missed"]))), color="#ffffff", size=45, kerning=-2, xalign=0.5, yalign=0.6), None
                
        def totaldamage_countdown(st, at, length=0.0):
            remaining = length + (st * 1500)
            if remaining < abs(int(game.player_counter["total_damage"])):
                return Text("%.0f" % remaining, color="#ffffff", size=45, kerning=-2, xalign=0.5, yalign=0.6), 0.01
            else:
                return Text(str(abs(int(game.player_counter["total_damage"]))), color="#ffffff", size=45, kerning=-2, xalign=0.5, yalign=0.6), None

    # Show a countdown for 10 seconds.
    image critical_ticker = DynamicDisplayable(critical_countdown, length=0.0)
    image missed_ticker = DynamicDisplayable(missed_countdown, length=0.0)
    image totaldamage_ticker = DynamicDisplayable(totaldamage_countdown, length=0.0)
            
screen get_ready():
    zorder 15
    timer 5.5 action [Hide("get_ready"), Function(game.resume_game)]
    timer 0.8 action [Play("mmsound","se/thud.ogg")]
    timer 2.5 action [Play("mmsound2","se/thud.ogg")]
    add At("readyfight_text_getready", getready_trans)
    add At("readyfight_text_fight", getready_second_trans)
    add "getready_blackbars"
    
screen battleground_back():
    zorder 10
    frame:
        background battleground_bg
        xsize 1920
        ysize 1080
        xalign 0.5
        yalign 0.5
        xpadding 0
        ypadding 0
    
screen battle_sprites(im, xypos):
    zorder 90
    tag sprites_battle

    showif game.attacker == game.player:
        add At(im, displaying_sprite_delay):
            pos xypos
            
    showif game.attacker == game.enemy:
        add At(im, displaying_sprite_delay_secondary):
            pos xypos
            
    add "crop_dialogbox" xalign 0.0 yalign 0.796
    
    on "show" action SetVariable("battlesprite_overlaying", True)
    on "hide" action SetVariable("battlesprite_overlaying", False)
    
    
image crop_dialogbox:
    im.Crop("battle/ui/window.png", (0, 37, 1920, 53))
    
image gameover_anim:
    contains:
        Solid("#000000")
    contains:
        "gui/game_over.png"
        xalign 0.5
        yalign 0.5
        alpha 0
        linear 2.0 alpha 1.0
    
