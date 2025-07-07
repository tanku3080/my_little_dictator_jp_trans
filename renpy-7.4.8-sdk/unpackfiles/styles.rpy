
########################################################################################################################
#### STYLES ############################################################################################################
########################################################################################################################
init-5:
    style pref_slider:
        xminimum 400
        xmaximum 400
        ymaximum 30
        xalign 0.5
        yalign 0.4
        left_bar "gui/overlay_hscrollbar_back_left.png"
        right_bar "gui/overlay_hscrollbar_back.png"
        hover_left_bar "gui/overlay_hscrollbar_back_hover.png"
        thumb "gui/overlay_scrollbar_button.png"
        hover_thumb "gui/overlay_scrollbar_button_hover.png"
        thumb_shadow None
        thumb_offset 15
        focus_mask True
        hover_sound "se/hover.ogg"
        activate_sound "se/click.ogg"

init -3:
    style readback_window:
        background None
        xalign 0.5
        yalign 0.1
        
    style readback_frame:
        background None
        xminimum 1920
        xmaximum 1920
        
    style readback_text:
        color "#FFFFFF"
        size 26
        kerning 1
        drop_shadow [(2, 2)]
        drop_shadow_color "#2C261F"
        outlines [(1, "#282828", 0, 0)]
        
    style readback_button:
        idle_background  "gui/codex_button_idle.png"
        hover_background "gui/codex_button_hover.png"
        selected_idle_background "gui/codex_button_selected_idle.png"
        selected_hover_background "gui/codex_button_hover.png"
        insensitive_background im.Grayscale(im.MatrixColor("gui/codex_button_idle.png", im.matrix.opacity(.5)))
        xminimum 300
        xmaximum 300
        yminimum 64
        left_padding 10
        right_padding 10
        top_padding 15
        yalign .5
        activate_sound "se/click.ogg"
        hover_sound "se/hover.ogg"
        focus_mask True
        
    style readback_button_text:
        size 18
        xalign 0.5
        text_align 0.5
        color "#FFFFFF"
        
    style readback_label_text:
        size 24
        drop_shadow [(2, 2)]
        drop_shadow_color "#2C261F"
        outlines [(1, "#282828", 0, 0)]
        
    style readback2_frame:
        background Frame("gui/texthistory_box.png",24,24)
        
