#----------------------------------------------------------------------------------------------------------------------------------------------------------
###CODEX
#----------------------------------------------------------------------------------------------------------------------------------------------------------
screen codex():
    modal True
    tag menu
    image "codexback"
    hbox:
        xalign 0.5
        yalign 0.5
        if codex_navchoice == "codex1":
            use codex1
        elif codex_navchoice == "codex2":
            use codex2
        elif codex_navchoice == "codex3":
            use codex3
        elif codex_navchoice == "codex5":
            use fuuhbarmuseum
        else:
            use codex1
    add "gui/bottom_bar.png" xalign 0.5 yalign 0.98
    hbox:
        style_group "readback"
        xalign 0.5 yalign 1.005
        textbutton _("Return") action [SetVariable("codex_navchoice", "codex0"), Hide("codex"), Return()] hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True at quick_eff
        textbutton _("Characters") action SetVariable("codex_navchoice", "codex1") hover_sound "se/hover.ogg" activate_sound "se/section.ogg" focus_mask True at quick_eff
        textbutton _("Map") action SetVariable("codex_navchoice", "codex2") hover_sound "se/hover.ogg" activate_sound "se/section.ogg" focus_mask True at quick_eff
        textbutton _("Command") action [Function(command_update), SetVariable("codex_navchoice", "codex3")] hover_sound "se/hover.ogg" activate_sound "se/section.ogg" focus_mask True at quick_eff
        textbutton _("Museum") action [Function(museum_update), SetVariable("codex_navchoice", "codex5")] hover_sound "se/hover.ogg" activate_sound "se/section.ogg" focus_mask True at quick_eff
        textbutton _("Main Menu") action MainMenu() hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True at quick_eff
    frame:
        style_group "readback2"
        ymaximum 85
        yminimum 85
        xmaximum 1875
        xpadding 10
        top_padding 10
        bottom_padding 10
        yalign 0.021
        xalign 0.5
        vbox:
            add "gui/codex_bar.png"
            xalign 0.5
            yalign 0.5
    frame:
        background Frame(im.Sepia("gui/outer_frame.png"), 200, 200)
        xminimum 1922
        yminimum 1082
                  
