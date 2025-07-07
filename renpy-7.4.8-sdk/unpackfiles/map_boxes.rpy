
########################################################################################################################
#### MAP UPDATES ######################################################################################################
########################################################################################################################
screen map_update():
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
            style_group "governor2"
            xminimum 1231
            xmaximum 1231
            yminimum 399
            ymaximum 399
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
                    xmaximum 1211
                    xminimum 1211
                    ymaximum 351
                    yminimum 351
                    viewport_yminimum 380
                    viewport_yoffset -15
                    yalign 0.5
                    side_yalign .5
                    side_ymaximum 350
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
                            xminimum 1181
                            xmaximum 1181
                            yminimum 40
                            ymaximum 40
                            xpadding 20
                            bottom_padding 10
                            top_padding 15
                            hbox:
                                style_group "governor"
                                xalign 0.5
                                yalign .5
                                vbox:
                                    null height 5
                                    text "{size=30}[map_update_title]{/size}"
                        frame:
                            style_group "governor2"
                            xminimum 1181
                            xmaximum 1181
                            yminimum 30
                            ymaximum 30
                            xpadding 20
                            bottom_padding 10
                            top_padding 25
                            hbox:
                                style_group "governor"
                                xalign 0.5
                                yalign .5
                                text "[map_update_subtitle]"
                        frame:
                            style_group "governor2"
                            xminimum 1181
                            xmaximum 1181
                            yminimum 200
                            ymaximum 200
                            xpadding 40
                            ypadding 40
                            hbox:
                                style_group "governor"
                                xalign 0.5
                                yalign .5
                                vbox:
                                    text "[map_update_description]":
                                        xalign 0.5
                                        text_align 0.5
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
        add "gui/overlay_title_update.png"
    hbox:
        style_group "bonus"
        xalign .827
        yalign .227
        imagebutton idle "yesno_no_small_idle" hover "yesno_no_small_hover" action [SetVariable("map_update_happen", False), Hide("map_update", False)] focus_mask True hover_sound "se/hover.ogg" activate_sound "se/click.ogg" at mapicon_eff

########################################################################################################################
#### MAP INVASION BOX ################################################################################################
########################################################################################################################
screen qbox():
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
            style_group "codexbasic"
            xminimum 1231
            xmaximum 1231
            yminimum 399
            ymaximum 399
            bottom_padding 1
            top_padding 1
            yalign 0.85
            xalign 0.51
            vbox:
                xalign 0.5
                yalign 0.5
                yfill False
                xfill False
                frame:
                    style_group "codexsubtitle"
                    xminimum 1221
                    xmaximum 1221
                    hbox:
                        text "[q_title]"
                hbox:
                    frame:
                        style_group "governor2"
                        xminimum 610
                        xmaximum 610
                        yminimum 315
                        ymaximum 315
                        hbox:
                            style_group "governor"
                            xalign 0.5
                            yalign 0.5
                            vbox:
                                add "gui/mission_image.jpg"
                    vbox:
                        frame:
                            style_group "codexbody"
                            xminimum 610
                            xmaximum 610
                            yminimum 225
                            ymaximum 225
                            xpadding 40
                            ypadding 30
                            xalign 0.5
                            yalign 0.5
                            text "[q_description]":
                                xalign 0.5
                                yalign 0.55
                                text_align 0.5
                        frame:
                            style_group "codexbasic"
                            xminimum 610
                            xmaximum 610
                            hbox:
                                style_group "missionbutton"
                                xalign 0.5
                                yalign 0.5
                                textbutton "Begin Mission" action [Hide("qbox"), Hide("unlocktown_tooltip"), Hide("siege_tooltip"), Jump(mapcontinue)] focus_mask True hover_sound "se/hover.ogg" activate_sound "se/click.ogg" at mapicon_eff
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
        if q_type == 1:
            add "gui/overlay_title_mainmission.png"
        elif q_type == 2:
            add "gui/overlay_title_sidemission.png"
        else:
            null height 0
    hbox:
        style_group "bonus"
        xalign .828
        yalign .227
        imagebutton idle "yesno_no_small_idle" hover "yesno_no_small_hover" action Hide("qbox", False) focus_mask True hover_sound "se/hover.ogg" activate_sound "se/click.ogg" at mapicon_eff

