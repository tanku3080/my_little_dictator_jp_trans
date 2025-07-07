
#####################################################################################################################################################
# EFFECTS
#####################################################################################################################################################
        
image speedlines = "back/effects/speedlines.png"

image mist: 
    additive 0.4
    "back/effects/mist1.png"
    0.1
    "back/effects/mist1.png" with Dissolve(1.5, alpha=True)
    4.0
    "back/effects/mist2.png" with Dissolve(1.5, alpha=True)
    4.0
    "back/effects/mist3.png" with Dissolve(1.5, alpha=True)
    4.0
    "back/effects/mist2.png" with Dissolve(1.5, alpha=True)
    4.0
    "back/effects/mist3.png" with Dissolve(1.5, alpha=True)
    4.0
    "back/effects/mist2.png" with Dissolve(1.5, alpha=True)
    4.0
    "back/effects/mist1.png" with Dissolve(1.5, alpha=True)
    4.0
    repeat
    
image bathmist: 
    additive 0.4
    contains:
        "back/effects/mist1.png" with Dissolve(1.5, alpha=True)
        4.0
        "back/effects/mist2.png" with Dissolve(1.5, alpha=True)
        4.0
        "back/effects/mist3.png" with Dissolve(1.5, alpha=True)
        4.0
        "back/effects/mist2.png" with Dissolve(1.5, alpha=True)
        4.0
        "back/effects/mist3.png" with Dissolve(1.5, alpha=True)
        4.0
        "back/effects/mist2.png" with Dissolve(1.5, alpha=True)
        4.0
        repeat    
    contains:
        "back/effects/mist1.png" with Dissolve(1.5, alpha=True)
        4.0
        "back/effects/mist2.png" with Dissolve(1.5, alpha=True)
        4.0
        "back/effects/mist3.png" with Dissolve(1.5, alpha=True)
        4.0
        "back/effects/mist2.png" with Dissolve(1.5, alpha=True)
        4.0
        "back/effects/mist3.png" with Dissolve(1.5, alpha=True)
        4.0
        "back/effects/mist2.png" with Dissolve(1.5, alpha=True)
        4.0
        repeat    
        
image snow2 = SnowBlossom("back/effects/snowflake.png", 200, 20, (20, 800), (20, 600))

image snow:
    contains:
        "snow2"
        zoom 0.5
        alpha 0.3
    contains:
        "snow2"
        alpha 0.7
    contains:
        "snow2"
        zoom 2.0
        alpha 0.5
    contains:
        "snow2"
        zoom 2.0
        alpha 0.5
    contains:
        "snow2"
        zoom 3.0
        alpha 0.4
    contains:
        "snow2"
        zoom 7.0
        alpha 0.3
    contains:
        "snow2"
        zoom 10.0
        alpha 0.2
        
image snowdistant:
    contains:
        "snow2"
        zoom 0.5
        alpha 0.3
    contains:
        "snow2"
        alpha 0.7
    contains:
        "snow2"
        zoom 0.4
        alpha 0.5
    contains:
        "snow2"
        zoom 0.8
        alpha 0.5
        
image snowlight:
    contains:
        "snowlight2"
        zoom 0.5
        alpha 0.3
    contains:
        "snowlight2"
        alpha 0.7
    contains:
        "snowlight2"
        zoom 2.0
        alpha 0.5
    contains:
        "snowlight2"
        zoom 2.0
        alpha 0.5
    contains:
        "snowlight2"
        zoom 3.0
        alpha 0.4
    contains:
        "snowlight2"
        zoom 7.0
        alpha 0.3
    contains:
        "snowlight2"
        zoom 10.0
        alpha 0.2
        
image snowlight2 = SnowBlossom("back/effects/snowflake.png", 15, 20, (20, 800), (20, 600))

image petal = SnowBlossom(anim.Filmstrip(im.Sepia("gui/petal.png"), (20, 20), (2, 1), .13), 30, 20, (10, 250), (10, 200))
        
image sparklight = SnowBlossom(anim.Filmstrip("back/effects/spark.png", (12.5, 12.5), (4, 4), .13), 20, 20, (20, 400), (-20, -500), 3)

image spark:
    contains:
        "sparklight"
    contains:
        "sparklight"
    contains:
        "sparklight"
        zoom 1.5
        alpha 0.4
    contains:
        "sparklight"
        zoom 1.2
        alpha 0.8
        
image sunrays:
    additive 1.0
    contains:
        "back/effects/sunray1.png" 
        alpha 0
        linear 4.5 alpha 1.5
        linear 3.5 alpha 0
        repeat
    contains:
        "back/effects/sunray2.png" 
        alpha 0
        linear 2.5 alpha 1.5
        linear 2.5 alpha 0
        repeat
    contains:
        "back/effects/sunray3.png" 
        alpha 0
        linear 2.0 alpha 1.5
        linear 2.0 alpha 0
        repeat
    contains:
        "back/effects/sunray4.png" 
        alpha 0
        linear 5.0 alpha 1.5
        linear 2.0 alpha 0
        repeat
        
image grime:
    additive 0.4
    alpha 0.7
    contains:
        "back/effects/grime.png" with hpunch
        zoom 1.0
        0.2
        "back/effects/grime.png" with vpunch
        zoom 1.2
        0.1
        "back/effects/grime.png" with hpunch
        zoom 1.5
        0.1
        "back/effects/grime.png" with vpunch
        zoom 1.1
        0.2
        repeat
    linear 2.0 alpha 0.3
    linear 2.0 alpha 0.5
    linear 2.0 alpha 0.2
    linear 1.0 alpha 0.7
    repeat
    
