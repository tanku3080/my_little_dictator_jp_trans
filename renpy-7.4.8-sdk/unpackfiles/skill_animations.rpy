


#VARIABLE TRANSFORMS
transform skill_move(start=(0,0), end=(800,800), dur=5.0):
    pos start
    linear dur pos end

transform displaying_sprite_delay():
    alpha 1.0
    
transform displaying_sprite_delay_secondary():
    alpha 1.0
    
transform flip_horizontal():
    xzoom -1
        
transform blank():
    alpha 0
    
transform flash_stat_trans():
    alpha 1.0
    rotate 0
    parallel:
        linear 0.2 rotate 1
        linear 0.4 rotate -2
        linear 0.2 rotate 1
        repeat
    parallel:
        linear 0.35 alpha 0.5
        linear 0.35 alpha 1.0
        pause 0.3
        repeat
    
transform shake():
    xalign 0.5
    yalign 0.5
    parallel:
        linear 0.02 xpos 0.555
        linear 0.02 xpos 0.455
        repeat
        
transform runover():
    xalign 0.5
    yalign 0.5
    parallel:
        linear 0.07 xpos 0.555
        linear 0.07 xpos 0.455
        repeat
        
transform dive():
    xalign 0.5
    yalign 0.5
    parallel:
        linear 0.03 rotate 10
        linear 0.03 rotate 0
        linear 0.03 rotate -10
        linear 0.03 rotate 0
        repeat
        
transform glowfade():
    alpha 1.0
    parallel:
        linear 0.35 alpha 0.5
        linear 0.35 alpha 1.0
        pause 0.3
        repeat
        
transform damaged():
    alpha 1.0
    parallel:
        linear 0.35 alpha 0.5
        linear 0.35 alpha 1.0
        pause 0.3
        repeat
    parallel:
        linear 0.01 xpos 0.005
        linear 0.01 xpos -0.005
        linear 0.01 xpos -0.005
        linear 0.01 xpos 0.005
        repeat
        
transform deathfade():
    alpha 1.0
    parallel:
        linear 0.35 alpha 0.3
        linear 0.35 alpha 0
        pause 0.3
        repeat
    parallel:
        linear 0.01 xpos 0.005
        linear 0.01 xpos -0.005
        linear 0.01 xpos -0.005
        linear 0.01 xpos 0.005
        repeat
        
transform phasein():
    alpha 0
    linear 0.3 xzoom 1.5 alpha 0.5 xalign 0.5
    linear 0.3 xzoom 1 alpha 0
    repeat
    
transform phaseout():
    xalign 0.5
    yalign 0.5
    parallel:
        linear 0.02 xpos 0.655
        linear 0.02 xpos 0.355
        repeat
    parallel:
        alpha 0
        linear 0.3 xzoom 1.5 alpha 0.5 xalign 0.5
        linear 0.3 xzoom 1 alpha 0
        repeat
        
transform deathskulls():
    alpha 1.0
    parallel:
        contains:
            "battle/skills/skull.png"
            xalign 0.65
            yalign 0.65
            zoom 1.0
            alpha 0
            linear 0.7 alpha 1.0 yalign 0.5
            linear 0.7 alpha 0 yalign 0.35
            repeat
        contains:
            "battle/skills/skull.png"
            xalign 0.35
            yalign 0.75
            zoom 0.8
            alpha 0
            linear 0.6 alpha 1.0 yalign 0.7
            linear 0.6 alpha 0 yalign 0.55
            repeat
        contains:
            "battle/skills/skull.png"
            xalign 0.45
            yalign 0.45
            zoom 0.3
            alpha 0
            linear 0.5 alpha 1.0 yalign 0.3
            linear 0.5 alpha 0 yalign 0.15
            repeat
        contains:
            "battle/skills/skull.png"
            xalign 0.53
            yalign 0.53
            zoom 0.4
            alpha 0
            linear 0.4 alpha 1.0 yalign 0.38
            linear 0.4 alpha 0 yalign 0.23
            repeat
        contains:
            "battle/skills/skull.png"
            xalign 0.57
            yalign 0.75
            zoom 0.65
            alpha 0.3
            linear 0.5 alpha 1.0 yalign 0.69
            linear 0.5 alpha 0 yalign 0.54
            repeat
        
transform getready_loadin_trans():
    alpha 0.8
    pause 4.2
    linear 0.2 alpha 0
    
transform getready_trans():
    xalign 0.5
    yalign 0.5
    alpha 0
    zoom 0
    pause 0.7
    alpha 1.0
    linear 0.1 zoom 1.0
    pause 0.9
    linear 0.3 yalign -0.5 alpha 0
    
transform getready_second_trans():
    xalign 0.5
    yalign 0.5
    alpha 0
    zoom 0
    pause 2.5
    alpha 1.0
    linear 0.1 zoom 1.0
    pause 0.9
    linear 0.3 yalign -0.5 alpha 0
    
image getready_blackbars:
    parallel:
        contains:
            Solid("#000000")
            xalign 0.5
            yalign 0
            size (1920, 220)
            alpha 1.0
            pause 3.8
            linear 2.0 yalign -0.5
        contains:
            Solid("#000000")
            xalign 0.5
            yalign 1.0
            size (1920, 220)
            alpha 1.0
            pause 3.8
            linear 2.0 yalign 1.5
    
transform intro_trans():
    xalign 0.7 alpha 0
    pause 0.6
    linear 0.1 xalign 0.5 alpha 1.0
    pause 2.3
    linear 0.1 xalign 0.3 alpha 0
    
transform intro_reverse_trans():
    xalign 0.3 alpha 0
    pause 0.6
    linear 0.1 xalign 0.5 alpha 1.0
    pause 2.3
    linear 0.1 xalign 0.7 alpha 0
    
transform switch_trans():
    xalign 0.7 alpha 0
    pause 4.4
    linear 0.1 xalign 0.5 alpha 1.0
    pause 2.3
    linear 0.1 xalign 0.3 alpha 0
    
transform switch_reverse_trans():
    xalign 0.3 alpha 0
    pause 4.4
    linear 0.1 xalign 0.5 alpha 1.0
    pause 2.3
    linear 0.1 xalign 0.7 alpha 0

transform intro_fade():
    alpha 0
    linear 0.5 alpha 1.0
    
transform full_spin():
    rotate 0
    linear 1.0 rotate -360
    repeat
    
transform full_reverse_spin():
    rotate 0
    linear 2.0 rotate 360
    repeat
    

    
#OFFENSIVE ANIMATIONS
image offensive_gunfire_back:
    anim.Filmstrip("battle/skills/gunfire.png", (60, 60), (2, 2), .03, xalign=0.5, yalign=0.5)
    xzoom -1
    yzoom -1
    
image offensive_gunfire_front:
    anim.Filmstrip("battle/skills/gunfire.png", (60, 60), (2, 2), .03, xalign=0.5, yalign=0.5)

image offensive_gunfire_big_back:
    anim.Filmstrip("battle/skills/gunfire_big.png", (120, 120), (2, 2), .03, xalign=0.5, yalign=0.5)
    xzoom -1
    yzoom -1
    
image offensive_gunfire_big_front:
    anim.Filmstrip("battle/skills/gunfire_big.png", (120, 120), (2, 2), .03, xalign=0.5, yalign=0.5)
    
image offensive_cannonblast_back:
    anim.Filmstrip("battle/skills/cannonblast_back.png", (498, 498), (4, 5), .05, loop=False, xalign=0.5, yalign=0.5)

image offensive_cannonblast_front:
    anim.Filmstrip("battle/skills/cannonblast_front.png", (498, 498), (4, 5), .05, loop=False, xalign=0.5, yalign=0.5)
    
image offensive_mediumcannonblast_back:
    anim.Filmstrip("battle/skills/mediumcannonblast_back.png", (332, 332), (4, 5), .05, loop=False, xalign=0.5, yalign=0.5)

image offensive_mediumcannonblast_front:
    anim.Filmstrip("battle/skills/mediumcannonblast_front.png", (332, 332), (4, 5), .05, loop=False, xalign=0.5, yalign=0.5)
    
image offensive_smallcannonblast_back:
    anim.Filmstrip("battle/skills/smallcannonblast_back.png", (166, 166), (4, 5), .05, loop=False, xalign=0.5, yalign=0.5)

image offensive_smallcannonblast_front:
    anim.Filmstrip("battle/skills/smallcannonblast_front.png", (166, 166), (4, 5), .05, loop=False, xalign=0.5, yalign=0.5)

image offensive_launcherblast_back:
    anim.Filmstrip("battle/skills/launcherblast_back.png", (498, 498), (4, 5), .05, loop=False, xalign=0.5, yalign=0.5)
    
image offensive_launcherblast_front:
    anim.Filmstrip("battle/skills/launcherblast_front.png", (498, 498), (4, 5), .05, loop=False, xalign=0.5, yalign=0.5)
    
image offensive_bouncingbomb_back:
    anim.Filmstrip("battle/skills/bouncingbomb.png", (80, 62), (4, 1), .02)
    xalign 0.25 yalign 0.4 alpha 0 zoom 1.0
    linear 0.01 alpha 1
    linear 0.35 xalign 0.5 yalign 0.04 zoom 0.95
    linear 0.15 xalign 0.7 yalign 0.2 zoom 0.9
    linear 0.01 alpha 0
    pause 4.0
    alpha 0
    
image offensive_bouncingbomb_front:
    anim.Filmstrip("battle/skills/bouncingbomb.png", (80, 62), (4, 1), .02)
    xalign 0.2 yalign 0.35 alpha 0 zoom 0.9
    linear 0.01 alpha 1
    linear 0.45 xalign -0.15 yalign 0.34 zoom 0.95
    linear 0.25 xalign -0.3 yalign 0.6 zoom 1.0
    linear 0.01 alpha 0
    pause 4.0
    alpha 0  
    
image offensive_hurricane_back:
    anim.Filmstrip("battle/skills/hurricane.png", (145, 85), (2, 1), .02)
    xalign 0.25 yalign 0.38 alpha 0 zoom 1 xzoom -1 yzoom -1
    linear 0.01 alpha 1
    linear 0.25 xalign 0.7 yalign 0.18 zoom 0.9
    linear 0.01 alpha 0
    pause 0.3
    repeat 1
    
image offensive_hurricane_front:
    anim.Filmstrip("battle/skills/hurricane.png", (145, 85), (2, 1), .02)
    xalign 0.2 yalign 0.35 alpha 0 zoom 0.9
    linear 0.01 alpha 1
    linear 0.25 xalign -0.3 yalign 0.6 zoom 1.0
    linear 0.01 alpha 0
    pause 0.3 
    repeat 1
    
image offensive_rp3rocket_back:
    anim.Filmstrip("battle/skills/rp3rocket.png", (73, 43), (2, 1), .02)
    xalign 0.25 yalign 0.4 alpha 0 zoom 1 xzoom -1 yzoom -1
    linear 0.01 alpha 1
    linear 0.25 xalign 0.7 yalign 0.2 zoom 0.9
    linear 0.01 alpha 0
    pause 0.3
    repeat 1
    
image offensive_rp3rocket_front:
    anim.Filmstrip("battle/skills/rp3rocket.png", (73, 43), (2, 1), .02)
    xalign 0.2 yalign 0.35 alpha 0 zoom 0.9
    linear 0.01 alpha 1
    linear 0.25 xalign -0.3 yalign 0.6 zoom 1.0
    linear 0.01 alpha 0
    pause 0.3 
    repeat 1
    
image offensive_stielhandgranate_back:
    anim.Filmstrip("battle/skills/stielhandgranate.png", (120, 120), (19, 1), .02)
    xalign 0.25 yalign 0.4 alpha 0 zoom 1.0
    linear 0.01 alpha 1
    linear 0.35 xalign 0.5 yalign 0.04 zoom 0.95
    linear 0.15 xalign 0.7 yalign 0.2 zoom 0.9
    linear 0.01 alpha 0
    pause 4.0
    alpha 0
    
image offensive_stielhandgranate_front:
    anim.Filmstrip("battle/skills/stielhandgranate.png", (120, 120), (19, 1), .02)
    xalign 0.2 yalign 0.35 alpha 0 zoom 0.9 xzoom -1
    linear 0.01 alpha 1
    linear 0.45 xalign -0.15 yalign 0.34 zoom 0.95
    linear 0.25 xalign -0.3 yalign 0.6 zoom 1.0
    linear 0.01 alpha 0
    pause 4.0
    alpha 0    
    
image offensive_molotovcocktail_back:
    anim.Filmstrip("battle/skills/molotovcocktail.png", (120, 120), (19, 1), .02)
    xalign 0.25 yalign 0.4 alpha 0 zoom 1.0
    linear 0.01 alpha 1
    linear 0.45 xalign 0.5 yalign 0.04 zoom 0.95
    linear 0.25 xalign 0.7 yalign 0.2 zoom 0.9
    linear 0.01 alpha 0
    pause 4.0
    alpha 0
    
image offensive_molotovcocktail_front:
    anim.Filmstrip("battle/skills/molotovcocktail.png", (120, 120), (19, 1), .02)
    xalign 0.2 yalign 0.35 alpha 0 zoom 0.9 xzoom -1
    linear 0.01 alpha 1
    linear 0.45 xalign -0.15 yalign 0.34 zoom 0.95
    linear 0.25 xalign -0.3 yalign 0.6 zoom 1.0
    linear 0.01 alpha 0
    pause 4.0
    alpha 0
    
image offensive_bolognese_back:
    anim.Filmstrip("battle/skills/bolognese.png", (120, 120), (19, 1), .02)
    xalign 0.25 yalign 0.4 alpha 0 zoom 1.0
    linear 0.01 alpha 1
    linear 0.45 xalign 0.5 yalign 0.04 zoom 0.95
    linear 0.25 xalign 0.7 yalign 0.2 zoom 0.9
    linear 0.01 alpha 0
    pause 4.0
    alpha 0
    
image offensive_bolognese_front:
    anim.Filmstrip("battle/skills/bolognese.png", (120, 120), (19, 1), .02)
    xalign 0.2 yalign 0.35 alpha 0 zoom 0.9 xzoom -1
    linear 0.01 alpha 1
    linear 0.45 xalign -0.15 yalign 0.34 zoom 0.95
    linear 0.25 xalign -0.3 yalign 0.6 zoom 1.0
    linear 0.01 alpha 0
    pause 4.0
    alpha 0
    
image offensive_baguette_back:
    anim.Filmstrip("battle/skills/baguette.png", (120, 120), (19, 1), .02)
    xalign 0.25 yalign 0.4 alpha 0 zoom 1.0
    linear 0.01 alpha 1
    linear 0.45 xalign 0.5 yalign 0.04 zoom 0.95
    linear 0.25 xalign 0.7 yalign 0.2 zoom 0.9
    linear 0.01 alpha 0
    pause 4.0
    alpha 0
    
image offensive_baguette_front:
    anim.Filmstrip("battle/skills/baguette.png", (120, 120), (19, 1), .02)
    xalign 0.2 yalign 0.35 alpha 0 zoom 0.9 xzoom -1
    linear 0.01 alpha 1
    linear 0.45 xalign -0.15 yalign 0.34 zoom 0.95
    linear 0.25 xalign -0.3 yalign 0.6 zoom 1.0
    linear 0.01 alpha 0
    pause 4.0
    alpha 0
    
image offensive_boomerang_back:
    anim.Filmstrip("battle/skills/boomerang.png", (120, 120), (19, 1), .02)
    xalign 0.25 yalign 0.4 alpha 0 zoom 1.0
    linear 0.01 alpha 1
    linear 0.45 xalign 0.5 yalign 0.04 zoom 0.95
    linear 0.25 xalign 0.71 yalign 0.06 zoom 0.9
    linear 0.01 alpha 0
    pause 4.0
    alpha 0
    
image offensive_boomerang_front:
    anim.Filmstrip("battle/skills/boomerang.png", (120, 120), (19, 1), .02)
    xalign 0.2 yalign 0.35 alpha 0 zoom 0.9 xzoom -1
    linear 0.01 alpha 1
    linear 0.45 xalign -0.15 yalign 0.34 zoom 0.95
    linear 0.25 xalign -0.3 yalign 0.6 zoom 1.0
    linear 0.01 alpha 0
    pause 4.0
    alpha 0
    
image offensive_clog_back:
    anim.Filmstrip("battle/skills/clog.png", (120, 120), (19, 1), .02)
    xalign 0.25 yalign 0.4 alpha 0 zoom 1.0 xzoom -1
    linear 0.01 alpha 1
    linear 0.45 xalign 0.5 yalign 0.04 zoom 0.95
    linear 0.25 xalign 0.7 yalign 0.2 zoom 0.9
    linear 0.01 alpha 0
    pause 4.0
    alpha 0
    
image offensive_clog_front:
    anim.Filmstrip("battle/skills/clog.png", (120, 120), (19, 1), .02)
    xalign 0.2 yalign 0.35 alpha 0 zoom 0.9
    linear 0.01 alpha 1
    linear 0.45 xalign -0.15 yalign 0.34 zoom 0.95
    linear 0.25 xalign -0.3 yalign 0.6 zoom 1.0
    linear 0.01 alpha 0
    pause 4.0
    alpha 0
    
image offensive_grenade_back:
    anim.Filmstrip("battle/skills/grenade.png", (120, 120), (19, 1), .02)
    xalign 0.25 yalign 0.4 alpha 0 zoom 1.0
    linear 0.01 alpha 1
    linear 0.45 xalign 0.5 yalign 0.04 zoom 0.95
    linear 0.25 xalign 0.7 yalign 0.2 zoom 0.9
    linear 0.01 alpha 0
    pause 4.0
    alpha 0
    