########################################################################################################################
#### MAP WONDERS #####################################################################################################
########################################################################################################################
screen wonder():
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
                            xpadding 20
                            bottom_padding 10
                            top_padding 15
                            hbox:
                                style_group "governor"
                                xalign 0.5
                                yalign .5
                                vbox:
                                    null height 5
                                    text "{size=30}[wonder_name]{/size}"
                        frame:
                            style_group "governor2"
                            xminimum 1450
                            xmaximum 1450
                            yminimum 30
                            ymaximum 30
                            bottom_padding 5
                            top_padding 17
                            hbox:
                                style_group "governor"
                                xalign 0.5
                                yalign 0.5
                                text "{color=#FF9915}W O R L D   W O N D E R{/color}"
                        frame:
                            style_group "governor2"
                            xminimum 1450
                            xmaximum 1450
                            yminimum 300
                            ymaximum 300
                            xpadding 5
                            ypadding 7
                            hbox:
                                style_group "governor"
                                xalign 0.5
                                yalign .5
                                add "[wonder_image]"
                        frame:
                            style_group "governor2"
                            xminimum 1450
                            xmaximum 1450
                            yminimum 30
                            ymaximum 30
                            top_padding 15
                            hbox:
                                style_group "governor"
                                xalign 0.5
                                yalign 0.5
                                text "[wonder_location]"        
                        frame:
                            style_group "governor2"
                            xminimum 1450
                            xmaximum 1450
                            yminimum 200
                            ymaximum 200
                            xpadding 40
                            top_padding 40
                            bottom_padding 30
                            hbox:
                                style_group "governor"
                                xalign 0.5
                                yalign 0.5
                                text "[wonder_description]":
                                    text_align 0.5
                        frame:
                            style_group "governor2"
                            xminimum 1450
                            xmaximum 1450
                            yminimum 100
                            ymaximum 100
                            xpadding 40
                            top_padding 40
                            bottom_padding 30
                            hbox:
                                style_group "governor"
                                xalign 0.5
                                yalign 0.5
                                text "[wonder_condition]":
                                    text_align 0.5
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
        add "gui/overlay_title_wonder.png"
    hbox:
        style_group "bonus"
        xalign .9
        yalign .093
        imagebutton idle "yesno_no_small_idle" hover "yesno_no_small_hover" action Hide("wonder", False) focus_mask True hover_sound "se/hover.ogg" activate_sound "se/click.ogg" at mapicon_eff
    