screen codex1():
    tag menu2
    vbox:
        hbox:
            frame:
                style_group "codexheading"
                xminimum 1824
                xmaximum 1824
                ymaximum 60
                yminimum 60
                hbox:
                    add "gui/codex/codex_heading_characters.jpg"
                
        hbox:
            frame:
                style_group "codexouter"
                vbox:
                    viewport:
                        scrollbars "vertical"
                        xmaximum 350
                        xminimum 350
                        ymaximum 740
                        yminimum 740
                        viewport_yminimum 774
                        viewport_yoffset -17
                        yalign 0.5
                        side_yalign .5
                        side_ymaximum 740
                        side_spacing -60
                        draggable False
                        mousewheel True
                        frame:
                            style_group "codexinner"
                            vbox:
                                for key, value in sorted(active_codex_profiles.items()):
                                    textbutton "[key]" action [
                                    SetVariable("profile_name", value[0]), 
                                    SetVariable("profile_flag", value[1]), 
                                    SetVariable("profile_birthplace", value[2]), 
                                    SetVariable("profile_description", value[3]), 
                                    SetVariable("profile_type", value[4]), 
                                    SetVariable("profile_birthday", value[5]), 
                                    SetVariable("profile_zodiac", value[6]), 
                                    SetVariable("profile_role", value[7]), 
                                    SetVariable("profile_height", value[8]), 
                                    SetVariable("profile_blood", value[9]), 
                                    SetVariable("profile_drink", value[10]), 
                                    SetVariable("profile_food", value[11]), 
                                    SetVariable("profile_weight", value[12]), 
                                    SetVariable("profile_sprite", value[13])
                                    ] at nav_eff focus_mask True
    
            frame:
                style_group "codexbasic"
                xminimum 1458
                xmaximum 1458
                yminimum 790
                ymaximum 790
                bottom_padding 1
                top_padding 1
                yalign 0.75
                xalign 0.9
                vbox:
                    xalign 0
                    yalign 0.5
                    viewport:
                        scrollbars "vertical"
                        xmaximum 1432
                        xminimum 1432
                        ymaximum 740
                        yminimum 740
                        viewport_yminimum 774
                        viewport_yoffset -16
                        xalign 0
                        yalign 0.5
                        side_yalign .5
                        side_ymaximum 740
                        side_spacing -40
                        draggable True
                        mousewheel True
                        vbox:
                            xalign 0
                            yalign 0.1
                            style_group "update_stat"
                            yfill False
                            xfill False
                            hbox:
                                frame:
                                    style_group "governor2"
                                    xminimum 200
                                    xmaximum 200
                                    yminimum 200
                                    ymaximum 200
                                    xpadding 5
                                    ypadding 5
                                    vbox:
                                        xalign 0.5
                                        yalign 0.5
                                        add profile_flag
                                frame:
                                    style_group "codexbasic"
                                    xminimum 1182
                                    xmaximum 1182
                                    yminimum 210
                                    ymaximum 210
                                    hbox:
                                        vbox:
                                            null height 10
                                            hbox:
                                                text "{size=50}[profile_name]{/size}"
                                            hbox:
                                                text "{size=30}{i}[profile_role]{/i}{/size}"
                            hbox:
                                vbox:
                                    frame:
                                        style_group "codexsubtitle"
                                        xminimum 1029
                                        xmaximum 1029
                                        hbox:
                                            text "Character Statistics"
                                    frame:
                                        style_group "governor2"
                                        xminimum 1000
                                        xmaximum 1000
                                        yminimum 224
                                        ymaximum 224
                                        hbox:
                                            vbox:
                                                frame:
                                                    style_group "codexstatstitle"
                                                    text "Type:"
                                                frame:
                                                    style_group "codexstatstitle"
                                                    text "Nation:"
                                                frame:
                                                    style_group "codexstatstitle"
                                                    text "Birthday:"
                                            vbox:
                                                frame:
                                                    style_group "codexstats"
                                                    text "[profile_type]".strip()
                                                frame:
                                                    style_group "codexstats"
                                                    text "[profile_birthplace]".strip()
                                                frame:
                                                    style_group "codexstats"
                                                    text "[profile_birthday]".strip()
                                            vbox:
                                                frame:
                                                    style_group "codexstatstitle"
                                                    text "Blood:"
                                                frame:
                                                    style_group "codexstatstitle"
                                                    text "Zodiac:"
                                                frame:
                                                    style_group "codexstatstitle"
                                                    text "Height:"
                                            vbox:
                                                frame:
                                                    style_group "codexstats"
                                                    text "[profile_blood]".strip()
                                                frame:
                                                    style_group "codexstats"
                                                    text "[profile_zodiac]".strip()
                                                frame:
                                                    style_group "codexstats"
                                                    text "[profile_height] cm".strip()
                                            vbox:
                                                frame:
                                                    style_group "codexstatstitle"
                                                    text "Weight:"
                                                frame:
                                                    style_group "codexstatstitle"
                                                    text "Fav. Food:"
                                                frame:
                                                    style_group "codexstatstitle"
                                                    text "Fav. Drink:"
                                            vbox:
                                                frame:
                                                    style_group "codexstats"
                                                    text "[profile_weight] kg".strip()
                                                frame:
                                                    style_group "codexstats"
                                                    text "[profile_food]".strip()
                                                frame:
                                                    style_group "codexstats"
                                                    text "[profile_drink]".strip()
                                vbox:
                                    frame:
                                        style_group "codexsubtitle"
                                        xminimum 363
                                        xmaximum 363
                                        hbox:
                                            text "Photograph"
                                    frame:
                                        style_group "codexprofile"
                                        add profile_sprite
                            hbox:
                                vbox:
                                    frame:
                                        style_group "codexsubtitle"
                                        xminimum 1392
                                        xmaximum 1392
                                        hbox:
                                            text "Character Bio"
                                    frame:                   
                                        style_group "codexbody"
                                        xminimum 1392
                                        xmaximum 1392
                                        yminimum 230
                                        ymaximum 230
                                        top_padding 60
                                        xpadding 60
                                        xalign 0.5
                                        hbox:
                                            text "[profile_description]":
                                                xalign 0.5
                                                text_align 0.5
                                                yalign 0.5
                                        
    

