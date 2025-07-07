
########################################################################################################################
#### MISSION SCREENS ##################################################################################################
########################################################################################################################
screen qlog():
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
            yminimum 570
            ymaximum 570
            bottom_padding 6
            top_padding 6
            yalign 0.85
            xalign 0.51
            vbox:
                xalign 0.5
                yalign 0.0
                yfill False
                xfill False
                vbox:
                    xalign 0.5
                    frame:
                        style_group "governor2"
                        xminimum 1490
                        xmaximum 1490
                        yminimum 100
                        ymaximum 100
                        hbox:
                            style_group "governor"
                            xalign 0.5
                            yalign .5
                            hbox:
                                style_group "missionlog"
                                xalign 0.5
                                yalign .5
                                for i in log.displayedtabs():
                                    textbutton i action [SetField(log, "tvar", i), log.newtab ] focus_mask True hover_sound "se/hover.ogg" activate_sound "se/section.ogg" at mapicon_eff
                    hbox:
                        vbox:
                            frame:
                                style_group "governor2"
                                xminimum 660
                                xmaximum 660
                                yminimum 20
                                ymaximum 20
                                xpadding 20
                                bottom_padding 10
                                top_padding 15
                                hbox:
                                    style_group "governor"
                                    xalign 0.5
                                    yalign .5
                                    vbox:
                                        null height 5
                                        text "Mission Select"
                            frame:
                                style_group "governor2"
                                xminimum 660
                                xmaximum 660
                                yminimum 460
                                ymaximum 460
                                xpadding 5
                                bottom_padding 20
                                top_padding 20
                                vbox:
                                    xalign 0
                                    yalign 0.5
                                    yfill False
                                    xfill False
                                    viewport:
                                        scrollbars "vertical"
                                        xmaximum 640
                                        xminimum 640
                                        ymaximum 411
                                        yminimum 411
                                        viewport_yminimum 444
                                        viewport_yoffset -16
                                        yalign 0.5
                                        side_yalign .5
                                        side_spacing -32
                                        draggable False
                                        mousewheel True
                                        vbox:
                                            xalign 0
                                            yalign 0.5
                                            for i in log.activetab():
                                                vbox:
                                                    style_group "missiontype"
                                                    xalign 0
                                                    yalign 0.5
                                                    textbutton i.title() action SetField(log, "qvar", i) focus_mask True hover_sound "se/hover.ogg" activate_sound "se/section.ogg" at mapicon_eff
                                                null height 1
                        vbox:
                            frame:
                                style_group "governor2"
                                xminimum 830
                                xmaximum 830
                                yminimum 20
                                ymaximum 20
                                xpadding 20
                                bottom_padding 10
                                top_padding 15
                                hbox:
                                    style_group "governor"
                                    xalign 0.5
                                    yalign .5
                                    vbox:
                                        null height 5
                                        text "Description"
                            frame:
                                style_group "governor2"
                                xminimum 830
                                xmaximum 830
                                yminimum 215
                                ymaximum 215
                                xpadding 40
                                bottom_padding 10
                                top_padding 15
                                hbox:
                                    style_group "governor"
                                    xalign 0.5
                                    yalign 0.5
                                    vbox:
                                        xalign 0.5
                                        yalign 0.5
                                        text log.activedescription() size 19 text_align 0.5
                            
                            hbox:
                                vbox:
                                    frame:
                                        style_group "governor2"
                                        xminimum 214
                                        xmaximum 214
                                        yminimum 20
                                        ymaximum 20
                                        xpadding 20
                                        bottom_padding 10
                                        top_padding 15
                                        hbox:
                                            style_group "governor"
                                            xalign 0.5
                                            yalign .5
                                            vbox:
                                                null height 5
                                                text "Terrain"
                                    frame:
                                        style_group "governor2"
                                        xminimum 214
                                        xmaximum 214
                                        yminimum 174
                                        ymaximum 174
                                        hbox:
                                            style_group "governor"
                                            xalign 0.5
                                            yalign .1
                                            vbox:
                                                for i in log.activeprogress():
                                                    add formatgoal(i)
                                vbox:
                                    frame:
                                        style_group "governor2"
                                        xminimum 616
                                        xmaximum 616
                                        yminimum 20
                                        ymaximum 20
                                        xpadding 20
                                        bottom_padding 10
                                        top_padding 15
                                        hbox:
                                            style_group "governor"
                                            xalign 0.5
                                            yalign .5
                                            vbox:
                                                null height 5
                                                text "Status"
                                    frame:
                                        style_group "governor2"
                                        xminimum 616
                                        xmaximum 616
                                        yminimum 174
                                        ymaximum 174
                                        xpadding 20
                                        bottom_padding 10
                                        top_padding 15
                                        hbox:
                                            style_group "governor"
                                            xalign 0.5
                                            yalign .5
                                            vbox:
                                                if log.activeimage():
                                                    add log.activeimage()
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
        add "gui/overlay_title_missionlog.png"
    hbox:
        style_group "bonus"
        xalign .9
        yalign .095
        imagebutton idle "yesno_no_small_idle" hover "yesno_no_small_hover" action Hide("qlog") focus_mask True hover_sound "se/hover.ogg" activate_sound "se/click.ogg" at mapicon_eff
    
screen tracker():
    fixed:
        align (1.0, 0.0)
        maximum (200,150)
        if log.tracked():
            textbutton "X" background None text_color "#000000" text_hover_color "#CCCCCC" text_size 12 align (1.0, 0.0) action [ log.stoptracking, Hide(log.tracker()), Show(log.tracker()) ]
        vbox:
            xfill True
            spacing 3
            if log.tracked():                
                text log.trackedtitle() color "#000000" size 18
                for i in log.trackerprogress():
                    text formatgoal(i) color "#000000" size 12

image notification:
    alpha 0.0
    Text(log.message(), color="#fff", outlines=[(2, "#000000", 0, 0)], text_align=0.5, font="font/hussar.otf")
    align (0.98, 0.02)
    linear 0.5 alpha 1.0
    pause 4.0
    linear 0.5 alpha 0.0

init python:
    def formatgoal(goal):
        str = ''
        if not goal.hidden():                                
            if goal.completed():
                str = "{0}".format(goal.description())
            elif goal.fetch():
                str = "{0}".format(goal.description())
            elif goal.failed():
                str = "{0}".format(goal.description())
            else:                                    
                str = "{0}".format(goal.description())
        else:
            if goal.required():
                str = "- ?????"
        return str                            
        
                     