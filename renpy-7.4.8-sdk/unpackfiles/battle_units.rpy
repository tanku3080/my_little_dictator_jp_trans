################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
                                                                     #  UNITS  #
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
#
#
#
################################################################
################################################################
################################################################
    #  COMMANDERS  #
################################################################
################################################################
################################################################

################################
#commander_churchill
################################

image commander_churchill_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_churchill_walk.png", (0, 258, 708, 258)), (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_churchill_walk_front:
    Fixed(anim.Filmstrip("battle/units/commander_churchill_walk.png", (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_churchill_static_back:
    Fixed(im.Crop("battle/units/commander_churchill_walk.png", (0, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_churchill_static_front:
    Fixed(im.Crop("battle/units/commander_churchill_walk.png", (0, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_churchill_main1_attack_back:
    contains:
        "seal_light"
        xpos 330
        ypos 430
    contains:
        "offensive_prismblast_back"
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/commander_churchill_main1_attack.png", (0, 258, 1770, 258)), (177, 258), (10, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
    
image commander_churchill_main1_attack_front:
    contains:
        "seal_light"
        xpos 330
        ypos 430
    contains:
        "offensive_prismblast_front"
    contains:
        Fixed(anim.Filmstrip("battle/units/commander_churchill_main1_attack.png", (177, 258), (10, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_churchill_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_churchill_main1_attack.png", (1593, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
                                                                        
image commander_churchill_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_churchill_main1_attack.png", (1593, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)   
    
image commander_churchill_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/commander_churchill_main1_attack.png", (0, 258, 1770, 258)), (177, 258), (10, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)  

image commander_churchill_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/commander_churchill_main1_attack.png", (177, 258), (10, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:                                          
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0

image commander_churchill_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_churchill_main1_attack.png", (1593, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_churchill_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_churchill_main1_attack.png", (1593, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)   
    
image commander_churchill_special1_attack_back:
    contains:
        "seal_light"
        xpos 330
        ypos 430
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/commander_churchill_special1_attack.png", (0, 258, 2478, 258)), (177, 258), (14, 1), .07, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
    
image commander_churchill_special1_attack_front:
    contains:
        "seal_light"
        xpos 330
        ypos 430
    contains:
        Fixed(anim.Filmstrip("battle/units/commander_churchill_special1_attack.png", (177, 258), (14, 1), .07, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_churchill_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_churchill_special1_attack.png", (2301, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_churchill_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_churchill_special1_attack.png", (2301, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)  
    
image commander_churchill_special2_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_churchill_special2_attack.png", (0, 258, 2478, 258)), (177, 258), (14, 1), .07, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
    
image commander_churchill_special2_attack_front:
    Fixed(anim.Filmstrip("battle/units/commander_churchill_special2_attack.png", (177, 258), (14, 1), .07, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_churchill_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_churchill_special2_attack.png", (2301, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_churchill_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_churchill_special2_attack.png", (2301, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)  
    
image commander_churchill_special3_attack_back:
    contains:
        "seal_light"
        xpos 330
        ypos 430
    contains:
        "reaction_crusade"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/commander_churchill_main1_attack.png", (0, 258, 1770, 258)), (177, 258), (10, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
    
image commander_churchill_special3_attack_front:
    contains:
        "seal_light"
        xpos 330
        ypos 430
    contains:
        Fixed(anim.Filmstrip("battle/units/commander_churchill_main1_attack.png", (177, 258), (10, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_crusade"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    
image commander_churchill_special3_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_churchill_main1_attack.png", (1593, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
                                                                        
image commander_churchill_special3_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_churchill_main1_attack.png", (1593, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image commander_churchill_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_churchill_walk.png", (0, 258, 708, 258)), (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_xcharm", xsize=840, ysize=840)

image commander_churchill_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/commander_churchill_walk.png", (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_xcharm", xsize=840, ysize=840)
    
image commander_churchill_main1_powerup_finalframe_back:
    At(Fixed(im.Crop("battle/units/commander_churchill_walk.png", (0, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)

image commander_churchill_main1_powerup_finalframe_front:
    At(Fixed(im.Crop("battle/units/commander_churchill_walk.png", (0, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    
image commander_churchill_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_churchill_walk.png", (0, 258, 708, 258)), (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image commander_churchill_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/commander_churchill_walk.png", (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image commander_churchill_heal_finalframe_back:
    Fixed(im.Crop("battle/units/commander_churchill_walk.png", (0, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_churchill_heal_finalframe_front:
    Fixed(im.Crop("battle/units/commander_churchill_walk.png", (0, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#commander_cyrano
################################

image commander_cyrano_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_cyrano_walk.png", (0, 258, 708, 258)), (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_cyrano_walk_front:
    Fixed(anim.Filmstrip("battle/units/commander_cyrano_walk.png", (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_cyrano_static_back:
    Fixed(im.Crop("battle/units/commander_cyrano_walk.png", (0, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_cyrano_static_front:
    Fixed(im.Crop("battle/units/commander_cyrano_walk.png", (0, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_cyrano_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_cyrano_main1_attack.png", (0, 258, 2478, 258)), (177, 258), (14, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
    
image commander_cyrano_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/commander_cyrano_main1_attack.png", (177, 258), (14, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_cyrano_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_cyrano_main1_attack.png", (2301, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_cyrano_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_cyrano_main1_attack.png", (2301, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)   
    
image commander_cyrano_main2_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_cyrano_main2_attack.png", (0, 258, 1593, 258)), (177, 258), (9, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
    
image commander_cyrano_main2_attack_front:
    Fixed(anim.Filmstrip("battle/units/commander_cyrano_main2_attack.png", (177, 258), (9, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_cyrano_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_cyrano_main2_attack.png", (1416, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_cyrano_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_cyrano_main2_attack.png", (1416, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)   
    
image commander_cyrano_special1_attack_back:
    contains:
        "seal_fire"
        xpos 330
        ypos 430
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.45
        alpha 1.0
    contains:
        "offensive_fireball_back"
    contains:
        "offensive_fireblast_back"
        xpos 590
        ypos 270
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/commander_cyrano_special1_attack.png", (0, 258, 2478, 258)), (177, 258), (14, 1), .07, xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
    
image commander_cyrano_special1_attack_front:
    contains:
        "seal_fire"
        xpos 330
        ypos 430
    contains:
        Fixed(anim.Filmstrip("battle/units/commander_cyrano_special1_attack.png", (177, 258), (14, 1), .07, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_fire"
        xalign -0.73 yalign 0.7 alpha 0
        pause 0.45
        alpha 1.0
    contains:
        "offensive_fireball_front"
    contains:
        "offensive_fireblast_front"
        xpos 300
        ypos 350

image commander_cyrano_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_cyrano_special1_attack.png", (2301, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_cyrano_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_cyrano_special1_attack.png", (2301, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)  
    
image commander_cyrano_special2_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_cyrano_special2_attack.png", (0, 258, 2124, 258)), (177, 258), (12, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
    
image commander_cyrano_special2_attack_front:
    Fixed(anim.Filmstrip("battle/units/commander_cyrano_special2_attack.png", (177, 258), (12, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_cyrano_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_cyrano_special2_attack.png", (1947, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_cyrano_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_cyrano_special2_attack.png", (1947, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)   
 
image commander_cyrano_special3_attack_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_cyrano_walk.png", (0, 258, 708, 258)), (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)

image commander_cyrano_special3_attack_front:
    contains:
        At(Fixed(anim.Filmstrip("battle/units/commander_cyrano_walk.png", (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    
image commander_cyrano_special3_attack_finalframe_back:
    At(Fixed(im.Crop("battle/units/commander_cyrano_walk.png", (0, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    
image commander_cyrano_special3_attack_finalframe_front:
    At(Fixed(im.Crop("battle/units/commander_cyrano_walk.png", (0, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    
image commander_cyrano_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_cyrano_walk.png", (0, 258, 708, 258)), (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_xspeed", xsize=840, ysize=840)

image commander_cyrano_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/commander_cyrano_walk.png", (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_xspeed", xsize=840, ysize=840)
    
image commander_cyrano_main1_powerup_finalframe_back:
    At(Fixed(im.Crop("battle/units/commander_cyrano_walk.png", (0, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)

image commander_cyrano_main1_powerup_finalframe_front:
    At(Fixed(im.Crop("battle/units/commander_cyrano_walk.png", (0, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    
image commander_cyrano_main2_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_cyrano_walk.png", (0, 258, 708, 258)), (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_positivity", xsize=840, ysize=840)

image commander_cyrano_main2_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/commander_cyrano_walk.png", (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_positivity", xsize=840, ysize=840)
    
image commander_cyrano_main2_powerup_finalframe_back:
    At(Fixed(im.Crop("battle/units/commander_cyrano_walk.png", (0, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)

image commander_cyrano_main2_powerup_finalframe_front:
    At(Fixed(im.Crop("battle/units/commander_cyrano_walk.png", (0, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    
image commander_cyrano_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_cyrano_walk.png", (0, 258, 708, 258)), (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image commander_cyrano_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/commander_cyrano_walk.png", (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image commander_cyrano_heal_finalframe_back:
    Fixed(im.Crop("battle/units/commander_cyrano_walk.png", (0, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_cyrano_heal_finalframe_front:
    Fixed(im.Crop("battle/units/commander_cyrano_walk.png", (0, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#commander_guderian
################################

image commander_guderian_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_guderian_walk.png", (0, 260, 708, 260)), (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_guderian_walk_front:
    Fixed(anim.Filmstrip("battle/units/commander_guderian_walk.png", (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_guderian_static_back:
    Fixed(im.Crop("battle/units/commander_guderian_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_guderian_static_front:
    Fixed(im.Crop("battle/units/commander_guderian_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_guderian_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_guderian_main1_attack.png", (0, 260, 2655, 260)), (177, 260), (15, 1), .03, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
    
image commander_guderian_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/commander_guderian_main1_attack.png", (177, 260), (15, 1), .03, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_guderian_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_guderian_main1_attack.png", (2478, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_guderian_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_guderian_main1_attack.png", (2478, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)   
    
image commander_guderian_main2_attack_back:
    contains:
        "offensive_stielhandgranate_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/commander_guderian_walk.png", (0, 260, 708, 260)), (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_guderian_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/commander_guderian_walk.png", (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_stielhandgranate_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image commander_guderian_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_guderian_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_guderian_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_guderian_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_guderian_special1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_guderian_special1_attack.png", (0, 260, 1947, 260)), (177, 260), (11, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
    
image commander_guderian_special1_attack_front:
    Fixed(anim.Filmstrip("battle/units/commander_guderian_special1_attack.png", (177, 260), (11, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_guderian_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_guderian_special1_attack.png", (1770, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_guderian_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_guderian_special1_attack.png", (1770, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)   
    
image commander_guderian_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 310
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_guderian_walk.png", (0, 260, 708, 260)), (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_xspeed", xsize=840, ysize=840)

image commander_guderian_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/commander_guderian_walk.png", (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_xspeed", xsize=840, ysize=840)
    
image commander_guderian_main1_powerup_finalframe_back:
    At(Fixed(im.Crop("battle/units/commander_guderian_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)

image commander_guderian_main1_powerup_finalframe_front:
    At(Fixed(im.Crop("battle/units/commander_guderian_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    
image commander_guderian_heal_back:
    contains:
        "seal_heal"
        xpos 310
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_guderian_walk.png", (0, 260, 708, 260)), (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image commander_guderian_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/commander_guderian_walk.png", (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image commander_guderian_heal_finalframe_back:
    Fixed(im.Crop("battle/units/commander_guderian_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_guderian_heal_finalframe_front:
    Fixed(im.Crop("battle/units/commander_guderian_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
    
################################
#commander_hitora
################################

image commander_hitora_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_hitora_walk.png", (0, 260, 708, 260)), (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_hitora_walk_front:
    Fixed(anim.Filmstrip("battle/units/commander_hitora_walk.png", (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_hitora_static_back:
    Fixed(im.Crop("battle/units/commander_hitora_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_hitora_static_front:
    Fixed(im.Crop("battle/units/commander_hitora_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_hitora_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_hitora_main1_attack.png", (0, 260, 2832, 260)), (177, 260), (16, 1), .03, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
    
image commander_hitora_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/commander_hitora_main1_attack.png", (177, 260), (16, 1), .03, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_hitora_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_hitora_main1_attack.png", (2655, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_hitora_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_hitora_main1_attack.png", (2655, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)   
    
image commander_hitora_main2_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_hitora_main2_attack.png", (0, 260, 1947, 260)), (177, 260), (11, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_hitora_main2_attack_front:
    Fixed(anim.Filmstrip("battle/units/commander_hitora_main2_attack.png", (177, 260), (11, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_hitora_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_hitora_main2_attack.png", (1770, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_hitora_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_hitora_main2_attack.png", (1770, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_hitora_special1_attack_back:
    parallel:
        contains:
            Fixed(im.Crop("battle/units/commander_hitora_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        contains:
            Fixed(im.Crop(At("battle/units/commander_hitora_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), phasein), xsize=840, ysize=840)
    
image commander_hitora_special1_attack_front:
    parallel:
        contains:
            Fixed(im.Crop("battle/units/commander_hitora_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        contains:
            Fixed(At(im.Crop("battle/units/commander_hitora_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), phasein), xsize=840, ysize=840)

image commander_hitora_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_hitora_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_hitora_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_hitora_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_hitora_special2_attack_back:
    parallel:
        contains:
            Fixed(anim.Filmstrip(im.Crop("battle/units/commander_hitora_special1_attack.png", (0, 260, 1947, 260)), (177, 260), (8, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        contains:
            Fixed(anim.Filmstrip(im.Crop("battle/units/commander_hitora_special2_attack.png", (0, 260, 1947, 260)), (177, 260), (8, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
            alpha 0
            linear 0.3 alpha 1.0
            pause 0.3
            linear 0.3 alpha 0
            repeat
        linear 0.4 xalign 0 yalign 0.1
        alignaround (0.01, 0.03)
        linear 1.8 xalign 0 yalign 0.08 counterclockwise circles 2
        pause 0.2
        linear 0.4 yalign 0.001
    
image commander_hitora_special2_attack_front:
    parallel:
        contains:
            Fixed(anim.Filmstrip("battle/units/commander_hitora_special1_attack.png", (177, 260), (8, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        contains:
            Fixed(anim.Filmstrip("battle/units/commander_hitora_special2_attack.png", (177, 260), (8, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
            alpha 0
            linear 0.3 alpha 1.0
            pause 0.3
            linear 0.3 alpha 0
            repeat
        linear 0.4 xalign 0 yalign 0.1
        alignaround (0.01, 0.03)
        linear 1.8 xalign 0 yalign 0.08 counterclockwise circles 2
        pause 0.2
        linear 0.4 yalign 0.001

image commander_hitora_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_hitora_special1_attack.png", (1770, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_hitora_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_hitora_special1_attack.png", (1770, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_hitora_special3_attack_back:
    contains:
        "seal_red"
        xpos 330
        ypos 450
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/commander_hitora_special1_attack.png", (0, 260, 1947, 260)), (177, 260), (8, 1), .08, loop=True, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/commander_hitora_special3_attack.png", (0, 260, 1947, 260)), (177, 260), (8, 1), .08, loop=True, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        alpha 0
        linear 0.3 alpha 1.0
        pause 0.3
        linear 0.3 alpha 0
        repeat
    
image commander_hitora_special3_attack_front:
    contains:
        "seal_red"
        xpos 330
        ypos 450
    contains:
        Fixed(anim.Filmstrip("battle/units/commander_hitora_special1_attack.png", (177, 260), (8, 1), .08, loop=True, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        Fixed(anim.Filmstrip("battle/units/commander_hitora_special3_attack.png", (177, 260), (8, 1), .08, loop=True, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        alpha 0
        linear 0.3 alpha 1.0
        pause 0.3
        linear 0.3 alpha 0
        repeat

image commander_hitora_special3_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_hitora_special1_attack.png", (1770, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_hitora_special3_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_hitora_special1_attack.png", (1770, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_hitora_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 450
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_hitora_walk.png", (0, 260, 708, 260)), (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_xarmor", xsize=840, ysize=840)

image commander_hitora_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 450
    contains:
        At(Fixed(anim.Filmstrip("battle/units/commander_hitora_walk.png", (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_xarmor", xsize=840, ysize=840)
    
image commander_hitora_main1_powerup_finalframe_back:
    At(Fixed(im.Crop("battle/units/commander_hitora_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)

image commander_hitora_main1_powerup_finalframe_front:
    At(Fixed(im.Crop("battle/units/commander_hitora_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    
image commander_hitora_main2_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 450
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_hitora_walk.png", (0, 260, 708, 260)), (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_blitz", xsize=840, ysize=840)

image commander_hitora_main2_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 450
    contains:
        At(Fixed(anim.Filmstrip("battle/units/commander_hitora_walk.png", (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_blitz", xsize=840, ysize=840)
    
image commander_hitora_main2_powerup_finalframe_back:
    At(Fixed(im.Crop("battle/units/commander_hitora_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)

image commander_hitora_main2_powerup_finalframe_front:
    At(Fixed(im.Crop("battle/units/commander_hitora_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    
image commander_hitora_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 450
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_hitora_walk.png", (0, 260, 708, 260)), (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image commander_hitora_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 450
    contains:
        At(Fixed(anim.Filmstrip("battle/units/commander_hitora_walk.png", (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image commander_hitora_heal_finalframe_back:
    Fixed(im.Crop("battle/units/commander_hitora_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_hitora_heal_finalframe_front:
    Fixed(im.Crop("battle/units/commander_hitora_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
    
################################
#commander_nyan
################################
    
image commander_nyan_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_nyan_walk.png", (0, 258, 708, 258)), (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_nyan_walk_front:
    Fixed(anim.Filmstrip("battle/units/commander_nyan_walk.png", (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_nyan_static_back:
    Fixed(im.Crop("battle/units/commander_nyan_walk.png", (0, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_nyan_static_front:
    Fixed(im.Crop("battle/units/commander_nyan_walk.png", (0, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_nyan_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_nyan_main1_attack.png", (0, 258, 4071, 258)), (177, 258), (23, 1), .04, xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
    
image commander_nyan_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/commander_nyan_main1_attack.png", (177, 258), (23, 1), .04, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_nyan_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_nyan_main1_attack.png", (3894, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_nyan_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_nyan_main1_attack.png", (3894, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)   
    
image commander_nyan_main2_attack_back:
    contains:
        "offensive_stielhandgranate_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/commander_nyan_main2_attack.png", (0, 258, 1770, 258)), (177, 258), (10, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)  

image commander_nyan_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/commander_nyan_main2_attack.png", (177, 258), (10, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:                                          
        "offensive_stielhandgranate_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0

image commander_nyan_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_nyan_main2_attack.png", (1593, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_nyan_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_nyan_main2_attack.png", (1593, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)   
    
image commander_nyan_special1_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/commander_nyan_special1_attack.png", (0, 258, 2301, 258)), (177, 258), (13, 1), .04, xalign=0.5, yalign=0.5), shake), xsize=840, ysize=840)
    
image commander_nyan_special1_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/commander_nyan_special1_attack.png", (177, 258), (13, 1), .04, xalign=0.5, yalign=0.5), shake), xsize=840, ysize=840)

image commander_nyan_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_nyan_special1_attack.png", (2124, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_nyan_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_nyan_special1_attack.png", (2124, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)   
    
image commander_nyan_special2_attack_back:
    contains:
        "seal_fire"
        xpos 331
        ypos 440
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/commander_nyan_main2_attack.png", (0, 258, 1770, 258)), (177, 258), (10, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
    
image commander_nyan_special2_attack_front:
    contains:
        "seal_fire"
        xpos 331
        ypos 440
    contains:
        Fixed(anim.Filmstrip("battle/units/commander_nyan_main2_attack.png", (177, 258), (10, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_nyan_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_nyan_main2_attack.png", (1593, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_nyan_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_nyan_main2_attack.png", (1593, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_nyan_special3_attack_back:
    contains:
        "seal_fire"
        xpos 331
        ypos 440
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/commander_nyan_main2_attack.png", (0, 258, 1770, 258)), (177, 258), (10, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
    
image commander_nyan_special3_attack_front:
    contains:
        "seal_fire"
        xpos 331
        ypos 440
    contains:
        Fixed(anim.Filmstrip("battle/units/commander_nyan_main2_attack.png", (177, 258), (10, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_nyan_special3_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_nyan_main2_attack.png", (1593, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_nyan_special3_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_nyan_main2_attack.png", (1593, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_nyan_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 331
        ypos 440
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_nyan_walk.png", (0, 258, 708, 258)), (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_xpower", xsize=840, ysize=840)

image commander_nyan_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 331
        ypos 440
    contains:
        At(Fixed(anim.Filmstrip("battle/units/commander_nyan_walk.png", (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_xpower", xsize=840, ysize=840)
    
image commander_nyan_main1_powerup_finalframe_back:
    At(Fixed(im.Crop("battle/units/commander_nyan_walk.png", (0, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)

image commander_nyan_main1_powerup_finalframe_front:
    At(Fixed(im.Crop("battle/units/commander_nyan_walk.png", (0, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    
image commander_nyan_heal_back:
    contains:
        "seal_heal"
        xpos 331
        ypos 440
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_nyan_walk.png", (0, 258, 708, 258)), (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image commander_nyan_heal_front:
    contains:
        "seal_heal"
        xpos 331
        ypos 440
    contains:
        At(Fixed(anim.Filmstrip("battle/units/commander_nyan_walk.png", (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image commander_nyan_heal_finalframe_back:
    Fixed(im.Crop("battle/units/commander_nyan_walk.png", (0, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_nyan_heal_finalframe_front:
    Fixed(im.Crop("battle/units/commander_nyan_walk.png", (0, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#commander_monty
################################

image commander_monty_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_monty_walk.png", (0, 260, 708, 260)), (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_monty_walk_front:
    Fixed(anim.Filmstrip("battle/units/commander_monty_walk.png", (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_monty_static_back:
    Fixed(im.Crop("battle/units/commander_monty_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_monty_static_front:
    Fixed(im.Crop("battle/units/commander_monty_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_monty_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_monty_main1_attack.png", (0, 260, 1239, 260)), (177, 260), (7, 1), .04, xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
    
image commander_monty_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/commander_monty_main1_attack.png", (177, 260), (7, 1), .04, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_monty_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_monty_main1_attack.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_monty_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_monty_main1_attack.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)   
    
image commander_monty_main2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/commander_monty_main2_attack.png", (0, 260, 1593, 260)), (177, 260), (9, 1), .04, xalign=0.5, yalign=0.5), shake), xsize=840, ysize=840)    
    
image commander_monty_main2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/commander_monty_main2_attack.png", (177, 260), (9, 1), .04, xalign=0.5, yalign=0.5), shake), xsize=840, ysize=840)

image commander_monty_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_monty_main2_attack.png", (1416, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_monty_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_monty_main2_attack.png", (1416, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)   
    
image commander_monty_special1_attack_back:
    contains:
        "seal_electric"
        xpos 330
        ypos 430
    contains:
        "reaction_lightning"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.45
        alpha 1.0
    contains:
        "offensive_lightning_back"
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/commander_monty_special1_attack.png", (0, 260, 2301, 260)), (177, 260), (13, 1), .04, xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image commander_monty_special1_attack_front:
    contains:
        "seal_electric"
        xpos 340
        ypos 440
    contains:
        Fixed(anim.Filmstrip("battle/units/commander_monty_special1_attack.png", (177, 260), (13, 1), .04, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_lightning"
        xpos -0.7 ypos 0.2 alpha 0
        pause 0.45
        alpha 1.0
    contains:
        "offensive_lightning_front"

image commander_monty_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_monty_special1_attack.png", (2124, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_monty_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_monty_special1_attack.png", (2124, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)   
    
image commander_monty_special2_attack_back:
    contains:
        "offensive_lightningball_back"
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/commander_monty_special2_attack.png", (0, 260, 2124, 260)), (177, 260), (12, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
    
image commander_monty_special2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/commander_monty_special2_attack.png", (177, 260), (12, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_lightningball_front"

image commander_monty_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_monty_special2_attack.png", (1947, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_monty_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_monty_special2_attack.png", (1947, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)   
    
image commander_monty_special3_attack_back:
    At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_monty_walk.png", (0, 260, 708, 260)), (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)

image commander_monty_special3_attack_front:
    At(Fixed(anim.Filmstrip("battle/units/commander_monty_walk.png", (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    
image commander_monty_special3_attack_finalframe_back:
    At(Fixed(im.Crop("battle/units/commander_monty_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)

image commander_monty_special3_attack_finalframe_front:
    At(Fixed(im.Crop("battle/units/commander_monty_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    
image commander_monty_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 345
        ypos 450
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_monty_walk.png", (0, 260, 708, 260)), (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_xarmor", xsize=840, ysize=840)

image commander_monty_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 345
        ypos 450
    contains:
        At(Fixed(anim.Filmstrip("battle/units/commander_monty_walk.png", (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_xarmor", xsize=840, ysize=840)
    
image commander_monty_main1_powerup_finalframe_back:
    At(Fixed(im.Crop("battle/units/commander_monty_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)

image commander_monty_main1_powerup_finalframe_front:
    At(Fixed(im.Crop("battle/units/commander_monty_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    
image commander_monty_heal_back:
    contains:
        "seal_heal"
        xpos 345
        ypos 450
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_monty_walk.png", (0, 260, 708, 260)), (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image commander_monty_heal_front:
    contains:
        "seal_heal"
        xpos 345
        ypos 450
    contains:
        At(Fixed(anim.Filmstrip("battle/units/commander_monty_walk.png", (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image commander_monty_heal_finalframe_back:
    Fixed(im.Crop("battle/units/commander_monty_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_monty_heal_finalframe_front:
    Fixed(im.Crop("battle/units/commander_monty_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#commander_negahitora
################################

image commander_negahitora_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_negahitora_walk.png", (0, 260, 708, 260)), (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_negahitora_walk_front:
    Fixed(anim.Filmstrip("battle/units/commander_negahitora_walk.png", (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_negahitora_static_back:
    Fixed(im.Crop("battle/units/commander_negahitora_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_negahitora_static_front:
    Fixed(im.Crop("battle/units/commander_negahitora_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_negahitora_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_negahitora_main1_attack.png", (0, 260, 2832, 260)), (177, 260), (16, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
    
image commander_negahitora_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/commander_negahitora_main1_attack.png", (177, 260), (16, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_negahitora_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_negahitora_main1_attack.png", (2655, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_negahitora_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_negahitora_main1_attack.png", (2655, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)   
    
image commander_negahitora_main2_attack_back:
    contains:
        "offensive_stielhandgranate_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/commander_negahitora_walk.png", (0, 260, 708, 260)), (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_negahitora_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/commander_negahitora_walk.png", (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_stielhandgranate_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image commander_negahitora_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_negahitora_walk.png", (0, 260, 179, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_negahitora_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_negahitora_walk.png", (0, 0, 179, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_negahitora_special1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_negahitora_special1_attack.png", (0, 260, 1947, 260)), (177, 260), (11, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_negahitora_special1_attack_front:
    Fixed(anim.Filmstrip("battle/units/commander_negahitora_special1_attack.png", (177, 260), (11, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_negahitora_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_negahitora_special1_attack.png", (1770, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_negahitora_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_negahitora_special1_attack.png", (1770, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_negahitora_special2_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_negahitora_special1_attack.png", (0, 260, 1947, 260)), (177, 260), (11, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_negahitora_special2_attack_front:
    Fixed(anim.Filmstrip("battle/units/commander_negahitora_special1_attack.png", (177, 260), (11, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_negahitora_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_negahitora_special1_attack.png", (1770, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_negahitora_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_negahitora_special1_attack.png", (1770, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_negahitora_special3_attack_back:
    parallel:
        contains:
            Fixed(im.Crop(At("battle/units/commander_negahitora_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), shake), xsize=840, ysize=840)
        contains:
            Fixed(im.Crop(At("battle/units/commander_negahitora_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), phaseout), xsize=840, ysize=840)
    
image commander_negahitora_special3_attack_front:
    parallel:
        contains:
            Fixed(At(im.Crop("battle/units/commander_negahitora_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), shake), xsize=840, ysize=840)
        contains:
            Fixed(At(im.Crop("battle/units/commander_negahitora_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), phaseout), xsize=840, ysize=840)

image commander_negahitora_special3_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_negahitora_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_negahitora_special3_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_negahitora_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_negahitora_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_negahitora_walk.png", (0, 260, 708, 260)), (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_xpower", xsize=840, ysize=840)

image commander_negahitora_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/commander_negahitora_walk.png", (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_xpower", xsize=840, ysize=840)
    
image commander_negahitora_main1_powerup_finalframe_back:
    At(Fixed(im.Crop("battle/units/commander_negahitora_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)

image commander_negahitora_main1_powerup_finalframe_front:
    At(Fixed(im.Crop("battle/units/commander_negahitora_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    
image commander_negahitora_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_negahitora_walk.png", (0, 260, 708, 260)), (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image commander_negahitora_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/commander_negahitora_walk.png", (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image commander_negahitora_heal_finalframe_back:
    Fixed(im.Crop("battle/units/commander_negahitora_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_negahitora_heal_finalframe_front:
    Fixed(im.Crop("battle/units/commander_negahitora_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#commander_rinni
################################

image commander_rinni_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_rinni_walk.png", (0, 260, 708, 260)), (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_rinni_walk_front:
    Fixed(anim.Filmstrip("battle/units/commander_rinni_walk.png", (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_rinni_static_back:
    Fixed(im.Crop("battle/units/commander_rinni_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_rinni_static_front:
    Fixed(im.Crop("battle/units/commander_rinni_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_rinni_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_rinni_main1_attack.png", (0, 260, 2478, 260)), (177, 260), (14, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
    
image commander_rinni_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/commander_rinni_main1_attack.png", (177, 260), (14, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_rinni_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_rinni_main1_attack.png", (2301, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_rinni_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_rinni_main1_attack.png", (2301, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)   
    
image commander_rinni_main2_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_rinni_main2_attack.png", (0, 260, 1416, 260)), (177, 260), (8, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
    
image commander_rinni_main2_attack_front:
    Fixed(anim.Filmstrip("battle/units/commander_rinni_main2_attack.png", (177, 260), (8, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_rinni_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_rinni_main2_attack.png", (1239, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_rinni_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_rinni_main2_attack.png", (1239, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_rinni_special1_attack_back:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/commander_rinni_special1_attack.png", (0, 260, 1239, 260)), (177, 260), (7, 1), .07, loop=True, xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
    contains:
        "reaction_ground"
        xalign 0.73 yalign 0.08
    
image commander_rinni_special1_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/commander_rinni_special1_attack.png", (177, 260), (7, 1), .07, loop=True, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_ground"
        xalign -0.37 yalign 0.71

image commander_rinni_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_rinni_special1_attack.png", (1062, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_rinni_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_rinni_special1_attack.png", (1062, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_rinni_special2_attack_back:
    contains:
        "offensive_bolognese_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/commander_rinni_walk.png", (0, 260, 708, 260)), (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_rinni_special2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/commander_rinni_walk.png", (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_bolognese_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image commander_rinni_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_rinni_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_rinni_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_rinni_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_rinni_special3_attack_back:
    parallel:
        contains:
            Fixed(anim.Filmstrip(im.Crop("battle/units/commander_rinni_main2_attack.png", (0, 260, 1416, 260)), (177, 260), (6, 1), .07, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
        contains:
            Fixed(anim.Filmstrip(im.Crop("battle/units/commander_rinni_special3_attack.png", (0, 260, 1416, 260)), (177, 260), (6, 1), .07, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
            alpha 0
            linear 0.5 alpha 1.0
            linear 0.5 alpha 0
            repeat
        linear 0.4 yalign 0.08
        linear 0.4 yalign 0.06
        linear 0.4 yalign 0.08
        linear 0.4 yalign 0.06
        linear 0.4 yalign 0.001
    
image commander_rinni_special3_attack_front:
    parallel:
        contains:
            Fixed(anim.Filmstrip("battle/units/commander_rinni_main2_attack.png", (177, 260), (6, 1), .07, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        contains:
            Fixed(anim.Filmstrip("battle/units/commander_rinni_special3_attack.png", (177, 260), (6, 1), .07, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
            alpha 0
            linear 0.5 alpha 1.0
            linear 0.5 alpha 0
            repeat
        linear 0.4 yalign 0.08
        linear 0.4 yalign 0.06
        linear 0.4 yalign 0.08
        linear 0.4 yalign 0.06
        linear 0.4 yalign 0.001

image commander_rinni_special3_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_rinni_main2_attack.png", (1239, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_rinni_special3_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_rinni_main2_attack.png", (1239, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_rinni_main2_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_rinni_walk.png", (0, 260, 708, 260)), (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_positivity", xsize=840, ysize=840)

image commander_rinni_main2_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/commander_rinni_walk.png", (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_positivity", xsize=840, ysize=840)
    
image commander_rinni_main2_powerup_finalframe_back:
    At(Fixed(im.Crop("battle/units/commander_rinni_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)

image commander_rinni_main2_powerup_finalframe_front:
    At(Fixed(im.Crop("battle/units/commander_rinni_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    
image commander_rinni_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_rinni_walk.png", (0, 260, 708, 260)), (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image commander_rinni_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/commander_rinni_walk.png", (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image commander_rinni_heal_finalframe_back:
    Fixed(im.Crop("battle/units/commander_rinni_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_rinni_heal_finalframe_front:
    Fixed(im.Crop("battle/units/commander_rinni_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#commander_roijean
################################

image commander_roijean_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_roijean_walk.png", (0, 258, 708, 258)), (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_roijean_walk_front:
    Fixed(anim.Filmstrip("battle/units/commander_roijean_walk.png", (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_roijean_static_back:
    Fixed(im.Crop("battle/units/commander_roijean_walk.png", (0, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_roijean_static_front:
    Fixed(im.Crop("battle/units/commander_roijean_walk.png", (0, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_roijean_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_roijean_main1_attack.png", (0, 258, 2478, 258)), (177, 258), (14, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
    
image commander_roijean_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/commander_roijean_main1_attack.png", (177, 258), (14, 1), .04, loop=False, xalign=0.51, yalign=0.5), xsize=840, ysize=840)

image commander_roijean_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_roijean_main1_attack.png", (2301, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_roijean_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_roijean_main1_attack.png", (2301, 0, 177, 258), xalign=0.51, yalign=0.5), xsize=840, ysize=840)   
    
image commander_roijean_main2_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_roijean_main2_attack.png", (0, 258, 1416, 258)), (177, 258), (8, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
    
image commander_roijean_main2_attack_front:
    Fixed(anim.Filmstrip("battle/units/commander_roijean_main2_attack.png", (177, 258), (8, 1), .04, loop=False, xalign=0.51, yalign=0.5), xsize=840, ysize=840)

image commander_roijean_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_roijean_main2_attack.png", (1239, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_roijean_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_roijean_main2_attack.png", (1239, 0, 177, 258), xalign=0.51, yalign=0.5), xsize=840, ysize=840)   
    
image commander_roijean_special1_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/commander_roijean_special1_attack.png", (0, 258, 2124, 258)), (177, 258), (12, 1), .07, xalign=0.5, yalign=0.5), shake), xsize=840, ysize=840)    

image commander_roijean_special1_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/commander_roijean_special1_attack.png", (177, 258), (12, 1), .07, xalign=0.5, yalign=0.5), shake), xsize=840, ysize=840)

image commander_roijean_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_roijean_special1_attack.png", (1947, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_roijean_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_roijean_special1_attack.png", (1947, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)  
    
image commander_roijean_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 320
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_roijean_walk.png", (0, 258, 708, 258)), (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_xaccuracy", xsize=840, ysize=840)

image commander_roijean_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 320
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/commander_roijean_walk.png", (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_xaccuracy", xsize=840, ysize=840)
    
image commander_roijean_main1_powerup_finalframe_back:
    At(Fixed(im.Crop("battle/units/commander_roijean_walk.png", (0, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)

image commander_roijean_main1_powerup_finalframe_front:
    At(Fixed(im.Crop("battle/units/commander_roijean_walk.png", (0, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    
image commander_roijean_special2_attack_back:
    contains:
        "offensive_baguette_back"
    contains:
        "reaction_hit"
        xalign 0.69 yalign 0.08 alpha 0 xzoom -1
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/commander_roijean_walk.png", (0, 258, 708, 258)), (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_roijean_special2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/commander_roijean_walk.png", (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_baguette_front"
    contains:
        "reaction_hit"
        xalign -0.28 yalign 0.67 alpha 0
        pause 0.75
        alpha 1.0
    
image commander_roijean_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_roijean_walk.png", (0, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_roijean_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_roijean_walk.png", (0, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_roijean_special3_attack_back:
    contains:
        "seal_powerup"
        xpos 320
        ypos 430
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/commander_roijean_walk.png", (0, 258, 708, 258)), (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_roijean_walk.png", (0, 258, 708, 258)), (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
        alpha 0
        linear 0.5 alpha 1.0
        linear 0.5 alpha 0
        repeat

image commander_roijean_special3_attack_front:
    contains:
        "seal_powerup"
        xpos 320
        ypos 430
    contains:
        Fixed(anim.Filmstrip("battle/units/commander_roijean_walk.png", (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        At(Fixed(anim.Filmstrip("battle/units/commander_roijean_walk.png", (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
        alpha 0
        linear 0.5 alpha 1.0
        linear 0.5 alpha 0
        repeat
    
image commander_roijean_special3_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_roijean_walk.png", (0, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_roijean_special3_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_roijean_walk.png", (0, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_roijean_heal_back:
    contains:
        "seal_heal"
        xpos 320
        ypos 440
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_roijean_walk.png", (0, 258, 708, 258)), (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image commander_roijean_heal_front:
    contains:
        "seal_heal"
        xpos 320
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/commander_roijean_walk.png", (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image commander_roijean_heal_finalframe_back:
    Fixed(im.Crop("battle/units/commander_roijean_walk.png", (0, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_roijean_heal_finalframe_front:
    Fixed(im.Crop("battle/units/commander_roijean_walk.png", (0, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#commander_rommel
################################

image commander_rommel_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_rommel_walk.png", (0, 260, 708, 260)), (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_rommel_walk_front:
    Fixed(anim.Filmstrip("battle/units/commander_rommel_walk.png", (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_rommel_static_back:
    Fixed(im.Crop("battle/units/commander_rommel_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_rommel_static_front:
    Fixed(im.Crop("battle/units/commander_rommel_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_rommel_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_rommel_main1_attack.png", (0, 260, 2655, 260)), (177, 260), (15, 1), .04, xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
    
image commander_rommel_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/commander_rommel_main1_attack.png", (177, 260), (15, 1), .04, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_rommel_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_rommel_main1_attack.png", (2478, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_rommel_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_rommel_main1_attack.png", (2478, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)   
    
image commander_rommel_main2_attack_back:
    contains:
        "offensive_stielhandgranate_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/commander_rommel_walk.png", (0, 260, 708, 260)), (177, 260), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_rommel_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/commander_rommel_walk.png", (177, 260), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_stielhandgranate_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image commander_rommel_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_rommel_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_rommel_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_rommel_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_rommel_special1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_rommel_special1_attack.png", (0, 260, 1947, 260)), (177, 260), (11, 1), .04, xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
    
image commander_rommel_special1_attack_front:
    Fixed(anim.Filmstrip("battle/units/commander_rommel_special1_attack.png", (177, 260), (11, 1), .04, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_rommel_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_rommel_special1_attack.png", (1770, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_rommel_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_rommel_special1_attack.png", (1770, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)   
    
image commander_rommel_special2_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_rommel_special2_attack.png", (0, 260, 1416, 260)), (177, 260), (8, 1), .04, xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
    
image commander_rommel_special2_attack_front:
    Fixed(anim.Filmstrip("battle/units/commander_rommel_special2_attack.png", (177, 260), (8, 1), .04, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_rommel_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_rommel_special2_attack.png", (1239, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_rommel_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_rommel_special2_attack.png", (1239, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)   
    
image commander_rommel_special3_attack_back:
    contains:
        "seal_powerup"
        xpos 310
        ypos 430
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/commander_rommel_special3_attack.png", (0, 260, 2124, 260)), (177, 260), (12, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_rommel_special3_attack.png", (0, 260, 2124, 260)), (177, 260), (12, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
        alpha 0
        linear 0.5 alpha 1.0
        linear 0.5 alpha 0
        repeat
    
image commander_rommel_special3_attack_front:
    contains:
        "seal_powerup"
        xpos 310
        ypos 430
    contains:
        Fixed(anim.Filmstrip("battle/units/commander_rommel_special3_attack.png", (177, 260), (12, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        At(Fixed(anim.Filmstrip("battle/units/commander_rommel_special3_attack.png", (177, 260), (12, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
        alpha 0
        linear 0.5 alpha 1.0
        linear 0.5 alpha 0
        repeat

image commander_rommel_special3_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_rommel_special3_attack.png", (1947, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_rommel_special3_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_rommel_special3_attack.png", (1947, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_rommel_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 310
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_rommel_walk.png", (0, 260, 708, 260)), (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_xspeed", xsize=840, ysize=840)

image commander_rommel_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 310
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/commander_rommel_walk.png", (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_xspeed", xsize=840, ysize=840)
    
image commander_rommel_main1_powerup_finalframe_back:
    At(Fixed(im.Crop("battle/units/commander_rommel_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)

image commander_rommel_main1_powerup_finalframe_front:
    At(Fixed(im.Crop("battle/units/commander_rommel_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    
image commander_rommel_main2_powerup_back:
    contains:
        "seal_powerup"
        xpos 310
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_rommel_walk.png", (0, 260, 708, 260)), (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_positivity", xsize=840, ysize=840)

image commander_rommel_main2_powerup_front:
    contains:
        "seal_powerup"
        xpos 310
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/commander_rommel_walk.png", (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_positivity", xsize=840, ysize=840)
    
image commander_rommel_main2_powerup_finalframe_back:
    At(Fixed(im.Crop("battle/units/commander_rommel_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)

image commander_rommel_main2_powerup_finalframe_front:
    At(Fixed(im.Crop("battle/units/commander_rommel_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    
image commander_rommel_heal_back:
    contains:
        "seal_heal"
        xpos 315
        ypos 440
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_rommel_walk.png", (0, 260, 708, 260)), (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image commander_rommel_heal_front:
    contains:
        "seal_heal"
        xpos 315
        ypos 440
    contains:
        At(Fixed(anim.Filmstrip("battle/units/commander_rommel_walk.png", (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image commander_rommel_heal_finalframe_back:
    Fixed(im.Crop("battle/units/commander_rommel_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_rommel_heal_finalframe_front:
    Fixed(im.Crop("battle/units/commander_rommel_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#commander_starin
################################

image commander_starin_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_starin_walk.png", (0, 260, 708, 260)), (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_starin_walk_front:
    Fixed(anim.Filmstrip("battle/units/commander_starin_walk.png", (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_starin_static_back:
    Fixed(im.Crop("battle/units/commander_starin_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_starin_static_front:
    Fixed(im.Crop("battle/units/commander_starin_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_starin_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_starin_main1_attack.png", (0, 260, 1770, 260)), (177, 260), (10, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    linear 0.4 yalign 0.08
    linear 0.4 yalign 0.06
    linear 0.4 yalign 0.08
    linear 0.4 yalign 0.06
    linear 0.4 yalign 0.001
    
image commander_starin_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/commander_starin_main1_attack.png", (177, 260), (10, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    linear 0.4 yalign 0.08
    linear 0.4 yalign 0.06
    linear 0.4 yalign 0.08
    linear 0.4 yalign 0.06
    linear 0.4 yalign 0.001

image commander_starin_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_starin_main1_attack.png", (1593, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_starin_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_starin_main1_attack.png", (1593, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)   
    
image commander_starin_main2_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_starin_main2_attack.png", (0, 260, 3009, 260)), (177, 260), (17, 1), .04, loop=True, xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
    
image commander_starin_main2_attack_front:
    Fixed(anim.Filmstrip("battle/units/commander_starin_main2_attack.png", (177, 260), (17, 1), .04, loop=True, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_starin_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_starin_main2_attack.png", (2832, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_starin_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_starin_main2_attack.png", (2832, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_starin_special1_attack_back:
    contains:
        "seal_dark"
        xpos 320
        ypos 430
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/commander_starin_special1_base.png", (0, 260, 1770, 260)), (177, 260), (10, 1), .08, loop=True, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/commander_starin_special1_attack.png", (0, 260, 1770, 260)), (177, 260), (10, 1), .08, loop=True, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        alpha 0
        linear 0.5 alpha 1.0
        linear 0.5 alpha 0
        repeat
    
image commander_starin_special1_attack_front:
    contains:
        "seal_dark"
        xpos 320
        ypos 430
    contains:
        Fixed(anim.Filmstrip("battle/units/commander_starin_special1_base.png", (177, 260), (10, 1), .08, loop=True, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        Fixed(anim.Filmstrip("battle/units/commander_starin_special1_attack.png", (177, 260), (10, 1), .08, loop=True, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        alpha 0
        linear 0.5 alpha 1.0
        linear 0.5 alpha 0
        repeat

image commander_starin_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_starin_special1_base.png", (1593, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_starin_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_starin_special1_base.png", (1593, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)  
    
image commander_starin_special2_attack_back:
    parallel:
        contains:
            Fixed(anim.Filmstrip(im.Crop("battle/units/commander_starin_special2_base.png", (0, 260, 1770, 260)), (177, 260), (10, 1), .07, loop=True, xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
        contains:
            Fixed(anim.Filmstrip(im.Crop("battle/units/commander_starin_special2_attack.png", (0, 260, 1770, 260)), (177, 260), (10, 1), .07, loop=True, xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
            alpha 0
            linear 0.5 alpha 1.0
            linear 0.5 alpha 0
            repeat
        linear 0.4 yalign 0.08
        linear 0.4 yalign 0.06
        linear 0.4 yalign 0.08
        linear 0.4 yalign 0.06
        linear 0.4 yalign 0.001
    
image commander_starin_special2_attack_front:
    parallel:
        contains:
            Fixed(anim.Filmstrip("battle/units/commander_starin_special2_base.png", (177, 260), (10, 1), .07, loop=True, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        contains:
            Fixed(anim.Filmstrip("battle/units/commander_starin_special2_attack.png", (177, 260), (10, 1), .07, loop=True, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
            alpha 0
            linear 0.5 alpha 1.0
            linear 0.5 alpha 0
            repeat
        linear 0.4 yalign 0.08
        linear 0.4 yalign 0.06
        linear 0.4 yalign 0.08
        linear 0.4 yalign 0.06
        linear 0.4 yalign 0.001

image commander_starin_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_starin_special2_base.png", (1593, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_starin_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_starin_special2_base.png", (1593, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image commander_starin_special3_attack_back:
    parallel:
        contains:
            Fixed(anim.Filmstrip(im.Crop("battle/units/commander_starin_special3_base.png", (0, 260, 1770, 260)), (177, 260), (10, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        contains:
            Fixed(anim.Filmstrip(im.Crop("battle/units/commander_starin_special3_attack.png", (0, 260, 1770, 260)), (177, 260), (10, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
            alpha 0
            linear 0.5 alpha 1.0
            linear 0.5 alpha 0
            repeat
        linear 0.4 yalign 0.08
        linear 0.4 yalign 0.06
        linear 0.4 yalign 0.08
        linear 0.4 yalign 0.06
        linear 0.4 yalign 0.001
    
image commander_starin_special3_attack_front:
    parallel:
        contains:
            Fixed(anim.Filmstrip("battle/units/commander_starin_special3_base.png", (177, 260), (10, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        contains:
            Fixed(anim.Filmstrip("battle/units/commander_starin_special3_attack.png", (177, 260), (10, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
            alpha 0
            linear 0.5 alpha 1.0
            linear 0.5 alpha 0
            repeat
        linear 0.4 yalign 0.08
        linear 0.4 yalign 0.06
        linear 0.4 yalign 0.08
        linear 0.4 yalign 0.06
        linear 0.4 yalign 0.001

image commander_starin_special3_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_starin_special3_base.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_starin_special3_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_starin_special3_base.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_starin_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 320
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_starin_walk.png", (0, 260, 708, 260)), (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_xpower", xsize=840, ysize=840)

image commander_starin_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 320
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/commander_starin_walk.png", (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_xpower", xsize=840, ysize=840)
    
image commander_starin_main1_powerup_finalframe_back:
    At(Fixed(im.Crop("battle/units/commander_starin_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)

image commander_starin_main1_powerup_finalframe_front:
    At(Fixed(im.Crop("battle/units/commander_starin_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    
image commander_starin_main2_powerup_back:
    contains:
        "seal_powerup"
        xpos 320
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_starin_walk.png", (0, 260, 708, 260)), (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_blitz", xsize=840, ysize=840)

image commander_starin_main2_powerup_front:
    contains:
        "seal_powerup"
        xpos 320
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/commander_starin_walk.png", (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_blitz", xsize=840, ysize=840)
    
image commander_starin_main2_powerup_finalframe_back:
    At(Fixed(im.Crop("battle/units/commander_starin_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)

image commander_starin_main2_powerup_finalframe_front:
    At(Fixed(im.Crop("battle/units/commander_starin_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    
image commander_starin_heal_back:
    contains:
        "seal_heal"
        xpos 320
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_starin_walk.png", (0, 260, 708, 260)), (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image commander_starin_heal_front:
    contains:
        "seal_heal"
        xpos 320
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/commander_starin_walk.png", (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image commander_starin_heal_finalframe_back:
    Fixed(im.Crop("battle/units/commander_starin_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_starin_heal_finalframe_front:
    Fixed(im.Crop("battle/units/commander_starin_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#commander_yamato
################################

image commander_yamato_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_yamato_walk.png", (0, 258, 708, 258)), (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_yamato_walk_front:
    Fixed(anim.Filmstrip("battle/units/commander_yamato_walk.png", (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_yamato_static_back:
    Fixed(im.Crop("battle/units/commander_yamato_walk.png", (0, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_yamato_static_front:
    Fixed(im.Crop("battle/units/commander_yamato_walk.png", (0, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_yamato_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_yamato_main1_attack.png", (0, 258, 2655, 258)), (177, 258), (15, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
    
image commander_yamato_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/commander_yamato_main1_attack.png", (177, 258), (15, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_yamato_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_yamato_main1_attack.png", (2478, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_yamato_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_yamato_main1_attack.png", (2478, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)   
    
image commander_yamato_main2_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_yamato_main2_attack.png", (0, 258, 3363, 258)), (177, 258), (19, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
    
image commander_yamato_main2_attack_front:
    Fixed(anim.Filmstrip("battle/units/commander_yamato_main2_attack.png", (177, 258), (19, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_yamato_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_yamato_main2_attack.png", (3186, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_yamato_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_yamato_main2_attack.png", (3186, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)   
    
image commander_yamato_special1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_yamato_special1_attack.png", (0, 258, 885, 258)), (177, 258), (5, 1), .07, loop=False, xalign=0.485, yalign=0.5), xsize=840, ysize=840)
    
image commander_yamato_special1_attack_front:
    Fixed(anim.Filmstrip("battle/units/commander_yamato_special1_attack.png", (177, 258), (5, 1), .07, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_yamato_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_yamato_special1_attack.png", (708, 258, 177, 258), xalign=0.485, yalign=0.5), xsize=840, ysize=840)
    
image commander_yamato_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_yamato_special1_attack.png", (708, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_yamato_special2_attack_back:
    parallel:
        contains:
            Fixed(anim.Filmstrip(im.Crop("battle/units/commander_yamato_special1_attack.png", (0, 258, 885, 258)), (177, 258), (5, 1), .07, loop=False, xalign=0.49, yalign=0.5), xsize=840, ysize=840)
        contains:
            Fixed(anim.Filmstrip(im.Crop("battle/units/commander_yamato_special2_attack.png", (0, 258, 885, 258)), (177, 258), (5, 1), .07, loop=False, xalign=0.49, yalign=0.5), xsize=840, ysize=840)
            alpha 0
            linear 0.5 alpha 1.0
            linear 0.5 alpha 0
            repeat
        linear 0.4 yalign 0.08
        linear 0.4 yalign 0.06
        linear 0.4 yalign 0.08
        linear 0.4 yalign 0.06
        linear 0.4 yalign 0.001
    
image commander_yamato_special2_attack_front:
    parallel:
        contains:
            Fixed(anim.Filmstrip("battle/units/commander_yamato_special1_attack.png", (177, 258), (5, 1), .07, loop=False, xalign=0.49, yalign=0.5), xsize=840, ysize=840)
        contains:
            Fixed(anim.Filmstrip("battle/units/commander_yamato_special2_attack.png", (177, 258), (5, 1), .07, loop=False, xalign=0.49, yalign=0.5), xsize=840, ysize=840)
            alpha 0
            linear 0.5 alpha 1.0
            linear 0.5 alpha 0
            repeat
        linear 0.4 yalign 0.08
        linear 0.4 yalign 0.06
        linear 0.4 yalign 0.08
        linear 0.4 yalign 0.06
        linear 0.4 yalign 0.001

image commander_yamato_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_yamato_walk.png", (0, 258, 177, 258), xalign=0.49, yalign=0.5), xsize=840, ysize=840)
    
image commander_yamato_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_yamato_walk.png", (0, 0, 177, 258), xalign=0.49, yalign=0.5), xsize=840, ysize=840)
    
image commander_yamato_special3_attack_back:
    contains:
        "seal_blue"
        xpos 327
        ypos 440
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/commander_yamato_special1_attack.png", (0, 258, 885, 258)), (177, 258), (5, 1), .07, loop=False, xalign=0.49, yalign=0.5), xsize=840, ysize=840)
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/commander_yamato_special2_attack.png", (0, 258, 885, 258)), (177, 258), (5, 1), .07, loop=False, xalign=0.49, yalign=0.5), xsize=840, ysize=840)
        alpha 0
        linear 0.5 alpha 1.0
        linear 0.5 alpha 0
        repeat
    
image commander_yamato_special3_attack_front:
    contains:
        "seal_blue"
        xpos 327
        ypos 440
    contains:
        Fixed(anim.Filmstrip("battle/units/commander_yamato_special1_attack.png", (177, 258), (5, 1), .07, loop=False, xalign=0.49, yalign=0.5), xsize=840, ysize=840)
    contains:
        Fixed(anim.Filmstrip("battle/units/commander_yamato_special2_attack.png", (177, 258), (5, 1), .07, loop=False, xalign=0.49, yalign=0.5), xsize=840, ysize=840)
        alpha 0
        linear 0.5 alpha 1.0
        linear 0.5 alpha 0
        repeat

image commander_yamato_special3_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_yamato_special3_attack.png", (708, 258, 177, 258), xalign=0.49, yalign=0.5), xsize=840, ysize=840)
    
image commander_yamato_special3_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_yamato_special3_attack.png", (708, 0, 177, 258), xalign=0.49, yalign=0.5), xsize=840, ysize=840)
    
image commander_yamato_special4_attack_back:
    contains:
        "seal_powerup"
        xpos 327
        ypos 430
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/commander_yamato_main1_attack.png", (0, 258, 2655, 258)), (177, 258), (15, 1), .04, loop=True, xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
    
image commander_yamato_special4_attack_front:
    contains:
        "seal_powerup"
        xpos 327
        ypos 430
    contains:
        Fixed(anim.Filmstrip("battle/units/commander_yamato_main1_attack.png", (177, 258), (15, 1), .04, loop=True, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_yamato_special4_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_yamato_main1_attack.png", (2478, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_yamato_special4_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_yamato_main1_attack.png", (2478, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)   
    
image commander_yamato_special5_attack_back:
    contains:
        "seal_electric"
        xpos 327
        ypos 440
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/commander_yamato_special3_base.png", (0, 258, 885, 258)), (177, 258), (5, 1), .07, loop=False, xalign=0.49, yalign=0.5), xsize=840, ysize=840)
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/commander_yamato_special3_attack.png", (0, 258, 885, 258)), (177, 258), (5, 1), .07, loop=False, xalign=0.49, yalign=0.5), xsize=840, ysize=840)
        alpha 0
        linear 0.5 alpha 1.0
        linear 0.5 alpha 0
        repeat
    
image commander_yamato_special5_attack_front:
    contains:
        "seal_electric"
        xpos 327
        ypos 440
    contains:
        Fixed(anim.Filmstrip("battle/units/commander_yamato_special3_base.png", (177, 258), (5, 1), .07, loop=False, xalign=0.49, yalign=0.5), xsize=840, ysize=840)
    contains:
        Fixed(anim.Filmstrip("battle/units/commander_yamato_special3_attack.png", (177, 258), (5, 1), .07, loop=False, xalign=0.49, yalign=0.5), xsize=840, ysize=840)
        alpha 0
        linear 0.5 alpha 1.0
        linear 0.5 alpha 0
        repeat

image commander_yamato_special5_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_yamato_special3_attack.png", (708, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_yamato_special5_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_yamato_special3_attack.png", (708, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_yamato_special6_attack_back:
    contains:
        "seal_powerup"
        xpos 327
        ypos 430
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/commander_yamato_main1_attack.png", (0, 258, 2655, 258)), (177, 258), (15, 1), .04, loop=True, xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
    
image commander_yamato_special6_attack_front:
    contains:
        "seal_powerup"
        xpos 327
        ypos 430
    contains:
        Fixed(anim.Filmstrip("battle/units/commander_yamato_main1_attack.png", (177, 258), (15, 1), .04, loop=True, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_yamato_special6_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_yamato_main1_attack.png", (2478, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_yamato_special6_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_yamato_main1_attack.png", (2478, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)   
    
image commander_yamato_special7_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_yamato_special1_attack.png", (0, 258, 885, 258)), (177, 258), (5, 1), .07, loop=False, xalign=0.49, yalign=0.5), xsize=840, ysize=840)
    linear 0.1 yalign 0.001
    linear 0.1 yalign 0.05
    linear 0.1 yalign 0.001
    repeat
    
image commander_yamato_special7_attack_front:
    Fixed(anim.Filmstrip("battle/units/commander_yamato_special1_attack.png", (177, 258), (5, 1), .07, loop=False, xalign=0.49, yalign=0.5), xsize=840, ysize=840)
    linear 0.1 yalign 0.001
    linear 0.1 yalign 0.05
    linear 0.1 yalign 0.001
    repeat

image commander_yamato_special7_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_yamato_special1_attack.png", (708, 258, 177, 258), xalign=0.45, yalign=0.5), xsize=840, ysize=840)
    
image commander_yamato_special7_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_yamato_special1_attack.png", (708, 0, 177, 258), xalign=0.45, yalign=0.5), xsize=840, ysize=840)
    
image commander_yamato_main2_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_yamato_walk.png", (0, 258, 708, 258)), (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_blitz", xsize=840, ysize=840)

image commander_yamato_main2_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/commander_yamato_walk.png", (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_blitz", xsize=840, ysize=840)
    
image commander_yamato_main2_powerup_finalframe_back:
    At(Fixed(im.Crop("battle/units/commander_yamato_walk.png", (0, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)

image commander_yamato_main2_powerup_finalframe_front:
    At(Fixed(im.Crop("battle/units/commander_yamato_walk.png", (0, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    
image commander_yamato_heal_back:
    contains:
        "seal_heal"
        xpos 325
        ypos 450
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_yamato_walk.png", (0, 258, 708, 258)), (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image commander_yamato_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 450
    contains:
        At(Fixed(anim.Filmstrip("battle/units/commander_yamato_walk.png", (177, 258), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image commander_yamato_heal_finalframe_back:
    Fixed(im.Crop("battle/units/commander_yamato_walk.png", (0, 258, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_yamato_heal_finalframe_front:
    Fixed(im.Crop("battle/units/commander_yamato_walk.png", (0, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
     
################################
#commander_zhukky
################################

image commander_zhukky_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_zhukky_walk.png", (0, 260, 708, 260)), (177, 260), (4, 1), .2, xalign=0.52, yalign=0.5), xsize=840, ysize=840)

image commander_zhukky_walk_front:
    Fixed(anim.Filmstrip("battle/units/commander_zhukky_walk.png", (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_zhukky_static_back:
    Fixed(im.Crop("battle/units/commander_zhukky_walk.png", (0, 260, 177, 260), xalign=0.52, yalign=0.5), xsize=840, ysize=840)

image commander_zhukky_static_front:
    Fixed(im.Crop("battle/units/commander_zhukky_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_zhukky_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/commander_zhukky_main1_attack.png", (0, 260, 1770, 260)), (177, 260), (10, 1), .04, loop=False, xalign=0.48, yalign=0.5), xsize=840, ysize=840)
    linear 0.4 yalign 0.08
    linear 0.4 yalign 0.06
    linear 0.4 yalign 0.08
    linear 0.4 yalign 0.06
    linear 0.4 yalign 0.001
    
image commander_zhukky_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/commander_zhukky_main1_attack.png", (177, 260), (10, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    linear 0.4 yalign 0.08
    linear 0.4 yalign 0.06
    linear 0.4 yalign 0.08
    linear 0.4 yalign 0.06
    linear 0.4 yalign 0.001

image commander_zhukky_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_zhukky_main1_attack.png", (1593, 260, 177, 260), xalign=0.47, yalign=0.5), xsize=840, ysize=840)
    
image commander_zhukky_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_zhukky_main1_attack.png", (1593, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)   
    
image commander_zhukky_main2_attack_back:
    contains:
        "offensive_molotovcocktail_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/commander_zhukky_walk.png", (0, 260, 708, 260)), (177, 260), (4, 1), .2, loop=True, xalign=0.52, yalign=0.5), xsize=840, ysize=840)

image commander_zhukky_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/commander_zhukky_walk.png", (177, 260), (4, 1), .2, loop=True, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_molotovcocktail_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image commander_zhukky_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_zhukky_walk.png", (0, 260, 177, 260), xalign=0.52, yalign=0.5), xsize=840, ysize=840)
    
image commander_zhukky_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_zhukky_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image commander_zhukky_special1_attack_back:
    contains:
        "reaction_snow"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        "offensive_iceball_back"
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/commander_zhukky_special1_attack.png", (0, 260, 2124, 260)), (177, 260), (12, 1), .04, loop=False, xalign=0.52, yalign=0.5), xsize=840, ysize=840)
    
image commander_zhukky_special1_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/commander_zhukky_special1_attack.png", (177, 260), (12, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_iceball_front"
    contains:
        "reaction_snow"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0

image commander_zhukky_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_zhukky_special1_attack.png", (1947, 260, 177, 260), xalign=0.52, yalign=0.5), xsize=840, ysize=840)
    
image commander_zhukky_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_zhukky_special1_attack.png", (1947, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)  
    
image commander_zhukky_special2_attack_back:
    contains:
        "seal_light"
        xpos 320
        ypos 435
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/commander_zhukky_special2_base.png", (0, 260, 1770, 260)), (177, 260), (10, 1), .08, loop=True, xalign=0.52, yalign=0.5), xsize=780, ysize=840) 
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/commander_zhukky_special2_attack.png", (0, 260, 1770, 260)), (177, 260), (10, 1), .08, loop=True, xalign=0.52, yalign=0.5), xsize=780, ysize=840)    
        alpha 0
        linear 0.5 alpha 1.0
        linear 0.5 alpha 0
        repeat
    
image commander_zhukky_special2_attack_front:
    contains:
        "seal_light"
        xpos 332
        ypos 440
    contains:
        Fixed(anim.Filmstrip("battle/units/commander_zhukky_special2_base.png", (177, 260), (10, 1), .08, loop=True, xalign=0.554, yalign=0.5), xsize=780, ysize=840)
    contains:
        Fixed(anim.Filmstrip("battle/units/commander_zhukky_special2_attack.png", (177, 260), (10, 1), .08, loop=True, xalign=0.554, yalign=0.5), xsize=780, ysize=840)
        alpha 0
        linear 0.5 alpha 1.0
        linear 0.5 alpha 0
        repeat

image commander_zhukky_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/commander_zhukky_special2_base.png", (1593, 260, 177, 260), xalign=0.52, yalign=0.5), xsize=840, ysize=840)
    
image commander_zhukky_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/commander_zhukky_special2_base.png", (1593, 0, 177, 260), xalign=0.554, yalign=0.5), xsize=840, ysize=840)  
    
image commander_zhukky_special3_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/commander_zhukky_special3_attack.png", (0, 260, 1947, 260)), (177, 260), (11, 1), .02, loop=True, xalign=0.5, yalign=0.5), shake), xsize=840, ysize=840)
    
image commander_zhukky_special3_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/commander_zhukky_special3_attack.png", (177, 260), (11, 1), .02, loop=True, xalign=0.5, yalign=0.5), shake), xsize=840, ysize=840)

image commander_zhukky_special3_attack_finalframe_back:
    Fixed(At(im.Crop("battle/units/commander_zhukky_special3_attack.png", (1770, 260, 177, 260), xalign=0.5, yalign=0.5), shake), xsize=840, ysize=840)
    
image commander_zhukky_special3_attack_finalframe_front:
    Fixed(At(im.Crop("battle/units/commander_zhukky_special3_attack.png", (1770, 0, 177, 260), xalign=0.5, yalign=0.5), shake), xsize=840, ysize=840)
    
image commander_zhukky_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 325
        ypos 435
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_zhukky_walk.png", (0, 260, 708, 260)), (177, 260), (4, 1), .2, xalign=0.52, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_xpower", xsize=840, ysize=840)

image commander_zhukky_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 334
        ypos 432
    contains:
        At(Fixed(anim.Filmstrip("battle/units/commander_zhukky_walk.png", (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_xpower", xsize=840, ysize=840)
    
image commander_zhukky_main1_powerup_finalframe_back:
    At(Fixed(im.Crop("battle/units/commander_zhukky_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)

image commander_zhukky_main1_powerup_finalframe_front:
    At(Fixed(im.Crop("battle/units/commander_zhukky_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    
image commander_zhukky_heal_back:
    contains:
        "seal_heal"
        xpos 320
        ypos 435
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/commander_zhukky_walk.png", (0, 260, 708, 260)), (177, 260), (4, 1), .2, xalign=0.52, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image commander_zhukky_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/commander_zhukky_walk.png", (177, 260), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image commander_zhukky_heal_finalframe_back:
    Fixed(im.Crop("battle/units/commander_zhukky_walk.png", (0, 260, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image commander_zhukky_heal_finalframe_front:
    Fixed(im.Crop("battle/units/commander_zhukky_walk.png", (0, 0, 177, 260), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################################################
################################################################
################################################################
    #  INFANTRY  #
################################################################
################################################################
################################################################   
    
################################
#infantry_germania_gunner_heer1
################################

image infantry_germania_gunner_heer1_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_gunner_heer1_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_gunner_heer1_walk_front:
    Fixed(anim.Filmstrip("battle/units/infantry_germania_gunner_heer1_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_gunner_heer1_static_back:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer1_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_gunner_heer1_static_front:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer1_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_gunner_heer1_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_gunner_heer1_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, xalign=0.51, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_gunner_heer1_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/infantry_germania_gunner_heer1_main1_attack.png", (150, 243), (3, 1), .05, xalign=0.505, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_gunner_heer1_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer1_main1_attack.png", (300, 243, 150, 243), xalign=0.51, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_gunner_heer1_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer1_main1_attack.png", (300, 0, 150, 243), xalign=0.505, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_gunner_heer1_main2_attack_back:
    contains:
        "offensive_stielhandgranate_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_gunner_heer1_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_gunner_heer1_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/infantry_germania_gunner_heer1_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_stielhandgranate_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image infantry_germania_gunner_heer1_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer1_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_gunner_heer1_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer1_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_gunner_heer1_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_gunner_heer1_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image infantry_germania_gunner_heer1_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/infantry_germania_gunner_heer1_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image infantry_germania_gunner_heer1_heal_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer1_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_gunner_heer1_heal_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer1_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#infantry_germania_marksman_heer1
################################

image infantry_germania_marksman_heer1_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_marksman_heer1_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_marksman_heer1_walk_front:
    Fixed(anim.Filmstrip("battle/units/infantry_germania_marksman_heer1_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_marksman_heer1_static_back:
    Fixed(im.Crop("battle/units/infantry_germania_marksman_heer1_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_marksman_heer1_static_front:
    Fixed(im.Crop("battle/units/infantry_germania_marksman_heer1_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_marksman_heer1_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_marksman_heer1_main1_attack.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_marksman_heer1_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/infantry_germania_marksman_heer1_main1_attack.png", (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_marksman_heer1_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_marksman_heer1_main1_attack.png", (513, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_marksman_heer1_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_marksman_heer1_main1_attack.png", (513, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_marksman_heer1_main2_attack_back:
    contains:
        "offensive_stielhandgranate_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_marksman_heer1_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image infantry_germania_marksman_heer1_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/infantry_germania_marksman_heer1_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_stielhandgranate_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    
image infantry_germania_marksman_heer1_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_marksman_heer1_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_marksman_heer1_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_marksman_heer1_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_marksman_heer1_heal_back:
    contains:
        "seal_heal"
        xpos 310
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_marksman_heer1_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image infantry_germania_marksman_heer1_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/infantry_germania_marksman_heer1_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image infantry_germania_marksman_heer1_heal_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_marksman_heer1_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_marksman_heer1_heal_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_marksman_heer1_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#infantry_germania_antitank_heer1
################################

image infantry_germania_antitank_heer1_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_antitank_heer1_walk.png", (0, 243, 684, 243)), (171, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_antitank_heer1_walk_front:
    Fixed(anim.Filmstrip("battle/units/infantry_germania_antitank_heer1_walk.png", (171, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_antitank_heer1_static_back:
    Fixed(im.Crop("battle/units/infantry_germania_antitank_heer1_walk.png", (0, 243, 171, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_antitank_heer1_static_front:
    Fixed(im.Crop("battle/units/infantry_germania_antitank_heer1_walk.png", (0, 0, 171, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_antitank_heer1_main1_attack_back:
    contains:
        "offensive_launcherblast_back"
        xpos 600
        ypos 220
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_antitank_heer1_main1_attack.png", (0, 244.5, 717, 244.5)), (179.25, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_antitank_heer1_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/infantry_germania_antitank_heer1_main1_attack.png", (179.25, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_launcherblast_front"
        xpos 210
        ypos 360

image infantry_germania_antitank_heer1_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_antitank_heer1_main1_attack.png", (537.75, 244.5, 179.25, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_antitank_heer1_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_antitank_heer1_main1_attack.png", (537.75, 0, 179.25, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_antitank_heer1_main2_attack_back:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_antitank_heer1_walk.png", (0, 243, 684, 243)), (171, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_landmine"
        xalign 0.77 yalign -0.6
        
image infantry_germania_antitank_heer1_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/infantry_germania_antitank_heer1_walk.png", (171, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_landmine"
        xalign -0.6 yalign 0.52
    
image infantry_germania_antitank_heer1_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_antitank_heer1_walk.png", (0, 243, 171, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_antitank_heer1_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_antitank_heer1_walk.png", (0, 0, 171, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_antitank_heer1_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_antitank_heer1_walk.png", (0, 243, 684, 243)), (171, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image infantry_germania_antitank_heer1_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/infantry_germania_antitank_heer1_walk.png", (171, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image infantry_germania_antitank_heer1_heal_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_antitank_heer1_walk.png", (0, 243, 171, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_antitank_heer1_heal_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_antitank_heer1_walk.png", (0, 0, 171, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#infantry_germania_gunner_heer3
################################

image infantry_germania_gunner_heer3_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_gunner_heer3_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_gunner_heer3_walk_front:
    Fixed(anim.Filmstrip("battle/units/infantry_germania_gunner_heer3_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_gunner_heer3_static_back:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer3_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_gunner_heer3_static_front:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer3_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_gunner_heer3_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_gunner_heer3_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, xalign=0.513, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_gunner_heer3_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/infantry_germania_gunner_heer3_main1_attack.png", (150, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_gunner_heer3_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer3_main1_attack.png", (300, 243, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_gunner_heer3_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer3_main1_attack.png", (300, 0, 150, 243), xalign=0.513, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_gunner_heer3_main2_attack_back:
    contains:
        "offensive_stielhandgranate_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_gunner_heer3_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_gunner_heer3_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/infantry_germania_gunner_heer3_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_stielhandgranate_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image infantry_germania_gunner_heer3_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer3_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_gunner_heer3_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer3_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_gunner_heer3_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_gunner_heer3_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image infantry_germania_gunner_heer3_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/infantry_germania_gunner_heer3_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image infantry_germania_gunner_heer3_heal_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer3_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_gunner_heer3_heal_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer3_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#infantry_germania_marksman_heer3
################################

image infantry_germania_marksman_heer3_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_marksman_heer3_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_marksman_heer3_walk_front:
    Fixed(anim.Filmstrip("battle/units/infantry_germania_marksman_heer3_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_marksman_heer3_static_back:
    Fixed(im.Crop("battle/units/infantry_germania_marksman_heer3_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_marksman_heer3_static_front:
    Fixed(im.Crop("battle/units/infantry_germania_marksman_heer3_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_marksman_heer3_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_marksman_heer3_main1_attack.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_marksman_heer3_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/infantry_germania_marksman_heer3_main1_attack.png", (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_marksman_heer3_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_marksman_heer3_main1_attack.png", (513, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_marksman_heer3_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_marksman_heer3_main1_attack.png", (513, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_marksman_heer3_main2_attack_back:
    contains:
        "offensive_stielhandgranate_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_marksman_heer3_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image infantry_germania_marksman_heer3_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/infantry_germania_marksman_heer3_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_stielhandgranate_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    
image infantry_germania_marksman_heer3_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_marksman_heer3_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_marksman_heer3_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_marksman_heer3_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_marksman_heer3_heal_back:
    contains:
        "seal_heal"
        xpos 295
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_marksman_heer3_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image infantry_germania_marksman_heer3_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/infantry_germania_marksman_heer3_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image infantry_germania_marksman_heer3_heal_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_marksman_heer3_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_marksman_heer3_heal_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_marksman_heer3_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#infantry_germania_antitank_heer3
################################

image infantry_germania_antitank_heer3_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_antitank_heer3_walk.png", (0, 243, 720, 243)), (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_antitank_heer3_walk_front:
    Fixed(anim.Filmstrip("battle/units/infantry_germania_antitank_heer3_walk.png", (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_antitank_heer3_static_back:
    Fixed(im.Crop("battle/units/infantry_germania_antitank_heer3_walk.png", (0, 243, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_antitank_heer3_static_front:
    Fixed(im.Crop("battle/units/infantry_germania_antitank_heer3_walk.png", (0, 0, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_antitank_heer3_main1_attack_back:
    contains:
        "offensive_launcherblast_back"
        xpos 600
        ypos 220
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_antitank_heer3_main1_attack.png", (0, 244.5, 717, 244.5)), (179.25, 244.5), (4, 1), .05, loop=False, xalign=0.485, yalign=0.505), xsize=840, ysize=840)

image infantry_germania_antitank_heer3_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/infantry_germania_antitank_heer3_main1_attack.png", (179.25, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_launcherblast_front"
        xpos 210
        ypos 360

image infantry_germania_antitank_heer3_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_antitank_heer3_main1_attack.png", (537.75, 244.5, 179.25, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_antitank_heer3_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_antitank_heer3_main1_attack.png", (537.75, 0, 179.25, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_antitank_heer3_main2_attack_back:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_antitank_heer3_walk.png", (0, 243, 720, 243)), (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_landmine"
        xalign 0.77 yalign -0.6
        
image infantry_germania_antitank_heer3_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/infantry_germania_antitank_heer3_walk.png", (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_landmine"
        xalign -0.6 yalign 0.52
    
image infantry_germania_antitank_heer3_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_antitank_heer3_walk.png", (0, 243, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_antitank_heer3_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_antitank_heer3_walk.png", (0, 0, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_antitank_heer3_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_antitank_heer3_walk.png", (0, 243, 720, 243)), (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image infantry_germania_antitank_heer3_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/infantry_germania_antitank_heer3_walk.png", (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image infantry_germania_antitank_heer3_heal_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_antitank_heer3_walk.png", (0, 243, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_antitank_heer3_heal_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_antitank_heer3_walk.png", (0, 0, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#infantry_germania_gunner_heer5
################################

image infantry_germania_gunner_heer5_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_gunner_heer5_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_gunner_heer5_walk_front:
    Fixed(anim.Filmstrip("battle/units/infantry_germania_gunner_heer5_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_gunner_heer5_static_back:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer5_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_gunner_heer5_static_front:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer5_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_gunner_heer5_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_gunner_heer5_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_gunner_heer5_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/infantry_germania_gunner_heer5_main1_attack.png", (150, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_gunner_heer5_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer5_main1_attack.png", (300, 243, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_gunner_heer5_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer5_main1_attack.png", (300, 0, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_gunner_heer5_main2_attack_back:
    contains:
        "offensive_stielhandgranate_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_gunner_heer5_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_gunner_heer5_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/infantry_germania_gunner_heer5_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_stielhandgranate_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image infantry_germania_gunner_heer5_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer5_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_gunner_heer5_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer5_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_gunner_heer5_special1_attack_back:
    contains:
        "offensive_bayonet_back"
    contains:
        "reaction_hit"
        xalign 0.69 yalign 0.08 alpha 0 xzoom -1
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_gunner_heer5_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_gunner_heer5_special1_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/infantry_germania_gunner_heer5_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_bayonet_front"
    contains:
        "reaction_hit"
        xalign -0.28 yalign 0.67 alpha 0
        pause 0.75
        alpha 1.0
    
image infantry_germania_gunner_heer5_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer5_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_gunner_heer5_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer5_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_gunner_heer5_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_gunner_heer5_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image infantry_germania_gunner_heer5_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/infantry_germania_gunner_heer5_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image infantry_germania_gunner_heer5_heal_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer5_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_gunner_heer5_heal_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer5_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#infantry_germania_marksman_heer5
################################

image infantry_germania_marksman_heer5_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_marksman_heer5_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_marksman_heer5_walk_front:
    Fixed(anim.Filmstrip("battle/units/infantry_germania_marksman_heer5_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_marksman_heer5_static_back:
    Fixed(im.Crop("battle/units/infantry_germania_marksman_heer5_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_marksman_heer5_static_front:
    Fixed(im.Crop("battle/units/infantry_germania_marksman_heer5_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_marksman_heer5_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_marksman_heer5_main1_attack.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_marksman_heer5_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/infantry_germania_marksman_heer5_main1_attack.png", (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_marksman_heer5_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_marksman_heer5_main1_attack.png", (513, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_marksman_heer5_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_marksman_heer5_main1_attack.png", (513, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_marksman_heer5_main2_attack_back:
    contains:
        "offensive_stielhandgranate_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_marksman_heer5_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image infantry_germania_marksman_heer5_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/infantry_germania_marksman_heer5_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_stielhandgranate_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    
image infantry_germania_marksman_heer5_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_marksman_heer5_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_marksman_heer5_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_marksman_heer5_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_marksman_heer5_heal_back:
    contains:
        "seal_heal"
        xpos 310
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_marksman_heer5_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image infantry_germania_marksman_heer5_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/infantry_germania_marksman_heer5_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image infantry_germania_marksman_heer5_heal_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_marksman_heer5_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_marksman_heer5_heal_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_marksman_heer5_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#infantry_germania_antitank_heer5
################################

image infantry_germania_antitank_heer5_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_antitank_heer5_walk.png", (0, 243, 684, 243)), (171, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_antitank_heer5_walk_front:
    Fixed(anim.Filmstrip("battle/units/infantry_germania_antitank_heer5_walk.png", (171, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_antitank_heer5_static_back:
    Fixed(im.Crop("battle/units/infantry_germania_antitank_heer5_walk.png", (0, 243, 171, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_antitank_heer5_static_front:
    Fixed(im.Crop("battle/units/infantry_germania_antitank_heer5_walk.png", (0, 0, 171, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_antitank_heer5_main1_attack_back:
    contains:
        "offensive_launcherblast_back"
        xpos 600
        ypos 220
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_antitank_heer5_main1_attack.png", (0, 244.5, 717, 244.5)), (179.25, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_antitank_heer5_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/infantry_germania_antitank_heer5_main1_attack.png", (179.25, 244.5), (4, 1), .05, loop=False, xalign=0.507, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_launcherblast_front"
        xpos 210
        ypos 360

image infantry_germania_antitank_heer5_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_antitank_heer5_main1_attack.png", (537.75, 244.5, 179.25, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_antitank_heer5_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_antitank_heer5_main1_attack.png", (537.75, 0, 179.25, 244.5), xalign=0.507, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_antitank_heer5_main2_attack_back:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_antitank_heer5_walk.png", (0, 243, 684, 243)), (171, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_landmine"
        xalign 0.77 yalign -0.6
        
image infantry_germania_antitank_heer5_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/infantry_germania_antitank_heer5_walk.png", (171, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_landmine"
        xalign -0.6 yalign 0.52
    
image infantry_germania_antitank_heer5_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_antitank_heer5_walk.png", (0, 243, 171, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_antitank_heer5_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_antitank_heer5_walk.png", (0, 0, 171, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_antitank_heer5_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_antitank_heer5_walk.png", (0, 243, 684, 243)), (171, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image infantry_germania_antitank_heer5_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/infantry_germania_antitank_heer5_walk.png", (171, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image infantry_germania_antitank_heer5_heal_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_antitank_heer5_walk.png", (0, 243, 171, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_antitank_heer5_heal_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_antitank_heer5_walk.png", (0, 0, 171, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

################################
#infantry_germania_gunner_heer7
################################

image infantry_germania_gunner_heer7_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_gunner_heer7_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_gunner_heer7_walk_front:
    Fixed(anim.Filmstrip("battle/units/infantry_germania_gunner_heer7_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_gunner_heer7_static_back:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer7_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_gunner_heer7_static_front:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer7_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_gunner_heer7_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_gunner_heer7_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_gunner_heer7_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/infantry_germania_gunner_heer7_main1_attack.png", (150, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_gunner_heer7_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer7_main1_attack.png", (300, 243, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_gunner_heer7_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer7_main1_attack.png", (300, 0, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_gunner_heer7_main2_attack_back:
    contains:
        "offensive_stielhandgranate_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_gunner_heer7_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_gunner_heer7_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/infantry_germania_gunner_heer7_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_stielhandgranate_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image infantry_germania_gunner_heer7_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer7_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_gunner_heer7_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer7_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_gunner_heer7_special1_attack_back:
    contains:
        "offensive_bayonet_back"
    contains:
        "reaction_hit"
        xalign 0.69 yalign 0.08 alpha 0 xzoom -1
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_gunner_heer7_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_gunner_heer7_special1_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/infantry_germania_gunner_heer7_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_bayonet_front"
    contains:
        "reaction_hit"
        xalign -0.28 yalign 0.67 alpha 0
        pause 0.75
        alpha 1.0
    
image infantry_germania_gunner_heer7_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer7_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_gunner_heer7_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer7_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_gunner_heer7_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_gunner_heer7_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image infantry_germania_gunner_heer7_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/infantry_germania_gunner_heer7_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image infantry_germania_gunner_heer7_heal_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer7_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_gunner_heer7_heal_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_gunner_heer7_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#infantry_germania_marksman_heer7
################################

image infantry_germania_marksman_heer7_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_marksman_heer7_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_marksman_heer7_walk_front:
    Fixed(anim.Filmstrip("battle/units/infantry_germania_marksman_heer7_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_marksman_heer7_static_back:
    Fixed(im.Crop("battle/units/infantry_germania_marksman_heer7_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_marksman_heer7_static_front:
    Fixed(im.Crop("battle/units/infantry_germania_marksman_heer7_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_marksman_heer7_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_marksman_heer7_main1_attack.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_marksman_heer7_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/infantry_germania_marksman_heer7_main1_attack.png", (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_marksman_heer7_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_marksman_heer7_main1_attack.png", (513, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_marksman_heer7_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_marksman_heer7_main1_attack.png", (513, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_marksman_heer7_main2_attack_back:
    contains:
        "offensive_stielhandgranate_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_marksman_heer7_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image infantry_germania_marksman_heer7_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/infantry_germania_marksman_heer7_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_stielhandgranate_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    
image infantry_germania_marksman_heer7_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_marksman_heer7_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_marksman_heer7_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_marksman_heer7_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_marksman_heer7_heal_back:
    contains:
        "seal_heal"
        xpos 310
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_marksman_heer7_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image infantry_germania_marksman_heer7_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/infantry_germania_marksman_heer7_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image infantry_germania_marksman_heer7_heal_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_marksman_heer7_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_marksman_heer7_heal_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_marksman_heer7_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#infantry_germania_antitank_heer7
################################

image infantry_germania_antitank_heer7_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_antitank_heer7_walk.png", (0, 243, 684, 243)), (171, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_antitank_heer7_walk_front:
    Fixed(anim.Filmstrip("battle/units/infantry_germania_antitank_heer7_walk.png", (171, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_antitank_heer7_static_back:
    Fixed(im.Crop("battle/units/infantry_germania_antitank_heer7_walk.png", (0, 243, 171, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_antitank_heer7_static_front:
    Fixed(im.Crop("battle/units/infantry_germania_antitank_heer7_walk.png", (0, 0, 171, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_antitank_heer7_main1_attack_back:
    contains:
        "offensive_launcherblast_back"
        xpos 600
        ypos 220
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_antitank_heer7_main1_attack.png", (0, 244.5, 717, 244.5)), (179.25, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_antitank_heer7_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/infantry_germania_antitank_heer7_main1_attack.png", (179.25, 244.5), (4, 1), .05, loop=False, xalign=0.507, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_launcherblast_front"
        xpos 210
        ypos 360

image infantry_germania_antitank_heer7_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_antitank_heer7_main1_attack.png", (537.75, 244.5, 179.25, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_antitank_heer7_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_antitank_heer7_main1_attack.png", (537.75, 0, 179.25, 244.5), xalign=0.507, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_antitank_heer7_main2_attack_back:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_antitank_heer7_walk.png", (0, 243, 684, 243)), (171, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_landmine"
        xalign 0.77 yalign -0.6
        
image infantry_germania_antitank_heer7_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/infantry_germania_antitank_heer7_walk.png", (171, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_landmine"
        xalign -0.6 yalign 0.52
    
image infantry_germania_antitank_heer7_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_antitank_heer7_walk.png", (0, 243, 171, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_antitank_heer7_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_antitank_heer7_walk.png", (0, 0, 171, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image infantry_germania_antitank_heer7_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/infantry_germania_antitank_heer7_walk.png", (0, 243, 684, 243)), (171, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image infantry_germania_antitank_heer7_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/infantry_germania_antitank_heer7_walk.png", (171, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image infantry_germania_antitank_heer7_heal_finalframe_back:
    Fixed(im.Crop("battle/units/infantry_germania_antitank_heer7_walk.png", (0, 243, 171, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image infantry_germania_antitank_heer7_heal_finalframe_front:
    Fixed(im.Crop("battle/units/infantry_germania_antitank_heer7_walk.png", (0, 0, 171, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
    
################################################################
################################################################
################################################################
    #  AIRSUPPORT  #
################################################################
################################################################
################################################################   
    
################################
#airsupport_dambuster
################################

image airsupport_dambuster_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_dambuster_walk.png", (0, 375, 2448, 375)), (612, 375), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_dambuster_walk_front:
    Fixed(anim.Filmstrip("battle/units/airsupport_dambuster_walk.png", (612, 375), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_dambuster_static_back:
    Fixed(im.Crop("battle/units/airsupport_dambuster_walk.png", (0, 375, 612, 375), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_dambuster_static_front:
    Fixed(im.Crop("battle/units/airsupport_dambuster_walk.png", (0, 0, 612, 375), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_dambuster_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_dambuster_main1_attack.png", (0, 375, 2448, 375)), (612, 375), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_dambuster_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/airsupport_dambuster_main1_attack.png", (612, 375), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_dambuster_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/airsupport_dambuster_main1_attack.png", (1836, 375, 612, 375), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_dambuster_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/airsupport_dambuster_main1_attack.png", (1836, 0, 612, 375), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_dambuster_main2_attack_back:
    contains:
        "offensive_bouncingbomb_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_dambuster_walk.png", (0, 375, 2448, 375)), (612, 375), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_dambuster_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/airsupport_dambuster_walk.png", (612, 375), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_bouncingbomb_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    
image airsupport_dambuster_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/airsupport_dambuster_walk.png", (0, 375, 612, 375), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_dambuster_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/airsupport_dambuster_walk.png", (0, 0, 612, 375), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_dambuster_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_dambuster_walk.png", (0, 375, 2448, 375)), (612, 375), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)

image airsupport_dambuster_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/airsupport_dambuster_walk.png", (612, 375), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image airsupport_dambuster_heal_finalframe_back:
    Fixed(im.Crop("battle/units/airsupport_dambuster_walk.png", (0, 375, 612, 375), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_dambuster_heal_finalframe_front:
    Fixed(im.Crop("battle/units/airsupport_dambuster_walk.png", (0, 0, 612, 375), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

################################
#airsupport_fopfighter
################################

image airsupport_fopfighter_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_fopfighter_walk.png", (0, 339, 2124, 339)), (531, 339), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_fopfighter_walk_front:
    Fixed(anim.Filmstrip("battle/units/airsupport_fopfighter_walk.png", (531, 339), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_fopfighter_static_back:
    Fixed(im.Crop("battle/units/airsupport_fopfighter_walk.png", (0, 339, 531, 339), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_fopfighter_static_front:
    Fixed(im.Crop("battle/units/airsupport_fopfighter_walk.png", (0, 0, 531, 339), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_fopfighter_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_fopfighter_main1_attack.png", (0, 339, 2124, 339)), (531, 339), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_fopfighter_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/airsupport_fopfighter_main1_attack.png", (531, 339), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_fopfighter_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/airsupport_fopfighter_main1_attack.png", (1593, 339, 531, 339), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_fopfighter_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/airsupport_fopfighter_main1_attack.png", (1593, 0, 531, 339), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_fopfighter_main2_attack_back:
    contains:
        "offensive_rp3rocket_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_fopfighter_walk.png", (0, 339, 2124, 339)), (531, 339), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_fopfighter_main2_attack_front:
    contains:
        "offensive_rp3rocket_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip("battle/units/airsupport_fopfighter_walk.png", (531, 339), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_fopfighter_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/airsupport_fopfighter_walk.png", (0, 339, 531, 339), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_fopfighter_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/airsupport_fopfighter_walk.png", (0, 0, 531, 339), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_fopfighter_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_fopfighter_walk.png", (0, 339, 2124, 339)), (531, 339), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)

image airsupport_fopfighter_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/airsupport_fopfighter_walk.png", (531, 339), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image airsupport_fopfighter_heal_finalframe_back:
    Fixed(im.Crop("battle/units/airsupport_fopfighter_walk.png", (0, 339, 531, 339), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_fopfighter_heal_finalframe_front:
    Fixed(im.Crop("battle/units/airsupport_fopfighter_walk.png", (0, 0, 531, 339), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#airsupport_freccia
################################

image airsupport_freccia_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_freccia_walk.png", (0, 195, 1272, 195)), (318, 195), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_freccia_walk_front:
    Fixed(anim.Filmstrip("battle/units/airsupport_freccia_walk.png", (318, 195), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_freccia_static_back:
    Fixed(im.Crop("battle/units/airsupport_freccia_walk.png", (0, 195, 318, 195), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_freccia_static_front:
    Fixed(im.Crop("battle/units/airsupport_freccia_walk.png", (0, 0, 318, 195), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_freccia_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_freccia_main1_attack.png", (0, 195, 1272, 195)), (318, 195), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_freccia_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/airsupport_freccia_main1_attack.png", (318, 195), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_freccia_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/airsupport_freccia_main1_attack.png", (954, 195, 318, 195), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_freccia_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/airsupport_freccia_main1_attack.png", (954, 0, 318, 195), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_freccia_main2_attack_back:
    contains:
        Fixed(At(anim.Filmstrip(im.Crop("battle/units/airsupport_freccia_walk.png", (0, 195, 1272, 195)), (318, 195), (4, 1), .05, xalign=0.5, yalign=0.5), dive), xsize=840, ysize=840)

image airsupport_freccia_main2_attack_front:
    contains:
        Fixed(At(anim.Filmstrip("battle/units/airsupport_freccia_walk.png", (318, 195), (4, 1), .05, xalign=0.5, yalign=0.5), dive), xsize=840, ysize=840)
    
image airsupport_freccia_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/airsupport_freccia_walk.png", (0, 195, 318, 195), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_freccia_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/airsupport_freccia_walk.png", (0, 0, 318, 195), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_freccia_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_freccia_walk.png", (0, 195, 1272, 195)), (318, 195), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)

image airsupport_freccia_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/airsupport_freccia_walk.png", (318, 195), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image airsupport_freccia_heal_finalframe_back:
    Fixed(im.Crop("battle/units/airsupport_freccia_walk.png", (0, 195, 318, 195), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_freccia_heal_finalframe_front:
    Fixed(im.Crop("battle/units/airsupport_freccia_walk.png", (0, 0, 318, 195), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#airsupport_griffin
################################

image airsupport_griffin_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_griffin_walk.png", (0, 447, 3000, 447)), (750, 447), (4, 1), .05, xalign=0.5, yalign=0.4), xsize=840, ysize=840)

image airsupport_griffin_walk_front:
    Fixed(anim.Filmstrip("battle/units/airsupport_griffin_walk.png", (750, 447), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_griffin_static_back:
    Fixed(im.Crop("battle/units/airsupport_griffin_walk.png", (0, 447, 750, 447), xalign=0.5, yalign=0.4), xsize=840, ysize=840)

image airsupport_griffin_static_front:
    Fixed(im.Crop("battle/units/airsupport_griffin_walk.png", (0, 0, 750, 447), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_griffin_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_griffin_main1_attack.png", (0, 447, 3000, 447)), (750, 447), (4, 1), .05, xalign=0.5, yalign=0.4), xsize=840, ysize=840)

image airsupport_griffin_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/airsupport_griffin_main1_attack.png", (750, 447), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_griffin_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/airsupport_griffin_main1_attack.png", (2250, 447, 750, 447), xalign=0.5, yalign=0.4), xsize=840, ysize=840)

image airsupport_griffin_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/airsupport_griffin_main1_attack.png", (2250, 0, 750, 447), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_griffin_main2_attack_back:
    contains:
        "offensive_gunfire_back"
        xpos 675
        ypos 320
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_griffin_walk.png", (0, 447, 3000, 447)), (750, 447), (4, 1), .05, xalign=0.5, yalign=0.4), xsize=840, ysize=840)

image airsupport_griffin_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/airsupport_griffin_walk.png", (750, 447), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 120
        ypos 600
    
image airsupport_griffin_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/airsupport_griffin_walk.png", (0, 447, 750, 447), xalign=0.5, yalign=0.4), xsize=840, ysize=840)

image airsupport_griffin_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/airsupport_griffin_walk.png", (0, 0, 750, 447), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_griffin_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_griffin_walk.png", (0, 447, 3000, 447)), (750, 447), (4, 1), .05, xalign=0.5, yalign=0.4), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)

image airsupport_griffin_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/airsupport_griffin_walk.png", (750, 447), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image airsupport_griffin_heal_finalframe_back:
    Fixed(im.Crop("battle/units/airsupport_griffin_walk.png", (0, 447, 750, 447), xalign=0.5, yalign=0.4), xsize=840, ysize=840)

image airsupport_griffin_heal_finalframe_front:
    Fixed(im.Crop("battle/units/airsupport_griffin_walk.png", (0, 0, 750, 447), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#airsupport_ironsides
################################

image airsupport_ironsides_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_ironsides_walk.png", (0, 348, 2304, 348)), (576, 348), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_ironsides_walk_front:
    Fixed(anim.Filmstrip("battle/units/airsupport_ironsides_walk.png", (576, 348), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_ironsides_static_back:
    Fixed(im.Crop("battle/units/airsupport_ironsides_walk.png", (0, 348, 576, 348), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_ironsides_static_front:
    Fixed(im.Crop("battle/units/airsupport_ironsides_walk.png", (0, 0, 576, 348), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_ironsides_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_ironsides_main1_attack.png", (0, 348, 2304, 348)), (576, 348), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_ironsides_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/airsupport_ironsides_main1_attack.png", (576, 348), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_ironsides_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/airsupport_ironsides_main1_attack.png", (1728, 348, 576, 348), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_ironsides_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/airsupport_ironsides_main1_attack.png", (1728, 0, 576, 348), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_ironsides_main2_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_ironsides_main2_attack.png", (0, 348, 2304, 348)), (576, 348), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_ironsides_main2_attack_front:
    Fixed(anim.Filmstrip("battle/units/airsupport_ironsides_main2_attack.png", (576, 348), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_ironsides_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/airsupport_ironsides_main2_attack.png", (1728, 348, 576, 348), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_ironsides_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/airsupport_ironsides_main2_attack.png", (1728, 0, 576, 348), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_ironsides_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_ironsides_walk.png", (0, 348, 2304, 348)), (576, 348), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)

image airsupport_ironsides_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/airsupport_ironsides_walk.png", (576, 348), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image airsupport_ironsides_heal_finalframe_back:
    Fixed(im.Crop("battle/units/airsupport_ironsides_walk.png", (0, 348, 576, 348), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_ironsides_heal_finalframe_front:
    Fixed(im.Crop("battle/units/airsupport_ironsides_walk.png", (0, 0, 576, 348), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#airsupport_petlyakov
################################

image airsupport_petlyakov_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_petlyakov_walk.png", (0, 348, 2304, 348)), (576, 348), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_petlyakov_walk_front:
    Fixed(anim.Filmstrip("battle/units/airsupport_petlyakov_walk.png", (576, 348), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_petlyakov_static_back:
    Fixed(im.Crop("battle/units/airsupport_petlyakov_walk.png", (0, 348, 576, 348), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_petlyakov_static_front:
    Fixed(im.Crop("battle/units/airsupport_petlyakov_walk.png", (0, 0, 576, 348), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_petlyakov_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_petlyakov_main1_attack.png", (0, 348, 2304, 348)), (576, 348), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_petlyakov_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/airsupport_petlyakov_main1_attack.png", (576, 348), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_petlyakov_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/airsupport_petlyakov_main1_attack.png", (1728, 348, 576, 348), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_petlyakov_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/airsupport_petlyakov_main1_attack.png", (1728, 0, 576, 348), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_petlyakov_main2_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_petlyakov_walk.png", (0, 348, 2304, 348)), (576, 348), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_petlyakov_main2_attack_front:
    Fixed(anim.Filmstrip("battle/units/airsupport_petlyakov_walk.png", (576, 348), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_petlyakov_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/airsupport_petlyakov_walk.png", (0, 348, 576, 348), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_petlyakov_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/airsupport_petlyakov_walk.png", (0, 0, 576, 348), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_petlyakov_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_petlyakov_walk.png", (0, 348, 2304, 348)), (576, 348), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)

image airsupport_petlyakov_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/airsupport_petlyakov_walk.png", (576, 348), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image airsupport_petlyakov_heal_finalframe_back:
    Fixed(im.Crop("battle/units/airsupport_petlyakov_walk.png", (0, 348, 576, 348), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_petlyakov_heal_finalframe_front:
    Fixed(im.Crop("battle/units/airsupport_petlyakov_walk.png", (0, 0, 576, 348), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#airsupport_rampage
################################

image airsupport_rampage_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_rampage_walk.png", (0, 255, 1752, 255)), (438, 255), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_rampage_walk_front:
    Fixed(anim.Filmstrip("battle/units/airsupport_rampage_walk.png", (438, 255), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_rampage_static_back:
    Fixed(im.Crop("battle/units/airsupport_rampage_walk.png", (0, 255, 438, 255), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_rampage_static_front:
    Fixed(im.Crop("battle/units/airsupport_rampage_walk.png", (0, 0, 438, 255), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_rampage_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_rampage_main1_attack.png", (0, 255, 1752, 255)), (438, 255), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_rampage_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/airsupport_rampage_main1_attack.png", (438, 255), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_rampage_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/airsupport_rampage_main1_attack.png", (1314, 255, 438, 255), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_rampage_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/airsupport_rampage_main1_attack.png", (1314, 0, 438, 255), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_rampage_main2_attack_back:
    contains:
        "offensive_rp3rocket_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_rampage_walk.png", (0, 255, 1752, 255)), (438, 255), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_rampage_main2_attack_front:
    contains:
        "offensive_rp3rocket_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip("battle/units/airsupport_rampage_walk.png", (438, 255), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_rampage_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/airsupport_rampage_walk.png", (0, 255, 438, 255), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_rampage_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/airsupport_rampage_walk.png", (0, 0, 438, 255), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_rampage_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_rampage_walk.png", (0, 255, 1752, 255)), (438, 255), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)

image airsupport_rampage_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/airsupport_rampage_walk.png", (438, 255), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image airsupport_rampage_heal_finalframe_back:
    Fixed(im.Crop("battle/units/airsupport_rampage_walk.png", (0, 255, 438, 255), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_rampage_heal_finalframe_front:
    Fixed(im.Crop("battle/units/airsupport_rampage_walk.png", (0, 0, 438, 255), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#airsupport_shrike
################################

image airsupport_shrike_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_shrike_walk.png", (0, 216, 1272, 216)), (318, 216), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_shrike_walk_front:
    Fixed(anim.Filmstrip("battle/units/airsupport_shrike_walk.png", (318, 216), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_shrike_static_back:
    Fixed(im.Crop("battle/units/airsupport_shrike_walk.png", (0, 216, 318, 216), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_shrike_static_front:
    Fixed(im.Crop("battle/units/airsupport_shrike_walk.png", (0, 0, 318, 216), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_shrike_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_shrike_main1_attack.png", (0, 216, 1272, 216)), (318, 216), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_shrike_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/airsupport_shrike_main1_attack.png", (318, 216), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_shrike_main1_attack_finalframe_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_shrike_walk.png", (0, 216, 1272, 216)), (318, 216), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_shrike_main1_attack_finalframe_front:
    Fixed(anim.Filmstrip("battle/units/airsupport_shrike_walk.png", (318, 216), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_shrike_main2_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_shrike_main2_attack.png", (0, 216, 1272, 216)), (318, 216), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_shrike_main2_attack_front:
    Fixed(anim.Filmstrip("battle/units/airsupport_shrike_main2_attack.png", (318, 216), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_shrike_main2_attack_finalframe_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_shrike_walk.png", (0, 216, 1272, 216)), (318, 216), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_shrike_main2_attack_finalframe_front:
    Fixed(anim.Filmstrip("battle/units/airsupport_shrike_walk.png", (318, 216), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_shrike_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_shrike_walk.png", (0, 216, 1272, 216)), (318, 216), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)

image airsupport_shrike_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/airsupport_shrike_walk.png", (318, 216), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image airsupport_shrike_heal_finalframe_back:
    Fixed(im.Crop("battle/units/airsupport_shrike_walk.png", (0, 216, 318, 216), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_shrike_heal_finalframe_front:
    Fixed(im.Crop("battle/units/airsupport_shrike_walk.png", (0, 0, 318, 216), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#airsupport_snotfire
################################

image airsupport_snotfire_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_snotfire_walk.png", (0, 216, 1200, 216)), (300, 216), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_snotfire_walk_front:
    Fixed(anim.Filmstrip("battle/units/airsupport_snotfire_walk.png", (300, 216), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_snotfire_static_back:
    Fixed(im.Crop("battle/units/airsupport_snotfire_walk.png", (0, 216, 300, 216), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_snotfire_static_front:
    Fixed(im.Crop("battle/units/airsupport_snotfire_walk.png", (0, 0, 300, 216), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_snotfire_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_snotfire_main1_attack.png", (0, 216, 1200, 216)), (300, 216), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_snotfire_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/airsupport_snotfire_main1_attack.png", (300, 216), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_snotfire_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/airsupport_snotfire_main1_attack.png", (900, 216, 300, 216), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_snotfire_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/airsupport_snotfire_main1_attack.png", (900, 0, 300, 216), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_snotfire_main2_attack_back:
    contains:
        Fixed(At(anim.Filmstrip(im.Crop("battle/units/airsupport_snotfire_walk.png", (0, 216, 1200, 216)), (300, 216), (4, 1), .05, xalign=0.5, yalign=0.5), dive), xsize=840, ysize=840)

image airsupport_snotfire_main2_attack_front:
    contains:
        Fixed(At(anim.Filmstrip("battle/units/airsupport_snotfire_walk.png", (300, 216), (4, 1), .05, xalign=0.5, yalign=0.5), dive), xsize=840, ysize=840)
    
image airsupport_snotfire_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/airsupport_snotfire_walk.png", (0, 216, 300, 216), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_snotfire_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/airsupport_snotfire_walk.png", (0, 0, 300, 216), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_snotfire_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_snotfire_walk.png", (0, 216, 1200, 216)), (300, 216), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)

image airsupport_snotfire_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/airsupport_snotfire_walk.png", (300, 216), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image airsupport_snotfire_heal_finalframe_back:
    Fixed(im.Crop("battle/units/airsupport_snotfire_walk.png", (0, 216, 300, 216), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_snotfire_heal_finalframe_front:
    Fixed(im.Crop("battle/units/airsupport_snotfire_walk.png", (0, 0, 300, 216), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#airsupport_swallow
################################

image airsupport_swallow_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_swallow_walk.png", (0, 222, 1392, 222)), (348, 222), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_swallow_walk_front:
    Fixed(anim.Filmstrip("battle/units/airsupport_swallow_walk.png", (348, 222), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_swallow_static_back:
    Fixed(im.Crop("battle/units/airsupport_swallow_walk.png", (0, 222, 348, 222), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_swallow_static_front:
    Fixed(im.Crop("battle/units/airsupport_swallow_walk.png", (0, 0, 348, 222), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_swallow_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_swallow_main1_attack.png", (0, 222, 1392, 222)), (348, 222), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_swallow_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/airsupport_swallow_main1_attack.png", (348, 222), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_swallow_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/airsupport_swallow_main1_attack.png", (1044, 222, 348, 222), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_swallow_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/airsupport_swallow_main1_attack.png", (1044, 0, 348, 222), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_swallow_main2_attack_back:
    contains:
        "offensive_hurricane_back"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_swallow_walk.png", (0, 222, 1392, 222)), (348, 222), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_swallow_main2_attack_front:
    contains:
        "offensive_hurricane_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip("battle/units/airsupport_swallow_walk.png", (348, 222), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_swallow_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/airsupport_swallow_walk.png", (0, 222, 348, 222), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_swallow_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/airsupport_swallow_walk.png", (0, 0, 348, 222), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_swallow_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_swallow_walk.png", (0, 222, 1392, 222)), (348, 222), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)

image airsupport_swallow_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/airsupport_swallow_walk.png", (348, 222), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image airsupport_swallow_heal_finalframe_back:
    Fixed(im.Crop("battle/units/airsupport_swallow_walk.png", (0, 222, 348, 222), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_swallow_heal_finalframe_front:
    Fixed(im.Crop("battle/units/airsupport_swallow_walk.png", (0, 0, 348, 222), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#airsupport_yakovlev
################################

image airsupport_yakovlev_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_yakovlev_walk.png", (0, 216, 1200, 216)), (300, 216), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_yakovlev_walk_front:
    Fixed(anim.Filmstrip("battle/units/airsupport_yakovlev_walk.png", (300, 216), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_yakovlev_static_back:
    Fixed(im.Crop("battle/units/airsupport_yakovlev_walk.png", (0, 216, 300, 216), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_yakovlev_static_front:
    Fixed(im.Crop("battle/units/airsupport_yakovlev_walk.png", (0, 0, 300, 216), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_yakovlev_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_yakovlev_main1_attack.png", (0, 216, 1200, 216)), (300, 216), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_yakovlev_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/airsupport_yakovlev_main1_attack.png", (300, 216), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_yakovlev_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/airsupport_yakovlev_main1_attack.png", (900, 216, 300, 216), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_yakovlev_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/airsupport_yakovlev_main1_attack.png", (900, 0, 300, 216), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_yakovlev_main2_attack_back:
    contains:
        Fixed(At(anim.Filmstrip(im.Crop("battle/units/airsupport_yakovlev_walk.png", (0, 216, 1200, 216)), (300, 216), (4, 1), .05, xalign=0.5, yalign=0.5), dive), xsize=840, ysize=840)

image airsupport_yakovlev_main2_attack_front:
    contains:
        Fixed(At(anim.Filmstrip("battle/units/airsupport_yakovlev_walk.png", (300, 216), (4, 1), .05, xalign=0.5, yalign=0.5), dive), xsize=840, ysize=840)
    
image airsupport_yakovlev_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/airsupport_yakovlev_walk.png", (0, 216, 300, 216), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_yakovlev_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/airsupport_yakovlev_walk.png", (0, 0, 300, 216), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_yakovlev_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_yakovlev_walk.png", (0, 216, 1200, 216)), (300, 216), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)

image airsupport_yakovlev_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/airsupport_yakovlev_walk.png", (300, 216), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image airsupport_yakovlev_heal_finalframe_back:
    Fixed(im.Crop("battle/units/airsupport_yakovlev_walk.png", (0, 216, 300, 216), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_yakovlev_heal_finalframe_front:
    Fixed(im.Crop("battle/units/airsupport_yakovlev_walk.png", (0, 0, 300, 216), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#airsupport_zero
################################
    
image airsupport_zero_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/airsupport_zero_main1_attack.png", (0, 216, 1200, 216)), (300, 216), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_zero_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/airsupport_zero_main1_attack.png", (300, 216), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image airsupport_zero_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/airsupport_zero_main1_attack.png", (900, 216, 300, 216), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image airsupport_zero_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/airsupport_zero_main1_attack.png", (900, 0, 300, 216), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################################################
################################################################
################################################################
    #  SPEZIALGRUPPE  #
################################################################
################################################################
################################################################   
    
################################
#specialgroup_finbard_gunner_heer2
################################

image specialgroup_finbard_gunner_heer2_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_finbard_gunner_heer2_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_finbard_gunner_heer2_walk_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_finbard_gunner_heer2_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_finbard_gunner_heer2_static_back:
    Fixed(im.Crop("battle/units/specialgroup_finbard_gunner_heer2_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_finbard_gunner_heer2_static_front:
    Fixed(im.Crop("battle/units/specialgroup_finbard_gunner_heer2_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_finbard_gunner_heer2_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_finbard_gunner_heer2_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, xalign=0.51, yalign=0.5), xsize=840, ysize=840)

image specialgroup_finbard_gunner_heer2_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_finbard_gunner_heer2_main1_attack.png", (150, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_finbard_gunner_heer2_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_finbard_gunner_heer2_main1_attack.png", (300, 243, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_finbard_gunner_heer2_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_finbard_gunner_heer2_main1_attack.png", (300, 0, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_finbard_gunner_heer2_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_finbard_gunner_heer2_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_finbard_gunner_heer2_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/specialgroup_finbard_gunner_heer2_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image specialgroup_finbard_gunner_heer2_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_finbard_gunner_heer2_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_finbard_gunner_heer2_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_finbard_gunner_heer2_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_finbard_gunner_heer2_special2_attack_back:
    contains:
        "reaction_snow"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        "offensive_snowball_back"
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_finbard_gunner_heer2_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_finbard_gunner_heer2_special2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/specialgroup_finbard_gunner_heer2_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_snowball_front"
        xpos 170
    contains:
        "reaction_snow"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    
image specialgroup_finbard_gunner_heer2_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_finbard_gunner_heer2_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_finbard_gunner_heer2_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_finbard_gunner_heer2_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_finbard_gunner_heer2_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_finbard_gunner_heer2_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image specialgroup_finbard_gunner_heer2_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/specialgroup_finbard_gunner_heer2_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image specialgroup_finbard_gunner_heer2_heal_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_finbard_gunner_heer2_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_finbard_gunner_heer2_heal_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_finbard_gunner_heer2_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#specialgroup_finbard_marksman_heer2
################################

image specialgroup_finbard_marksman_heer2_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_finbard_marksman_heer2_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_finbard_marksman_heer2_walk_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_finbard_marksman_heer2_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_finbard_marksman_heer2_static_back:
    Fixed(im.Crop("battle/units/specialgroup_finbard_marksman_heer2_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_finbard_marksman_heer2_static_front:
    Fixed(im.Crop("battle/units/specialgroup_finbard_marksman_heer2_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_finbard_marksman_heer2_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_finbard_marksman_heer2_main1_attack.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .05, loop=False, xalign=0.51, yalign=0.5), xsize=840, ysize=840)

image specialgroup_finbard_marksman_heer2_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_finbard_marksman_heer2_main1_attack.png", (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_finbard_marksman_heer2_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_finbard_marksman_heer2_main1_attack.png", (513, 244.5, 171, 244.5), xalign=0.51, yalign=0.5), xsize=840, ysize=840)

image specialgroup_finbard_marksman_heer2_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_finbard_marksman_heer2_main1_attack.png", (513, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_finbard_marksman_heer2_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_finbard_marksman_heer2_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image specialgroup_finbard_marksman_heer2_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/specialgroup_finbard_marksman_heer2_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    
image specialgroup_finbard_marksman_heer2_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_finbard_marksman_heer2_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_finbard_marksman_heer2_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_finbard_marksman_heer2_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_finbard_marksman_heer2_heal_back:
    contains:
        "seal_heal"
        xpos 310
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_finbard_marksman_heer2_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image specialgroup_finbard_marksman_heer2_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/specialgroup_finbard_marksman_heer2_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image specialgroup_finbard_marksman_heer2_heal_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_finbard_marksman_heer2_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_finbard_marksman_heer2_heal_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_finbard_marksman_heer2_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#specialgroup_rumanum_gunner_heer7
################################

image specialgroup_rumanum_gunner_heer7_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_rumanum_gunner_heer7_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_rumanum_gunner_heer7_walk_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_rumanum_gunner_heer7_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_rumanum_gunner_heer7_static_back:
    Fixed(im.Crop("battle/units/specialgroup_rumanum_gunner_heer7_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_rumanum_gunner_heer7_static_front:
    Fixed(im.Crop("battle/units/specialgroup_rumanum_gunner_heer7_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image specialgroup_rumanum_gunner_heer7_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_rumanum_gunner_heer7_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_rumanum_gunner_heer7_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_rumanum_gunner_heer7_main1_attack.png", (150, 243), (3, 1), .05, xalign=0.49, yalign=0.5), xsize=840, ysize=840)

image specialgroup_rumanum_gunner_heer7_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_rumanum_gunner_heer7_main1_attack.png", (300, 243, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_rumanum_gunner_heer7_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_rumanum_gunner_heer7_main1_attack.png", (300, 0, 150, 243), xalign=0.49, yalign=0.5), xsize=840, ysize=840)
        
image specialgroup_rumanum_gunner_heer7_main2_attack_back:
    contains:
        "offensive_stielhandgranate_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_rumanum_gunner_heer7_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_rumanum_gunner_heer7_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/specialgroup_rumanum_gunner_heer7_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_stielhandgranate_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image specialgroup_rumanum_gunner_heer7_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_rumanum_gunner_heer7_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_rumanum_gunner_heer7_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_rumanum_gunner_heer7_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_rumanum_gunner_heer7_special1_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/specialgroup_rumanum_gunner_heer7_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .02, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image specialgroup_rumanum_gunner_heer7_special1_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/specialgroup_rumanum_gunner_heer7_walk.png", (126, 243), (4, 1), .02, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image specialgroup_rumanum_gunner_heer7_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_rumanum_gunner_heer7_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_rumanum_gunner_heer7_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_rumanum_gunner_heer7_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image specialgroup_rumanum_gunner_heer7_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_rumanum_gunner_heer7_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image specialgroup_rumanum_gunner_heer7_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/specialgroup_rumanum_gunner_heer7_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image specialgroup_rumanum_gunner_heer7_heal_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_rumanum_gunner_heer7_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_rumanum_gunner_heer7_heal_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_rumanum_gunner_heer7_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
################################
#specialgroup_rumanum_antitank_heer7
################################

image specialgroup_rumanum_antitank_heer7_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_rumanum_antitank_heer7_walk.png", (0, 243, 720, 243)), (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_rumanum_antitank_heer7_walk_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_rumanum_antitank_heer7_walk.png", (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_rumanum_antitank_heer7_static_back:
    Fixed(im.Crop("battle/units/specialgroup_rumanum_antitank_heer7_walk.png", (0, 243, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_rumanum_antitank_heer7_static_front:
    Fixed(im.Crop("battle/units/specialgroup_rumanum_antitank_heer7_walk.png", (0, 0, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_rumanum_antitank_heer7_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_rumanum_antitank_heer7_main1_attack.png", (0, 244.5, 717, 244.5)), (179.25, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_rumanum_antitank_heer7_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_rumanum_antitank_heer7_main1_attack.png", (179.25, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_rumanum_antitank_heer7_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_rumanum_antitank_heer7_main1_attack.png", (537.75, 244.5, 179.25, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_rumanum_antitank_heer7_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_rumanum_antitank_heer7_main1_attack.png", (537.75, 0, 179.25, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_rumanum_antitank_heer7_main2_attack_back:
    contains:
        "offensive_stielhandgranate_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_rumanum_antitank_heer7_walk.png", (0, 243, 720, 243)), (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image specialgroup_rumanum_antitank_heer7_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/specialgroup_rumanum_antitank_heer7_walk.png", (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_stielhandgranate_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    
image specialgroup_rumanum_antitank_heer7_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_rumanum_antitank_heer7_walk.png", (0, 243, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_rumanum_antitank_heer7_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_rumanum_antitank_heer7_walk.png", (0, 0, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_rumanum_antitank_heer7_special1_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/specialgroup_rumanum_antitank_heer7_walk.png", (0, 243, 720, 243)), (180, 243), (4, 1), .02, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)

image specialgroup_rumanum_antitank_heer7_special1_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/specialgroup_rumanum_antitank_heer7_walk.png", (180, 243), (4, 1), .02, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image specialgroup_rumanum_antitank_heer7_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_rumanum_antitank_heer7_walk.png", (0, 243, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_rumanum_antitank_heer7_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_rumanum_antitank_heer7_walk.png", (0, 0, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_rumanum_antitank_heer7_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_rumanum_antitank_heer7_walk.png", (0, 243, 720, 243)), (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image specialgroup_rumanum_antitank_heer7_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/specialgroup_rumanum_antitank_heer7_walk.png", (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image specialgroup_rumanum_antitank_heer7_heal_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_rumanum_antitank_heer7_walk.png", (0, 243, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_rumanum_antitank_heer7_heal_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_rumanum_antitank_heer7_walk.png", (0, 0, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#specialgroup_rumanum_cavalry_heer7
################################

image specialgroup_rumanum_cavalry_heer7_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_rumanum_cavalry_heer7_walk.png", (0, 243, 636, 243)), (159, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_rumanum_cavalry_heer7_walk_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_rumanum_cavalry_heer7_walk.png", (159, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_rumanum_cavalry_heer7_static_back:
    Fixed(im.Crop("battle/units/specialgroup_rumanum_cavalry_heer7_walk.png", (0, 243, 159, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_rumanum_cavalry_heer7_static_front:
    Fixed(im.Crop("battle/units/specialgroup_rumanum_cavalry_heer7_walk.png", (0, 0, 159, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 

image specialgroup_rumanum_cavalry_heer7_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_rumanum_cavalry_heer7_main1_attack.png", (0, 243, 1908, 243)), (159, 243), (12, 1), .07, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_rumanum_cavalry_heer7_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_rumanum_cavalry_heer7_main1_attack.png", (159, 243), (12, 1), .07, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_rumanum_cavalry_heer7_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_rumanum_cavalry_heer7_main1_attack.png", (0, 243, 159, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_rumanum_cavalry_heer7_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_rumanum_cavalry_heer7_main1_attack.png", (0, 0, 159, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_rumanum_cavalry_heer7_main2_attack_back:
    contains:
        "offensive_stielhandgranate_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_rumanum_cavalry_heer7_walk.png", (0, 243, 636, 243)), (159, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_rumanum_cavalry_heer7_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/specialgroup_rumanum_cavalry_heer7_walk.png", (159, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_stielhandgranate_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image specialgroup_rumanum_cavalry_heer7_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_rumanum_cavalry_heer7_walk.png", (0, 243, 159, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_rumanum_cavalry_heer7_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_rumanum_cavalry_heer7_walk.png", (0, 0, 159, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image specialgroup_rumanum_cavalry_heer7_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_rumanum_cavalry_heer7_walk.png", (0, 243, 636, 243)), (159, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image specialgroup_rumanum_cavalry_heer7_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/specialgroup_rumanum_cavalry_heer7_walk.png", (159, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image specialgroup_rumanum_cavalry_heer7_heal_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_rumanum_cavalry_heer7_walk.png", (0, 243, 159, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_rumanum_cavalry_heer7_heal_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_rumanum_cavalry_heer7_walk.png", (0, 0, 159, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
################################
#specialgroup_afrikaakorps_gunner_heer5
################################

image specialgroup_afrikaakorps_gunner_heer5_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_afrikaakorps_gunner_heer5_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_afrikaakorps_gunner_heer5_walk_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_afrikaakorps_gunner_heer5_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_afrikaakorps_gunner_heer5_static_back:
    Fixed(im.Crop("battle/units/specialgroup_afrikaakorps_gunner_heer5_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_afrikaakorps_gunner_heer5_static_front:
    Fixed(im.Crop("battle/units/specialgroup_afrikaakorps_gunner_heer5_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_afrikaakorps_gunner_heer5_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_afrikaakorps_gunner_heer5_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_afrikaakorps_gunner_heer5_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_afrikaakorps_gunner_heer5_main1_attack.png", (150, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_afrikaakorps_gunner_heer5_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_afrikaakorps_gunner_heer5_main1_attack.png", (300, 243, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_afrikaakorps_gunner_heer5_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_afrikaakorps_gunner_heer5_main1_attack.png", (300, 0, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_afrikaakorps_gunner_heer5_main2_attack_back:
    contains:
        "offensive_stielhandgranate_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_afrikaakorps_gunner_heer5_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_afrikaakorps_gunner_heer5_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/specialgroup_afrikaakorps_gunner_heer5_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_stielhandgranate_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image specialgroup_afrikaakorps_gunner_heer5_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_afrikaakorps_gunner_heer5_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_afrikaakorps_gunner_heer5_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_afrikaakorps_gunner_heer5_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_afrikaakorps_gunner_heer5_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_afrikaakorps_gunner_heer5_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image specialgroup_afrikaakorps_gunner_heer5_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/specialgroup_afrikaakorps_gunner_heer5_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image specialgroup_afrikaakorps_gunner_heer5_heal_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_afrikaakorps_gunner_heer5_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_afrikaakorps_gunner_heer5_heal_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_afrikaakorps_gunner_heer5_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#specialgroup_afrikaakorps_marksman_heer5
################################

image specialgroup_afrikaakorps_marksman_heer5_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_afrikaakorps_marksman_heer5_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_afrikaakorps_marksman_heer5_walk_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_afrikaakorps_marksman_heer5_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_afrikaakorps_marksman_heer5_static_back:
    Fixed(im.Crop("battle/units/specialgroup_afrikaakorps_marksman_heer5_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_afrikaakorps_marksman_heer5_static_front:
    Fixed(im.Crop("battle/units/specialgroup_afrikaakorps_marksman_heer5_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_afrikaakorps_marksman_heer5_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_afrikaakorps_marksman_heer5_main1_attack.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_afrikaakorps_marksman_heer5_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_afrikaakorps_marksman_heer5_main1_attack.png", (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_afrikaakorps_marksman_heer5_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_afrikaakorps_marksman_heer5_main1_attack.png", (513, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_afrikaakorps_marksman_heer5_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_afrikaakorps_marksman_heer5_main1_attack.png", (513, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_afrikaakorps_marksman_heer5_main2_attack_back:
    contains:
        "offensive_stielhandgranate_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_afrikaakorps_marksman_heer5_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image specialgroup_afrikaakorps_marksman_heer5_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/specialgroup_afrikaakorps_marksman_heer5_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_stielhandgranate_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    
image specialgroup_afrikaakorps_marksman_heer5_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_afrikaakorps_marksman_heer5_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_afrikaakorps_marksman_heer5_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_afrikaakorps_marksman_heer5_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_afrikaakorps_marksman_heer5_heal_back:
    contains:
        "seal_heal"
        xpos 310
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_afrikaakorps_marksman_heer5_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image specialgroup_afrikaakorps_marksman_heer5_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/specialgroup_afrikaakorps_marksman_heer5_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image specialgroup_afrikaakorps_marksman_heer5_heal_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_afrikaakorps_marksman_heer5_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_afrikaakorps_marksman_heer5_heal_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_afrikaakorps_marksman_heer5_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#specialgroup_afrikaakorps_antitank_heer5
################################

image specialgroup_afrikaakorps_antitank_heer5_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_afrikaakorps_antitank_heer5_walk.png", (0, 243, 684, 243)), (171, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_afrikaakorps_antitank_heer5_walk_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_afrikaakorps_antitank_heer5_walk.png", (171, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_afrikaakorps_antitank_heer5_static_back:
    Fixed(im.Crop("battle/units/specialgroup_afrikaakorps_antitank_heer5_walk.png", (0, 243, 171, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_afrikaakorps_antitank_heer5_static_front:
    Fixed(im.Crop("battle/units/specialgroup_afrikaakorps_antitank_heer5_walk.png", (0, 0, 171, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_afrikaakorps_antitank_heer5_main1_attack_back:
    contains:
        "offensive_launcherblast_back"
        xpos 600
        ypos 220
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_afrikaakorps_antitank_heer5_main1_attack.png", (0, 244.5, 717, 244.5)), (179.25, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_afrikaakorps_antitank_heer5_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/specialgroup_afrikaakorps_antitank_heer5_main1_attack.png", (179.25, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_launcherblast_front"
        xpos 160
        ypos 300

image specialgroup_afrikaakorps_antitank_heer5_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_afrikaakorps_antitank_heer5_main1_attack.png", (537.75, 244.5, 179.25, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_afrikaakorps_antitank_heer5_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_afrikaakorps_antitank_heer5_main1_attack.png", (537.75, 0, 179.25, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_afrikaakorps_antitank_heer5_main2_attack_back:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_afrikaakorps_antitank_heer5_walk.png", (0, 243, 684, 243)), (171, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_landmine"
        xalign 0.77 yalign -0.6
        
image specialgroup_afrikaakorps_antitank_heer5_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/specialgroup_afrikaakorps_antitank_heer5_walk.png", (171, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_landmine"
        xalign -0.6 yalign 0.52
    
image specialgroup_afrikaakorps_antitank_heer5_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_afrikaakorps_antitank_heer5_walk.png", (0, 243, 171, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_afrikaakorps_antitank_heer5_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_afrikaakorps_antitank_heer5_walk.png", (0, 0, 171, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_afrikaakorps_antitank_heer5_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_afrikaakorps_antitank_heer5_walk.png", (0, 243, 684, 243)), (171, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image specialgroup_afrikaakorps_antitank_heer5_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
       At(Fixed(anim.Filmstrip("battle/units/specialgroup_afrikaakorps_antitank_heer5_walk.png", (171, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image specialgroup_afrikaakorps_antitank_heer5_heal_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_afrikaakorps_antitank_heer5_walk.png", (0, 243, 171, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_afrikaakorps_antitank_heer5_heal_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_afrikaakorps_antitank_heer5_walk.png", (0, 0, 171, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#specialgroup_vitalia_gunner_heer3
################################

image specialgroup_vitalia_gunner_heer3_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_vitalia_gunner_heer3_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_vitalia_gunner_heer3_walk_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_vitalia_gunner_heer3_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_vitalia_gunner_heer3_static_back:
    Fixed(im.Crop("battle/units/specialgroup_vitalia_gunner_heer3_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_vitalia_gunner_heer3_static_front:
    Fixed(im.Crop("battle/units/specialgroup_vitalia_gunner_heer3_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_vitalia_gunner_heer3_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_vitalia_gunner_heer3_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, xalign=0.52, yalign=0.505), xsize=840, ysize=840)

image specialgroup_vitalia_gunner_heer3_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_vitalia_gunner_heer3_main1_attack.png", (150, 243), (3, 1), .05, xalign=0.49, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_vitalia_gunner_heer3_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_vitalia_gunner_heer3_main1_attack.png", (300, 243, 150, 243), xalign=0.52, yalign=0.505), xsize=840, ysize=840)

image specialgroup_vitalia_gunner_heer3_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_vitalia_gunner_heer3_main1_attack.png", (300, 0, 150, 243), xalign=0.49, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_vitalia_gunner_heer3_main2_attack_back:
    contains:
        "offensive_stielhandgranate_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_vitalia_gunner_heer3_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_vitalia_gunner_heer3_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/specialgroup_vitalia_gunner_heer3_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_stielhandgranate_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image specialgroup_vitalia_gunner_heer3_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_vitalia_gunner_heer3_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_vitalia_gunner_heer3_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_vitalia_gunner_heer3_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_vitalia_gunner_heer3_special1_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/specialgroup_vitalia_gunner_heer3_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .02, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)

image specialgroup_vitalia_gunner_heer3_special1_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/specialgroup_vitalia_gunner_heer3_walk.png", (126, 243), (4, 1), .02, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image specialgroup_vitalia_gunner_heer3_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_vitalia_gunner_heer3_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_vitalia_gunner_heer3_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_vitalia_gunner_heer3_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_vitalia_gunner_heer3_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_vitalia_gunner_heer3_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image specialgroup_vitalia_gunner_heer3_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/specialgroup_vitalia_gunner_heer3_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image specialgroup_vitalia_gunner_heer3_heal_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_vitalia_gunner_heer3_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_vitalia_gunner_heer3_heal_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_vitalia_gunner_heer3_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#specialgroup_vitalia_marksman_heer3
################################

image specialgroup_vitalia_marksman_heer3_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_vitalia_marksman_heer3_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_vitalia_marksman_heer3_walk_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_vitalia_marksman_heer3_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_vitalia_marksman_heer3_static_back:
    Fixed(im.Crop("battle/units/specialgroup_vitalia_marksman_heer3_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_vitalia_marksman_heer3_static_front:
    Fixed(im.Crop("battle/units/specialgroup_vitalia_marksman_heer3_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_vitalia_marksman_heer3_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_vitalia_marksman_heer3_main1_attack.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_vitalia_marksman_heer3_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_vitalia_marksman_heer3_main1_attack.png", (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_vitalia_marksman_heer3_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_vitalia_marksman_heer3_main1_attack.png", (513, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_vitalia_marksman_heer3_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_vitalia_marksman_heer3_main1_attack.png", (513, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_vitalia_marksman_heer3_main2_attack_back:
    contains:
        "offensive_stielhandgranate_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_vitalia_marksman_heer3_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image specialgroup_vitalia_marksman_heer3_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/specialgroup_vitalia_marksman_heer3_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_stielhandgranate_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    
image specialgroup_vitalia_marksman_heer3_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_vitalia_marksman_heer3_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_vitalia_marksman_heer3_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_vitalia_marksman_heer3_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_vitalia_marksman_heer3_heal_back:
    contains:
        "seal_heal"
        xpos 300
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_vitalia_marksman_heer3_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image specialgroup_vitalia_marksman_heer3_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/specialgroup_vitalia_marksman_heer3_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image specialgroup_vitalia_marksman_heer3_heal_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_vitalia_marksman_heer3_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_vitalia_marksman_heer3_heal_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_vitalia_marksman_heer3_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#specialgroup_vitalia_frogman_heer5
################################

image specialgroup_vitalia_frogman_heer5_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_vitalia_frogman_heer5_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_vitalia_frogman_heer5_walk_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_vitalia_frogman_heer5_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_vitalia_frogman_heer5_static_back:
    Fixed(im.Crop("battle/units/specialgroup_vitalia_frogman_heer5_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_vitalia_frogman_heer5_static_front:
    Fixed(im.Crop("battle/units/specialgroup_vitalia_frogman_heer5_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_vitalia_frogman_heer5_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_vitalia_frogman_heer5_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_vitalia_frogman_heer5_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_vitalia_frogman_heer5_main1_attack.png", (150, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_vitalia_frogman_heer5_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_vitalia_frogman_heer5_main1_attack.png", (300, 243, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_vitalia_frogman_heer5_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_vitalia_frogman_heer5_main1_attack.png", (300, 0, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_vitalia_frogman_heer5_main2_attack_back:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_vitalia_frogman_heer5_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_landmine"
        xalign 0.77 yalign -0.6

image specialgroup_vitalia_frogman_heer5_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/specialgroup_vitalia_frogman_heer5_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_landmine"
        xalign -0.6 yalign 0.52
        
image specialgroup_vitalia_frogman_heer5_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_vitalia_frogman_heer5_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_vitalia_frogman_heer5_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_vitalia_frogman_heer5_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_vitalia_frogman_heer5_special1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_vitalia_frogman_heer5_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_vitalia_frogman_heer5_special1_attack_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_vitalia_frogman_heer5_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_vitalia_frogman_heer5_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_vitalia_frogman_heer5_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_vitalia_frogman_heer5_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_vitalia_frogman_heer5_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_vitalia_frogman_heer5_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_vitalia_frogman_heer5_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image specialgroup_vitalia_frogman_heer5_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/specialgroup_vitalia_frogman_heer5_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image specialgroup_vitalia_frogman_heer5_heal_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_vitalia_frogman_heer5_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_vitalia_frogman_heer5_heal_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_vitalia_frogman_heer5_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#specialgroup_zipangu_gunner_heer1
################################

image specialgroup_zipangu_gunner_heer1_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_zipangu_gunner_heer1_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_zipangu_gunner_heer1_walk_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_zipangu_gunner_heer1_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_zipangu_gunner_heer1_static_back:
    Fixed(im.Crop("battle/units/specialgroup_zipangu_gunner_heer1_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_zipangu_gunner_heer1_static_front:
    Fixed(im.Crop("battle/units/specialgroup_zipangu_gunner_heer1_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_zipangu_gunner_heer1_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_zipangu_gunner_heer1_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_zipangu_gunner_heer1_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_zipangu_gunner_heer1_main1_attack.png", (150, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_zipangu_gunner_heer1_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_zipangu_gunner_heer1_main1_attack.png", (300, 243, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_zipangu_gunner_heer1_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_zipangu_gunner_heer1_main1_attack.png", (300, 0, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_zipangu_gunner_heer1_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_zipangu_gunner_heer1_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_zipangu_gunner_heer1_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/specialgroup_zipangu_gunner_heer1_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image specialgroup_zipangu_gunner_heer1_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_zipangu_gunner_heer1_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_zipangu_gunner_heer1_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_zipangu_gunner_heer1_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_zipangu_gunner_heer1_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_zipangu_gunner_heer1_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image specialgroup_zipangu_gunner_heer1_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/specialgroup_zipangu_gunner_heer1_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image specialgroup_zipangu_gunner_heer1_heal_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_zipangu_gunner_heer1_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_zipangu_gunner_heer1_heal_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_zipangu_gunner_heer1_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#specialgroup_zipangu_marksman_heer1
################################

image specialgroup_zipangu_marksman_heer1_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_zipangu_marksman_heer1_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_zipangu_marksman_heer1_walk_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_zipangu_marksman_heer1_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_zipangu_marksman_heer1_static_back:
    Fixed(im.Crop("battle/units/specialgroup_zipangu_marksman_heer1_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_zipangu_marksman_heer1_static_front:
    Fixed(im.Crop("battle/units/specialgroup_zipangu_marksman_heer1_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_zipangu_marksman_heer1_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_zipangu_marksman_heer1_main1_attack.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_zipangu_marksman_heer1_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_zipangu_marksman_heer1_main1_attack.png", (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_zipangu_marksman_heer1_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_zipangu_marksman_heer1_main1_attack.png", (513, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_zipangu_marksman_heer1_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_zipangu_marksman_heer1_main1_attack.png", (513, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_zipangu_marksman_heer1_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_zipangu_marksman_heer1_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image specialgroup_zipangu_marksman_heer1_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/specialgroup_zipangu_marksman_heer1_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    
image specialgroup_zipangu_marksman_heer1_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_zipangu_marksman_heer1_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_zipangu_marksman_heer1_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_zipangu_marksman_heer1_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_zipangu_marksman_heer1_heal_back:
    contains:
        "seal_heal"
        xpos 300
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_zipangu_marksman_heer1_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image specialgroup_zipangu_marksman_heer1_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/specialgroup_zipangu_marksman_heer1_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image specialgroup_zipangu_marksman_heer1_heal_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_zipangu_marksman_heer1_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_zipangu_marksman_heer1_heal_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_zipangu_marksman_heer1_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#specialgroup_nord_gunner_heer2
################################

image specialgroup_nord_gunner_heer2_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_nord_gunner_heer2_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_nord_gunner_heer2_walk_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_nord_gunner_heer2_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_nord_gunner_heer2_static_back:
    Fixed(im.Crop("battle/units/specialgroup_nord_gunner_heer2_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_nord_gunner_heer2_static_front:
    Fixed(im.Crop("battle/units/specialgroup_nord_gunner_heer2_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_nord_gunner_heer2_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_nord_gunner_heer2_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_nord_gunner_heer2_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_nord_gunner_heer2_main1_attack.png", (150, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_nord_gunner_heer2_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_nord_gunner_heer2_main1_attack.png", (300, 243, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_nord_gunner_heer2_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_nord_gunner_heer2_main1_attack.png", (300, 0, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_nord_gunner_heer2_main2_attack_back:
    contains:
        "offensive_stielhandgranate_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_nord_gunner_heer2_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_nord_gunner_heer2_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/specialgroup_nord_gunner_heer2_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_stielhandgranate_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image specialgroup_nord_gunner_heer2_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_nord_gunner_heer2_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_nord_gunner_heer2_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_nord_gunner_heer2_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_nord_gunner_heer2_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_nord_gunner_heer2_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image specialgroup_nord_gunner_heer2_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/specialgroup_nord_gunner_heer2_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image specialgroup_nord_gunner_heer2_heal_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_nord_gunner_heer2_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_nord_gunner_heer2_heal_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_nord_gunner_heer2_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#specialgroup_nord_marksman_heer2
################################

image specialgroup_nord_marksman_heer2_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_nord_marksman_heer2_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_nord_marksman_heer2_walk_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_nord_marksman_heer2_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_nord_marksman_heer2_static_back:
    Fixed(im.Crop("battle/units/specialgroup_nord_marksman_heer2_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_nord_marksman_heer2_static_front:
    Fixed(im.Crop("battle/units/specialgroup_nord_marksman_heer2_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_nord_marksman_heer2_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_nord_marksman_heer2_main1_attack.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_nord_marksman_heer2_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_nord_marksman_heer2_main1_attack.png", (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_nord_marksman_heer2_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_nord_marksman_heer2_main1_attack.png", (513, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_nord_marksman_heer2_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_nord_marksman_heer2_main1_attack.png", (513, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_nord_marksman_heer2_main2_attack_back:
    contains:
        "offensive_stielhandgranate_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_nord_marksman_heer2_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image specialgroup_nord_marksman_heer2_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/specialgroup_nord_marksman_heer2_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_stielhandgranate_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    
image specialgroup_nord_marksman_heer2_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_nord_marksman_heer2_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_nord_marksman_heer2_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_nord_marksman_heer2_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_nord_marksman_heer2_heal_back:
    contains:
        "seal_heal"
        xpos 310
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_nord_marksman_heer2_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image specialgroup_nord_marksman_heer2_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/specialgroup_nord_marksman_heer2_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image specialgroup_nord_marksman_heer2_heal_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_nord_marksman_heer2_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_nord_marksman_heer2_heal_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_nord_marksman_heer2_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
##################################
#specialgroup_nord_antitank_heer2
##################################

image specialgroup_nord_antitank_heer2_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_nord_antitank_heer2_walk.png", (0, 243, 684, 243)), (171, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_nord_antitank_heer2_walk_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_nord_antitank_heer2_walk.png", (171, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_nord_antitank_heer2_static_back:
    Fixed(im.Crop("battle/units/specialgroup_nord_antitank_heer2_walk.png", (0, 243, 171, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_nord_antitank_heer2_static_front:
    Fixed(im.Crop("battle/units/specialgroup_nord_antitank_heer2_walk.png", (0, 0, 171, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_nord_antitank_heer2_main1_attack_back:
    contains:
        "offensive_launcherblast_back"
        xpos 600
        ypos 220
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_nord_antitank_heer2_main1_attack.png", (0, 244.5, 717, 244.5)), (179.25, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_nord_antitank_heer2_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/specialgroup_nord_antitank_heer2_main1_attack.png", (179.25, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_launcherblast_front"
        xpos 160
        ypos 300

image specialgroup_nord_antitank_heer2_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_nord_antitank_heer2_main1_attack.png", (537.75, 244.5, 179.25, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_nord_antitank_heer2_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_nord_antitank_heer2_main1_attack.png", (537.75, 0, 179.25, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_nord_antitank_heer2_main2_attack_back:
    contains:
        "offensive_stielhandgranate_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_nord_antitank_heer2_walk.png", (0, 243, 684, 243)), (171, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image specialgroup_nord_antitank_heer2_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/specialgroup_nord_antitank_heer2_walk.png", (171, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_stielhandgranate_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    
image specialgroup_nord_antitank_heer2_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_nord_antitank_heer2_walk.png", (0, 243, 171, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_nord_antitank_heer2_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_nord_antitank_heer2_walk.png", (0, 0, 171, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_nord_antitank_heer2_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_nord_antitank_heer2_walk.png", (0, 243, 684, 243)), (171, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image specialgroup_nord_antitank_heer2_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/specialgroup_nord_antitank_heer2_walk.png", (171, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image specialgroup_nord_antitank_heer2_heal_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_nord_antitank_heer2_walk.png", (0, 243, 171, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_nord_antitank_heer2_heal_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_nord_antitank_heer2_walk.png", (0, 0, 171, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

################################
#specialgroup_uboatcosplay_heer6
################################

image specialgroup_uboatcosplay_heer6_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_uboatcosplay_heer6_walk.png", (0, 243, 1788, 243)), (447, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_uboatcosplay_heer6_walk_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_uboatcosplay_heer6_walk.png", (447, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_uboatcosplay_heer6_static_back:
    Fixed(im.Crop("battle/units/specialgroup_uboatcosplay_heer6_walk.png", (0, 243, 447, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_uboatcosplay_heer6_static_front:
    Fixed(im.Crop("battle/units/specialgroup_uboatcosplay_heer6_walk.png", (0, 0, 447, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_uboatcosplay_heer6_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_uboatcosplay_heer6_main1_attack.png", (0, 243, 5364, 243)), (447, 243), (12, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_uboatcosplay_heer6_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_uboatcosplay_heer6_main1_attack.png", (447, 243), (12, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_uboatcosplay_heer6_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_uboatcosplay_heer6_main1_attack.png", (4917, 243, 447, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_uboatcosplay_heer6_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_uboatcosplay_heer6_main1_attack.png", (4917, 0, 447, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_uboatcosplay_heer6_main2_attack_back:
    contains:
        "offensive_stielhandgranate_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_uboatcosplay_heer6_walk.png", (0, 243, 1788, 243)), (447, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_uboatcosplay_heer6_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/specialgroup_uboatcosplay_heer6_walk.png", (447, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_stielhandgranate_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image specialgroup_uboatcosplay_heer6_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_uboatcosplay_heer6_walk.png", (0, 243, 447, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_uboatcosplay_heer6_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_uboatcosplay_heer6_walk.png", (0, 0, 447, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_uboatcosplay_heer6_special1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_uboatcosplay_heer6_walk.png", (0, 243, 1788, 243)), (447, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_uboatcosplay_heer6_special1_attack_front:
    Fixed(anim.Filmstrip("battle/units/specialgroup_uboatcosplay_heer6_walk.png", (447, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_uboatcosplay_heer6_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_uboatcosplay_heer6_walk.png", (0, 243, 447, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_uboatcosplay_heer6_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_uboatcosplay_heer6_walk.png", (0, 0, 447, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image specialgroup_uboatcosplay_heer6_heal_back:
    contains:
        "seal_heal"
        xpos 290
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/specialgroup_uboatcosplay_heer6_walk.png", (0, 243, 1788, 243)), (447, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image specialgroup_uboatcosplay_heer6_heal_front:
    contains:
        "seal_heal"
        xpos 290
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/specialgroup_uboatcosplay_heer6_walk.png", (447, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image specialgroup_uboatcosplay_heer6_heal_finalframe_back:
    Fixed(im.Crop("battle/units/specialgroup_uboatcosplay_heer6_walk.png", (0, 243, 447, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image specialgroup_uboatcosplay_heer6_heal_finalframe_front:
    Fixed(im.Crop("battle/units/specialgroup_uboatcosplay_heer6_walk.png", (0, 0, 447, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
    
################################################################
################################################################
################################################################
    #  TANKS  #
################################################################
################################################################
################################################################
    
################################
#panzer_7tp
################################

image panzer_7tp_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_7tp_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_7tp_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_7tp_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_7tp_static_back:
    Fixed(im.Crop("battle/units/panzer_7tp_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_7tp_static_front:
    Fixed(im.Crop("battle/units/panzer_7tp_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_7tp_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 710
        ypos 65
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_7tp_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_7tp_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_7tp_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 160
        ypos 280

image panzer_7tp_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_7tp_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_7tp_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_7tp_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_7tp_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_7tp_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_7tp_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_7tp_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_7tp_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_7tp_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_7tp_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_7tp_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_7tp_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_7tp_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megaspeed", xsize=840, ysize=840)
    
image panzer_7tp_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_7tp_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megaspeed", xsize=840, ysize=840)
    
image panzer_7tp_main1_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_7tp_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_7tp_main1_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_7tp_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_7tp_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_7tp_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_7tp_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_7tp_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_7tp_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_7tp_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_7tp_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_7tp_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_47mmapx
################################

image panzer_47mmapx_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_47mmapx_walk.png", (0, 321, 1404, 321)), (468, 321), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_47mmapx_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_47mmapx_walk.png", (468, 321), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_47mmapx_static_back:
    Fixed(im.Crop("battle/units/panzer_47mmapx_walk.png", (0, 321, 468, 321), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_47mmapx_static_front:
    Fixed(im.Crop("battle/units/panzer_47mmapx_walk.png", (0, 0, 468, 321), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_47mmapx_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_47mmapx_main1_attack.png", (0, 321, 3276, 321)), (468, 321), (7, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_47mmapx_main1_attack_front:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_47mmapx_main1_attack.png", (0, 0, 3276, 321)), (468, 321), (7, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image panzer_47mmapx_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_47mmapx_main1_attack.png", (2808, 321, 468, 321), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_47mmapx_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_47mmapx_main1_attack.png", (2808, 0, 468, 321), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_47mmapx_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_47mmapx_walk.png", (0, 321, 1404, 321)), (468, 321), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_47mmapx_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_47mmapx_walk.png", (468, 321), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_47mmapx_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_47mmapx_walk.png", (0, 321, 468, 321), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_47mmapx_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_47mmapx_walk.png", (0, 0, 468, 321), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_archer
################################

image panzer_archer_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_archer_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_archer_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_archer_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_archer_static_back:
    Fixed(im.Crop("battle/units/panzer_archer_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_archer_static_front:
    Fixed(im.Crop("battle/units/panzer_archer_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_archer_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 880
        ypos 30
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_archer_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_archer_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_archer_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 0
        ypos 400

image panzer_archer_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_archer_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_archer_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_archer_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_archer_main2_attack_back:
    contains:
        Fixed(im.Crop("battle/units/panzer_archer_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_back"
        xpos 485
        ypos 340
    
image panzer_archer_main2_attack_front:
    contains:
        Fixed(im.Crop("battle/units/panzer_archer_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 425
        ypos 370
    
image panzer_archer_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_archer_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_archer_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_archer_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_archer_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_archer_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megapower", xsize=840, ysize=840)
    
image panzer_archer_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_archer_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megapower", xsize=840, ysize=840)
    
image panzer_archer_main1_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_archer_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_archer_main1_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_archer_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_archer_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_archer_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_archer_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_archer_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_archer_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_archer_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_archer_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_archer_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_ba10
################################

image panzer_ba10_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_ba10_walk.png", (0, 309, 1620, 309)), (405, 309), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_ba10_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_ba10_walk.png", (405, 309), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_ba10_static_back:
    Fixed(im.Crop("battle/units/panzer_ba10_walk.png", (0, 309, 405, 309), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_ba10_static_front:
    Fixed(im.Crop("battle/units/panzer_ba10_walk.png", (0, 0, 405, 309), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_ba10_main1_attack_back:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_ba10_main1_attack.png", (0, 309, 1620, 309)), (405, 309), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_smallcannonblast_back"
        xpos 465
        ypos 285
        
image panzer_ba10_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_ba10_main1_attack.png", (0, 0, 1620, 309)), (405, 309), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_smallcannonblast_front"
        xpos 355
        ypos 335

image panzer_ba10_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_ba10_main1_attack.png", (1215, 309, 405, 309), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_ba10_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_ba10_main1_attack.png", (1215, 0, 405, 309), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_ba10_main2_attack_back:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_ba10_main1_attack.png", (0, 309, 1620, 309)), (405, 309), (4, 1), .01, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_back"
        xpos 430
        ypos 330
        
image panzer_ba10_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_ba10_main1_attack.png", (0, 0, 1620, 309)), (405, 309), (4, 1), .01, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 401
        ypos 401

image panzer_ba10_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_ba10_main1_attack.png", (1215, 309, 405, 309), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_ba10_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_ba10_main1_attack.png", (1215, 0, 405, 309), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_ba10_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_ba10_walk.png", (0, 309, 1620, 309)), (405, 309), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_ba10_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_ba10_walk.png", (405, 309), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_ba10_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_ba10_walk.png", (0, 309, 405, 309), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_ba10_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_ba10_walk.png", (0, 0, 405, 309), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#antitank_sdkfz250
################################

image antitank_sdkfz250_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_sdkfz250_walk.png", (0, 294, 1584, 294)), (396, 294), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_sdkfz250_walk_front:
    Fixed(anim.Filmstrip("battle/units/antitank_sdkfz250_walk.png", (396, 294), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_sdkfz250_static_back:
    Fixed(im.Crop("battle/units/antitank_sdkfz250_walk.png", (0, 294, 396, 294), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_sdkfz250_static_front:
    Fixed(im.Crop("battle/units/antitank_sdkfz250_walk.png", (0, 0, 396, 294), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_sdkfz250_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_sdkfz250_main1_attack.png", (0, 351, 2772, 351)), (396, 351), (7, 1), .05, loop=False, xalign=0.5, yalign=0.442), xsize=840, ysize=840)
        
image antitank_sdkfz250_main1_attack_front:
    Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_sdkfz250_main1_attack.png", (0, 0, 2772, 351)), (396, 351), (7, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image antitank_sdkfz250_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/antitank_sdkfz250_main1_attack.png", (2376, 351, 396, 351), xalign=0.5, yalign=0.442), xsize=840, ysize=840)
    
image antitank_sdkfz250_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/antitank_sdkfz250_main1_attack.png", (2376, 0, 396, 351), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_sdkfz250_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_sdkfz250_walk.png", (0, 294, 1584, 294)), (396, 294), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image antitank_sdkfz250_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/antitank_sdkfz250_walk.png", (396, 294), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image antitank_sdkfz250_heal_finalframe_back:
    Fixed(im.Crop("battle/units/antitank_sdkfz250_walk.png", (0, 294, 396, 294), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_sdkfz250_heal_finalframe_front:
    Fixed(im.Crop("battle/units/antitank_sdkfz250_walk.png", (0, 0, 396, 294), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_bishopsph
################################

image panzer_bishopsph_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_bishopsph_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_bishopsph_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_bishopsph_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_bishopsph_static_back:
    Fixed(im.Crop("battle/units/panzer_bishopsph_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_bishopsph_static_front:
    Fixed(im.Crop("battle/units/panzer_bishopsph_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_bishopsph_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 720
        ypos 100
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_bishopsph_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_bishopsph_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_bishopsph_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 180
        ypos 320

image panzer_bishopsph_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_bishopsph_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_bishopsph_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_bishopsph_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_bishopsph_special1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_bishopsph_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_bishopsph_special1_attack_front:
    Fixed(anim.Filmstrip("battle/units/panzer_bishopsph_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_bishopsph_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_bishopsph_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_bishopsph_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_bishopsph_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_bishopsph_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_bishopsph_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megapower", xsize=840, ysize=840)
    
image panzer_bishopsph_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_bishopsph_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megapower", xsize=840, ysize=840)
    
image panzer_bishopsph_main1_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_bishopsph_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_bishopsph_main1_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_bishopsph_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_bishopsph_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_bishopsph_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_bishopsph_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_bishopsph_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_bishopsph_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_bishopsph_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_bishopsph_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_bishopsph_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_braatovervalwagen
################################

image panzer_braatovervalwagen_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_braatovervalwagen_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_braatovervalwagen_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_braatovervalwagen_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_braatovervalwagen_static_back:
    Fixed(im.Crop("battle/units/panzer_braatovervalwagen_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_braatovervalwagen_static_front:
    Fixed(im.Crop("battle/units/panzer_braatovervalwagen_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_braatovervalwagen_main1_attack_back:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_braatovervalwagen_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .03, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_back"
        xpos 605
        ypos 240
        
image panzer_braatovervalwagen_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_braatovervalwagen_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .03, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 280
        ypos 400

image panzer_braatovervalwagen_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_braatovervalwagen_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_braatovervalwagen_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_braatovervalwagen_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_braatovervalwagen_main2_attack_back:
    contains:
        "offensive_gunfire_big_back"
        xpos 550
        ypos 290
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_braatovervalwagen_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_braatovervalwagen_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_braatovervalwagen_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_big_front"
        xpos 225
        ypos 445
    
image panzer_braatovervalwagen_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_braatovervalwagen_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_braatovervalwagen_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_braatovervalwagen_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)    
    
image panzer_braatovervalwagen_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_braatovervalwagen_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_braatovervalwagen_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_braatovervalwagen_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_braatovervalwagen_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_braatovervalwagen_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_braatovervalwagen_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_braatovervalwagen_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_bt42
################################

image panzer_bt42_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_bt42_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_bt42_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_bt42_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_bt42_static_back:
    Fixed(im.Crop("battle/units/panzer_bt42_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_bt42_static_front:
    Fixed(im.Crop("battle/units/panzer_bt42_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_bt42_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 710
        ypos 80
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_bt42_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_bt42_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_bt42_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 170
        ypos 290

image panzer_bt42_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_bt42_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_bt42_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_bt42_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image panzer_bt42_special1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_bt42_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_bt42_special1_attack_front:
    Fixed(anim.Filmstrip("battle/units/panzer_bt42_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_bt42_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_bt42_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_bt42_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_bt42_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_bt42_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_bt42_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_bt42_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_bt42_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_bt42_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_bt42_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_bt42_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_bt42_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_bt42_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_bt42_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megapower", xsize=840, ysize=840)
    
image panzer_bt42_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_bt42_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megapower", xsize=840, ysize=840)
    
image panzer_bt42_main1_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_bt42_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_bt42_main1_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_bt42_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_bt42_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_bt42_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_bt42_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_bt42_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_bt42_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_bt42_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_bt42_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_bt42_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_carroarmato
################################

image panzer_carroarmato_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_carroarmato_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_carroarmato_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_carroarmato_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_carroarmato_static_back:
    Fixed(im.Crop("battle/units/panzer_carroarmato_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_carroarmato_static_front:
    Fixed(im.Crop("battle/units/panzer_carroarmato_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_carroarmato_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 730
        ypos 60
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_carroarmato_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_carroarmato_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_carroarmato_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 150
        ypos 300

image panzer_carroarmato_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_carroarmato_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_carroarmato_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_carroarmato_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_carroarmato_main2_attack_back:
    contains:
        "offensive_gunfire_back"
        xpos 550
        ypos 290
    contains:
        "offensive_gunfire_back"
        xpos 510
        ypos 235
    contains:
        Fixed(im.Crop("battle/units/panzer_carroarmato_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_carroarmato_main2_attack_front:
    contains:
        Fixed(im.Crop("battle/units/panzer_carroarmato_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 225
        ypos 445
    contains:
        "offensive_gunfire_front"
        xpos 338
        ypos 320
    
image panzer_carroarmato_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_carroarmato_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_carroarmato_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_carroarmato_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_carroarmato_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_carroarmato_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megaspeed", xsize=840, ysize=840)
    
image panzer_carroarmato_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_carroarmato_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megaspeed", xsize=840, ysize=840)
    
image panzer_carroarmato_main1_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_carroarmato_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_carroarmato_main1_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_carroarmato_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_carroarmato_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_carroarmato_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_carroarmato_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_carroarmato_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_carroarmato_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_carroarmato_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_carroarmato_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_carroarmato_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_charb1
################################

image panzer_charb1_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_charb1_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_charb1_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_charb1_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=800)
    
image panzer_charb1_static_back:
    Fixed(im.Crop("battle/units/panzer_charb1_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_charb1_static_front:
    Fixed(im.Crop("battle/units/panzer_charb1_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=800)
    
image panzer_charb1_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 760
        ypos 80
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_charb1_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_charb1_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_charb1_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=800)
    contains:
        "offensive_cannonblast_front"
        xpos 80
        ypos 330

image panzer_charb1_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_charb1_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_charb1_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_charb1_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=800)
        
image panzer_charb1_main2_attack_back:
    contains:
        "offensive_smallcannonblast_back"
        xpos 590
        ypos 290
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_charb1_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_charb1_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_charb1_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=800)
    contains:
        "offensive_smallcannonblast_front"
        xpos 183
        ypos 458
    
image panzer_charb1_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_charb1_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_charb1_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_charb1_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=800)
    
image panzer_charb1_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_charb1_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megaspeed", xsize=840, ysize=840)
    
image panzer_charb1_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 410
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_charb1_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=800), boost_white)
    contains:
        Fixed("reaction_powerup_megaspeed", xsize=840, ysize=800)
    
image panzer_charb1_main1_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_charb1_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_charb1_main1_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_charb1_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=800)
    
image panzer_charb1_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_charb1_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_charb1_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_charb1_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=800), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=800)
    
image panzer_charb1_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_charb1_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_charb1_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_charb1_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=800)
    
################################
#panzer_charfcm
################################

image panzer_charfcm_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_charfcm_walk.png", (0, 840, 2520, 587)), (840, 587), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=587)
    
image panzer_charfcm_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_charfcm_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=760)
    
image panzer_charfcm_static_back:
    Fixed(im.Crop("battle/units/panzer_charfcm_walk.png", (0, 840, 840, 587), xalign=0.5, yalign=0.5), xsize=840, ysize=587)
    
image panzer_charfcm_static_front:
    Fixed(im.Crop("battle/units/panzer_charfcm_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=760)
    
image panzer_charfcm_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 810
        ypos 15
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_charfcm_main1_attack.png", (0, 840, 3360, 587)), (840, 587), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=587)
        
image panzer_charfcm_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_charfcm_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=760)
    contains:
        "offensive_cannonblast_front"
        xpos 50
        ypos 300

image panzer_charfcm_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_charfcm_main1_attack.png", (2520, 840, 840, 587), xalign=0.5, yalign=0.5), xsize=840, ysize=587)
    
image panzer_charfcm_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_charfcm_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=760)
        
image panzer_charfcm_main2_attack_back:
    contains:
        "offensive_gunfire_back"
        xpos 649
        ypos 245
    contains:
        Fixed(im.Crop("battle/units/panzer_charfcm_walk.png", (0, 840, 840, 587), xalign=0.5, yalign=0.5), xsize=840, ysize=587)
    contains:
        "offensive_gunfire_back"
        xpos 720
        ypos 365
        rotate 27
    contains:
        "offensive_gunfire_front"
        xpos 120
        ypos 467
    
image panzer_charfcm_main2_attack_front:
    contains:
        "offensive_gunfire_back"
        xpos 708
        ypos 135
    contains:
        Fixed(im.Crop("battle/units/panzer_charfcm_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=760)
    contains:
        "offensive_gunfire_front"
        xpos 318
        ypos 525
        rotate -37
    contains:
        "offensive_gunfire_front"
        xpos 125
        ypos 463
    
image panzer_charfcm_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_charfcm_walk.png", (0, 840, 840, 587), xalign=0.5, yalign=0.5), xsize=840, ysize=587)
    
image panzer_charfcm_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_charfcm_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=760)
    
image panzer_charfcm_special1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_charfcm_walk.png", (0, 840, 2520, 587)), (840, 587), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=587)
    
image panzer_charfcm_special1_attack_front:
    Fixed(anim.Filmstrip("battle/units/panzer_charfcm_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=760)
    
image panzer_charfcm_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_charfcm_walk.png", (0, 840, 840, 587), xalign=0.5, yalign=0.5), xsize=840, ysize=587)
    
image panzer_charfcm_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_charfcm_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=760)
    
image panzer_charfcm_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_charfcm_walk.png", (0, 840, 2520, 587)), (840, 587), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=587)
    
image panzer_charfcm_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_charfcm_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=760)
    
image panzer_charfcm_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_charfcm_walk.png", (0, 840, 840, 587), xalign=0.5, yalign=0.5), xsize=840, ysize=587)
    
image panzer_charfcm_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_charfcm_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=760)
    
image panzer_charfcm_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_charfcm_walk.png", (0, 840, 2520, 587)), (840, 587), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=587), boost_white)
    contains:
        Fixed("reaction_powerup_megaspeed", xsize=840, ysize=840)
    
image panzer_charfcm_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_charfcm_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=760), boost_white)
    contains:
        Fixed("reaction_powerup_megaspeed", xsize=840, ysize=760)
    
image panzer_charfcm_main1_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_charfcm_walk.png", (0, 840, 840, 587), xalign=0.5, yalign=0.5), xsize=840, ysize=587)
    
image panzer_charfcm_main1_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_charfcm_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=760)
    
image panzer_charfcm_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_charfcm_walk.png", (0, 840, 2520, 587)), (840, 587), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=587), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_charfcm_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_charfcm_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=760), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=760)
    
image panzer_charfcm_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_charfcm_walk.png", (0, 840, 840, 587), xalign=0.5, yalign=0.5), xsize=840, ysize=587)
    
image panzer_charfcm_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_charfcm_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=760)
    
################################
#panzer_churchill
################################

image panzer_churchill_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_churchill_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_churchill_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_churchill_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_churchill_static_back:
    Fixed(im.Crop("battle/units/panzer_churchill_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_churchill_static_front:
    Fixed(im.Crop("battle/units/panzer_churchill_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_churchill_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 700
        ypos 110
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_churchill_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_churchill_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_churchill_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 160
        ypos 342

image panzer_churchill_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_churchill_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_churchill_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_churchill_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_churchill_main2_attack_back:
    contains:
        "offensive_gunfire_back"
        xpos 605
        ypos 319
    contains:
        Fixed(im.Crop("battle/units/panzer_churchill_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_churchill_main2_attack_front:
    contains:
        Fixed(im.Crop("battle/units/panzer_churchill_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 250
        ypos 480
        
image panzer_churchill_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_churchill_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_churchill_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_churchill_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)  
    
image panzer_churchill_special1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_churchill_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_churchill_special1_attack_front:
    Fixed(anim.Filmstrip("battle/units/panzer_churchill_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_churchill_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_churchill_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_churchill_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_churchill_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_churchill_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_churchill_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megaarmor", xsize=840, ysize=840)
    
image panzer_churchill_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_churchill_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megaarmor", xsize=840, ysize=840)
    
image panzer_churchill_main1_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_churchill_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_churchill_main1_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_churchill_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_churchill_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_churchill_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_churchill_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_churchill_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_churchill_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_churchill_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_churchill_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_churchill_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_crusader
################################

image panzer_crusader_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_crusader_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_crusader_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_crusader_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_crusader_static_back:
    Fixed(im.Crop("battle/units/panzer_crusader_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_crusader_static_front:
    Fixed(im.Crop("battle/units/panzer_crusader_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_crusader_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 700
        ypos 110
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_crusader_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_crusader_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_crusader_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 160
        ypos 320

image panzer_crusader_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_crusader_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_crusader_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_crusader_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_crusader_main2_attack_back:
    contains:
        "offensive_gunfire_back"
        xpos 610
        ypos 330
    contains:
        Fixed(im.Crop("battle/units/panzer_crusader_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_crusader_main2_attack_front:
    contains:
        Fixed(im.Crop("battle/units/panzer_crusader_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 280
        ypos 490
    
image panzer_crusader_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_crusader_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_crusader_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_crusader_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)   
    
image panzer_crusader_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_crusader_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_crusader_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_crusader_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_crusader_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_crusader_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_crusader_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_crusader_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_crusader_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_crusader_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megaspeed", xsize=840, ysize=840)
    
image panzer_crusader_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_crusader_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megaspeed", xsize=840, ysize=840)
    
image panzer_crusader_main1_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_crusader_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_crusader_main1_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_crusader_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_crusader_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_crusader_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_crusader_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_crusader_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_crusader_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_crusader_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_crusader_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_crusader_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_covenanter
################################

image panzer_covenanter_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_covenanter_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_covenanter_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_covenanter_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_covenanter_static_back:
    Fixed(im.Crop("battle/units/panzer_covenanter_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_covenanter_static_front:
    Fixed(im.Crop("battle/units/panzer_covenanter_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_covenanter_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 700
        ypos 110
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_covenanter_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_covenanter_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_covenanter_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 180
        ypos 310

image panzer_covenanter_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_covenanter_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_covenanter_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_covenanter_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_covenanter_main2_attack_back:
    contains:
        "offensive_gunfire_back"
        xpos 530
        ypos 260
    contains:
        Fixed(im.Crop("battle/units/panzer_covenanter_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_covenanter_main2_attack_front:
    contains:
        Fixed(im.Crop("battle/units/panzer_covenanter_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 265
        ypos 388
    
image panzer_covenanter_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_covenanter_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_covenanter_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_covenanter_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)  
    
image panzer_covenanter_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_covenanter_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_covenanter_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_covenanter_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_covenanter_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_covenanter_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_covenanter_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_covenanter_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_covenanter_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_covenanter_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megaspeed", xsize=840, ysize=840)
    
image panzer_covenanter_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_covenanter_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megaspeed", xsize=840, ysize=840)
    
image panzer_covenanter_main1_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_covenanter_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_covenanter_main1_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_covenanter_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image panzer_covenanter_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_covenanter_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_covenanter_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_covenanter_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_covenanter_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_covenanter_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_covenanter_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_covenanter_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#antitank_elefant
################################

image antitank_elefant_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_elefant_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_elefant_walk_front:
    Fixed(anim.Filmstrip("battle/units/antitank_elefant_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_elefant_static_back:
    Fixed(im.Crop("battle/units/antitank_elefant_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_elefant_static_front:
    Fixed(im.Crop("battle/units/antitank_elefant_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_elefant_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 860
        ypos 10
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_elefant_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image antitank_elefant_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_elefant_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 10
        ypos 390

image antitank_elefant_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/antitank_elefant_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_elefant_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/antitank_elefant_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image antitank_elefant_main2_attack_back:
    contains:
        "offensive_gunfire_back"
        xpos 605
        ypos 335
    contains:
        Fixed(im.Crop("battle/units/antitank_elefant_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_elefant_main2_attack_front:
    contains:
        Fixed(im.Crop("battle/units/antitank_elefant_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 260
        ypos 450
    
image antitank_elefant_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/antitank_elefant_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_elefant_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/antitank_elefant_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_elefant_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_elefant_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image antitank_elefant_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/antitank_elefant_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image antitank_elefant_heal_finalframe_back:
    Fixed(im.Crop("battle/units/antitank_elefant_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_elefant_heal_finalframe_front:
    Fixed(im.Crop("battle/units/antitank_elefant_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_felthaubits
################################

image panzer_felthaubits_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_felthaubits_walk.png", (0, 321, 1404, 321)), (468, 321), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_felthaubits_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_felthaubits_walk.png", (468, 321), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_felthaubits_static_back:
    Fixed(im.Crop("battle/units/panzer_felthaubits_walk.png", (0, 321, 468, 321), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_felthaubits_static_front:
    Fixed(im.Crop("battle/units/panzer_felthaubits_walk.png", (0, 0, 468, 321), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_felthaubits_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_felthaubits_main1_attack.png", (0, 321, 3276, 321)), (468, 321), (7, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_felthaubits_main1_attack_front:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_felthaubits_main1_attack.png", (0, 0, 3276, 321)), (468, 321), (7, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image panzer_felthaubits_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_felthaubits_main1_attack.png", (2808, 321, 468, 321), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_felthaubits_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_felthaubits_main1_attack.png", (2808, 0, 468, 321), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_felthaubits_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_felthaubits_walk.png", (0, 321, 1404, 321)), (468, 321), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_felthaubits_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_felthaubits_walk.png", (468, 321), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_felthaubits_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_felthaubits_walk.png", (0, 321, 468, 321), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_felthaubits_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_felthaubits_walk.png", (0, 0, 468, 321), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#antitank_hornisse
################################

image antitank_hornisse_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_hornisse_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_hornisse_walk_front:
    Fixed(anim.Filmstrip("battle/units/antitank_hornisse_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_hornisse_static_back:
    Fixed(im.Crop("battle/units/antitank_hornisse_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_hornisse_static_front:
    Fixed(im.Crop("battle/units/antitank_hornisse_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_hornisse_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 890
        ypos 0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_hornisse_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image antitank_hornisse_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_hornisse_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos -40
        ypos 420

image antitank_hornisse_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/antitank_hornisse_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_hornisse_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/antitank_hornisse_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image antitank_hornisse_main2_attack_back:
    contains:
        Fixed(im.Crop("battle/units/antitank_hornisse_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 140
        ypos 469
    
image antitank_hornisse_main2_attack_front:
    contains:
        Fixed(im.Crop("battle/units/antitank_hornisse_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_back"
        xpos 672
        ypos 210
    
image antitank_hornisse_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/antitank_hornisse_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_hornisse_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/antitank_hornisse_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image antitank_hornisse_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_hornisse_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image antitank_hornisse_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/antitank_hornisse_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image antitank_hornisse_heal_finalframe_back:
    Fixed(im.Crop("battle/units/antitank_hornisse_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_hornisse_heal_finalframe_front:
    Fixed(im.Crop("battle/units/antitank_hornisse_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_hotchkiss
################################

image panzer_hotchkiss_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_hotchkiss_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_hotchkiss_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_hotchkiss_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_hotchkiss_static_back:
    Fixed(im.Crop("battle/units/panzer_hotchkiss_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_hotchkiss_static_front:
    Fixed(im.Crop("battle/units/panzer_hotchkiss_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_hotchkiss_main1_attack_back:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_hotchkiss_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_mediumcannonblast_back"
        xpos 580
        ypos 165
        
image panzer_hotchkiss_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_hotchkiss_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_mediumcannonblast_front"
        xpos 258
        ypos 290

image panzer_hotchkiss_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_hotchkiss_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_hotchkiss_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_hotchkiss_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_hotchkiss_main2_attack_back:
    contains:
        "offensive_gunfire_back"
        xpos 453
        ypos 280
    contains:
        Fixed(im.Crop("battle/units/panzer_hotchkiss_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_hotchkiss_main2_attack_front:
    contains:
        "offensive_gunfire_front"
        xpos 325
        ypos 345
    contains:
        Fixed(im.Crop("battle/units/panzer_hotchkiss_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
    
image panzer_hotchkiss_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_hotchkiss_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_hotchkiss_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_hotchkiss_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)  
    
image panzer_hotchkiss_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_hotchkiss_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_hotchkiss_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_hotchkiss_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_hotchkiss_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_hotchkiss_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_hotchkiss_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_hotchkiss_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_is2
################################

image panzer_is2_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_is2_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_is2_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_is2_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_is2_static_back:
    Fixed(im.Crop("battle/units/panzer_is2_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_is2_static_front:
    Fixed(im.Crop("battle/units/panzer_is2_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_is2_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 910
        ypos 40
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_is2_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_is2_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_is2_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos -35
        ypos 445

image panzer_is2_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_is2_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_is2_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_is2_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_is2_special1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_is2_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_is2_special1_attack_front:
    Fixed(anim.Filmstrip("battle/units/panzer_is2_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_is2_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_is2_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_is2_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_is2_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_is2_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_is2_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_is2_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_is2_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_is2_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_is2_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_is2_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_is2_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_is2_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_is2_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megaarmor", xsize=840, ysize=840)
    
image panzer_is2_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_is2_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megaarmor", xsize=840, ysize=840)
    
image panzer_is2_main1_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_is2_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_is2_main1_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_is2_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_is2_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_is2_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_is2_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_is2_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_is2_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_is2_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_is2_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_is2_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#antitank_jagdpanzer
################################

image antitank_jagdpanzer_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_jagdpanzer_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_jagdpanzer_walk_front:
    Fixed(anim.Filmstrip("battle/units/antitank_jagdpanzer_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_jagdpanzer_static_back:
    Fixed(im.Crop("battle/units/antitank_jagdpanzer_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_jagdpanzer_static_front:
    Fixed(im.Crop("battle/units/antitank_jagdpanzer_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_jagdpanzer_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 800
        ypos 50
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_jagdpanzer_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image antitank_jagdpanzer_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_jagdpanzer_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos -30
        ypos 420

image antitank_jagdpanzer_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/antitank_jagdpanzer_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_jagdpanzer_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/antitank_jagdpanzer_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image antitank_jagdpanzer_main2_attack_back:
    contains:
        Fixed(im.Crop("battle/units/antitank_jagdpanzer_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_back"
        xpos 513
        ypos 313
        
image antitank_jagdpanzer_main2_attack_front:
    contains:
        Fixed(im.Crop("battle/units/antitank_jagdpanzer_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 380
        ypos 380
    
image antitank_jagdpanzer_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/antitank_jagdpanzer_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_jagdpanzer_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/antitank_jagdpanzer_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image antitank_jagdpanzer_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_jagdpanzer_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image antitank_jagdpanzer_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/antitank_jagdpanzer_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image antitank_jagdpanzer_heal_finalframe_back:
    Fixed(im.Crop("battle/units/antitank_jagdpanzer_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_jagdpanzer_heal_finalframe_front:
    Fixed(im.Crop("battle/units/antitank_jagdpanzer_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#antitank_jagdpanther
################################

image antitank_jagdpanther_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_jagdpanther_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_jagdpanther_walk_front:
    Fixed(anim.Filmstrip("battle/units/antitank_jagdpanther_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_jagdpanther_static_back:
    Fixed(im.Crop("battle/units/antitank_jagdpanther_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_jagdpanther_static_front:
    Fixed(im.Crop("battle/units/antitank_jagdpanther_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_jagdpanther_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 840
        ypos 65
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_jagdpanther_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image antitank_jagdpanther_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_jagdpanther_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 0
        ypos 420

image antitank_jagdpanther_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/antitank_jagdpanther_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_jagdpanther_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/antitank_jagdpanther_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image antitank_jagdpanther_main2_attack_back:
    contains:
        "offensive_gunfire_back"
        xpos 520
        ypos 270
    contains:
        Fixed(im.Crop("battle/units/antitank_jagdpanther_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_jagdpanther_main2_attack_front:
    contains:
        Fixed(im.Crop("battle/units/antitank_jagdpanther_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 180
        ypos 437
    
image antitank_jagdpanther_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/antitank_jagdpanther_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_jagdpanther_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/antitank_jagdpanther_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_jagdpanther_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_jagdpanther_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image antitank_jagdpanther_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/antitank_jagdpanther_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image antitank_jagdpanther_heal_finalframe_back:
    Fixed(im.Crop("battle/units/antitank_jagdpanther_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_jagdpanther_heal_finalframe_front:
    Fixed(im.Crop("battle/units/antitank_jagdpanther_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#antitank_jagdtiger
################################

image antitank_jagdtiger_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_jagdtiger_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_jagdtiger_walk_front:
    Fixed(anim.Filmstrip("battle/units/antitank_jagdtiger_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_jagdtiger_static_back:
    Fixed(im.Crop("battle/units/antitank_jagdtiger_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_jagdtiger_static_front:
    Fixed(im.Crop("battle/units/antitank_jagdtiger_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_jagdtiger_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 840
        ypos 60
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_jagdtiger_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image antitank_jagdtiger_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_jagdtiger_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 10
        ypos 410

image antitank_jagdtiger_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/antitank_jagdtiger_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_jagdtiger_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/antitank_jagdtiger_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image antitank_jagdtiger_main2_attack_back:
    contains:
        Fixed(im.Crop("battle/units/antitank_jagdtiger_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_back"
        xpos 644
        ypos 333
        
image antitank_jagdtiger_main2_attack_front:
    contains:
        Fixed(im.Crop("battle/units/antitank_jagdtiger_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 258
        ypos 526
    
image antitank_jagdtiger_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/antitank_jagdtiger_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_jagdtiger_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/antitank_jagdtiger_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_jagdtiger_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_jagdtiger_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image antitank_jagdtiger_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/antitank_jagdtiger_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image antitank_jagdtiger_heal_finalframe_back:
    Fixed(im.Crop("battle/units/antitank_jagdtiger_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_jagdtiger_heal_finalframe_front:
    Fixed(im.Crop("battle/units/antitank_jagdtiger_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_konigstiger
################################

image panzer_konigstiger_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_konigstiger_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_konigstiger_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_konigstiger_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_konigstiger_static_back:
    Fixed(im.Crop("battle/units/panzer_konigstiger_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_konigstiger_static_front:
    Fixed(im.Crop("battle/units/panzer_konigstiger_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_konigstiger_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 860
        ypos 64
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_konigstiger_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_konigstiger_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_konigstiger_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 20
        ypos 420

image panzer_konigstiger_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_konigstiger_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_konigstiger_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_konigstiger_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_konigstiger_main2_attack_back:
    contains:
        Fixed(im.Crop("battle/units/panzer_konigstiger_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_back"
        xpos 661
        ypos 343
        
image panzer_konigstiger_main2_attack_front:
    contains:
        Fixed(im.Crop("battle/units/panzer_konigstiger_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 295
        ypos 522
    
image panzer_konigstiger_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_konigstiger_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_konigstiger_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_konigstiger_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_konigstiger_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_konigstiger_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_konigstiger_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_konigstiger_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_konigstiger_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_konigstiger_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_konigstiger_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_konigstiger_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_konigstiger_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_konigstiger_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megapower", xsize=840, ysize=840)
    
image panzer_konigstiger_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_konigstiger_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megapower", xsize=840, ysize=840)
    
image panzer_konigstiger_main1_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_konigstiger_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_konigstiger_main1_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_konigstiger_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_konigstiger_main2_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_konigstiger_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_stukatablets", xsize=840, ysize=840)
    
image panzer_konigstiger_main2_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_konigstiger_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_stukatablets", xsize=840, ysize=840)
    
image panzer_konigstiger_main2_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_konigstiger_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_konigstiger_main2_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_konigstiger_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_konigstiger_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_konigstiger_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_konigstiger_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_konigstiger_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_konigstiger_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_konigstiger_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_konigstiger_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_konigstiger_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_l335
################################

image panzer_l335_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_l335_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_l335_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_l335_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_l335_static_back:
    Fixed(im.Crop("battle/units/panzer_l335_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_l335_static_front:
    Fixed(im.Crop("battle/units/panzer_l335_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_l335_main1_attack_back:
    contains:
        "offensive_gunfire_back"
        xpos 525
        ypos 340
    contains:
        "offensive_gunfire_back"
        xpos 545
        ypos 350
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_l335_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .04, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_l335_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_l335_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .04, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 340
        ypos 418
    contains:
        "offensive_gunfire_front"
        xpos 358
        ypos 433

image panzer_l335_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_l335_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_l335_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_l335_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_l335_special1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_l335_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_l335_special1_attack_front:
    Fixed(anim.Filmstrip("battle/units/panzer_l335_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_l335_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_l335_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_l335_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_l335_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_l335_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_l335_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_l335_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_l335_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_l335_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_l335_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_l335_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_l335_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_l335_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_l335_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megaspeed", xsize=840, ysize=840)
    
image panzer_l335_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_l335_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megaspeed", xsize=840, ysize=840)
    
image panzer_l335_main1_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_l335_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_l335_main1_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_l335_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_l335_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_l335_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_l335_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_l335_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_l335_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_l335_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_l335_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_l335_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#antitank_marder
################################

image antitank_marder_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_marder_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_marder_walk_front:
    Fixed(anim.Filmstrip("battle/units/antitank_marder_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_marder_static_back:
    Fixed(im.Crop("battle/units/antitank_marder_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_marder_static_front:
    Fixed(im.Crop("battle/units/antitank_marder_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_marder_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 820
        ypos 30
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_marder_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image antitank_marder_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_marder_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 30
        ypos 362

image antitank_marder_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/antitank_marder_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_marder_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/antitank_marder_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_marder_special1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_marder_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_marder_special1_attack_front:
    Fixed(anim.Filmstrip("battle/units/antitank_marder_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_marder_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/antitank_marder_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_marder_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/antitank_marder_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_marder_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_marder_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image antitank_marder_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/antitank_marder_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image antitank_marder_heal_finalframe_back:
    Fixed(im.Crop("battle/units/antitank_marder_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_marder_heal_finalframe_front:
    Fixed(im.Crop("battle/units/antitank_marder_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_kv1
################################

image panzer_kv1_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_kv1_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_kv1_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_kv1_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_kv1_static_back:
    Fixed(im.Crop("battle/units/panzer_kv1_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_kv1_static_front:
    Fixed(im.Crop("battle/units/panzer_kv1_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_kv1_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 804
        ypos 70
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_kv1_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_kv1_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_kv1_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 80
        ypos 370

image panzer_kv1_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_kv1_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_kv1_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_kv1_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_kv1_main2_attack_back:
    contains:
        "offensive_gunfire_back"
        xpos 634
        ypos 342
    contains:
        Fixed(im.Crop("battle/units/panzer_kv1_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_kv1_main2_attack_front:
    contains:
        Fixed(im.Crop("battle/units/panzer_kv1_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 293
        ypos 510
    
image panzer_kv1_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_kv1_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_kv1_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_kv1_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)  
    
image panzer_kv1_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_kv1_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_kv1_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_kv1_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_kv1_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_kv1_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_kv1_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_kv1_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_kv1_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_kv1_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megaspeed", xsize=840, ysize=840)
    
image panzer_kv1_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_kv1_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megaspeed", xsize=840, ysize=840)
    
image panzer_kv1_main1_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_kv1_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_kv1_main1_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_kv1_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_kv1_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_kv1_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_kv1_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_kv1_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_kv1_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_kv1_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_kv1_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_kv1_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_kv2
################################

image panzer_kv2_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_kv2_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_kv2_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_kv2_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_kv2_static_back:
    Fixed(im.Crop("battle/units/panzer_kv2_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_kv2_static_front:
    Fixed(im.Crop("battle/units/panzer_kv2_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_kv2_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 800
        ypos 30
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_kv2_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_kv2_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_kv2_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 83
        ypos 326

image panzer_kv2_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_kv2_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_kv2_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_kv2_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_kv2_main2_attack_back:
    contains:
        "offensive_gunfire_back"
        xpos 630
        ypos 345
    contains:
        Fixed(im.Crop("battle/units/panzer_kv2_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_kv2_main2_attack_front:
    contains:
        Fixed(im.Crop("battle/units/panzer_kv2_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 293
        ypos 510
    
image panzer_kv2_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_kv2_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_kv2_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_kv2_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_kv2_special1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_kv2_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_kv2_special1_attack_front:
    Fixed(anim.Filmstrip("battle/units/panzer_kv2_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_kv2_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_kv2_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_kv2_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_kv2_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_kv2_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_kv2_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_kv2_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_kv2_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_kv2_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_kv2_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_kv2_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_kv2_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_kv2_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_kv2_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megapower", xsize=840, ysize=840)
    
image panzer_kv2_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_kv2_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megapower", xsize=840, ysize=840)
    
image panzer_kv2_main1_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_kv2_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_kv2_main1_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_kv2_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_kv2_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_kv2_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_kv2_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_kv2_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_kv2_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_kv2_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_kv2_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_kv2_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_matilda1
################################

image panzer_matilda1_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_matilda1_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_matilda1_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_matilda1_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_matilda1_static_back:
    Fixed(im.Crop("battle/units/panzer_matilda1_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_matilda1_static_front:
    Fixed(im.Crop("battle/units/panzer_matilda1_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_matilda1_main1_attack_back:
    contains:
        "offensive_gunfire_big_back"
        xpos 517
        ypos 280
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_matilda1_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_matilda1_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_matilda1_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_big_front"
        xpos 300
        ypos 395

image panzer_matilda1_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_matilda1_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_matilda1_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_matilda1_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_matilda1_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_matilda1_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_matilda1_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_matilda1_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_matilda1_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_matilda1_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_matilda1_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_matilda1_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_matilda1_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_matilda1_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_matilda1_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_matilda1_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_matilda1_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_matilda1_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_matilda1_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_matilda1_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_matilda2
################################

image panzer_matilda2_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_matilda2_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_matilda2_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_matilda2_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_matilda2_static_back:
    Fixed(im.Crop("battle/units/panzer_matilda2_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_matilda2_static_front:
    Fixed(im.Crop("battle/units/panzer_matilda2_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_matilda2_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 730
        ypos 110
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_matilda2_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_matilda2_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_matilda2_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 140
        ypos 340

image panzer_matilda2_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_matilda2_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_matilda2_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_matilda2_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_matilda2_main2_attack_back:
    contains:
        "offensive_gunfire_back"
        xpos 560
        ypos 310
    contains:
        Fixed(im.Crop("battle/units/panzer_matilda2_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_matilda2_main2_attack_front:
    contains:
        "offensive_gunfire_front"
        xpos 300
        ypos 360
    contains:
        Fixed(im.Crop("battle/units/panzer_matilda2_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_matilda2_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_matilda2_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_matilda2_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_matilda2_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)  
    
image panzer_matilda2_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_matilda2_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_matilda2_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_matilda2_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_matilda2_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_matilda2_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_matilda2_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_matilda2_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_matilda2_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_matilda2_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megaspeed", xsize=840, ysize=840)
    
image panzer_matilda2_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_matilda2_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megaspeed", xsize=840, ysize=840)
    
image panzer_matilda2_main1_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_matilda2_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_matilda2_main1_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_matilda2_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_matilda2_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_matilda2_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_matilda2_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_matilda2_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_matilda2_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_matilda2_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_matilda2_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_matilda2_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_maus
################################

image panzer_maus_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_maus_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_maus_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_maus_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=730)
    
image panzer_maus_static_back:
    Fixed(im.Crop("battle/units/panzer_maus_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_maus_static_front:
    Fixed(im.Crop("battle/units/panzer_maus_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=730)
    
image panzer_maus_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 820
        ypos 0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_maus_main1_attack.png", (0, 840, 3360, 600)), (840, 600), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_maus_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_maus_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=730)
    contains:
        "offensive_cannonblast_front"
        xpos 0
        ypos 275

image panzer_maus_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_maus_main1_attack.png", (2520, 840, 840, 600), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_maus_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_maus_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=730)
    
image panzer_maus_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_maus_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_xpower", xsize=840, ysize=840)
    
image panzer_maus_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_maus_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=730), boost_white)
    contains:
        Fixed("reaction_powerup_xpower", xsize=840, ysize=730)
    
image panzer_maus_main1_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_maus_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_maus_main1_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_maus_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=730)
    
image panzer_maus_special1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_maus_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_maus_special1_attack_front:
    Fixed(anim.Filmstrip("battle/units/panzer_maus_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=730)
    
image panzer_maus_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_maus_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_maus_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_maus_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=730)
    
image panzer_maus_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_maus_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_maus_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_maus_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=730)
    
image panzer_maus_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_maus_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_maus_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_maus_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=730)
    
image panzer_maus_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_maus_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_maus_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_maus_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=730), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=730)
    
image panzer_maus_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_maus_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_maus_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_maus_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=730)
    
################################
#panzer_mech
################################

image panzer_mech_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_mech_walk.png", (0, 312, 1176, 312)), (294, 312), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_mech_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_mech_walk.png", (294, 312), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_mech_static_back:
    Fixed(im.Crop("battle/units/panzer_mech_main1_attack.png", (0, 315, 294, 315), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_mech_static_front:
    Fixed(im.Crop("battle/units/panzer_mech_main1_attack.png", (0, 0, 294, 315), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_mech_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_mech_main1_attack.png", (0, 315, 2940, 315)), (294, 315), (10, 1), .02, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_mech_main1_attack_front:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_mech_main1_attack.png", (0, 0, 2940, 315)), (294, 315), (10, 1), .02, xalign=0.53, yalign=0.51), xsize=840, ysize=840)

image panzer_mech_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_mech_main1_attack.png", (0, 315, 294, 315), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_mech_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_mech_main1_attack.png", (0, 0, 294, 315), xalign=0.53, yalign=0.51), xsize=840, ysize=840)
    
image panzer_mech_main2_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_mech_walk.png", (0, 312, 1176, 312)), (294, 312), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_mech_main2_attack_front:
    Fixed(anim.Filmstrip("battle/units/panzer_mech_walk.png", (294, 312), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_mech_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_mech_main1_attack.png", (0, 315, 294, 315), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_mech_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_mech_main1_attack.png", (0, 0, 294, 315), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_mech_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_mech_walk.png", (0, 312, 1176, 312)), (294, 312), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_xaccuracy", xsize=840, ysize=840)
    
image panzer_mech_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_mech_walk.png", (294, 312), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_xaccuracy", xsize=840, ysize=840)
    
image panzer_mech_main1_powerup_finalframe_back:
    At(Fixed(im.Crop("battle/units/panzer_mech_walk.png", (0, 312, 294, 312), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    
image panzer_mech_main1_powerup_finalframe_front:
    At(Fixed(im.Crop("battle/units/panzer_mech_walk.png", (0, 0, 294, 312), xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    
image panzer_mech_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_mech_walk.png", (0, 312, 1176, 312)), (294, 312), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_mech_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_mech_walk.png", (294, 312), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_mech_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_mech_walk.png", (0, 312, 294, 312), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_mech_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_mech_walk.png", (0, 0, 294, 312), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_odessa
################################

image panzer_odessa_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_odessa_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_odessa_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_odessa_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_odessa_static_back:
    Fixed(im.Crop("battle/units/panzer_odessa_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_odessa_static_front:
    Fixed(im.Crop("battle/units/panzer_odessa_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_odessa_main1_attack_back:
    contains:
        "offensive_gunfire_back"
        xpos 540
        ypos 200
        pause 0.1
        ypos 190
        pause 0.05
        ypos 200
        pause 0.05
        repeat
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_odessa_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_odessa_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_odessa_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 305
        ypos 315
        pause 0.1
        ypos 305
        pause 0.05
        ypos 315
        pause 0.05
        repeat

image panzer_odessa_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_odessa_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_odessa_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_odessa_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_odessa_main2_attack_back:
    contains:
        "offensive_gunfire_back"
        xpos 705
        ypos 255
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_odessa_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_odessa_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_odessa_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 300
        ypos 457
        pause 0.1
        ypos 455
        pause 0.05
        ypos 457
        pause 0.05
        repeat
    
image panzer_odessa_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_odessa_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_odessa_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_odessa_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_odessa_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_odessa_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_odessa_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_odessa_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_odessa_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_odessa_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_odessa_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_odessa_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#antitank_pak36
################################

image antitank_pak36_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_pak36_walk.png", (0, 291, 1176, 291)), (294, 291), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_pak36_walk_front:
    Fixed(anim.Filmstrip("battle/units/antitank_pak36_walk.png", (294, 291), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_pak36_static_back:
    Fixed(im.Crop("battle/units/antitank_pak36_walk.png", (0, 291, 294, 291), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_pak36_static_front:
    Fixed(im.Crop("battle/units/antitank_pak36_walk.png", (0, 0, 294, 291), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_pak36_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_pak36_main1_attack.png", (0, 291, 2583, 291)), (369, 291), (7, 1), .04, loop=False, xalign=0.48, yalign=0.5), xsize=840, ysize=840)
        
image antitank_pak36_main1_attack_front:
    Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_pak36_main1_attack.png", (0, 0, 2583, 291)), (369, 291), (7, 1), .04, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image antitank_pak36_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/antitank_pak36_main1_attack.png", (2214, 291, 369, 291), xalign=0.48, yalign=0.5), xsize=840, ysize=840)
    
image antitank_pak36_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/antitank_pak36_main1_attack.png", (2214, 0, 369, 291), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_pak36_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_pak36_walk.png", (0, 291, 1176, 291)), (294, 291), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image antitank_pak36_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/antitank_pak36_walk.png", (294, 291), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image antitank_pak36_heal_finalframe_back:
    Fixed(im.Crop("battle/units/antitank_pak36_walk.png", (0, 291, 294, 291), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_pak36_heal_finalframe_front:
    Fixed(im.Crop("battle/units/antitank_pak36_walk.png", (0, 0, 294, 291), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_panther
################################

image panzer_panther_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panther_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panther_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_panther_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panther_static_back:
    Fixed(im.Crop("battle/units/panzer_panther_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panther_static_front:
    Fixed(im.Crop("battle/units/panzer_panther_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panther_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 815
        ypos 72
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panther_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_panther_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panther_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 20
        ypos 405

image panzer_panther_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panther_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panther_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panther_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_panther_main2_attack_back:
    contains:
        Fixed(im.Crop("battle/units/panzer_panther_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_back"
        xpos 570
        ypos 320
        
image panzer_panther_main2_attack_front:
    contains:
        Fixed(im.Crop("battle/units/panzer_panther_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 222
        ypos 490
    
image panzer_panther_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panther_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panther_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panther_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panther_special1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panther_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panther_special1_attack_front:
    Fixed(anim.Filmstrip("battle/units/panzer_panther_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panther_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panther_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panther_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panther_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panther_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_panther_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_panther_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_panther_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_panther_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panther_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panther_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panther_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panther_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panther_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_xcharm", xsize=840, ysize=840)
    
image panzer_panther_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_panther_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_xcharm", xsize=840, ysize=840)
    
image panzer_panther_main1_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panther_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panther_main1_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panther_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panther_main2_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panther_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_stukatablets", xsize=840, ysize=840)
    
image panzer_panther_main2_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_panther_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_stukatablets", xsize=840, ysize=840)
    
image panzer_panther_main2_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panther_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panther_main2_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panther_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panther_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panther_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_panther_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_panther_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_panther_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panther_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panther_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panther_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_pantserwagen
################################

image panzer_pantserwagen_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_pantserwagen_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_pantserwagen_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_pantserwagen_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_pantserwagen_static_back:
    Fixed(im.Crop("battle/units/panzer_pantserwagen_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_pantserwagen_static_front:
    Fixed(im.Crop("battle/units/panzer_pantserwagen_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_pantserwagen_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 740
        ypos 40
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_pantserwagen_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_pantserwagen_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_pantserwagen_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 125
        ypos 287

image panzer_pantserwagen_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_pantserwagen_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_pantserwagen_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_pantserwagen_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_pantserwagen_main2_attack_back:
    contains:
        "offensive_gunfire_back"
        xpos 570
        ypos 258
    contains:
        "offensive_gunfire_back"
        xpos 616
        ypos 258
    contains:
        Fixed(im.Crop("battle/units/panzer_pantserwagen_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 220
        ypos 510
    
image panzer_pantserwagen_main2_attack_front:
    contains:
        "offensive_gunfire_back"
        xpos 690
        ypos 279
    contains:
        Fixed(im.Crop("battle/units/panzer_pantserwagen_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 170
        ypos 474
    contains:
        "offensive_gunfire_front"
        xpos 300
        ypos 391
    
image panzer_pantserwagen_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_pantserwagen_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_pantserwagen_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_pantserwagen_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)  
    
image panzer_pantserwagen_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_pantserwagen_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_pantserwagen_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_pantserwagen_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_pantserwagen_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_pantserwagen_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_pantserwagen_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_pantserwagen_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_panzer1
################################

image panzer_panzer1_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panzer1_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer1_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_panzer1_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer1_static_back:
    Fixed(im.Crop("battle/units/panzer_panzer1_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer1_static_front:
    Fixed(im.Crop("battle/units/panzer_panzer1_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer1_main1_attack_back:
    contains:
        "offensive_gunfire_back"
        xpos 570
        ypos 240
        pause 0.1
        ypos 230
        pause 0.05
        ypos 240
        pause 0.05
        repeat
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panzer1_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_panzer1_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panzer1_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 240
        ypos 410
        pause 0.1
        ypos 390 xpos 245
        pause 0.05
        ypos 410 xpos 240
        pause 0.05
        repeat

image panzer_panzer1_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panzer1_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer1_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panzer1_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer1_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_panzer1_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_panzer1_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_panzer1_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_panzer1_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panzer1_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer1_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panzer1_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer1_main2_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panzer1_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_stukatablets", xsize=840, ysize=840)
    
image panzer_panzer1_main2_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_panzer1_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_stukatablets", xsize=840, ysize=840)
    
image panzer_panzer1_main2_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panzer1_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer1_main2_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panzer1_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer1_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panzer1_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_panzer1_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_panzer1_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_panzer1_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panzer1_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer1_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panzer1_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_panzer2
################################

image panzer_panzer2_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panzer2_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer2_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_panzer2_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer2_static_back:
    Fixed(im.Crop("battle/units/panzer_panzer2_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer2_static_front:
    Fixed(im.Crop("battle/units/panzer_panzer2_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer2_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 720
        ypos 110
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panzer2_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_panzer2_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panzer2_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 180
        ypos 320

image panzer_panzer2_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panzer2_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer2_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panzer2_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_panzer2_main2_attack_back:
    contains:
        "offensive_gunfire_back"
        xpos 550
        ypos 270
    contains:
        Fixed(im.Crop("battle/units/panzer_panzer2_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer2_main2_attack_front:
    contains:
        Fixed(im.Crop("battle/units/panzer_panzer2_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 260
        ypos 410
    
image panzer_panzer2_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panzer2_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer2_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panzer2_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer2_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_panzer2_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_panzer2_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_panzer2_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_panzer2_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panzer2_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer2_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panzer2_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer2_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panzer2_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megaarmor", xsize=840, ysize=840)
    
image panzer_panzer2_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_panzer2_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megaarmor", xsize=840, ysize=840)
    
image panzer_panzer2_main1_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panzer2_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer2_main1_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panzer2_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer2_main2_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panzer2_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_stukatablets", xsize=840, ysize=840)
    
image panzer_panzer2_main2_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_panzer2_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_stukatablets", xsize=840, ysize=840)
    
image panzer_panzer2_main2_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panzer2_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer2_main2_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panzer2_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer2_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panzer2_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_panzer2_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_panzer2_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_panzer2_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panzer2_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer2_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panzer2_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_panzer3
################################

image panzer_panzer3_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panzer3_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer3_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_panzer3_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=800)
    
image panzer_panzer3_static_back:
    Fixed(im.Crop("battle/units/panzer_panzer3_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer3_static_front:
    Fixed(im.Crop("battle/units/panzer_panzer3_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=800)
    
image panzer_panzer3_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 790
        ypos 75
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panzer3_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_panzer3_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panzer3_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=800)
    contains:
        "offensive_cannonblast_front"
        xpos 80
        ypos 350

image panzer_panzer3_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panzer3_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer3_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panzer3_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=800)
        
image panzer_panzer3_main2_attack_back:
    contains:
        "offensive_gunfire_back"
        xpos 600
        ypos 345
    contains:
        Fixed(im.Crop("battle/units/panzer_panzer3_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer3_main2_attack_front:
    contains:
        Fixed(im.Crop("battle/units/panzer_panzer3_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=800)
    contains:
        "offensive_gunfire_front"
        xpos 260
        ypos 430
    
image panzer_panzer3_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panzer3_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer3_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panzer3_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=800)
    
image panzer_panzer3_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_panzer3_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_panzer3_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_panzer3_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=800)
    
image panzer_panzer3_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panzer3_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer3_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panzer3_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=800)
    
image panzer_panzer3_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panzer3_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megapower", xsize=840, ysize=840)
    
image panzer_panzer3_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_panzer3_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=800), boost_white)
    contains:
        Fixed("reaction_powerup_megapower", xsize=840, ysize=800)
    
image panzer_panzer3_main1_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panzer3_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer3_main1_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panzer3_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=800)
    
image panzer_panzer3_main2_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panzer3_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_stukatablets", xsize=840, ysize=840)
    
image panzer_panzer3_main2_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_panzer3_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=800), boost_white)
    contains:
        Fixed("reaction_powerup_stukatablets", xsize=840, ysize=800)
    
image panzer_panzer3_main2_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panzer3_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer3_main2_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panzer3_walk.png", (0, 0, 840, 800), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer3_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panzer3_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_panzer3_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_panzer3_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=800), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=800)
    
image panzer_panzer3_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panzer3_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer3_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panzer3_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=800)
    
################################
#panzer_panzer4
################################

image panzer_panzer4_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panzer4_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer4_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_panzer4_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer4_static_back:
    Fixed(im.Crop("battle/units/panzer_panzer4_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer4_static_front:
    Fixed(im.Crop("battle/units/panzer_panzer4_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer4_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 700
        ypos 110
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panzer4_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_panzer4_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panzer4_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 180
        ypos 320

image panzer_panzer4_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panzer4_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer4_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panzer4_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_panzer4_main2_attack_back:
    contains:
        "offensive_gunfire_back"
        xpos 600
        ypos 340
    contains:
        Fixed(im.Crop("battle/units/panzer_panzer4_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer4_main2_attack_front:
    contains:
        Fixed(im.Crop("battle/units/panzer_panzer4_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 223
        ypos 458
    
image panzer_panzer4_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panzer4_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer4_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panzer4_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer4_special1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panzer4_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer4_special1_attack_front:
    Fixed(anim.Filmstrip("battle/units/panzer_panzer4_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer4_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panzer4_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer4_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panzer4_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer4_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_panzer4_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_panzer4_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_panzer4_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_panzer4_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panzer4_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer4_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panzer4_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer4_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panzer4_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megacharm", xsize=840, ysize=840)
    
image panzer_panzer4_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_panzer4_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megacharm", xsize=840, ysize=840)
    
image panzer_panzer4_main1_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panzer4_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer4_main1_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panzer4_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer4_main2_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panzer4_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_stukatablets", xsize=840, ysize=840)
    
image panzer_panzer4_main2_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_panzer4_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_stukatablets", xsize=840, ysize=840)
    
image panzer_panzer4_main2_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panzer4_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer4_main2_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panzer4_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer4_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panzer4_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_panzer4_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_panzer4_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_panzer4_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panzer4_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer4_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panzer4_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_panzer38t
################################

image panzer_panzer38t_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panzer38t_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer38t_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_panzer38t_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer38t_static_back:
    Fixed(im.Crop("battle/units/panzer_panzer38t_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer38t_static_front:
    Fixed(im.Crop("battle/units/panzer_panzer38t_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer38t_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 740
        ypos 80
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panzer38t_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_panzer38t_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panzer38t_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 120
        ypos 320

image panzer_panzer38t_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panzer38t_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer38t_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panzer38t_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_panzer38t_main2_attack_back:
    contains:
        "offensive_gunfire_back"
        xpos 577
        ypos 303
    contains:
        "offensive_gunfire_back"
        xpos 537
        ypos 242
    contains:
        Fixed(im.Crop("battle/units/panzer_panzer38t_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer38t_main2_attack_front:
    contains:
        Fixed(im.Crop("battle/units/panzer_panzer38t_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 260
        ypos 378
    contains:
        "offensive_gunfire_front"
        xpos 263
        ypos 458
    
image panzer_panzer38t_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panzer38t_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer38t_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panzer38t_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer38t_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_panzer38t_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_panzer38t_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_panzer38t_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_panzer38t_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panzer38t_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer38t_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panzer38t_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer38t_main2_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panzer38t_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_stukatablets", xsize=840, ysize=840)
    
image panzer_panzer38t_main2_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_panzer38t_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_stukatablets", xsize=840, ysize=840)
    
image panzer_panzer38t_main2_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panzer38t_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer38t_main2_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panzer38t_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer38t_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_panzer38t_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_panzer38t_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_panzer38t_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_panzer38t_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_panzer38t_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_panzer38t_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_panzer38t_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#antitank_panzerjager
################################

image antitank_panzerjager_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_panzerjager_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_panzerjager_walk_front:
    Fixed(anim.Filmstrip("battle/units/antitank_panzerjager_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_panzerjager_static_back:
    Fixed(im.Crop("battle/units/antitank_panzerjager_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_panzerjager_static_front:
    Fixed(im.Crop("battle/units/antitank_panzerjager_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_panzerjager_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 700
        ypos 120
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_panzerjager_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image antitank_panzerjager_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_panzerjager_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 180
        ypos 320

image antitank_panzerjager_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/antitank_panzerjager_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_panzerjager_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/antitank_panzerjager_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_panzerjager_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_panzerjager_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image antitank_panzerjager_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/antitank_panzerjager_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image antitank_panzerjager_heal_finalframe_back:
    Fixed(im.Crop("battle/units/antitank_panzerjager_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_panzerjager_heal_finalframe_front:
    Fixed(im.Crop("battle/units/antitank_panzerjager_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_renaultft
################################

image panzer_renaultft_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_renaultft_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultft_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_renaultft_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultft_static_back:
    Fixed(im.Crop("battle/units/panzer_renaultft_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultft_static_front:
    Fixed(im.Crop("battle/units/panzer_renaultft_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultft_main1_attack_back:
    contains:
        "offensive_mediumcannonblast_back"
        xpos 570
        ypos 170
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_renaultft_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_renaultft_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_renaultft_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_mediumcannonblast_front"
        xpos 268
        ypos 273

image panzer_renaultft_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_renaultft_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultft_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_renaultft_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultft_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_renaultft_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megaspeed", xsize=840, ysize=840)
    
image panzer_renaultft_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_renaultft_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megaspeed", xsize=840, ysize=840)
    
image panzer_renaultft_main1_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_renaultft_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultft_main1_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_renaultft_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultft_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_renaultft_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_renaultft_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_renaultft_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_renaultft_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_renaultft_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultft_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_renaultft_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultft_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_renaultft_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_renaultft_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_renaultft_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_renaultft_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_renaultft_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultft_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_renaultft_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_renaultr3540
################################

image panzer_renaultr3540_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_renaultr3540_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultr3540_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_renaultr3540_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultr3540_static_back:
    Fixed(im.Crop("battle/units/panzer_renaultr3540_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultr3540_static_front:
    Fixed(im.Crop("battle/units/panzer_renaultr3540_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultr3540_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 720
        ypos 65
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_renaultr3540_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_renaultr3540_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_renaultr3540_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 90
        ypos 320

image panzer_renaultr3540_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_renaultr3540_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultr3540_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_renaultr3540_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_renaultr3540_main2_attack_back:
    contains:
        "offensive_gunfire_back"
        xpos 473
        ypos 265
    contains:
        Fixed(im.Crop("battle/units/panzer_renaultr3540_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_renaultr3540_main2_attack_front:
    contains:
        "offensive_gunfire_front"
        xpos 274
        ypos 365
    contains:
        Fixed(im.Crop("battle/units/panzer_renaultr3540_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultr3540_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_renaultr3540_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultr3540_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_renaultr3540_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultr3540_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_renaultr3540_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_renaultr3540_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_renaultr3540_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_renaultr3540_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_renaultr3540_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultr3540_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_renaultr3540_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultr3540_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_renaultr3540_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megaspeed", xsize=840, ysize=840)
    
image panzer_renaultr3540_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_renaultr3540_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megaspeed", xsize=840, ysize=840)
    
image panzer_renaultr3540_main1_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_renaultr3540_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultr3540_main1_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_renaultr3540_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultr3540_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_renaultr3540_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_renaultr3540_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_renaultr3540_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_renaultr3540_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_renaultr3540_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultr3540_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_renaultr3540_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_renaultr35serpana
################################

image panzer_renaultr35serpana_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_renaultr35serpana_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultr35serpana_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_renaultr35serpana_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultr35serpana_static_back:
    Fixed(im.Crop("battle/units/panzer_renaultr35serpana_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultr35serpana_static_front:
    Fixed(im.Crop("battle/units/panzer_renaultr35serpana_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultr35serpana_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 720
        ypos 65
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_renaultr35serpana_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_renaultr35serpana_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_renaultr35serpana_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 90
        ypos 320

image panzer_renaultr35serpana_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_renaultr35serpana_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultr35serpana_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_renaultr35serpana_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_renaultr35serpana_main2_attack_back:
    contains:
        "offensive_gunfire_back"
        xpos 473
        ypos 265
    contains:
        Fixed(im.Crop("battle/units/panzer_renaultr35serpana_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_renaultr35serpana_main2_attack_front:
    contains:
        "offensive_gunfire_front"
        xpos 274
        ypos 365
    contains:
        Fixed(im.Crop("battle/units/panzer_renaultr35serpana_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultr35serpana_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_renaultr35serpana_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultr35serpana_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_renaultr35serpana_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultr35serpana_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_renaultr35serpana_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_renaultr35serpana_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_renaultr35serpana_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_renaultr35serpana_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_renaultr35serpana_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultr35serpana_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_renaultr35serpana_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultr35serpana_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_renaultr35serpana_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megaspeed", xsize=840, ysize=840)
    
image panzer_renaultr35serpana_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_renaultr35serpana_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megaspeed", xsize=840, ysize=840)
    
image panzer_renaultr35serpana_main1_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_renaultr35serpana_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultr35serpana_main1_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_renaultr35serpana_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultr35serpana_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_renaultr35serpana_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_renaultr35serpana_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_renaultr35serpana_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_renaultr35serpana_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_renaultr35serpana_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_renaultr35serpana_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_renaultr35serpana_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_semovente
################################

image panzer_semovente_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_semovente_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_semovente_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_semovente_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_semovente_static_back:
    Fixed(im.Crop("battle/units/panzer_semovente_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_semovente_static_front:
    Fixed(im.Crop("battle/units/panzer_semovente_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_semovente_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 740
        ypos 95
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_semovente_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_semovente_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_semovente_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 85
        ypos 370

image panzer_semovente_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_semovente_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_semovente_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_semovente_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_semovente_special1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_semovente_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_semovente_special1_attack_front:
    Fixed(anim.Filmstrip("battle/units/panzer_semovente_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_semovente_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_semovente_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_semovente_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_semovente_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_semovente_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_semovente_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_semovente_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_semovente_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_semovente_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_semovente_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_semovente_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_semovente_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_semovente_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_semovente_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_semovente_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_semovente_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_semovente_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_semovente_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_semovente_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_semovente_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_somuas35
################################

image panzer_somuas35_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_somuas35_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_somuas35_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_somuas35_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_somuas35_static_back:
    Fixed(im.Crop("battle/units/panzer_somuas35_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_somuas35_static_front:
    Fixed(im.Crop("battle/units/panzer_somuas35_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_somuas35_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 750
        ypos 20
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_somuas35_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_somuas35_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_somuas35_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 80
        ypos 300

image panzer_somuas35_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_somuas35_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_somuas35_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_somuas35_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_somuas35_main2_attack_back:
    contains:
        "offensive_gunfire_back"
        xpos 560
        ypos 265
    contains:
        Fixed(im.Crop("battle/units/panzer_somuas35_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_somuas35_main2_attack_front:
    contains:
        Fixed(im.Crop("battle/units/panzer_somuas35_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 340
        ypos 365
        
image panzer_somuas35_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_somuas35_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_somuas35_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_somuas35_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_somuas35_special1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_somuas35_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_somuas35_special1_attack_front:
    Fixed(anim.Filmstrip("battle/units/panzer_somuas35_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_somuas35_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_somuas35_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_somuas35_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_somuas35_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_somuas35_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_somuas35_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_somuas35_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_somuas35_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_somuas35_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_somuas35_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_somuas35_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_somuas35_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_somuas35_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_somuas35_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megapower", xsize=840, ysize=840)
    
image panzer_somuas35_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_somuas35_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megapower", xsize=840, ysize=840)
    
image panzer_somuas35_main1_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_somuas35_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_somuas35_main1_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_somuas35_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_somuas35_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_somuas35_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_somuas35_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_somuas35_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_somuas35_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_somuas35_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_somuas35_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_somuas35_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_stug3
################################

image panzer_stug3_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_stug3_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_stug3_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_stug3_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_stug3_static_back:
    Fixed(im.Crop("battle/units/panzer_stug3_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_stug3_static_front:
    Fixed(im.Crop("battle/units/panzer_stug3_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_stug3_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 715
        ypos 140
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_stug3_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_stug3_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_stug3_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 180
        ypos 345

image panzer_stug3_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_stug3_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_stug3_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_stug3_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_stug3_special1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_stug3_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_stug3_special1_attack_front:
    Fixed(anim.Filmstrip("battle/units/panzer_stug3_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_stug3_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_stug3_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_stug3_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_stug3_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_stug3_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_stug3_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_stug3_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_stug3_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_stug3_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_stug3_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_stug3_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_stug3_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_stug3_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_stug3_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megapower", xsize=840, ysize=840)
    
image panzer_stug3_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_stug3_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megapower", xsize=840, ysize=840)
    
image panzer_stug3_main1_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_stug3_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_stug3_main1_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_stug3_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_stug3_main2_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_stug3_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_stukatablets", xsize=840, ysize=840)
    
image panzer_stug3_main2_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_stug3_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_stukatablets", xsize=840, ysize=840)
    
image panzer_stug3_main2_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_stug3_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_stug3_main2_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_stug3_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_stug3_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_stug3_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_stug3_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_stug3_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_stug3_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_stug3_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_stug3_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_stug3_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_stug4
################################

image panzer_stug4_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_stug4_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_stug4_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_stug4_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_stug4_static_back:
    Fixed(im.Crop("battle/units/panzer_stug4_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_stug4_static_front:
    Fixed(im.Crop("battle/units/panzer_stug4_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_stug4_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 865
        ypos 72
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_stug4_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_stug4_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_stug4_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 0
        ypos 440

image panzer_stug4_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_stug4_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_stug4_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_stug4_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_stug4_main2_attack_back:
    contains:
        Fixed(im.Crop("battle/units/panzer_stug4_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_back"
        xpos 390
        ypos 300
        
image panzer_stug4_main2_attack_front:
    contains:
        Fixed(im.Crop("battle/units/panzer_stug4_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 355
        ypos 315
    
image panzer_stug4_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_stug4_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_stug4_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_stug4_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image panzer_stug4_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_stug4_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_stug4_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_stug4_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_stug4_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_stug4_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_stug4_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_stug4_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_stug4_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_stug4_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megapower", xsize=840, ysize=840)
    
image panzer_stug4_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_stug4_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megapower", xsize=840, ysize=840)
    
image panzer_stug4_main1_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_stug4_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_stug4_main1_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_stug4_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_stug4_main2_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_stug4_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_stukatablets", xsize=840, ysize=840)
    
image panzer_stug4_main2_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_stug4_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_stukatablets", xsize=840, ysize=840)
    
image panzer_stug4_main2_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_stug4_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_stug4_main2_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_stug4_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_stug4_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_stug4_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_stug4_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_stug4_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_stug4_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_stug4_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_stug4_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_stug4_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_su100
################################

image panzer_su100_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_su100_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_su100_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_su100_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_su100_static_back:
    Fixed(im.Crop("battle/units/panzer_su100_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_su100_static_front:
    Fixed(im.Crop("battle/units/panzer_su100_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_su100_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 835
        ypos 55
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_su100_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_su100_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_su100_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 10
        ypos 400

image panzer_su100_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_su100_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_su100_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_su100_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_su100_special1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_su100_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_su100_special1_attack_front:
    Fixed(anim.Filmstrip("battle/units/panzer_su100_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_su100_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_su100_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_su100_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_su100_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_su100_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_su100_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_su100_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_su100_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_su100_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_su100_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_su100_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_su100_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_su100_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_su100_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megapower", xsize=840, ysize=840)
    
image panzer_su100_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_su100_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megapower", xsize=840, ysize=840)
    
image panzer_su100_main1_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_su100_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_su100_main1_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_su100_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_su100_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_su100_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_su100_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_su100_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_su100_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_su100_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_su100_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_su100_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#antitank_t13
################################

image antitank_t13_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_t13_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_t13_walk_front:
    Fixed(anim.Filmstrip("battle/units/antitank_t13_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_t13_static_back:
    Fixed(im.Crop("battle/units/antitank_t13_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_t13_static_front:
    Fixed(im.Crop("battle/units/antitank_t13_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_t13_main1_attack_back:
    contains:
        "offensive_mediumcannonblast_back"
        xpos 650
        ypos 150
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_t13_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image antitank_t13_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_t13_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_mediumcannonblast_front"
        xpos 280
        ypos 300

image antitank_t13_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/antitank_t13_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_t13_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/antitank_t13_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image antitank_t13_main2_attack_back:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_t13_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_back"
        xpos 515
        ypos 295
        
image antitank_t13_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_t13_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 430
        ypos 340
    
image antitank_t13_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/antitank_t13_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_t13_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/antitank_t13_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_t13_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_t13_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megapower", xsize=840, ysize=840)
    
image antitank_t13_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/antitank_t13_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megapower", xsize=840, ysize=840)
    
image antitank_t13_main1_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/antitank_t13_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_t13_main1_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/antitank_t13_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_t13_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/antitank_t13_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image antitank_t13_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/antitank_t13_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image antitank_t13_heal_finalframe_back:
    Fixed(im.Crop("battle/units/antitank_t13_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image antitank_t13_heal_finalframe_front:
    Fixed(im.Crop("battle/units/antitank_t13_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_t34
################################

image panzer_t34_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_t34_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_t34_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_t34_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_t34_static_back:
    Fixed(im.Crop("battle/units/panzer_t34_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_t34_static_front:
    Fixed(im.Crop("battle/units/panzer_t34_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_t34_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 815
        ypos 65
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_t34_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_t34_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_t34_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 70
        ypos 370

image panzer_t34_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_t34_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_t34_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_t34_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_t34_main2_attack_back:
    contains:
        "offensive_gunfire_back"
        xpos 590
        ypos 343
    contains:
        Fixed(im.Crop("battle/units/panzer_t34_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_t34_main2_attack_front:
    contains:
        Fixed(im.Crop("battle/units/panzer_t34_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 310
        ypos 480
    
image panzer_t34_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_t34_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_t34_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_t34_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_t34_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_t34_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_t34_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_t34_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_t34_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_t34_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_t34_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_t34_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_t34_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_t34_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_xspeed", xsize=840, ysize=840)
    
image panzer_t34_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_t34_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_xspeed", xsize=840, ysize=840)
    
image panzer_t34_main1_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_t34_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_t34_main1_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_t34_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_t34_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_t34_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_t34_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_t34_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_t34_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_t34_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_t34_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_t34_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_t35
################################

image panzer_t35_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_t35_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_t35_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_t35_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_t35_static_back:
    Fixed(im.Crop("battle/units/panzer_t35_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_t35_static_front:
    Fixed(im.Crop("battle/units/panzer_t35_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_t35_main1_attack_back:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_t35_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_back"
        xpos 710
        ypos 40
        
image panzer_t35_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_t35_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 160
        ypos 250

image panzer_t35_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_t35_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_t35_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_t35_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_t35_main2_attack_back:
    contains:
        "offensive_smallcannonblast_back"
        xpos 725
        ypos 120
    contains:
        "offensive_smallcannonblast_back"
        xpos 740
        ypos 180
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_t35_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_t35_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_t35_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_smallcannonblast_front"
        xpos 60
        ypos 435
    contains:
        "offensive_smallcannonblast_front"
        xpos 170
        ypos 445
    
image panzer_t35_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_t35_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_t35_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_t35_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_t35_special1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_t35_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_t35_special1_attack_front:
    Fixed(anim.Filmstrip("battle/units/panzer_t35_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_t35_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_t35_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_t35_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_t35_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_t35_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_t35_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_t35_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_t35_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_t35_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_t35_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_t35_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_t35_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_t35_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_t35_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_xpower", xsize=840, ysize=840)
    
image panzer_t35_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_t35_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_xpower", xsize=840, ysize=840)
    
image panzer_t35_main1_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_t35_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_t35_main1_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_t35_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_t35_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_t35_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_t35_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_t35_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_t35_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_t35_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_t35_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_t35_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_tiger
################################

image panzer_tiger_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_tiger_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_tiger_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_tiger_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_tiger_static_back:
    Fixed(im.Crop("battle/units/panzer_tiger_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_tiger_static_front:
    Fixed(im.Crop("battle/units/panzer_tiger_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_tiger_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 870
        ypos 35
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_tiger_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_tiger_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_tiger_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 0
        ypos 405

image panzer_tiger_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_tiger_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_tiger_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_tiger_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_tiger_main2_attack_back:
    contains:
        "offensive_gunfire_back"
        xpos 631
        ypos 343
    contains:
        Fixed(im.Crop("battle/units/panzer_tiger_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_tiger_main2_attack_front:
    contains:
        Fixed(im.Crop("battle/units/panzer_tiger_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 240
        ypos 470
    
image panzer_tiger_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_tiger_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_tiger_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_tiger_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_tiger_special1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_tiger_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_tiger_special1_attack_front:
    Fixed(anim.Filmstrip("battle/units/panzer_tiger_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_tiger_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_tiger_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_tiger_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_tiger_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_tiger_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_tiger_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_tiger_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_tiger_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_tiger_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_tiger_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_tiger_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_tiger_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_tiger_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_tiger_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megaarmor", xsize=840, ysize=840)
    
image panzer_tiger_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_tiger_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_megaarmor", xsize=840, ysize=840)
    
image panzer_tiger_main1_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_tiger_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_tiger_main1_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_tiger_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_tiger_main2_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_tiger_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_stukatablets", xsize=840, ysize=840)
    
image panzer_tiger_main2_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_tiger_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_stukatablets", xsize=840, ysize=840)
    
image panzer_tiger_main2_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_tiger_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_tiger_main2_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_tiger_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_tiger_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_tiger_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_tiger_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_tiger_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_tiger_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_tiger_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_tiger_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_tiger_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_tks
################################

image panzer_tks_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_tks_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_tks_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_tks_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_tks_static_back:
    Fixed(im.Crop("battle/units/panzer_tks_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_tks_static_front:
    Fixed(im.Crop("battle/units/panzer_tks_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_tks_main1_attack_back:
    contains:
        "offensive_gunfire_big_back"
        xpos 690
        ypos 180
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_tks_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .03, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_tks_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_tks_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .03, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_big_front"              
        xpos 50
        ypos 495

image panzer_tks_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_tks_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_tks_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_tks_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image panzer_tks_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(im.Crop("battle/units/panzer_tks_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_tks_main2_attack_front:
    contains:
        Fixed(im.Crop("battle/units/panzer_tks_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0

image panzer_tks_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_tks_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_tks_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_tks_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_tks_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_tks_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_tks_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_tks_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_tks_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_tks_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_tks_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_tks_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_tks_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_tks_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_tks_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_tks_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_tks_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_tks_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_tks_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_tks_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_toldi
################################

image panzer_toldi_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_toldi_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_toldi_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_toldi_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_toldi_static_back:
    Fixed(im.Crop("battle/units/panzer_toldi_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_toldi_static_front:
    Fixed(im.Crop("battle/units/panzer_toldi_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_toldi_main1_attack_back:
    contains:
        "offensive_mediumcannonblast_back"
        xpos 670
        ypos 128
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_toldi_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_toldi_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_toldi_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_mediumcannonblast_front"
        xpos 175
        ypos 334

image panzer_toldi_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_toldi_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_toldi_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_toldi_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_toldi_main2_attack_back:
    contains:
        "offensive_gunfire_back"
        xpos 570
        ypos 270
    contains:
        Fixed(im.Crop("battle/units/panzer_toldi_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_toldi_main2_attack_front:
    contains:
        Fixed(im.Crop("battle/units/panzer_toldi_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 295
        ypos 403
    
image panzer_toldi_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_toldi_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_toldi_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_toldi_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_toldi_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_toldi_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_toldi_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_toldi_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_toldi_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_toldi_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_toldi_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_toldi_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_toldi_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_toldi_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_toldi_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_toldi_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_toldi_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_toldi_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_toldi_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_toldi_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_turan
################################

image panzer_turan_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_turan_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_turan_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_turan_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_turan_static_back:
    Fixed(im.Crop("battle/units/panzer_turan_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_turan_static_front:
    Fixed(im.Crop("battle/units/panzer_turan_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_turan_main1_attack_back:
    contains:
        "offensive_mediumcannonblast_back"
        xpos 685
        ypos 130
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_turan_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_turan_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_turan_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_mediumcannonblast_front"
        xpos 180
        ypos 345

image panzer_turan_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_turan_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_turan_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_turan_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_turan_main2_attack_back:
    contains:
        "offensive_gunfire_back"
        xpos 615
        ypos 323
    contains:
        Fixed(im.Crop("battle/units/panzer_turan_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_turan_main2_attack_front:
    contains:
        Fixed(im.Crop("battle/units/panzer_turan_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 320
        ypos 470
    
image panzer_turan_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_turan_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_turan_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_turan_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_turan_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_turan_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_turan_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_turan_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_turan_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_turan_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_turan_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_turan_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_turan_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_turan_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_turan_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_turan_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_turan_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_turan_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_turan_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_turan_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_ursus
################################

image panzer_ursus_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_ursus_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_ursus_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_ursus_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=820)
    
image panzer_ursus_static_back:
    Fixed(im.Crop("battle/units/panzer_ursus_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_ursus_static_front:
    Fixed(im.Crop("battle/units/panzer_ursus_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=820)
    
image panzer_ursus_main1_attack_back:
    contains:
        "offensive_smallcannonblast_back"
        xpos 530
        ypos 220
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_ursus_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_ursus_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_ursus_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=820)
    contains:
        "offensive_smallcannonblast_front"
        xpos 340
        ypos 290

image panzer_ursus_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_ursus_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_ursus_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_ursus_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=820)
    
image panzer_ursus_main2_attack_back:
    contains:
        Fixed(im.Crop("battle/units/panzer_ursus_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 180
        ypos 510
    contains:
        "offensive_gunfire_front"
        xpos 235
        ypos 335
        rotate 35
    contains:
        "offensive_gunfire_front"
        xpos 380
        ypos 415
        rotate -60
    contains:
        "offensive_gunfire_front"
        xpos 330
        ypos 285
        rotate 70
    
image panzer_ursus_main2_attack_front:
    contains:
        Fixed(im.Crop("battle/units/panzer_ursus_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=820)
    contains:
        "offensive_gunfire_back"
        xpos 535
        ypos 175
        rotate -35
    contains:
        "offensive_gunfire_back"
        xpos 625
        ypos 277
        rotate 31
    contains:
        "offensive_gunfire_back"
        xpos 480
        ypos 200
        rotate -60
    
image panzer_ursus_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_ursus_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_ursus_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_ursus_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=820)
    
image panzer_ursus_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_ursus_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_ursus_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_ursus_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=820), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=820)
    
image panzer_ursus_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_ursus_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_ursus_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_ursus_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=820)
    
################################
#panzer_valentine
################################

image panzer_valentine_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_valentine_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_valentine_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_valentine_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_valentine_static_back:
    Fixed(im.Crop("battle/units/panzer_valentine_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_valentine_static_front:
    Fixed(im.Crop("battle/units/panzer_valentine_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_valentine_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 765
        ypos 75
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_valentine_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_valentine_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_valentine_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 120
        ypos 345

image panzer_valentine_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_valentine_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_valentine_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_valentine_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_valentine_main2_attack_back:
    contains:
        Fixed(im.Crop("battle/units/panzer_valentine_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_back"
        xpos 470
        ypos 226
        
image panzer_valentine_main2_attack_front:
    contains:
        Fixed(im.Crop("battle/units/panzer_valentine_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_gunfire_front"
        xpos 278
        ypos 317
    
image panzer_valentine_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_valentine_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_valentine_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_valentine_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_valentine_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_valentine_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_valentine_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_valentine_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_valentine_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_valentine_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_valentine_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_valentine_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_valentine_main1_powerup_back:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_valentine_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_xspeed", xsize=840, ysize=840)
    
image panzer_valentine_main1_powerup_front:
    contains:
        "seal_powerup"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_valentine_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), boost_white)
    contains:
        Fixed("reaction_powerup_xspeed", xsize=840, ysize=840)
    
image panzer_valentine_main1_powerup_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_valentine_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_valentine_main1_powerup_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_valentine_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_valentine_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_valentine_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_valentine_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_valentine_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_valentine_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_valentine_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_valentine_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_valentine_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#panzer_zrinyi
################################

image panzer_zrinyi_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_zrinyi_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_zrinyi_walk_front:
    Fixed(anim.Filmstrip("battle/units/panzer_zrinyi_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_zrinyi_static_back:
    Fixed(im.Crop("battle/units/panzer_zrinyi_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_zrinyi_static_front:
    Fixed(im.Crop("battle/units/panzer_zrinyi_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_zrinyi_main1_attack_back:
    contains:
        "offensive_cannonblast_back"
        xpos 750
        ypos 100
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_zrinyi_main1_attack.png", (0, 840, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image panzer_zrinyi_main1_attack_front:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_zrinyi_main1_attack.png", (0, 0, 3360, 840)), (840, 840), (4, 1), .1, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_cannonblast_front"
        xpos 130
        ypos 350

image panzer_zrinyi_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_zrinyi_main1_attack.png", (2520, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_zrinyi_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_zrinyi_main1_attack.png", (2520, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_zrinyi_special2_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/panzer_zrinyi_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_zrinyi_special2_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/panzer_zrinyi_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image panzer_zrinyi_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_zrinyi_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_zrinyi_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_zrinyi_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_zrinyi_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/panzer_zrinyi_walk.png", (0, 840, 2520, 840)), (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_zrinyi_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/panzer_zrinyi_walk.png", (840, 840), (3, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_machineheal", xsize=840, ysize=840)
    
image panzer_zrinyi_heal_finalframe_back:
    Fixed(im.Crop("battle/units/panzer_zrinyi_walk.png", (0, 840, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image panzer_zrinyi_heal_finalframe_front:
    Fixed(im.Crop("battle/units/panzer_zrinyi_walk.png", (0, 0, 840, 840), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################################################
################################################################
################################################################
    #  ENEMIES  #
################################################################
################################################################
################################################################
    
################################
#polix_gunner_heer1
################################

image polix_gunner_heer1_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/polix_gunner_heer1_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image polix_gunner_heer1_walk_front:
    Fixed(anim.Filmstrip("battle/units/polix_gunner_heer1_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image polix_gunner_heer1_static_back:
    Fixed(im.Crop("battle/units/polix_gunner_heer1_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image polix_gunner_heer1_static_front:
    Fixed(im.Crop("battle/units/polix_gunner_heer1_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image polix_gunner_heer1_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/polix_gunner_heer1_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image polix_gunner_heer1_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/polix_gunner_heer1_main1_attack.png", (150, 243), (3, 1), .05, loop=False, xalign=0.492, yalign=0.5), xsize=840, ysize=840)

image polix_gunner_heer1_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/polix_gunner_heer1_main1_attack.png", (300, 243, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image polix_gunner_heer1_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/polix_gunner_heer1_main1_attack.png", (300, 0, 150, 243), xalign=0.492, yalign=0.5), xsize=840, ysize=840)
        
image polix_gunner_heer1_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/polix_gunner_heer1_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image polix_gunner_heer1_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/polix_gunner_heer1_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image polix_gunner_heer1_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/polix_gunner_heer1_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image polix_gunner_heer1_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/polix_gunner_heer1_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image polix_gunner_heer1_special1_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/polix_gunner_heer1_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .05, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image polix_gunner_heer1_special1_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/polix_gunner_heer1_walk.png", (126, 243), (4, 1), .05, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image polix_gunner_heer1_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/polix_gunner_heer1_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image polix_gunner_heer1_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/polix_gunner_heer1_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image polix_gunner_heer1_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/polix_gunner_heer1_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image polix_gunner_heer1_heal_front:
    contains:
        "seal_heal"
        xpos 320
        ypos 435
    contains:
        At(Fixed(anim.Filmstrip("battle/units/polix_gunner_heer1_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image polix_gunner_heer1_heal_finalframe_back:
    Fixed(im.Crop("battle/units/polix_gunner_heer1_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image polix_gunner_heer1_heal_finalframe_front:
    Fixed(im.Crop("battle/units/polix_gunner_heer1_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
################################
#polix_cavalry_heer1
################################

image polix_cavalry_heer1_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/polix_cavalry_heer1_walk.png", (0, 243, 636, 243)), (159, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image polix_cavalry_heer1_walk_front:
    Fixed(anim.Filmstrip("battle/units/polix_cavalry_heer1_walk.png", (159, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image polix_cavalry_heer1_static_back:
    Fixed(im.Crop("battle/units/polix_cavalry_heer1_walk.png", (0, 243, 159, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image polix_cavalry_heer1_static_front:
    Fixed(im.Crop("battle/units/polix_cavalry_heer1_walk.png", (0, 0, 159, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 

image polix_cavalry_heer1_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/polix_cavalry_heer1_main1_attack.png", (0, 243, 1908, 243)), (159, 243), (12, 1), .07, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image polix_cavalry_heer1_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/polix_cavalry_heer1_main1_attack.png", (159, 243), (12, 1), .07, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image polix_cavalry_heer1_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/polix_cavalry_heer1_main1_attack.png", (0, 243, 159, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image polix_cavalry_heer1_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/polix_cavalry_heer1_main1_attack.png", (0, 0, 159, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image polix_cavalry_heer1_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/polix_cavalry_heer1_walk.png", (0, 243, 636, 243)), (159, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image polix_cavalry_heer1_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/polix_cavalry_heer1_walk.png", (159, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image polix_cavalry_heer1_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/polix_cavalry_heer1_walk.png", (0, 243, 159, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image polix_cavalry_heer1_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/polix_cavalry_heer1_walk.png", (0, 0, 159, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image polix_cavalry_heer1_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/polix_cavalry_heer1_walk.png", (0, 243, 636, 243)), (159, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image polix_cavalry_heer1_heal_front:
    contains:
        "seal_heal"
        xpos 340
        ypos 435
    contains:
        At(Fixed(anim.Filmstrip("battle/units/polix_cavalry_heer1_walk.png", (159, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image polix_cavalry_heer1_heal_finalframe_back:
    Fixed(im.Crop("battle/units/polix_cavalry_heer1_walk.png", (0, 243, 159, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image polix_cavalry_heer1_heal_finalframe_front:
    Fixed(im.Crop("battle/units/polix_cavalry_heer1_walk.png", (0, 0, 159, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
################################
#dania_gunner_heer2
################################

image dania_gunner_heer2_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/dania_gunner_heer2_walk.png", (0, 243, 672, 243)), (168, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image dania_gunner_heer2_walk_front:
    Fixed(anim.Filmstrip("battle/units/dania_gunner_heer2_walk.png", (168, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image dania_gunner_heer2_static_back:
    Fixed(im.Crop("battle/units/dania_gunner_heer2_walk.png", (0, 243, 168, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image dania_gunner_heer2_static_front:
    Fixed(im.Crop("battle/units/dania_gunner_heer2_walk.png", (0, 0, 168, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image dania_gunner_heer2_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/dania_gunner_heer2_main1_attack.png", (0, 243, 549, 243)), (183, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image dania_gunner_heer2_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/dania_gunner_heer2_main1_attack.png", (183, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image dania_gunner_heer2_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/dania_gunner_heer2_main1_attack.png", (366, 243, 183, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image dania_gunner_heer2_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/dania_gunner_heer2_main1_attack.png", (366, 0, 183, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image dania_gunner_heer2_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/dania_gunner_heer2_walk.png", (0, 243, 672, 243)), (168, 243), (4, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image dania_gunner_heer2_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/dania_gunner_heer2_walk.png", (168, 243), (4, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image dania_gunner_heer2_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/dania_gunner_heer2_walk.png", (504, 243, 168, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image dania_gunner_heer2_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/dania_gunner_heer2_walk.png", (504, 0, 168, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image dania_gunner_heer2_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/dania_gunner_heer2_walk.png", (0, 243, 672, 243)), (168, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image dania_gunner_heer2_heal_front:
    contains:
        "seal_heal"
        xpos 345
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/dania_gunner_heer2_walk.png", (168, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image dania_gunner_heer2_heal_finalframe_back:
    Fixed(im.Crop("battle/units/dania_gunner_heer2_walk.png", (0, 243, 168, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image dania_gunner_heer2_heal_finalframe_front:
    Fixed(im.Crop("battle/units/dania_gunner_heer2_walk.png", (0, 0, 168, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#norda_gunner_heer2
################################

image norda_gunner_heer2_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/norda_gunner_heer2_walk.png", (0, 243, 624, 243)), (156, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image norda_gunner_heer2_walk_front:
    Fixed(anim.Filmstrip("battle/units/norda_gunner_heer2_walk.png", (156, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image norda_gunner_heer2_static_back:
    Fixed(im.Crop("battle/units/norda_gunner_heer2_walk.png", (0, 243, 156, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image norda_gunner_heer2_static_front:
    Fixed(im.Crop("battle/units/norda_gunner_heer2_walk.png", (0, 0, 156, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image norda_gunner_heer2_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/norda_gunner_heer2_main1_attack.png", (0, 243, 540, 243)), (180, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image norda_gunner_heer2_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/norda_gunner_heer2_main1_attack.png", (180, 243), (3, 1), .05, xalign=0.49, yalign=0.5), xsize=840, ysize=840)
    
image norda_gunner_heer2_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/norda_gunner_heer2_main1_attack.png", (360, 243, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image norda_gunner_heer2_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/norda_gunner_heer2_main1_attack.png", (360, 0, 180, 243), xalign=0.49, yalign=0.5), xsize=840, ysize=840)
    
image norda_gunner_heer2_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/norda_gunner_heer2_walk.png", (0, 243, 624, 243)), (156, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image norda_gunner_heer2_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/norda_gunner_heer2_walk.png", (156, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image norda_gunner_heer2_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/norda_gunner_heer2_walk.png", (0, 243, 156, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image norda_gunner_heer2_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/norda_gunner_heer2_walk.png", (0, 0, 156, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image norda_gunner_heer2_special2_attack_back:
    contains:
        "reaction_snow"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        "offensive_snowball_back"
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/norda_gunner_heer2_walk.png", (0, 243, 624, 243)), (156, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image norda_gunner_heer2_special2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/norda_gunner_heer2_walk.png", (156, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_snowball_front"
        xpos 170
    contains:
        "reaction_snow"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    
image norda_gunner_heer2_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/norda_gunner_heer2_walk.png", (0, 243, 156, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image norda_gunner_heer2_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/norda_gunner_heer2_walk.png", (0, 0, 156, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image norda_gunner_heer2_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/norda_gunner_heer2_walk.png", (0, 243, 624, 243)), (156, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image norda_gunner_heer2_heal_front:
    contains:
        "seal_heal"
        xpos 345
        ypos 435
    contains:
        At(Fixed(anim.Filmstrip("battle/units/norda_gunner_heer2_walk.png", (156, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image norda_gunner_heer2_heal_finalframe_back:
    Fixed(im.Crop("battle/units/norda_gunner_heer2_walk.png", (0, 243, 156, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image norda_gunner_heer2_heal_finalframe_front:
    Fixed(im.Crop("battle/units/norda_gunner_heer2_walk.png", (0, 0, 156, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#norda_marksman_heer2
################################

image norda_marksman_heer2_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/norda_marksman_heer2_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image norda_marksman_heer2_walk_front:
    Fixed(anim.Filmstrip("battle/units/norda_marksman_heer2_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image norda_marksman_heer2_static_back:
    Fixed(im.Crop("battle/units/norda_marksman_heer2_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image norda_marksman_heer2_static_front:
    Fixed(im.Crop("battle/units/norda_marksman_heer2_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image norda_marksman_heer2_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/norda_marksman_heer2_main1_attack.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image norda_marksman_heer2_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/norda_marksman_heer2_main1_attack.png", (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image norda_marksman_heer2_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/norda_marksman_heer2_main1_attack.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image norda_marksman_heer2_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/norda_marksman_heer2_main1_attack.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image norda_marksman_heer2_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/norda_marksman_heer2_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image norda_marksman_heer2_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/norda_marksman_heer2_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    
image norda_marksman_heer2_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/norda_marksman_heer2_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image norda_marksman_heer2_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/norda_marksman_heer2_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image norda_marksman_heer2_special2_attack_back:
    contains:
        "reaction_snow"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        "offensive_snowball_back"
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/norda_marksman_heer2_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image norda_marksman_heer2_special2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/norda_marksman_heer2_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_snowball_front"
        xpos 170
    contains:
        "reaction_snow"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    
image norda_marksman_heer2_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/norda_marksman_heer2_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image norda_marksman_heer2_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/norda_marksman_heer2_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image norda_marksman_heer2_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/norda_marksman_heer2_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image norda_marksman_heer2_heal_front:
    contains:
        "seal_heal"
        xpos 350
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/norda_marksman_heer2_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image norda_marksman_heer2_heal_finalframe_back:
    Fixed(im.Crop("battle/units/norda_marksman_heer2_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image norda_marksman_heer2_heal_finalframe_front:
    Fixed(im.Crop("battle/units/norda_marksman_heer2_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#batavia_gunner_heer3
################################

image batavia_gunner_heer3_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/batavia_gunner_heer3_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image batavia_gunner_heer3_walk_front:
    Fixed(anim.Filmstrip("battle/units/batavia_gunner_heer3_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image batavia_gunner_heer3_static_back:
    Fixed(im.Crop("battle/units/batavia_gunner_heer3_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image batavia_gunner_heer3_static_front:
    Fixed(im.Crop("battle/units/batavia_gunner_heer3_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image batavia_gunner_heer3_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/batavia_gunner_heer3_main1_attack.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image batavia_gunner_heer3_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/batavia_gunner_heer3_main1_attack.png", (171, 244.5), (4, 1), .05, loop=False, xalign=0.505, yalign=0.5), xsize=840, ysize=840)

image batavia_gunner_heer3_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/batavia_gunner_heer3_main1_attack.png", (513, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image batavia_gunner_heer3_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/batavia_gunner_heer3_main1_attack.png", (513, 0, 171, 244.5), xalign=0.505, yalign=0.5), xsize=840, ysize=840)
    
image batavia_gunner_heer3_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/batavia_gunner_heer3_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image batavia_gunner_heer3_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/batavia_gunner_heer3_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    
image batavia_gunner_heer3_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/batavia_gunner_heer3_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image batavia_gunner_heer3_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/batavia_gunner_heer3_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image batavia_gunner_heer3_special3_attack_back:
    contains:
        "offensive_clog_back"
    contains:
        "reaction_hit"
        xalign 0.69 yalign 0.08 alpha 0 xzoom -1
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/batavia_gunner_heer3_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image batavia_gunner_heer3_special3_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/batavia_gunner_heer3_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_clog_front"
    contains:
        "reaction_hit"
        xalign -0.28 yalign 0.67 alpha 0
        pause 0.75
        alpha 1.0
    
image batavia_gunner_heer3_special3_attack_finalframe_back:
    Fixed(im.Crop("battle/units/batavia_gunner_heer3_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image batavia_gunner_heer3_special3_attack_finalframe_front:
    Fixed(im.Crop("battle/units/batavia_gunner_heer3_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image batavia_gunner_heer3_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/batavia_gunner_heer3_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image batavia_gunner_heer3_heal_front:
    contains:
        "seal_heal"
        xpos 340
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/batavia_gunner_heer3_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image batavia_gunner_heer3_heal_finalframe_back:
    Fixed(im.Crop("battle/units/batavia_gunner_heer3_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image batavia_gunner_heer3_heal_finalframe_front:
    Fixed(im.Crop("battle/units/batavia_gunner_heer3_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#belgae_gunner_heer3
################################

image belgae_gunner_heer3_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/belgae_gunner_heer3_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image belgae_gunner_heer3_walk_front:
    Fixed(anim.Filmstrip("battle/units/belgae_gunner_heer3_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image belgae_gunner_heer3_static_back:
    Fixed(im.Crop("battle/units/belgae_gunner_heer3_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image belgae_gunner_heer3_static_front:
    Fixed(im.Crop("battle/units/belgae_gunner_heer3_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image belgae_gunner_heer3_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/belgae_gunner_heer3_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image belgae_gunner_heer3_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/belgae_gunner_heer3_main1_attack.png", (150, 243), (3, 1), .05, xalign=0.49, yalign=0.5), xsize=840, ysize=840)

image belgae_gunner_heer3_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/belgae_gunner_heer3_main1_attack.png", (300, 243, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image belgae_gunner_heer3_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/belgae_gunner_heer3_main1_attack.png", (300, 0, 150, 243), xalign=0.49, yalign=0.5), xsize=840, ysize=840)
        
image belgae_gunner_heer3_main2_attack_back:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/belgae_gunner_heer3_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_landmine"
        xalign 0.77 yalign -0.6

image belgae_gunner_heer3_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/belgae_gunner_heer3_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_landmine"
        xalign -0.6 yalign 0.52
        
image belgae_gunner_heer3_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/belgae_gunner_heer3_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image belgae_gunner_heer3_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/belgae_gunner_heer3_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image belgae_gunner_heer3_special3_attack_back:
    contains:
        "offensive_sprout_back"
    contains:
        "reaction_hit"
        xalign 0.69 yalign 0.08 alpha 0 xzoom -1
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/belgae_gunner_heer3_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image belgae_gunner_heer3_special3_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/belgae_gunner_heer3_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_sprout_front"
        xpos 100
    contains:
        "reaction_hit"
        xalign -0.28 yalign 0.67 alpha 0
        pause 0.75
        alpha 1.0
        
image belgae_gunner_heer3_special3_attack_finalframe_back:
    Fixed(im.Crop("battle/units/belgae_gunner_heer3_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image belgae_gunner_heer3_special3_attack_finalframe_front:
    Fixed(im.Crop("battle/units/belgae_gunner_heer3_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image belgae_gunner_heer3_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/belgae_gunner_heer3_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image belgae_gunner_heer3_heal_front:
    contains:
        "seal_heal"
        xpos 320
        ypos 435
    contains:
        At(Fixed(anim.Filmstrip("battle/units/belgae_gunner_heer3_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image belgae_gunner_heer3_heal_finalframe_back:
    Fixed(im.Crop("battle/units/belgae_gunner_heer3_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image belgae_gunner_heer3_heal_finalframe_front:
    Fixed(im.Crop("battle/units/belgae_gunner_heer3_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
################################
#franzo_gunner_heer2
################################

image franzo_gunner_heer2_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/franzo_gunner_heer2_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image franzo_gunner_heer2_walk_front:
    Fixed(anim.Filmstrip("battle/units/franzo_gunner_heer2_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image franzo_gunner_heer2_static_back:
    Fixed(im.Crop("battle/units/franzo_gunner_heer2_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image franzo_gunner_heer2_static_front:
    Fixed(im.Crop("battle/units/franzo_gunner_heer2_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image franzo_gunner_heer2_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/franzo_gunner_heer2_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image franzo_gunner_heer2_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/franzo_gunner_heer2_main1_attack.png", (150, 243), (3, 1), .05, xalign=0.49, yalign=0.5), xsize=840, ysize=840)

image franzo_gunner_heer2_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/franzo_gunner_heer2_main1_attack.png", (300, 243, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image franzo_gunner_heer2_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/franzo_gunner_heer2_main1_attack.png", (300, 0, 150, 243), xalign=0.49, yalign=0.5), xsize=840, ysize=840)
        
image franzo_gunner_heer2_main2_attack_back:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/franzo_gunner_heer2_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_landmine"
        xalign 0.77 yalign -0.6

image franzo_gunner_heer2_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/franzo_gunner_heer2_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_landmine"
        xalign -0.6 yalign 0.52
        
image franzo_gunner_heer2_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/franzo_gunner_heer2_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image franzo_gunner_heer2_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/franzo_gunner_heer2_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image franzo_gunner_heer2_special2_attack_back:
    contains:
        "offensive_baguette_back"
    contains:
        "reaction_hit"
        xalign 0.69 yalign 0.08 alpha 0 xzoom -1
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/franzo_gunner_heer2_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image franzo_gunner_heer2_special2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/franzo_gunner_heer2_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_baguette_front"
    contains:
        "reaction_hit"
        xalign -0.28 yalign 0.67 alpha 0
        pause 0.75
        alpha 1.0
    
image franzo_gunner_heer2_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/franzo_gunner_heer2_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image franzo_gunner_heer2_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/franzo_gunner_heer2_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image franzo_gunner_heer2_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/franzo_gunner_heer2_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image franzo_gunner_heer2_heal_front:
    contains:
        "seal_heal"
        xpos 320
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/franzo_gunner_heer2_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image franzo_gunner_heer2_heal_finalframe_back:
    Fixed(im.Crop("battle/units/franzo_gunner_heer2_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image franzo_gunner_heer2_heal_finalframe_front:
    Fixed(im.Crop("battle/units/franzo_gunner_heer2_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
################################
#franzo_gunner_heer3
################################

image franzo_gunner_heer3_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/franzo_gunner_heer3_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image franzo_gunner_heer3_walk_front:
    Fixed(anim.Filmstrip("battle/units/franzo_gunner_heer3_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image franzo_gunner_heer3_static_back:
    Fixed(im.Crop("battle/units/franzo_gunner_heer3_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image franzo_gunner_heer3_static_front:
    Fixed(im.Crop("battle/units/franzo_gunner_heer3_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image franzo_gunner_heer3_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/franzo_gunner_heer3_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image franzo_gunner_heer3_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/franzo_gunner_heer3_main1_attack.png", (150, 243), (3, 1), .05, xalign=0.49, yalign=0.5), xsize=840, ysize=840)

image franzo_gunner_heer3_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/franzo_gunner_heer3_main1_attack.png", (300, 243, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image franzo_gunner_heer3_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/franzo_gunner_heer3_main1_attack.png", (300, 0, 150, 243), xalign=0.49, yalign=0.5), xsize=840, ysize=840)
        
image franzo_gunner_heer3_main2_attack_back:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/franzo_gunner_heer3_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_landmine"
        xalign 0.77 yalign -0.6

image franzo_gunner_heer3_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/franzo_gunner_heer3_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_landmine"
        xalign -0.6 yalign 0.52
        
image franzo_gunner_heer3_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/franzo_gunner_heer3_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image franzo_gunner_heer3_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/franzo_gunner_heer3_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image franzo_gunner_heer3_special2_attack_back:
    contains:
        "offensive_baguette_back"
    contains:
        "reaction_hit"
        xalign 0.69 yalign 0.08 alpha 0 xzoom -1
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/franzo_gunner_heer3_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image franzo_gunner_heer3_special2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/franzo_gunner_heer3_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_baguette_front"
    contains:
        "reaction_hit"
        xalign -0.28 yalign 0.67 alpha 0
        pause 0.75
        alpha 1.0
    
image franzo_gunner_heer3_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/franzo_gunner_heer3_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image franzo_gunner_heer3_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/franzo_gunner_heer3_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image franzo_gunner_heer3_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/franzo_gunner_heer3_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image franzo_gunner_heer3_heal_front:
    contains:
        "seal_heal"
        xpos 320
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/franzo_gunner_heer3_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image franzo_gunner_heer3_heal_finalframe_back:
    Fixed(im.Crop("battle/units/franzo_gunner_heer3_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image franzo_gunner_heer3_heal_finalframe_front:
    Fixed(im.Crop("battle/units/franzo_gunner_heer3_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
################################
#franzo_marksman_heer3
################################

image franzo_marksman_heer3_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/franzo_marksman_heer3_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image franzo_marksman_heer3_walk_front:
    Fixed(anim.Filmstrip("battle/units/franzo_marksman_heer3_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image franzo_marksman_heer3_static_back:
    Fixed(im.Crop("battle/units/franzo_marksman_heer3_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image franzo_marksman_heer3_static_front:
    Fixed(im.Crop("battle/units/franzo_marksman_heer3_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image franzo_marksman_heer3_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/franzo_marksman_heer3_main1_attack.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image franzo_marksman_heer3_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/franzo_marksman_heer3_main1_attack.png", (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image franzo_marksman_heer3_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/franzo_marksman_heer3_main1_attack.png", (513, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image franzo_marksman_heer3_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/franzo_marksman_heer3_main1_attack.png", (513, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image franzo_marksman_heer3_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/franzo_marksman_heer3_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image franzo_marksman_heer3_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/franzo_marksman_heer3_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    
image franzo_marksman_heer3_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/franzo_marksman_heer3_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image franzo_marksman_heer3_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/franzo_marksman_heer3_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image franzo_marksman_heer3_special2_attack_back:
    contains:
        "offensive_baguette_back"
    contains:
        "reaction_hit"
        xalign 0.69 yalign 0.08 alpha 0 xzoom -1
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/franzo_marksman_heer3_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image franzo_marksman_heer3_special2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/franzo_marksman_heer3_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_baguette_front"
    contains:
        "reaction_hit"
        xalign -0.28 yalign 0.67 alpha 0
        pause 0.75
        alpha 1.0
    
image franzo_marksman_heer3_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/franzo_marksman_heer3_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image franzo_marksman_heer3_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/franzo_marksman_heer3_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image franzo_marksman_heer3_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/franzo_marksman_heer3_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image franzo_marksman_heer3_heal_front:
    contains:
        "seal_heal"
        xpos 340
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/franzo_marksman_heer3_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image franzo_marksman_heer3_heal_finalframe_back:
    Fixed(im.Crop("battle/units/franzo_marksman_heer3_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image franzo_marksman_heer3_heal_finalframe_front:
    Fixed(im.Crop("battle/units/franzo_marksman_heer3_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#franzo_gunner_heer4
################################

image franzo_gunner_heer4_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/franzo_gunner_heer4_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image franzo_gunner_heer4_walk_front:
    Fixed(anim.Filmstrip("battle/units/franzo_gunner_heer4_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image franzo_gunner_heer4_static_back:
    Fixed(im.Crop("battle/units/franzo_gunner_heer4_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image franzo_gunner_heer4_static_front:
    Fixed(im.Crop("battle/units/franzo_gunner_heer4_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image franzo_gunner_heer4_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/franzo_gunner_heer4_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, xalign=0.51, yalign=0.5), xsize=840, ysize=840)
    
image franzo_gunner_heer4_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/franzo_gunner_heer4_main1_attack.png", (150, 243), (3, 1), .05, xalign=0.49, yalign=0.5), xsize=840, ysize=840)

image franzo_gunner_heer4_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/franzo_gunner_heer4_main1_attack.png", (300, 243, 150, 243), xalign=0.51, yalign=0.5), xsize=840, ysize=840)

image franzo_gunner_heer4_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/franzo_gunner_heer4_main1_attack.png", (300, 0, 150, 243), xalign=0.49, yalign=0.5), xsize=840, ysize=840)
        
image franzo_gunner_heer4_main2_attack_back:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/franzo_gunner_heer4_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_landmine"
        xalign 0.77 yalign -0.6

image franzo_gunner_heer4_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/franzo_gunner_heer4_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_landmine"
        xalign -0.6 yalign 0.52
        
image franzo_gunner_heer4_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/franzo_gunner_heer4_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image franzo_gunner_heer4_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/franzo_gunner_heer4_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image franzo_gunner_heer4_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/franzo_gunner_heer4_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image franzo_gunner_heer4_heal_front:
    contains:
        "seal_heal"
        xpos 325
        ypos 435
    contains:
        At(Fixed(anim.Filmstrip("battle/units/franzo_gunner_heer4_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image franzo_gunner_heer4_heal_finalframe_back:
    Fixed(im.Crop("battle/units/franzo_gunner_heer4_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image franzo_gunner_heer4_heal_finalframe_front:
    Fixed(im.Crop("battle/units/franzo_gunner_heer4_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)     
    
################################
#franzo_marksman_heer4
################################

image franzo_marksman_heer4_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/franzo_marksman_heer4_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image franzo_marksman_heer4_walk_front:
    Fixed(anim.Filmstrip("battle/units/franzo_marksman_heer4_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image franzo_marksman_heer4_static_back:
    Fixed(im.Crop("battle/units/franzo_marksman_heer4_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image franzo_marksman_heer4_static_front:
    Fixed(im.Crop("battle/units/franzo_marksman_heer4_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image franzo_marksman_heer4_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/franzo_marksman_heer4_main1_attack.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image franzo_marksman_heer4_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/franzo_marksman_heer4_main1_attack.png", (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image franzo_marksman_heer4_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/franzo_marksman_heer4_main1_attack.png", (513, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image franzo_marksman_heer4_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/franzo_marksman_heer4_main1_attack.png", (513, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image franzo_marksman_heer4_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/franzo_marksman_heer4_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image franzo_marksman_heer4_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/franzo_marksman_heer4_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    
image franzo_marksman_heer4_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/franzo_marksman_heer4_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image franzo_marksman_heer4_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/franzo_marksman_heer4_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image franzo_marksman_heer4_heal_back:
    contains:
        "seal_heal"
        xpos 300
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/franzo_marksman_heer4_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image franzo_marksman_heer4_heal_front:
    contains:
        "seal_heal"
        xpos 350
        ypos 435
    contains:
        At(Fixed(anim.Filmstrip("battle/units/franzo_marksman_heer4_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image franzo_marksman_heer4_heal_finalframe_back:
    Fixed(im.Crop("battle/units/franzo_marksman_heer4_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image franzo_marksman_heer4_heal_finalframe_front:
    Fixed(im.Crop("battle/units/franzo_marksman_heer4_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#westafrikaa_gunner_heer3
################################

image westafrikaa_gunner_heer3_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/westafrikaa_gunner_heer3_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image westafrikaa_gunner_heer3_walk_front:
    Fixed(anim.Filmstrip("battle/units/westafrikaa_gunner_heer3_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image westafrikaa_gunner_heer3_static_back:
    Fixed(im.Crop("battle/units/westafrikaa_gunner_heer3_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image westafrikaa_gunner_heer3_static_front:
    Fixed(im.Crop("battle/units/westafrikaa_gunner_heer3_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image westafrikaa_gunner_heer3_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/westafrikaa_gunner_heer3_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image westafrikaa_gunner_heer3_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/westafrikaa_gunner_heer3_main1_attack.png", (150, 243), (3, 1), .05, xalign=0.49, yalign=0.5), xsize=840, ysize=840)

image westafrikaa_gunner_heer3_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/westafrikaa_gunner_heer3_main1_attack.png", (300, 243, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image westafrikaa_gunner_heer3_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/westafrikaa_gunner_heer3_main1_attack.png", (300, 0, 150, 243), xalign=0.49, yalign=0.5), xsize=840, ysize=840)
        
image westafrikaa_gunner_heer3_main2_attack_back:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/westafrikaa_gunner_heer3_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_landmine"
        xalign 0.77 yalign -0.6

image westafrikaa_gunner_heer3_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/westafrikaa_gunner_heer3_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_landmine"
        xalign -0.6 yalign 0.52
        
image westafrikaa_gunner_heer3_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/westafrikaa_gunner_heer3_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image westafrikaa_gunner_heer3_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/westafrikaa_gunner_heer3_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image westafrikaa_gunner_heer3_special2_attack_back:
    contains:
        "offensive_baguette_back"
    contains:
        "reaction_hit"
        xalign 0.69 yalign 0.08 alpha 0 xzoom -1
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/westafrikaa_gunner_heer3_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image westafrikaa_gunner_heer3_special2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/westafrikaa_gunner_heer3_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_baguette_front"
    contains:
        "reaction_hit"
        xalign -0.28 yalign 0.67 alpha 0
        pause 0.75
        alpha 1.0
    
image westafrikaa_gunner_heer3_special2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/westafrikaa_gunner_heer3_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image westafrikaa_gunner_heer3_special2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/westafrikaa_gunner_heer3_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image westafrikaa_gunner_heer3_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/westafrikaa_gunner_heer3_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image westafrikaa_gunner_heer3_heal_front:
    contains:
        "seal_heal"
        xpos 320
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/westafrikaa_gunner_heer3_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image westafrikaa_gunner_heer3_heal_finalframe_back:
    Fixed(im.Crop("battle/units/westafrikaa_gunner_heer3_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image westafrikaa_gunner_heer3_heal_finalframe_front:
    Fixed(im.Crop("battle/units/westafrikaa_gunner_heer3_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
################################
#serpana_gunner_heer5
################################

image serpana_gunner_heer5_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/serpana_gunner_heer5_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image serpana_gunner_heer5_walk_front:
    Fixed(anim.Filmstrip("battle/units/serpana_gunner_heer5_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image serpana_gunner_heer5_static_back:
    Fixed(im.Crop("battle/units/serpana_gunner_heer5_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image serpana_gunner_heer5_static_front:
    Fixed(im.Crop("battle/units/serpana_gunner_heer5_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image serpana_gunner_heer5_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/serpana_gunner_heer5_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image serpana_gunner_heer5_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/serpana_gunner_heer5_main1_attack.png", (150, 243), (3, 1), .05, xalign=0.49, yalign=0.5), xsize=840, ysize=840)

image serpana_gunner_heer5_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/serpana_gunner_heer5_main1_attack.png", (300, 243, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image serpana_gunner_heer5_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/serpana_gunner_heer5_main1_attack.png", (300, 0, 150, 243), xalign=0.49, yalign=0.5), xsize=840, ysize=840)
        
image serpana_gunner_heer5_main2_attack_back:
    contains:
        "offensive_stielhandgranate_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/serpana_gunner_heer5_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image serpana_gunner_heer5_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/serpana_gunner_heer5_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_stielhandgranate_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image serpana_gunner_heer5_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/serpana_gunner_heer5_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image serpana_gunner_heer5_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/serpana_gunner_heer5_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image serpana_gunner_heer5_special1_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/serpana_gunner_heer5_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .02, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image serpana_gunner_heer5_special1_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/serpana_gunner_heer5_walk.png", (126, 243), (4, 1), .02, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image serpana_gunner_heer5_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/serpana_gunner_heer5_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image serpana_gunner_heer5_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/serpana_gunner_heer5_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image serpana_gunner_heer5_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/serpana_gunner_heer5_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image serpana_gunner_heer5_heal_front:
    contains:
        "seal_heal"
        xpos 320
        ypos 435
    contains:
        At(Fixed(anim.Filmstrip("battle/units/serpana_gunner_heer5_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image serpana_gunner_heer5_heal_finalframe_back:
    Fixed(im.Crop("battle/units/serpana_gunner_heer5_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image serpana_gunner_heer5_heal_finalframe_front:
    Fixed(im.Crop("battle/units/serpana_gunner_heer5_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
################################
#serpana_antitank_heer5
################################

image serpana_antitank_heer5_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/serpana_antitank_heer5_walk.png", (0, 243, 720, 243)), (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image serpana_antitank_heer5_walk_front:
    Fixed(anim.Filmstrip("battle/units/serpana_antitank_heer5_walk.png", (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image serpana_antitank_heer5_static_back:
    Fixed(im.Crop("battle/units/serpana_antitank_heer5_walk.png", (0, 243, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image serpana_antitank_heer5_static_front:
    Fixed(im.Crop("battle/units/serpana_antitank_heer5_walk.png", (0, 0, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image serpana_antitank_heer5_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/serpana_antitank_heer5_main1_attack.png", (0, 244.5, 717, 244.5)), (179.25, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image serpana_antitank_heer5_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/serpana_antitank_heer5_main1_attack.png", (179.25, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image serpana_antitank_heer5_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/serpana_antitank_heer5_main1_attack.png", (537.75, 244.5, 179.25, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image serpana_antitank_heer5_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/serpana_antitank_heer5_main1_attack.png", (537.75, 0, 179.25, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image serpana_antitank_heer5_main2_attack_back:
    contains:
        "offensive_stielhandgranate_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/serpana_antitank_heer5_walk.png", (0, 243, 720, 243)), (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image serpana_antitank_heer5_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/serpana_antitank_heer5_walk.png", (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_stielhandgranate_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    
image serpana_antitank_heer5_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/serpana_antitank_heer5_walk.png", (0, 243, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image serpana_antitank_heer5_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/serpana_antitank_heer5_walk.png", (0, 0, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image serpana_antitank_heer5_special1_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/serpana_antitank_heer5_walk.png", (0, 243, 720, 243)), (180, 243), (4, 1), .02, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)

image serpana_antitank_heer5_special1_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/serpana_antitank_heer5_walk.png", (180, 243), (4, 1), .02, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image serpana_antitank_heer5_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/serpana_antitank_heer5_walk.png", (0, 243, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image serpana_antitank_heer5_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/serpana_antitank_heer5_walk.png", (0, 0, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image serpana_antitank_heer5_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/serpana_antitank_heer5_walk.png", (0, 243, 720, 243)), (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image serpana_antitank_heer5_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/serpana_antitank_heer5_walk.png", (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image serpana_antitank_heer5_heal_finalframe_back:
    Fixed(im.Crop("battle/units/serpana_antitank_heer5_walk.png", (0, 243, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image serpana_antitank_heer5_heal_finalframe_front:
    Fixed(im.Crop("battle/units/serpana_antitank_heer5_walk.png", (0, 0, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#shifta_gunner_heer4
################################

image shifta_gunner_heer4_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/shifta_gunner_heer4_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image shifta_gunner_heer4_walk_front:
    Fixed(anim.Filmstrip("battle/units/shifta_gunner_heer4_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image shifta_gunner_heer4_static_back:
    Fixed(im.Crop("battle/units/shifta_gunner_heer4_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image shifta_gunner_heer4_static_front:
    Fixed(im.Crop("battle/units/shifta_gunner_heer4_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image shifta_gunner_heer4_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/shifta_gunner_heer4_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image shifta_gunner_heer4_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/shifta_gunner_heer4_main1_attack.png", (150, 243), (3, 1), .05, xalign=0.49, yalign=0.5), xsize=840, ysize=840)

image shifta_gunner_heer4_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/shifta_gunner_heer4_main1_attack.png", (300, 243, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image shifta_gunner_heer4_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/shifta_gunner_heer4_main1_attack.png", (300, 0, 150, 243), xalign=0.49, yalign=0.5), xsize=840, ysize=840)
        
image shifta_gunner_heer4_main2_attack_back:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/shifta_gunner_heer4_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_landmine"
        xalign 0.77 yalign -0.6

image shifta_gunner_heer4_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/shifta_gunner_heer4_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_landmine"
        xalign -0.6 yalign 0.52
        
image shifta_gunner_heer4_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/shifta_gunner_heer4_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image shifta_gunner_heer4_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/shifta_gunner_heer4_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image shifta_gunner_heer4_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/shifta_gunner_heer4_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image shifta_gunner_heer4_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/shifta_gunner_heer4_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image shifta_gunner_heer4_heal_finalframe_back:
    Fixed(im.Crop("battle/units/shifta_gunner_heer4_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image shifta_gunner_heer4_heal_finalframe_front:
    Fixed(im.Crop("battle/units/shifta_gunner_heer4_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
################################
#anzac_gunner_heer6
################################

image anzac_gunner_heer6_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/anzac_gunner_heer6_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image anzac_gunner_heer6_walk_front:
    Fixed(anim.Filmstrip("battle/units/anzac_gunner_heer6_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image anzac_gunner_heer6_static_back:
    Fixed(im.Crop("battle/units/anzac_gunner_heer6_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image anzac_gunner_heer6_static_front:
    Fixed(im.Crop("battle/units/anzac_gunner_heer6_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image anzac_gunner_heer6_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/anzac_gunner_heer6_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, loop=False, xalign=0.51, yalign=0.5), xsize=840, ysize=840)
    
image anzac_gunner_heer6_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/anzac_gunner_heer6_main1_attack.png", (150, 243), (3, 1), .05, loop=False, xalign=0.49, yalign=0.5), xsize=840, ysize=840)

image anzac_gunner_heer6_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/anzac_gunner_heer6_main1_attack.png", (300, 243, 150, 243), xalign=0.51, yalign=0.5), xsize=840, ysize=840)

image anzac_gunner_heer6_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/anzac_gunner_heer6_main1_attack.png", (300, 0, 150, 243), xalign=0.49, yalign=0.5), xsize=840, ysize=840)
        
image anzac_gunner_heer6_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/anzac_gunner_heer6_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image anzac_gunner_heer6_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/anzac_gunner_heer6_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image anzac_gunner_heer6_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/anzac_gunner_heer6_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image anzac_gunner_heer6_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/anzac_gunner_heer6_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image anzac_gunner_heer6_special1_attack_back:
    contains:
        "offensive_boomerang_back"
    contains:
        "reaction_hit"
        xalign 0.69 yalign 0.08 alpha 0 xzoom -1
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/anzac_gunner_heer6_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image anzac_gunner_heer6_special1_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/anzac_gunner_heer6_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_boomerang_front"
    contains:
        "reaction_hit"
        xalign -0.28 yalign 0.67 alpha 0
        pause 0.75
        alpha 1.0
        
image anzac_gunner_heer6_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/anzac_gunner_heer6_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image anzac_gunner_heer6_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/anzac_gunner_heer6_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image anzac_gunner_heer6_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/anzac_gunner_heer6_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image anzac_gunner_heer6_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/anzac_gunner_heer6_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image anzac_gunner_heer6_heal_finalframe_back:
    Fixed(im.Crop("battle/units/anzac_gunner_heer6_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image anzac_gunner_heer6_heal_finalframe_front:
    Fixed(im.Crop("battle/units/anzac_gunner_heer6_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
################################
#britannia_pirate_heer6
################################

image britannia_pirate_heer6_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_pirate_heer6_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_pirate_heer6_walk_front:
    Fixed(anim.Filmstrip("battle/units/britannia_pirate_heer6_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_pirate_heer6_static_back:
    Fixed(im.Crop("battle/units/britannia_pirate_heer6_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_pirate_heer6_static_front:
    Fixed(im.Crop("battle/units/britannia_pirate_heer6_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image britannia_pirate_heer6_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_pirate_heer6_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_pirate_heer6_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/britannia_pirate_heer6_main1_attack.png", (150, 243), (3, 1), .05, xalign=0.49, yalign=0.5), xsize=840, ysize=840)

image britannia_pirate_heer6_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_pirate_heer6_main1_attack.png", (300, 243, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_pirate_heer6_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_pirate_heer6_main1_attack.png", (300, 0, 150, 243), xalign=0.49, yalign=0.5), xsize=840, ysize=840)
        
image britannia_pirate_heer6_main2_attack_back:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_pirate_heer6_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_landmine"
        xalign 0.77 yalign -0.6

image britannia_pirate_heer6_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/britannia_pirate_heer6_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_landmine"
        xalign -0.6 yalign 0.52
        
image britannia_pirate_heer6_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_pirate_heer6_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_pirate_heer6_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_pirate_heer6_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_pirate_heer6_special1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_pirate_heer6_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_pirate_heer6_special1_attack_front:
    Fixed(anim.Filmstrip("battle/units/britannia_pirate_heer6_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_pirate_heer6_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_pirate_heer6_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_pirate_heer6_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_pirate_heer6_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image britannia_pirate_heer6_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_pirate_heer6_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image britannia_pirate_heer6_heal_front:
    contains:
        "seal_heal"
        xpos 320
        ypos 435
    contains:
        At(Fixed(anim.Filmstrip("battle/units/britannia_pirate_heer6_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image britannia_pirate_heer6_heal_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_pirate_heer6_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_pirate_heer6_heal_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_pirate_heer6_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
################################
#britannia_shark_heer6
################################

image britannia_shark_heer6_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_shark_heer6_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_shark_heer6_walk_front:
    Fixed(anim.Filmstrip("battle/units/britannia_shark_heer6_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_shark_heer6_static_back:
    Fixed(im.Crop("battle/units/britannia_shark_heer6_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_shark_heer6_static_front:
    Fixed(im.Crop("battle/units/britannia_shark_heer6_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image britannia_shark_heer6_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_shark_heer6_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_shark_heer6_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/britannia_shark_heer6_main1_attack.png", (150, 243), (3, 1), .05, xalign=0.49, yalign=0.5), xsize=840, ysize=840)

image britannia_shark_heer6_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_shark_heer6_main1_attack.png", (300, 243, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_shark_heer6_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_shark_heer6_main1_attack.png", (300, 0, 150, 243), xalign=0.49, yalign=0.5), xsize=840, ysize=840)
        
image britannia_shark_heer6_main2_attack_back:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_shark_heer6_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_landmine"
        xalign 0.77 yalign -0.6

image britannia_shark_heer6_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/britannia_shark_heer6_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_landmine"
        xalign -0.6 yalign 0.52
        
image britannia_shark_heer6_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_shark_heer6_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_shark_heer6_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_shark_heer6_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_shark_heer6_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_shark_heer6_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image britannia_shark_heer6_heal_front:
    contains:
        "seal_heal"
        xpos 320
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/britannia_shark_heer6_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image britannia_shark_heer6_heal_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_shark_heer6_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_shark_heer6_heal_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_shark_heer6_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
################################
#britannia_gunner_heer2
################################

image britannia_gunner_heer2_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_gunner_heer2_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_gunner_heer2_walk_front:
    Fixed(anim.Filmstrip("battle/units/britannia_gunner_heer2_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_gunner_heer2_static_back:
    Fixed(im.Crop("battle/units/britannia_gunner_heer2_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_gunner_heer2_static_front:
    Fixed(im.Crop("battle/units/britannia_gunner_heer2_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image britannia_gunner_heer2_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_gunner_heer2_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_gunner_heer2_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/britannia_gunner_heer2_main1_attack.png", (150, 243), (3, 1), .05, xalign=0.49, yalign=0.5), xsize=840, ysize=840)

image britannia_gunner_heer2_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_gunner_heer2_main1_attack.png", (300, 243, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_gunner_heer2_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_gunner_heer2_main1_attack.png", (300, 0, 150, 243), xalign=0.49, yalign=0.5), xsize=840, ysize=840)
        
image britannia_gunner_heer2_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_gunner_heer2_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_gunner_heer2_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/britannia_gunner_heer2_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image britannia_gunner_heer2_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_gunner_heer2_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_gunner_heer2_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_gunner_heer2_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_gunner_heer2_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_gunner_heer2_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image britannia_gunner_heer2_heal_front:
    contains:
        "seal_heal"
        xpos 320
        ypos 435
    contains:
        At(Fixed(anim.Filmstrip("battle/units/britannia_gunner_heer2_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image britannia_gunner_heer2_heal_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_gunner_heer2_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_gunner_heer2_heal_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_gunner_heer2_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
################################
#britannia_gunner_heer3
################################

image britannia_gunner_heer3_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_gunner_heer3_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_gunner_heer3_walk_front:
    Fixed(anim.Filmstrip("battle/units/britannia_gunner_heer3_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_gunner_heer3_static_back:
    Fixed(im.Crop("battle/units/britannia_gunner_heer3_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_gunner_heer3_static_front:
    Fixed(im.Crop("battle/units/britannia_gunner_heer3_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image britannia_gunner_heer3_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_gunner_heer3_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_gunner_heer3_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/britannia_gunner_heer3_main1_attack.png", (150, 243), (3, 1), .05, loop=False, xalign=0.492, yalign=0.5), xsize=840, ysize=840)

image britannia_gunner_heer3_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_gunner_heer3_main1_attack.png", (300, 243, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_gunner_heer3_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_gunner_heer3_main1_attack.png", (300, 0, 150, 243), xalign=0.492, yalign=0.5), xsize=840, ysize=840)
        
image britannia_gunner_heer3_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_gunner_heer3_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_gunner_heer3_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/britannia_gunner_heer3_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image britannia_gunner_heer3_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_gunner_heer3_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_gunner_heer3_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_gunner_heer3_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_gunner_heer3_special3_attack_back:
    contains:
        "offensive_teacup_back"
    contains:
        "reaction_hit"
        xalign 0.69 yalign 0.08 alpha 0 xzoom -1
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_gunner_heer3_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_gunner_heer3_special3_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/britannia_gunner_heer3_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_teacup_front"
    contains:
        "reaction_hit"
        xalign -0.28 yalign 0.67 alpha 0
        pause 0.75
        alpha 1.0
    
image britannia_gunner_heer3_special3_attack_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_gunner_heer3_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_gunner_heer3_special3_attack_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_gunner_heer3_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image britannia_gunner_heer3_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_gunner_heer3_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image britannia_gunner_heer3_heal_front:
    contains:
        "seal_heal"
        xpos 320
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/britannia_gunner_heer3_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image britannia_gunner_heer3_heal_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_gunner_heer3_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_gunner_heer3_heal_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_gunner_heer3_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
################################
#britannia_antitank_heer3
################################

image britannia_antitank_heer3_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_antitank_heer3_walk.png", (0, 243, 720, 243)), (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_antitank_heer3_walk_front:
    Fixed(anim.Filmstrip("battle/units/britannia_antitank_heer3_walk.png", (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_antitank_heer3_static_back:
    Fixed(im.Crop("battle/units/britannia_antitank_heer3_walk.png", (0, 243, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_antitank_heer3_static_front:
    Fixed(im.Crop("battle/units/britannia_antitank_heer3_walk.png", (0, 0, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_antitank_heer3_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_antitank_heer3_main1_attack.png", (0, 244.5, 717, 244.5)), (179.25, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_antitank_heer3_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/britannia_antitank_heer3_main1_attack.png", (179.25, 244.5), (4, 1), .05, loop=False, xalign=0.495, yalign=0.5), xsize=840, ysize=840)

image britannia_antitank_heer3_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_antitank_heer3_main1_attack.png", (537.75, 244.5, 179.25, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_antitank_heer3_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_antitank_heer3_main1_attack.png", (537.75, 0, 179.25, 244.5), xalign=0.495, yalign=0.5), xsize=840, ysize=840)
    
image britannia_antitank_heer3_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_antitank_heer3_walk.png", (0, 243, 720, 243)), (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image britannia_antitank_heer3_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/britannia_antitank_heer3_walk.png", (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    
image britannia_antitank_heer3_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_antitank_heer3_walk.png", (0, 243, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_antitank_heer3_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_antitank_heer3_walk.png", (0, 0, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_antitank_heer3_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_antitank_heer3_walk.png", (0, 243, 720, 243)), (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image britannia_antitank_heer3_heal_front:
    contains:
        "seal_heal"
        xpos 310
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/britannia_antitank_heer3_walk.png", (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image britannia_antitank_heer3_heal_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_antitank_heer3_walk.png", (0, 243, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_antitank_heer3_heal_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_antitank_heer3_walk.png", (0, 0, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#britannia_marksman_heer3
################################

image britannia_marksman_heer3_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_marksman_heer3_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_marksman_heer3_walk_front:
    Fixed(anim.Filmstrip("battle/units/britannia_marksman_heer3_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_marksman_heer3_static_back:
    Fixed(im.Crop("battle/units/britannia_marksman_heer3_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_marksman_heer3_static_front:
    Fixed(im.Crop("battle/units/britannia_marksman_heer3_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_marksman_heer3_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_marksman_heer3_main1_attack.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_marksman_heer3_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/britannia_marksman_heer3_main1_attack.png", (171, 244.5), (4, 1), .05, loop=False, xalign=0.495, yalign=0.5), xsize=840, ysize=840)

image britannia_marksman_heer3_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_marksman_heer3_main1_attack.png", (513, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_marksman_heer3_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_marksman_heer3_main1_attack.png", (513, 0, 171, 244.5), xalign=0.495, yalign=0.5), xsize=840, ysize=840)
    
image britannia_marksman_heer3_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_marksman_heer3_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image britannia_marksman_heer3_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/britannia_marksman_heer3_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    
image britannia_marksman_heer3_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_marksman_heer3_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_marksman_heer3_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_marksman_heer3_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_marksman_heer3_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_marksman_heer3_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image britannia_marksman_heer3_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/britannia_marksman_heer3_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image britannia_marksman_heer3_heal_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_marksman_heer3_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_marksman_heer3_heal_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_marksman_heer3_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#britannia_admiral_heer5
################################

image britannia_admiral_heer5_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_admiral_heer5_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_admiral_heer5_walk_front:
    Fixed(anim.Filmstrip("battle/units/britannia_admiral_heer5_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_admiral_heer5_static_back:
    Fixed(im.Crop("battle/units/britannia_admiral_heer5_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_admiral_heer5_static_front:
    Fixed(im.Crop("battle/units/britannia_admiral_heer5_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image britannia_admiral_heer5_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_admiral_heer5_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_admiral_heer5_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/britannia_admiral_heer5_main1_attack.png", (150, 243), (3, 1), .05, xalign=0.49, yalign=0.5), xsize=840, ysize=840)

image britannia_admiral_heer5_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_admiral_heer5_main1_attack.png", (300, 243, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_admiral_heer5_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_admiral_heer5_main1_attack.png", (300, 0, 150, 243), xalign=0.49, yalign=0.5), xsize=840, ysize=840)
        
image britannia_admiral_heer5_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_admiral_heer5_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_admiral_heer5_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/britannia_admiral_heer5_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image britannia_admiral_heer5_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_admiral_heer5_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_admiral_heer5_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_admiral_heer5_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_admiral_heer5_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_admiral_heer5_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image britannia_admiral_heer5_heal_front:
    contains:
        "seal_heal"
        xpos 325
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/britannia_admiral_heer5_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image britannia_admiral_heer5_heal_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_admiral_heer5_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_admiral_heer5_heal_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_admiral_heer5_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
################################
#britannia_frogman_heer5
################################

image britannia_frogman_heer5_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_frogman_heer5_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_frogman_heer5_walk_front:
    Fixed(anim.Filmstrip("battle/units/britannia_frogman_heer5_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_frogman_heer5_static_back:
    Fixed(im.Crop("battle/units/britannia_frogman_heer5_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_frogman_heer5_static_front:
    Fixed(im.Crop("battle/units/britannia_frogman_heer5_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image britannia_frogman_heer5_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_frogman_heer5_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, xalign=0.51, yalign=0.5), xsize=840, ysize=840)
    
image britannia_frogman_heer5_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/britannia_frogman_heer5_main1_attack.png", (150, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_frogman_heer5_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_frogman_heer5_main1_attack.png", (300, 243, 150, 243), xalign=0.51, yalign=0.5), xsize=840, ysize=840)

image britannia_frogman_heer5_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_frogman_heer5_main1_attack.png", (300, 0, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image britannia_frogman_heer5_main2_attack_back:
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_frogman_heer5_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_landmine"
        xalign 0.77 yalign -0.6

image britannia_frogman_heer5_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/britannia_frogman_heer5_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "reaction_landmine"
        xalign -0.6 yalign 0.52
        
image britannia_frogman_heer5_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_frogman_heer5_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_frogman_heer5_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_frogman_heer5_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_frogman_heer5_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_frogman_heer5_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image britannia_frogman_heer5_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/britannia_frogman_heer5_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image britannia_frogman_heer5_heal_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_frogman_heer5_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_frogman_heer5_heal_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_frogman_heer5_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
################################
#britannia_camelcavalry_heer5
################################

image britannia_camelcavalry_heer5_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_camelcavalry_heer5_walk.png", (0, 243, 636, 243)), (159, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_camelcavalry_heer5_walk_front:
    Fixed(anim.Filmstrip("battle/units/britannia_camelcavalry_heer5_walk.png", (159, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_camelcavalry_heer5_static_back:
    Fixed(im.Crop("battle/units/britannia_camelcavalry_heer5_walk.png", (0, 243, 159, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_camelcavalry_heer5_static_front:
    Fixed(im.Crop("battle/units/britannia_camelcavalry_heer5_walk.png", (0, 0, 159, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image britannia_camelcavalry_heer5_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_camelcavalry_heer5_main1_attack.png", (0, 243, 477, 243)), (159, 243), (3, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_camelcavalry_heer5_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/britannia_camelcavalry_heer5_main1_attack.png", (159, 243), (3, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_camelcavalry_heer5_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_camelcavalry_heer5_main1_attack.png", (318, 243, 159, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_camelcavalry_heer5_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_camelcavalry_heer5_main1_attack.png", (318, 0, 159, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image britannia_camelcavalry_heer5_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_camelcavalry_heer5_walk.png", (0, 243, 636, 243)), (159, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_camelcavalry_heer5_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/britannia_camelcavalry_heer5_walk.png", (159, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image britannia_camelcavalry_heer5_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_camelcavalry_heer5_walk.png", (0, 243, 159, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_camelcavalry_heer5_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_camelcavalry_heer5_walk.png", (0, 0, 159, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_camelcavalry_heer5_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_camelcavalry_heer5_walk.png", (0, 243, 636, 243)), (159, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image britannia_camelcavalry_heer5_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/britannia_camelcavalry_heer5_walk.png", (159, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image britannia_camelcavalry_heer5_heal_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_camelcavalry_heer5_walk.png", (0, 243, 159, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_camelcavalry_heer5_heal_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_camelcavalry_heer5_walk.png", (0, 0, 159, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
################################
#iraji_gunner_heer6
################################

image iraji_gunner_heer6_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/iraji_gunner_heer6_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image iraji_gunner_heer6_walk_front:
    Fixed(anim.Filmstrip("battle/units/iraji_gunner_heer6_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image iraji_gunner_heer6_static_back:
    Fixed(im.Crop("battle/units/iraji_gunner_heer6_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image iraji_gunner_heer6_static_front:
    Fixed(im.Crop("battle/units/iraji_gunner_heer6_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image iraji_gunner_heer6_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/iraji_gunner_heer6_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image iraji_gunner_heer6_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/iraji_gunner_heer6_main1_attack.png", (150, 243), (3, 1), .05, loop=False, xalign=0.49, yalign=0.5), xsize=840, ysize=840)

image iraji_gunner_heer6_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/iraji_gunner_heer6_main1_attack.png", (300, 243, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image iraji_gunner_heer6_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/iraji_gunner_heer6_main1_attack.png", (300, 0, 150, 243), xalign=0.49, yalign=0.5), xsize=840, ysize=840)
        
image iraji_gunner_heer6_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/iraji_gunner_heer6_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image iraji_gunner_heer6_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/iraji_gunner_heer6_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image iraji_gunner_heer6_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/iraji_gunner_heer6_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image iraji_gunner_heer6_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/iraji_gunner_heer6_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image iraji_gunner_heer6_special1_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/iraji_gunner_heer6_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .02, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image iraji_gunner_heer6_special1_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/iraji_gunner_heer6_walk.png", (126, 243), (4, 1), .02, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image iraji_gunner_heer6_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/iraji_gunner_heer6_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image iraji_gunner_heer6_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/iraji_gunner_heer6_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image iraji_gunner_heer6_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/iraji_gunner_heer6_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image iraji_gunner_heer6_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/iraji_gunner_heer6_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image iraji_gunner_heer6_heal_finalframe_back:
    Fixed(im.Crop("battle/units/iraji_gunner_heer6_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image iraji_gunner_heer6_heal_finalframe_front:
    Fixed(im.Crop("battle/units/iraji_gunner_heer6_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
################################
#britannia_gunner_heer6
################################

image britannia_gunner_heer6_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_gunner_heer6_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_gunner_heer6_walk_front:
    Fixed(anim.Filmstrip("battle/units/britannia_gunner_heer6_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_gunner_heer6_static_back:
    Fixed(im.Crop("battle/units/britannia_gunner_heer6_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_gunner_heer6_static_front:
    Fixed(im.Crop("battle/units/britannia_gunner_heer6_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image britannia_gunner_heer6_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_gunner_heer6_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, loop=False, xalign=0.51, yalign=0.5), xsize=840, ysize=840)
    
image britannia_gunner_heer6_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/britannia_gunner_heer6_main1_attack.png", (150, 243), (3, 1), .05, loop=False, xalign=0.49, yalign=0.5), xsize=840, ysize=840)

image britannia_gunner_heer6_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_gunner_heer6_main1_attack.png", (300, 243, 150, 243), xalign=0.51, yalign=0.5), xsize=840, ysize=840)

image britannia_gunner_heer6_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_gunner_heer6_main1_attack.png", (300, 0, 150, 243), xalign=0.49, yalign=0.5), xsize=840, ysize=840)
        
image britannia_gunner_heer6_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_gunner_heer6_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_gunner_heer6_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/britannia_gunner_heer6_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image britannia_gunner_heer6_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_gunner_heer6_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_gunner_heer6_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_gunner_heer6_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_gunner_heer6_special3_attack_back:
    contains:
        "offensive_teacup_back"
    contains:
        "reaction_hit"
        xalign 0.69 yalign 0.08 alpha 0 xzoom -1
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_gunner_heer6_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_gunner_heer6_special3_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/britannia_gunner_heer6_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_teacup_front"
    contains:
        "reaction_hit"
        xalign -0.28 yalign 0.67 alpha 0
        pause 0.75
        alpha 1.0
    
image britannia_gunner_heer6_special3_attack_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_gunner_heer6_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_gunner_heer6_special3_attack_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_gunner_heer6_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image britannia_gunner_heer6_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_gunner_heer6_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image britannia_gunner_heer6_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/britannia_gunner_heer6_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image britannia_gunner_heer6_heal_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_gunner_heer6_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_gunner_heer6_heal_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_gunner_heer6_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
################################
#britannia_antitank_heer6
################################

image britannia_antitank_heer6_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_antitank_heer6_walk.png", (0, 243, 720, 243)), (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_antitank_heer6_walk_front:
    Fixed(anim.Filmstrip("battle/units/britannia_antitank_heer6_walk.png", (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_antitank_heer6_static_back:
    Fixed(im.Crop("battle/units/britannia_antitank_heer6_walk.png", (0, 243, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_antitank_heer6_static_front:
    Fixed(im.Crop("battle/units/britannia_antitank_heer6_walk.png", (0, 0, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_antitank_heer6_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_antitank_heer6_main1_attack.png", (0, 244.5, 717, 244.5)), (179.25, 244.5), (4, 1), .05, loop=False, xalign=0.49, yalign=0.51), xsize=840, ysize=840)

image britannia_antitank_heer6_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/britannia_antitank_heer6_main1_attack.png", (179.25, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_antitank_heer6_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_antitank_heer6_main1_attack.png", (537.75, 244.5, 179.25, 244.5), xalign=0.49, yalign=0.51), xsize=840, ysize=840)

image britannia_antitank_heer6_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_antitank_heer6_main1_attack.png", (537.75, 0, 179.25, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_antitank_heer6_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_antitank_heer6_walk.png", (0, 243, 720, 243)), (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image britannia_antitank_heer6_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/britannia_antitank_heer6_walk.png", (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    
image britannia_antitank_heer6_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_antitank_heer6_walk.png", (0, 243, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_antitank_heer6_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_antitank_heer6_walk.png", (0, 0, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_antitank_heer6_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_antitank_heer6_walk.png", (0, 243, 720, 243)), (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image britannia_antitank_heer6_heal_front:
    contains:
        "seal_heal"
        xpos 310
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/britannia_antitank_heer6_walk.png", (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image britannia_antitank_heer6_heal_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_antitank_heer6_walk.png", (0, 243, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_antitank_heer6_heal_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_antitank_heer6_walk.png", (0, 0, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#britannia_marksman_heer6
################################

image britannia_marksman_heer6_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_marksman_heer6_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_marksman_heer6_walk_front:
    Fixed(anim.Filmstrip("battle/units/britannia_marksman_heer6_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_marksman_heer6_static_back:
    Fixed(im.Crop("battle/units/britannia_marksman_heer6_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_marksman_heer6_static_front:
    Fixed(im.Crop("battle/units/britannia_marksman_heer6_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_marksman_heer6_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_marksman_heer6_main1_attack.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_marksman_heer6_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/britannia_marksman_heer6_main1_attack.png", (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_marksman_heer6_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_marksman_heer6_main1_attack.png", (513, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_marksman_heer6_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_marksman_heer6_main1_attack.png", (513, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_marksman_heer6_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_marksman_heer6_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image britannia_marksman_heer6_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/britannia_marksman_heer6_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    
image britannia_marksman_heer6_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_marksman_heer6_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_marksman_heer6_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_marksman_heer6_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_marksman_heer6_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_marksman_heer6_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image britannia_marksman_heer6_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/britannia_marksman_heer6_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image britannia_marksman_heer6_heal_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_marksman_heer6_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_marksman_heer6_heal_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_marksman_heer6_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#britannia_gunner_heer4
################################

image britannia_gunner_heer4_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_gunner_heer4_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_gunner_heer4_walk_front:
    Fixed(anim.Filmstrip("battle/units/britannia_gunner_heer4_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_gunner_heer4_static_back:
    Fixed(im.Crop("battle/units/britannia_gunner_heer4_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_gunner_heer4_static_front:
    Fixed(im.Crop("battle/units/britannia_gunner_heer4_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image britannia_gunner_heer4_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_gunner_heer4_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_gunner_heer4_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/britannia_gunner_heer4_main1_attack.png", (150, 243), (3, 1), .05, loop=False, xalign=0.49, yalign=0.5), xsize=840, ysize=840)

image britannia_gunner_heer4_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_gunner_heer4_main1_attack.png", (300, 243, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_gunner_heer4_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_gunner_heer4_main1_attack.png", (300, 0, 150, 243), xalign=0.49, yalign=0.5), xsize=840, ysize=840)
        
image britannia_gunner_heer4_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_gunner_heer4_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_gunner_heer4_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/britannia_gunner_heer4_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image britannia_gunner_heer4_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_gunner_heer4_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_gunner_heer4_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_gunner_heer4_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image britannia_gunner_heer4_special3_attack_back:
    contains:
        "offensive_walkingstick_back"
    contains:
        "reaction_hit"
        xalign 0.69 yalign 0.08 alpha 0 xzoom -1
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_gunner_heer4_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_gunner_heer4_special3_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/britannia_gunner_heer4_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_walkingstick_front"
    contains:
        "reaction_hit"
        xalign -0.28 yalign 0.67 alpha 0
        pause 0.75
        alpha 1.0
    
image britannia_gunner_heer4_special3_attack_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_gunner_heer4_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_gunner_heer4_special3_attack_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_gunner_heer4_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image britannia_gunner_heer4_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/britannia_gunner_heer4_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image britannia_gunner_heer4_heal_front:
    contains:
        "seal_heal"
        xpos 325
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/britannia_gunner_heer4_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image britannia_gunner_heer4_heal_finalframe_back:
    Fixed(im.Crop("battle/units/britannia_gunner_heer4_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image britannia_gunner_heer4_heal_finalframe_front:
    Fixed(im.Crop("battle/units/britannia_gunner_heer4_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
################################
#partisan_gunner_heer4
################################

image partisan_gunner_heer4_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/partisan_gunner_heer4_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image partisan_gunner_heer4_walk_front:
    Fixed(anim.Filmstrip("battle/units/partisan_gunner_heer4_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image partisan_gunner_heer4_static_back:
    Fixed(im.Crop("battle/units/partisan_gunner_heer4_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image partisan_gunner_heer4_static_front:
    Fixed(im.Crop("battle/units/partisan_gunner_heer4_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image partisan_gunner_heer4_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/partisan_gunner_heer4_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image partisan_gunner_heer4_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/partisan_gunner_heer4_main1_attack.png", (150, 243), (3, 1), .05, xalign=0.49, yalign=0.5), xsize=840, ysize=840)

image partisan_gunner_heer4_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/partisan_gunner_heer4_main1_attack.png", (300, 243, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image partisan_gunner_heer4_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/partisan_gunner_heer4_main1_attack.png", (300, 0, 150, 243), xalign=0.49, yalign=0.5), xsize=840, ysize=840)
        
image partisan_gunner_heer4_main2_attack_back:
    contains:
        "offensive_stielhandgranate_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/partisan_gunner_heer4_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image partisan_gunner_heer4_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/partisan_gunner_heer4_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_stielhandgranate_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image partisan_gunner_heer4_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/partisan_gunner_heer4_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image partisan_gunner_heer4_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/partisan_gunner_heer4_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image partisan_gunner_heer4_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/partisan_gunner_heer4_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image partisan_gunner_heer4_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/partisan_gunner_heer4_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image partisan_gunner_heer4_heal_finalframe_back:
    Fixed(im.Crop("battle/units/partisan_gunner_heer4_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image partisan_gunner_heer4_heal_finalframe_front:
    Fixed(im.Crop("battle/units/partisan_gunner_heer4_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
################################
#partisan_marksman_heer4
################################

image partisan_marksman_heer4_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/partisan_marksman_heer4_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image partisan_marksman_heer4_walk_front:
    Fixed(anim.Filmstrip("battle/units/partisan_marksman_heer4_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image partisan_marksman_heer4_static_back:
    Fixed(im.Crop("battle/units/partisan_marksman_heer4_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image partisan_marksman_heer4_static_front:
    Fixed(im.Crop("battle/units/partisan_marksman_heer4_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image partisan_marksman_heer4_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/partisan_marksman_heer4_main1_attack.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image partisan_marksman_heer4_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/partisan_marksman_heer4_main1_attack.png", (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image partisan_marksman_heer4_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/partisan_marksman_heer4_main1_attack.png", (513, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image partisan_marksman_heer4_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/partisan_marksman_heer4_main1_attack.png", (513, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image partisan_marksman_heer4_main2_attack_back:
    contains:
        "offensive_stielhandgranate_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/partisan_marksman_heer4_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image partisan_marksman_heer4_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/partisan_marksman_heer4_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_stielhandgranate_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    
image partisan_marksman_heer4_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/partisan_marksman_heer4_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image partisan_marksman_heer4_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/partisan_marksman_heer4_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image partisan_marksman_heer4_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/partisan_marksman_heer4_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image partisan_marksman_heer4_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/partisan_marksman_heer4_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image partisan_marksman_heer4_heal_finalframe_back:
    Fixed(im.Crop("battle/units/partisan_marksman_heer4_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image partisan_marksman_heer4_heal_finalframe_front:
    Fixed(im.Crop("battle/units/partisan_marksman_heer4_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#grecia_gunner_heer5
################################

image grecia_gunner_heer5_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/grecia_gunner_heer5_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image grecia_gunner_heer5_walk_front:
    Fixed(anim.Filmstrip("battle/units/grecia_gunner_heer5_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image grecia_gunner_heer5_static_back:
    Fixed(im.Crop("battle/units/grecia_gunner_heer5_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image grecia_gunner_heer5_static_front:
    Fixed(im.Crop("battle/units/grecia_gunner_heer5_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image grecia_gunner_heer5_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/grecia_gunner_heer5_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, xalign=0.51, yalign=0.5), xsize=840, ysize=840)
    
image grecia_gunner_heer5_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/grecia_gunner_heer5_main1_attack.png", (150, 243), (3, 1), .05, xalign=0.49, yalign=0.5), xsize=840, ysize=840)

image grecia_gunner_heer5_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/grecia_gunner_heer5_main1_attack.png", (300, 243, 150, 243), xalign=0.51, yalign=0.5), xsize=840, ysize=840)

image grecia_gunner_heer5_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/grecia_gunner_heer5_main1_attack.png", (300, 0, 150, 243), xalign=0.49, yalign=0.5), xsize=840, ysize=840)
        
image grecia_gunner_heer5_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/grecia_gunner_heer5_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image grecia_gunner_heer5_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/grecia_gunner_heer5_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image grecia_gunner_heer5_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/grecia_gunner_heer5_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image grecia_gunner_heer5_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/grecia_gunner_heer5_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image grecia_gunner_heer5_special1_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/grecia_gunner_heer5_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .02, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image grecia_gunner_heer5_special1_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/grecia_gunner_heer5_walk.png", (126, 243), (4, 1), .02, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image grecia_gunner_heer5_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/grecia_gunner_heer5_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image grecia_gunner_heer5_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/grecia_gunner_heer5_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image grecia_gunner_heer5_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/grecia_gunner_heer5_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image grecia_gunner_heer5_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/grecia_gunner_heer5_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image grecia_gunner_heer5_heal_finalframe_back:
    Fixed(im.Crop("battle/units/grecia_gunner_heer5_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image grecia_gunner_heer5_heal_finalframe_front:
    Fixed(im.Crop("battle/units/grecia_gunner_heer5_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
################################
#grecia_marksman_heer5
################################

image grecia_marksman_heer5_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/grecia_marksman_heer5_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image grecia_marksman_heer5_walk_front:
    Fixed(anim.Filmstrip("battle/units/grecia_marksman_heer5_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image grecia_marksman_heer5_static_back:
    Fixed(im.Crop("battle/units/grecia_marksman_heer5_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image grecia_marksman_heer5_static_front:
    Fixed(im.Crop("battle/units/grecia_marksman_heer5_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image grecia_marksman_heer5_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/grecia_marksman_heer5_main1_attack.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image grecia_marksman_heer5_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/grecia_marksman_heer5_main1_attack.png", (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image grecia_marksman_heer5_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/grecia_marksman_heer5_main1_attack.png", (513, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image grecia_marksman_heer5_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/grecia_marksman_heer5_main1_attack.png", (513, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image grecia_marksman_heer5_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/grecia_marksman_heer5_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image grecia_marksman_heer5_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/grecia_marksman_heer5_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    
image grecia_marksman_heer5_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/grecia_marksman_heer5_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image grecia_marksman_heer5_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/grecia_marksman_heer5_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image grecia_marksman_heer5_heal_back:
    contains:
        "seal_heal"
        xpos 300
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/grecia_marksman_heer5_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image grecia_marksman_heer5_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/grecia_marksman_heer5_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image grecia_marksman_heer5_heal_finalframe_back:
    Fixed(im.Crop("battle/units/grecia_marksman_heer5_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image grecia_marksman_heer5_heal_finalframe_front:
    Fixed(im.Crop("battle/units/grecia_marksman_heer5_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#sovia_gunner_heer2
################################

image sovia_gunner_heer2_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/sovia_gunner_heer7_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_gunner_heer2_walk_front:
    Fixed(anim.Filmstrip("battle/units/sovia_gunner_heer7_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_gunner_heer2_static_back:
    Fixed(im.Crop("battle/units/sovia_gunner_heer7_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_gunner_heer2_static_front:
    Fixed(im.Crop("battle/units/sovia_gunner_heer7_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image sovia_gunner_heer2_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/sovia_gunner_heer7_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_gunner_heer2_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/sovia_gunner_heer7_main1_attack.png", (150, 243), (3, 1), .05, xalign=0.49, yalign=0.5), xsize=840, ysize=840)

image sovia_gunner_heer2_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/sovia_gunner_heer7_main1_attack.png", (300, 243, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_gunner_heer2_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/sovia_gunner_heer7_main1_attack.png", (300, 0, 150, 243), xalign=0.49, yalign=0.5), xsize=840, ysize=840)
        
image sovia_gunner_heer2_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/sovia_gunner_heer7_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_gunner_heer2_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/sovia_gunner_heer7_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image sovia_gunner_heer2_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/sovia_gunner_heer7_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_gunner_heer2_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/sovia_gunner_heer7_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_gunner_heer2_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/sovia_gunner_heer7_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image sovia_gunner_heer2_heal_front:
    contains:
        "seal_heal"
        xpos 320
        ypos 435
    contains:
        At(Fixed(anim.Filmstrip("battle/units/sovia_gunner_heer7_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image sovia_gunner_heer2_heal_finalframe_back:
    Fixed(im.Crop("battle/units/sovia_gunner_heer7_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_gunner_heer2_heal_finalframe_front:
    Fixed(im.Crop("battle/units/sovia_gunner_heer7_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
################################
#sovia_antitank_heer2
################################

image sovia_antitank_heer2_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/sovia_antitank_heer7_walk.png", (0, 243, 720, 243)), (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_antitank_heer2_walk_front:
    Fixed(anim.Filmstrip("battle/units/sovia_antitank_heer7_walk.png", (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_antitank_heer2_static_back:
    Fixed(im.Crop("battle/units/sovia_antitank_heer7_walk.png", (0, 243, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_antitank_heer2_static_front:
    Fixed(im.Crop("battle/units/sovia_antitank_heer7_walk.png", (0, 0, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_antitank_heer2_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/sovia_antitank_heer7_main1_attack.png", (0, 244.5, 717, 244.5)), (179.25, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_antitank_heer2_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/sovia_antitank_heer7_main1_attack.png", (179.25, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_antitank_heer2_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/sovia_antitank_heer7_main1_attack.png", (537.75, 244.5, 179.25, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_antitank_heer2_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/sovia_antitank_heer7_main1_attack.png", (537.75, 0, 179.25, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_antitank_heer2_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/sovia_antitank_heer7_walk.png", (0, 243, 720, 243)), (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image sovia_antitank_heer2_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/sovia_antitank_heer7_walk.png", (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    
image sovia_antitank_heer2_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/sovia_antitank_heer7_walk.png", (0, 243, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_antitank_heer2_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/sovia_antitank_heer7_walk.png", (0, 0, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_antitank_heer2_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/sovia_antitank_heer7_walk.png", (0, 243, 720, 243)), (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image sovia_antitank_heer2_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/sovia_antitank_heer7_walk.png", (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image sovia_antitank_heer2_heal_finalframe_back:
    Fixed(im.Crop("battle/units/sovia_antitank_heer7_walk.png", (0, 243, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_antitank_heer2_heal_finalframe_front:
    Fixed(im.Crop("battle/units/sovia_antitank_heer7_walk.png", (0, 0, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#sovia_marksman_heer2
################################

image sovia_marksman_heer2_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/sovia_marksman_heer7_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_marksman_heer2_walk_front:
    Fixed(anim.Filmstrip("battle/units/sovia_marksman_heer7_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_marksman_heer2_static_back:
    Fixed(im.Crop("battle/units/sovia_marksman_heer7_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_marksman_heer2_static_front:
    Fixed(im.Crop("battle/units/sovia_marksman_heer7_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_marksman_heer2_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/sovia_marksman_heer7_main1_attack.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_marksman_heer2_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/sovia_marksman_heer7_main1_attack.png", (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_marksman_heer2_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/sovia_marksman_heer7_main1_attack.png", (513, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_marksman_heer2_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/sovia_marksman_heer7_main1_attack.png", (513, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_marksman_heer2_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/sovia_marksman_heer7_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image sovia_marksman_heer2_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/sovia_marksman_heer7_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    
image sovia_marksman_heer2_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/sovia_marksman_heer7_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_marksman_heer2_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/sovia_marksman_heer7_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_marksman_heer2_heal_back:
    contains:
        "seal_heal"
        xpos 300
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/sovia_marksman_heer7_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image sovia_marksman_heer2_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/sovia_marksman_heer7_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image sovia_marksman_heer2_heal_finalframe_back:
    Fixed(im.Crop("battle/units/sovia_marksman_heer7_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_marksman_heer2_heal_finalframe_front:
    Fixed(im.Crop("battle/units/sovia_marksman_heer7_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#sovia_gunner_heer7
################################

image sovia_gunner_heer7_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/sovia_gunner_heer7_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_gunner_heer7_walk_front:
    Fixed(anim.Filmstrip("battle/units/sovia_gunner_heer7_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_gunner_heer7_static_back:
    Fixed(im.Crop("battle/units/sovia_gunner_heer7_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_gunner_heer7_static_front:
    Fixed(im.Crop("battle/units/sovia_gunner_heer7_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image sovia_gunner_heer7_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/sovia_gunner_heer7_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_gunner_heer7_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/sovia_gunner_heer7_main1_attack.png", (150, 243), (3, 1), .05, xalign=0.49, yalign=0.5), xsize=840, ysize=840)

image sovia_gunner_heer7_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/sovia_gunner_heer7_main1_attack.png", (300, 243, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_gunner_heer7_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/sovia_gunner_heer7_main1_attack.png", (300, 0, 150, 243), xalign=0.49, yalign=0.5), xsize=840, ysize=840)
        
image sovia_gunner_heer7_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/sovia_gunner_heer7_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_gunner_heer7_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/sovia_gunner_heer7_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image sovia_gunner_heer7_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/sovia_gunner_heer7_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_gunner_heer7_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/sovia_gunner_heer7_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_gunner_heer7_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/sovia_gunner_heer7_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image sovia_gunner_heer7_heal_front:
    contains:
        "seal_heal"
        xpos 320
        ypos 435
    contains:
        At(Fixed(anim.Filmstrip("battle/units/sovia_gunner_heer7_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image sovia_gunner_heer7_heal_finalframe_back:
    Fixed(im.Crop("battle/units/sovia_gunner_heer7_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_gunner_heer7_heal_finalframe_front:
    Fixed(im.Crop("battle/units/sovia_gunner_heer7_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
################################
#sovia_antitank_heer7
################################

image sovia_antitank_heer7_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/sovia_antitank_heer7_walk.png", (0, 243, 720, 243)), (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_antitank_heer7_walk_front:
    Fixed(anim.Filmstrip("battle/units/sovia_antitank_heer7_walk.png", (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_antitank_heer7_static_back:
    Fixed(im.Crop("battle/units/sovia_antitank_heer7_walk.png", (0, 243, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_antitank_heer7_static_front:
    Fixed(im.Crop("battle/units/sovia_antitank_heer7_walk.png", (0, 0, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_antitank_heer7_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/sovia_antitank_heer7_main1_attack.png", (0, 244.5, 717, 244.5)), (179.25, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_antitank_heer7_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/sovia_antitank_heer7_main1_attack.png", (179.25, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_antitank_heer7_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/sovia_antitank_heer7_main1_attack.png", (537.75, 244.5, 179.25, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_antitank_heer7_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/sovia_antitank_heer7_main1_attack.png", (537.75, 0, 179.25, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_antitank_heer7_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/sovia_antitank_heer7_walk.png", (0, 243, 720, 243)), (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image sovia_antitank_heer7_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/sovia_antitank_heer7_walk.png", (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    
image sovia_antitank_heer7_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/sovia_antitank_heer7_walk.png", (0, 243, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_antitank_heer7_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/sovia_antitank_heer7_walk.png", (0, 0, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_antitank_heer7_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/sovia_antitank_heer7_walk.png", (0, 243, 720, 243)), (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image sovia_antitank_heer7_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/sovia_antitank_heer7_walk.png", (180, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image sovia_antitank_heer7_heal_finalframe_back:
    Fixed(im.Crop("battle/units/sovia_antitank_heer7_walk.png", (0, 243, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_antitank_heer7_heal_finalframe_front:
    Fixed(im.Crop("battle/units/sovia_antitank_heer7_walk.png", (0, 0, 180, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#sovia_marksman_heer7
################################

image sovia_marksman_heer7_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/sovia_marksman_heer7_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_marksman_heer7_walk_front:
    Fixed(anim.Filmstrip("battle/units/sovia_marksman_heer7_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_marksman_heer7_static_back:
    Fixed(im.Crop("battle/units/sovia_marksman_heer7_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_marksman_heer7_static_front:
    Fixed(im.Crop("battle/units/sovia_marksman_heer7_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_marksman_heer7_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/sovia_marksman_heer7_main1_attack.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_marksman_heer7_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/sovia_marksman_heer7_main1_attack.png", (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_marksman_heer7_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/sovia_marksman_heer7_main1_attack.png", (513, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_marksman_heer7_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/sovia_marksman_heer7_main1_attack.png", (513, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_marksman_heer7_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/sovia_marksman_heer7_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image sovia_marksman_heer7_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/sovia_marksman_heer7_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    
image sovia_marksman_heer7_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/sovia_marksman_heer7_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_marksman_heer7_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/sovia_marksman_heer7_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_marksman_heer7_heal_back:
    contains:
        "seal_heal"
        xpos 300
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/sovia_marksman_heer7_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image sovia_marksman_heer7_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/sovia_marksman_heer7_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image sovia_marksman_heer7_heal_finalframe_back:
    Fixed(im.Crop("battle/units/sovia_marksman_heer7_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_marksman_heer7_heal_finalframe_front:
    Fixed(im.Crop("battle/units/sovia_marksman_heer7_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#sovia_cavalry_heer7
################################

image sovia_cavalry_heer7_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/sovia_cavalry_heer7_walk.png", (0, 243, 636, 243)), (159, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_cavalry_heer7_walk_front:
    Fixed(anim.Filmstrip("battle/units/sovia_cavalry_heer7_walk.png", (159, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_cavalry_heer7_static_back:
    Fixed(im.Crop("battle/units/sovia_cavalry_heer7_walk.png", (0, 243, 159, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_cavalry_heer7_static_front:
    Fixed(im.Crop("battle/units/sovia_cavalry_heer7_walk.png", (0, 0, 159, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 

image sovia_cavalry_heer7_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/sovia_cavalry_heer7_main1_attack.png", (0, 243, 1908, 243)), (159, 243), (12, 1), .07, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_cavalry_heer7_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/sovia_cavalry_heer7_main1_attack.png", (159, 243), (12, 1), .07, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_cavalry_heer7_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/sovia_cavalry_heer7_main1_attack.png", (0, 243, 159, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_cavalry_heer7_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/sovia_cavalry_heer7_main1_attack.png", (0, 0, 159, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_cavalry_heer7_main2_attack_back:
    contains:
        "offensive_grenade_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/sovia_cavalry_heer7_walk.png", (0, 243, 636, 243)), (159, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image sovia_cavalry_heer7_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/sovia_cavalry_heer7_walk.png", (159, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_grenade_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image sovia_cavalry_heer7_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/sovia_cavalry_heer7_walk.png", (0, 243, 159, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_cavalry_heer7_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/sovia_cavalry_heer7_walk.png", (0, 0, 159, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image sovia_cavalry_heer7_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/sovia_cavalry_heer7_walk.png", (0, 243, 636, 243)), (159, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image sovia_cavalry_heer7_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/sovia_cavalry_heer7_walk.png", (159, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image sovia_cavalry_heer7_heal_finalframe_back:
    Fixed(im.Crop("battle/units/sovia_cavalry_heer7_walk.png", (0, 243, 159, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image sovia_cavalry_heer7_heal_finalframe_front:
    Fixed(im.Crop("battle/units/sovia_cavalry_heer7_walk.png", (0, 0, 159, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
################################
#zombie_gunner_heer8
################################

image zombie_gunner_heer8_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/zombie_gunner_heer8_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image zombie_gunner_heer8_walk_front:
    Fixed(anim.Filmstrip("battle/units/zombie_gunner_heer8_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image zombie_gunner_heer8_static_back:
    Fixed(im.Crop("battle/units/zombie_gunner_heer8_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image zombie_gunner_heer8_static_front:
    Fixed(im.Crop("battle/units/zombie_gunner_heer8_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
image zombie_gunner_heer8_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/zombie_gunner_heer8_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image zombie_gunner_heer8_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/zombie_gunner_heer8_main1_attack.png", (150, 243), (3, 1), .05, xalign=0.49, yalign=0.5), xsize=840, ysize=840)

image zombie_gunner_heer8_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/zombie_gunner_heer8_main1_attack.png", (300, 243, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image zombie_gunner_heer8_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/zombie_gunner_heer8_main1_attack.png", (300, 0, 150, 243), xalign=0.49, yalign=0.5), xsize=840, ysize=840)
        
image zombie_gunner_heer8_main2_attack_back:
    contains:
        "offensive_stielhandgranate_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/zombie_gunner_heer8_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image zombie_gunner_heer8_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/zombie_gunner_heer8_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_stielhandgranate_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image zombie_gunner_heer8_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/zombie_gunner_heer8_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image zombie_gunner_heer8_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/zombie_gunner_heer8_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image zombie_gunner_heer8_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/zombie_gunner_heer8_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image zombie_gunner_heer8_heal_front:
    contains:
        "seal_heal"
        xpos 320
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/zombie_gunner_heer8_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image zombie_gunner_heer8_heal_finalframe_back:
    Fixed(im.Crop("battle/units/zombie_gunner_heer8_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image zombie_gunner_heer8_heal_finalframe_front:
    Fixed(im.Crop("battle/units/zombie_gunner_heer8_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840) 
    
################################
#zhina_gunner_heer1
################################

image zhina_gunner_heer1_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/zhina_gunner_heer1_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image zhina_gunner_heer1_walk_front:
    Fixed(anim.Filmstrip("battle/units/zhina_gunner_heer1_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image zhina_gunner_heer1_static_back:
    Fixed(im.Crop("battle/units/zhina_gunner_heer1_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image zhina_gunner_heer1_static_front:
    Fixed(im.Crop("battle/units/zhina_gunner_heer1_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image zhina_gunner_heer1_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/zhina_gunner_heer1_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image zhina_gunner_heer1_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/zhina_gunner_heer1_main1_attack.png", (150, 243), (3, 1), .05, xalign=0.505, yalign=0.5), xsize=840, ysize=840)
    
image zhina_gunner_heer1_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/zhina_gunner_heer1_main1_attack.png", (300, 243, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image zhina_gunner_heer1_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/zhina_gunner_heer1_main1_attack.png", (300, 0, 150, 243), xalign=0.505, yalign=0.5), xsize=840, ysize=840)
    
image zhina_gunner_heer1_main2_attack_back:
    contains:
        "offensive_stielhandgranate_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/zhina_gunner_heer1_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image zhina_gunner_heer1_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/zhina_gunner_heer1_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_stielhandgranate_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image zhina_gunner_heer1_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/zhina_gunner_heer1_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image zhina_gunner_heer1_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/zhina_gunner_heer1_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image zhina_gunner_heer1_special1_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/zhina_gunner_heer1_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .02, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)

image zhina_gunner_heer1_special1_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/zhina_gunner_heer1_walk.png", (126, 243), (4, 1), .02, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image zhina_gunner_heer1_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/zhina_gunner_heer1_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image zhina_gunner_heer1_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/zhina_gunner_heer1_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image zhina_gunner_heer1_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/zhina_gunner_heer1_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image zhina_gunner_heer1_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/zhina_gunner_heer1_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image zhina_gunner_heer1_heal_finalframe_back:
    Fixed(im.Crop("battle/units/zhina_gunner_heer1_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image zhina_gunner_heer1_heal_finalframe_front:
    Fixed(im.Crop("battle/units/zhina_gunner_heer1_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#zhina_marksman_heer1
################################

image zhina_marksman_heer1_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/zhina_marksman_heer1_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image zhina_marksman_heer1_walk_front:
    Fixed(anim.Filmstrip("battle/units/zhina_marksman_heer1_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image zhina_marksman_heer1_static_back:
    Fixed(im.Crop("battle/units/zhina_marksman_heer1_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image zhina_marksman_heer1_static_front:
    Fixed(im.Crop("battle/units/zhina_marksman_heer1_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image zhina_marksman_heer1_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/zhina_marksman_heer1_main1_attack.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image zhina_marksman_heer1_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/zhina_marksman_heer1_main1_attack.png", (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image zhina_marksman_heer1_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/zhina_marksman_heer1_main1_attack.png", (513, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image zhina_marksman_heer1_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/zhina_marksman_heer1_main1_attack.png", (513, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image zhina_marksman_heer1_main2_attack_back:
    contains:
        "offensive_stielhandgranate_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/zhina_marksman_heer1_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image zhina_marksman_heer1_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/zhina_marksman_heer1_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_stielhandgranate_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    
image zhina_marksman_heer1_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/zhina_marksman_heer1_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image zhina_marksman_heer1_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/zhina_marksman_heer1_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image zhina_marksman_heer1_special1_attack_back:
    Fixed(At(anim.Filmstrip(im.Crop("battle/units/zhina_marksman_heer1_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .02, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)

image zhina_marksman_heer1_special1_attack_front:
    Fixed(At(anim.Filmstrip("battle/units/zhina_marksman_heer1_walk.png", (171, 244.5), (4, 1), .02, xalign=0.5, yalign=0.5), runover), xsize=840, ysize=840)
    
image zhina_marksman_heer1_special1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/zhina_marksman_heer1_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image zhina_marksman_heer1_special1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/zhina_marksman_heer1_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image zhina_marksman_heer1_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/zhina_marksman_heer1_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image zhina_marksman_heer1_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/zhina_marksman_heer1_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image zhina_marksman_heer1_heal_finalframe_back:
    Fixed(im.Crop("battle/units/zhina_marksman_heer1_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image zhina_marksman_heer1_heal_finalframe_front:
    Fixed(im.Crop("battle/units/zhina_marksman_heer1_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#meowist_gunner_heer1
################################

image meowist_gunner_heer1_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/meowist_gunner_heer1_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image meowist_gunner_heer1_walk_front:
    Fixed(anim.Filmstrip("battle/units/meowist_gunner_heer1_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image meowist_gunner_heer1_static_back:
    Fixed(im.Crop("battle/units/meowist_gunner_heer1_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image meowist_gunner_heer1_static_front:
    Fixed(im.Crop("battle/units/meowist_gunner_heer1_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image meowist_gunner_heer1_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/meowist_gunner_heer1_main1_attack.png", (0, 243, 450, 243)), (150, 243), (3, 1), .05, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image meowist_gunner_heer1_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/meowist_gunner_heer1_main1_attack.png", (150, 243), (3, 1), .05, xalign=0.49, yalign=0.5), xsize=840, ysize=840)
    
image meowist_gunner_heer1_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/meowist_gunner_heer1_main1_attack.png", (300, 243, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image meowist_gunner_heer1_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/meowist_gunner_heer1_main1_attack.png", (300, 0, 150, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image meowist_gunner_heer1_main2_attack_back:
    contains:
        "offensive_stielhandgranate_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/meowist_gunner_heer1_walk.png", (0, 243, 504, 243)), (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image meowist_gunner_heer1_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/meowist_gunner_heer1_walk.png", (126, 243), (3, 1), .2, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_stielhandgranate_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
        
image meowist_gunner_heer1_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/meowist_gunner_heer1_walk.png", (252, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image meowist_gunner_heer1_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/meowist_gunner_heer1_walk.png", (252, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image meowist_gunner_heer1_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/meowist_gunner_heer1_walk.png", (0, 243, 504, 243)), (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image meowist_gunner_heer1_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/meowist_gunner_heer1_walk.png", (126, 243), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image meowist_gunner_heer1_heal_finalframe_back:
    Fixed(im.Crop("battle/units/meowist_gunner_heer1_walk.png", (0, 243, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image meowist_gunner_heer1_heal_finalframe_front:
    Fixed(im.Crop("battle/units/meowist_gunner_heer1_walk.png", (0, 0, 126, 243), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################
#meowist_marksman_heer1
################################

image meowist_marksman_heer1_walk_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/meowist_marksman_heer1_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image meowist_marksman_heer1_walk_front:
    Fixed(anim.Filmstrip("battle/units/meowist_marksman_heer1_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image meowist_marksman_heer1_static_back:
    Fixed(im.Crop("battle/units/meowist_marksman_heer1_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image meowist_marksman_heer1_static_front:
    Fixed(im.Crop("battle/units/meowist_marksman_heer1_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image meowist_marksman_heer1_main1_attack_back:
    Fixed(anim.Filmstrip(im.Crop("battle/units/meowist_marksman_heer1_main1_attack.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image meowist_marksman_heer1_main1_attack_front:
    Fixed(anim.Filmstrip("battle/units/meowist_marksman_heer1_main1_attack.png", (171, 244.5), (4, 1), .05, loop=False, xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image meowist_marksman_heer1_main1_attack_finalframe_back:
    Fixed(im.Crop("battle/units/meowist_marksman_heer1_main1_attack.png", (513, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image meowist_marksman_heer1_main1_attack_finalframe_front:
    Fixed(im.Crop("battle/units/meowist_marksman_heer1_main1_attack.png", (513, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image meowist_marksman_heer1_main2_attack_back:
    contains:
        "offensive_stielhandgranate_back"
    contains:
        "reaction_fire"
        xalign 0.73 yalign 0.08 alpha 0
        pause 0.75
        alpha 1.0
    contains:
        Fixed(anim.Filmstrip(im.Crop("battle/units/meowist_marksman_heer1_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        
image meowist_marksman_heer1_main2_attack_front:
    contains:
        Fixed(anim.Filmstrip("battle/units/meowist_marksman_heer1_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    contains:
        "offensive_stielhandgranate_front"
    contains:
        "reaction_fire"
        xalign -0.37 yalign 0.71 alpha 0
        pause 0.75
        alpha 1.0
    
image meowist_marksman_heer1_main2_attack_finalframe_back:
    Fixed(im.Crop("battle/units/meowist_marksman_heer1_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image meowist_marksman_heer1_main2_attack_finalframe_front:
    Fixed(im.Crop("battle/units/meowist_marksman_heer1_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
image meowist_marksman_heer1_heal_back:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip(im.Crop("battle/units/meowist_marksman_heer1_walk.png", (0, 244.5, 684, 244.5)), (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)

image meowist_marksman_heer1_heal_front:
    contains:
        "seal_heal"
        xpos 330
        ypos 430
    contains:
        At(Fixed(anim.Filmstrip("battle/units/meowist_marksman_heer1_walk.png", (171, 244.5), (4, 1), .2, xalign=0.5, yalign=0.5), xsize=840, ysize=840), heal_green)
    contains:
        Fixed("reaction_heal", xsize=840, ysize=840)
    
image meowist_marksman_heer1_heal_finalframe_back:
    Fixed(im.Crop("battle/units/meowist_marksman_heer1_walk.png", (0, 244.5, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)

image meowist_marksman_heer1_heal_finalframe_front:
    Fixed(im.Crop("battle/units/meowist_marksman_heer1_walk.png", (0, 0, 171, 244.5), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
    
################################

################################################################
################################################################
################################################################
    #  FIGHTER PROFILES  #
################################################################
################################################################
################################################################

image mia_profile = "battle/gfx/mia_profile.png"

image infantry_germania_gunner_heer1_profile = "battle/gfx/infantry_germania_gunner_heer1_profile.png"
image infantry_germania_gunner_heer3_profile = "battle/gfx/infantry_germania_gunner_heer3_profile.png"
image infantry_germania_gunner_heer5_profile = "battle/gfx/infantry_germania_gunner_heer5_profile.png"
image infantry_germania_gunner_heer7_profile = "battle/gfx/infantry_germania_gunner_heer7_profile.png"
image infantry_germania_antitank_heer1_profile = "battle/gfx/infantry_germania_antitank_heer1_profile.png"
image infantry_germania_antitank_heer3_profile = "battle/gfx/infantry_germania_antitank_heer3_profile.png"
image infantry_germania_antitank_heer5_profile = "battle/gfx/infantry_germania_antitank_heer5_profile.png"
image infantry_germania_antitank_heer7_profile = "battle/gfx/infantry_germania_antitank_heer7_profile.png"
image infantry_germania_marksman_heer1_profile = "battle/gfx/infantry_germania_marksman_heer1_profile.png"
image infantry_germania_marksman_heer3_profile = "battle/gfx/infantry_germania_marksman_heer3_profile.png"
image infantry_germania_marksman_heer5_profile = "battle/gfx/infantry_germania_marksman_heer5_profile.png"
image infantry_germania_marksman_heer7_profile = "battle/gfx/infantry_germania_marksman_heer7_profile.png"
image infantry_britannia_antitank_heer6_profile = "battle/gfx/infantry_britannia_antitank_heer6_profile.png"
image infantry_britannia_gunner_heer6_profile = "battle/gfx/infantry_britannia_gunner_heer6_profile.png"
image infantry_britannia_frogman_heer5_profile = "battle/gfx/infantry_britannia_frogman_heer5_profile.png"
image infantry_britannia_admiral_heer5_profile = "battle/gfx/infantry_britannia_admiral_heer5_profile.png"
image infantry_anzac_gunner_heer6_profile = "battle/gfx/infantry_anzac_gunner_heer6_profile.png"
image infantry_franzo_gunner_heer4_profile = "battle/gfx/infantry_franzo_gunner_heer4_profile.png"
image infantry_franzo_marksman_heer4_profile = "battle/gfx/infantry_franzo_marksman_heer4_profile.png"
image infantry_sovia_gunner_heer7_profile = "battle/gfx/infantry_sovia_gunner_heer7_profile.png"
image infantry_sovia_marksman_heer7_profile = "battle/gfx/infantry_sovia_marksman_heer7_profile.png"

image commander_churchill_profile = "battle/gfx/commander_churchill_profile.png"
image commander_cyrano_profile = "battle/gfx/commander_cyrano_profile.png"
image commander_guderian_profile = "battle/gfx/commander_guderian_profile.png"
image commander_hitora_profile = "battle/gfx/commander_hitora_profile.png"
image commander_nyan_profile = "battle/gfx/commander_nyan_profile.png"
image commander_monty_profile = "battle/gfx/commander_monty_profile.png"
image commander_rinni_profile = "battle/gfx/commander_rinni_profile.png"
image commander_roijean_profile = "battle/gfx/commander_roijean_profile.png"
image commander_rommel_profile = "battle/gfx/commander_rommel_profile.png"
image commander_starin_profile = "battle/gfx/commander_starin_profile.png"
image commander_smigly_profile = "battle/gfx/commander_smigly_profile.png"
image commander_yamato_heer0_profile = "battle/gfx/commander_yamato_profile.png"
image commander_yamato_heer1_profile = "battle/gfx/commander_yamato_profile.png"
image commander_yamato_heer2_profile = "battle/gfx/commander_yamato_profile.png"
image commander_yamato_heer3_profile = "battle/gfx/commander_yamato_profile.png"
image commander_yamato_heer4_profile = "battle/gfx/commander_yamato_profile.png"
image commander_yamato_heer5_profile = "battle/gfx/commander_yamato_profile.png"
image commander_yamato_heer6_profile = "battle/gfx/commander_yamato_profile.png"
image commander_yamato_heer7_profile = "battle/gfx/commander_yamato_profile.png"
image commander_yamato_heer8_profile = "battle/gfx/commander_yamato_profile.png"
image commander_zhukky_profile = "battle/gfx/commander_zhukky_profile.png"
image panzer_7tp_profile = "battle/gfx/panzer_7tp_profile.png"
image panzer_47mmapx_profile = "battle/gfx/panzer_47mmapx_profile.png"
image panzer_archer_profile = "battle/gfx/panzer_archer_profile.png"
image panzer_ba10_profile = "battle/gfx/panzer_ba10_profile.png"
image panzer_bishopsph_profile = "battle/gfx/panzer_bishopsph_profile.png"
image panzer_braatovervalwagen_profile = "battle/gfx/panzer_braatovervalwagen_profile.png"
image panzer_bt42_profile = "battle/gfx/panzer_bt42_profile.png"
image panzer_carroarmato_profile = "battle/gfx/panzer_carroarmato_profile.png"
image panzer_charb1_profile = "battle/gfx/panzer_charb1_profile.png"
image panzer_charfcm_profile = "battle/gfx/panzer_charfcm_profile.png"
image panzer_churchill_profile = "battle/gfx/panzer_churchill_profile.png"
image panzer_covenanter_profile = "battle/gfx/panzer_covenanter_profile.png"
image panzer_crusader_profile = "battle/gfx/panzer_crusader_profile.png"
image antitank_elefant_profile = "battle/gfx/antitank_elefant_profile.png"
image antitank_hornisse_profile = "battle/gfx/antitank_hornisse_profile.png"
image panzer_hotchkiss_profile = "battle/gfx/panzer_hotchkiss_profile.png"
image panzer_is2_profile = "battle/gfx/panzer_is2_profile.png"
image antitank_jagdpanther_profile = "battle/gfx/antitank_jagdpanther_profile.png"
image antitank_jagdpanzer_profile = "battle/gfx/antitank_jagdpanzer_profile.png"
image antitank_jagdtiger_profile = "battle/gfx/antitank_jagdtiger_profile.png"
image panzer_konigstiger_profile = "battle/gfx/panzer_konigstiger_profile.png"
image panzer_kv1_profile = "battle/gfx/panzer_kv1_profile.png"
image panzer_kv2_profile = "battle/gfx/panzer_kv2_profile.png"
image panzer_l335_profile = "battle/gfx/panzer_l335_profile.png"
image antitank_marder_profile = "battle/gfx/antitank_marder_profile.png"
image panzer_matilda1_profile = "battle/gfx/panzer_matilda1_profile.png"
image panzer_matilda2_profile = "battle/gfx/panzer_matilda2_profile.png"
image panzer_maus_profile = "battle/gfx/panzer_maus_profile.png"
image panzer_mech_profile = "battle/gfx/panzer_mech_profile.png"
image panzer_odessa_profile = "battle/gfx/panzer_odessa_profile.png"
image antitank_pak36_profile = "battle/gfx/antitank_pak36_profile.png"
image panzer_panther_profile = "battle/gfx/panzer_panther_profile.png"
image panzer_pantserwagen_profile = "battle/gfx/panzer_pantserwagen_profile.png"
image panzer_panzer1_profile = "battle/gfx/panzer_panzer1_profile.png"
image panzer_panzer2_profile = "battle/gfx/panzer_panzer2_profile.png"
image panzer_panzer3_profile = "battle/gfx/panzer_panzer3_profile.png"
image panzer_panzer38t_profile = "battle/gfx/panzer_panzer38t_profile.png"
image panzer_panzer4_profile = "battle/gfx/panzer_panzer4_profile.png"
image antitank_panzerjager_profile = "battle/gfx/antitank_panzerjager_profile.png"
image panzer_renaultft_profile = "battle/gfx/panzer_renaultft_profile.png"
image panzer_renaultr3540_profile = "battle/gfx/panzer_renaultr3540_profile.png"
image antitank_sdkfz250_profile = "battle/gfx/antitank_sdkfz250_profile.png"
image panzer_semovente_profile = "battle/gfx/panzer_semovente_profile.png"
image panzer_somuas35_profile = "battle/gfx/panzer_somuas35_profile.png"
image panzer_stug3_profile = "battle/gfx/panzer_stug3_profile.png"
image panzer_stug4_profile = "battle/gfx/panzer_stug4_profile.png"
image panzer_su100_profile = "battle/gfx/panzer_su100_profile.png"
image antitank_t13_profile = "battle/gfx/antitank_t13_profile.png"
image panzer_t34_profile = "battle/gfx/panzer_t34_profile.png"
image panzer_t35_profile = "battle/gfx/panzer_t35_profile.png"
image panzer_tiger_profile = "battle/gfx/panzer_tiger_profile.png"
image panzer_tks_profile = "battle/gfx/panzer_tks_profile.png"
image panzer_toldi_profile = "battle/gfx/panzer_toldi_profile.png"
image panzer_turan_profile = "battle/gfx/panzer_turan_profile.png"
image panzer_ursus_profile = "battle/gfx/panzer_ursus_profile.png"
image panzer_valentine_profile = "battle/gfx/panzer_valentine_profile.png"
image panzer_zrinyi_profile = "battle/gfx/panzer_zrinyi_profile.png"

image specialgroup_afrikaakorps_antitank_heer5_profile = "battle/gfx/specialgroup_afrikaakorps_antitank_heer5_profile.png"
image specialgroup_afrikaakorps_gunner_heer5_profile = "battle/gfx/specialgroup_afrikaakorps_gunner_heer5_profile.png"
image specialgroup_afrikaakorps_marksman_heer5_profile = "battle/gfx/specialgroup_afrikaakorps_marksman_heer5_profile.png"
image specialgroup_finbard_marksman_heer2_profile = "battle/gfx/specialgroup_finbard_marksman_heer2_profile.png"
image specialgroup_finbard_gunner_heer2_profile = "battle/gfx/specialgroup_finbard_gunner_heer2_profile.png"
image specialgroup_nord_antitank_heer2_profile = "battle/gfx/specialgroup_nord_antitank_heer2_profile.png"
image specialgroup_nord_gunner_heer2_profile = "battle/gfx/specialgroup_nord_gunner_heer2_profile.png"
image specialgroup_nord_marksman_heer2_profile = "battle/gfx/specialgroup_nord_marksman_heer2_profile.png"
image specialgroup_rumanum_antitank_heer7_profile = "battle/gfx/specialgroup_rumanum_antitank_heer7_profile.png"
image specialgroup_rumanum_cavalry_heer7_profile = "battle/gfx/specialgroup_rumanum_cavalry_heer7_profile.png"
image specialgroup_rumanum_gunner_heer7_profile = "battle/gfx/specialgroup_rumanum_gunner_heer7_profile.png"
image specialgroup_uboatcosplay_heer6_profile = "battle/gfx/specialgroup_uboatcosplay_heer6_profile.png"
image specialgroup_vitalia_frogman_heer5_profile = "battle/gfx/specialgroup_vitalia_frogman_heer5_profile.png"
image specialgroup_vitalia_gunner_heer3_profile = "battle/gfx/specialgroup_vitalia_gunner_heer3_profile.png"
image specialgroup_vitalia_marksman_heer3_profile = "battle/gfx/specialgroup_vitalia_marksman_heer3_profile.png"
image specialgroup_zipangu_gunner_heer1_profile = "battle/gfx/specialgroup_zipangu_gunner_heer1_profile.png"
image specialgroup_zipangu_marksman_heer1_profile = "battle/gfx/specialgroup_zipangu_marksman_heer1_profile.png"
image specialgroup_grecia_gunner_heer5_profile = "battle/gfx/specialgroup_grecia_gunner_heer5_profile.png"
image specialgroup_grecia_marksman_heer5_profile = "battle/gfx/specialgroup_grecia_marksman_heer5_profile.png"

image airsupport_freccia_profile = "battle/gfx/airsupport_freccia_profile.png"
image airsupport_shrike_profile = "battle/gfx/airsupport_shrike_profile.png"
image airsupport_ironsides_profile = "battle/gfx/airsupport_ironsides_profile.png"
image airsupport_griffin_profile = "battle/gfx/airsupport_griffin_profile.png"
image airsupport_swallow_profile = "battle/gfx/airsupport_swallow_profile.png"
image airsupport_fopfighter_profile = "battle/gfx/airsupport_fopfighter_profile.png"
image airsupport_dambuster_profile = "battle/gfx/airsupport_dambuster_profile.png"
image airsupport_snotfire_profile = "battle/gfx/airsupport_snotfire_profile.png"
image airsupport_rampage_profile = "battle/gfx/airsupport_rampage_profile.png"
image airsupport_yakovlev_profile = "battle/gfx/airsupport_yakovlev_profile.png"
image airsupport_petlyakov_profile = "battle/gfx/airsupport_petlyakov_profile.png"

image other_batavia_gunner_heer3_profile = "battle/gfx/other_batavia_gunner_heer3_profile.png"
image other_britannia_gunner_heer3_profile = "battle/gfx/other_britannia_gunner_heer3_profile.png"
image other_dania_gunner_heer2_profile = "battle/gfx/other_dania_gunner_heer2_profile.png"
image other_franzo_gunner_heer3_profile = "battle/gfx/other_franzo_gunner_heer3_profile.png"
image other_norda_gunner_heer2_profile = "battle/gfx/other_norda_gunner_heer2_profile.png"
image other_norda_marksman_heer2_profile = "battle/gfx/other_norda_marksman_heer2_profile.png"
image other_polix_cavalry_heer1_profile = "battle/gfx/other_polix_cavalry_heer1_profile.png"
image other_polix_gunner_heer1_profile = "battle/gfx/other_polix_gunner_heer1_profile.png"
image other_serpana_antitank_heer5_profile = "battle/gfx/other_serpana_antitank_heer5_profile.png"
image other_serpana_gunner_heer5_profile = "battle/gfx/other_serpana_gunner_heer5_profile.png"
