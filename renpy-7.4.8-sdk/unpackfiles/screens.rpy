   
########################################################################################################################
#### SAY SCREEN #######################################################################################################
########################################################################################################################
screen say(who, what, side_image=None, two_window=False):
    default side_image = True
    default two_window = True
    default quick_menu = True
    vbox:
        yminimum 210 ymaximum 210 yalign 1.0 xalign 0.0 xmaximum 360
        add "black"
    if side_image:
        add side_image xalign 0.0 yalign 1.0
    else:
        add SideImage() xalign 0.0 yalign 1.0
    if not two_window:
        window:
            id "window"
            has vbox
            if who:
                text who id "who"
            text what id "what"
    else:
        vbox:
            yalign 1.0
            xalign 0.5
            window:
                id "window"
                has vbox
                text what id "what"
        vbox:
            if who:
                vbox:
                    style "say_who_window"
                    text who:
                        id "who"
    use quick_menu
    #key "mousedown_3" action FileTakeScreenshot()
    
    key 'rollback' action [SetVariable("yvalue", 1.0), ShowMenu("text_history")]
    
########################################################################################################################
#### CHOICE SCREEN ####################################################################################################
########################################################################################################################
screen choice(items):
    tag menu
    if voxpopmode_enabled:
        modal True
        add Solid("#000000") alpha 0.6
        add "gear2" xalign 0.685 yalign 0.785
        add "gear" xalign 0.315 yalign 0.785
        frame:
            style_group "voxpopouter"
            frame:
                style_group "voxpopmiddle"
                vbox:
                    xalign 0.5
                    yalign 0.5
                    yfill False
                    xfill False
                    vbox:
                        xalign 0.5
                        yalign 0.7
                        text "Ask around and find out what people think . . ."
                    frame:
                        style_group "voxpopinner"
                        vbox:
                            xalign 0.5
                            yalign 0.5
                            grid 3 3:
                                xfill False
                                style_group "vp"
                                for caption, action, chosen in items:
                                    if action:
                                        button:
                                            action action hover_sound "se/hover.ogg" activate_sound "se/click.ogg"
                                            text caption style "menu_choice"
                                    else:
                                        text caption style "menu_caption"    
                                for j in range(0, 9 - len(items)):
                                    null
            hbox:
                xalign 0.5
                yalign 1.019
                xfill False
                style_group "vp"
                textbutton "Leave" action [Jump(voxpopjump), SensitiveIf(voxpopleave_sensitive)]
        use voxpop_overlay_frame
        
    else:
        add "gear2" xalign 0.685 yalign 0.71
        add "gear" xalign 0.315 yalign 0.71
        frame:
            background "gui/overlay_choice_back.png"
            xalign .5
            yalign .5
            xmaximum 1300
            xminimum 1300
            ymaximum 487
            yminimum 487
            yfill False
            xfill False
        vbox:
            style_group "menu"
            xalign .5
            if len(items) > 3:
                if len(items) > 4:
                    yalign .59
                else:
                    yalign .63
                grid 2 3:
                    xfill False
                    style_group "choicegrid"
                    for caption, action, chosen in items:
                        if action:
                            button:
                                action action hover_sound "se/hover.ogg" activate_sound "se/click.ogg"
                                text caption style "menu_choice"
                        else:
                            text caption style "menu_caption" 
                    for j in range(0, 6 - len(items)):
                        null
            else:
                if len(items) > 2:
                    yalign .583
                else:
                    yalign .573
                for caption, action, chosen in items:
                    if action:
                        button:
                            action action hover_sound "se/hover.ogg" activate_sound "se/click.ogg"
                            style "menu_choice_button"
                            text caption style "menu_choice"
                    else:
                        text caption style "menu_caption" 
        add "gui/overlay_frame_back2.png":
            xalign 0.5
            yalign 0.32
        add "gui/overlay_title_choice.png":
            xalign 0.5
            yalign 0.352
        
########################################################################################################################
#### INPUT ##############################################################################################################
########################################################################################################################
screen input(prompt):
    window:
        has vbox
        text prompt
        input id "input"
    use quick_menu
        
########################################################################################################################
#### NVL ################################################################################################################
########################################################################################################################
screen nvl(dialogue, items=None):
    window:
        style "nvl_window"
        has vbox:
            style "nvl_vbox"
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id
                has hbox:
                    spacing 10
                if who is not None:
                    text who id who_id
                text what id what_id
        if items:
            vbox:
                id "menu"
                for caption, action, chosen in items:
                    if action:
                        button:
                            style "nvl_menu_choice_button"
                            action action
                            text caption style "nvl_menu_choice"
                    else:
                        text caption style "nvl_dialogue"
    add SideImage() xalign 0.0 yalign 1.0
    use quick_menu
    
########################################################################################################################
#### MAIN MENU #########################################################################################################
########################################################################################################################
screen mainmenu_animation_screen():
    add "mainmenu_back"
    add "mainmenu_animation"
    add "gear2" xalign 0.76 at gear_eff
    add "gear" xalign 0.24 at gear_eff
    add "gui/mainmenu_back.png" xalign 0.5 at mm_eff
    if mmboomsound:
        timer 1.8 action [Play("mmsound","se/boom.ogg"), SetVariable("mmboomsound", False)]
    timer 0.1 action [Play("mmsound2","se/tank_drive.ogg"), Play("mmsound3","se/gears.ogg")]
    timer 4.0 action [Stop("mmsound2", fadeout=3.0), Stop("mmsound3", fadeout=3.0)]

screen main_menu():
    tag menu
    default show_mainmenu_nav = True
    use mainmenu_animation_screen id "animscreen"
    
    if show_mainmenu_nav:
        use mainmenu_nav id "common"
    else:
        use bonus id "common"
        
    add "logo_shadow"
    add "logo" at logo_eff
    
    