########################################################################################################################
#### MAP ALLEGIANCES ##################################################################################################
########################################################################################################################
screen map1allegiances():
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
            xminimum 1490
            xmaximum 1490
            yminimum 670
            ymaximum 670
            bottom_padding 6
            top_padding 6
            yalign 0.85
            xalign 0.51
            vbox:
                xalign 0.5
                yalign 0.0
                yfill False
                xfill False
                frame:
                    style_group "governor2"
                    xminimum 1485
                    xmaximum 1485
                    yminimum 30
                    ymaximum 30
                    xpadding 20
                    bottom_padding 10
                    top_padding 15
                    hbox:
                        style_group "governor"
                        xalign 0.5
                        yalign .5
                        vbox:
                            null height 5
                            text "{size=30}[allegiances_name]{/size}"
                hbox:
                    frame:
                        style_group "governor2"
                        xminimum 495
                        xmaximum 495
                        yminimum 20
                        ymaximum 20
                        xpadding 20
                        bottom_padding -3
                        top_padding 10
                        hbox:
                            style_group "governor"
                            xalign 0.5
                            yalign 0.5
                            text "Location":
                                xalign 0.5
                                yalign 0.5
                    frame:
                        style_group "governor2"
                        xminimum 495
                        xmaximum 495
                        yminimum 20
                        ymaximum 20
                        xpadding 20
                        bottom_padding -3
                        top_padding 10
                        hbox:
                            style_group "governor"
                            xalign 0.5
                            yalign 0.5
                            text "Official Flag":
                                xalign 0.5
                                yalign 0.5
                    frame:
                        style_group "governor2"
                        xminimum 495
                        xmaximum 495
                        yminimum 20
                        ymaximum 20
                        xpadding 20
                        bottom_padding -3
                        top_padding 10
                        hbox:
                            style_group "governor"
                            xalign 0.5
                            yalign 0.5
                            text "Course of Action":
                                xalign 0.5
                                yalign 0.5
                hbox:
                    style_group "governor"
                    vbox:
                        frame:
                            style_group "governor2"
                            xminimum 495
                            xmaximum 495
                            yminimum 120
                            ymaximum 120
                            top_padding 20
                            bottom_padding 5
                            xpadding 15
                            text "[allegiances_description]":
                                yalign 0.5
                                xalign 0.5
                                text_align 0.5
                        frame:
                            style_group "governor2"
                            xminimum 495
                            xmaximum 495
                            yminimum 20
                            ymaximum 20
                            xpadding 20
                            bottom_padding -3
                            top_padding 10
                            hbox:
                                style_group "governor"
                                xalign 0.5
                                yalign .5
                                text "Country Information":
                                    xalign 0.5
                                    yalign .5
                        frame:
                            style_group "governor2"
                            xminimum 495
                            xmaximum 495
                            yminimum 142
                            ymaximum 142
                            hbox:
                                vbox:
                                    frame:
                                        style_group "main_stats"
                                        xminimum 201
                                        xmaximum 201
                                        yminimum 54
                                        ymaximum 54
                                        top_padding 8
                                        bottom_padding 2
                                        text "Power:":
                                            xalign 0.5
                                            yalign 0.8
                                    frame:
                                        style_group "main_stats"
                                        xminimum 201
                                        xmaximum 201
                                        yminimum 54
                                        ymaximum 54
                                        top_padding 8
                                        bottom_padding 2
                                        text "Hostility:":
                                            xalign 0.5
                                            yalign 0.8
                                    frame:
                                        style_group "main_stats"
                                        xminimum 201
                                        xmaximum 201
                                        yminimum 54
                                        ymaximum 54
                                        top_padding 8
                                        bottom_padding 2
                                        text "Allegiance:":
                                            xalign 0.5
                                            yalign 0.8
                                vbox:
                                    frame:
                                        style_group "town_stats"
                                        xminimum 281
                                        xmaximum 281
                                        yminimum 54
                                        ymaximum 54
                                        top_padding 7
                                        bottom_padding 1
                                        text "[allegiances_power]":
                                            xalign 0.5
                                            yalign 0.8
                                    frame:
                                        style_group "town_stats"
                                        xminimum 281
                                        xmaximum 281
                                        yminimum 54
                                        ymaximum 54
                                        top_padding 7
                                        bottom_padding 1
                                        text "[allegiances_hostility]":
                                            xalign 0.5
                                            yalign 0.8
                                    frame:
                                        style_group "town_stats"
                                        xminimum 281
                                        xmaximum 281
                                        yminimum 54
                                        ymaximum 54
                                        top_padding 7
                                        bottom_padding 1
                                        text "[allegiances_allegiance]":
                                            xalign 0.5
                                            yalign 0.8
                    vbox:
                        xminimum 495
                        xmaximum 495
                        yminimum 310
                        ymaximum 310
                        frame:
                            style_group "governor2"
                            xminimum 495
                            xmaximum 495
                            yminimum 185
                            ymaximum 185
                            xpadding 0
                            top_padding 10
                            bottom_padding 0
                            text "[allegiances_flag2]":
                                xalign 0.5
                                yalign 0.5
                        frame:
                            style_group "governor2"
                            xminimum 495
                            xmaximum 495
                            yminimum 55
                            ymaximum 55
                            top_padding 11
                            bottom_padding 0
                            text "'[allegiances_motto]'":
                                xalign 0.5
                                yalign 0.5
                                size 14
                    vbox:
                        xminimum 495
                        xmaximum 495
                        yminimum 341
                        ymaximum 341
                        frame:
                            style_group "governor2"
                            xminimum 495
                            xmaximum 495
                            yminimum 341
                            ymaximum 341
                            ypadding 10
                            xpadding 20
                            text "[allegiances_coa]":
                                xalign 0.5
                                yalign 0.55
                                text_align 0.5
                frame:
                    style_group "governor2"
                    xminimum 1485
                    xmaximum 1485
                    yminimum 190
                    ymaximum 190
                    xpadding 19
                    bottom_padding 18
                    top_padding 20
                    viewport:
                        scrollbars "vertical"
                        xmaximum 1480
                        xminimum 1480
                        ymaximum 141
                        yminimum 141
                        viewport_yminimum 170
                        viewport_yoffset -15
                        yalign 0.5
                        side_yalign .5
                        side_ymaximum 200
                        side_spacing -20
                        draggable False
                        mousewheel True
                        vbox:
                            xalign 0.5
                            grid active_allegiances_grid_x active_allegiances_grid_y:
                                style_group "allegiancestext"
                                for key, value in sorted(active_allegiances_items.items()):
                                    vbox:
                                        imagebutton action [
                                                SetVariable("allegiances_motto", value[0]), 
                                                SetVariable("allegiances_flag2", value[2]), 
                                                SetVariable("allegiances_description", value[3]), 
                                                SetVariable("allegiances_name", value[4]), 
                                                SetVariable("allegiances_coa", value[5]), 
                                                SetVariable("allegiances_hostility", value[6]), 
                                                SetVariable("allegiances_power", value[7]), 
                                                SetVariable("allegiances_allegiance", value[8])
                                        ] idle ("flag_" + value[9].lower().replace(" ", "").replace(".", "") + "_idle") hover ("flag_"+ value[9].lower().replace(" ", "").replace(".", "") + "_hover") focus_mask True hover_sound "se/hover.ogg" activate_sound "se/section.ogg" at mapicon_eff
                                        text value[9]
                                for i in range(0, active_allegiances_grid_num - len(active_allegiances_items)):  
                                    vbox:
                                        null width 100
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
        add "gui/overlay_title_factions.png"
    hbox:
        style_group "bonus"
        xalign .9
        yalign .093
        imagebutton idle "yesno_no_small_idle" hover "yesno_no_small_hover" action [SetVariable("allegiances_motto", germania_motto), SetVariable("allegiances_flag2", germania_flag2), SetVariable("allegiances_description", germania_description), SetVariable("allegiances_name", germania_name), SetVariable("allegiances_coa", germania_coa), SetVariable("allegiances_hostility", germania_hostility), SetVariable("allegiances_power", germania_power), SetVariable("allegiances_allegiance", germania_allegiance), Hide("map1allegiances")] focus_mask True hover_sound "se/hover.ogg" activate_sound "se/click.ogg" at mapicon_eff
    