image offensive_grenade_front:
    anim.Filmstrip("battle/skills/grenade.png", (120, 120), (19, 1), .02)
    xalign 0.2 yalign 0.35 alpha 0 zoom 0.9 xzoom -1
    linear 0.01 alpha 1
    linear 0.45 xalign -0.15 yalign 0.34 zoom 0.95
    linear 0.25 xalign -0.3 yalign 0.6 zoom 1.0
    linear 0.01 alpha 0
    pause 4.0
    alpha 0   
    
image offensive_teacup_back:
    anim.Filmstrip("battle/skills/teacup.png", (120, 120), (19, 1), .02)
    xalign 0.25 yalign 0.4 alpha 0 zoom 1.0
    linear 0.01 alpha 1
    linear 0.35 xalign 0.5 yalign 0.04 zoom 0.95
    linear 0.25 xalign 0.7 yalign 0.2 zoom 0.9
    linear 0.01 alpha 0
    pause 4.0
    alpha 0
    
image offensive_teacup_front:
    anim.Filmstrip("battle/skills/teacup.png", (120, 120), (19, 1), .02)
    xalign 0.2 yalign 0.35 alpha 0 zoom 0.9 xzoom -1
    linear 0.01 alpha 1
    linear 0.35 xalign -0.15 yalign 0.34 zoom 0.95
    linear 0.25 xalign -0.3 yalign 0.6 zoom 1.0
    linear 0.01 alpha 0
    pause 4.0
    alpha 0   
    
image offensive_walkingstick_back:
    anim.Filmstrip("battle/skills/walkingstick.png", (120, 120), (19, 1), .02)
    xalign 0.25 yalign 0.4 alpha 0 zoom 1.0
    linear 0.01 alpha 1
    linear 0.45 xalign 0.5 yalign 0.04 zoom 0.95
    linear 0.25 xalign 0.7 yalign 0.2 zoom 0.9
    linear 0.01 alpha 0
    pause 4.0
    alpha 0
    
image offensive_walkingstick_front:
    anim.Filmstrip("battle/skills/walkingstick.png", (120, 120), (19, 1), .02)
    xalign 0.2 yalign 0.35 alpha 0 zoom 0.9 xzoom -1
    linear 0.01 alpha 1
    linear 0.45 xalign -0.15 yalign 0.34 zoom 0.95
    linear 0.25 xalign -0.3 yalign 0.6 zoom 1.0
    linear 0.01 alpha 0
    pause 4.0
    alpha 0   
    
image offensive_lightning_back:
    contains:
        anim.Filmstrip("battle/skills/lightning.png", (500, 500), (2, 2), .04)
        xalign 0.21 yalign 0.38
        
image offensive_lightning_front:
    contains:
        anim.Filmstrip("battle/skills/lightning.png", (500, 500), (2, 2), .04)
        xalign -0.5 yalign 0.43
        
image offensive_fireball_back:
    contains:
        anim.Filmstrip("battle/skills/explo_small.png", (224, 192), (4, 5), .04)
        xalign 0.21 yalign 0.38 alpha 0 zoom 0.5
        linear 0.01 alpha 1
        linear 0.35 xalign 0.73 yalign 0.1 zoom 0.9
        linear 0.1 alpha 1
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
    contains:
        anim.Filmstrip("battle/skills/explo_small.png", (224, 192), (4, 5), .04)
        xalign 0.21 yalign 0.38 alpha 0 zoom 0.5 additive 0.5
        linear 0.01 alpha 0.8 
        linear 0.35 xalign 0.73 yalign 0.1 zoom 0.9
        linear 0.1 alpha 0.8
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
        
image offensive_fireball_front:
    contains:
        anim.Filmstrip("battle/skills/explo_small.png", (224, 192), (4, 5), .04)
        xalign 0.1 yalign 0.43 alpha 0 zoom 0.5
        linear 0.01 alpha 1
        linear 0.35 xalign -0.35 yalign 0.73 zoom 0.9
        linear 0.1 alpha 1
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
    contains:
        anim.Filmstrip("battle/skills/explo_small.png", (224, 192), (4, 5), .04)
        xalign 0.1 yalign 0.43 alpha 0 zoom 0.5
        linear 0.01 alpha 1
        linear 0.35 xalign -0.35 yalign 0.73 zoom 0.9
        linear 0.1 alpha 0.8
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
    
image offensive_fireblast_back:
    anim.Filmstrip("battle/skills/cannonblast_back.png", (498, 498), (4, 5), .05, loop=False, xalign=0.5, yalign=0.5)
    
image offensive_fireblast_front:
    anim.Filmstrip("battle/skills/cannonblast_front.png", (498, 498), (4, 5), .05, loop=False, xalign=0.5, yalign=0.5)
    
image offensive_bayonet_back:
    contains:
        "battle/skills/bayonet.png"
        xalign 0.21 yalign 0.38 alpha 0 zoom 0.5 additive 0.5 xzoom -1 yzoom -1
        linear 0.01 alpha 0.8 
        linear 0.35 xalign 0.73 yalign 0.12 zoom 0.9
        linear 0.1 alpha 0.8
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
        
image offensive_bayonet_front:
    contains:
        "battle/skills/bayonet.png"
        xalign 0.1 yalign 0.43 alpha 0 zoom 0.9
        linear 0.01 alpha 1
        linear 0.35 xalign -0.35 yalign 0.73 zoom 1.0
        linear 0.1 alpha 0.8
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
    
image offensive_iceball_back:
    contains:
        "battle/skills/iceball.png"
        xalign 0.21 yalign 0.38 alpha 0 zoom 0.5
        pause 0.4
        linear 0.01 alpha 1
        linear 0.35 xalign 0.73 yalign 0.1 zoom 0.9
        linear 0.1 alpha 1
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
        repeat
    contains:
        "battle/skills/iceball.png"
        xalign 0.21 yalign 0.38 alpha 0 zoom 0.5 additive 0.5
        pause 0.2
        linear 0.01 alpha 0.8 
        linear 0.35 xalign 0.73 yalign 0.12 zoom 0.9
        linear 0.1 alpha 0.8
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
        repeat
    contains:
        "battle/skills/iceball.png"
        xalign 0.21 yalign 0.38 alpha 0 zoom 0.5 additive 0.5
        pause 0.3
        linear 0.01 alpha 0.8 
        linear 0.35 xalign 0.73 yalign 0.14 zoom 0.9
        linear 0.1 alpha 0.8
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
        repeat
        
image offensive_iceball_front:
    contains:
        "battle/skills/iceball.png"
        xalign 0.1 yalign 0.43 alpha 0 zoom 0.9
        pause 0.4
        linear 0.01 alpha 1
        linear 0.35 xalign -0.33 yalign 0.76 zoom 1.0
        linear 0.1 alpha 0.8
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
        repeat
    contains:
        "battle/skills/iceball.png"
        xalign 0.1 yalign 0.43 alpha 0 zoom 0.9
        pause 0.2
        linear 0.01 alpha 1
        linear 0.35 xalign -0.35 yalign 0.73 zoom 1.0
        linear 0.1 alpha 0.8
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
        repeat
    contains:
        "battle/skills/iceball.png"
        xalign 0.1 yalign 0.43 alpha 0 zoom 0.9
        pause 0.3
        linear 0.01 alpha 1
        linear 0.35 xalign -0.32 yalign 0.7 zoom 1.0
        linear 0.1 alpha 0.8
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
        repeat
        
image offensive_lightningball_back:
    contains:
        anim.Filmstrip("battle/skills/lightningball.png", (84, 84), (3, 1), .03, xalign=0.5, yalign=0.5)
        xalign 0.21 yalign 0.38 alpha 0 zoom 0.5
        pause 0.4
        linear 0.01 alpha 1
        linear 0.35 xalign 0.73 yalign 0.1 zoom 0.9
        linear 0.1 alpha 1
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
        repeat
    contains:
        anim.Filmstrip("battle/skills/lightningball.png", (84, 84), (3, 1), .03, xalign=0.5, yalign=0.5)
        xalign 0.21 yalign 0.38 alpha 0 zoom 0.5 additive 0.5
        pause 0.2
        linear 0.01 alpha 0.8 
        linear 0.35 xalign 0.73 yalign 0.12 zoom 0.9
        linear 0.1 alpha 0.8
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
        repeat
    contains:
        anim.Filmstrip("battle/skills/lightningball.png", (84, 84), (3, 1), .03, xalign=0.5, yalign=0.5)
        xalign 0.21 yalign 0.38 alpha 0 zoom 0.5 additive 0.5
        pause 0.3
        linear 0.01 alpha 0.8 
        linear 0.35 xalign 0.73 yalign 0.14 zoom 0.9
        linear 0.1 alpha 0.8
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
        repeat
        
image offensive_lightningball_front:
    contains:
        anim.Filmstrip("battle/skills/lightningball.png", (84, 84), (3, 1), .03, xalign=0.5, yalign=0.5)
        xalign 0.1 yalign 0.43 alpha 0 zoom 0.9
        pause 0.4
        linear 0.01 alpha 1
        linear 0.35 xalign -0.33 yalign 0.76 zoom 1.0
        linear 0.1 alpha 0.8
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
        repeat
    contains:
        anim.Filmstrip("battle/skills/lightningball.png", (84, 84), (3, 1), .03, xalign=0.5, yalign=0.5)
        xalign 0.1 yalign 0.43 alpha 0 zoom 0.9
        pause 0.2
        linear 0.01 alpha 1
        linear 0.35 xalign -0.35 yalign 0.73 zoom 1.0
        linear 0.1 alpha 0.8
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
        repeat
    contains:
        anim.Filmstrip("battle/skills/lightningball.png", (84, 84), (3, 1), .03, xalign=0.5, yalign=0.5)
        xalign 0.1 yalign 0.43 alpha 0 zoom 0.9
        pause 0.3
        linear 0.01 alpha 1
        linear 0.35 xalign -0.32 yalign 0.7 zoom 1.0
        linear 0.1 alpha 0.8
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
        repeat
        
image offensive_snowball_back:
    contains:
        "battle/skills/snowball.png"
        xalign 0.21 yalign 0.38 alpha 0 zoom 0.5
        pause 0.4
        linear 0.01 alpha 1
        linear 0.35 xalign 0.73 yalign 0.1 zoom 0.9
        linear 0.1 alpha 1
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
        repeat
    contains:
        "battle/skills/snowball.png"
        xalign 0.21 yalign 0.38 alpha 0 zoom 0.5 additive 0.5
        pause 0.2
        linear 0.01 alpha 0.8 
        linear 0.35 xalign 0.73 yalign 0.12 zoom 0.9
        linear 0.1 alpha 0.8
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
        repeat
    contains:
        "battle/skills/snowball.png"
        xalign 0.21 yalign 0.38 alpha 0 zoom 0.5 additive 0.5
        pause 0.3
        linear 0.01 alpha 0.8 
        linear 0.35 xalign 0.73 yalign 0.14 zoom 0.9
        linear 0.1 alpha 0.8
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
        repeat
        
image offensive_snowball_front:
    contains:
        "battle/skills/snowball.png"
        xalign 0.1 yalign 0.43 alpha 0 zoom 0.9
        pause 0.4
        linear 0.01 alpha 1
        linear 0.35 xalign -0.33 yalign 0.71 zoom 1.0
        linear 0.1 alpha 0.8
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
        repeat
    contains:
        "battle/skills/snowball.png"
        xalign 0.1 yalign 0.43 alpha 0 zoom 0.9
        pause 0.2
        linear 0.01 alpha 1
        linear 0.35 xalign -0.35 yalign 0.68 zoom 1.0
        linear 0.1 alpha 0.8
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
        repeat
    contains:
        "battle/skills/snowball.png"
        xalign 0.1 yalign 0.43 alpha 0 zoom 0.9
        pause 0.3
        linear 0.01 alpha 1
        linear 0.35 xalign -0.32 yalign 0.65 zoom 1.0
        linear 0.1 alpha 0.8
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
        repeat
        
image offensive_sprout_back:
    contains:
        "battle/skills/sprout.png"
        xalign 0.21 yalign 0.38 alpha 0 zoom 0.5
        pause 0.4
        linear 0.01 alpha 1
        linear 0.35 xalign 0.73 yalign 0.1 zoom 0.9
        linear 0.1 alpha 1
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
        repeat
    contains:
        "battle/skills/sprout.png"
        xalign 0.21 yalign 0.38 alpha 0 zoom 0.5 additive 0.5
        pause 0.2
        linear 0.01 alpha 0.8 
        linear 0.35 xalign 0.73 yalign 0.12 zoom 0.9
        linear 0.1 alpha 0.8
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
        repeat
    contains:
        "battle/skills/sprout.png"
        xalign 0.21 yalign 0.38 alpha 0 zoom 0.5 additive 0.5
        pause 0.3
        linear 0.01 alpha 0.8 
        linear 0.35 xalign 0.73 yalign 0.14 zoom 0.9
        linear 0.1 alpha 0.8
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
        repeat
        
image offensive_sprout_front:
    contains:
        "battle/skills/sprout.png"
        xalign 0.15 yalign 0.43 alpha 0 zoom 0.9
        pause 0.4
        linear 0.01 alpha 1
        linear 0.35 xalign -0.33 yalign 0.71 zoom 1.0
        linear 0.1 alpha 0.8
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
        repeat
    contains:
        "battle/skills/sprout.png"
        xalign 0.15 yalign 0.43 alpha 0 zoom 0.9
        pause 0.2
        linear 0.01 alpha 1
        linear 0.35 xalign -0.35 yalign 0.68 zoom 1.0
        linear 0.1 alpha 0.8
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
        repeat
    contains:
        "battle/skills/sprout.png"
        xalign 0.15 yalign 0.43 alpha 0 zoom 0.9
        pause 0.3
        linear 0.01 alpha 1
        linear 0.35 xalign -0.32 yalign 0.65 zoom 1.0
        linear 0.1 alpha 0.8
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
        repeat
    
image offensive_prismblast_back:
    contains:
        At("battle/skills/prism_small.png", full_spin)
        xalign 0.21 yalign 0.38 alpha 0 zoom 0.5
        pause 0.4
        linear 0.01 alpha 1
        linear 0.35 xalign 0.73 yalign 0.1 zoom 0.9
        linear 0.1 alpha 1
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
        repeat
    contains:
        At("battle/skills/prism_small.png", full_spin)
        xalign 0.21 yalign 0.38 alpha 0 zoom 0.5 additive 0.5
        pause 0.4
        linear 0.01 alpha 0.8 
        linear 0.35 xalign 0.73 yalign 0.12 zoom 0.9
        linear 0.1 alpha 0.8
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
        repeat
    contains:
        At("battle/skills/prism_small.png", full_spin)
        xalign 0.21 yalign 0.38 alpha 0 zoom 0.5 additive 0.5
        pause 0.4
        linear 0.01 alpha 0.8 
        linear 0.35 xalign 0.73 yalign 0.14 zoom 0.9
        linear 0.1 alpha 0.8
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
        repeat
        
image offensive_prismblast_front:
    contains:
        At("battle/skills/prism_small.png", full_spin)
        xalign 0.1 yalign 0.43 alpha 0 zoom 0.9
        pause 0.4
        linear 0.01 alpha 1
        linear 0.35 xalign -0.33 yalign 0.76 zoom 1.0
        linear 0.1 alpha 0.8
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
        repeat
    contains:
        At("battle/skills/prism_small.png", full_spin)
        xalign 0.1 yalign 0.43 alpha 0 zoom 0.9
        pause 0.2
        linear 0.01 alpha 1
        linear 0.35 xalign -0.35 yalign 0.73 zoom 1.0
        linear 0.1 alpha 0.8
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
        repeat
    contains:
        At("battle/skills/prism_small.png", full_spin)
        xalign 0.1 yalign 0.43 alpha 0 zoom 0.9
        pause 0.3
        linear 0.01 alpha 1
        linear 0.35 xalign -0.32 yalign 0.7 zoom 1.0
        linear 0.1 alpha 0.8
        linear 0.01 alpha 0
        pause 4.0
        alpha 0
        repeat
        
#SEALS ANIMATIONS
image seal_ground:
    parallel:
        contains:
            im.Crop("battle/skills/seals_glow.png", (360, 0, 180, 180))
        contains:
            im.Crop("battle/skills/seals.png", (360, 0, 180, 180))
            alpha 1.0
            linear 1.0 alpha 0.5
            linear 1.0 alpha 1.0
            repeat
        contains:
            im.Crop("battle/skills/seals_glow.png", (360, 0, 180, 180))
            alpha 0.8 additive 0.5
            linear 1.0 alpha 0.5
            linear 1.0 alpha 0.8
            repeat
        alpha 0
        linear 0.4 alpha 1.0
        linear 0.4 alpha 0
        repeat
        
image seal_red:
    parallel:
        contains:
            im.Crop("battle/skills/seals_glow.png", (0, 180, 180, 180))
        contains:
            im.Crop("battle/skills/seals.png", (0, 180, 180, 180))
            alpha 1.0
            linear 1.0 alpha 0.5
            linear 1.0 alpha 1.0
            repeat
        contains:
            im.Crop("battle/skills/seals_glow.png", (0, 180, 180, 180))
            alpha 0.8 additive 0.5
            linear 1.0 alpha 0.5
            linear 1.0 alpha 0.8
            repeat
        alpha 0
        linear 0.4 alpha 1.0
        linear 0.4 alpha 0
        repeat
        
image seal_fire:
    parallel:
        contains:
            im.Crop("battle/skills/seals_glow.png", (0, 180, 180, 180))
        contains:
            im.Crop("battle/skills/seals.png", (180, 180, 180, 180))
            alpha 1.0
            linear 1.0 alpha 0.5
            linear 1.0 alpha 1.0
            repeat
        contains:
            im.Crop("battle/skills/seals_glow.png", (180, 180, 180, 180))
            alpha 0.8 additive 0.5
            linear 1.0 alpha 0.5
            linear 1.0 alpha 0.8
            repeat
        alpha 0
        linear 0.4 alpha 1.0
        linear 0.4 alpha 0
        repeat
        
