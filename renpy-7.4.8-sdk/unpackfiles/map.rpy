
########################################################################################################################
#### MAP SCREEN #######################################################################################################
########################################################################################################################
python:
    vp = ui.viewport(draggable=True, mousewheel=True, xmaximum=1200, ymaximum=600, child_size=(1920, 1080))
    ui.fixed() 
    for button in menu_buttons:
        ui.textbutton (button[0], clicked = button[1], background=None)
        ui.imagebutton (button[0], clicked = button[1], background=None)
        ui.close()
        ui.bar(adjustment=vp.xadjustment, style='scrollbar')
        ui.bar(adjustment=vp.yadjustment, style='vscrollbar')
        ui.close()

init python:
    class ScreenData(object):
        def __init__(self, geographic_map, political_map, eastern_map):
            self.geographic_map = geographic_map
            self.political_map = political_map
            self.eastern_map = eastern_map
            self.map = political_map
            
#init python:
    #import pygame
    #def dd_cursor_position(st, at):
        #x, y = renpy.get_mouse_pos()
        #return Text("{size=-5}%d - %d"%(x, y)), .1
        
#screen debug_tools():
    #zorder 10**10
    #add DynamicDisplayable(dd_cursor_position) xpos 10 yalign 0.1

screen invasion_markers():
    for key, value in sorted(active_invasionbeacons_items.items()):
        vbox:
            xalign value[3] yalign value[4]
            imagebutton action [
                SetVariable("mapcontinue", key), 
                SetVariable("q_description", value[0]), 
                SetVariable("q_title", value[1]), 
                SetVariable("q_type", value[2]), 
                Show("qbox")
            ] idle "in_idle" hover "in_hover" focus_mask True hover_sound "se/hover.ogg" activate_sound "se/fightui.ogg"
        
screen city_markers():
    for key, value in active_maptown_items.items():
        vbox:
            xalign value[23] yalign value[24]
            if value[20]:
                imagebutton idle "map_marker_insensitive" hover "map_marker_insensitive" action NullAction() hovered Show("siege_tooltip") unhovered Hide("siege_tooltip")
            elif not value[18]:
                imagebutton idle "map_marker_insensitive" hover "map_marker_insensitive" action NullAction() hovered Show("unlocktown_tooltip") unhovered Hide("unlocktown_tooltip")
            else:
                imagebutton action [
                    SetVariable("maptown_profileimg", key), 
                    SetVariable("maptown_name", value[0]), 
                    SetVariable("maptown_size", value[1]), 
                    SetVariable("maptown_governor", value[2]), 
                    SetVariable("maptown_governor_pic", value[3]), 
                    SetVariable("maptown_hostility", value[4]), 
                    SetVariable("maptown_alignment", value[5]), 
                    SetVariable("maptown_population", value[6]), 
                    SetVariable("maptown_publicorder", value[7]), 
                    SetVariable("maptown_influence", value[8]),
                    SetVariable("maptown_command", value[9]), 
                    SetVariable("maptown_management", value[10]), 
                    SetVariable("maptown_farming_worth", value[11]), 
                    SetVariable("maptown_mining_worth", value[12]),
                    SetVariable("maptown_industry_worth", value[13]), 
                    SetVariable("maptown_trade_worth", value[14]), 
                    SetVariable("maptown_entertainment_worth", value[15]), 
                    SetVariable("maptown_military_worth", value[16]), 
                    SetVariable("maptown_corruption_worth", value[17]), 
                    SetVariable("maptown_unlocktown", value[18]), 
                    SetVariable("maptown_martial", value[19]), 
                    SetVariable("maptown_siege", value[20]), 
                    SetVariable("maptown_company_img", value[21]), 
                    SetVariable("maptown_company_text", value[22]),
                    Show("maptown")
                ] idle "map_marker_idle" hover "map_marker_hover" insensitive "map_marker_insensitive" focus_mask True hover_sound "se/hover.ogg" activate_sound "se/maptown.ogg"

screen wonder_markers():
    for key, value in active_mapwonders_items.items():
        vbox:
            xalign value[6] yalign value[7]
            imagebutton action [
                SetVariable("wonder_name", value[0]), 
                SetVariable("wonder_location", value[1]), 
                SetVariable("wonder_description", value[2]), 
                SetVariable("wonder_condition", value[3]), 
                SetVariable("wonder_icon", value[4]), 
                SetVariable("wonder_image", value[5]),
                Show("wonder")
            ] idle (key  + "_big_idle") hover (key + "_big_hover") focus_mask True hover_sound "se/hover.ogg" activate_sound "se/wonder.ogg" at mapicon_eff
    
screen viewport1(mapdata):
    viewport id "vp":
        style_group "capitalstext"
        edgescroll (150, 150)
        xmaximum 1900
        ymaximum 890
        ypos 0.09
        draggable True
        mousewheel False
        child_size (2500, 2500)
        add mapdata.map
        if not mapdata.map == mapdata.eastern_map:
            use wonder_markers
            use city_markers
            use invasion_markers
        
screen mapchoice1(mapdata):
    tag menu
    add "black"
    vbox:
        xalign 0.5
        yalign 0.1
        use viewport1(mapdata)
    add "gui/bottom_bar.png" xalign 0.5 yalign 0.98
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
            add "gui/map_bar.png"
            xalign 0.5
            yalign 0.5
    vbox:
        style_group "maptype"
        xalign 0.5 yalign 0.969
        hbox:
            textbutton _("Allegiances Map") action SetField(mapdata, "map", mapdata.political_map) hover_sound "se/hover.ogg" activate_sound "se/section.ogg" focus_mask True at mapicon_eff
            textbutton _("Geographic Map") action SetField(mapdata, "map", mapdata.geographic_map) hover_sound "se/hover.ogg" activate_sound "se/section.ogg" focus_mask True at mapicon_eff
            textbutton _("Oriasia Map") action SetField(mapdata, "map", mapdata.eastern_map) hover_sound "se/hover.ogg" activate_sound "se/section.ogg" focus_mask True at mapicon_eff
            textbutton _("Mission Log") action Show("qlog") hover_sound "se/hover.ogg" activate_sound "se/info.ogg" focus_mask True at mapicon_eff
            textbutton _("Factions Log") action Show("map1allegiances") hover_sound "se/hover.ogg" activate_sound "se/info.ogg" focus_mask True at mapicon_eff
    frame:
        background Frame(im.Sepia("gui/outer_frame.png"), 200, 200)
    if map_update_happen:
        timer 0.1 action Show("map_update")
    $ renpy.block_rollback()
    
    key "h" action NullAction()

########################################################################################################################
#### MAP TOOLTIPS ######################################################################################################
########################################################################################################################
screen unlocktown_tooltip():
    frame:
        style_group "maptooltip"
        xalign 0.04
        yalign 0.12
        text "This city's information hasn't been unlocked yet.":
            xalign 0.5
            text_align 0.5
        
screen siege_tooltip():
    frame:
        style_group "maptooltip"
        xalign 0.04
        yalign 0.12
        text "This city is under siege.":
            xalign 0.5
            text_align 0.5
        

        
        
        
