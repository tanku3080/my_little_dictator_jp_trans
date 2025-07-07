#----------------------------------------------------------------------------------------------------------------------------------------------------------
###MENU GRAPHICS
#----------------------------------------------------------------------------------------------------------------------------------------------------------
########################################################
# Menu Images #################################################
########################################################
image splash = "gui/logo.png"
image cds = "gui/cds.png"

image sepiabrown:
    Solid("#704214")
    alpha 0.5

image black_fade:
    Solid(color("#000000"))
    alpha 0.7

image display_image = ConditionSwitch(
    "current_image == 1", "gui/display1.png",
    "current_image == 2", "gui/display2.png",
    "current_image == 3", "gui/display3.png",
    "current_image == 4", "gui/display4.png")

image display_image_overlay = ConditionSwitch(
    "temp_image == 1", "gui/display1.png",
    "temp_image == 2", "gui/display2.png",
    "temp_image == 3", "gui/display3.png",
    "temp_image == 4", "gui/display4.png",
    "temp_image == 5", im.MatrixColor("gui/display1.png", im.matrix.opacity(0.0) * im.matrix.tint(1.0, 0.1, 0.1)))

image nav_logo = LiveComposite((442, 172), (0, 0), im.FactorScale("gui/logo_shadow.png", 0.5), (21, 21), im.FactorScale("gui/logo2.png", 0.5))

image nav_chibi_random:
    choice:
        im.FactorScale("character/chibi/chibi_zhukky.png", 0.35)
    choice:
        im.FactorScale("character/chibi/chibi_churchill.png", 0.35)
    choice:
        im.FactorScale("character/chibi/chibi_cyrano.png", 0.35)
    choice:
        im.FactorScale("character/chibi/chibi_hitora.png", 0.35)
    choice:
        im.FactorScale("character/chibi/chibi_starin.png", 0.35)
    choice:
        im.FactorScale("character/chibi/chibi_rinni.png", 0.35)

image dis_chibi_random:
    choice:
        "character/chibi/chibi_zhukky.png"
    choice:
        "character/chibi/chibi_churchill.png"
    choice:
        "character/chibi/chibi_cyrano.png"
    choice:
        "character/chibi/chibi_hitora.png"
    choice:
        "character/chibi/chibi_starin.png"
    choice:
        "character/chibi/chibi_rinni.png"
        
image disclaimer:
    contains:
        "black"
    contains:
        xalign 1.12
        yalign 0.5
        "dis_chibi_random"
    contains:
        xalign 0.2 
        yalign 0.4
        Fixed(Text(["[disclaimer_text]"], size=24, outlines=[(1, "#000000", 0, 0)], text_align=0.5, color="#FFFFFF", drop_shadow=None), xsize=1050, ysize=750)
    contains:
        xalign 0.2
        yalign 0.92
        Fixed(Text(["© 2022 WarGirl Games, All Rights Reserved, My Little Dictator and all elements thereof"], size=20, outlines=[(1, "#000000", 0, 0)], text_align=0.5, color="#FFFFFF", drop_shadow=None), xsize=1050, ysize=50)

image post_disclaimer:
    contains:
        "black"
    contains:
        xalign 0.5
        yalign 0.55
        Fixed(Text(["[post_disclaimer_text]"], size=24, outlines=[(1, "#000000", 0, 0)], text_align=0.5, color="#FFFFFF", drop_shadow=None), xsize=1050, ysize=200)
        
image splashready:
    contains:
        "black"
    contains:
        xalign 0.5
        "rotater"
    contains:
        "fire4"
    contains:
        Frame(im.Sepia("gui/outer_frame.png"), 200, 200)
        