image seal_dark:
    parallel:
        contains:
            im.Crop("battle/skills/seals_glow.png", (0, 180, 180, 180))
        contains:
            im.Crop("battle/skills/seals.png", (360, 360, 180, 180))
            alpha 1.0
            linear 1.0 alpha 0.5
            linear 1.0 alpha 1.0
            repeat
        contains:
            im.Crop("battle/skills/seals_glow.png", (360, 360, 180, 180))
            alpha 0.8 additive 0.5
            linear 1.0 alpha 0.5
            linear 1.0 alpha 0.8
            repeat
        alpha 0
        linear 0.4 alpha 1.0
        linear 0.4 alpha 0
        repeat
        
image seal_light:
    parallel:
        contains:
            im.Crop("battle/skills/seals_glow.png", (180, 360, 180, 180))
        contains:
            im.Crop("battle/skills/seals.png", (0, 360, 180, 180))
            alpha 1.0
            linear 1.0 alpha 0.5
            linear 1.0 alpha 1.0
            repeat
        contains:
            im.Crop("battle/skills/seals_glow.png", (0, 360, 180, 180))
            alpha 0.8 additive 0.5
            linear 1.0 alpha 0.5
            linear 1.0 alpha 0.8
            repeat
        alpha 0
        linear 0.4 alpha 1.0
        linear 0.4 alpha 0
        repeat
        
image seal_electric:
    parallel:
        contains:
            im.Crop("battle/skills/seals_glow.png", (180, 360, 180, 180))
        contains:
            im.Crop("battle/skills/seals.png", (180, 360, 180, 180))
            alpha 1.0
            linear 1.0 alpha 0.5
            linear 1.0 alpha 1.0
            repeat
        contains:
            im.Crop("battle/skills/seals_glow.png", (180, 360, 180, 180))
            alpha 0.8 additive 0.5
            linear 1.0 alpha 0.5
            linear 1.0 alpha 0.8
            repeat
        alpha 0
        linear 0.4 alpha 1.0
        linear 0.4 alpha 0
        repeat
        
image seal_blue:
    parallel:
        contains:
            im.Crop("battle/skills/seals_glow.png", (360, 180, 180, 180))
        contains:
            im.Crop("battle/skills/seals.png", (0, 360, 180, 180))
            alpha 1.0
            linear 1.0 alpha 0.5
            linear 1.0 alpha 1.0
            repeat
        contains:
            im.Crop(im.MatrixColor("battle/skills/seals_glow.png", im.matrix.brightness(0.9)), (360, 180, 180, 180))
            alpha 0.8 additive 0.5
            linear 1.0 alpha 0.5
            linear 1.0 alpha 0.8
            repeat
        alpha 0
        linear 0.4 alpha 1.0
        linear 0.4 alpha 0
        repeat
        
image seal_powerup:
    parallel:
        contains:
            im.Crop(im.MatrixColor("battle/skills/seals_glow.png", im.matrix.brightness(1)), (180, 360, 180, 180))
        contains:
            im.Crop(im.MatrixColor("battle/skills/seals.png", im.matrix.brightness(1)), (0, 360, 180, 180))
            alpha 1.0
            linear 1.0 alpha 0.5
            linear 1.0 alpha 1.0
            repeat
        contains:
            im.Crop(im.MatrixColor("battle/skills/seals_glow.png", im.matrix.brightness(1)), (0, 360, 180, 180))
            alpha 0.8 additive 0.5
            linear 1.0 alpha 0.5
            linear 1.0 alpha 0.8
            repeat
        alpha 0
        linear 0.4 alpha 1.0
        linear 0.4 alpha 0
        repeat
        
image seal_heal:
    parallel:
        contains:
            im.Crop("battle/skills/seals_glow.png", (180, 0, 180, 180))
        contains:
            im.Crop("battle/skills/seals.png", (180, 0, 180, 180))
            alpha 1.0
            linear 1.0 alpha 0.5
            linear 1.0 alpha 1.0
            repeat
        contains:
            im.Crop("battle/skills/seals_glow.png", (180, 0, 180, 180))
            alpha 0.8 additive 0.5
            linear 1.0 alpha 0.5
            linear 1.0 alpha 0.8                     
            repeat
        alpha 0
        linear 0.4 alpha 1.0
        linear 0.4 alpha 0
        repeat
        
image seal_love:
    parallel:
        contains:
            im.Crop("battle/skills/seals_glow.png", (0, 0, 180, 180))
        contains:
            im.Crop("battle/skills/seals.png", (0, 0, 180, 180))
            alpha 1.0
            linear 1.0 alpha 0.5
            linear 1.0 alpha 1.0
            repeat
        contains:
            im.Crop("battle/skills/seals_glow.png", (0, 0, 180, 180))
            alpha 0.8 additive 0.5
            linear 1.0 alpha 0.5
            linear 1.0 alpha 0.8
            repeat
        alpha 0
        linear 0.4 alpha 1.0
        linear 0.4 alpha 0
        repeat
        

#REACTION ANIMATIONS
image reaction_none = Null()

image reaction_powerup_aimup:
    additive 1.0
    alpha 0.7
    parallel:
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/barrier.png", im.matrix.desaturate() * im.matrix.tint(0.2, 1.0, 0.2)), (150, 150), (1, 1), .07, xalign=0.5, yalign=0.5)
            rotate 0 zoom 2.0
            linear 0.1 rotate 360
            repeat
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/barrier.png", im.matrix.desaturate() * im.matrix.tint(0.5, 1.0, 0.5)), (150, 150), (1, 1), .07, xalign=0.5, yalign=0.5)
            rotate 0 zoom 2.0
            linear 0.4 rotate -360
            repeat
            
image reaction_powerup_bunkerin:
    additive 1.0
    alpha 0.7
    parallel:
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/barrier.png", im.matrix.desaturate() * im.matrix.tint(1.0, 1.0, 0.2)), (150, 150), (1, 1), .07, xalign=0.5, yalign=0.5)
            rotate 0 zoom 2.0
            linear 0.1 rotate 360
            repeat
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/barrier.png", im.matrix.desaturate() * im.matrix.tint(1.0, 1.0, 0.2)), (150, 150), (1, 1), .07, xalign=0.5, yalign=0.5)
            rotate 0 zoom 2.0
            linear 0.4 rotate -360
            repeat
            
image reaction_powerup_positivity:
    additive 1.0
    alpha 0.7
    parallel:
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/barrier.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.5, 0.2)), (150, 150), (1, 1), .07, xalign=0.5, yalign=0.5)
            rotate 0 zoom 2.0
            linear 0.2 rotate 360
            repeat
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/barrier.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.5, 0.2)), (150, 150), (1, 1), .07, xalign=0.5, yalign=0.5)
            rotate 0 zoom 2.0
            linear 0.4 rotate -360
            repeat
            
image reaction_powerup_blitz:
    additive 1.0
    alpha 0.7
    parallel:
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/barrier.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.2, 0.2)), (150, 150), (1, 1), .07, xalign=0.5, yalign=0.5)
            rotate 0 zoom 2.0
            linear 0.1 rotate 360
            repeat
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/barrier.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.2, 0.2)), (150, 150), (1, 1), .07, xalign=0.5, yalign=0.5)
            rotate 0 zoom 2.0
            linear 0.4 rotate -360
            repeat
            
image reaction_powerup_stukatablets:
    additive 1.0
    alpha 0.7
    parallel:
        contains:
            anim.Filmstrip("battle/skills/barrier.png", (150, 150), (1, 1), .07, xalign=0.5, yalign=0.5)
            rotate 0 zoom 2.0
            linear 0.1 rotate 360
            repeat
        contains:
            anim.Filmstrip("battle/skills/barrier.png", (150, 150), (1, 1), .07, xalign=0.5, yalign=0.5)
            rotate 0 zoom 2.0
            linear 0.4 rotate -360
            repeat

image reaction_powerup_megaaccuracy:
    additive 1.0
    alpha 0.7
    parallel:
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/barrier.png", im.matrix.desaturate() * im.matrix.tint(0.2, 1.0, 0.2)), (150, 150), (1, 1), .07, xalign=0.5, yalign=0.5)
            rotate 0 zoom 2.0
            linear 0.1 rotate 360
            repeat
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/barrier.png", im.matrix.desaturate() * im.matrix.tint(0.5, 1.0, 0.5)), (150, 150), (1, 1), .07, xalign=0.5, yalign=0.5)
            rotate 0 zoom 2.0
            linear 0.4 rotate -360
            repeat
            
image reaction_powerup_megaarmor:
    additive 1.0
    alpha 0.7
    parallel:
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/barrier.png", im.matrix.desaturate() * im.matrix.tint(1.0, 1.0, 0.2)), (150, 150), (1, 1), .07, xalign=0.5, yalign=0.5)
            rotate 0 zoom 2.0
            linear 0.1 rotate 360
            repeat
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/barrier.png", im.matrix.desaturate() * im.matrix.tint(1.0, 1.0, 0.2)), (150, 150), (1, 1), .07, xalign=0.5, yalign=0.5)
            rotate 0 zoom 2.0
            linear 0.4 rotate -360
            repeat
            
image reaction_powerup_megacharm:
    additive 1.0
    alpha 0.7
    parallel:
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/barrier.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.5, 0.2)), (150, 150), (1, 1), .07, xalign=0.5, yalign=0.5)
            rotate 0 zoom 2.0
            linear 0.2 rotate 360
            repeat
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/barrier.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.5, 0.2)), (150, 150), (1, 1), .07, xalign=0.5, yalign=0.5)
            rotate 0 zoom 2.0
            linear 0.4 rotate -360
            repeat
            
image reaction_powerup_megapower:
    additive 1.0
    alpha 0.7
    parallel:
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/barrier.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.2, 0.2)), (150, 150), (1, 1), .07, xalign=0.5, yalign=0.5)
            rotate 0 zoom 2.0
            linear 0.1 rotate 360
            repeat
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/barrier.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.2, 0.2)), (150, 150), (1, 1), .07, xalign=0.5, yalign=0.5)
            rotate 0 zoom 2.0
            linear 0.4 rotate -360
            repeat
            
image reaction_powerup_megaspeed:
    additive 1.0
    alpha 0.7
    parallel:
        contains:
            anim.Filmstrip("battle/skills/barrier.png", (150, 150), (1, 1), .07, xalign=0.5, yalign=0.5)
            rotate 0 zoom 2.0
            linear 0.1 rotate 360
            repeat
        contains:
            anim.Filmstrip("battle/skills/barrier.png", (150, 150), (1, 1), .07, xalign=0.5, yalign=0.5)
            rotate 0 zoom 2.0
            linear 0.4 rotate -360
            repeat
                          
image reaction_powerup_xaccuracy:
    additive 1.0
    alpha 0.7
    parallel:
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/barrier.png", im.matrix.desaturate() * im.matrix.tint(0.2, 1.0, 0.2)), (150, 150), (1, 1), .07, xalign=0.5, yalign=0.5)
            rotate 0 zoom 2.0
            linear 0.05 rotate -360
            repeat
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/barrier.png", im.matrix.desaturate() * im.matrix.tint(0.5, 1.0, 0.5)), (150, 150), (1, 1), .07, xalign=0.5, yalign=0.5)
            rotate 0 zoom 2.0
            linear 0.2 rotate 360
            repeat
            
image reaction_powerup_xarmor:
    additive 1.0
    alpha 0.7
    parallel:
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/barrier.png", im.matrix.desaturate() * im.matrix.tint(1.0, 1.0, 0.2)), (150, 150), (1, 1), .07, xalign=0.5, yalign=0.5)
            rotate 0 zoom 2.0
            linear 0.05 rotate -360
            repeat
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/barrier.png", im.matrix.desaturate() * im.matrix.tint(1.0, 1.0, 0.2)), (150, 150), (1, 1), .07, xalign=0.5, yalign=0.5)
            rotate 0 zoom 2.0
            linear 0.2 rotate 360
            repeat
            
image reaction_powerup_xcharm:
    additive 1.0
    alpha 0.7
    parallel:
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/barrier.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.5, 0.2)), (150, 150), (1, 1), .07, xalign=0.5, yalign=0.5)
            rotate 0 zoom 2.0
            linear 0.05 rotate -360
            repeat
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/barrier.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.5, 0.2)), (150, 150), (1, 1), .07, xalign=0.5, yalign=0.5)
            rotate 0 zoom 2.0
            linear 0.2 rotate 360
            repeat
            
image reaction_powerup_xpower:
    additive 1.0
    alpha 0.7
    parallel:
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/barrier.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.2, 0.2)), (150, 150), (1, 1), .07, xalign=0.5, yalign=0.5)
            rotate 0 zoom 2.0
            linear 0.05 rotate -360
            repeat
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/barrier.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.2, 0.2)), (150, 150), (1, 1), .07, xalign=0.5, yalign=0.5)
            rotate 0 zoom 2.0
            linear 0.2 rotate 360
            repeat
            
image reaction_powerup_xspeed:
    additive 1.0
    alpha 0.7
    parallel:
        contains:
            anim.Filmstrip("battle/skills/barrier.png", (150, 150), (1, 1), .07, xalign=0.5, yalign=0.5)
            rotate 0 zoom 2.0
            linear 0.05 rotate -360
            repeat
        contains:
            anim.Filmstrip("battle/skills/barrier.png", (150, 150), (1, 1), .07, xalign=0.5, yalign=0.5)
            rotate 0 zoom 2.0
            linear 0.2 rotate 360
            repeat
            
image reaction_heal:
    alpha 1.0
    parallel:
        contains:
            anim.Filmstrip("battle/skills/heal_particle.png", (28, 28), (2, 1), .05, xalign=0.5, yalign=0.5)
            xalign 0.65
            yalign 0.65
            zoom 2.0
            alpha 0
            linear 0.7 alpha 1.0 yalign 0.5
            linear 0.7 alpha 0 yalign 0.35
            repeat
        contains:
            anim.Filmstrip("battle/skills/heal_particle_glow.png", (28, 28), (2, 1), .05, xalign=0.5, yalign=0.5)
            xalign 0.35
            yalign 0.75
            zoom 1.8
            alpha 0
            linear 0.6 alpha 1.0 yalign 0.7
            linear 0.6 alpha 0 yalign 0.55
            repeat
        contains:
            anim.Filmstrip("battle/skills/heal_particle.png", (28, 28), (2, 1), .05, xalign=0.5, yalign=0.5)
            xalign 0.45
            yalign 0.45
            zoom 1.3
            alpha 0
            linear 0.5 alpha 1.0 yalign 0.3
            linear 0.5 alpha 0 yalign 0.15
            repeat
        contains:
            anim.Filmstrip("battle/skills/heal_particle_glow.png", (28, 28), (2, 1), .05, xalign=0.5, yalign=0.5)
            xalign 0.53
            yalign 0.53
            zoom 1.4
            alpha 0
            linear 0.4 alpha 1.0 yalign 0.38
            linear 0.4 alpha 0 yalign 0.23
            repeat
        contains:
            anim.Filmstrip("battle/skills/heal_particle_glow.png", (28, 28), (2, 1), .05, xalign=0.5, yalign=0.5)
            xalign 0.57
            yalign 0.75
            zoom 0.65
            alpha 1.3
            linear 0.5 alpha 1.0 yalign 0.69
            linear 0.5 alpha 0 yalign 0.54
            repeat
            
image reaction_machineheal:
    alpha 1.0
    parallel:
        contains:
            anim.Filmstrip("battle/skills/heal_gear.png", (174, 174), (2, 1), .05, xalign=0.5, yalign=0.5)
            xalign 0.65
            yalign 0.65
            zoom 1.0
            alpha 0
            linear 0.7 alpha 1.0 yalign 0.5
            linear 0.7 alpha 0 yalign 0.35
            repeat
        contains:
            anim.Filmstrip("battle/skills/heal_gear.png", (174, 174), (2, 1), .05, xalign=0.5, yalign=0.5)
            xalign 0.35
            yalign 0.75
            zoom 0.8
            alpha 0
            linear 0.6 alpha 1.0 yalign 0.7
            linear 0.6 alpha 0 yalign 0.55
            repeat
        contains:
            anim.Filmstrip("battle/skills/heal_gear.png", (174, 174), (2, 1), .05, xalign=0.5, yalign=0.5)
            xalign 0.45
            yalign 0.45
            zoom 0.3
            alpha 0
            linear 0.5 alpha 1.0 yalign 0.3
            linear 0.5 alpha 0 yalign 0.15
            repeat
        contains:
            anim.Filmstrip("battle/skills/heal_gear.png", (174, 174), (2, 1), .05, xalign=0.5, yalign=0.5)
            xalign 0.85
            yalign 0.65
            zoom 0.3
            alpha 0
            linear 0.5 alpha 1.0 yalign 0.5
            linear 0.5 alpha 0 yalign 0.25
            repeat
        contains:
            anim.Filmstrip("battle/skills/heal_gear.png", (174, 174), (2, 1), .05, xalign=0.5, yalign=0.5)
            xalign 0.53
            yalign 0.53
            zoom 0.4
            alpha 0
            linear 0.4 alpha 1.0 yalign 0.38
            linear 0.4 alpha 0 yalign 0.23
            repeat
        contains:
            anim.Filmstrip("battle/skills/heal_gear.png", (174, 174), (2, 1), .05, xalign=0.5, yalign=0.5)
            xalign 0.57
            yalign 0.75
            zoom 0.65
            alpha 0.3
            linear 0.5 alpha 1.0 yalign 0.69
            linear 0.5 alpha 0 yalign 0.54
            repeat