screen codex2():
    tag menu2
    vbox:
        hbox:
            frame:
                style_group "codexheading"
                xminimum 1824
                xmaximum 1824
                ymaximum 60
                yminimum 60
                hbox:
                    add "gui/codex/codex_heading_map.jpg"
        hbox:
            frame:
                style_group "codexbasic"
                xminimum 1828
                xmaximum 1828
                yminimum 790
                ymaximum 790
                bottom_padding 1
                top_padding 1
                yalign 0.75
                xalign 0.9
                vbox:
                    xalign 0.5
                    yalign 0.5
                    yfill False
                    xfill False
                    viewport:
                        scrollbars None
                        xmaximum 1816
                        xminimum 1816
                        ymaximum 774
                        yminimum 774
                        yalign 0.5
                        side_yalign .5
                        side_ymaximum 740
                        side_spacing -40
                        draggable True
                        mousewheel True
                        vbox:
                            xalign 0.5
                            yalign 0.5
                            add mapdata.map:
                                zoom 0.9

            
screen codex3():
    tag menu2
    vbox:
        hbox:
            frame:
                style_group "codexheading"
                xminimum 1824
                xmaximum 1824
                ymaximum 60
                yminimum 60
                hbox:
                    add "gui/codex/codex_heading_command.jpg"
        hbox:
            frame:
                style_group "codexbasic"
                xminimum 1828
                xmaximum 1828
                yminimum 790
                ymaximum 790
                bottom_padding 1
                top_padding 1
                yalign 0.75
                xalign 0.9
                viewport:
                    scrollbars "vertical"
                    xmaximum 1802
                    xminimum 1802
                    ymaximum 740
                    yminimum 740
                    viewport_yminimum 774
                    viewport_yoffset -16
                    yalign 0.5
                    xalign 0
                    side_yalign .5
                    side_ymaximum 740
                    side_spacing -40
                    draggable True
                    mousewheel True
                    vbox:
                        xalign 0.5
                        vbox:
                            frame:                   
                                style_group "commandbody"
                                xminimum 1762
                                xmaximum 1762
                                vbox:
                                    xalign 0
                                    hbox:
                                        xalign 0.5
                                        frame:
                                            style_group "commandoverlay"
                                            vbox:
                                                frame:
                                                    style_group "command"
                                                    background Frame("gui/stat_box_dark.png",24,24)
                                                    xminimum 425
                                                    xmaximum 425
                                                    yminimum 56
                                                    ymaximum 56
                                                    xalign 0.5
                                                    top_padding 18
                                                    vbox:
                                                        xalign 0.5
                                                        label "{i}Die Füühbar{/i}":
                                                            xalign 0.5
                                                            text_size 18
                                                frame:
                                                    style_group "governor2"
                                                    xminimum 425
                                                    xmaximum 425
                                                    yminimum 224
                                                    ymaximum 224
                                                    ypadding 8
                                                    add "side hitora hat angry":
                                                        xalign 0.5
                                                frame:
                                                    style_group "command"
                                                    xminimum 425
                                                    xmaximum 425
                                                    yminimum 108
                                                    ymaximum 108
                                                    xalign 0.5
                                                    ypadding 7
                                                    text militarycircle_hitora_name:
                                                        xalign 0.5
                                                        yalign 0.5
                                    hbox:
                                        frame:
                                            style_group "commandoverlay"
                                            vbox:
                                                frame:
                                                    style_group "command"
                                                    background Frame("gui/stat_box_dark.png",24,24)
                                                    xminimum 425
                                                    xmaximum 425
                                                    yminimum 56
                                                    ymaximum 56
                                                    xalign 0.5
                                                    top_padding 18
                                                    vbox:
                                                        xalign 0.5
                                                        label "{i}Oberkommando des Truppe{/i}":
                                                            xalign 0.5
                                                            text_size 18
                                        frame:
                                            style_group "commandoverlay"
                                            vbox:
                                                frame:
                                                    style_group "command"
                                                    background Frame("gui/stat_box_dark.png",24,24)
                                                    xminimum 425
                                                    xmaximum 425
                                                    yminimum 56
                                                    ymaximum 56
                                                    xalign 0.5
                                                    top_padding 18
                                                    vbox:
                                                        xalign 0.5
                                                        label "{i}Oberkommando der Vehrmaxt{/i}":
                                                            xalign 0.5
                                                            text_size 18
                                        frame:
                                            style_group "commandoverlay"
                                            vbox:
                                                frame:
                                                    style_group "command"
                                                    background Frame("gui/stat_box_dark.png",24,24)
                                                    xminimum 425
                                                    xmaximum 425
                                                    yminimum 56
                                                    ymaximum 56
                                                    xalign 0.5
                                                    top_padding 18
                                                    vbox:
                                                        xalign 0.5
                                                        label "{i}Oberkommando der See{/i}":
                                                            xalign 0.5
                                                            text_size 18
                                        frame:
                                            style_group "commandoverlay"
                                            vbox:
                                                frame:
                                                    style_group "command"
                                                    background Frame("gui/stat_box_dark.png",24,24)
                                                    xminimum 425
                                                    xmaximum 425
                                                    yminimum 56
                                                    ymaximum 56
                                                    xalign 0.5
                                                    top_padding 18
                                                    vbox:
                                                        xalign 0.5
                                                        label "{i}Oberkommando der Ruftwaffe{/i}":
                                                            xalign 0.5
                                                            text_size 18
                                    null height 2
                                    vbox:
                                        xalign 0
                                        yalign 0.5
                                        grid active_militarycircle_grid_x active_militarycircle_grid_y:
                                            xfill False
                                            style_group "vp"
                                            for key, value in sorted(active_militarycircle_items.items()):
                                                frame:
                                                    style_group "commandoverlay"
                                                    vbox:
                                                        frame:
                                                            style_group "governor2"
                                                            xminimum 425
                                                            xmaximum 425
                                                            yminimum 224
                                                            ymaximum 224
                                                            ypadding 8
                                                            add key:
                                                                xalign 0.5
                                                                yalign 0.5
                                                        frame:
                                                            style_group "command"
                                                            xminimum 425
                                                            xmaximum 425
                                                            yminimum 108
                                                            ymaximum 108
                                                            xalign 0.5
                                                            text value:
                                                                xalign 0.5
                                                                yalign 0.5
                                            for j in range(0, active_militarycircle_grid_num - len(active_militarycircle_items)):   
                                                frame:
                                                    style_group "commandoverlay"
                                                    vbox:
                                                        frame:
                                                            style_group "governor2"
                                                            xminimum 425
                                                            xmaximum 425
                                                            yminimum 224
                                                            ymaximum 224
                                                            ypadding 8
                                                            null
                                                        frame:
                                                            style_group "command"
                                                            xminimum 425
                                                            xmaximum 425
                                                            yminimum 108
                                                            ymaximum 108
                                                            xalign 0.5
                                                            null
                                    hbox:
                                        frame:
                                            style_group "commandoverlay"
                                            vbox:
                                                frame:
                                                    style_group "command"
                                                    background Frame("gui/stat_box_dark.png",24,24)
                                                    xminimum 1736
                                                    xmaximum 1736
                                                    yminimum 56
                                                    ymaximum 56
                                                    xalign 0.5
                                                    top_padding 18
                                                    vbox:
                                                        xalign 0.5
                                                        label "{i}Inner Circle and Administration{/i}":
                                                            xalign 0.5
                                                            text_size 18
                                                        
                                    vbox:
                                        xalign 0
                                        yalign 0.5
                                        grid active_innercircle_grid_x active_innercircle_grid_y:
                                            xfill False
                                            style_group "vp"
                                            for key, value in sorted(active_innercircle_items.items()):
                                                frame:
                                                    style_group "commandoverlay"
                                                    vbox:
                                                        frame:
                                                            style_group "governor2"
                                                            xminimum 425
                                                            xmaximum 425
                                                            yminimum 224
                                                            ymaximum 224
                                                            ypadding 8
                                                            add key:
                                                                xalign 0.5
                                                                yalign 0.5
                                                        frame:
                                                            style_group "command"
                                                            xminimum 425
                                                            xmaximum 425
                                                            yminimum 108
                                                            ymaximum 108
                                                            xalign 0.5
                                                            text value:
                                                                xalign 0.5
                                                                yalign 0.5
                                            for j in range(0, active_innercircle_grid_num - len(active_innercircle_items)):   
                                                frame:
                                                    style_group "commandoverlay"
                                                    vbox:
                                                        frame:
                                                            style_group "governor2"
                                                            xminimum 425
                                                            xmaximum 425
                                                            yminimum 224
                                                            ymaximum 224
                                                            ypadding 8
                                                            null
                                                        frame:
                                                            style_group "command"
                                                            xminimum 425
                                                            xmaximum 425
                                                            yminimum 108
                                                            ymaximum 108
                                                            xalign 0.5
                                                            null
                                    vbox:
                                        frame:
                                            style_group "commandoverlay"
                                            vbox:
                                                frame:
                                                    style_group "command"
                                                    background Frame("gui/stat_box_dark.png",24,24)
                                                    xminimum 1736
                                                    xmaximum 1736
                                                    yminimum 56
                                                    ymaximum 56
                                                    xalign 0.5
                                                    top_padding 18
                                                    vbox:
                                                        xalign 0.5
                                                        label "{i}Active Army Groups{/i}":
                                                            xalign 0.5
                                                            text_size 18
                                    vbox:
                                        xalign 0
                                        yalign 0.5
                                        grid active_armygroups_grid_x active_armygroups_grid_y:
                                            xfill False
                                            style_group "vp"
                                            for key, value in sorted(active_armygroups_items.items()):
                                                frame:
                                                    style_group "insignia"
                                                    vbox:
                                                        frame:
                                                            style_group "insignia_inner"
                                                            yminimum 150
                                                            ymaximum 150
                                                            text value:
                                                                xalign 0.5
                                                                yalign 0.5
                                            for j in range(0, active_armygroups_grid_num - len(active_armygroups_items)):   
                                                frame:
                                                    style_group "insignia"
                                                    vbox:
                                                        frame:
                                                            style_group "insignia_inner"
                                                            yminimum 150
                                                            ymaximum 150
                                                            null
                                    vbox:
                                        frame:
                                            style_group "commandoverlay"
                                            vbox:
                                                frame:
                                                    style_group "command"
                                                    background Frame("gui/stat_box_dark.png",24,24)
                                                    xminimum 1736
                                                    xmaximum 1736
                                                    yminimum 56
                                                    ymaximum 56
                                                    xalign 0.5
                                                    top_padding 18
                                                    vbox:
                                                        xalign 0.5
                                                        label "{i}Active Armies{/i}":
                                                            xalign 0.5
                                                            text_size 18
                                    vbox:
                                        xalign 0
                                        yalign 0.5
                                        grid active_armies_grid_x active_armies_grid_y:
                                            xfill False
                                            style_group "vp"
                                            for key, value in sorted(active_armies_items.items()):
                                                frame:
                                                    style_group "insignia"
                                                    vbox:
                                                        frame:
                                                            style_group "insignia_inner"
                                                            yminimum 150
                                                            ymaximum 150
                                                            text value:
                                                                xalign 0.5
                                                                yalign 0.5
                                            for j in range(0, active_armies_grid_num - len(active_armies_items)):   
                                                frame:
                                                    style_group "insignia"
                                                    vbox:
                                                        frame:
                                                            style_group "insignia_inner"
                                                            yminimum 150
                                                            ymaximum 150
                                                            null
                                    vbox:
                                        frame:
                                            style_group "commandoverlay"
                                            vbox:
                                                frame:
                                                    style_group "command"
                                                    background Frame("gui/stat_box_dark.png",24,24)
                                                    xminimum 1736
                                                    xmaximum 1736
                                                    yminimum 56
                                                    ymaximum 56
                                                    xalign 0.5
                                                    top_padding 18
                                                    vbox:
                                                        xalign 0.5
                                                        label "{i}Active Korps{/i}":
                                                            xalign 0.5
                                                            text_size 18
                                    vbox:
                                        xalign 0
                                        yalign 0.5
                                        grid active_korps_grid_x active_korps_grid_y:
                                            xfill False
                                            style_group "vp"
                                            for key, value in sorted(active_korps_items.items()):
                                                frame:
                                                    style_group "insignia"
                                                    vbox:
                                                        frame:
                                                            style_group "insignia_inner"
                                                            yminimum 150
                                                            ymaximum 150
                                                            text value:
                                                                xalign 0.5
                                                                yalign 0.5
                                            for j in range(0, active_korps_grid_num - len(active_korps_items)):   
                                                frame:
                                                    style_group "insignia"
                                                    vbox:
                                                        frame:
                                                            style_group "insignia_inner"
                                                            yminimum 150
                                                            ymaximum 150
                                                            null
                                    vbox:
                                        frame:
                                            style_group "commandoverlay"
                                            vbox:
                                                frame:
                                                    style_group "command"
                                                    background Frame("gui/stat_box_dark.png",24,24)
                                                    xminimum 1736
                                                    xmaximum 1736
                                                    yminimum 56
                                                    ymaximum 56
                                                    xalign 0.5
                                                    top_padding 18
                                                    vbox:
                                                        xalign 0.5
                                                        label "{i}Active Divisions{/i}":
                                                            xalign 0.5
                                                            text_size 18
                                    vbox:
                                        xalign 0
                                        yalign 0.5
                                        grid active_divisions_grid_x active_divisions_grid_y:
                                            xfill False
                                            style_group "vp"
                                            for key, value in sorted(active_divisions_items.items()):
                                                frame:
                                                    style_group "insignia"
                                                    vbox:
                                                        frame:
                                                            style_group "insignia_inner"
                                                            yminimum 150
                                                            ymaximum 150
                                                            text value:
                                                                xalign 0.5
                                                                yalign 0.5
                                            for j in range(0, active_divisions_grid_num - len(active_divisions_items)):
                                                frame:
                                                    style_group "insignia"
                                                    vbox:
                                                        frame:
                                                            style_group "insignia_inner"
                                                            yminimum 150
                                                            ymaximum 150
                                                            null
                                    vbox:
                                        frame:
                                            style_group "commandoverlay"
                                            vbox:
                                                frame:
                                                    style_group "command"
                                                    background Frame("gui/stat_box_dark.png",24,24)
                                                    xminimum 1736
                                                    xmaximum 1736
                                                    yminimum 56
                                                    ymaximum 56
                                                    xalign 0.5
                                                    top_padding 18
                                                    vbox:
                                                        xalign 0.5
                                                        label "{i}Active Special Formations{/i}":
                                                            xalign 0.5
                                                            text_size 18
                                    vbox:
                                        xalign 0
                                        yalign 0.5
                                        grid active_spezialformations_grid_x active_spezialformations_grid_y:
                                            xfill False
                                            style_group "vp"
                                            for key, value in sorted(active_spezialformations_items.items()):
                                                frame:
                                                    style_group "insignia"
                                                    vbox:
                                                        frame:
                                                            style_group "insignia_inner"
                                                            yminimum 150
                                                            ymaximum 150
                                                            text value:
                                                                xalign 0.5
                                                                yalign 0.5
                                            for j in range(0, active_spezialformations_grid_num - len(active_spezialformations_items)):   
                                                frame:
                                                    style_group "insignia"
                                                    vbox:
                                                        frame:
                                                            style_group "insignia_inner"
                                                            yminimum 150
                                                            ymaximum 150
                                                            null


            