screen mainmenu_nav():
    tag menu2
    frame:
        style_group "bonus"
        xalign 0.498
        yalign 1.017
        vbox:
            hbox:
                textbutton _("New Game") action Show("game_mode") hover_sound "se/hover.ogg" activate_sound "se/click.ogg" at bonus_eff focus_mask True
                textbutton _("Load Data") action [ShowMenu("load"), Stop("mmsound", fadeout=1.0), Stop("mmsound2", fadeout=1.0), Stop("mmsound3", fadeout=1.0)] hover_sound "se/hover.ogg" activate_sound "se/click.ogg" at bonus_eff focus_mask True
                textbutton _("Options") action [ShowMenu("preferences"), Stop("mmsound", fadeout=1.0), Stop("mmsound2", fadeout=1.0), Stop("mmsound3", fadeout=1.0)] hover_sound "se/hover.ogg" activate_sound "se/click.ogg" at bonus_eff focus_mask True
            null height -5
            hbox:
                textbutton _("Bonus") action SetScreenVariable("show_mainmenu_nav", False) hover_sound "se/hover.ogg" activate_sound "se/click.ogg" at bonus_eff focus_mask True
                textbutton _("Credits") action [SensitiveIf(persistent.nyan_campaign_unlocked), Start("mainmenu_credits")] hover_sound "se/hover.ogg" activate_sound "se/click.ogg" at bonus_eff focus_mask True ypos 0
                textbutton _("Quit Game") action Quit(confirm=True) hover_sound "se/hover.ogg" activate_sound "se/click.ogg" at bonus_eff focus_mask True
        