image reaction_hit:
    anim.Filmstrip("battle/skills/hit.png", (92, 92), (2, 2), .05, xalign=0.5, yalign=0.5)
    
image reaction_ground:
    anim.Filmstrip("battle/skills/strafe.png", (200, 200), (2, 2), .07, xalign=0.5, yalign=0.5)
    
image reaction_prism:
    parallel:
        contains:
            At("battle/skills/prism_small.png", full_spin)
            xalign 0.4 yalign 0.5
        contains:
            At("battle/skills/prism_small.png", full_spin)
            xalign 0.6 yalign 0.3
        contains:
            At("battle/skills/prism_small.png", full_spin)
            xalign 0.45 yalign 0.7
    
image reaction_fire:
    anim.Filmstrip("battle/skills/fire.png", (234, 234), (2, 2), .07, xalign=0.5, yalign=0.5)
    alpha 0.9
    
image reaction_snow:
    anim.Filmstrip("battle/skills/snow.png", (234, 234), (2, 2), .07, xalign=0.5, yalign=0.5)
    alpha 0.9
    
image reaction_gas:
    parallel:
        contains:
            anim.Filmstrip("battle/skills/gas_cloud.png", (189, 152), (3, 1), .07, xalign=0.5, yalign=0.5)
            alpha 0.3 zoom 1.5
            linear 1.0 zoom 1.0
            linear 1.0 zoom 1.5
            repeat
    
image reaction_ice:
    contains:
        anim.Filmstrip("battle/skills/ice_crystals.png", (70, 168), (7, 1), .07, xalign=0.5, yalign=0.5)
        alpha 0.9 xalign 0.45 yalign 0.6
    contains:
        anim.Filmstrip("battle/skills/ice_crystals.png", (70, 168), (7, 1), .04, xalign=0.5, yalign=0.5)
        alpha 0.9 xalign 0.4 yalign 0.6 zoom 0.5
    contains:
        anim.Filmstrip("battle/skills/ice_crystals.png", (70, 168), (7, 1), .05, xalign=0.5, yalign=0.5)
        alpha 0.9 xalign 0.54 yalign 0.6 zoom 0.7
    contains:
        anim.Filmstrip("battle/skills/ice_crystals.png", (70, 168), (7, 1), .03, xalign=0.5, yalign=0.5)
        alpha 0.9 xalign 0.3 yalign 0.55 zoom 0.3
    contains:
        anim.Filmstrip("battle/skills/ice_crystals.png", (70, 168), (7, 1), .06, xalign=0.5, yalign=0.5)
        alpha 0.9 xalign 0.6 yalign 0.55 zoom 0.25
    
image reaction_lightning:
    alpha 0.9
    parallel: 
        contains:
            anim.Filmstrip("battle/skills/lightning_particle.png", (90, 90), (2, 1), .07, xalign=0.5, yalign=0.5)
            xalign 0.55 yalign 0.65
        contains:
            anim.Filmstrip("battle/skills/lightning_particle.png", (90, 90), (2, 1), .05, xalign=0.5, yalign=0.5)
            xalign 0.55 yalign 0.65 rotate 45
        contains:
            anim.Filmstrip("battle/skills/lightning_particle.png", (90, 90), (2, 1), .06, xalign=0.5, yalign=0.5)
            xalign 0.55 yalign 0.65 rotate 270
        contains:
            anim.Filmstrip("battle/skills/lightning_particle.png", (90, 90), (2, 1), .07, xalign=0.5, yalign=0.5)
            xalign 0.45 yalign 0.45
        contains:
            anim.Filmstrip("battle/skills/lightning_particle.png", (90, 90), (2, 1), .05, xalign=0.5, yalign=0.5)
            xalign 0.45 yalign 0.45 rotate 45
        contains:
            anim.Filmstrip("battle/skills/lightning_particle.png", (90, 90), (2, 1), .06, xalign=0.5, yalign=0.5)
            xalign 0.45 yalign 0.45 rotate 270
        contains:
            anim.Filmstrip("battle/skills/lightning_particle.png", (90, 90), (2, 1), .07, xalign=0.5, yalign=0.5)
            xalign 0.5 yalign 0.35
        contains:
            anim.Filmstrip("battle/skills/lightning_particle.png", (90, 90), (2, 1), .05, xalign=0.5, yalign=0.5)
            xalign 0.5 yalign 0.35 rotate 45
        contains:
            anim.Filmstrip("battle/skills/lightning_particle.png", (90, 90), (2, 1), .06, xalign=0.5, yalign=0.5)
            xalign 0.5 yalign 0.35 rotate 270
        contains:
            anim.Filmstrip("battle/skills/lightning_particle.png", (90, 90), (2, 1), .07, xalign=0.5, yalign=0.5)
            xalign 0.47 yalign 0.55
        contains:
            anim.Filmstrip("battle/skills/lightning_particle.png", (90, 90), (2, 1), .05, xalign=0.5, yalign=0.5)
            xalign 0.47 yalign 0.55 rotate 45
        contains:
            anim.Filmstrip("battle/skills/lightning_particle.png", (90, 90), (2, 1), .06, xalign=0.5, yalign=0.5)
            xalign 0.47 yalign 0.55 rotate 270
        contains:
            anim.Filmstrip("battle/skills/lightning_particle.png", (90, 90), (2, 1), .07, xalign=0.5, yalign=0.5)
            xalign 0.52 yalign 0.41
        contains:
            anim.Filmstrip("battle/skills/lightning_particle.png", (90, 90), (2, 1), .05, xalign=0.5, yalign=0.5)
            xalign 0.52 yalign 0.41 rotate 45
        contains:
            anim.Filmstrip("battle/skills/lightning_particle.png", (90, 90), (2, 1), .06, xalign=0.5, yalign=0.5)
            xalign 0.52 yalign 0.41 rotate 270
        contains:
            anim.Filmstrip("battle/skills/lightning_particle.png", (90, 90), (2, 1), .07, xalign=0.5, yalign=0.5)
            xalign 0.44 yalign 0.29
        contains:
            anim.Filmstrip("battle/skills/lightning_particle.png", (90, 90), (2, 1), .05, xalign=0.5, yalign=0.5)
            xalign 0.44 yalign 0.29 rotate 45
        contains:
            anim.Filmstrip("battle/skills/lightning_particle.png", (90, 90), (2, 1), .06, xalign=0.5, yalign=0.5)
            xalign 0.44 yalign 0.29 rotate 270
        contains:
            anim.Filmstrip("battle/skills/lightning_particle.png", (90, 90), (2, 1), .07, xalign=0.5, yalign=0.5)
            xalign 0.41 yalign 0.5 rotate 130
        contains:
            anim.Filmstrip("battle/skills/lightning_particle.png", (90, 90), (2, 1), .07, xalign=0.5, yalign=0.5)
            xalign 0.43 yalign 0.58 rotate 40
        contains:
            anim.Filmstrip("battle/skills/lightning_particle.png", (90, 90), (2, 1), .06, xalign=0.5, yalign=0.5)
            xalign 0.46 yalign 0.56 rotate 10
        contains:
            anim.Filmstrip("battle/skills/lightning_particle.png", (90, 90), (2, 1), .06, xalign=0.5, yalign=0.5)
            xalign 0.46 yalign 0.56 rotate 45
        contains:
            anim.Filmstrip("battle/skills/lightning_particle.png", (90, 90), (2, 1), .06, xalign=0.5, yalign=0.5)
            xalign 0.46 yalign 0.56 rotate 270
        contains:
            anim.Filmstrip("battle/skills/lightning_particle.png", (90, 90), (2, 1), .03, xalign=0.5, yalign=0.5)
            xalign 0.44 yalign 0.3 rotate 70
        contains:
            anim.Filmstrip("battle/skills/lightning_particle.png", (90, 90), (2, 1), .04, xalign=0.5, yalign=0.5)
            xalign 0.42 yalign 0.31 rotate 320
        contains:
            anim.Filmstrip("battle/skills/lightning_particle.png", (90, 90), (2, 1), .04, xalign=0.5, yalign=0.5)
            xalign 0.42 yalign 0.31 rotate 55
        contains:
            anim.Filmstrip("battle/skills/lightning_particle.png", (90, 90), (2, 1), .04, xalign=0.5, yalign=0.5)
            xalign 0.42 yalign 0.31 rotate 220
        contains:
            anim.Filmstrip("battle/skills/lightning_particle.png", (90, 90), (2, 1), .04, xalign=0.5, yalign=0.5)
            xalign 0.4 yalign 0.41 rotate 120
        contains:
            anim.Filmstrip("battle/skills/lightning_particle.png", (90, 90), (2, 1), .04, xalign=0.5, yalign=0.5)
            xalign 0.4 yalign 0.41 rotate 55
        contains:
            anim.Filmstrip("battle/skills/lightning_particle.png", (90, 90), (2, 1), .04, xalign=0.5, yalign=0.5)
            xalign 0.4 yalign 0.41 rotate 220
    
image reaction_landmine:
    anim.Filmstrip("battle/skills/landmine.png", (596, 596), (4, 3), .05, loop=False, xalign=0.5, yalign=0.5)
    
image reaction_dark:
    parallel: 
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/strafe.png", im.matrix.desaturate() * im.matrix.tint(0.5, 0, 0.5)), (200, 200), (2, 2), .07, xalign=0.5, yalign=0.5)
            xalign 0.41 yalign 0.5
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/strafe.png", im.matrix.desaturate() * im.matrix.tint(0.5, 0, 0.5)), (200, 200), (2, 2), .09, xalign=0.5, yalign=0.5)
            xalign 0.6 yalign 0.5
        contains:
            anim.Filmstrip("battle/skills/dark_particles.png", (80, 80), (2, 1), .07, xalign=0.5, yalign=0.5)
            xalign 0.65
            yalign 0.65
            zoom 1.3
            alpha 1.0
            linear 0.7 alpha 0.3 yalign 0.5
            linear 0.7 alpha 1.0 yalign 0.65
            repeat
        contains:
            anim.Filmstrip("battle/skills/dark_particles.png", (80, 80), (2, 1), .07, xalign=0.5, yalign=0.5)
            xalign 0.3
            yalign 0.35
            zoom 1.3
            alpha 1.0
            linear 0.7 alpha 0.3 yalign 0.1
            linear 0.7 alpha 1.0 yalign 0.25
            repeat  
        contains:
            anim.Filmstrip("battle/skills/dark_particles.png", (80, 80), (2, 1), .07, xalign=0.5, yalign=0.5)
            xalign 0.35
            yalign 0.7
            zoom 1.1
            alpha 0.3
            linear 0.6 alpha 1.0 yalign 0.7
            linear 0.6 alpha 0.3 yalign 0.75
            repeat
        contains:
            anim.Filmstrip("battle/skills/dark_particles.png", (80, 80), (2, 1), .07, xalign=0.5, yalign=0.5)
            xalign 0.45
            yalign 0.35
            zoom 1
            alpha 1.0
            linear 0.5 alpha 0.3 yalign 0.3
            linear 0.5 alpha 1.0 yalign 0.45
            repeat
        contains:
            anim.Filmstrip("battle/skills/dark_particles.png", (80, 80), (2, 1), .07, xalign=0.5, yalign=0.5)
            xalign 0.23
            yalign 0.43
            zoom 0.8
            alpha 0.3
            linear 0.4 alpha 1.0 yalign 0.38
            linear 0.4 alpha 0.3 yalign 0.53
            repeat
        contains:
            anim.Filmstrip("battle/skills/dark_particles.png", (80, 80), (2, 1), .07, xalign=0.5, yalign=0.5)
            xalign 0.57
            yalign 0.63
            zoom 0.7
            alpha 1.0
            linear 0.5 alpha 0.3 yalign 0.69
            linear 0.5 alpha 1.0 yalign 0.75
            repeat
            
image reaction_dark2:
    parallel: 
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/strafe.png", im.matrix.desaturate() * im.matrix.tint(0.5, 0, 0.5)), (200, 200), (2, 2), .07, xalign=0.5, yalign=0.5)
            xalign 0.35 yalign 0.5
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/strafe.png", im.matrix.desaturate() * im.matrix.tint(0.5, 0, 0.5)), (200, 200), (2, 2), .09, xalign=0.5, yalign=0.5)
            xalign 0.55 yalign 0.5
        contains:
            anim.Filmstrip("battle/skills/dark_particles.png", (80, 80), (2, 1), .07, xalign=0.5, yalign=0.5)
            zoom 1.5
            xalign .45 yalign .3
            alignaround (.45, .5)
            linear 4.0 xalign .45 yalign .3 counterclockwise circles 3
            repeat
        contains:
            anim.Filmstrip("battle/skills/dark_particles.png", (80, 80), (2, 1), .07, xalign=0.5, yalign=0.5)
            zoom 1.5
            xalign .45 yalign .7
            alignaround (.45, .5)
            linear 4.0 xalign .45 yalign .7 counterclockwise circles 3
            repeat
        contains:
            anim.Filmstrip("battle/skills/dark_particles.png", (80, 80), (2, 1), .07, xalign=0.5, yalign=0.5)
            zoom 1.5
            xalign .25 yalign .5
            alignaround (.45, .5)
            linear 4.0 xalign .25 yalign .5 counterclockwise circles 3
            repeat
        contains:
            anim.Filmstrip("battle/skills/dark_particles.png", (80, 80), (2, 1), .07, xalign=0.5, yalign=0.5)
            zoom 1.5
            xalign .65 yalign .5
            alignaround (.45, .5)
            linear 4.0 xalign .65 yalign .5 counterclockwise circles 3
            repeat
            
image reaction_reddark:
    parallel: 
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/strafe.png", im.matrix.desaturate() * im.matrix.tint(1, 0.25, 0.25)), (200, 200), (2, 2), .07, xalign=0.5, yalign=0.5)
            xalign 0.41 yalign 0.5
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/strafe.png", im.matrix.desaturate() * im.matrix.tint(1, 0.25, 0.25)), (200, 200), (2, 2), .09, xalign=0.5, yalign=0.5)
            xalign 0.6 yalign 0.5
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/dark_particles.png", im.matrix.desaturate() * im.matrix.tint(1, 0.25, 0.25)), (80, 80), (2, 1), .07, xalign=0.5, yalign=0.5)
            xalign 0.65
            yalign 0.65
            zoom 1.3
            alpha 1.0
            linear 0.7 alpha 0.3 yalign 0.5
            linear 0.7 alpha 1.0 yalign 0.65
            repeat
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/dark_particles.png", im.matrix.desaturate() * im.matrix.tint(1, 0.25, 0.25)), (80, 80), (2, 1), .07, xalign=0.5, yalign=0.5)
            xalign 0.3
            yalign 0.35
            zoom 1.3
            alpha 1.0
            linear 0.7 alpha 0.3 yalign 0.1
            linear 0.7 alpha 1.0 yalign 0.25
            repeat  
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/dark_particles.png", im.matrix.desaturate() * im.matrix.tint(1, 0.25, 0.25)), (80, 80), (2, 1), .07, xalign=0.5, yalign=0.5)
            xalign 0.35
            yalign 0.7
            zoom 1.1
            alpha 0.3
            linear 0.6 alpha 1.0 yalign 0.7
            linear 0.6 alpha 0.3 yalign 0.75
            repeat
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/dark_particles.png", im.matrix.desaturate() * im.matrix.tint(1, 0.25, 0.25)), (80, 80), (2, 1), .07, xalign=0.5, yalign=0.5)
            xalign 0.45
            yalign 0.35
            zoom 1
            alpha 1.0
            linear 0.5 alpha 0.3 yalign 0.3
            linear 0.5 alpha 1.0 yalign 0.45
            repeat
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/dark_particles.png", im.matrix.desaturate() * im.matrix.tint(1, 0.25, 0.25)), (80, 80), (2, 1), .07, xalign=0.5, yalign=0.5)
            xalign 0.23
            yalign 0.43
            zoom 0.8
            alpha 0.3
            linear 0.4 alpha 1.0 yalign 0.38
            linear 0.4 alpha 0.3 yalign 0.53
            repeat
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/dark_particles.png", im.matrix.desaturate() * im.matrix.tint(1, 0.25, 0.25)), (80, 80), (2, 1), .07, xalign=0.5, yalign=0.5)
            xalign 0.57
            yalign 0.63
            zoom 0.7
            alpha 1.0
            linear 0.5 alpha 0.3 yalign 0.69
            linear 0.5 alpha 1.0 yalign 0.75
            repeat
            
image reaction_reddark2:
    parallel: 
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/strafe.png", im.matrix.desaturate() * im.matrix.tint(1, 0.25, 0.25)), (200, 200), (2, 2), .07, xalign=0.5, yalign=0.5)
            xalign 0.35 yalign 0.5
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/strafe.png", im.matrix.desaturate() * im.matrix.tint(1, 0.25, 0.25)), (200, 200), (2, 2), .09, xalign=0.5, yalign=0.5)
            xalign 0.55 yalign 0.5
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/dark_particles.png", im.matrix.desaturate() * im.matrix.tint(1, 0.25, 0.25)), (80, 80), (2, 1), .07, xalign=0.5, yalign=0.5)
            zoom 1.5
            xalign .45 yalign .3
            alignaround (.45, .5)
            linear 4.0 xalign .45 yalign .3 counterclockwise circles 3
            repeat
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/dark_particles.png", im.matrix.desaturate() * im.matrix.tint(1, 0.25, 0.25)), (80, 80), (2, 1), .07, xalign=0.5, yalign=0.5)
            zoom 1.5
            xalign .45 yalign .7
            alignaround (.45, .5)
            linear 4.0 xalign .45 yalign .7 counterclockwise circles 3
            repeat
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/dark_particles.png", im.matrix.desaturate() * im.matrix.tint(1, 0.25, 0.25)), (80, 80), (2, 1), .07, xalign=0.5, yalign=0.5)
            zoom 1.5
            xalign .25 yalign .5
            alignaround (.45, .5)
            linear 4.0 xalign .25 yalign .5 counterclockwise circles 3
            repeat
        contains:
            anim.Filmstrip(im.MatrixColor("battle/skills/dark_particles.png", im.matrix.desaturate() * im.matrix.tint(1, 0.25, 0.25)), (80, 80), (2, 1), .07, xalign=0.5, yalign=0.5)
            zoom 1.5
            xalign .65 yalign .5
            alignaround (.45, .5)
            linear 4.0 xalign .65 yalign .5 counterclockwise circles 3
            repeat
            