image mainmenu_back:
    contains:
        "black"
    contains:
        im.MatrixColor("back/map/westernmap.jpg", im.matrix.desaturate() * im.matrix.tint(1.0, 0.1, 0.1))
    contains:
        im.MatrixColor("gui/transparent2.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.8, 0.8)) 
        alpha 0.7
    contains:
        "rotater"
        xalign 0.5
    contains:
        "fire4"
    contains:
        "spark"
    contains:
        Frame(im.Sepia("gui/outer_frame.png"), 200, 200)
        
image campaignselection_back:
    contains:
        "black"
    contains:
        im.MatrixColor("back/map/westernmap.jpg", im.matrix.desaturate() * im.matrix.tint(1.0, 0.1, 0.1))
    contains:
        im.MatrixColor("gui/transparent2.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.8, 0.8)) 
        alpha 0.7
    contains:
        "rotater"
        xalign 0.5
    contains:
        "fire4"
    contains:
        "spark"
    contains:
        "gui/campaign_selection.png"
        xalign 0.12
        yalign 0.49
    contains:
        Frame(im.Sepia("gui/outer_frame.png"), 200, 200)
        
image gamemode_nyanquest_insensitive:
    im.Sepia("gui/gamemode_nyanquest.png")
    alpha 0.6
    
image campaign_conquest_complete = LiveComposite(
    (781, 169),
    (0, 0), Transform(im.Sepia("gui/campaign_conquest.png"), alpha=0.4),
    (190, 30), "gui/map/mission_status_success.png")
    
image campaign_resistance_complete = LiveComposite(
    (781, 169),
    (0, 0), Transform(im.Sepia("gui/campaign_resistance.png"), alpha=0.4),
    (190, 30), "gui/map/mission_status_success.png")
    
image campaign_evan_complete = LiveComposite(
    (781, 169),
    (0, 0), Transform(im.Sepia("gui/campaign_evan.png"), alpha=0.4),
    (190, 30), "gui/map/mission_status_success.png")
    
image campaign_tito_complete = LiveComposite(
    (781, 169),
    (0, 0), Transform(im.Sepia("gui/campaign_tito.png"), alpha=0.4),
    (190, 30), "gui/map/mission_status_success.png")
    
        
image rotater = At(im.FactorScale("gui/spin.png", 1.2), rotater_anim) 
image gear = At("gui/gear.png", rotater_anim2)
image gear2 = At("gui/gear.png", rotater_anim3)
image logo = At("gui/logo2.png", logointro_eff)
image logo_shadow = At("gui/logo_shadow.png", logoshadow_eff)

image side logo_th:
    HBox(Null(width=15), VBox(im.FactorScale(im.Sepia("gui/logo2.png"), 0.4), Null(height=60)))
    alpha 0.3
image gmroot = "balcony"
image ctc1:
    anim.Filmstrip("gui/ctc.png", (40, 40), (12, 1), .10, xpos=0.743, ypos=0.945, xanchor=0, yanchor=0)
    
image battle_reload_icon =At(im.FactorScale(im.Crop("gui/undo_symbol.png", (0, 10, 30, 30)), 1.5), rotater_anim4)
    
########################################################
# Chibi #################################################
########################################################
image title_tank:
    contains:
        im.FactorScale("character/panzer.png", 0.4)
        rotate 0
        
image title_ship:
    contains:
        im.FactorScale("character/ship.png", 0.35)
        rotate 0

image title_planes:
    contains:
        im.FactorScale("back/sky/junker2.png", 0.55)
        rotate 0
        
image title_planes2:
    contains:
        im.FactorScale("back/sky/junker2.png", 0.3)
        rotate 0
        
image title_planes3:
    contains:
        im.FactorScale("back/sky/junker2.png", 0.22)
        rotate 0

image title_vrocket_left = "gui/vrocket_left.png"
image title_vrocket_right = "gui/vrocket_right.png"

image title_chibi:
    contains:
        im.FactorScale("character/chibi/chibi_zhukky.png", 0.5)
        xalign 0.84
        yalign 0.85
        rotate 25
    contains:
        im.FactorScale("character/chibi/chibi_rinni.png", 0.55)
        xalign 0.2
        yalign 0.75
        rotate -20
    contains:
        im.FactorScale("character/chibi/chibi_cyrano.png", 0.65)
        xalign 0.83
        yalign 0.75
        rotate 15
    contains:
        im.FactorScale("character/chibi/chibi_starin.png", 0.75)
        xalign 0.27
        yalign 0.4
        rotate -10
    contains:
        im.FactorScale("character/chibi/chibi_churchill.png", 0.78)
        xalign 0.77
        yalign 0.35
        rotate 5
    contains:
        im.FactorScale("character/chibi/chibi_hitora.png", 0.9)
        xalign 0.5
        ypos -0.15
        rotate 0

image mainmenu_animation:
    contains:
        "title_planes3" 
        xzoom -1
        yalign 0.7
        ypos 0.85
        xpos -0.4
        alpha 0
        0.8
        linear 0.5 xpos -0.66 ypos 0.68 alpha 0.9
    contains:
        "title_planes3"
        yalign 0.7
        xpos 0.4
        ypos 0.85
        alpha 0
        0.8
        linear 0.5 xpos 0.66 ypos 0.68 alpha 0.9
    contains:
        "title_planes2" 
        xzoom -1
        yalign 0.7
        ypos 0.85
        xpos -0.4
        alpha 0
        0.8
        linear 0.5 xpos -0.8 ypos 0.7 alpha 0.9
    contains:
        "title_planes2"
        yalign 0.7
        xpos 0.4
        ypos 0.85
        alpha 0
        0.8
        linear 0.5 xpos 0.8 ypos 0.7 alpha 0.9
    contains:
        "title_planes" 
        xzoom -1
        yalign 0.7
        ypos 0.85
        xpos -0.4
        alpha 0
        0.8
        linear 0.5 xpos -0.57 ypos 0.66 alpha 0.9
    contains:
        "title_planes"
        yalign 0.7
        xpos 0.4
        ypos 0.85
        alpha 0
        0.8
        linear 0.5 xpos 0.57 ypos 0.65 alpha 0.9
    contains:
        "title_vrocket_left"
        xalign 0.5
        yalign 1.5
        0.6
        linear 0.5 yalign 0.65
        linear 0.5 xalign 0.07 yalign 0.45
    contains:
        "title_vrocket_right"
        xalign 0.5
        yalign 1.5
        0.6
        linear 0.5 yalign 0.65
        linear 0.5 xalign 0.93 yalign 0.45
    contains:
        "title_ship"
        xzoom -1
        xalign 0.5
        ypos 1.2
        xpos 0.1
        alpha 0
        0.3
        linear 0.5 ypos 0.28 alpha 1.0
        linear 0.3 xpos -0.13
    contains:
        "title_ship"
        xalign 0.5
        xpos 0.9
        alpha 0
        ypos 1.2
        0.3
        linear 0.5 ypos 0.28 alpha 1.0
        linear 0.3 xpos 1.13
    contains:
        "title_chibi"
        xalign 0.48
        ypos 1.5
        0.2
        linear 0.8 ypos -0.02
    contains:
        "title_tank"
        xzoom -1
        xalign 0.5
        ypos 1.4
        0.2
        linear 0.5 ypos 0.5
        linear 0.5 xalign 0.1
    contains:
        "title_tank"
        xalign 0.5
        ypos 1.4
        0.2
        linear 0.5 ypos 0.5
        linear 0.5 xalign 0.9
        
########################################################
# Colors #################################################
########################################################
image white = Solid(color("#FFFFFF"))
image black = Solid(color("#000000"))
image codexback = Solid(color("#241F18"))

########################################################
# Transparents #################################################
########################################################
image transparent = "gui/transparent1.png" 
image transparent2 = "gui/transparent2.png"

########################################################
# Act Labels #################################################
########################################################
image main_frame = Frame(im.Sepia("gui/outer_frame.png"), 200, 200)
image prologue:
    contains:
        im.MatrixColor("back/map/westernmap.jpg", im.matrix.desaturate() * im.matrix.tint(1.0, 0.1, 0.1))
        xalign 0.5
        yalign 0.5
    contains:
        im.MatrixColor("gui/transparent2.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.8, 0.8))
        alpha 0.7
    contains:
        "rotater"
        xalign 0.5
    contains:
        "fire4"
    contains:
        "spark"
    contains:
        "gui/prologue.png"
        xalign 0.5
        yalign 0.5
    contains:
        Frame(im.Sepia("gui/outer_frame.png"), 200, 200)
        
image actone:
    contains:
        im.MatrixColor("back/map/westernmap.jpg", im.matrix.desaturate() * im.matrix.tint(1.0, 0.1, 0.1))
        xalign 0.5
        yalign 0.5
    contains:
        im.MatrixColor("gui/transparent2.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.8, 0.8))
        alpha 0.7
    contains:
        "rotater"
        xalign 0.5
    contains:
        "fire4"
    contains:
        "spark"
    contains:
        "gui/act1_back.png"
    contains:
        "gui/act1.png"
        xalign 0.2
        yalign 0.5
    contains:
        im.MatrixColor("character/chibi/chibi_hitora.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.9, 0.8))
        xalign 1.0
        yalign 0.5
    contains:
        Frame(im.Sepia("gui/outer_frame.png"), 200, 200)
        
image acttwo:
    contains:
        im.MatrixColor("back/map/westernmap.jpg", im.matrix.desaturate() * im.matrix.tint(1.0, 0.1, 0.1))
        xalign 0.5
        yalign 0.5
    contains:
        im.MatrixColor("gui/transparent2.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.8, 0.8))
        alpha 0.7
    contains:
        "rotater"
        xalign 0.5
    contains:
        "fire4"
    contains:
        "spark"
    contains:
        "gui/act2_back.png"
    contains:
        "gui/act2.png"
        xalign 0.2
        yalign 0.5
    contains:
        im.MatrixColor("character/chibi/chibi_zhukky.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.9, 0.8))
        xalign 1.0
        yalign 0.5
    contains:
        Frame(im.Sepia("gui/outer_frame.png"), 200, 200)
        
image actthree:
    contains:
        im.MatrixColor("back/map/westernmap.jpg", im.matrix.desaturate() * im.matrix.tint(1.0, 0.1, 0.1))
        xalign 0.5
        yalign 0.5
    contains:
        im.MatrixColor("gui/transparent2.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.8, 0.8))
        alpha 0.7
    contains:
        "rotater"
        xalign 0.5
    contains:
        "fire4"
    contains:
        "spark"
    contains:
        "gui/act3_back.png"
    contains:
        "gui/act3.png"
        xalign 0.2
        yalign 0.5
    contains:
        im.MatrixColor("character/chibi/chibi_cyrano.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.9, 0.8))
        xalign 1.0
        yalign 0.5
    contains:
        Frame(im.Sepia("gui/outer_frame.png"), 200, 200)
        
image actfour:
    contains:
        im.MatrixColor("back/map/westernmap.jpg", im.matrix.desaturate() * im.matrix.tint(1.0, 0.1, 0.1))
        xalign 0.5
        yalign 0.5
    contains:
        im.MatrixColor("gui/transparent2.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.8, 0.8))
        alpha 0.7
    contains:
        "rotater"
        xalign 0.5
    contains:
        "fire4"
    contains:
        "spark"
    contains:
        "gui/act4_back.png"
    contains:
        "gui/act4.png"
        xalign 0.2
        yalign 0.5
    contains:
        im.MatrixColor("character/chibi/chibi_rinni.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.9, 0.8))
        xalign 1.0
        yalign 0.5
    contains:
        Frame(im.Sepia("gui/outer_frame.png"), 200, 200)
        
image actfive:
    contains:
        im.MatrixColor("back/map/westernmap.jpg", im.matrix.desaturate() * im.matrix.tint(1.0, 0.1, 0.1))
        xalign 0.5
        yalign 0.5
    contains:
        im.MatrixColor("gui/transparent2.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.8, 0.8))
        alpha 0.7
    contains:
        "rotater"
        xalign 0.5
    contains:
        "fire4"
    contains:
        "spark"
    contains:
        "gui/act5_back.png"
    contains:
        "gui/act5.png"
        xalign 0.2
        yalign 0.5
    contains:
        im.MatrixColor("character/chibi/chibi_churchill.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.9, 0.8))
        xalign 1.0
        yalign 0.5
    contains:
        Frame(im.Sepia("gui/outer_frame.png"), 200, 200)
        
image actsix:
    contains:
        im.MatrixColor("back/map/westernmap.jpg", im.matrix.desaturate() * im.matrix.tint(1.0, 0.1, 0.1))
        xalign 0.5
        yalign 0.5
    contains:
        im.MatrixColor("gui/transparent2.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.8, 0.8))
        alpha 0.7
    contains:
        "rotater"
        xalign 0.5
    contains:
        "fire4"
    contains:
        "spark"
    contains:
        "gui/act6_back.png"
    contains:
        "gui/act6.png"
        xalign 0.2
        yalign 0.5
    contains:
        im.MatrixColor("character/chibi/chibi_starin.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.9, 0.8))
        xalign 1.0
        yalign 0.5
    contains:
        Frame(im.Sepia("gui/outer_frame.png"), 200, 200)
        
image epilogue:
    contains:
        im.MatrixColor("back/map/westernmap.jpg", im.matrix.desaturate() * im.matrix.tint(1.0, 0.1, 0.1))
        xalign 0.5
        yalign 0.5
    contains:
        im.MatrixColor("gui/transparent2.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.8, 0.8))
        alpha 0.7
    contains:
        "rotater"
        xalign 0.5
    contains:
        "fire4"
    contains:
        "spark"
    contains:
        "gui/epilogue.png"
        xalign 0.5
        yalign 0.5
    contains:
        Frame(im.Sepia("gui/outer_frame.png"), 200, 200)
        
image theend:
    contains:
        "black"
    contains:
        "gui/the_end.png"
        xalign 0.5
        yalign 0.5

########################################################
# Credits #################################################
########################################################
image creditback = im.Sepia("gui/creditsback.jpg")
image creditanimation:
    contains:
        xalign 1.3 yalign -0.55
        anim.Filmstrip(im.Sepia("battle/units/commander_yamato_walk.png"), (177, 258), (4, 1), .2)
        pause 191
        linear 63 yalign 1.45 xalign -0.5
        
    contains:
        choice:
            anim.Filmstrip(im.Sepia("battle/units/panzer_maus_walk.png"), (840, 840), (3, 1), .2)
        choice:
            anim.Filmstrip(im.Sepia("battle/units/panzer_t35_walk.png"), (840, 840), (3, 1), .2)
        choice:
            anim.Filmstrip(im.Sepia("battle/units/panzer_charfcm_walk.png"), (840, 840), (3, 1), .2)
        xalign 1.7 yalign -2.8
        pause 172
        linear 60 yalign 3.1 xalign -0.8
        
    contains:
        choice:
            anim.Filmstrip(im.Sepia("battle/units/panzer_somuas35_walk.png"), (840, 840), (3, 1), .2)
        choice:
            anim.Filmstrip(im.Sepia("battle/units/panzer_charb1_walk.png"), (840, 840), (3, 1), .2)
        choice:
            anim.Filmstrip(im.Sepia("battle/units/panzer_su100_walk.png"), (840, 840), (3, 1), .2)
        xalign 1.7 yalign -2.8
        pause 155
        linear 60 yalign 3.1 xalign -0.8
        
    contains:
        choice:
            anim.Filmstrip(im.Sepia("battle/units/panzer_stug4_walk.png"), (840, 840), (3, 1), .2)
        choice:
            anim.Filmstrip(im.Sepia("battle/units/panzer_valentine_walk.png"), (840, 840), (3, 1), .2)
        choice:
            anim.Filmstrip(im.Sepia("battle/units/panzer_churchill_walk.png"), (840, 840), (3, 1), .2)
        xalign 1.7 yalign -2.8
        pause 140
        linear 60 yalign 3.1 xalign -0.8
        
    contains:
        choice:
            anim.Filmstrip(im.Sepia("battle/units/panzer_kv1_walk.png"), (840, 840), (3, 1), .2)
        choice:
            anim.Filmstrip(im.Sepia("battle/units/panzer_tiger_walk.png"), (840, 840), (3, 1), .2)
        choice:
            anim.Filmstrip(im.Sepia("battle/units/panzer_semovente_walk.png"), (840, 840), (3, 1), .2)
        xalign 1.7 yalign -2.8
        pause 125
        linear 60 yalign 3.1 xalign -0.8
        
    contains:
        choice:
            anim.Filmstrip(im.Sepia("battle/units/panzer_bt42_walk.png"), (840, 840), (3, 1), .2)
        choice:
            anim.Filmstrip(im.Sepia("battle/units/panzer_toldi_walk.png"), (840, 840), (3, 1), .2)
        choice:
            anim.Filmstrip(im.Sepia("battle/units/panzer_turan_walk.png"), (840, 840), (3, 1), .2)
        xalign 1.7 yalign -2.8
        pause 110
        linear 60 yalign 3.1 xalign -0.8
        
    contains:
        choice:
            anim.Filmstrip(im.Sepia("battle/units/panzer_panzer4_walk.png"), (840, 840), (3, 1), .2)
        choice:
            anim.Filmstrip(im.Sepia("battle/units/antitank_t13_walk.png"), (840, 840), (3, 1), .2)
        choice:
            anim.Filmstrip(im.Sepia("battle/units/panzer_crusader_walk.png"), (840, 840), (3, 1), .2)
        xalign 1.7 yalign -2.8
        pause 95
        linear 60 yalign 3.1 xalign -0.8

    contains:
        choice:
            anim.Filmstrip(im.Sepia("battle/units/panzer_matilda1_walk.png"), (840, 840), (3, 1), .2)
        choice:
            anim.Filmstrip(im.Sepia("battle/units/panzer_panzer3_walk.png"), (840, 840), (3, 1), .2)
        choice:
            anim.Filmstrip(im.Sepia("battle/units/panzer_kv2_walk.png"), (840, 840), (3, 1), .2)
        xalign 1.7 yalign -2.8
        pause 80
        linear 60 yalign 3.1 xalign -0.8
        
    contains:
        choice:
            anim.Filmstrip(im.Sepia("battle/units/panzer_t34_walk.png"), (840, 840), (3, 1), .2)
        choice:
            anim.Filmstrip(im.Sepia("battle/units/panzer_panzer2_walk.png"), (840, 840), (3, 1), .2)
        choice:
            anim.Filmstrip(im.Sepia("battle/units/panzer_l335_walk.png"), (840, 840), (3, 1), .2)
        xalign 1.7 yalign -2.8
        pause 65
        linear 60 yalign 3.1 xalign -0.8
        
    contains:
        choice:
            anim.Filmstrip(im.Sepia("battle/units/panzer_7tp_walk.png"), (840, 840), (3, 1), .2)
        choice:
            anim.Filmstrip(im.Sepia("battle/units/panzer_panzer1_walk.png"), (840, 840), (3, 1), .2)
        choice:
            anim.Filmstrip(im.Sepia("battle/units/panzer_renaultft_walk.png"), (840, 840), (3, 1), .2)
        xalign 1.7 yalign -2.8
        pause 50
        linear 60 yalign 3.1 xalign -0.8
            
    contains:
        xalign 1.0 yalign -0.55
        anim.Filmstrip(im.Sepia("battle/units/infantry_germania_gunner_heer1_walk.png"), (126, 243), (4, 1), .2)
        pause 44
        linear 60 yalign 1.45 xalign -0.65
        
    contains:
        xalign 1.25 yalign -0.55
        anim.Filmstrip(im.Sepia("battle/units/infantry_germania_gunner_heer1_walk.png"), (126, 243), (4, 1), .2)
        pause 39
        linear 60 yalign 1.45 xalign -0.4
        
    contains:
        xalign 1.5 yalign -0.55
        anim.Filmstrip(im.Sepia("battle/units/infantry_germania_gunner_heer1_walk.png"), (126, 243), (4, 1), .2)
        pause 34
        linear 60 yalign 1.45 xalign -0.15
        
    contains:
        xalign 1.0 yalign -0.55
        anim.Filmstrip(im.Sepia("battle/units/commander_guderian_walk.png"), (177, 260), (4, 1), .2)
        pause 35
        linear 60 yalign 1.45 xalign -0.65
        
    contains:
        xalign 1.25 yalign -0.55
        anim.Filmstrip(im.Sepia("battle/units/commander_rommel_walk.png"), (177, 260), (4, 1), .19)
        pause 30
        linear 60 yalign 1.45 xalign -0.4
        
    contains:
        xalign 1.5 yalign -0.55
        anim.Filmstrip(im.Sepia("battle/units/commander_nyan_walk.png"), (177, 258), (4, 1), .17)
        pause 25
        linear 60 yalign 1.45 xalign -0.15
        
    contains:
        xalign 1.075 yalign -0.55
        anim.Filmstrip(im.Sepia("battle/units/commander_monty_walk.png"), (177, 260), (4, 1), .2)
        pause 25
        linear 60 yalign 1.45 xalign -0.525
        
    contains:
        xalign 1.325 yalign -0.55
        anim.Filmstrip(im.Sepia("battle/units/commander_roijean_walk.png"), (177, 258), (4, 1), .18)
        pause 20
        linear 60 yalign 1.45 xalign -0.275
        
    contains:
        xalign 1 yalign -0.55
        anim.Filmstrip(im.Sepia("battle/units/commander_rinni_walk.png"), (177, 260), (4, 1), .2)
        pause 20
        linear 60 yalign 1.45 xalign -0.65
        
    contains:
        xalign 1.25 yalign -0.55
        anim.Filmstrip(im.Sepia("battle/units/commander_starin_walk.png"), (177, 260), (4, 1), .17)
        pause 15
        linear 60 yalign 1.45 xalign -0.4
        
    contains:
        xalign 1.5 yalign -0.55
        anim.Filmstrip(im.Sepia("battle/units/commander_zhukky_walk.png"), (177, 260), (4, 1), .2)
        pause 10
        linear 60 yalign 1.45 xalign -0.15
        
    contains:
        xalign 1.075 yalign -0.45
        anim.Filmstrip(im.Sepia("battle/units/commander_churchill_walk.png"), (177, 258), (4, 1), .18)
        pause 10
        linear 60 yalign 1.35 xalign -0.525
        
    contains:
        xalign 1.325 yalign -0.45
        anim.Filmstrip(im.Sepia("battle/units/commander_cyrano_walk.png"), (177, 258), (4, 1), .19)
        pause 5
        linear 60 yalign 1.35 xalign -0.275
        
    contains:
        xalign 1.2 yalign -0.45
        anim.Filmstrip(im.Sepia("battle/units/commander_hitora_walk.png"), (177, 260), (4, 1), .2)
        linear 60 yalign 1.35 xalign -0.4
        
init python:
    special_thanks = u"""#Domi-Sama 
0$kull 
3epo
Aaron - Exiled WereSheep in Torment
aaron corff
Abdulaziz Al-Kaboor
ABruneianKickstarterBacker
Agus Hartono
AKASlaphappy
Akures
Alexander Hartmann
Alexander Hilyard
Alexander Kimball
Alexander Mason
Alexander White
Alexis Perron
Alfred C. Glassell III
Allen92
Almicha 
AlmostHuman
Anaël Verrier
Andokar 
Andrew Juljenjai
Angelo Vos
Anne Nonymous
Antonio Carbone
Apprentice Sysadmin of Gensokyo
Aqualuft Games
Arie Hofland
Austin Stanley
BakaMage 
Bas van G
Ben Knuchel
Benjamin Moorman
bigbistro
biskmater 
Blackheaven 
Blake O'Brien
BlueDecember 
Bradley 
Bradley Holt
Brian McCain
BrioCyrain 
Bruno Santos
Bryan Russowsky
bryce 
bugrom
Butter-T 
Carim 
Carlo Spinale
CherryWood 
Chris
Chris Aziz
Chris Bastion
Christian Ortner
Christopher Gebhart
Christopher J Headley
Cody 
Cody Spence
Colin Gogian
Cory F.
cory lester
Cosmic Cooking Hunter 77
Cristobal Mera
Crusader Flame
Cythna
Daniel Chiem
Daniel Lin
Daniel Zielinski
Darjeeling 
Darrell Hawkins
David Long
David Telles
Davram 
Dawn
Denovo 
Desu Nyan Uguu
Diaboros
DieGottschalk
DKDevil
Dokaeris 
Dominic Ivey
Donald Ferris
Dorago 
Draco
Drew 
E. T. Young
Edward T.
Edwin Kam
Emmi Kaarlampi
Encrypted12345
EntomaRays
Eric
Eric Christofferson
Erich Sheogorath
Erwan Hellouin
Ethan Ritzert
Evan Collins
Fahmi Fauzi
Far2close - Visual Novel Playthroughs
Fenrir12 
Flavio Reis
Florizzare
Francisco Garcia
Gabriel Ma
GameOn Dev
Gareth Edwards
Garrett Muggy
Garric
gekiganwing
Genesis Echanes
Glaring Mistake
Gralorn
Greg Polander
Gregor Hoogstad
Guillaume Lebigot
Gunnar Hogberg
Gustavo Capelli
Hans Christian Solberg
Harminder
Harrison Bailey
HAXNEF 
Haz 
Henry Tran
Hunter
Hussain Ahmadi
HWaie 
Icewolf999 
inguma 
Ivron
Iwan C. A. Smith: Knight of Lord British
Ixere
Izkda
Jacob Marsden
Jacob Prestage
James
James Kahalewai III 
James Lofshult ((Solav))
Jared Boese
Jarred Nation
Jason
Jason Sperber
Jason Zapasnik
Jean-Paul Trevino
Jesse Mckay Corbin
jimmy chou
Joanna Horosky
Joannes808 
John Allen IV
John Truong
Jordan Minh-Anh Cognard
Jorden Theodore Fredrick Leis
Jos Liliendahl Hansen
Joseph Lilonsky
Joshua
Joshua Carroll
Joshua Santini
Julian 
Kamil Rydzewski
Karbunos
Karl Lassen
Kaulu 
Kiejzar
Klotsz
KM_Yamato 
Konsulus
KraHa~n 
Kristan Heisken
KV
L 
Lachlan
Laurence Stratton
Laurent Patillon
Ledabot
Leeland Zary
Lester Cruz
Louis Le Vau
Lucas Rosseto Giglioti
Luke Michel
Lyle Schwartz
Magnificent Beard
Manuel Loeffler
Marco Kroening
Marcus Soll
Mark Douglas
Martin
mASSter 
Mathew Fang
Matthew Clark
Matthew De Leon
Matthew Jacob Chua Wepee
Matthew Ley
Matthew Myers
Matthew Schupack
Max Sibrits
Mazikeen Wagner
Mecatronico
Meepsheep
Megan Yee
Melon
Michael Brand
Michael Connell
Michael Gantz
Michael Grubmüller
Michael J. Vanecek
Miguel De serpa
Miguel Morales
Mikael Knall
Minh Thai
Mitchell Jobe
Mr.Quija
Mud 
N/A 
Narazumo 
Nathan Lee
Nathaniel Pahl
NEET Operative
Neil Elcome
NekoKuchi 
Ng Kian Chuan
NGUYEN Remy
Nicholas A Bryant
Nico B
Nigrow
Novangel
Nuclear IL-2
Nykyta Zolf Yuzkov
Oberon's Paradox
OfficialJab
Olivier Lebeau-Paradis
Olof Johansson Ström
Onery
Ott3r 
Pal Miller
paranoidkitten
Party Commissar
Patrick Ellis
Paul H
Paul 'Vaendryl'
Peo01
Per Kristian Brastad
Peter Schnare
Piichimi
Priscilla Dustbunny
promontoryID 
puncake
qtR
QuakeRiley
qw 
raemz
Rainiel Bangkig
Redcomet
Reforced
Reginald Hebert
Reiji Tsusaka
Remi Andre Borgen
Revontulet
Revontulet1982 
Rewind 
Reya
Richard Ford
Rigrot
Robert McNaughton
roger templeton
Ryan Erickson
S.J.
Sam
Sam Garamy
Samuel Foster
Samu-kun
Sazriel 
Scott Hazlett, Cold Beverage Studios
SDude 
Sean Murphy
Sean Titmarsh
Sebastian de With
sgebad 
Shinobi
Silentwatcher
SilverWasp
Simo Nyyssönen
Sir Sovy
Sneko
SomeRandomName
Squall Systems
Standstill
Stefan Brender
Stefan Ebner
Stephen Lemelin
Steven Holt
Steven Kolenberg
Steven Lord
Steven Michael Quast
Sven
T. J. F.
Takasu 
Tamamo No Mae
Tannan
TeeraTaa Shiro
Teru
Th3Crew
The Loli Assassin
Thomas Bixenmann
Thomas Palka
Thomas Zilling
Tim 
Tim Reilly
Tim Thacher
Timmothy Clarke
Tom Donnelly
Tom Rothamel
Torolf - Alchemist of the Obsidian Order
tropicalmonsoon
Tsuki
Tyler
Tyler Stone
Umbra
USRPG
VaporGuey 
Varik 
Venron
Vincent Nougier
Vítězslav Konečný
Võ Tran Triet
WAK37 
Wexmajor
White Silver
Will Bryant
William Orgek
Wim Looman
windFx 
Yamato
YP Lim
Zack Wood
Zaelthul
Zantetsu
Zuripai Games
Zweckon
Leet Music
Blue Wolfie Music
PyTom
The entire team at CDS
Kickstarter
Patreon
Valve
The Hyperspace Forums
Lemmasoft Forums
Google Fonts
Font Squirrel
Ikaros Publications
...and anyone else we haven't mentioned.
\n \n 
And an additional, huge thank you to all our patient backers and fans, across all platforms, throughout the world!
\n \n 
"""
        
    sound_attributions = u"""\n
'Spitfire and B-17 Taxi by', Fight2FlyPhoto (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/Fight2FlyPhoto/sounds/142897/
\n
'Two Spitfires Flyby', Fight2FlyPhoto (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/Fight2FlyPhoto/sounds/142901/
\n
'Spitfires and Bf-109 Flyby', Fight2FlyPhoto (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/Fight2FlyPhoto/sounds/142902/
\n
'Machine Gun Burst 50 Cal', Mike Koenig (soundbible.com) licensed under CC BY 3.0 License / Modified and mixed
https://soundbible.com/1228-Machine-Gun-Burst-50-Cal.html
\n
'Automatic Machine Gun 3x', Mike Koenig (soundbible.com) licensed under CC BY 3.0 License / Modified and mixed
https://soundbible.com/1201-Automatic-Machine-Gun-3x.html
\n
'mp 38 schmeisser (Variations) WW2', Lubini (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/Lubini/sounds/338046/
\n
'Applaus - Seminar, kurz', BockelSound (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/BockelSound/sounds/488175/
\n
'Apple Bite', Simon Craggs (soundbible.com) licensed under CC BY 3.0 License / Modified and mixed
https://soundbible.com/1968-Apple-Bite.html
\n
'High Definition Machine Gun', WEL (soundbible.com) licensed under CC BY 3.0 License / Modified and mixed
https://soundbible.com/1575-High-Definition-Machine-Gun.html
\n
'Bath - Body emerging', Sirderf (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/Sirderf/sounds/332282/
\n
'Bath - Body movements', Sirderf (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/Sirderf/sounds/332280/
\n
'Gun Battle Sound', ReamProductions (soundbible.com) licensed under CC BY 3.0 License / Modified and mixed
https://soundbible.com/2078-Gun-Battle-Sound.html
\n
'flak blast 1', Piotr123 (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/Piotr123/sounds/551533/
\n
'Distant WW2 Gunfire Kent', Cheeseheadburger (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/Cheeseheadburger/sounds/170478/
\n
'PPSh-41 - Soviet Submachine Gun', Lubini (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/Lubini/sounds/338323/
\n
'Street Battle: Lviv Ukraine - WW1 Reconstruction', Lubini (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/Lubini/sounds/337773/
\n
'Battle Sound Effects ~ Siren, Storm, Vocals, Explosions', DudeAwesome (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/DudeAwesome/sounds/385846/
\n
'Angry_Mob', unchaz (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/unchaz/sounds/150954/
\n
'Multi Groan 2', vtownpunks (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/vtownpunks/sounds/63631/
\n
'20060810petersclock01', dobroide (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/dobroide/sounds/21934/
\n
'Air Raid Soundscape', CGEffex (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/CGEffex/sounds/93843/
\n
'Cave ambience', Little Robot Sound Factory (zapsplat.com) licensed under CC BY 4.0 License / Modified and mixed
https://www.zapsplat.com/music/cave-ambience/
\n
'stuka01', Sphyrna (freesound.org) licensed under Sampling+ License / Modified and mixed
https://freesound.org/people/Sphyrna/sounds/69189/
\n
'FDoor Open And Close', rivernile7 (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/rivernile7/sounds/234244/
\n
'Door Opening', Hitrison (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/Hitrison/sounds/198869/
\n
'Sliding Wooden Door', Evil-Dog (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/Evil-Dog/sounds/265338/
\n
'elephant voice 44', y89312 (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/y89312/sounds/139875/
\n
'Fire_Forest_Inferno', Dynamicell (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/Dynamicell/sounds/17548/
\n
'Water Mill (Golspie Mill, Scotland)', Albrecht Ihlenburg (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/borralbi/sounds/342822/
\n
'Spooky Large Sliding Metal Door', kernschall (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/kernschall/sounds/411108/
\n
'Ba-da-dum', Simon_Lacelle (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/Simon_Lacelle/sounds/37215/
\n
'Ham Radio Bands - 80mHams', kwahmah_02 (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/kwahmah_02/sounds/254526/
\n
'Singing Birds 2 - (Kouri Forest - Salonika)', Ali@k (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/Ali@k/sounds/156562/
\n
'Wolf run', sabotovat (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/sabotovat/sounds/414350/
\n
'sarahbuzzer.mp3', nofeedbak (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/nofeedbak/sounds/21871/
\n
'vibraslap_small02.wav', soundbytez (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/soundbytez/sounds/99241/
\n
'greece_naxos_cicadas_1', sbordage (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/sbordage/sounds/126741/
\n
'Tank', snottyboy (soundbible.com) licensed under CC BY 3.0 License / Modified and mixed
https://soundbible.com/1325-Tank.html
\n
'Warcry Yarghh! - British Male', theuncertainman (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/theuncertainman/sounds/402645/
\n
'Success Resolution Video Game Fanfare Sound Effect', FunWithSound (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/FunWithSound/sounds/456968/
\n
'Retro 8-bit game, hero death', Little Robot Sound Factory (zapsplat.com) licensed under CC BY 4.0 License / Modified and mixed
https://www.zapsplat.com/music/retro-8-bit-game-hero-death/
\n
'Video Game Death Sound Effect', harrietniamh (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/harrietniamh/sounds/415079/
\n
'Machine Gun', BlastwaveFX (soundbible.com) licensed under CC BY 3.0 License / Modified and mixed
https://soundbible.com/640-Machine-Gun.html
\n
'Fantasy game, spell 00', Little Robot Sound Factory (zapsplat.com) licensed under CC BY 4.0 License / Modified and mixed
https://www.zapsplat.com/music/fantasy-game-spell-00/
\n
'Fantasy game, spell 01', Little Robot Sound Factory (zapsplat.com) licensed under CC BY 4.0 License / Modified and mixed
https://www.zapsplat.com/music/fantasy-game-spell-01/
\n
'Ueno Shamisen - Japan', RTB45 (freesound.org) licensed under CC BY 3.0 License / Modified and mixed
https://freesound.org/people/RTB45/sounds/195521/
\n
'Armistice Centenary Match (+ Vickers MG Shoot)', The Full 9 (thefull9.net) licensed under CC BY 4.0 License / Modified and mixed
https://www.youtube.com/watch?v=2tqN5HXmUW8
\n
Additional sound effects from https://www.zapsplat.com
\n \n 
"""

image creditscroll:
    contains:
        alpha 0
        yalign 0.48
        xalign 0.5
        "gui/logo2.png"
        0.5
        linear 1.0 alpha 1.0
        3.0
        linear 3.9 ypos 0.0 yanchor 1.0
    contains:    
        Text([      
        "{size=-10}Created by{/size} \nDesertFox \n \n \n",
        "\n{size=-10}Executive Producers{/size} \nSteven Michael Quast \nLaurence Stratton \n \n \n",
        "\n{size=-10}Writing{/size} \nDesertFox \n \n \n",
        "\n{size=-10}Character Artwork{/size} \nGreenTeaNeko \n \n \n",
        "\n{size=-10}CG Artwork{/size} \nGreenTeaNeko \n \n \n",
        "\n{size=-10}Collateral Damage Studios Producer{/size} \nNg Kian Chuan \n \n \n",
        "\n{size=-10}Background Artwork{/size} \nBadriel \n \n \n",
        "\n{size=-10}Pixel Artwork{/size} \nRBL \nIevgen Khomenko \n \n \n",
        "\n{size=-10}Concept Art{/size} \nGreenTeaNeko \nArtist_Anonymous \n \n \n",
        "\n{size=-10}Additional Artwork{/size} \nbonkiru \nDesertFox \n \n \n",
        "\n{size=-10}Battle Engine Programming{/size} \nDragoonHP \n \n \n",
        "\n{size=-10}Bulk Programming{/size} \nDesertFox \n \n \n",
        "\n{size=-10}Proofreading{/size} \nHistoryGuy \n \n \n",
        "\n{size=-10}Original Music{/size} \nBelgerum \n \n \n",
        "\n{size=-10}OP Theme Song{/size} \n{i}'Battlefield of Love'{/i} \n{size=-10}Music and Lyrics{/size} \nMatthew Myers \n{size=-10}Vocals{/size} \nSneko \n{size=-10}Produced by{/size} \nLeet Music \n \n \n",
        "\n{size=-10}ED Theme Song{/size} \n{i}'Rise'{/i} \n{size=-10}Music{/size} \nBlue Wolfie Music \n{size=-10}Lyrics{/size} \nMegan Yee \n{size=-10}Vocals{/size} \nMegan Yee \n{size=-10}Produced by{/size} \nBlue Wolfie Music \n \n \n",
        "\n{size=-10}Sound Design{/size} \nDesertFox \n \n \n",
        "\n{size=-10}Beta Testing{/size} \nAWOL \nCharles Flyingpad \nEonymia \nFinnishTheFin \nHistoryGuy \nMatthew Warren \nNaej Niluomud \nPal Miller \nRonnie Powell \nVerthand \n \n \n",
        "\n{size=-10}Special Thanks{/size}\n[special_thanks]\n \n \n",
        ], outlines=[(2, "#000000", 0, 0)], size=40, drop_shadow=None, text_align=0.5, color="#FFFFFF", xsize=1100)
        anchor (0.5, 0.0)
        pos (0.5, 1.0)
        pause 3.5
        linear 173.0 ypos 0.0 yanchor 1.0
    contains:    
        Text([      
        "\n{size=-10}Sound Attributions{/size} {size=-16}\n[sound_attributions]{/size}\n \n \n",
        "\n{size=-10}Artwork Attributions{/size} {size=-16}\n \n'Uboat VIIC', splatypi (blendswap.com) licensed under CC BY / Modified \n https://www.blendswap.com/blend/15004 \n \n'Ladoga Karelia terrain', Finnish Wartime Photograph Archive (SA-Kuva) licensed under CC BY 4.0 / Modified \nhttps://en.wikipedia.org/wiki/File:Ladoga_Karelia_terrain.jpg \n \n'Peenemünde, Germany', t.przechlewski (commons.wikimedia.org) licensed under CC BY 3.0 / Modified \n https://commons.wikimedia.org/wiki/File:Peenem%C3%BCnde,_Germany_-_panoramio_(1).jpg \n \n'Vexiloid of the Roman Empire', Ssolbergj (commons.wikimedia.org) licensed under CC BY 3.0 / Modified \n https://commons.wikimedia.org/wiki/File:Vexiloid_of_the_Roman_Empire.PNG \n \n'Ship's deck and railing', Richard George Davis (deviantart.com), licensed under CC BY 3.0 / Modified \n https://www.deviantart.com/richardgeorgedavis \n{/size} \n \n",
        "\n{size=-10}Built using the{/size} \nRen'Py Engine \n \n \n",
        "\n{size=-18}[disclaimer_text] \n{/size} \n \n \n",
        "\n{size=-18}© 2022 WarGirl Games, All Rights Reserved, \nMy Little Dictator and all elements thereof{/size} \n \n \n",
        "\n{size=-5}{image=gui/logo.png}{/size}\n",
        "\n{size=-10}© 2013-2022 WarGirl Games\nwar-girl.com{/size} \n \n \n",
        "\n{size=-5}{image=gui/cds.png}{/size}\n",
        "\n{size=-10}C.D.S Collateral Damage Studios\ncollateralds.com{/size} \n \n \n",
        "\n{size=-3}Thanks for playing!{/size} \n \n \n \n"  
        ], outlines=[(2, "#000000", 0, 0)], size=40, drop_shadow=None, text_align=0.5, color="#FFFFFF", xsize=1000)
        anchor (0.5, 0.0)
        pos (0.5, 1.0)
        pause 169
        linear 92.0 ypos 0.0 yanchor 1.0    
        
    
########################################################
# Objects #################################################
########################################################
image black_lines = "gui/black_lines.png"
image black_lines2:
    contains:
        "black"
        size (1920, 200)
        yalign 0
        alpha 0.97
    contains:
        "black"
        size (1920, 300)
        yalign 1.0
        alpha 0.97