########################################################################################################################
#### NAVIGATION ########################################################################################################
########################################################################################################################
screen navigation():
    add "black"
    add im.MatrixColor("back/map/westernmap.jpg", im.matrix.desaturate() * im.matrix.tint(1.0, 0.1, 0.1))
    add im.MatrixColor("gui/transparent2.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.8, 0.8)) alpha 0.7
    frame:
        background "gui/nav_back.png"
        yalign 0.5
        xalign 1.0
        ysize 1080
        xsize 484
    vbox:
        add "nav_chibi_random"
        yalign 0.03
        xalign 0.955
    vbox:
        add "nav_logo"
        yalign 0.24
        xalign 0.985
    vbox:
        style_group "nav"
        xalign 0.994
        yalign .92
        textbutton _("Return") action Return() hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True at nav_eff
        if not main_menu:
            textbutton _("Save Data") action ShowMenu("save") hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True at nav_eff
        textbutton _("Load Data") action ShowMenu("load") hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True at nav_eff
        textbutton _("Options") action ShowMenu("preferences") hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True at nav_eff
        if not main_menu:
            textbutton _("Main Menu") action MainMenu() hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True at nav_eff
        if main_menu:
            textbutton _("Gallery") action ShowMenu("cg_gallery") hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True at nav_eff
            textbutton _("Jukebox") action ShowMenu("music_room") hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True at nav_eff
        textbutton _("Quit Game") action Quit(confirm=True) hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True at nav_eff

########################################################################################################################
#### SAVE AND LOAD #####################################################################################################
########################################################################################################################
screen file_picker():
    vbox:
        xalign 0.17
        yalign 0.53
        null height 30
        hbox:
            xalign 0.5
            style_group "file_picker_nav"
            textbutton _("Q"):
                action FilePage("quick")
            textbutton _("A"):
                action FilePage("auto")
            for i in range(1, 19):
                textbutton str(i):
                    action FilePage(i)
        null height 5
        $ columns = 2
        $ rows = 4
        grid columns rows:
            xmaximum 1000
            ymaximum 900
            transpose True
            xfill False
            style_group "file_picker"
            for i in range(1, columns * rows + 1):
                button:
                    action FileAction(i)
                    hbox:
                        vbox:
                            frame:
                                style_group "governor2"
                                add FileScreenshot(i) size(244,137) xalign 0.5 yalign 0.5
                        vbox:
                            $ file_title = "% 2s. %s" % (FileSlotName(i, columns * rows), FileSaveName(i))
                            $ file_description = "%s" % (FileTime(i, empty=_("Empty Slot")))
                            frame:
                                style_group "governor2"
                                yminimum 150
                                ymaximum 150
                                xsize 320
                                xalign 0.5
                                yalign 0.5
                                ypadding 10
                                vbox:
                                    style_group "file_picker"
                                    xsize 300
                                    yminimum 50
                                    ymaximum 50
                                    xalign 0.5
                                    yalign 0.55
                                    text file_title:
                                        yalign 0.5
                                        size 15
                                    null height 1
                                    text file_description:
                                        yalign 0.5
                                        size 24
                        key "save_delete" action FileDelete(i)
                    
screen save():
    tag menu
    use navigation id "navi_navigation"
    frame:
        background "gui/load_back.png"
        yalign 0.5
        xalign 0.1
        ysize 1016
        xsize 1369
    vbox:
        xalign 0.37
        yalign 0.065
        add "gui/overlay_title_save.png"
    use file_picker
    frame:
        background Frame(im.Sepia("gui/outer_frame.png"), 200, 200)

screen load():
    tag menu
    use navigation id "navi_navigation"
    frame:
        background "gui/load_back.png"
        yalign 0.5
        xalign 0.1
        ysize 1016
        xsize 1369
    vbox:
        xalign 0.37
        yalign 0.065
        add "gui/overlay_title_load.png"
    use file_picker
    frame:
        background Frame(im.Sepia("gui/outer_frame.png"), 200, 200)

########################################################################################################################
#### PREFERENCES ######################################################################################################
########################################################################################################################
screen preferences():
    tag menu
    use navigation id "navi_navigation"
    frame:
        background "gui/config_back.png"
        yalign 0.5
        xalign 0.1
        ysize 1016
        xsize 1369
    vbox:
        xalign 0.14
        yalign 0.76
        add "display_image"
    vbox:
        xalign 0.14
        yalign 0.76
        add "display_image_overlay"
    vbox:
        xalign 0.1
        yalign 0.92
        style_group "pref_display"
        hbox:
            textbutton _("Fullscreen") action [Preference("display", "fullscreen"), SetVariable("current_image", 1)] hovered SetVariable("temp_image", 1) unhovered SetVariable("temp_image", current_image)
            textbutton _("Large Window") action [Preference("display", 1.0), SetVariable("current_image", 2)] hovered SetVariable("temp_image", 2) unhovered SetVariable("temp_image", current_image)
        hbox:
            textbutton _("Medium Window") action [Preference("display", 0.71111), SetVariable("current_image", 3)] hovered SetVariable("temp_image", 3) unhovered SetVariable("temp_image", current_image)
            textbutton _("Small Window") action [Preference("display", 0.55555), SetVariable("current_image", 4)] hovered SetVariable("temp_image", 4) unhovered SetVariable("temp_image", current_image)
    vbox:
        xalign 0.19
        yalign 0.22
        style_group "pref"
        hbox:
            vbox:
                frame:
                    style_group "pref_dark"
                    xminimum 600
                    xmaximum 600
                    yminimum 30
                    ymaximum 30
                    bottom_padding 0
                    label _("Skip Text"):
                        xalign 0.5
                frame:
                    xminimum 600
                    xmaximum 600
                    yminimum 100
                    ymaximum 100
                    hbox:
                        xalign 0.5
                        textbutton _("Skip Seen Text") action Preference("skip", "seen")
                        textbutton _("Skip All Text") action Preference("skip", "all")
            null width 20
            vbox:
                frame:
                    style_group "pref_dark"
                    xminimum 600
                    xmaximum 600
                    yminimum 30
                    ymaximum 30
                    bottom_padding 0
                    label _("After Choices"):
                        xalign 0.5
                frame:
                    xminimum 600
                    xmaximum 600
                    yminimum 100
                    ymaximum 100
                    hbox:
                        xalign 0.5
                        textbutton _("Stop Skipping") action Preference("after choices", "stop")
                        textbutton _("Keep Skipping") action Preference("after choices", "skip")
        hbox:
            vbox:
                frame:
                    style_group "pref_dark"
                    xminimum 600
                    xmaximum 600
                    yminimum 30
                    ymaximum 30
                    bottom_padding 0
                    label _("Text Speed"):
                        xalign 0.5
                frame:
                    xminimum 600
                    xmaximum 600
                    yminimum 60
                    ymaximum 60
                    hbox:
                        xalign 0.5
                        text "MIN"
                        null width 10
                        bar value Preference("text speed")                  
                        null width 10
                        text "MAX"
            null width 20
            vbox:
                frame:
                    style_group "pref_dark"
                    xminimum 600
                    xmaximum 600
                    yminimum 30
                    ymaximum 30
                    bottom_padding 0
                    label _("Auto-Forward Time"):
                        xalign 0.5
                frame:
                    xminimum 600
                    xmaximum 600
                    yminimum 60
                    ymaximum 60
                    hbox:
                        xalign 0.5
                        text "MIN"
                        null width 10
                        bar value Preference("auto-forward time")
                        null width 10
                        text "MAX"
    vbox:
        xalign 0.592
        yalign 0.89
        style_group "pref"
        vbox:
            frame:
                style_group "pref_dark"
                xminimum 540
                xmaximum 540
                yminimum 30
                ymaximum 30
                bottom_padding 0
                label _("Music Volume"):
                    xalign 0.5
            frame:
                xminimum 540
                xmaximum 540
                yminimum 60
                ymaximum 60
                bottom_padding 10
                hbox:
                    xalign 0.5
                    text "MIN"
                    null width 10
                    bar value Preference("music volume")
                    null width 10
                    text "MAX"
            frame:
                style_group "pref_dark"
                xminimum 540
                xmaximum 540
                yminimum 30
                ymaximum 30
                bottom_padding 0
                hbox:
                    xalign 0.5
                    null width 50
                    label _("SFX Volume"):
                        xalign 0.5
                    null width 100
                    frame:
                        background None
                        top_padding 4
                        bottom_padding -4
                        text "Silly SFX":
                            size 14
                    imagebutton auto "gui/tickbox_%s.png" action [ToggleVariable("silly_sounds", true_value=True, false_value=False), Function(silly_sounds_enabled)] hover_sound "se/hover.ogg" activate_sound "se/click.ogg"
                    
            frame:
                xminimum 540
                xmaximum 540
                yminimum 60
                ymaximum 60
                bottom_padding 10
                hbox:
                    xalign 0.5
                    text "MIN"
                    null width 10
                    bar value Preference("sound volume")
                    null width 10
                    text "MAX"
            frame:
                style_group "pref_dark"
                xminimum 540
                xmaximum 540
                yminimum 30
                ymaximum 30
                bottom_padding 0
                label _("Voice Volume"):
                    xalign 0.5
            frame:
                xminimum 540
                xmaximum 540
                yminimum 60
                ymaximum 60
                bottom_padding 10
                hbox:
                    xalign 0.5
                    text "MIN"
                    null width 10
                    bar value Preference("voice volume")
                    null width 10
                    text "MAX"
    frame:
        background Frame(im.Sepia("gui/outer_frame.png"), 200, 200)
        
    on "show" action SetVariable("config.dismiss_blocking_transitions", True)
    on "replace" action SetVariable("config.dismiss_blocking_transitions", True)
    on "hide" action SetVariable("config.dismiss_blocking_transitions", False)
    on "replaced" action SetVariable("config.dismiss_blocking_transitions", False)

########################################################################################################################
#### YES / NO ###########################################################################################################
########################################################################################################################
screen yesno_prompt(message, yes_action, no_action):
    modal True
    zorder 200
    
    add Solid("#000000") alpha 0.6
    add "gear2" xalign 0.63 yalign 0.655
    add "gear" xalign 0.37 yalign 0.655
    frame:
        style_group "yesno"
        vbox:
            xalign 0.5
            yalign 0.93
            hbox:
                label _(message):
                    xalign 0.5
            null height 18
            hbox:
                xalign 0.5
                imagebutton auto "gui/yesno_yes_%s.png" action yes_action hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True at quick_eff
                null width 60
                imagebutton auto "gui/yesno_no_%s.png" action no_action hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True at quick_eff
    vbox:
        xalign .5
        yalign .408
        add "gui/overlay_title_systemaction.png"
                
    key "game_menu" action no_action
    
########################################################################################################################
#### QUICK MENU #######################################################################################################
########################################################################################################################    
screen quick_menu():
    hbox:
        style_group "quick"
        grid 5 2:
            imagebutton auto "gui/quick_backlog_%s.png" action ShowMenu('text_history') at quick_eff hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True tooltip "Text Backlog"
            imagebutton auto "gui/quick_auto_%s.png" action Preference("auto-forward", "toggle") at quick_eff hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True tooltip "Auto-Forward"
            imagebutton auto "gui/quick_skip_%s.png" action Skip() at quick_eff hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True tooltip "Skip Text"
            imagebutton auto "gui/quick_config_%s.png" action ShowMenu('preferences') at quick_eff hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True tooltip "Options"
            imagebutton auto "gui/quick_mainmenu_%s.png" action MainMenu() at quick_eff hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True tooltip "Main Menu"
            imagebutton auto "gui/quick_qsave_%s.png" action QuickSave() at quick_eff hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True tooltip "Quick Save"
            imagebutton auto "gui/quick_save_%s.png" action ShowMenu('save') at quick_eff hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True tooltip "Save"
            imagebutton auto "gui/quick_qload_%s.png" action QuickLoad() at quick_eff hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True tooltip "Quick Load"
            imagebutton auto "gui/quick_load_%s.png" action ShowMenu('load') at quick_eff hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True tooltip "Load"
            imagebutton auto "gui/quick_codex_%s.png" action [
                SensitiveIf(codex_unlocked), 
                ShowMenu("codex"), 
                SetVariable("codex_navchoice", "codex1"), 
                SetVariable("profile_name", profile_yamato_name), 
                SetVariable("profile_flag", profile_yamato_flag), 
                SetVariable("profile_birthplace", profile_yamato_birthplace), 
                SetVariable("profile_description", profile_yamato_description), 
                SetVariable("profile_type", profile_yamato_type), 
                SetVariable("profile_birthday", profile_yamato_birthday), 
                SetVariable("profile_zodiac", profile_yamato_zodiac), 
                SetVariable("profile_role", profile_yamato_role), 
                SetVariable("profile_height", profile_yamato_height), 
                SetVariable("profile_blood", profile_yamato_blood), 
                SetVariable("profile_drink", profile_yamato_drink), 
                SetVariable("profile_weight", profile_yamato_weight), 
                SetVariable("profile_food", profile_yamato_food), 
                SetVariable("profile_sprite", profile_yamato_sprite)
            ] at quick_eff hover_sound "se/hover.ogg" activate_sound "se/info.ogg" focus_mask True tooltip "Codex"
            
            
            
    $ tooltip = GetTooltip()
    
    if tooltip:
        frame:
            style_group "tooltip2_box"
            vbox:
                xalign 0.5
                yalign 0.5
                text "[tooltip]"
    
########################################################################################################################
#### BONUS #############################################################################################################
########################################################################################################################
screen bonus():
    tag menu2
    frame:
        style_group "bonus"
        xalign 0.498
        yalign 1.017
        vbox:
            hbox:
                textbutton _("New Game") action Show("game_mode") hover_sound "se/hover.ogg" activate_sound "se/click.ogg" at bonus_eff focus_mask True
                textbutton _("Load Data") action [ShowMenu("load"), Stop("mmsound", fadeout=1.0), Stop("mmsound2", fadeout=1.0), Stop("mmsound3", fadeout=1.0)] hover_sound "se/hover.ogg" activate_sound "se/click.ogg" at bonus_eff focus_mask True
                textbutton _("Options") action [ShowMenu("preferences"), Stop("mmsound", fadeout=1.0), Stop("mmsound2", fadeout=1.0), Stop("mmsound3", fadeout=1.0)] hover_sound "se/hover.ogg" activate_sound "se/click.ogg" at bonus_eff focus_mask True
            null height -5
            hbox:
                textbutton _("Gallery") action [ShowMenu("cg_gallery"), Stop("mmsound", fadeout=1.0), Stop("mmsound2", fadeout=1.0), Stop("mmsound3", fadeout=1.0)] hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True at bonus_eff
                textbutton _("Jukebox") action [ShowMenu("music_room"), Stop("mmsound", fadeout=1.0), Stop("mmsound2", fadeout=1.0), Stop("mmsound3", fadeout=1.0)] hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True at bonus_eff
                textbutton _("{image=gui/undo_symbol.png}") action SetScreenVariable("show_mainmenu_nav",True) hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True at bonus_eff top_padding 0
        
########################################################################################################################
#### TEXT HISTORY ######################################################################################################
########################################################################################################################
init -4 python:
    store.text_history_enabled = False
    config.locked = False 
    config.readback_buffer_length = 100 # number of lines stored
    
    config.readback_disallowed_tags = ["size"] # a list of tags that will be removed in the text history
    config.readback_choice_prefix = ">> "   # this is prefixed to the choices the user makes in readback
    # ends adding new config variables
    config.locked = True
    NameList = {
        "Rommel": "side rommel normal",
        "Sovian General": "side soviangeneral normal",
        "Furry Girl": "side rommel normal",
        "Ewalda": im.Sepia("character/side/ewalda_th.png"),
        "Eisenhoo": im.Sepia("character/side/eisenhoo_th.png"),
        "Pattonko": im.Sepia("character/side/patton_th.png"),
        "MacArtha": im.Sepia("character/side/macartha_th.png"),
        "Leopold": im.Sepia("character/side/leopold_th.png"),
        "Blondy": im.Sepia("character/side/blondi_th.png"),
        "Hoth": im.Sepia("character/side/hoth_th.png"),
        "Wild Bear": im.Sepia("character/side/hoth_th.png"),
        "Revolutionary": "side desertaxis normal",
        "Radish Ali": "side desertman normal",
        "Ztauffenborg": "side ztauffenborg normal",
        "Yamamoto": "side yamamoto determined",
        "Zipangu Admiral": "side yamamoto determined",
        "Metaxas": "side metaxas normal",
        "Wounded Soldier": "side man normal",
        "Huntziger": "side franzo normal",
        "Hoppyner": "side hoppyner normal",
        "Petain": "side billotte normal",
        "Wavell": "side wavell normal",
        "Gariboldi": "side gariboldi normal",
        "Vinkelman": "side soldier normal",
        "Old General": "side gariboldi normal",
        "Keitel": im.Sepia("character/side/keitel_th.png"),
        "Quisling": "side quisling normal",
        "Older Man": "side quisling normal",
        "Kanari": im.Sepia("character/side/kanari_th.png"),
        "Ooster": im.Sepia("character/side/ooster_th.png"),
        "Beck": "side beck normal",
        "Mysterious General": "side beck normal",
        "Evan Braun": "side evanbraun evil",
        "Goosetapo Officer": "side gestapo normal",
        "Handsome Stranger": "side evanbraun evil",
        "Rude Ostralasian": "side aussieman normal",
        "Rich Man": "side politician normal",
        "Franzo Soldier": "side franzo normal",
        "Franco": "side basicgeneral happy",
        "Pilot": "side soldier normal",
        "Major": "side germaniangeneral normal",
        "Jorge VI": "side politician2 normal",
        "Zorge": "side politician2 normal",
        "Borkind": "side borkind normal",
        "Peasant Girl": "side woman normal",
        "Valkenhorst": "side valkenhorst normal",
        "Zhina Soldier": "side oriasiangeneral normal",
        "Young Secretary": "side borkind normal",
        "Nygaaaaardsvool": "side politician2 normal",
        "Hess": "side hess normal",
        "Speaker": "side hess normal",
        "Hubala": "side hubal determined",
        "Linge": "side germaniangeneral normal",
        "Luge": "side luge normal",
        "Ironsides": "side basicgeneral normal",
        "Bound": "side oldwoman normal",
        "Norda Soldier": "side norda normal",
        "Lammers": "side politician normal",
        "Teleki": "side official normal",
        "Christian X": "side christian normal",
        "Prior": "side prior normal",
        "Cshima": "side sima normal",
        "Chambers": "side chambers normal",
        "Halifax": "side halifax normal",
        "Polix Soldier": "side polix normal",
        "Sikorskia": "side sikorski normal",
        "Gort": "side gort normal",
        "Dau": "side germanianadmiral normal",
        "Germanian Admiral": "side germanianadmiral normal",
        "Weygand": "side weygand normal",
        "Kirponos": "side kirponos normal",
        "Pavlov": "side pavlov normal",
        "Dimashenka": "side dimashenka normal",
        "Leynaud": "side reynaud normal",
        "Billotte": "side billotte normal",
        "Talatier": "side reynaud normal",
        "Dania Soldier": "side daniayouth normal",
        "Monty": "side monty normal",
        "Yamato": "side yamato",
        "Hitora": "side hitora hat angry",
        "Antoness": "side antoness normal",
        "Redhead Girl": "side antoness normal",
        "Kalinesgu": "side kalinesgu normal",
        "Finbardish Soldier": "side finbard normal",
        "King Garol": "side king normal",
        "Rinni": "side rinni hat normal",
        "Mussorinni": "side rinni hat normal",
        "Starin": "side starin hat normal",
        "Reine": "side roijean hat normal",
        "Leclercia": "side roijean hat normal",
        "Zhukky": "side zhukky hat normal",
        "Goring": "side goring determined",
        "Joebbels": "side joebbels normal",
        "Dunitz": "side dunitz bored",
        "Nyan Katshex": "side nyan normal",
        "Roosevelt": "side roosevelt normal",
        "Churchill": "side churchill hat normal",
        "Cyrano": "side cyrano hat normal",
        "Cute Girl": "side cyrano hat normal",
        "Hirahita": "side hirahita normal",
        "Prince Paulie": "side politician determined",
        "Mannerheim": "side mannerheim normal",
        "Dresckow": "side dresckow normal",
        "Mysterious Man": "side dresckow normal",
        "Tito": "side tito normal",
        "Scrappy Girl": "side tito normal",
        "Wilhelmina": "side kaiser normal",
        "Badoglio": "side badoglio hat normal",
        "Battenia": "side battenia normal",
        "Stuffy": "side stuffy normal",
        "Manstein": "side manstein normal",
        "Pretty Girl": "side manstein normal",
        "Smigly": "side smigly normal",
        "Horthy": "side horthy normal",
        "Guderian": "side guderian normal",
        "Gamelin": "side gamelin normal",
        "Molotov": "side molotov normal",
        "Graziani": "side graziani normal",
        "Vitalian Officer": "side graziani normal",
        "Cavallero": "side cavallero normal",
        "Messe": "side messe normal",
        "Vasile": "side vasile normal",
        "Maletti": "side vitalia normal",
        "Vitalia Soldier": "side vitalia normal",
        "Brookie": "side brookie normal",
        "Jumbo": "side jumbo normal",
        "Haakon": "side haakon normal",
        "Simovic": "side simovic normal",
        "Mihaila": "side mihaila normal",
        "Nega-Hitora": "side negahitora",
        "Hitora?": "side negahitora",
        " ": "character/side/narrator_th.png",
        "Nurse": "side nurse normal",
        "Lieutenant": "side oriasiangeneral normal",
        "Shopkeep": "side fatman normal",
        "Doctor": "side politician normal",
        "Politician": "side politician normal",
        "Short Girl": "side starin hat normal",
        "Voice": "character/side/blank_th.png",
        "Agent": "side agent normal",
        "Attendant": "side official normal",
        "Stachie": "side stachie normal",
        "Trainer": "side fatman normal",
        "Sonny": "side politician normal",
        "Engineer": "side axis normal",
        "Himmora": "character/side/himmora_th.png",
        "Crowd": "character/side/blank_th.png",
        "Everyone": "character/side/blank_th.png",
        "Daughter": "character/side/blank_th.png",
        "Apparition": "character/side/blank_th.png",
        "Freyaborg": im.Sepia("character/side/freyaborg_th.png"),
        "GI Soldier": "side amerika normal",
        "MIB Agent": "side agent normal",
        "King": "side king normal",
        "Dietling": "side dietling normal",
        "Takeshi": "side takeshi normal",
        "Youth": "side youth normal",
        "Official": "side official normal",
        "Vleischer": "side vleischer normal",
        "Maid": "side maid normal",
        "Servant": "side servant1 normal",
        "Brother": "side oldman normal",
        "Fat Man": "side fatman normal",
        "Polix Resister": "side hubal normal",
        "Girl": "side woman normal",
        "Strange Girl": "side zhukky hat moe2",
        "Beauty": "side hirahita normal",
        "Old Man": "side oldman normal",
        "Old Woman": "side oldwoman normal",
        "Man": "side man normal",
        "Gentleman": "side official normal",
        "Woman": "side woman normal",
        "Driver": "side soldier normal",
        "Germanian General": "side germaniangeneral normal",
        "Kaupisch": "side germaniangeneraloberst normal",
        "Listte": "side germaniangeneraloberst normal",
        "Britannian General": "side britanniangeneral normal",
        "Bloody Vasey": "side vasey determined",
        "Iraji General": "side desertgeneral normal",
        "Sovian General": "side soviangeneral normal",
        "Klima": "side klima normal",
        "ZZ Officer": "side zombiegeneral determined",
        "ZZ Soldier": "side zombiesoldier determined",
        "Fake Polix Soldier": "side polixfake determined",
        "Zchaal": "side zchaal normal",
        "Junior": "side takeshi normal",
        "Soldier": "side soldier normal",
        "Zipangu Soldier": "side zipangu normal",
        "Zipanguese Soldier": "side axis normal",
        "Medic": "side axis normal",
        "Axle Soldier": "side axis normal",
        "Germanian Soldier": "side axis normal",
        "Germanian Paratrooper": "side winteraxis normal",
        "Alliance Soldier": "side allied normal",
        "Sovian Soldier": "side sovian normal",
        None: "character/side/narrator_th.png"
    }
                
    def HistoryImage(name = None):
        if name in NameList:
            return NameList[name]
        else:
            #return Null()
            return "character/side/blank_th.png"
    
init -2 python:
    # Two custom characters that store what they said
    class ReadbackADVCharacter(ADVCharacter):
        def do_done(self, who, what):
            store_say(who, what)
            store.current_voice = ''
            return

    class ReadbackNVLCharacter(NVLCharacter):
        def do_done(self, who, what):
            store_say(who, what)
            store.current_voice = ''
            return
            
    # this enables us to show the current line in readback without having to bother the buffer with raw shows
    def say_wrapper(who, what, **kwargs):
        store_current_line(who, what)
        return renpy.show_display_say(who, what, **kwargs)
    config.nvl_show_display_say = say_wrapper
    adv = ReadbackADVCharacter(show_function=say_wrapper)
    nvl = ReadbackNVLCharacter()
    NVLCharacter = ReadbackNVLCharacter
    
    # rewriting voice function to replay voice files when you clicked dialogues in text history screen
    def voice(file, **kwargs):
        if not config.has_voice:
            return
        _voice.play = file
        store.current_voice = file

    # overwriting standard menu handler
    # Overwriting menu functions makes Text History log choice which users choose.
    def menu(items, **add_input): 
        newitems = []
        for label, val in items:
            if val == None:
                narrator(label, interact=False)
            else:
                newitems.append((label, val))
        rv = renpy.display_menu(newitems, **add_input)
        # logging menu choice label.
        for label, val in items:
            if rv == val:
                store.current_voice = ''
                store_say(None, config.readback_choice_prefix + label)
        return rv
    def nvl_screen_dialogue(): 
        """
         Returns widget_properties and dialogue for the current NVL
         mode screen.
         """
        widget_properties = { }
        dialogue = [ ]
        for i, entry in enumerate(nvl_list):
            if not entry:
                continue
            who, what, kwargs = entry
            if i == len(nvl_list) - 1:
                who_id = "who"
                what_id = "what"
                window_id = "window"
            else:
                who_id = "who%d" % i
                what_id = "what%d" % i
                window_id = "window%d" % i
            widget_properties[who_id] = kwargs["who_args"]
            widget_properties[what_id] = kwargs["what_args"]
            widget_properties[window_id] = kwargs["window_args"]
            dialogue.append((who, what, who_id, what_id, window_id))
        return widget_properties, dialogue
        
    # Overwriting nvl menu function
    def nvl_menu(items):
        renpy.mode('nvl_menu')
        if nvl_list is None:
            store.nvl_list = [ ]
        screen = None
        if renpy.has_screen("nvl_choice"):
            screen = "nvl_choice"
        elif renpy.has_screen("nvl"):
            screen = "nvl"
        if screen is not None:
            widget_properties, dialogue = nvl_screen_dialogue()
            rv = renpy.display_menu(
                items,
                widget_properties=widget_properties,
                screen=screen,
                scope={ "dialogue" : dialogue },
                window_style=style.nvl_menu_window,
                choice_style=style.nvl_menu_choice,
                choice_chosen_style=style.nvl_menu_choice_chosen,
                choice_button_style=style.nvl_menu_choice_button,
                choice_chosen_button_style=style.nvl_menu_choice_chosen_button,
                type="nvl",                      
                )
            for label, val in items:
                if rv == val:
                    store.current_voice = ''
                    store_say(None, config.readback_choice_prefix + label)
            return rv
        # Traditional version.
        ui.layer("transient")
        ui.clear()
        ui.close()
        ui.window(style=__s(style.nvl_window))
        ui.vbox(style=__s(style.nvl_vbox))
        for i in nvl_list:
            if not i:
                continue
            who, what, kw = i            
            rv = renpy.show_display_say(who, what, **kw)
        renpy.display_menu(items, interact=False,
                           window_style=__s(style.nvl_menu_window),
                           choice_style=__s(style.nvl_menu_choice),
                           choice_chosen_style=__s(style.nvl_menu_choice_chosen),
                           choice_button_style=__s(style.nvl_menu_choice_button),
                           choice_chosen_button_style=__s(style.nvl_menu_choice_chosen_button),
                           )
        ui.close()
        roll_forward = renpy.roll_forward_info()
        rv = ui.interact(roll_forward=roll_forward)
        renpy.checkpoint(rv)
        for label, val in items:
            if rv == val:
                store.current_voice = ''
                store_say(None, config.readback_choice_prefix + label)
        return rv
    ## readback
    readback_buffer = []
    current_line = None
    current_voice = None
    def side_image(prefix_tag="side"):
        """
        :doc: side_image_function

        Returns the side image associated with the currently speaking character,
        or a Null displayable if no such side image exists.
        """
        name = renpy.get_side_image(prefix_tag, image_tag=config.side_image_tag, not_showing=config.side_image_only_not_showing)
        if name is None:
            return Null()
        else:
            return ImageReference(name)
    def store_say(who, what):
        global readback_buffer, current_voice
        if preparse_say_for_store(what):
            new_line = (preparse_say_for_store(who), preparse_say_for_store(what), current_voice)
            readback_buffer = readback_buffer + [new_line]
            readback_prune()
    def store_current_line(who, what):
        global current_line, current_voice
        current_line = (preparse_say_for_store(who), preparse_say_for_store(what), current_voice)
    # remove text tags from dialogue lines 
    disallowed_tags_regexp = ""
    for tag in config.readback_disallowed_tags:
        if disallowed_tags_regexp != "":
            disallowed_tags_regexp += "|"
        disallowed_tags_regexp += "{"+tag+"=.*?}|{"+tag+"}|{/"+tag+"}"
    import re
    remove_tags_expr = re.compile(disallowed_tags_regexp) # remove tags undesirable in readback
    def preparse_say_for_store(input):
        global remove_tags_expr
        if input:
            return re.sub(remove_tags_expr, "", input)
    def readback_prune():
        global readback_buffer
        while len(readback_buffer) > config.readback_buffer_length:
            del readback_buffer[0]
    
    
init python:
    yvalue = 1.0
    class NewAdj(renpy.display.behavior.Adjustment):
        def change(self,value):
            if value > self._range and self._value == self._range:
                return Return()
            else:
                return renpy.display.behavior.Adjustment.change(self, value)         
    def store_yvalue(y):
        global yvalue
        yvalue = int(y)
        
screen text_history():
    image "gui/transparent2.png"
    image "gui/transparent2.png"
    tag menu
    if not current_line and len(readback_buffer) == 0:
        $ lines_to_show = []
    elif current_line and len(readback_buffer) == 0:
        $ lines_to_show = [current_line]
    elif current_line and not ( ( len(readback_buffer) == 3 and current_line == readback_buffer[-2]) or current_line == readback_buffer[-1]):  
        $ lines_to_show = readback_buffer + [current_line]
    else:
        $ lines_to_show = readback_buffer
    $ adj = NewAdj(changed = store_yvalue, step = 300)
    frame:
        style_group "readback"
        xalign 0.5
        yalign 0.51
        frame:
            style_group "readback2"
            xalign 0.5
            ypadding 20
            xpadding 20
            has viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                yinitial yvalue
                yadjustment adj
                xminimum 1804
                xmaximum 1804
                yminimum 850
                ymaximum 850
                side_xalign .95
                side_yalign .5
            vbox:
                for line in lines_to_show:
                    frame:
                        style_group "readback2"
                        right_padding 50
                        xminimum 1760
                        xmaximum 1760
                        yminimum 210
                        ymaximum 210
                        hbox:
                            style_group "readback"
                            vbox:
                                frame:
                                    style_group "readback2"
                                    add HistoryImage( line[0] )
                            null width 50
                            vbox:
                                yalign .5
                                if line[0] and line[0] != " ":
                                    vbox:
                                        label line[0] # name
                                        null height 5
                                if line[1]:   
                                    # if there's no voice just log a dialogue
                                    if not line[2]:
                                        text line[1]
                                 # else, dialogue will be saved as a button of which plays voice when clicked
                                else: 
                                    textbutton line[1] action Play("voice", line[2] )
                    null height -5
    add "gui/bottom_bar.png" xalign 0.5 yalign 0.98
    hbox:
        style_group "readback"
        xalign 0.5 yalign 1.005
        textbutton _("Return") action Return() hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True at quick_eff
        textbutton _("Save Data") action ShowMenu('save') hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True at quick_eff
        textbutton _("Load Data") action ShowMenu('load') hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True at quick_eff
        textbutton _("Options") action ShowMenu('preferences') hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True at quick_eff
        textbutton _("Main Menu") action MainMenu() hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True at quick_eff
        textbutton _("Quit Game") action Quit(confirm=True) hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True at quick_eff
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
            add "gui/history_bar.png"
            xalign 0.5
            yalign 0.5
    frame:
        background Frame(im.Sepia("gui/outer_frame.png"), 200, 200)
        xminimum 1922
        yminimum 1082
        
########################################################################################################################
#### GAME MODE SCREEN #################################################################################################
########################################################################################################################
screen game_mode():
    modal True
    add Solid("#000000") alpha 0.6
    add "gear2" xalign 0.685 yalign 0.71
    add "gear" xalign 0.315 yalign 0.71
    frame:
        background "gui/overlay_choice_back.png"
        xalign .5
        yalign .5
        xmaximum 1300
        xminimum 1300
        ymaximum 487
        yminimum 487
        yfill False
        xfill False
        hbox:
            xalign 0.54
            yalign 0.89
            imagebutton idle "gui/gamemode_maingame.png" insensitive "gui/gamemode_maingame.png" action [Stop("mmsound", fadeout=1.0), Stop("mmsound2", fadeout=1.0), Stop("mmsound3", fadeout=1.0), Start()] at campaign_eff hover_sound "se/hover.ogg" activate_sound "se/researchui.ogg"
            imagebutton idle "gui/gamemode_nyanquest.png" insensitive "gamemode_nyanquest_insensitive" action [SensitiveIf(persistent.nyan_campaign_unlocked), SetVariable("current_campaign", "campaign_nyanquest"), Hide("game_mode"), Start("campaign_nyanquest")] at campaign_eff hover_sound "se/hover.ogg" activate_sound "se/fightui.ogg"
    vbox:
        xalign 0.828
        yalign 0.298
        imagebutton idle "yesno_no_small_idle" hover "yesno_no_small_hover" action Hide("game_mode") focus_mask True hover_sound "se/hover.ogg" activate_sound "se/click.ogg" at mapicon_eff
    add "gui/overlay_title_selectgame.png":
        xalign 0.5
        yalign 0.352
        
########################################################################################################################
#### CAMPAIGN SCREEN #################################################################################################
########################################################################################################################
screen campaign_selection():
    tag menu
    add "campaignselection_back"
    vbox:
        xalign 0.177
        yalign 0.59
        viewport:
            scrollbars "vertical"
            xmaximum 820
            xminimum 820
            ymaximum 670
            yminimum 670
            yalign 0.5
            side_yalign .5
            side_ymaximum 600
            side_spacing 0
            draggable True
            mousewheel True
            arrowkeys True
            vbox:
                xalign 0.5
                yalign 0.5
                add "gui/campaign_main_bar.png"
                frame:
                    background None
                    xsize 780
                    xpadding 20
                    ypadding 16
                    xalign 0.5
                    yalign 0.5
                    text "The main story, detailing the exploits of Commander Yamato Yamamoto as he battles his way across Europa.":
                        size 20
                        text_align 0.5
                if not conquest_campaign_completed:
                    imagebutton idle "gui/campaign_conquest.png" insensitive "gui/campaign_insensitive.png" action [Show("level_selection")] at campaign_eff hover_sound "se/hover.ogg" activate_sound "se/equip.ogg" hovered [Show("campaign_hitora_rinni"), Hide("campaign_yamato")] unhovered [Hide("campaign_hitora_rinni"), Show("campaign_yamato")]
                else:
                    add "campaign_conquest_complete"
                null height 5
                if not resistance_campaign_completed:
                    imagebutton idle "gui/campaign_resistance.png" insensitive "gui/campaign_insensitive.png" action [SensitiveIf(resistance_campaign_unlocked), SetVariable("current_campaign", "campaign_resistance"), Jump("campaign_resistance")] at campaign_eff hover_sound "se/hover.ogg" activate_sound "se/fightui.ogg" hovered [Show("campaign_cyrano_churchill"), Hide("campaign_yamato")] unhovered [Hide("campaign_cyrano_churchill"), Show("campaign_yamato")]
                else:
                    add "campaign_resistance_complete"
                null height 5
                imagebutton idle "gui/campaign_totalwar.png" insensitive "gui/campaign_insensitive.png" action [SensitiveIf(totalwar_campaign_unlocked), SetVariable("current_campaign", "campaign_totalwar"), Jump("campaign_totalwar")] at campaign_eff hover_sound "se/hover.ogg" activate_sound "se/fightui.ogg" hovered [Show("campaign_starin"), Hide("campaign_yamato")] unhovered [Hide("campaign_starin"), Show("campaign_yamato")]
                null height 10
                add "gui/campaign_side_bar.png"
                frame:
                    background None
                    xsize 780
                    xpadding 20
                    ypadding 16
                    xalign 0.5
                    yalign 0.5
                    text "Extra optional campaigns that are unlocked throughout. Play to enhance the plot and gameplay of the main game.":
                        size 20
                        text_align 0.5
                if not evan_campaign_completed:
                    imagebutton idle "gui/campaign_evan.png" insensitive "gui/campaign_insensitive.png" action [SensitiveIf(evan_campaign_unlocked), SetVariable("current_campaign", "campaign_evan"), Jump("campaign_evan")] at campaign_eff hover_sound "se/hover.ogg" activate_sound "se/fightui.ogg" hovered [Show("campaign_hitora_yamato"), Hide("campaign_yamato")] unhovered [Hide("campaign_hitora_yamato"), Show("campaign_yamato")]
                else:
                    add "campaign_evan_complete"
                null height 5
                if not tito_campaign_completed:
                    imagebutton idle "gui/campaign_tito.png" insensitive "gui/campaign_insensitive.png" action [SensitiveIf(tito_campaign_unlocked), SetVariable("current_campaign", "campaign_tito"), Jump("campaign_tito")] at campaign_eff hover_sound "se/hover.ogg" activate_sound "se/fightui.ogg" hovered [Show("campaign_churchill_rinni"), Hide("campaign_yamato")] unhovered [Hide("campaign_churchill_rinni"), Show("campaign_yamato")]
                else:
                    add "campaign_tito_complete"
    vbox:
        xalign 0.543
        yalign 0.107
        imagebutton idle "yesno_no_small_idle" hover "yesno_no_small_hover" action MainMenu() focus_mask True hover_sound "se/hover.ogg" activate_sound "se/click.ogg" at mapicon_eff

    on "show" action Show("campaign_yamato")
    on "replace" action Show("campaign_yamato")
    on "hide" action [Hide("campaign_yamato"), Hide("campaign_starin"), Hide("campaign_hitora_rinni"), Hide("campaign_cyrano_churchill"), Hide("campaign_hitora_yamato"), Hide("campaign_churchill_rinni")]
    on "replaced" action [Hide("campaign_yamato"), Hide("campaign_starin"), Hide("campaign_hitora_rinni"), Hide("campaign_cyrano_churchill"), Hide("campaign_hitora_yamato"), Hide("campaign_churchill_rinni")]
    
screen campaign_hitora_rinni():
    vbox:
        add "character/hitora/campaign_hitora.png" at campaign_characters_eff
        xalign 0.8
        yalign 0
    vbox:
        add "character/rinni/campaign_rinni.png" at campaign_characters_eff
        xalign 1.7
        yalign 0.1
        
screen campaign_hitora_yamato():
    vbox:
        add "character/hitora/campaign_hitora.png" at campaign_characters_eff
        xalign 0.8
        yalign 0
    vbox:
        add "character/campaign_yamato.png" at campaign_characters_eff
        xalign 1.22
        yalign 0
        
screen campaign_yamato():
    vbox:
        add "character/campaign_yamato.png" at campaign_characters_eff
        xalign 1.0
        yalign 0
        
screen campaign_starin():
    vbox:
        add "character/starin/campaign_starin.png" at campaign_characters_eff
        xalign 1.15
        yalign 0.3

screen campaign_cyrano_churchill():
    vbox:
        add "character/churchill/campaign_churchill.png" at campaign_characters_eff
        xalign 1.4
        yalign 0
    vbox:
        add "character/cyrano/campaign_cyrano.png" at campaign_characters_eff
        xalign 0.98
        yalign 0.2
        
screen campaign_churchill_rinni():
    vbox:
        add "character/churchill/campaign_churchill.png" at campaign_characters_eff
        xalign 0.85
        yalign 0
    vbox:
        add "character/rinni/campaign_rinni.png" at campaign_characters_eff
        xalign 1.7
        yalign 0.1
    
########################################################################################################################
#### LEVEL SELECTION SCREEN ###########################################################################################
########################################################################################################################
screen level_selection():
    modal True
    add Solid("#000000") alpha 0.6
    add "gear2" xalign 0.685 yalign 0.71
    add "gear" xalign 0.315 yalign 0.71
    frame:
        background "gui/overlay_choice_back.png"
        xalign .5
        yalign .5
        xmaximum 1300
        xminimum 1300
        ymaximum 487
        yminimum 487
        yfill False
        xfill False
        hbox:
            xalign 0.54
            yalign 0.89
            imagebutton idle "gui/levelselection_easy.png" action [SetVariable("cp_levelset", 60), SetVariable("max_cp_levelset", 60), SetVariable("cp", 650), SetVariable("max_cp", 650), SetVariable("level_choice", 1), SetVariable("current_campaign", "campaign_conquest"), Hide("level_selection"), Hide("campaign_selection"), Jump("campaign_conquest")] at campaign_eff hover_sound "se/hover.ogg" activate_sound "se/fightui.ogg" tooltip level_easy_tooltip
            imagebutton idle "gui/levelselection_normal.png" action [SetVariable("cp_levelset", 50), SetVariable("max_cp_levelset", 50), SetVariable("cp", 500), SetVariable("max_cp", 500), SetVariable("level_choice", 2), SetVariable("current_campaign", "campaign_conquest"), Hide("level_selection"), Hide("campaign_selection"), Jump("campaign_conquest")] at campaign_eff hover_sound "se/hover.ogg" activate_sound "se/fightui.ogg" tooltip level_normal_tooltip
            imagebutton idle "gui/levelselection_expert.png" action [SetVariable("cp_levelset", 40), SetVariable("max_cp_levelset", 40), SetVariable("cp", 350), SetVariable("max_cp", 350), SetVariable("level_choice", 3), SetVariable("current_campaign", "campaign_conquest"), Hide("level_selection"), Hide("campaign_selection"), Jump("campaign_conquest")] at campaign_eff hover_sound "se/hover.ogg" activate_sound "se/fightui.ogg" tooltip level_hard_tooltip
    vbox:
        xalign 0.828
        yalign 0.298
        imagebutton idle "yesno_no_small_idle" hover "yesno_no_small_hover" action [Hide("level_selection"), Hide("campaign_hitora_rinni"), Show("campaign_yamato")] focus_mask True hover_sound "se/hover.ogg" activate_sound "se/unequip.ogg" at mapicon_eff
    add "gui/overlay_title_battledifficulty.png":
        xalign 0.5
        yalign 0.352
        
    $ tooltip = GetTooltip()
    
    if tooltip:
        frame:
            style_group "tooltip3_box"
            vbox:
                xalign 0.5
                yalign 0.5
                text "[tooltip]"
        
