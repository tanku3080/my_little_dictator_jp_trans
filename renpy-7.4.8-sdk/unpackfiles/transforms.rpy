
########################################################################################################################
#### TRANSFORMS #######################################################################################################
########################################################################################################################
init -2:
    transform flip_horizontal:
        xzoom -1
        
    transform rotater_anim:
        xpos 0.5
        ypos 0.5
        xanchor 0.5
        yanchor 0.5
        rotate 0
        linear 90.0 rotate 360
        repeat
        
    transform sidetoside_anim:
        xalign 0.5
        yalign 0.5
        xanchor 0.5
        yanchor 0.5
        rotate 0
        linear 1.0 rotate 10
        linear 1.0 rotate 0
        linear 1.0 rotate -10
        linear 1.0 rotate 0
        repeat
        
    transform questionbubble_anim:
        rotate 0
        linear 1.0 rotate 2
        linear 1.0 rotate 0
        linear 1.0 rotate -2
        linear 1.0 rotate 0
        repeat
        
    transform crown_anim:
        alpha 1.0
        pause 0.12
        alpha 0
        pause 0.12
        alpha 1.0
        pause 0.12
        alpha 0
        pause 0.12
        alpha 1.0
        pause 0.12
        alpha 0
        pause 0.12
        alpha 1.0
        pause 2.0
        alpha 0
        pause 1.0
        repeat
        
    transform titleback2:
        zoom 1.5 xpos 0 ypos 0 xanchor 0 yanchor 100 
        linear 8.0 xpos -453 ypos 0
        repeat      
        
    transform titleback3:
        zoom 1.5 xpos -453 ypos 0 xanchor 0 yanchor 100 
        linear 8.0 xpos 0 ypos 0
        repeat          
        
    transform rotater_anim2:
        xpos 0.5
        ypos 0.5
        xanchor 0.5
        yanchor 0.5
        rotate 0
        linear 3.0 rotate -360
        repeat          
        
    transform rotater_anim3:
        xpos 0.5
        ypos 0.5
        xanchor 0.5
        yanchor 0.5
        rotate 0
        linear 3.0 rotate 360
        repeat
        
    transform rotater_anim4:
        xpos 0.5
        ypos 0.5
        xanchor 0.5
        yanchor 0.5
        rotate 0
        linear 0.5 rotate -360
        repeat
        
    transform nav_eff:
        on idle:
            xalign 0.98
            yalign .5
        on selected_idle:
            xalign 0.98
            yalign .5
        on hover:
            easein 0.3 ypos 0.47
        on selected_hover:
            easein 0.3 ypos 0.47
            
    transform mapicon_eff:
        on idle:
            xalign 0.5
        on selected_idle:
            xalign 0.5
        on hover:
            xalign 0.5
        on selected_hover:
            xalign 0.5
            
    transform campaign_eff:
        on idle:
            alpha 0.8
            yalign .5
        on selected_idle:
            alpha 0.8
            yalign .5
        on hover:
            alpha 1.0
            easein 0.3 ypos 0.48
        on selected_hover:
            alpha 1.0
            easein 0.3 ypos 0.48
            
    transform campaign_characters_eff:
        xpos 0.2 alpha 0
        linear 0.3 xpos 0.0001 alpha 1.0
        
    transform planeleft_eff:
        yalign 0.7
        ypos 0.85
        xpos -0.4
        alpha 0
        0.8
        linear 0.5 xpos -0.57 ypos 0.66 alpha 0.9
        
    transform planeright_eff:
        yalign 0.7
        xpos 0.4
        ypos 0.85
        alpha 0
        0.8
        linear 0.5 xpos 0.57 ypos 0.65 alpha 0.9
        
    transform planeleft2_eff:
        yalign 0.7
        ypos 0.85
        xpos -0.4
        alpha 0
        0.8
        linear 0.5 xpos -0.8 ypos 0.7 alpha 0.9
        
    transform planeright2_eff:
        yalign 0.7
        xpos 0.4
        ypos 0.85
        alpha 0
        0.8
        linear 0.5 xpos 0.8 ypos 0.7 alpha 0.9
        
    transform planeleft3_eff:
        yalign 0.7
        ypos 0.85
        xpos -0.4
        alpha 0
        0.8
        linear 0.5 xpos -0.66 ypos 0.68 alpha 0.9
        
    transform planeright3_eff:
        yalign 0.7
        xpos 0.4
        ypos 0.85
        alpha 0
        0.8
        linear 0.5 xpos 0.66 ypos 0.68 alpha 0.9
        
    transform mmbuttons_eff:
        yalign 1.3
        0.12
        linear 0.5 yalign 1.0
        
    transform bonus_eff:
        on idle:
            ypos 0
        on selected_idle:
            ypos 0
        on hover:
            easein 0.3 ypos -.05
        on selected_hover:
            easein 0.3 ypos -.05
            
    transform map_eff:
        on idle:
            xalign 0.7
            yalign .2
        on selected_idle:
            xalign 0.7
            yalign .2
        on hover:
            easein 0.3 xpos 0.98
        on selected_hover:
            easein 0.3 xpos 0.98
            
    transform title_eff:
        ypos 1.5
        0.2
        linear 0.8 ypos -0.02
        
    transform mm_eff:
        yalign 1.5
        0.12
        linear 0.5 yalign 1.0
        
    transform titletankleft_eff:
        xzoom -1
        xalign 0.5
        ypos 1.4
        0.2
        linear 0.5 ypos 0.5
        linear 0.5 xalign 0.1
        
    transform titletankright_eff:
        xalign 0.5
        ypos 1.4
        0.2
        linear 0.5 ypos 0.5
        linear 0.5 xalign 0.9
        
    transform titleshipleft_eff:
        xalign 0.5
        ypos 1.2
        xpos 0.1
        alpha 0
        0.3
        linear 0.5 ypos 0.28 alpha 1.0
        linear 0.3 xpos -0.13
        
    transform titleshipright_eff:
        xalign 0.5
        xpos 0.9
        alpha 0
        ypos 1.2
        0.3
        linear 0.5 ypos 0.28 alpha 1.0
        linear 0.3 xpos 1.13
        
    transform vrocketleft_eff:
        xalign 0.5
        yalign 1.5
        0.6
        linear 0.5 yalign 0.45
        linear 0.5 xalign 0.07
        
    transform vrocketright_eff:
        xalign 0.5
        yalign 1.5
        0.6
        linear 0.5 yalign 0.45
        linear 0.5 xalign 0.93
        
    transform fire_eff:
        alpha 0
        linear 2.0 alpha 1.0
        
    transform gear_eff:
        yalign 1.3
        0.01
        linear 1.0 yalign 0.975
        
    transform logo_eff:
        xpos 0.5
        ypos 0.72
        xanchor 0.5
        yanchor 0.5
        linear 0.2 rotate 0 zoom 1.0
        linear 0.2 rotate -1 zoom 1.0025
        linear 0.2 rotate 0 zoom 1.005
        linear 0.2 rotate 1 zoom 1.0075
        linear 0.2 rotate 0 zoom 1.01
        linear 0.2 rotate -1 zoom 1.0075
        linear 0.2 rotate 0 zoom 1.005
        linear 0.2 rotate 1 zoom 1.0025
        linear 0.2 rotate 0 zoom 1.0
        linear 0.2 rotate -1 zoom 0.9975
        linear 0.2 rotate 0 zoom 0.995
        linear 0.2 rotate 1 zoom 0.9925
        linear 0.2 rotate 0 zoom 0.99
        linear 0.2 rotate -1 zoom 0.9925
        linear 0.2 rotate 0 zoom 0.995
        linear 0.2 rotate 1 zoom 0.9975
        repeat   
        
    transform blur(child):
        contains:
            child
            alpha 1.0
        contains:
            child
            alpha 0.15 xoffset -3
        contains:
            child
            alpha 0.15 xoffset 3
        contains:
            child
            alpha 0.15 yoffset -3
        contains:
            child
            alpha 0.15 yoffset 3
        contains:
            child
            alpha 0.15 xoffset -6
        contains:
            child
            alpha 0.15 xoffset 6
        contains:
            child
            alpha 0.15 yoffset -6
        contains:
            child
            alpha 0.15 yoffset 6
        contains:
            child
            alpha 0.15 xoffset -9
        contains:
            child
            alpha 0.15 xoffset 9
        contains:
            child
            alpha 0.15 yoffset -9
        contains:
            child
            alpha 0.15 yoffset 9
            
    transform logointro_eff:
        zoom 20
        alpha 0
        xpos 0.5
        ypos 0.72
        xanchor 0.5
        yanchor 0.5
        1.5
        alpha 1.0
        linear 0.5 zoom 1
        
    transform logoshadow_eff:
        zoom 0
        alpha 0
        xpos 0.5
        ypos 0.72
        xanchor 0.5
        yanchor 0.5
        1.4
        linear 0.5 zoom 1 alpha 1.0
        
    transform quick_eff:
        on idle:
            alpha 1.0
            ypos 0
        on selected_idle:
            alpha 1.5
            ypos 0
        on hover:
            alpha 1.5
            easein 0.2 ypos -0.03
        on selected_hover:
            alpha 1.5
            easein 0.2 ypos -0.03
            
    transform cod_eff:
        on idle:
            xalign 0.74
            yalign .82
        on selected_idle:
            xalign 0.74
            yalign .82
        on hover:
            easein 0.3 xpos .76
        on selected_hover:
            easein 0.3 xpos .76
            
    transform cod2_eff:
        on idle:
            xalign 0.74
            yalign .82
        on selected_idle:
            xalign 0.74
            yalign .82
        on hover:
            easein 0.3 ypos .87
        on selected_hover:
            easein 0.3 ypos .87  
            
    transform cod3_eff:
        on idle:
            xalign 0.74
            yalign .87
        on selected_idle:
            xalign 0.74
            yalign .87
        on hover:
            easein 0.3 ypos .82
        on selected_hover:
            easein 0.3 ypos .82 
           
    transform victoryscreen_slideinleft_hitora_eff:
        xpos 0.0001 alpha 0
        linear 0.3 xpos 1.05 alpha 1.0
        
    transform victoryscreen_slideinleft_churchill_eff:
        xpos 0.0001 ypos -0.03 alpha 0
        linear 0.3 xpos 0.5 alpha 1.0
        
    transform victoryscreen_slideinleft_rinni_eff:
        xpos 0.0001 ypos -0.04 alpha 0
        linear 0.3 xpos 0.5 alpha 1.0
    
    transform victoryscreen_slideinright_yamato_eff:
        xpos 0.0001 alpha 0
        linear 0.3 xpos -0.78 alpha 1.0
        
    transform victoryscreen_slideinright_cyrano_eff:
        xpos 0.0001 ypos -0.05 alpha 0
        linear 0.3 xpos -0.55 alpha 1.0
        
    transform victoryscreen_slideinright_starin_eff:
        xpos 0.0001 ypos -0.01 alpha 0
        linear 0.3 xpos -0.6 alpha 1.0
            
define battleopening  = CropMove(0.8, "custom", (0, 0.5, 1.0, 0), (0, 0.5), (0.0, 0.0, 1.0, 1.0), (0, 0))
define battleclose = CropMove(0.8, "custom", (0.0, 0.0, 1.0, 1.0), (0, 0), (0, 0.5, 1.0, 0), (0, 0.5), False)