########################################################################################################################
#### MAP TOWN BOX #####################################################################################################
########################################################################################################################
screen maptown():
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
                                    text "{size=30}" + maptown_name + "{/size}"
                        frame:
                            style_group "governor2"
                            xminimum 1450
                            xmaximum 1450
                            yminimum 30
                            ymaximum 30
                            bottom_padding 5
                            top_padding 17
                            hbox:
                                style_group "governor"
                                xalign 0.5
                                yalign 0.5
                                text "{color=#FF9915}" + maptown_size + "{/color}"
                        hbox:
                            frame:
                                style_group "governor2"
                                xminimum 790
                                xmaximum 790
                                yminimum 30
                                ymaximum 30
                                top_padding 15
                                hbox:
                                    style_group "governor"
                                    xalign 0.5
                                    yalign 0.7
                                    text "Governor Information"
                            frame:
                                style_group "governor2"
                                xminimum 660
                                xmaximum 660
                                yminimum 30
                                ymaximum 30
                                top_padding 15
                                hbox:
                                    style_group "governor"
                                    xalign 0.5
                                    yalign 0.7
                                    text "City Information"
                        hbox:
                            frame:
                                style_group "governor2"
                                xminimum 790
                                xmaximum 790
                                yminimum 210
                                ymaximum 210
                                hbox:
                                    style_group "governor"
                                    vbox:
                                        frame:
                                            style_group "governor2"
                                            xminimum 350
                                            xmaximum 350
                                            yminimum 210
                                            ymaximum 210
                                            top_padding 5
                                            bottom_padding -5
                                            right_padding 5
                                            text maptown_governor_pic
                                    vbox:
                                        frame:
                                            style_group "main_stats"
                                            xminimum 175
                                            xmaximum 175
                                            yminimum 56
                                            ymaximum 56
                                            top_padding 12
                                            text "Governor:":
                                                xalign 0.5
                                                yalign 0.5
                                        frame:
                                            style_group "main_stats"
                                            xminimum 175
                                            xmaximum 175
                                            yminimum 56
                                            ymaximum 56
                                            top_padding 12
                                            text "Command:":
                                                xalign 0.5
                                                yalign 0.5
                                        frame:
                                            style_group "main_stats"
                                            xminimum 175
                                            xmaximum 175
                                            yminimum 56
                                            ymaximum 56
                                            top_padding 12
                                            text "Management:":
                                                xalign 0.5
                                                yalign 0.5
                                        frame:
                                            style_group "main_stats"
                                            xminimum 175
                                            xmaximum 175
                                            yminimum 56
                                            ymaximum 56
                                            top_padding 12
                                            text "Influence:":
                                                xalign 0.5
                                                yalign 0.5
                                    vbox:
                                        frame:
                                            style_group "town_stats"
                                            xminimum 237
                                            xmaximum 237
                                            yminimum 56
                                            ymaximum 56
                                            top_padding 15
                                            text maptown_governor:
                                                xalign 0.5
                                                yalign 0.7
                                        frame:
                                            style_group "town_stats"
                                            xminimum 237
                                            xmaximum 237
                                            yminimum 56
                                            ymaximum 56
                                            ypadding -17
                                            text maptown_command:
                                                xalign 0.5
                                                yalign 0.4
                                        frame:
                                            style_group "town_stats"
                                            xminimum 237
                                            xmaximum 237
                                            yminimum 56
                                            ymaximum 56
                                            ypadding -6
                                            text maptown_management:
                                                xalign 0.5
                                                yalign 0.5
                                        frame:
                                            style_group "town_stats"
                                            xminimum 237
                                            xmaximum 237
                                            yminimum 56
                                            ymaximum 56
                                            ypadding -6
                                            text maptown_influence:
                                                xalign 0.5
                                                yalign 0.5
                            vbox:
                                frame:
                                    style_group "governor2"
                                    xminimum 660
                                    xmaximum 660
                                    yminimum 200
                                    ymaximum 200
                                    xpadding 5
                                    bottom_padding 6
                                    top_padding 6
                                    vbox:
                                        xalign 0.5
                                        hbox:
                                            style_group "governor"
                                            xalign 0.5
                                            vbox:
                                                frame:
                                                    style_group "governor2"
                                                    xminimum 240
                                                    xmaximum 240
                                                    yminimum 218
                                                    ymaximum 218
                                                    add "[maptown_profileimg]icon"
                                            vbox:
                                                frame:
                                                    style_group "main_stats"
                                                    xminimum 175
                                                    xmaximum 175
                                                    yminimum 56
                                                    ymaximum 56
                                                    top_padding 12
                                                    text "Population:":
                                                        xalign 0.5
                                                        yalign 0.5
                                                frame:
                                                    style_group "main_stats"
                                                    xminimum 175
                                                    xmaximum 175
                                                    yminimum 56
                                                    ymaximum 56
                                                    top_padding 12
                                                    text "Allegiance:":
                                                        xalign 0.5
                                                        yalign 0.5
                                                frame:
                                                    style_group "main_stats"
                                                    xminimum 175
                                                    xmaximum 175
                                                    yminimum 56
                                                    ymaximum 56
                                                    top_padding 12
                                                    text "Morale:":
                                                        xalign 0.5
                                                        yalign 0.5
                                                frame:
                                                    style_group "main_stats"
                                                    xminimum 175
                                                    xmaximum 175
                                                    yminimum 56
                                                    ymaximum 56
                                                    top_padding 12
                                                    text "Hostility:":
                                                        xalign 0.5
                                                        yalign 0.5
                                            vbox:
                                                frame:
                                                    style_group "town_stats"
                                                    xminimum 220
                                                    xmaximum 220
                                                    yminimum 56
                                                    ymaximum 56
                                                    top_padding 16
                                                    text str(maptown_population):
                                                        xalign 0.5
                                                        yalign 0.8
                                                frame:
                                                    style_group "town_stats"
                                                    xminimum 220
                                                    xmaximum 220
                                                    yminimum 56
                                                    ymaximum 56
                                                    top_padding 15
                                                    text maptown_alignment:
                                                        xalign 0.5
                                                        yalign 0.8
                                                frame:
                                                    style_group "town_stats"
                                                    xminimum 220
                                                    xmaximum 220
                                                    yminimum 56
                                                    ymaximum 56
                                                    top_padding 15
                                                    if maptown_publicorder > 0:
                                                        text "{color=12FF00}+" + str(maptown_publicorder) + "{/color}":
                                                            xalign 0.5
                                                            yalign 0.8
                                                    else:
                                                        text "{color=FF0000}" + str(maptown_publicorder) + "{/color}":
                                                            xalign 0.5
                                                            yalign 0.8
                                                frame:
                                                    style_group "town_stats"
                                                    xminimum 220
                                                    xmaximum 220
                                                    yminimum 56
                                                    ymaximum 56
                                                    top_padding 15
                                                    text maptown_hostility:
                                                        xalign 0.5
                                                        yalign 0.8
                                                        
                        hbox:
                            vbox:
                                frame:
                                    style_group "governor2"
                                    xminimum 1450
                                    xmaximum 1450
                                    yminimum 30
                                    ymaximum 30
                                    top_padding 15
                                    hbox:
                                        style_group "governor"
                                        xalign 0.5
                                        yalign 0.7
                                        text "Active Garrison"
                                vbox:
                                    xalign 0.5
                                    yalign 0.5
                                    xfill False
                                    style_group "vp"
                                    frame:
                                        style_group "fuuhbarmuseum"
                                        xminimum 1450
                                        xmaximum 1450
                                        yminimum 125
                                        ymaximum 125
                                        vbox:
                                            xalign 0.5
                                            hbox:
                                                xalign 0.5
                                                for g in maptown_martial:
                                                    frame:
                                                        style_group "main_stats"
                                                        xminimum 135
                                                        xmaximum 135
                                                        yminimum 125
                                                        ymaximum 125
                                                        xpadding 4
                                                        ypadding 4
                                                        add g:
                                                            xalign 0.5
                                                            yalign 0.5
                                                        
                        hbox:
                            vbox:
                                frame:
                                    style_group "governor2"
                                    xminimum 791
                                    xmaximum 791
                                    yminimum 30
                                    ymaximum 30
                                    top_padding 15
                                    hbox:
                                        style_group "governor"
                                        xalign 0.5
                                        yalign 0.7
                                        text "Local Businesses"
                                vbox:
                                    xalign 0
                                    yalign 0.5
                                    xfill False
                                    style_group "vp"
                                    frame:
                                        style_group "fuuhbarmuseum"
                                        xminimum 790
                                        xmaximum 790
                                        yminimum 540
                                        ymaximum 540
                                        hbox:
                                            vbox:
                                                for d in sorted(maptown_company_img):
                                                    frame:
                                                        style_group "fuuhbarmuseum_inner"
                                                        xminimum 180
                                                        xmaximum 180
                                                        yminimum 180
                                                        ymaximum 180
                                                        xpadding 0
                                                        add d:
                                                            xalign 0.5
                                                            yalign 0.5
                                            vbox:
                                                for key, value in sorted(maptown_company_text.items()):
                                                    frame:
                                                        style_group "fuuhbarmuseum_inner"
                                                        xminimum 600
                                                        xmaximum 600
                                                        yminimum 180
                                                        ymaximum 180
                                                        xpadding 30
                                                        text "{size=20}[key]{/size}\n\n[value]":
                                                            xalign 0.5
                                                            yalign 0.5
                                                                     
                            vbox:
                                frame:
                                    style_group "governor2"
                                    xminimum 660
                                    xmaximum 660
                                    yminimum 30
                                    ymaximum 30
                                    top_padding 15
                                    hbox:
                                        style_group "governor"
                                        xalign 0.5
                                        yalign 0.7
                                        text "Economic Information"
                                vbox:
                                    xalign 0
                                    yalign 0.5
                                    xfill False
                                    style_group "vp"
                                    frame:
                                        style_group "fuuhbarmuseum"
                                        xminimum 660
                                        xmaximum 660
                                        yminimum 546
                                        ymaximum 546
                                        hbox:
                                            vbox:
                                                for key, value in economic_areas.items():
                                                    frame:
                                                        style_group "main_stats"
                                                        xminimum 308
                                                        xmaximum 308
                                                        yminimum 68
                                                        ymaximum 68
                                                        ypadding 6
                                                        xpadding 5
                                                        hbox:
                                                            add key
                                                            null width 30
                                                            vbox:
                                                                null height 20
                                                                text value:
                                                                    xalign 0.5
                                                                    yalign 0.7
                                                                    size 20
                                            vbox:
                                                frame:
                                                    style_group "town_stats"
                                                    xminimum 340
                                                    xmaximum 340
                                                    yminimum 77
                                                    ymaximum 77
                                                    text maptown_farming_worth:
                                                        xalign 0.5
                                                        yalign 0.7
                                                        size 20
                                                frame:
                                                    style_group "town_stats"
                                                    xminimum 340
                                                    xmaximum 340
                                                    yminimum 77
                                                    ymaximum 77
                                                    text maptown_mining_worth:
                                                        xalign 0.5
                                                        yalign 0.7
                                                        size 20
                                                frame:
                                                    style_group "town_stats"
                                                    xminimum 340
                                                    xmaximum 340
                                                    yminimum 77
                                                    ymaximum 77
                                                    text maptown_industry_worth:
                                                        xalign 0.5
                                                        yalign 0.7
                                                        size 20
                                                frame:
                                                    style_group "town_stats"
                                                    xminimum 340
                                                    xmaximum 340
                                                    yminimum 77
                                                    ymaximum 77
                                                    text maptown_trade_worth:
                                                        xalign 0.5
                                                        yalign 0.7
                                                        size 20
                                                frame:
                                                    style_group "town_stats"
                                                    xminimum 340
                                                    xmaximum 340
                                                    yminimum 77
                                                    ymaximum 77
                                                    text maptown_entertainment_worth:
                                                        xalign 0.5
                                                        yalign 0.7
                                                        size 20
                                                frame:
                                                    style_group "town_stats"
                                                    xminimum 340
                                                    xmaximum 340
                                                    yminimum 77
                                                    ymaximum 77
                                                    text maptown_military_worth:
                                                        xalign 0.5
                                                        yalign 0.7
                                                        size 20
                                                frame:
                                                    style_group "town_stats"
                                                    xminimum 340
                                                    xmaximum 340
                                                    yminimum 77
                                                    ymaximum 77
                                                    text maptown_corruption_worth:
                                                        xalign 0.5
                                                        yalign 0.7
                                                        size 20
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
        add "gui/overlay_title_city.png"
    hbox:
        style_group "bonus"
        xalign .9
        yalign .093
        imagebutton idle "yesno_no_small_idle" hover "yesno_no_small_hover" action [Hide("maptown", False)] focus_mask True hover_sound "se/hover.ogg" activate_sound "se/click.ogg" at mapicon_eff
    
    