screen fuuhbarmuseum():
    tag menu2
    vbox:
        hbox:
            frame:
                style_group "codexheading"
                xminimum 1824
                xmaximum 1824
                ymaximum 60
                yminimum 60
                hbox:
                    add "gui/codex/codex_heading_fuuhbarmuseum.jpg"
        hbox:
            frame:
                style_group "codexbasic"
                xminimum 1828
                xmaximum 1828
                yminimum 790
                ymaximum 790
                bottom_padding 1
                top_padding 1
                yalign 0.75
                xalign 0.9
                viewport:
                    scrollbars "vertical"
                    xmaximum 1802
                    xminimum 1802
                    ymaximum 740
                    yminimum 740
                    viewport_yminimum 774
                    viewport_yoffset -16
                    yalign 0.5
                    xalign 0
                    side_yalign .5
                    side_ymaximum 740
                    side_spacing -40
                    draggable True
                    mousewheel True
                    vbox:
                        xalign 0.5
                        vbox:
                            frame:                   
                                style_group "codexbody"
                                xminimum 1762
                                xmaximum 1762
                                yminimum 145
                                ymaximum 145
                                bottom_padding 25
                                xpadding 80
                                hbox:
                                    text "[fuuhbarmuseum_description]":
                                        text_align 0.5
                                        xalign 0.5
                        vbox:
                            frame:
                                style_group "codexsubtitle"
                                xminimum 1762
                                xmaximum 1762
                                hbox:
                                    text "Museum Floorplan"
                        vbox:
                            frame:
                                style_group "codexsubtitle"
                                xminimum 1762
                                xmaximum 1762
                                vbox:
                                    xalign 0.5
                                    yalign 0.5
                                    frame:
                                        background "museum_level1"
                                        xminimum 1664
                                        xmaximum 1664
                                        yminimum 1100
                                        ymaximum 1100
                                        vbox:
                                            yalign 0.9
                                            xalign 0.01
                                            text "Entrance Hall":
                                                size 28
                                            text "Germanian exhibits"
                                    frame:
                                        background "museum_level2"
                                        xminimum 1664
                                        xmaximum 1664
                                        yminimum 1100
                                        ymaximum 1100
                                        vbox:
                                            yalign 0.9
                                            xalign 0.01
                                            text "North Wing":
                                                size 28
                                            text "Northern exhibits"
                                    frame:
                                        background "museum_level3"
                                        xminimum 1664
                                        xmaximum 1664
                                        yminimum 1100
                                        ymaximum 1100
                                        vbox:
                                            yalign 0.9
                                            xalign 0.01
                                            text "West Wing":
                                                size 28
                                            text "Franzo / Western exhibits"
                                    frame:
                                        background "museum_level4"
                                        xminimum 1664
                                        xmaximum 1664
                                        yminimum 1100
                                        ymaximum 1100
                                        vbox:
                                            yalign 0.9
                                            xalign 0.01
                                            text "South Wing":
                                                size 28
                                            text "Southern exhibits"
                                    frame:
                                        background "museum_level5"
                                        xminimum 1664
                                        xmaximum 1664
                                        yminimum 1100
                                        ymaximum 1100
                                        vbox:
                                            yalign 0.9
                                            xalign 0.01
                                            text "Central Hall":
                                                size 28
                                            text "Britannian / Grecian exhibits"
                                    frame:
                                        background "museum_level6"
                                        xminimum 1664
                                        xmaximum 1664
                                        yminimum 1100
                                        ymaximum 1100
                                        vbox:
                                            yalign 0.9
                                            xalign 0.01
                                            text "East Wing":
                                                size 28
                                            text "Sovian / Eastern exhibits"
                                    frame:
                                        background "museum_level7"
                                        xminimum 1664
                                        xmaximum 1664
                                        yminimum 1100
                                        ymaximum 1100
                                        vbox:
                                            yalign 0.9
                                            xalign 0.01
                                            text "Outer Hall":
                                                size 28
                                            text "Oriasian exhibits"
                                    frame:
                                        background "museum_levelb"
                                        xminimum 1664
                                        xmaximum 1664
                                        yminimum 1100
                                        ymaximum 1100
                                        vbox:
                                            yalign 0.9
                                            xalign 0.01
                                            text "Basement":
                                                size 28
                                            text "Unpopular exhibits"
                                    null height 45
                        vbox:
                            frame:
                                style_group "codexsubtitle"
                                xminimum 1762
                                xmaximum 1762
                                hbox:
                                    text "Captured Exhibits Information"
                        vbox:
                            xalign 0
                            yalign 0.5
                            grid active_fuuhbarmuseum_grid_x active_fuuhbarmuseum_grid_y:
                                xfill False
                                style_group "vp"
                                for key, value in sorted(active_fuuhbarmuseum_items.items()):
                                    frame:
                                        style_group "fuuhbarmuseum"
                                        xminimum 576
                                        xmaximum 576
                                        hbox:
                                            frame:
                                                style_group "fuuhbarmuseum_inner"
                                                xminimum 188
                                                xmaximum 188
                                                yminimum 188
                                                ymaximum 188
                                                add key:
                                                    xalign 0.5
                                                    yalign 0.5
                                            vbox:
                                                frame:
                                                    style_group "fuuhbarmuseum_inner"
                                                    xminimum 387
                                                    xmaximum 387
                                                    yminimum 50
                                                    ymaximum 50
                                                    top_padding 13
                                                    text value[0]:
                                                        xalign 0.5
                                                        yalign 0.5
                                                        size 18
                                                frame:
                                                    style_group "fuuhbarmuseum_inner"
                                                    xminimum 387
                                                    xmaximum 387
                                                    yminimum 138
                                                    ymaximum 138
                                                    text value[1]:
                                                        xalign 0.5
                                                        yalign 0.5
                                for j in range(0, active_fuuhbarmuseum_grid_num - len(active_fuuhbarmuseum_items)):   
                                    frame:
                                        style_group "fuuhbarmuseum"
                                        xminimum 576
                                        xmaximum 576
                                        hbox:
                                            frame:
                                                style_group "fuuhbarmuseum_inner"
                                                xminimum 188
                                                xmaximum 188
                                                yminimum 188
                                                ymaximum 188
                                                add "captured_x":
                                                    xalign 0.5
                                                    yalign 0.5
                                            vbox:
                                                frame:
                                                    style_group "fuuhbarmuseum_inner"
                                                    xminimum 387
                                                    xmaximum 387
                                                    yminimum 50
                                                    ymaximum 50
                                                    top_padding 13
                                                    text "???????????":
                                                        xalign 0.5
                                                        yalign 0.5
                                                        size 18
                                                frame:
                                                    style_group "fuuhbarmuseum_inner"
                                                    xminimum 387
                                                    xmaximum 387
                                                    yminimum 138
                                                    ymaximum 138
                                                    text "????????? ??? ????":
                                                        xalign 0.5
                                                        yalign 0.5
                                                    
                                                    
                                                    