image reaction_skulls:
    parallel:
        contains:
            "battle/skills/skull.png"
            xalign 0.65
            yalign 0.65
            zoom 1.0
            alpha 0
            linear 0.7 alpha 1.0 yalign 0.5
            linear 0.7 alpha 0 yalign 0.35
            repeat
        contains:
            "battle/skills/skull.png"
            xalign 0.35
            yalign 0.75
            zoom 0.8
            alpha 0
            linear 0.6 alpha 1.0 yalign 0.7
            linear 0.6 alpha 0 yalign 0.55
            repeat
        contains:
            "battle/skills/skull.png"
            xalign 0.45
            yalign 0.45
            zoom 0.3
            alpha 0
            linear 0.5 alpha 1.0 yalign 0.3
            linear 0.5 alpha 0 yalign 0.15
            repeat
        contains:
            "battle/skills/skull.png"
            xalign 0.53
            yalign 0.53
            zoom 0.4
            alpha 0
            linear 0.4 alpha 1.0 yalign 0.38
            linear 0.4 alpha 0 yalign 0.23
            repeat
        contains:
            "battle/skills/skull.png"
            xalign 0.57
            yalign 0.75
            zoom 0.65
            alpha 0.3
            linear 0.5 alpha 1.0 yalign 0.69
            linear 0.5 alpha 0 yalign 0.54
            repeat
    
image reaction_explo_small:
    anim.Filmstrip("battle/skills/explo_small.png", (224, 192), (4, 5), .05, xalign=0.5, yalign=0.5)
    
image reaction_explo_med:
    anim.Filmstrip("battle/skills/explo_med.png", (512, 512), (4, 5), .05, xalign=0.5, yalign=0.5)
    
image reaction_explo_big:
    anim.Filmstrip("battle/skills/explo_big.png", (608, 608), (4, 5), .05, xalign=0.5, yalign=0.5)
    
image reaction_explo_small_noloop:
    anim.Filmstrip("battle/skills/explo_small.png", (224, 192), (4, 5), .05, loop=False, xalign=0.5, yalign=0.5)
    
image reaction_explo_med_noloop:
    anim.Filmstrip("battle/skills/explo_med.png", (512, 512), (4, 5), .05, loop=False, xalign=0.5, yalign=0.5)
    
image reaction_explo_big_noloop:
    anim.Filmstrip("battle/skills/explo_big.png", (608, 608), (4, 5), .05, loop=False, xalign=0.5, yalign=0.5)
    
image reaction_none:
    "#000"
    alpha 0
    
image reaction_slash:
    "battle/skills/slash.png" 
    xalign 0.1 yalign 0.5 rotate 0 alpha 0.3 yzoom -1
    linear 0.1 xalign 0.5 yalign 0.5 alpha 0.9 
    linear 0.1 xalign 1.0 yalign 0.5 alpha 0.3
    xalign 0.1 yalign 1.0 rotate 40 alpha 0.3
    linear 0.1 xalign 0.5 yalign 0.5 alpha 0.9
    linear 0.1 xalign 1.0 yalign 0.1 alpha 0.3
    xalign 0.1 yalign 0.1 rotate -50 alpha 0.3
    linear 0.1 xalign 0.5 yalign 0.5 alpha 0.9
    linear 0.1 xalign 1.0 yalign 1.0 alpha 0.3
    rotate 10
    repeat
    
image reaction_backslash:
    "battle/skills/slash.png" 
    xalign 1.0 yalign 0.5 rotate 0 alpha 0.3 yzoom -1
    linear 0.1 xalign 0.5 yalign 0.5 alpha 0.9 
    linear 0.1 xalign 0.1 yalign 0.5 alpha 0.3
    xalign 1.0 yalign 1.0 rotate 40 alpha 0.3
    linear 0.1 xalign 0.5 yalign 0.5 alpha 0.9
    linear 0.1 xalign 0.1 yalign 0.1 alpha 0.3
    xalign 1.0 yalign 0.1 rotate -50 alpha 0.3
    linear 0.1 xalign 0.5 yalign 0.5 alpha 0.9
    linear 0.1 xalign 0.1 yalign 1.0 alpha 0.3
    rotate 10
    repeat
    
image reaction_crusade:
    parallel:
        contains:
            "battle/skills/light_ray1.png"
            xalign 0.5 yalign 0.52 alpha 0 additive 1
            pause 0.2
            linear 0.3 alpha 1.0
            linear 1.0 alpha 0
        contains:
            "battle/skills/light_ray2.png"
            xalign 0.48 yalign 0.52 alpha 0 additive 1
            pause 0.3
            linear 0.3 alpha 1.0
            linear 1.0 alpha 0
        contains:
            "battle/skills/light_ray2.png"
            xalign 0.52 yalign 0.52 alpha 0 additive 1 xzoom -1
            pause 0.4
            linear 0.3 alpha 1.0
            linear 1.0 alpha 0
        contains:
            "battle/skills/light_ray2.png"
            xalign 0.46 yalign 0.5 alpha 0 additive 1 rotate 10
            pause 0.5
            linear 0.3 alpha 1.0
            linear 1.0 alpha 0
        contains:
            "battle/skills/light_ray2.png"
            xalign 0.54 yalign 0.5 alpha 0 additive 1 xzoom -1
            pause 0.45
            linear 0.3 alpha 1.0
            linear 1.0 alpha 0
        contains:
            "battle/skills/light_cloud.png"
            xalign 0.5 yalign 0.4 zoom 0
            linear 0.3 zoom 1
            pause 2.0
            linear 1.0 alpha 0
        contains:
            "battle/skills/light_aura.png"
            xalign 0.5 yalign 0.5 zoom 0 additive 1
            linear 0.3 zoom 1 yalign -0.05
            linear 2.0 yalign -0.2
            linear 1.0 alpha 0
    
image reaction_strafe:
    anim.Filmstrip("battle/skills/strafe.png", (200, 200), (2, 2), .07, xalign=0.5, yalign=0.5)
    xalign 0.2 yalign 0.55 alpha 1.0
    pause .28
    xalign 0.4 yalign 0.5
    pause .28
    xalign 0.6 yalign 0.45
    pause .28
    xalign 0.8 yalign 0.4
    pause .28
    alpha 0
    repeat
    
image reaction_enemystrafe:
    anim.Filmstrip("battle/skills/strafe.png", (200, 200), (2, 2), .07, xalign=0.5, yalign=0.5)
    xalign 0.8 yalign 0.4 alpha 1.0
    pause .28
    xalign 0.6 yalign 0.45
    pause .28
    xalign 0.4 yalign 0.5
    pause .28
    xalign 0.2 yalign 0.55
    pause .28
    alpha 0
    repeat
        
image wind_leaves1:
    anim.Filmstrip("battle/skills/wind_particle.png", (64, 64), (2, 2), .3)
    xalign 0.7 yalign 0.6
    linear 0.5 xalign 0.3 yalign 0.5
    linear 0.5 xalign 0.7 yalign 0.4
    repeat
        
image wind_leaves2:
    anim.Filmstrip("battle/skills/wind_particle.png", (64, 64), (2, 2), .2)
    xalign 0.6 yalign 0.5
    linear 0.5 xalign 0.4 yalign 0.4 rotate 2
    linear 0.5 xalign 0.6 yalign 0.3 rotate -2
    repeat
    
image reaction_wind:
    anim.Filmstrip("battle/skills/wind.png", (226, 226), (2, 2), .07)
    xalign 0.55 yalign 0.5 alpha 0.5 additive 0.5
    linear 0.1 xalign 0.6 yalign 0.51
    linear 0.1 xalign 0.55 yalign 0.5
    linear 0.1 xalign 0.5 yalign 0.49
    linear 0.1 xalign 0.55 yalign 0.5
    repeat

    

    
    
#FULLSCREEN ANIMATIONS
        
image fullscreen_regeneration_front:
    contains:
        "#5DFF4B"
        alpha 0
        linear 0.01 alpha 0.95
        pause 0.2
        linear 1.5 alpha 0
image fullscreen_regeneration_back = "fullscreen_regeneration_front"

image fullscreen_superup_front:
    contains:
        "#FFFFFF"
        alpha 0
        linear 0.01 alpha 0.95
        pause 0.2
        linear 1.5 alpha 0
image fullscreen_superup_back = "fullscreen_superup_front"
        
image fullscreen_desertfox_front:
    parallel:
        contains:
            "back/effects/storm_darkness.png"
            alpha 0
            linear 0.2 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.2 alpha 0
        contains:
            "battle/skills/rommel_head.png"
            xalign 0.5 yalign 0.45 zoom 0 alpha 0
            linear 0.3 alpha 0.7 zoom 1.0
            linear 0.1 alpha 0
            pause 1.0
            repeat
        contains:
            "battle/skills/rommel_head.png"
            xalign 0.75 yalign 0.25 zoom 0 alpha 0
            pause 0.2
            linear 0.3 alpha 0.7 zoom 0.9
            linear 0.1 alpha 0
            pause 0.8
            repeat
        contains:
            "battle/skills/rommel_head.png"
            xalign 0.25 yalign 0.65 zoom 0 alpha 0
            pause 0.4
            linear 0.3 alpha 0.7 zoom 1.0
            linear 0.1 alpha 0
            pause 0.6
            repeat
        contains:
            "battle/skills/rommel_head.png"
            xalign 0.15 yalign 0.35 zoom 0 alpha 0
            pause 0.6
            linear 0.3 alpha 0.7 zoom 0.7
            linear 0.1 alpha 0
            pause 0.4
            repeat
        contains:
            "battle/skills/rommel_head.png"
            xalign 0.85 yalign 0.7 zoom 0 alpha 0
            pause 0.8
            linear 0.3 alpha 0.7 zoom 0.9
            linear 0.1 alpha 0
            pause 0.2
            repeat
        contains:
            "battle/skills/rommel_head.png"
            xalign 0.4 yalign 0.55 zoom 0 alpha 0
            pause 1.0
            linear 0.3 alpha 0.7 zoom 0.8
            linear 0.1 alpha 0
            repeat
        contains:
            "#FFFFFF"
            alpha 0
            linear 0.01 alpha 0.95
            pause 0.2
            linear 1.5 alpha 0
    alpha 1.0
    pause 2.8
    linear 0.2 alpha 0
image fullscreen_desertfox_back = "fullscreen_desertfox_front"
    
image fullscreen_sandstorm_front:
    parallel:
        contains:
            anim.Filmstrip("battle/skills/wind.png", (226, 226), (2, 2), .07)
            alpha 0.8 xalign 0.77 yalign 0.13
            linear 0.3 xalign 0.87 yalign 0.28
            linear 0.3 xalign 0.77 yalign 0.43
            linear 0.3 xalign 0.67 yalign 0.28
            linear 0.3 xalign 0.77 yalign 0.13
            linear 0.3 xalign 0.87 yalign 0.28
            linear 0.3 xalign 0.77 yalign 0.43
            linear 0.3 xalign 0.67 yalign 0.28
            linear 0.3 xalign 0.77 yalign 0.13
            linear 0.3 xalign 0.87 yalign 0.28 alpha 0
        contains:
            anim.Filmstrip("battle/skills/wind.png", (226, 226), (2, 2), .07)
            alpha 0.8 xalign 0.77 yalign 0.43
            linear 0.3 xalign 0.67 yalign 0.28
            linear 0.3 xalign 0.77 yalign 0.13
            linear 0.3 xalign 0.87 yalign 0.28
            linear 0.3 xalign 0.77 yalign 0.43
            linear 0.3 xalign 0.67 yalign 0.28
            linear 0.3 xalign 0.77 yalign 0.13
            linear 0.3 xalign 0.87 yalign 0.28
            linear 0.3 xalign 0.77 yalign 0.43
            linear 0.3 xalign 0.67 yalign 0.28 alpha 0
        contains:
            "#FFFFFF"
            alpha 0
            linear 0.01 alpha 0.95
            pause 0.2
            linear 1.5 alpha 0
        contains:
            SnowBlossom(anim.Filmstrip("battle/skills/wind_particle.png", (64, 64), (2, 2), .3), 2000, 20, (1000, 3000), (200, 1000))
            alpha 1.0
            pause 2.0
            linear 1.0 alpha 0
image fullscreen_sandstorm_back = "fullscreen_sandstorm_front"

image fullscreen_germanianstrafe_front:
    parallel:
        contains:
            SnowBlossom(anim.Filmstrip(im.Crop("battle/units/airsupport_shrike_main1_attack.png", (0, 216, 1272, 216)), (318, 216), (4, 1), .05), 10, 300, (2000, 2100), (-800, -900))
            alpha 1.0
            pause 2.8
            linear 0.2 alpha 0
image fullscreen_germanianstrafe_back = "fullscreen_germanianstrafe_front"

image fullscreen_enemygermanianstrafe_back:
    parallel:
        contains:
            SnowBlossom(anim.Filmstrip("battle/units/airsupport_shrike_main1_attack.png", (318, 216), (4, 1), .05), 5, 300, (-1000, -1100), (800, 900), 0.5)
            alpha 1.0
            pause 2.8
            linear 0.2 alpha 0
image fullscreen_enemygermanianstrafe_front = "fullscreen_enemygermanianstrafe_back"
            
image fullscreen_zipangustrafe_front:
    parallel:
        contains:
            SnowBlossom(anim.Filmstrip(im.Crop("battle/units/airsupport_zero_main1_attack.png", (0, 216, 1200, 216)), (300, 216), (4, 1), .05), 10, 300, (2000, 2100), (-800, -900))
            alpha 1.0
            pause 2.8
            linear 0.2 alpha 0
image fullscreen_zipangustrafe_back = "fullscreen_zipangustrafe_front"
            
image fullscreen_fistsoffury_front:
    parallel:
        contains:
            "back/effects/bladekiru.png"
            pause 0.05
            "back/effects/bladekiru1.png"
            pause 0.05
            "back/effects/bladekiru2.png"
            pause 0.05
            "back/effects/bladekiru3.png"
            pause 0.05
            "back/effects/bladekiru4.png"
            pause 0.05
            repeat
        contains:
            "#FFFFFF"
            alpha 0
            linear 0.01 alpha 0.95
            pause 0.2
            linear 1.5 alpha 0
        pause 2.0
        linear 1.5 alpha 0
image fullscreen_fistsoffury_back = "fullscreen_fistsoffury_front"
            
image fullscreen_quickattack_front:
    parallel:
        contains:
            "back/effects/bladekiru.png"
            pause 0.05
            "back/effects/bladekiru1.png"
            pause 0.05
            "back/effects/bladekiru2.png"
            pause 0.05
            "back/effects/bladekiru3.png"
            pause 0.05
            "back/effects/bladekiru4.png"
            pause 0.05
            repeat
        contains:
            "#FFFFFF"
            alpha 0
            linear 0.01 alpha 0.95
            pause 0.2
            linear 1.5 alpha 0
        contains:
            SnowBlossom(anim.Filmstrip("battle/skills/wind_particle.png", (64, 64), (2, 2), .3), 2000, 20, (1000, 3000), (200, 1000))
            alpha 1.0
            pause 2.0
            linear 1.0 alpha 0
image fullscreen_quickattack_back = "fullscreen_quickattack_front"
            
image northexpedition_star:
    contains:
        "battle/skills/northexpedition_star.png"
        rotate 0
        linear 0.5 rotate 360
        repeat
        
image renin_star:
    contains:
        "battle/skills/renin_star.png"
        rotate 0
        linear 0.5 rotate -360
        repeat
    
image fullscreen_northexpedition_front:
    parallel:
        contains:
            "#FF0000"
            alpha 0
            linear 0.01 alpha 0.95
            pause 0.7
            linear 1.0 alpha 0
        contains:
            SnowBlossom("northexpedition_star", 2000, 20, (1000, 3000), (200, 1000))
            alpha 0.7
            pause 2.0
            linear 1.0 alpha 0
        contains:
            "battle/skills/northexpedition_kanji1.png"
            xalign 0.5 yalign 0.45 zoom 0 alpha 0
            linear 0.3 alpha 0.7 zoom 1.0
            linear 0.1 alpha 0
        contains:
            "battle/skills/northexpedition_kanji2.png"
            xalign 0.5 yalign 0.45 zoom 0 alpha 0
            pause 0.4
            linear 0.3 alpha 0.7 zoom 1.0
            linear 0.1 alpha 0
        contains:
            "battle/skills/northexpedition_kanji3.png"
            xalign 0.5 yalign 0.45 zoom 0 alpha 0
            pause 0.8
            linear 0.3 alpha 0.7 zoom 1.0
            linear 0.1 alpha 0
image fullscreen_northexpedition_back = "fullscreen_northexpedition_front"
            