init -2:
    style default:
        font "font/hussar.otf"
        kerning 1
        size 26
        color "#FFFFFF"
        drop_shadow [(1.5, 1.2)]
        drop_shadow_color "#2C261F"
        outlines [(2, "#282828", 0, 0)]
        line_spacing 10
        line_overlap_split -5
        
    style button:
        activate_sound "se/click.ogg"
        hover_sound "se/hover.ogg"
        focus_mask True
        
    style imagebutton:
        hover_sound "se/hover.ogg"
        activate_sound "se/click.ogg"
        
    style textbutton:
        activate_sound "se/click.ogg"
        hover_sound "se/hover.ogg"
        focus_mask True
        
    style window:
        background "gui/window.png"
        left_padding 400
        right_padding 500
        top_padding 130
        bottom_padding 10
        xmaximum 1920
        xminimum 1920
        ymaximum 300
        yminimum 300
        xalign 0.5
        
    style hotspot:
        hover_sound "se/hover.ogg"
        activate_sound "se/click.ogg"
        
    style imagemap:
        activate_sound "se/click.ogg"
    
    style menu_window:
        background "gui/overlay_voxpop_frame.png"
        xalign .32
        yalign .28
        left_margin 300
        top_margin 20
        
    style menu_choice:
        size 22
        xalign .5
        yalign .5
        color "#FFFFFF"
        
    style menu_choice_button:
        idle_background Frame("gui/pref_button_idle.png", 24, 24)
        hover_background Frame("gui/pref_button_hover.png", 24, 24)
        selected_idle_background Frame("gui/pref_button_selected_idle.png", 24, 24)
        selected_hover_background Frame("gui/pref_button_hover.png", 24, 24)
        insensitive_background Frame (im.Grayscale(im.MatrixColor("gui/pref_button_idle.png", im.matrix.opacity(.5))), 24, 24)
        xminimum 1000
        xmaximum 1000
        yminimum 84
        top_padding 13
        xfill False
        yfill False
        xalign 0.5
        yalign 0.5
        activate_sound "se/click.ogg"
        hover_sound "se/hover.ogg"
        focus_mask True
        
    style nav_button:
        xysize (448, 106)
        selected_idle_background "party_section_button_selected_idle"
        idle_background "party_section_button_idle"
        hover_background "party_section_button_hover"
        insensitive_background "party_section_button_insensitive"
        top_padding 13
        yalign 0.5
        focus_mask True
        hover_sound "se/hover.ogg"
        activate_sound "se/click.ogg"
        
    style nav_button_text:
        size 24
        xalign 0.5
        text_align 0.5
        color "#FFFFFF"
        
    style nav_label_text:
        size 22
        drop_shadow [(2, 2)]
        drop_shadow_color "#2C261F"
        outlines [(1, "#282828", 0, 0)]
        
    style missionlog_frame:
        background None
        xpadding 15
        ypadding 15
        
    style missionlog_button:
        xysize (492, 106)
        selected_idle_background Frame("party_section_button_selected_idle", 5, 5)
        idle_background Frame("party_section_button_idle", 5, 5)
        hover_background Frame("party_section_button_hover", 5, 5)
        insensitive_background Frame("party_section_button_insensitive", 5, 5)
        yalign 0.5
        activate_sound "se/click.ogg"
        hover_sound "se/hover.ogg"
        focus_mask True
        
    style missionlog_button_text:
        size 20
        xalign 0.5
        yalign 0.6
        color "#FFFFFF"
        
    style missionlog_text:
        color "#FFFFFF"
        size 22
        
    style bonus_frame:
        background None
        xpadding 15
        ypadding 15
        
    style bonus_button:
        idle_background Frame("gui/codex_button_idle.png", 10, 10)
        hover_background Frame("gui/codex_button_hover.png", 10, 10)
        selected_idle_background Frame("gui/codex_button_selected_idle.png", 10, 10)
        selected_hover_background Frame("gui/codex_button_hover.png", 10, 10)
        insensitive_background Frame(im.Grayscale(im.MatrixColor("gui/codex_button_idle.png", im.matrix.opacity(.5))), 10, 10)
        xminimum 265
        xmaximum 265
        yminimum 62
        ymaximum 62
        left_padding 10
        right_padding 10
        top_padding 13
        yalign 0.5
        activate_sound "se/click.ogg"
        hover_sound "se/hover.ogg"
        focus_mask True
        
    style bonus_button_text:
        size 18
        xalign 0.5
        text_align 0.5
        color "#FFFFFF"
        
    style bonus_label_text:
        size 22
        drop_shadow [(2, 2)]
        drop_shadow_color "#2C261F"
        outlines [(1, "#282828", 0, 0)]
        
    style bonus_text:
        color "#FFFFFF"
        
    style vp_hbox:
        xalign 0.5
        xfill False
        
    style vp_button:
        idle_background Frame("gui/pref_button_idle.png", 24, 24)
        hover_background Frame("gui/pref_button_hover.png", 24, 24)
        selected_idle_background Frame("gui/pref_button_selected_idle.png", 24, 24)
        selected_hover_background Frame("gui/pref_button_hover.png", 24, 24)
        insensitive_background Frame (im.Grayscale(im.MatrixColor("gui/pref_button_idle.png", im.matrix.opacity(.5))), 24, 24)
        xminimum 400
        xmaximum 400
        yminimum 90
        ymaximum 90
        xpadding 10
        top_padding 13
        xalign 0.5
        yalign 0.5
        activate_sound "se/click.ogg"
        hover_sound "se/hover.ogg"
        focus_mask True
        
    style vp_button_text:
        size 22
        xalign 0.5
        text_align 0.5
        color "#FFFFFF"
        
    style vp_text:
        color "#FFFFFF"
        
    style choicegrid_hbox:
        xalign 0.5
        xfill False
        
    style choicegrid_button:
        idle_background Frame("gui/pref_button_idle.png", 24, 24)
        hover_background Frame("gui/pref_button_hover.png", 24, 24)
        selected_idle_background Frame("gui/pref_button_selected_idle.png", 24, 24)
        selected_hover_background Frame("gui/pref_button_hover.png", 24, 24)
        insensitive_background Frame (im.Grayscale(im.MatrixColor("gui/pref_button_idle.png", im.matrix.opacity(.5))), 24, 24)
        xminimum 600
        xmaximum 600
        yminimum 90
        ymaximum 90
        xpadding 10
        top_padding 13
        xalign 0.5
        yalign 0.5
        activate_sound "se/click.ogg"
        hover_sound "se/hover.ogg"
        focus_mask True
        
    style choicegrid_button_text:
        size 22
        xalign 0.5
        text_align 0.5
        color "#FFFFFF"
        
    style choicegrid_text:
        color "#FFFFFF"
        
    style file_picker_frame:
        background None
        xalign 0
        xminimum 420
        
    style file_picker_nav_button:
        idle_background "gui/blank_idle.png"
        hover_background "gui/blank_hover.png"
        selected_idle_background "gui/blank_selected_idle.png"
        selected_hover_background "gui/blank_hover.png"
        insensitive_background im.Grayscale("gui/blank_idle.png")
        xminimum 60
        xmaximum 60
        yminimum 60
        ymaximum 60
        top_padding 19
        left_padding 13
        xalign 0.5
        text_align 0.5
        activate_sound "se/click.ogg"
        hover_sound "se/hover.ogg"
        focus_mask True
        
    style file_picker_nav_button_text:
        size 19
        xalign 0.5
        yalign 0.5
        text_align 0.5
        
    style file_picker_button:
        idle_background "gui/picker_button_back.png"
        hover_background im.MatrixColor("gui/picker_button_back.png", im.matrix.brightness(0.2) * im.matrix.tint(1.0, 0.3, 0.3 ))
        selected_idle_background im.MatrixColor("gui/picker_button_back.png", im.matrix.brightness(0.1) * im.matrix.tint(0.7, 0.3, 0.3 ))
        selected_hover_background im.MatrixColor("gui/picker_button_back.png", im.matrix.brightness(0.2) * im.matrix.tint(1.0, 0.3, 0.3 ))
        insensitive_background im.Grayscale("gui/picker_button_back.png")
        ypadding 20
        xpadding 20
        xminimum 620
        xmaximum 620
        yminimum 190
        ymaximum 190
        activate_sound "se/click.ogg"
        hover_sound "se/hover.ogg"
        focus_mask True
        
    style file_picker_text:
        size 15
        xalign 0.5
        color "#FFFFFF"
        
    style pref_frame:
        background Frame("gui/stat_box.png",24,24)
        xpadding 15
        ypadding 15
        xalign 0.5
        text_align 0.5
        
    style pref_dark_frame:
        background Frame("gui/stat_box_dark.png",24,24)
        xpadding 15
        ypadding 15
        xalign 0.5
        text_align 0.5
        
    style pref_button:        
        idle_background Frame ("gui/pref_button_idle.png", 24, 24)
        hover_background Frame ("gui/pref_button_hover.png", 24, 24)
        selected_idle_background Frame ("gui/pref_button_selected_idle.png", 24, 24)
        selected_hover_background Frame ("gui/pref_button_hover.png", 24, 24)
        insensitive_background Frame (im.Grayscale(im.MatrixColor("gui/pref_button_idle.png", im.matrix.opacity(.5))), 24, 24)
        xminimum 260
        xmaximum 260
        yminimum 90
        ymaximum 90
        xpadding 30
        top_padding 12
        activate_sound "se/click.ogg"
        hover_sound "se/hover.ogg"
        focus_mask True
        
    style pref_text:
        size 16
        yoffset 6
        color "#FFFFFF"
        
    style pref_label_text:
        text_align 0.5
        xalign 0.5
        color "#FFFFFF"
        size 19
        
    style pref_button_text:
        size 19
        color "#FFFFFF"
        
    style pref_display_button:        
        idle_background Frame ("gui/maptype_button_idle.png", 10, 10)
        hover_background Frame ("gui/maptype_button_hover.png", 10, 10)
        selected_idle_background Frame ("gui/maptype_button_selected_idle.png", 10, 10)
        selected_hover_background Frame ("gui/maptype_button_hover.png", 10, 10)
        insensitive_background Frame (im.Grayscale(im.MatrixColor("gui/maptype_button_idle.png", im.matrix.opacity(.5))), 10, 10)
        xminimum 260
        xmaximum 260
        yminimum 60
        ymaximum 60
        xpadding 30
        top_padding 12
        activate_sound "se/click.ogg"
        hover_sound "se/hover.ogg"
        focus_mask True
        
    style pref_display_button_text:
        size 17
        color "#FFFFFF"
        
    style soundtest_button:
        xalign 1.0
        activate_sound "se/click.ogg"
        hover_sound "se/hover.ogg"
        focus_mask True
        
    style yesno_frame:
        background "gui/yesno_frame.png"
        xalign 0.5
        yalign 0.5
        xsize 1109
        ysize 380
        
    style yesno_label_text:
        size 25
        drop_shadow [(2, 2)]
        drop_shadow_color "#2C261F"
        outlines [(1, "#282828", 0, 0)]
        
    style quick_hbox:
        xalign .995
        yalign .993
        xpadding 4
        
    style quick_frame:
        background None
        
    style quick_text:
        size 11
        text_align 0.5
        xalign 0.5
        
    style music_frame_text:
        color "#FFFFFF"
        size  20
        
    style music_frame_frame:
        background None
        top_margin 140
        
    style music_frame_button_text:
        size 17
        
    style soundwave_frame_frame:
        background Frame("gui/frame.png", 24, 24)
        xminimum 590
        xmaximum 590
        yminimum 92
        ymaximum 92
        top_padding 15
        bottom_padding 10
        xpadding 10
        top_margin 3
        xalign 0.5
        
    style soundwave_frame_text:
        size 26
        
    style song_frame_text:
        color "#FFFFFF"
        size 18
        xalign 0.5
        yalign 0.5
        
    style song_frame_button_text:
        size 15
        color "#FFFFFF"
        yalign 0.5
        xalign 0.5
        
    style song_frame_button:
        idle_background Frame ("gui/pref_button_idle.png", 10, 10)
        hover_background Frame ("gui/pref_button_hover.png", 10, 10)
        selected_idle_background Frame ("gui/pref_button_selected_idle.png", 10, 10)
        selected_hover_background Frame ("gui/pref_button_hover.png", 10, 10)
        insensitive_background Frame (im.Grayscale(im.MatrixColor("gui/pref_button_idle.png", im.matrix.opacity(.3))), 10, 10)
        xminimum 300
        xmaximum 300
        yminimum 65
        ymaximum 65
        xalign 0.5
        xpadding 20
        bottom_padding -3
        top_padding 10
        ymargin 0
        activate_sound "se/click.ogg"
        hover_sound "se/hover.ogg"
        focus_mask True
        
    style codexinner_frame:
        background None
        xalign 0.01
        yalign 0.9
        
    style codexinner_text:
        color "#FFFFFF"
        size 20
        xalign 0.5
        yalign 0.5
        
    style codexinner_vbox:    
        yalign 0.5
        
    style codexinner_button_text:
        size 20
        color "#FFFFFF"     
        yalign 0.5
        xalign 0.5
        
    style codexinner_button:
        idle_background Frame ("gui/pref_button_idle.png", 24, 24)
        hover_background Frame ("gui/pref_button_hover.png", 24, 24)
        selected_idle_background Frame ("gui/pref_button_selected_idle.png", 24, 24)
        selected_hover_background Frame ("gui/pref_button_hover.png", 24, 24)
        insensitive_background Frame (im.Grayscale(im.MatrixColor("gui/pref_button_idle.png", im.matrix.opacity(.5))), 24, 24)
        xminimum 310
        xmaximum 310
        yminimum 90
        ymaximum 90
        xalign 0.5
        xpadding 10
        top_padding 12
        activate_sound "se/click.ogg"
        hover_sound "se/hover.ogg"
        focus_mask True
        
    style missionbutton_text:
        size 18
        xalign 0.5
        text_align 0.5
        drop_shadow None
        outlines [(2, "#282828", 0, 0)]
        
    style missionbutton_button:
        idle_background Frame("gui/battleguiparty_cancelbutton_idle.png", 10, 10)
        hover_background Frame("gui/battleguiparty_cancelbutton_hover.png", 10, 10)
        yminimum 80
        xminimum 600
        activate_sound "se/click.ogg"
        hover_sound "se/hover.ogg"
        focus_mask True
        
    style missionbutton_button_text:
        size 24
        xalign 0.5
        yalign 0.7
        text_align 0.5
        drop_shadow None
        outlines [(2, "#282828", 0, 0)]
        color "#FFFFFF"
        
    style maptype_button:
        idle_background "gui/maptype_button_idle.png"
        hover_background "gui/maptype_button_hover.png"
        selected_idle_background "gui/maptype_button_selected_idle.png"
        selected_hover_background "gui/maptype_button_hover.png"
        insensitive_background im.Grayscale(im.MatrixColor("gui/maptype_button_idle.png", im.matrix.opacity(.5)))
        xsize 346
        top_padding 19
        activate_sound "se/click.ogg"
        hover_sound "se/hover.ogg"
        focus_mask True
        
    style maptype_button_text:
        size 20
        xalign 0.5
        yalign 0.7
        text_align 0.5
        drop_shadow None
        outlines [(2, "#282828", 0, 0)]
        color "#FFFFFF"
        
    style missiontype_button:
        idle_background "gui/missiontype_button_idle.png"
        hover_background "gui/missiontype_button_hover.png"
        selected_idle_background "gui/missiontype_button_selected_idle.png"
        selected_hover_background "gui/missiontype_button_hover.png"
        insensitive_background im.Grayscale(im.MatrixColor("gui/missiontype_button_idle.png", im.matrix.opacity(.5)))
        xsize 600
        bottom_margin 20
        top_padding 31
        activate_sound "se/click.ogg"
        hover_sound "se/hover.ogg"
        focus_mask True
        
    style missiontype_button_text:
        size 18
        xalign 0.5
        yalign 0.7
        text_align 0.5
        drop_shadow None
        outlines [(2, "#282828", 0, 0)]
        color "#FFFFFF"
        
    style overlayboxsmall_text:
        color "#FFFFFF"
        size 19
        xalign .5
        
    style overlayboxsmall_frame:
        background "gui/overlay_box_small.png"
        top_padding 25
        bottom_padding 20
        
    style overlayboxsmall_button_text:
        size 20
        
    style overlayboxsmall_button:
        xalign .5
        yalign .9
        activate_sound "se/click.ogg"
        hover_sound "se/hover.ogg"
        focus_mask True
        
    style overlayboxlarge_text:
        color "#FFFFFF"
        size 19
        xalign .5
        
    style overlayboxlarge_frame:
        background "gui/overlay_box_large.png"
        top_padding 25
        bottom_padding 20
        
    style overlayboxlarge_button_text:
        size 20
        
    style overlayboxlarge_button:
        xalign .5
        yalign .9
        activate_sound "se/click.ogg"
        hover_sound "se/hover.ogg"
        focus_mask True
        
    style maptooltip_frame:
        background Frame("gui/frame.png", 24, 24)
        xpadding 30
        xminimum 400
        xmaximum 700
        top_padding 20
        
    style maptooltip_text:
        size 18
        xalign 0.5
        text_align 0.5
        color "#FFFFFF"
        
    style update_stat_text:
        color "#FFFFFF"
        size 16
        xalign 0
        
    style update_stat_hyperlink_text:
        size 14
        idle_color "#FFFFFF"
        hover_color "#E10900"
        
    style update_stat_button_text:
        size 16
        
    style button_text:
        color "#FFFFFF"
        
    style gallery_frame:
        background Frame("gui/frame.png", 24, 24)
        xpadding 10
        
    style gallery_button:
        size_group "gm_nav"
        ypadding 8
        yalign .5
        activate_sound "se/click.ogg"
        hover_sound "se/hover.ogg"
        focus_mask True
        
    style gallery_text:
        color "#FFFFFF"
        
    style gallery_button_text:
        color "#FFFFFF"
        hover_color "#E10900"
        selected_idle_color "#5e5e5e"
        
    style say_who_window:
        xpos 250
        xalign 0.5
        xmaximum 500
        ymaximum 200
        left_padding 10
        right_padding 10
        top_padding 0
        bottom_padding 0
        ypos 855
        background None
        text_align 0.5
        
    style say_label:
        kerning 4
        xalign 0.5
        text_align 0.5
        outlines [(1, "#282213", 0, 0)]
        size 25
        drop_shadow None
        
    style map_info_frame:
        background None
        
    style map_info_text:
        xalign 0
        color "#FFFFFF"
        size 14
        drop_shadow None
        
    style allegiancestext_text:
        xalign 0.5
        size 14
        color "#FFFFFF"
        drop_shadow None
        kerning 2
        
    style allegiancestext_button:
        activate_sound "se/click.ogg"
        hover_sound "se/hover.ogg"
        focus_mask True
        
    style governor_frame:
        background "gui/mapmenu_frame2.png"
        
    style governor_text:
        color "#FFFFFF"
        size 20
        drop_shadow None
        
    style governor_label_text:
        size 22
        drop_shadow None
        
    style governor2_text:
        color "#FFFFFF"
        size 16
        drop_shadow None
        
    style governor2_frame:
        background Frame("gui/texthistory_box.png",24,24)
        
    style town_stats_text:
        color "#FFFFFF"
        size 14
        drop_shadow None
        
    style town_stats_label:
        size 18
        color "#FFFFFF"
        drop_shadow None
        
    style town_stats_frame:
        background Frame("gui/stat_box.png",24,24)
        
    style battle_stats_text:
        color "#FFFFFF"
        size 16
        drop_shadow None
        
    style battle_stats_label:
        size 18
        color "#FFFFFF"
        drop_shadow None
        
    style battle_stats_frame:
        background Frame("gui/stat_box.png",24,24)
        ypadding 0
        xpadding 0
        
    style command_frame:
        background Frame("gui/stat_box.png",24,24)
        
    style command_text:
        color "#FFFFFF"
        size 16
        drop_shadow None
        text_align 0.5
        line_spacing 2
        kerning 0
        
    style command_label:
        size 20
        color "#FFFFFF"
        drop_shadow None
        line_spacing 0.5
        
    style command_vbox:
        xminimum 400
        xmaximum 400
    
    style commandbody_frame:
        background Frame("gui/texthistory_box.png",24,24)
        
    style commandoverlay_frame:
        background Frame("gui/texthistory_box.png",24,24)
        xminimum 425
        xmaximum 425
        xalign 0.5
       
    style fuuhbarmuseum_frame:
        background Frame("gui/texthistory_box.png",24,24)
        yminimum 170
        ymaximum 170
        xalign 0.5
        
    style fuuhbarmuseum_inner_text:
        color "#FFFFFF"
        size 14
        kerning 0
        drop_shadow None
        text_align 0.5
        line_spacing 1.5
        
    style fuuhbarmuseum_inner_label:
        size 18
        color "#FFFFFF"
        drop_shadow None
        
    style fuuhbarmuseum_inner_frame:
        background Frame("gui/stat_box.png",24,24)
        xalign 0.5
        ypadding 7
        xpadding 10
        
    style research_frame:
        background Frame("gui/texthistory_box.png",24,24)
        xalign 0.5
        
    style research_upper_frame:
        background Frame("gui/stat_box.png",24,24)
        xalign 0.5
        ypadding 5
        xminimum 140
        xmaximum 140
        yminimum 94
        ymaximum 94
        
    style research_lower_frame:
        background Frame("gui/stat_box.png",20,20)
        xalign 0.5
        ypadding 7
        xminimum 140
        xmaximum 140
        yminimum 60
        ymaximum 60
        top_padding 10

    style research_lower_text:
        color "#FFFFFF"
        xalign 0.5
        yalign 0.5
        size 13
        kerning 0
        drop_shadow None
        text_align 0.5
        line_spacing 1.5

    style research_counter_frame:
        background "gui/white_circle.png"
        xpadding 10
        top_padding 7
        
    style research_counter_text:
        size 16
        color "#000"
        outlines [(0, "#282213", 0, 0)]
        drop_shadow None
        
    style researchinsensitive_frame:
        background Frame(im.MatrixColor("gui/texthistory_box.png", im.matrix.opacity(0.5)),20,20)
        xalign 0.5
        
    style researchinsensitive_upper_frame:
        background Frame(im.MatrixColor("gui/stat_box.png", im.matrix.opacity(0.5)),20,20)
        xalign 0.5
        ypadding 5
        xminimum 140
        xmaximum 140
        yminimum 94
        ymaximum 94
        
    style researchinsensitive_lower_frame:
        background Frame(im.MatrixColor("gui/stat_box.png", im.matrix.opacity(0.5)),20,20)
        xalign 0.5
        ypadding 7
        xminimum 140
        xmaximum 140
        yminimum 60
        ymaximum 60
        top_padding 10
        
    style researchinsensitive_lower_text:
        color "#FFFFFF"
        xalign 0.5
        yalign 0.5
        size 13
        kerning 0
        drop_shadow None
        text_align 0.5
        line_spacing 1.5
        
    style insignia_frame:
        background Frame("gui/texthistory_box.png",24,24)
        xminimum 243
        xmaximum 243
        yminimum 150
        ymaximum 150
        xalign 0.5
        
    style insignia_vbox:
        xalign 0.5
        yalign 0.5
        
    style insignia_inner_text:
        color "#FFFFFF"
        size 17
        kerning 0
        drop_shadow None
        text_align 0.5
        line_spacing 1
        
    style insignia_inner_label:
        size 18
        color "#FFFFFF"
        drop_shadow None
        
    style insignia_inner_frame:
        background Frame("gui/stat_box.png",24,24)
        xminimum 238
        xmaximum 238
        xalign 0.5
        ypadding 7
  
    style codexouter_frame:
        background Frame("gui/texthistory_box.png",24,24)
        xminimum 370
        xmaximum 370
        yminimum 790
        ymaximum 790
        bottom_padding 1
        top_padding 1
        yalign 0.7
        xalign 0.5
        
    style codexouter_vbox:
        xalign 0.5
        yalign 0.5
        yfill False
        xfill False
        
    style codexouter_button_text:
        size 20
        
    style codexouter_text:
        size 16
        color "#FFFFFF"
        
    style codexheading_frame:
        background Frame("gui/texthistory_box.png",24,24)
        yminimum 25
        ymaximum 25
        xpadding 7
        ypadding 7
        
    style codexsubtitle_frame:
        background Frame("gui/texthistory_box.png",24,24)
        yminimum 25
        ymaximum 25
        xpadding 20
        top_padding 16
        bottom_padding 5
        
    style codexsubtitle_text:                                    
        color "#FFFFFF"
        size 22
        kerning 0
        drop_shadow None
        
    style codexsubtitle_hbox:
        xalign 0.5
        yalign 0.5      
        
    style codexbody_frame:
        background Frame("gui/texthistory_box.png",24,24)
        xpadding 40
        ypadding 40
        
    style codexbody_text:                                    
        color "#FFFFFF"
        size 20
        kerning 0
        drop_shadow None
        
    style codexbody_hbox:
        xalign 0
        yalign 0
        
    style codexbasic_frame:
        background Frame("gui/texthistory_box.png",24,24)
        
    style codexbasic_text:                                    
        color "#FFFFFF"
        size 20
        kerning 0
        drop_shadow None
        
    style codexbasic_hbox:
        xalign 0.5
        yalign 0.5
        
    style codexprofile_frame:
        background Frame("gui/texthistory_box.png",24,24)
        xminimum 350
        xmaximum 350
        yminimum 210
        ymaximum 210
        top_padding 7
        bottom_padding 7
        right_padding 7
        
    style codexstats_text:
        color "#FFFFFF"
        size 17
        drop_shadow None
        kerning 0
        xalign 0.5                                                   
        yalign 0.7
        
    style codexstats_frame:
        background Frame("gui/stat_box.png",24,24)
        xminimum 194
        xmaximum 194
        yminimum 70
        ymaximum 70
        top_padding 8
        
    style codexstatstitle_text:
        color "#FFFFFF"
        size 18
        italic True
        drop_shadow None
        kerning 0
        xalign 0.5                                                   
        yalign 0.7
        
    style codexstatstitle_frame:
        background Frame("gui/stat_box_dark.png",24,24)
        xminimum 145
        xmaximum 145
        yminimum 70
        ymaximum 70
        top_padding 11
        
    style main_stats_text:
        color "#FFFFFF"
        size 16
        drop_shadow None
        
    style main_stats_label:
        size 18
        color "#FFFFFF"
        drop_shadow None
        
    style main_stats_frame:
        background Frame("gui/stat_box_dark.png",24,24)
        xpadding 0
        ypadding 0
        
    style voxpopouter_frame:
        background "gui/overlay_box_small.png"
        top_padding 25
        bottom_padding 20
        xalign .5
        yalign .5
        xmaximum 1300
        xminimum 1300
        ymaximum 638
        yminimum 638
        yfill False
        xfill False
        
    style voxpopmiddle_text:
        color "#FFFFFF"
        size 20
        drop_shadow None
        
    style voxpopmiddle_frame:
        background Frame("gui/texthistory_box.png",24,24)
        xminimum 1231
        xmaximum 1231
        yminimum 340
        ymaximum 340
        bottom_padding 5
        top_padding 20
        yalign 0.67
        xalign 0.51
        
    style voxpopinner_text:
        color "#FFFFFF"
        size 20
        drop_shadow None
        
    style voxpopinner_frame:
        background Frame("gui/texthistory_box.png",24,24)
        xminimum 1221
        xmaximum 1221
        yminimum 290
        ymaximum 290
        xpadding 3
        bottom_padding 10
        top_padding 10
        yalign 0.9
        
    style availablesection_button:
        xysize (428, 106)
        selected_idle_background "party_section_button_selected_idle"
        idle_background "party_section_button_idle"
        hover_background "party_section_button_hover"
        insensitive_background "party_section_button_insensitive"
        activate_sound "se/section.ogg"
        hover_sound "se/hover.ogg"
        focus_mask True
        
    style researchsection_button:
        idle_background Frame ("gui/pref_button_idle.png", 24, 24)
        hover_background Frame ("gui/pref_button_hover.png", 24, 24)
        selected_idle_background Frame ("gui/pref_button_selected_idle.png", 24, 24)
        selected_hover_background Frame ("gui/pref_button_hover.png", 24, 24)
        insensitive_background Frame (im.Grayscale(im.MatrixColor("gui/pref_button_idle.png", im.matrix.opacity(.5))), 24, 24)
        xminimum 340
        xmaximum 340
        yminimum 90
        ymaximum 90
        xpadding 10
        top_padding 10
        activate_sound "se/click.ogg"
        hover_sound "se/hover.ogg"
        focus_mask True
        
    style battle_text is default:
        color "#ffffff"
    
    style party_text:
        size 13
        outlines [(1, "#282828", 0, 0)]
        drop_shadow [(0, 0)]
        kerning 0
            
    style cp_text:
        font "font/ralewayblack.ttf"
        kerning -2.5
        color "#ffffff"
        drop_shadow [(1.5, 1.2)]
        drop_shadow_color "#2C261F"
        outlines [(2, "#282828", 0, 0)]
        
    style sovspeak:
        font "font/ralewayblack.ttf"
        size 25
        line_leading 1
        
    style description_box_outer_frame:
        background "gui/overlay_box_large.png"
        top_padding 25
        bottom_padding 20
        xalign .5
        yalign .5
        xmaximum 1569
        xminimum 1569
        ymaximum 910
        yminimum 910
        yfill False
        xfill False
        
    style description_box_outer_text:
        color "#ffffff"
        size 19
        xalign .5
        
    style description_box_outer_button_text:
        size 20
        
    style description_box_outer_button:
        xalign .5
        yalign .9
    
    style description_box_inner_frame:
        background Frame("gui/texthistory_box.png",24,24)
        xminimum 1500
        xmaximum 1500
        yminimum 670
        ymaximum 670
        bottom_padding 1
        top_padding 1
        yalign 0.85
        xalign 0.51
        
    style description_box_inner_text:
        color "#ffffff"
        size 16
        drop_shadow None
        
    style description_box_central_frame:
        background Frame("gui/texthistory_box.png",24,24)
        
    style description_box_central_text:
        color "#ffffff"
        size 16
        drop_shadow None
        
    style description_box_dark_frame:
        background Frame("gui/texthistory_dark_box.png",20,20)
        
    style description_box_dark_text:
        color "#ffffff"
        size 16
        drop_shadow None
        
    style victoryscreen_text:
        color "#ffffff"
        size 19
        xalign .5
        
    style victoryscreen_frame:
        background "gui/victory_screen.png"
        top_padding 25
        bottom_padding 20
        
    style victoryscreen_button_text:
        size 20
        
    style victoryscreen_button:
        xalign .5
        yalign .9
            
    style tooltip_box_frame:
        background Frame("gui/frame.png", 24, 24)
        xsize 850
        ysize 90
        xalign 0.99
        yalign 0.015
        xpadding 30
        top_padding 20
        
    style tooltip_box_text:
        size 15
        xalign 0.5
        yalign 0.5
        text_align 0.5
        
    style tooltip2_box_frame:
        background Frame("gui/frame.png", 24, 24)
        xsize 200
        ysize 75
        xalign 0.99
        yalign 0.01
        xpadding 20
        top_padding 20
        
    style tooltip2_box_text:
        size 16
        xalign 0.5
        yalign 0.5
        text_align 0.5
        
    style tooltip3_box_frame:
        background Frame("gui/frame.png", 24, 24)
        xsize 780
        ysize 100
        xalign 0.5
        yalign 0.98
        xpadding 20
        top_padding 20
        
    style tooltip3_box_text:
        size 16
        xalign 0.5
        yalign 0.5
        text_align 0.5
        
init -1 python:
    style.ruby_style = Style(style.default)
    style.ruby_style.size = 18
    style.ruby_style.yoffset = 35
    style.default.ruby_style = style.ruby_style
        
init 1:
    style vscrollbar:
        top_bar Frame("gui/overlay_vscrollbar_back.png", 30,30)
        bottom_bar Frame("gui/overlay_vscrollbar_back.png", 30,30)
        xmaximum 30
        thumb "gui/overlay_scrollbar_button.png"
        hover_thumb "gui/overlay_scrollbar_button_hover.png"
        thumb_offset 12
        