image sunraysflip:
    additive 1.0
    contains:
        "back/effects/sunray1.png"
        xzoom -1
        xalign 1.0
        alpha 0
        linear 4.5 alpha 1.5
        linear 3.5 alpha 0
        repeat
    contains:
        "back/effects/sunray2.png" 
        xzoom -1
        xalign 1.0
        alpha 0
        linear 2.5 alpha 1.5
        linear 2.5 alpha 0
        repeat
    contains:
        "back/effects/sunray3.png" 
        xzoom -1
        xalign 1.0
        alpha 0
        linear 2.0 alpha 1.5
        linear 2.0 alpha 0
        repeat
    contains:
        "back/effects/sunray4.png" 
        xzoom -1
        xalign 1.0
        alpha 0
        linear 5.0 alpha 1.5
        linear 2.0 alpha 0
        repeat
        
image smoke:
    additive 0.2
    contains:
        "back/effects/smoke1.png" 
        alpha 0
        linear 4.5 alpha 1.5
        linear 3.5 alpha 0
        repeat
    contains:
        "back/effects/smoke2.png" 
        alpha 0
        linear 2.5 alpha 1.5
        linear 2.5 alpha 0
        repeat
    contains:
        "back/effects/smoke3.png" 
        alpha 0
        linear 2.0 alpha 1.5
        linear 2.0 alpha 0
        repeat
    contains:
        "back/effects/smoke4.png" 
        alpha 0
        linear 5.0 alpha 1.5
        linear 2.0 alpha 0
        repeat
        
image yellowsmoke:
    contains:
        im.MatrixColor("back/effects/smoke1.png", im.matrix.desaturate() * im.matrix.tint(1, 1, 0))
        alpha 0
        yzoom -1
        linear 4.5 alpha 1
        linear 3.5 alpha 0
        repeat
    contains:
        im.MatrixColor("back/effects/smoke2.png", im.matrix.desaturate() * im.matrix.tint(1, 1, 0))
        alpha 0
        yzoom -1
        linear 2.5 alpha 1
        linear 2.5 alpha 0
        repeat
    contains:
        im.MatrixColor("back/effects/smoke3.png", im.matrix.desaturate() * im.matrix.tint(1, 1, 0))
        alpha 0
        yzoom -1
        linear 2.0 alpha 1
        linear 2.0 alpha 0
        repeat
    contains:
        im.MatrixColor("back/effects/smoke4.png", im.matrix.desaturate() * im.matrix.tint(1, 1, 0))
        alpha 0
        yzoom -1
        linear 5.0 alpha 1
        linear 2.0 alpha 0
        repeat   

image pow:
    contains:
        "black"
        0.08
        "white"
        0.08
        "back/effects/pow1.jpg"
        0.08
        "white"
        0.08
        "back/effects/pow3.jpg"
        0.08
        "back/effects/pow4.jpg"
        0.08
        "black"
        0.08
        "white"
        0.08
        "back/effects/pow5.jpg"
        0.08
        "back/effects/pow6.jpg"
        0.08
        "black"
        0.08
        "white"
        0.08
        "black"
        0.08
        "back/effects/pow2.jpg"
        0.08
        "white"
        0.08
        "black"
        0.08
        repeat
        
image darkspell:
    contains:
        "back/effects/magic3.png"
        alpha 0.3
        linear 2.3 alpha 0
        linear 2.3 alpha 0.3
        repeat

image fire:
    additive 0.5
    contains:
        "back/effects/fire3.png"
        alpha 0.3
    contains:
        "back/effects/fire1.png" 
        alpha 0
        linear 1.0 alpha 0.8
        linear 1.0 alpha 0
        1.5
        repeat
    contains:
        "back/effects/fire2.png" 
        alpha 0
        0.5
        linear 1.0 alpha 0.8
        linear 1.0 alpha 0
        1.0
        repeat
    contains:
        "back/effects/fire3.png" 
        alpha 0
        1.0
        linear 0.7 alpha 0.8
        linear 0.7 alpha 0
        0.5
        repeat
    contains:
        "back/effects/fire4.png" 
        alpha 0
        1.5
        linear 1.0 alpha 0.8
        linear 1.0 alpha 0
        repeat
    contains:
        "back/effects/fire5.png" 
        alpha 0
        linear 0.7 alpha 0.5
        linear 0.7 alpha 0
        repeat        
        
image fire2:
    additive 1.0
    contains:
        "back/effects/fire1.png" 
        alpha 0
        linear 4.5 alpha 0.2
        linear 3.5 alpha 0
        repeat
    contains:
        "back/effects/fire2.png" 
        alpha 0
        linear 2.5 alpha 0.2
        linear 2.5 alpha 0
        repeat
    contains:
        "back/effects/fire3.png" 
        alpha 0
        linear 2.0 alpha 0.2
        linear 2.0 alpha 0
        repeat
    contains:
        "back/effects/fire4.png" 
        alpha 0
        linear 5.0 alpha 0.2
        linear 2.0 alpha 0
        repeat    

image fire4:
    contains:
        "back/effects/fire1.png" 
        alpha 0.3
    contains:
        "back/effects/fire2.png" 
        alpha 0.3
    contains:
        "back/effects/fire3.png" 
        alpha 0.3
        
        