image fullscreen_scarletrevolution_front:
    parallel:
        contains:
            "cg_scarletrevolution"
            alpha 0
            linear 0.01 alpha 0.95
            pause 0.8
            linear 1.9 alpha 0
        contains:
            "#FF0000"
            alpha 0
            linear 0.01 alpha 0.95
            pause 0.1
            linear 0.5 alpha 0
        contains:
            "reaction_explo_med_noloop"
            xalign 0.1
            yalign 0.6
            pause 0.9
            linear 0.1 alpha 0
        contains:
            "reaction_explo_big_noloop"
            xalign 0.9
            yalign 0.5
            pause 0.9
            linear 0.1 alpha 0
        contains:
            "fullscreen_fireball_front"
        contains:
            "back/effects/explosion2.png" with hpunch
            alpha 0.3
            xzoom -1
            yzoom -1
            xalign 0.1
            yalign 0.9
            0.25
            linear 0.5 xalign 0.9 yalign 0.1
            0.01
            linear 0.5 zoom 2.0 alpha 0
image fullscreen_scarletrevolution_back = "fullscreen_scarletrevolution_front"
            
image fullscreen_redgeneralissima_front:
    parallel:
        contains:
            "cg_redgeneralissima"
            alpha 0
            linear 0.01 alpha 0.95
            pause 0.8
            linear 1.9 alpha 0
        contains:
            "#FF0000"
            alpha 0
            linear 0.01 alpha 0.95
            pause 0.1
            linear 0.5 alpha 0
        contains:
            "reaction_explo_med_noloop"
            xalign 0.1
            yalign 0.6
            pause 0.9
            linear 0.1 alpha 0
        contains:
            "reaction_explo_big_noloop"
            xalign 0.9
            yalign 0.5
            pause 0.9
            linear 0.1 alpha 0
        contains:
            "fullscreen_fireball_front"
        contains:
            "back/effects/explosion2.png" with hpunch
            alpha 0.3
            xzoom -1
            yzoom -1
            xalign 0.1
            yalign 0.9
            0.25
            linear 0.5 xalign 0.9 yalign 0.1
            0.01
            linear 0.5 zoom 2.0 alpha 0
image fullscreen_redgeneralissima_back = "fullscreen_redgeneralissima_front"
            
image fullscreen_thousandyearstrike_front:
    parallel:
        contains:
            At("back/effects/storm_darkness.png", vpunch)
            pause 0.3
            At("back/effects/storm_darkness.png", hpunch)
            pause 0.3
            repeat
        contains:
            "cg_thousandyearstrike"
            alpha 0
            linear 0.01 alpha 0.95
            pause 0.7
            linear 1.0 alpha 0
        contains:
            "#FF0000"
            alpha 0
            linear 0.01 alpha 0.95
            pause 0.1
            linear 0.5 alpha 0

        contains:
            "fullscreen_fireball_front"
        contains:
            "back/effects/explosion2.png" with hpunch
            alpha 0.3
            xzoom -1
            yzoom -1
            xalign 0.1
            yalign 0.9
            0.25
            linear 0.5 xalign 0.9 yalign 0.1
            0.01
            linear 0.5 zoom 2.0 alpha 0
image fullscreen_thousandyearstrike_back = "fullscreen_thousandyearstrike_front"

image fullscreen_chomp_front:
    parallel:
        contains:
            At("back/effects/storm_darkness.png", vpunch)
            pause 0.3
            At("back/effects/storm_darkness.png", hpunch)
            pause 0.3
            repeat
        contains:
            "#000000"
            alpha 1.0
            pause 0.1
            linear 3.0 alpha 0
        contains:
            "battle/skills/chomp.png"
            xalign 0.5 yalign 0.45 zoom 0 alpha 0
            linear 0.3 alpha 0.7 zoom 1.0
            linear 0.1 alpha 0
            pause 1.0
            repeat
        contains:
            "battle/skills/chomp.png"
            xalign 0.75 yalign 0.25 zoom 0 alpha 0
            pause 0.2
            linear 0.3 alpha 0.7 zoom 0.9
            linear 0.1 alpha 0
            pause 0.8
            repeat
        contains:
            "battle/skills/chomp.png"
            xalign 0.25 yalign 0.65 zoom 0 alpha 0
            pause 0.4
            linear 0.3 alpha 0.7 zoom 1.0
            linear 0.1 alpha 0
            pause 0.6
            repeat
        contains:
            "battle/skills/chomp.png"
            xalign 0.15 yalign 0.35 zoom 0 alpha 0
            pause 0.6
            linear 0.3 alpha 0.7 zoom 0.7
            linear 0.1 alpha 0
            pause 0.4
            repeat
        contains:
            "battle/skills/chomp.png"
            xalign 0.85 yalign 0.7 zoom 0 alpha 0
            pause 0.8
            linear 0.3 alpha 0.7 zoom 0.9
            linear 0.1 alpha 0
            pause 0.2
            repeat
        contains:
            "battle/skills/chomp.png"
            xalign 0.4 yalign 0.55 zoom 0 alpha 0
            pause 1.0
            linear 0.3 alpha 0.7 zoom 0.8
            linear 0.1 alpha 0
            repeat
        
image fullscreen_chomp_back = "fullscreen_chomp_front"

image fullscreen_brains_front:
    parallel:
        contains:
            At("back/effects/storm_darkness.png", vpunch)
            pause 0.3
            At("back/effects/storm_darkness.png", hpunch)
            pause 0.3
            repeat
        contains:
            "#FF0000"
            alpha 1.0
            pause 0.1
            linear 3.0 alpha 0
        contains:
            "battle/skills/chomp.png"
            xalign 0.5 yalign 0.45 zoom 0 alpha 0
            linear 0.3 alpha 0.7 zoom 1.0
            linear 0.1 alpha 0
            pause 1.0
            repeat
        contains:
            "battle/skills/chomp.png"
            xalign 0.75 yalign 0.25 zoom 0 alpha 0
            pause 0.2
            linear 0.3 alpha 0.7 zoom 0.9
            linear 0.1 alpha 0
            pause 0.8
            repeat
        contains:
            "battle/skills/chomp.png"
            xalign 0.25 yalign 0.65 zoom 0 alpha 0
            pause 0.4
            linear 0.3 alpha 0.7 zoom 1.0
            linear 0.1 alpha 0
            pause 0.6
            repeat
        contains:
            "battle/skills/chomp.png"
            xalign 0.15 yalign 0.35 zoom 0 alpha 0
            pause 0.6
            linear 0.3 alpha 0.7 zoom 0.7
            linear 0.1 alpha 0
            pause 0.4
            repeat
        contains:
            "battle/skills/chomp.png"
            xalign 0.85 yalign 0.7 zoom 0 alpha 0
            pause 0.8
            linear 0.3 alpha 0.7 zoom 0.9
            linear 0.1 alpha 0
            pause 0.2
            repeat
        contains:
            "battle/skills/chomp.png"
            xalign 0.4 yalign 0.55 zoom 0 alpha 0
            pause 1.0
            linear 0.3 alpha 0.7 zoom 0.8
            linear 0.1 alpha 0
            repeat
        
image fullscreen_brains_back = "fullscreen_brains_front"

image fullscreen_brainwash_front:
    parallel:
        contains:
            At("back/effects/storm_darkness.png", vpunch)
            pause 0.3
            At("back/effects/storm_darkness.png", hpunch)
            pause 0.3
            repeat
        contains:
            "#000000"
            alpha 0
            linear 0.01 alpha 0.65
            linear 3.0 alpha 0
        contains:
            "battle/skills/obey1.png"
            xalign 0.5 yalign 0.45 zoom 0 alpha 0
            linear 0.3 alpha 0.7 zoom 1.0
            linear 0.1 alpha 0
            pause 1.0
            repeat
        contains:
            "battle/skills/obey1.png"
            xalign 0.75 yalign 0.25 zoom 0 alpha 0
            pause 0.2
            linear 0.3 alpha 0.7 zoom 0.9
            linear 0.1 alpha 0
            pause 0.8
            repeat
        contains:
            "battle/skills/obey1.png"
            xalign 0.25 yalign 0.65 zoom 0 alpha 0
            pause 0.4
            linear 0.3 alpha 0.7 zoom 1.0
            linear 0.1 alpha 0
            pause 0.6
            repeat
        contains:
            "battle/skills/obey1.png"
            xalign 0.15 yalign 0.35 zoom 0 alpha 0
            pause 0.6
            linear 0.3 alpha 0.7 zoom 0.7
            linear 0.1 alpha 0
            pause 0.4
            repeat
        contains:
            "battle/skills/obey1.png"
            xalign 0.85 yalign 0.7 zoom 0 alpha 0
            pause 0.8
            linear 0.3 alpha 0.7 zoom 0.9
            linear 0.1 alpha 0
            pause 0.2
            repeat
        contains:
            "battle/skills/obey1.png"
            xalign 0.4 yalign 0.55 zoom 0 alpha 0
            pause 1.0
            linear 0.3 alpha 0.7 zoom 0.8
            linear 0.1 alpha 0
            repeat
        contains:
            "#FF0000"
            alpha 0
            linear 0.01 alpha 0.95
            pause 0.2
            linear 1.5 alpha 0
        
image fullscreen_brainwash_back = "fullscreen_brainwash_front"

image fullscreen_quickmarch_front:
    parallel:
        contains:
            At("back/effects/storm_darkness.png", vpunch)
            pause 0.3
            At("back/effects/storm_darkness.png", hpunch)
            pause 0.3
            repeat
        
image fullscreen_quickmarch_back = "fullscreen_quickmarch_front"

image fullscreen_battlecry_front:
    parallel:
        contains:
            At("back/effects/storm_darkness.png", vpunch)
            pause 0.3
            At("back/effects/storm_darkness.png", hpunch)
            pause 0.3
            repeat
        contains:
            "#000000"
            alpha 0
            linear 0.01 alpha 0.65
            linear 3.0 alpha 0
        contains:
            "#FF0000"
            alpha 0
            linear 0.01 alpha 0.95
            pause 0.2
            linear 1.5 alpha 0
        
image fullscreen_battlecry_back = "fullscreen_battlecry_front"

image fullscreen_pureevil_front:
    parallel:
        contains:
            At("back/effects/storm_darkness.png", vpunch)
            pause 0.3
            At("back/effects/storm_darkness.png", hpunch)
            pause 0.3
            repeat
        contains:
            "hitora hat powers large fade"
            xalign 0.5
            yalign 1.0
            alpha 1.0
            linear 3.0 alpha 0
        contains:
            "#FF0000"
            alpha 0
            linear 0.01 alpha 0.95
            pause 0.1
            linear 0.5 alpha 0
        contains:
            "fullscreen_fireball_front"
        contains:
            "back/effects/explosion2.png" with hpunch
            alpha 0.3
            xzoom -1
            yzoom -1
            xalign 0.1
            yalign 0.9
            0.25
            linear 0.5 xalign 0.9 yalign 0.1
            0.01
            linear 0.5 zoom 2.0 alpha 0
image fullscreen_pureevil_back = "fullscreen_pureevil_front"

image fullscreen_polka_front:
    parallel:
        contains:
            At("back/effects/storm_darkness.png", vpunch)
            pause 0.3
            At("back/effects/storm_darkness.png", hpunch)
            pause 0.3
            repeat
        contains:
            SnowBlossom("battle/skills/musicnote.png", 100, 50, (-3500), (0), fast=True, horizontal=True)
            pause 2.0
            linear 1.0 alpha 0
image fullscreen_polka_back = "fullscreen_polka_front"

image fullscreen_cyberstrike_front:
    parallel:
        contains:
            At("back/effects/storm_darkness.png", vpunch)
            pause 0.3
            At("back/effects/storm_darkness.png", hpunch)
            pause 0.3
            repeat
        contains:
            SnowBlossom(im.MatrixColor("battle/skills/katyusha.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.2, 0.2)), 1000, 0, (-4200), (3500))
            pause 2.0
            linear 1.0 alpha 0
        contains:
            "cg_cyberstrike"
            alpha 0
            linear 0.01 alpha 0.95
            pause 0.7
            linear 1.0 alpha 0
        contains:
            "#FF0000"
            alpha 0
            linear 0.01 alpha 0.95
            pause 0.1
            linear 0.5 alpha 0
        contains:
            "fullscreen_fireball_front"
        contains:
            "back/effects/explosion2.png" with hpunch
            alpha 0.3
            xzoom -1
            yzoom -1
            xalign 0.1
            yalign 0.9
            0.25
            linear 0.5 xalign 0.9 yalign 0.1
            0.01
            linear 0.5 zoom 2.0 alpha 0
image fullscreen_cyberstrike_back = "fullscreen_pureevil_front"

image fullscreen_nanoattack_front:
    parallel:
        contains:
            "#16B334"
            alpha 0
            linear 0.01 alpha 0.95
            pause 0.1
            linear 0.5 alpha 0
        contains:
            "back/effects/explosion2.png" with hpunch
            alpha 0.3
            xzoom -1
            yzoom -1
            xalign 0.1
            yalign 0.9
            0.25
            linear 0.5 xalign 0.9 yalign 0.1
            0.01
            linear 0.5 zoom 2.0 alpha 0
        contains:
            SnowBlossom(anim.Filmstrip("battle/skills/digital.png", (25, 25), (2, 1), .4), 1000, 50, (0), (700))
            pause 2.0
            linear 1.0 alpha 0
        contains:
            SnowBlossom(anim.Filmstrip("battle/skills/digital.png", (25, 25), (2, 1), .4), 1000, 50, (0), (700))
            pause 2.0
            linear 1.0 alpha 0
        contains:
            SnowBlossom(anim.Filmstrip("battle/skills/digital2.png", (25, 25), (2, 1), .4), 1000, 50, (0), (700))
            pause 2.0
            linear 1.0 alpha 0
        contains:
            SnowBlossom(anim.Filmstrip("battle/skills/digital2.png", (25, 25), (2, 1), .4), 1000, 50, (0), (700))
            pause 2.0
            linear 1.0 alpha 0
image fullscreen_nanoattack_back = "fullscreen_pureevil_front"

image fullscreen_doppelganger_front:
    parallel:
        contains:
            At("back/effects/storm_darkness.png", vpunch)
            pause 0.3
            At("back/effects/storm_darkness.png", hpunch)
            pause 0.3
            repeat
        contains:
            "#FFFFFF"
            alpha 0
            linear 0.01 alpha 0.95
            pause 0.1
            linear 0.5 alpha 0
image fullscreen_doppelganger_back = "fullscreen_pureevil_front"

image fullscreen_electricstorm_front:
    parallel:
        contains:
            "back/effects/storm_darkness.png"
            alpha 0
            linear 0.2 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.2 alpha 0
        contains:
            "cg_storm"
            alpha 1.0
            pause 0.5
            linear 0.6 alpha 0
image fullscreen_electricstorm_back = "fullscreen_electricstorm_front"
        
image fullscreen_shockwave_front:
    parallel:
        contains:
            "back/effects/storm_darkness.png"
            alpha 0
            linear 0.2 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.2 alpha 0

image fullscreen_shockwave_back = "fullscreen_shockwave_front"
            
image fullscreen_fireball_front:
    parallel:
        contains:
            SnowBlossom(anim.Filmstrip("back/effects/spark.png", (12.5, 12.5), (4, 4), .13), 20, 20, (20, 400), (-20, -500), 3)
            alpha 1.0
            pause 2.0
            linear 1.0 alpha 0
        contains:
            SnowBlossom(anim.Filmstrip("back/effects/spark.png", (12.5, 12.5), (4, 4), .13), 20, 20, (20, 400), (-20, -500), 3)
            alpha 1.0
            pause 2.0
            linear 1.0 alpha 0
        contains:
            SnowBlossom(anim.Filmstrip("back/effects/spark.png", (12.5, 12.5), (4, 4), .13), 20, 20, (20, 400), (-20, -500), 3)
            zoom 1.5 alpha 0.4
            pause 2.0
            linear 1.0 alpha 0
        contains:
            SnowBlossom(anim.Filmstrip("back/effects/spark.png", (12.5, 12.5), (4, 4), .13), 20, 20, (20, 400), (-20, -500), 3)
            zoom 1.2 alpha 0.8
            pause 2.0
            linear 1.0 alpha 0
image fullscreen_fireball_back = "fullscreen_fireball_front"
            
image fullscreen_iceburst_front:
    parallel:
        contains:
            "back/effects/storm_darkness.png"
            alpha 0
            linear 0.2 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.2 alpha 0
        contains:
            SnowBlossom("back/effects/snowflake.png", 200, 20, (-20, -800), (20, 600))
            zoom 0.5 alpha 0.3
            pause 2.0
            linear 1.0 alpha 0
        contains:
            SnowBlossom("back/effects/snowflake.png", 200, 20, (-20, -800), (20, 600))
            alpha 0.7
            pause 2.0
            linear 1.0 alpha 0
        contains:
            SnowBlossom("back/effects/snowflake.png", 200, 20, (-20, -800), (20, 600))
            zoom 2.0 alpha 0.5
            pause 2.0
            linear 1.0 alpha 0
        contains:
            SnowBlossom("back/effects/snowflake.png", 200, 20, (-20, -800), (20, 600))
            zoom 2.0 alpha 0.5
            pause 2.0
            linear 1.0 alpha 0
        contains:
            SnowBlossom("back/effects/snowflake.png", 200, 20, (-20, -800), (20, 600))
            zoom 3.0 alpha 0.4
            pause 2.0
            linear 1.0 alpha 0
        contains:
            SnowBlossom("back/effects/snowflake.png", 200, 20, (-20, -800), (20, 600))
            zoom 7.0 alpha 0.3
            pause 2.0
            linear 1.0 alpha 0
        contains:
            SnowBlossom("back/effects/snowflake.png", 200, 20, (-20, -800), (20, 600))
            zoom 10.0 alpha 0.2
            pause 2.0
            linear 1.0 alpha 0
image fullscreen_iceburst_back = "fullscreen_iceburst_front"
            
image fullscreen_frozenwinter_front:
    parallel:
        contains:
            "back/effects/storm_darkness.png"
            alpha 0
            linear 0.2 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.2 alpha 0
        contains:
            SnowBlossom("battle/skills/icicle.png", 120, 20, (-400, -500), (2500, 3000), 3)
            alpha 1.0
            pause 2.0
            linear 1.0 alpha 0
        contains:
            SnowBlossom(At("battle/skills/ice_particle.png", full_spin), 30, 20, (-20, -40), (200, 400), 3)
            zoom 1.2 alpha 0.8
            pause 2.0
            linear 1.0 alpha 0
            
image fullscreen_frozenwinter_back:
    parallel:
        contains:
            "back/effects/storm_darkness.png"
            alpha 0
            linear 0.2 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.2 alpha 0
        contains:
            SnowBlossom(At("battle/skills/icicle.png", flip_horizontal), 120, 20, (400, 500), (2500, 3000), 3)
            alpha 1.0
            pause 2.0
            linear 1.0 alpha 0
        contains:
            SnowBlossom(At("battle/skills/ice_particle.png", full_spin), 30, 20, (20, 40), (200, 400), 3)
            zoom 1.2 alpha 0.8
            pause 2.0
            linear 1.0 alpha 0
            
image fullscreen_truebalance_front:
    parallel:
        contains:
            SnowBlossom("back/effects/snowflake.png", 250, 20, (0, 0), (-120, -1600))
            alpha 1.0
            pause 2.0
            linear 1.0 alpha 0
        contains:
            "battle/skills/light_aura.png"
            xalign 0.5 yalign 0.9 zoom 0 additive 1
            linear 0.3 zoom 4 yalign -0.9
            linear 2.0 yalign 0.1
            linear 1.0 alpha 0
        contains:
            "#FFFFFF"
            alpha 0
            linear 0.01 alpha 0.95
            pause 0.2
            linear 1.5 alpha 0
image fullscreen_truebalance_back = "fullscreen_truebalance_front"
            
image fullscreen_patience_front:
    parallel:
        contains:
            "battle/skills/patience.png"
            alpha 0.9 xalign 0.5 yalign 0.5 zoom 2.0
            linear 3.0 zoom 0.5 alpha 0
        contains:
            SnowBlossom("battle/skills/ice_particle.png", 2000, 20, (100, 300), (200, 400))
            alpha 0
            pause 2.0
            linear 0.35 alpha 1.0
            linear 0.35 alpha 0
        contains:
            SnowBlossom(anim.Filmstrip("battle/skills/autumnleaf.png", (34, 34), (1, 1), .13), 2000, 20, (100, 300), (200, 400))
            alpha 0
            pause 1.5
            linear 0.35 alpha 1.0
            linear 0.35 alpha 0
        contains:
            SnowBlossom(anim.Filmstrip("battle/skills/wind_particle.png", (64, 64), (2, 2), .3), 2000, 20, (100, 300), (200, 400))
            alpha 0
            pause 1.0
            linear 0.35 alpha 1.0
            linear 0.35 alpha 0
        contains:
            SnowBlossom(anim.Filmstrip("gui/petal.png", (20, 20), (2, 1), .13), 2000, 20, (100, 300), (200, 400))
            alpha 0
            pause 0.5
            linear 0.35 alpha 1.0
            linear 0.35 alpha 0
        contains:
            "#FFFFFF"
            alpha 0
            linear 0.01 alpha 0.95
            pause 0.2
            linear 1.5 alpha 0
image fullscreen_patience_back = "fullscreen_patience_front"
            
image fullscreen_bushido_front:
    parallel:
        contains:
            "#000000"
            alpha 0
            linear 0.01 alpha 0.95
            pause 0.2
            linear 1.5 alpha 0
        contains:
            "cg_bushido"
            alpha 0
            linear 0.01 alpha 0.95
            pause 0.5
            linear 1.0 alpha 0
        contains:
            SnowBlossom(anim.Filmstrip("gui/petal.png", (20, 20), (2, 1), .13), 2000, 20, (100, 300), (200, 400))
            alpha 1.0
            pause 2.0
            linear 1.0 alpha 0
        contains:
            "#000000"
            alpha 0
            linear 0.01 alpha 0.95
            pause 0.2
            linear 1.5 alpha 0
image fullscreen_bushido_back = "fullscreen_bushido_front"
            
image fullscreen_samurai_front:
    parallel:
        contains:
            "cg_samurai"
            alpha 0
            linear 0.01 alpha 0.95
            pause 0.8
            linear 1.0 alpha 0
        contains:
            SnowBlossom(anim.Filmstrip("gui/petal.png", (20, 20), (2, 1), .13), 2000, 20, (100, 300), (200, 400))
            alpha 1.0
            pause 2.0
            linear 1.0 alpha 0
        contains:
            "#FFFFFF"
            alpha 0
            linear 0.01 alpha 0.95
            pause 0.2
            linear 1.5 alpha 0
image fullscreen_samurai_back = "fullscreen_samurai_front"
            
image fullscreen_rainyseason_front:
    parallel:
        contains:
            "back/effects/storm_darkness.png"
            alpha 0
            linear 0.2 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.2 alpha 0
        contains:
            "heavyrain"
            alpha 0
            linear 0.01 alpha 0.95
            pause 1.8
            linear 1.0 alpha 0
        contains:
            "#FFFFFF"
            alpha 0
            linear 0.01 alpha 0.95
            pause 0.2
            linear 1.5 alpha 0
image fullscreen_rainyseason_back = "fullscreen_rainyseason_front"
            
image fullscreen_autumnbreeze_front:
    parallel:
        contains:
            SnowBlossom(anim.Filmstrip("battle/skills/autumnleaf.png", (34, 34), (1, 1), .13), 2000, 20, (100, 300), (200, 400))
            alpha 1.0
            pause 2.0
            linear 1.0 alpha 0
        contains:
            "#FFCC00"
            alpha 0
            linear 0.01 alpha 0.95
            pause 0.2
            linear 1.5 alpha 0
image fullscreen_autumnbreeze_back = "fullscreen_autumnbreeze_front"
            
image fullscreen_summerdance_front:
    parallel:
        contains:
            "#FFFFFF"
            alpha 0
            linear 0.01 alpha 0.95
            pause 0.2
            linear 1.5 alpha 0
        contains:
            "cg_summerdance"
            alpha 0
            linear 0.01 alpha 0.75
            pause 2.0
            linear 1.0 alpha 0
        contains:
            SnowBlossom(anim.Filmstrip("gui/petal.png", (20, 20), (2, 1), .13), 2000, 20, (100, 300), (200, 400))
            alpha 1.0
            pause 2.0
            linear 1.0 alpha 0
image fullscreen_summerdance_back = "fullscreen_summerdance_front"
            
image fullscreen_typhoon_front:
    parallel:
        contains:
            anim.Filmstrip("battle/skills/wind.png", (226, 226), (2, 2), .07)
            alpha 0.8 xalign 0.77 yalign 0.13
            linear 0.3 xalign 0.87 yalign 0.28
            linear 0.3 xalign 0.77 yalign 0.43
            linear 0.3 xalign 0.67 yalign 0.28
            linear 0.3 xalign 0.77 yalign 0.13
            linear 0.3 xalign 0.87 yalign 0.28
            linear 0.3 xalign 0.77 yalign 0.43
            linear 0.3 xalign 0.67 yalign 0.28
            linear 0.3 xalign 0.77 yalign 0.13
            linear 0.3 xalign 0.87 yalign 0.28 alpha 0
        contains:
            anim.Filmstrip("battle/skills/wind.png", (226, 226), (2, 2), .07)
            alpha 0.8 xalign 0.77 yalign 0.43
            linear 0.3 xalign 0.67 yalign 0.28
            linear 0.3 xalign 0.77 yalign 0.13
            linear 0.3 xalign 0.87 yalign 0.28
            linear 0.3 xalign 0.77 yalign 0.43
            linear 0.3 xalign 0.67 yalign 0.28
            linear 0.3 xalign 0.77 yalign 0.13
            linear 0.3 xalign 0.87 yalign 0.28
            linear 0.3 xalign 0.77 yalign 0.43
            linear 0.3 xalign 0.67 yalign 0.28 alpha 0
        contains:
            "battle/skills/wave.png"
            xalign 4.5 yalign 1.5
            linear 1.5 xalign 2.5 yalign 1.0
            linear 0.75 xalign 1.5 alpha 0 yalign 1.25
        contains:
            "battle/skills/wave.png"
            xalign 3.5 yalign 1.5
            linear 1.5 xalign 1.5 yalign 1.0
            linear 0.75 xalign 0.5 alpha 0 yalign 1.25
        contains:
            "battle/skills/wave.png"
            xalign 2.5 yalign 1.5
            linear 1.5 xalign 0.5 yalign 1.0
            linear 0.75 xalign -0.5 alpha 0 yalign 1.25
        contains:
            "battle/skills/wave.png"
            xalign 1.5 yalign 1.5
            linear 1.5 xalign -0.5 yalign 1.0
            linear 0.75 xalign -1.5 alpha 0 yalign 1.25
        contains:
            "battle/skills/wave.png"
            xalign 0.5 yalign 1.5
            linear 1.5 xalign -1.5 yalign 1.0
            linear 0.75 xalign -2.5 alpha 0 yalign 1.25
        contains:
            "#FFFFFF"
            alpha 0
            linear 0.01 alpha 0.95
            pause 0.2
            linear 1.5 alpha 0
        contains:
            SnowBlossom(anim.Filmstrip("battle/skills/wind_particle.png", (64, 64), (2, 2), .3), 2000, 20, (1000, 3000), (200, 1000))
            alpha 1.0
            pause 2.0
            linear 1.0 alpha 0
image fullscreen_typhoon_back = "fullscreen_typhoon_front"
    
image fullscreen_bombardment_front:
    parallel:
        contains:
            "back/effects/storm_darkness.png"
            alpha 0
            linear 0.2 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.2 alpha 0
        contains:
            anim.Filmstrip("battle/skills/explo_med.png", (512, 512), (4, 5), .05, xalign=0.5, yalign=0.5)
            xalign 0.45 yalign 0.35 alpha 1.0
            pause 1.0
            linear 0.3 alpha 0
        contains:
            anim.Filmstrip("battle/skills/explo_med.png", (512, 512), (4, 5), .04, xalign=0.5, yalign=0.5)
            xalign 0.5 yalign 0.2 alpha 0
            pause 0.8
            alpha 1.0
            pause 1.0
            linear 0.3 alpha 0
        contains:
            anim.Filmstrip("battle/skills/explo_med.png", (512, 512), (4, 5), .03, xalign=0.5, yalign=0.5)
            xalign 0.25 yalign 0.5 alpha 0
            pause 1.0
            alpha 1.0
            pause 1.0
            linear 0.3 alpha 0
        contains:
            anim.Filmstrip("battle/skills/explo_med.png", (512, 512), (4, 5), .05, xalign=0.5, yalign=0.5)
            xalign 0.05 yalign 0.4 alpha 0
            pause 1.2
            alpha 1.0
            pause 1.0
            linear 0.3 alpha 0
        contains:
            anim.Filmstrip("battle/skills/explo_med.png", (512, 512), (4, 5), .04, xalign=0.5, yalign=0.5)
            xalign 0.15 yalign 0.6 alpha 0
            pause 1.5
            alpha 1.0
            pause 1.0
            linear 0.3 alpha 0
            
image fullscreen_bombardment_back:
    parallel:
        contains:
            "back/effects/storm_darkness.png"
            alpha 0
            linear 0.2 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.2 alpha 0
        contains:
            anim.Filmstrip("battle/skills/explo_med.png", (512, 512), (4, 5), .05, xalign=0.5, yalign=0.5)
            xalign 0.5 yalign 0.25 alpha 1.0
            pause 1.0
            linear 0.3 alpha 0
        contains:
            anim.Filmstrip("battle/skills/explo_med.png", (512, 512), (4, 5), .04, xalign=0.5, yalign=0.5)
            xalign 0.4 yalign 0.55 alpha 0
            pause 0.8
            alpha 1.0
            pause 1.0
            linear 0.3 alpha 0
        contains:
            anim.Filmstrip("battle/skills/explo_med.png", (512, 512), (4, 5), .03, xalign=0.5, yalign=0.5)
            xalign 0.65 yalign 0.1 alpha 0
            pause 1.0
            alpha 1.0
            pause 1.0
            linear 0.3 alpha 0
        contains:
            anim.Filmstrip("battle/skills/explo_med.png", (512, 512), (4, 5), .05, xalign=0.5, yalign=0.5)
            xalign 0.95 yalign 0.2 alpha 0
            pause 1.2
            alpha 1.0
            pause 1.0
            linear 0.3 alpha 0
        contains:
            anim.Filmstrip("battle/skills/explo_med.png", (512, 512), (4, 5), .04, xalign=0.5, yalign=0.5)
            xalign 0.85 yalign 0.05 alpha 0
            pause 1.5
            alpha 1.0
            pause 1.0
            linear 0.3 alpha 0
          
image fullscreen_groundpound_front:
    parallel:
        contains:
            "back/effects/storm_darkness.png"
            alpha 0
            linear 0.2 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.2 alpha 0
        contains:
            SnowBlossom("battle/skills/ground.png", 20, 20, (0, 0), (1000, 3000), 3)
            pause 2.0
            linear 1.0 alpha 0
        contains:
            "#FFFFFF"
            alpha 0
            linear 0.01 alpha 0.95
            pause 0.2
            linear 1.5 alpha 0
image fullscreen_groundpound_back = "fullscreen_groundpound_front"
            
image earth_big:
    "battle/skills/earth.png"
    zoom 2.0
            
image earth_medium:
    "battle/skills/earth.png"
    zoom 0.5
    
image earth_small:
    "battle/skills/earth.png"
    zoom 0.3
            
image fullscreen_earthstrike_front:
    parallel:
        contains:
            "back/effects/storm_darkness.png"
            alpha 0
            linear 0.2 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.2 alpha 0
        contains:
            SnowBlossom(At("earth_big", full_spin), 3, 20, (-400, -500), (500, 600), 3)
            alpha 0.6
            pause 2.0
            linear 1.0 alpha 0
        contains:
            SnowBlossom(At("battle/skills/earth.png", full_spin), 5, 20, (-600, -800), (600, 800), 3)
            alpha 0.7
            pause 2.0
            linear 1.0 alpha 0
        contains:
            SnowBlossom(At("earth_medium", full_spin), 8, 40, (-800, -1000), (1000, 1200), 3)
            alpha 0.8
            pause 2.0
            linear 1.0 alpha 0
        contains:
            SnowBlossom(At("earth_small", full_spin), 10, 80, (-1400, -1500), (1500, 1600), 3)
            alpha 0.9
            pause 2.0
            linear 1.0 alpha 0
        contains:
            "#FFFFFF"
            alpha 0
            linear 0.01 alpha 0.95
            pause 0.2
            linear 1.5 alpha 0
image fullscreen_earthstrike_back = "fullscreen_earthstrike_front"
            
image fullscreen_pose_front:
    contains:
        "#FFFFFF"
        alpha 0
        linear 0.01 alpha 0.95
        pause 0.2
        linear 1.5 alpha 0
image fullscreen_pose_back = "fullscreen_pose_front"
            
image clock_huge:
    "battle/skills/clock.png"
    zoom 4.0
    
image clock_big:
    "battle/skills/clock.png"
    zoom 2.0
            
image clock_medium:
    "battle/skills/clock.png"
    zoom 0.5
    
image clock_small:
    "battle/skills/clock.png"
    zoom 0.3
            
image fullscreen_finesthour_front:
    parallel:
        contains:
            "back/effects/storm_darkness.png"
            alpha 0
            linear 0.2 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.2 alpha 0
        contains:
            SnowBlossom(At("clock_huge", full_reverse_spin), 2, 20, (-200, -300), (200, 400), 3)
            alpha 0.4
            pause 2.0
            linear 1.0 alpha 0
        contains:
            SnowBlossom(At("clock_big", full_reverse_spin), 3, 20, (-400, -500), (500, 600), 3)
            alpha 0.6
            pause 2.0
            linear 1.0 alpha 0
        contains:
            SnowBlossom(At("battle/skills/clock.png", full_reverse_spin), 5, 20, (-600, -800), (600, 800), 3)
            alpha 0.7
            pause 2.0
            linear 1.0 alpha 0
        contains:
            SnowBlossom(At("clock_medium", full_reverse_spin), 8, 40, (-800, -1000), (1000, 1200), 3)
            alpha 0.8
            pause 2.0
            linear 1.0 alpha 0
        contains:
            SnowBlossom(At("clock_small", full_reverse_spin), 10, 80, (-1400, -1500), (1500, 1600), 3)
            alpha 0.9
            pause 2.0
            linear 1.0 alpha 0
        contains:
            "#FFFFFF"
            alpha 0
            linear 0.01 alpha 0.95
            pause 0.2
            linear 1.5 alpha 0
image fullscreen_finesthour_back = "fullscreen_finesthour_front"
            
image fullscreen_prismblast_front:
    parallel:
        contains:
            "back/effects/storm_darkness.png"
            alpha 0
            linear 0.2 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.2 alpha 0
        contains:
            "#FFFFFF"
            alpha 0
            linear 0.01 alpha 0.95
            pause 0.2
            linear 1.5 alpha 0
        contains:
            SnowBlossom(At("battle/skills/prism_big.png", full_spin), 20, 0, (-2000, -4000), (0, 0), 3)
            alpha 1.0
            pause 2.0
            linear 1.0 alpha 0
        contains:
            SnowBlossom("battle/skills/prism_small.png", 120, 20, (-500, -1000), (2500, 3000), 3)
            alpha 1.0
            pause 2.0
            linear 1.0 alpha 0
        contains:
            SnowBlossom(At("battle/skills/prism.png", full_spin), 30, 20, (-20, -40), (200, 400), 3)
            zoom 1.2 alpha 0.8
            pause 2.0
            linear 1.0 alpha 0
image fullscreen_prismblast_back = "fullscreen_prismblast_front"
            
image shooting_stars:
    parallel:
        contains:
            alpha 0.5
            "back/effects/ef1.jpg"
            zoom 2.0
            xalign 0
            yalign 0.99
            pause 0.05
            linear 0.1 xalign 1.0 yalign -0.01
            repeat
        contains:
            alpha 0.5
            "back/effects/ef3.jpg"
            zoom 2.0
            xalign 0
            yalign 0.99
            linear 0.1 xalign 1.0 yalign -0.01
            repeat
            
image fullscreen_crusade_front:
    parallel:
        contains:
            "back/effects/explosion3.png" with hpunch
            alpha 0.5
            xzoom -1
            yzoom -1
            xalign 0.1
            yalign 0.9
            0.25
            linear 0.5 xalign 0.9 yalign 0.1
            0.25
            linear 0.5 zoom 2.0 alpha 0
        contains:
            "shooting_stars"
            alpha 1.0
            pause 2.0
            linear 1.0 alpha 0
        contains:
            alpha 0
            pause 1.5
            alpha 1.0
            "back/effects/explosion2.png"
            linear 1.0 zoom 1.0 alpha 0 yalign 0.5
            "back/effects/explosion1.png"
            linear 1.0 zoom 1.0 alpha 0 yalign 0.5
            "back/effects/explosion3.png"
            linear 1.0 zoom 1.0 alpha 0 yalign 0.5
image fullscreen_crusade_back = "fullscreen_crusade_front"
            
image fullscreen_mustardgas_front:
    parallel:
        contains:
            "grime"
            pause 2.0
            linear 1.0 alpha 0
        contains:
            "battle/skills/skull.png"
            xalign 0.15
            yalign 0.35
            zoom 1.0
            alpha 0
            linear 0.7 alpha 1.0 yalign 0.25
            linear 0.7 alpha 0 yalign 0.1
            repeat
        contains:
            "battle/skills/skull.png"
            xalign 0.65
            yalign 0.65
            zoom 1.0
            alpha 0
            linear 0.7 alpha 1.0 yalign 0.5
            linear 0.7 alpha 0 yalign 0.35
            repeat
        contains:
            "battle/skills/skull.png"
            xalign 0.35
            yalign 0.75
            zoom 0.8
            alpha 0
            linear 0.6 alpha 1.0 yalign 0.7
            linear 0.6 alpha 0 yalign 0.55
            repeat
        contains:
            "battle/skills/skull.png"
            xalign 0.85
            yalign 0.75
            zoom 0.8
            alpha 0
            linear 0.6 alpha 1.0 yalign 0.7
            linear 0.6 alpha 0 yalign 0.55
            repeat
        contains:
            "battle/skills/skull.png"
            xalign 0.45
            yalign 0.45
            zoom 0.3
            alpha 0
            linear 0.5 alpha 1.0 yalign 0.3
            linear 0.5 alpha 0 yalign 0.15
            repeat
        contains:
            "battle/skills/skull.png"
            xalign 0.75
            yalign 0.55
            zoom 0.3
            alpha 0
            linear 0.5 alpha 1.0 yalign 0.3
            linear 0.5 alpha 0 yalign 0.15
            repeat
        contains:
            "battle/skills/skull.png"
            xalign 0.53
            yalign 0.53
            zoom 0.4
            alpha 0
            linear 0.4 alpha 1.0 yalign 0.38
            linear 0.4 alpha 0 yalign 0.23
            repeat
        contains:
            "battle/skills/skull.png"
            xalign 0.57
            yalign 0.75
            zoom 0.65
            alpha 0.3
            linear 0.5 alpha 1.0 yalign 0.69
            linear 0.5 alpha 0 yalign 0.54
            repeat
        contains:
            "battle/skills/skull.png"
            xalign 0.93
            yalign 0.53
            zoom 0.4
            alpha 0
            linear 0.4 alpha 1.0 yalign 0.38
            linear 0.4 alpha 0 yalign 0.23
            repeat
        contains:
            "battle/skills/skull.png"
            xalign 0.1
            yalign 0.73
            zoom 0.4
            alpha 0
            linear 0.4 alpha 1.0 yalign 0.68
            linear 0.4 alpha 0 yalign 0.53
            repeat
        contains:
            "yellowsmoke"
            pause 2.0
            linear 1.0 alpha 0
image fullscreen_mustardgas_back = "fullscreen_mustardgas_front"
            
image fullscreen_absorb_front:
    parallel:
        contains:
            "#FFFFFF"
            alpha 0 xalign 0.5 yalign 0.5
            linear 0.2 alpha 0.6
            linear 0.5 alpha 0.3
            linear 0.5 alpha 0.6
            linear 0.5 alpha 0.3
            linear 0.5 alpha 0.6
            linear 0.2 alpha 0
image fullscreen_absorb_back = "fullscreen_absorb_front"
            
image fullscreen_powerofrenin_front:
    parallel:
        contains:
            "#FF0000"
            alpha 0 xalign 0.5 yalign 0.5
            linear 0.2 alpha 0.6
            linear 0.5 alpha 0.3
            linear 0.5 alpha 0.6
            linear 0.5 alpha 0.3
            linear 0.5 alpha 0.6
            linear 0.2 alpha 0
        contains:
            "back/effects/storm_darkness.png"
            alpha 0
            linear 0.2 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.2 alpha 0
        contains:
            SnowBlossom("renin_star", 2000, 20, (-1000, -3000), (1000, 3000))
            zoom 0.5 alpha 0.3
            pause 2.0
            linear 1.0 alpha 0
        contains:
            SnowBlossom("renin_star", 2000, 20, (-1000, -3000), (1000, 3000))
            alpha 0.7
            pause 2.0
            linear 1.0 alpha 0
image fullscreen_powerofrenin_back = "fullscreen_powerofrenin_front"
            
image fullscreen_sovianwinter_front:
    parallel:
        contains:
            "back/effects/explosion2.png"
            alpha 0 xalign 0.5 yalign 0.5 zoom 1.5 additive 0.5
            linear 0.2 alpha 0.6 rotate 72
            linear 0.5 alpha 0.3 rotate 180
            linear 0.5 alpha 0.6 rotate 360
            linear 0.5 alpha 0.3 rotate 540
            linear 0.5 alpha 0.6 rotate 720
            linear 0.2 alpha 0
        contains:
            "back/effects/storm_darkness.png"
            alpha 0
            linear 0.2 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.2 alpha 0
        contains:
            SnowBlossom("back/effects/snowflake.png", 200, 20, (-20, -800), (20, 600))
            zoom 0.5 alpha 0.3
            pause 2.0
            linear 1.0 alpha 0
        contains:
            SnowBlossom("back/effects/snowflake.png", 200, 20, (-20, -800), (20, 600))
            alpha 0.7
            pause 2.0
            linear 1.0 alpha 0
        contains:
            SnowBlossom("back/effects/snowflake.png", 200, 20, (-20, -800), (20, 600))
            zoom 2.0 alpha 0.5
            pause 2.0
            linear 1.0 alpha 0
        contains:
            SnowBlossom(anim.Filmstrip("battle/skills/dark_particles.png", (80, 80), (2, 1), .07, xalign=0.5, yalign=0.5), 120, 20, (-1000, -1100), (800, 900), 3)
            alpha 1.0
            pause 2.0
            linear 1.0 alpha 0
        contains:
            SnowBlossom(anim.Filmstrip("battle/skills/dark_particles.png", (80, 80), (2, 1), .07, xalign=0.5, yalign=0.5), 120, 20, (-1000, -1100), (800, 900), 3)
            zoom 1.5 alpha 0.8
            pause 2.0
            linear 1.0 alpha 0
image fullscreen_sovianwinter_back = "fullscreen_sovianwinter_front"
            
image fullscreen_katyusha_front:
    parallel:
        contains:
            "back/effects/storm_darkness.png"
            alpha 0
            linear 0.2 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.2 alpha 0
        contains:
            SnowBlossom("battle/skills/katyusha.png", 100, 50, (-4200), (3500))
            pause 2.0
            linear 1.0 alpha 0
image fullscreen_katyusha_back = "fullscreen_katyusha_front"
            
image fullscreen_fissure_front:
    parallel:
        contains:
            At("back/effects/storm_darkness.png", vpunch)
            pause 0.3
            At("back/effects/storm_darkness.png", hpunch)
            pause 0.3
            repeat
image fullscreen_fissure_back = "fullscreen_fissure_front"
            
image fullscreen_flamesofwar_front:
    parallel:
        contains:
            "back/effects/storm_darkness.png"
            alpha 0
            linear 0.2 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.2 alpha 0
        contains:
            anim.Filmstrip("battle/skills/fire.png", (234, 234), (2, 2), .07, xalign=0.5, yalign=0.5)
            xalign 0.24 yalign 0.65 alpha 1.0
            linear 0.2 xalign 0.23
            linear 0.2 xalign 0.25
            linear 0.2 xalign 0.23
            linear 0.2 xalign 0.25
            linear 0.2 xalign 0.23
            linear 0.2 xalign 0.25 alpha 0
        contains:
            anim.Filmstrip("battle/skills/fire.png", (234, 234), (2, 2), .07, xalign=0.5, yalign=0.5)
            xalign 0.24 yalign 0.65 alpha 0
            pause 0.8
            alpha 1.0
            linear 0.2 xalign 0.23
            linear 0.2 xalign 0.25
            linear 0.2 xalign 0.23
            linear 0.2 xalign 0.25
            linear 0.2 xalign 0.23
            linear 0.2 xalign 0.25 alpha 0
        contains:
            anim.Filmstrip("battle/skills/fire.png", (234, 234), (2, 2), .07, xalign=0.5, yalign=0.5)
            xalign 0.24 yalign 0.6 alpha 0
            pause 1.0
            alpha 1.0
            linear 0.2 xalign 0.23
            linear 0.2 xalign 0.25
            linear 0.2 xalign 0.23
            linear 0.2 xalign 0.25
            linear 0.2 xalign 0.23
            linear 0.2 xalign 0.25 alpha 0
        contains:
            anim.Filmstrip("battle/skills/fire.png", (234, 234), (2, 2), .07, xalign=0.5, yalign=0.5)
            xalign 0.24 yalign 0.55 alpha 0
            pause 1.2
            alpha 1.0
            linear 0.2 xalign 0.23
            linear 0.2 xalign 0.25
            linear 0.2 xalign 0.23
            linear 0.2 xalign 0.25
            linear 0.2 xalign 0.23
            linear 0.2 xalign 0.25 alpha 0
        contains:
            anim.Filmstrip("battle/skills/fire.png", (234, 234), (2, 2), .07, xalign=0.5, yalign=0.5)
            xalign 0.24 yalign 0.5 alpha 0
            pause 1.5
            alpha 1.0
            linear 0.2 xalign 0.23
            linear 0.2 xalign 0.25
            linear 0.2 xalign 0.23
            linear 0.2 xalign 0.25
            linear 0.2 xalign 0.23
            linear 0.2 xalign 0.25 alpha 0
        contains:
            "fire"
            alpha 0 xalign 0.5 yalign 0.5 zoom 1.1
            linear 0.2 alpha 0.6 zoom 1.0
            linear 0.5 alpha 0.3 zoom 1.1
            linear 0.5 alpha 0.6 zoom 1.0
            linear 0.5 alpha 0.3 zoom 1.1
            linear 0.5 alpha 0.6 zoom 1.0
            linear 0.2 alpha 0 zoom 1.1
            
image fullscreen_flamesofwar_back:
    parallel:
        contains:
            "back/effects/storm_darkness.png"
            alpha 0
            linear 0.2 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            linear 0.2 alpha 0
        contains:
            anim.Filmstrip("battle/skills/fire.png", (234, 234), (2, 2), .07, xalign=0.5, yalign=0.5)
            xalign 0.76 yalign 0.35 alpha 1.0
            linear 0.2 xalign 0.75
            linear 0.2 xalign 0.77
            linear 0.2 xalign 0.75
            linear 0.2 xalign 0.77
            linear 0.2 xalign 0.75
            linear 0.2 xalign 0.77 alpha 0
        contains:
            anim.Filmstrip("battle/skills/fire.png", (234, 234), (2, 2), .07, xalign=0.5, yalign=0.5)
            xalign 0.76 yalign 0.35 alpha 0
            pause 0.8
            alpha 1.0
            linear 0.2 xalign 0.75
            linear 0.2 xalign 0.77
            linear 0.2 xalign 0.75
            linear 0.2 xalign 0.77
            linear 0.2 xalign 0.75
            linear 0.2 xalign 0.77 alpha 0
        contains:
            anim.Filmstrip("battle/skills/fire.png", (234, 234), (2, 2), .07, xalign=0.5, yalign=0.5)
            xalign 0.76 yalign 0.3 alpha 0
            pause 1.0
            alpha 1.0
            linear 0.2 xalign 0.75
            linear 0.2 xalign 0.77
            linear 0.2 xalign 0.75
            linear 0.2 xalign 0.77
            linear 0.2 xalign 0.75
            linear 0.2 xalign 0.77 alpha 0
        contains:
            anim.Filmstrip("battle/skills/fire.png", (234, 234), (2, 2), .07, xalign=0.5, yalign=0.5)
            xalign 0.76 yalign 0.25 alpha 0
            pause 1.2
            alpha 1.0
            linear 0.2 xalign 0.75
            linear 0.2 xalign 0.77
            linear 0.2 xalign 0.75
            linear 0.2 xalign 0.77
            linear 0.2 xalign 0.75
            linear 0.2 xalign 0.77 alpha 0
        contains:
            anim.Filmstrip("battle/skills/fire.png", (234, 234), (2, 2), .07, xalign=0.5, yalign=0.5)
            xalign 0.76 yalign 0.2 alpha 0
            pause 1.5
            alpha 1.0
            linear 0.2 xalign 0.75
            linear 0.2 xalign 0.77
            linear 0.2 xalign 0.75
            linear 0.2 xalign 0.77
            linear 0.2 xalign 0.75
            linear 0.2 xalign 0.77 alpha 0
        contains:
            "fire"
            alpha 0 xalign 0.5 yalign 0.5 zoom 1.1
            linear 0.2 alpha 0.6 zoom 1.0
            linear 0.5 alpha 0.3 zoom 1.1
            linear 0.5 alpha 0.6 zoom 1.0
            linear 0.5 alpha 0.3 zoom 1.1
            linear 0.5 alpha 0.6 zoom 1.0
            linear 0.2 alpha 0 zoom 1.1
            
image fullscreen_purge_front:
    parallel:
        contains:
            At("back/effects/storm_darkness.png", vpunch)
            pause 0.3
            At("back/effects/storm_darkness.png", hpunch)
            pause 0.3
            repeat
        contains:
            "battle/skills/skull.png"
            xalign 0.15
            yalign 0.35
            zoom 1.0
            alpha 0
            linear 0.7 alpha 1.0 yalign 0.25
            linear 0.7 alpha 0 yalign 0.1
            repeat
        contains:
            "battle/skills/skull.png"
            xalign 0.65
            yalign 0.65
            zoom 1.0
            alpha 0
            linear 0.7 alpha 1.0 yalign 0.5
            linear 0.7 alpha 0 yalign 0.35
            repeat
        contains:
            "battle/skills/skull.png"
            xalign 0.35
            yalign 0.75
            zoom 0.8
            alpha 0
            linear 0.6 alpha 1.0 yalign 0.7
            linear 0.6 alpha 0 yalign 0.55
            repeat
        contains:
            "battle/skills/skull.png"
            xalign 0.85
            yalign 0.75
            zoom 0.8
            alpha 0
            linear 0.6 alpha 1.0 yalign 0.7
            linear 0.6 alpha 0 yalign 0.55
            repeat
        contains:
            "battle/skills/skull.png"
            xalign 0.45
            yalign 0.45
            zoom 0.3
            alpha 0
            linear 0.5 alpha 1.0 yalign 0.3
            linear 0.5 alpha 0 yalign 0.15
            repeat
        contains:
            "battle/skills/skull.png"
            xalign 0.75
            yalign 0.55
            zoom 0.3
            alpha 0
            linear 0.5 alpha 1.0 yalign 0.3
            linear 0.5 alpha 0 yalign 0.15
            repeat
        contains:
            "battle/skills/skull.png"
            xalign 0.53
            yalign 0.53
            zoom 0.4
            alpha 0
            linear 0.4 alpha 1.0 yalign 0.38
            linear 0.4 alpha 0 yalign 0.23
            repeat
        contains:
            "battle/skills/skull.png"
            xalign 0.57
            yalign 0.75
            zoom 0.65
            alpha 0.3
            linear 0.5 alpha 1.0 yalign 0.69
            linear 0.5 alpha 0 yalign 0.54
            repeat
        contains:
            "battle/skills/skull.png"
            xalign 0.93
            yalign 0.53
            zoom 0.4
            alpha 0
            linear 0.4 alpha 1.0 yalign 0.38
            linear 0.4 alpha 0 yalign 0.23
            repeat
        contains:
            "battle/skills/skull.png"
            xalign 0.1
            yalign 0.73
            zoom 0.4
            alpha 0
            linear 0.4 alpha 1.0 yalign 0.68
            linear 0.4 alpha 0 yalign 0.53
            repeat
image fullscreen_purge_back = "fullscreen_purge_front"



