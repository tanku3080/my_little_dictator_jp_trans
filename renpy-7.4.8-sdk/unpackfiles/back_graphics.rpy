#####################################################################################################################################################
###  BACKGROUNDS
#####################################################################################################################################################
image armycamp = "back/armycamp.jpg"
image port = "back/port.jpg"
image tunnel = "back/tunnel.jpg"
image train = "back/train1.jpg"
image train2 = "back/train2.jpg"
image train_country_travel:
    contains:
        "back/train3.jpg"
    contains:
        "back/train3.jpg"
        ypos 0
        linear 0.08 ypos 0.007
        linear 0.08 ypos 0
        repeat
image train_snow_travel:
    contains:
        "back/train4.jpg"
    contains:
        "snow_day"
        ypos 0
        linear 0.08 ypos 0.007
        linear 0.08 ypos 0
        repeat
    contains:
        "transparent"
    contains:
        "snowdistant"
    contains:
        "back/train_overlay.png"
        ypos 0.007
        linear 0.08 ypos 0
        linear 0.08 ypos 0.007
        repeat
image train_overlay = "back/train_overlay.png"
image hospital_day = "back/hospital_day.jpg"
image hospital_night = "back/hospital_night.jpg"
image temple = "back/temple.jpg"
image imperium = "back/imperium.jpg"
image imperium_sunset = "back/imperium_sunset.jpg"
image imperium_boss:
    contains:
        "back/imperium_night.jpg"
    contains:
        "back/imperium_boss.jpg"
        alpha 0
        linear 2.0 alpha 1.0
        pause 0.3
        linear 2.0 alpha 0
        repeat
image lutetia = "back/lutetia.jpg"
image lutetia_tower = "back/lutetia_tower.jpg"
image pyramid = "back/pyramid.jpg"
image altberlin = "back/altberlin.jpg"
image moskva = "back/moskva.jpg"
image albion_day = "back/albion_day.jpg"
image albion_night = "back/albion_night.jpg"
image bigben_room_day = "back/bigben_room_day.jpg"
image bigben_room_night = "back/bigben_room_night.jpg"
image bigben_room_night_shake:
    contains:
        "back/bigben_room_night.jpg"
    contains:
        "back/bigben_room_night.jpg" with vpunch
        pause 4.2
        repeat 12
        
image starinbase = "back/starinbase.jpg"
image staringrada = "back/staringrada.jpg"    
image savanna = "back/savanna.jpg"
image village1 = "back/village1.jpg"
image village2 = "back/village2.jpg"
image city1 = "back/city1.jpg"
image city1flip:
    contains:
        "back/city1.jpg"
        xzoom -1
image city2 = "back/city2.jpg"
image city3 = "back/city3.jpg"
image city4 = "back/city4.jpg"
image city4_night = "back/city4_night.jpg"
image stadium = "back/stadium.jpg"
image stadium2 = "back/stadium2.jpg"
image alley1 = "back/alley1.jpg"
image alley2 = "back/alley2.jpg"        
image alley_gray = im.Grayscale("back/alley2.jpg")
image warroom = "back/warroom.jpg"
image warroom_large = "back/warroom_large.jpg"
image warroom_dark = "back/warroom_dark.jpg"
image balcony = "back/balcony.jpg"
image balcony_night = "back/balcony_night.jpg"
image corridor = "back/corridor.jpg"
image corridor_night = "back/corridor_night.jpg"
image corridor_sunset = "back/corridor_sunset.jpg"
image dining_room = "back/dining_room.jpg"
image hitora_room = "back/hitora_room.jpg"
image hitora_room_night = im.MatrixColor("back/hitora_room.jpg", im.matrix.brightness(-.5) * im.matrix.tint(0.3, 0.3, 0.9) * im.matrix.saturation(0.7) * im.matrix.contrast(0.8))
image yamato_room = "back/yamato_room.jpg"
image yamato_room_sepia = im.Sepia(im.MatrixColor("back/yamato_room.jpg", im.matrix.brightness(0.3) * im.matrix.tint(1, 1, 1)))
image yamato_room_night = "back/yamato_room_night.jpg"
image tent = "back/tent.jpg"
image berghof_day = "back/berghof_day.jpg"
image berghof_zoom = "back/berghof_zoom.jpg"
image berghof_dark = "back/berghof_dark.jpg"
image berghof_night = "back/berghof_night.jpg"
image mansion1 = "back/mansion1.jpg"
image mansion2 = "back/mansion2.jpg"
image mansion3 = "back/mansion3.jpg"
image mansion3_night = "back/mansion3_night.jpg"
image mansion_room = "back/mansion_room.jpg"
image palace_room = "back/palace_room.jpg"
image palace_room_night = "back/palace_room_night.jpg"
image snow_day = "back/snow_day.jpg"
image snow_tanks = "back/snow_tanks.jpg"
image snow_slopes = "back/snow_slopes.jpg"
image snow_farm = "back/snow_farm.jpg"
image saltmines = "back/saltmines.jpg"
image beach_day = "back/beach_day.jpg"
image beach_evening = "back/beach_evening.jpg"
image beach_rain = "back/beach_rain.jpg"
image beachhead = "back/beachhead.jpg"
image beach_trees = "back/beach_trees.jpg"
image beach_trees_battle:
    contains:
        "back/beach_trees.jpg"
    contains:
        alpha 1.0
        "back/beach_trees.jpg" with hpunch
        0.01
        "back/beach_trees.jpg" with vpunch
        0.1
        "back/beach_trees.jpg" with hpunch
        0.05
        "back/beach_trees.jpg" with hpunch
        0.1
        "back/beach_trees.jpg" with hpunch
        linear 0.5 alpha 0
        10.0
        repeat
image farm_day = "back/farm_day.jpg"
image forest_day = "back/forest_day.jpg"
image woodland_day = "back/woodland_day.jpg"
image woodland_night = "back/woodland_night.jpg"
image woodland_clearing = "back/woodland_clearing.jpg"
image woodland_cave = "back/woodland_cave.jpg"
image countrylane_day = "back/countrylane_day.jpg"
image countrylane_day_notree = "back/countrylane_day_notree.jpg"
image countrylane_day_notree_night = "back/countrylane_day_notree_night.jpg"
image field_day = "back/field_day.jpg"
image field_rain = "back/field_rain.jpg"
image field_day_notree = "back/field_day_notree.jpg"
image desert_day = "back/desert_day.jpg"
image desert_night = "back/desert_night.jpg"
image desert_smoke = "back/desert_smoke.jpg"
image desert_town = "back/desert_town.jpg"
image desert_tanks = "back/desert_tanks.jpg"
image bombback = "back/effects/bomb.jpg"
image edooh_palace = "back/edooh_palace.jpg"
image edooh_palace_stomp:
    contains:
        "edooh_palace" with vpunch
        2.0
        repeat
image edooh = "back/edooh.jpg"
image whitehouse = "back/whitehouse.jpg"
image reflectingpalace = "back/reflectingpalace.jpg"
image zhina_lane = "back/zhina_lane.jpg"
image zhina_temple = "back/zhina_temple.jpg"
image zhina_temple_night = "back/zhina_temple_night.jpg"
image zhina_temple_room = "back/zhina_temple_room.jpg"
image zhina_temple_room_distort:
    contains:
        "zhina_temple_room"
    contains:
        "back/zhina_temple_room.jpg"
        alpha 0.7 xalign 0.5 yalign 0.5
        linear 2.0 xzoom 1.25 yzoom 0.75 alpha 0.6
        linear 2.0 yzoom 1.25 xzoom 0.75 alpha 0.7
        repeat
image westernmap = "back/map/westernmap.jpg"
image westernmapsmall = im.Sepia(im.FactorScale("back/map/westernmap.jpg", 0.299))

image tankinside:
    contains:
        Solid(color("#373737"))
    contains:
        "transparent"

image yamato_swordplay:
    contains:
        Fixed(im.Crop("battle/units/commander_yamato_main1_attack.png", (1593, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        pause 4.0
        Fixed(im.Crop("battle/units/commander_yamato_main1_attack.png", (1770, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        pause 0.1
        Fixed(im.Crop("battle/units/commander_yamato_main1_attack.png", (708, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        pause 0.1
        Fixed(im.Crop("battle/units/commander_yamato_main1_attack.png", (885, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        pause 0.1
        Fixed(im.Crop("battle/units/commander_yamato_main1_attack.png", (1062, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        pause 0.1
        Fixed(im.Crop("battle/units/commander_yamato_main1_attack.png", (1770, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        pause 0.1
        Fixed(im.Crop("battle/units/commander_yamato_main1_attack.png", (1062, 0, 177, 258), xalign=0.5, yalign=0.5), xsize=840, ysize=840)
        pause 0.1
        repeat
        

image nightmare_composite = LiveComposite(
    (3333, 2666),
    (0, 0), "gui/nightmareback.jpg",
    (1787, 0), At("specialgroup_zipangu_gunner_heer1_walk_front", flip_horizontal),
    (1627, 180), "yamato_swordplay",
    (2107, 1520), "panzer_ba10_walk_front",
    (2647, 1350), At("zhina_gunner_heer1_walk_front", flip_horizontal),
    (1767, 1900), At("meowist_marksman_heer1_walk_front", flip_horizontal),
    (2417, 1700), "zhina_gunner_heer1_walk_front")

image nightmare2_composite = LiveComposite(
    (3333, 2666),
    (0, 0), "gui/nightmareback.jpg",
    (1850, -100), "zhina_gunner_heer1_walk_front",
    (2410, 190), "meowist_gunner_heer1_walk_front",
    (1280, -150), At("zhina_gunner_heer1_walk_front", flip_horizontal),
    (1300, 440), At("zhina_gunner_heer1_walk_front", flip_horizontal),
    (1627, 180), "yamato_swordplay")

image nightmare3_composite = LiveComposite(
    (3333, 2666),
    (0, 0), "gui/nightmareback.jpg",
    (1850, -100), "zhina_gunner_heer1_main1_attack_front",
    (2410, 190), "meowist_gunner_heer1_main1_attack_front",
    (1280, -150), At("zhina_gunner_heer1_main1_attack_front", flip_horizontal),
    (1300, 440), At("zhina_gunner_heer1_main1_attack_front", flip_horizontal),
    (1627, 180), "yamato_swordplay")

image nightmare1:
    contains:
        "nightmare_composite"
        xalign 0.01 yalign 0.5
    contains:
        "spark"
    contains:
        "transparent2"
    contains:
        "grime"

image nightmare2:
    contains:
        "nightmare_composite"
        xalign 0.01 yalign 0.5
        pause 1.0
        linear 5.0 xalign 0.9 yalign 0.05
    contains:
        "spark"
    contains:
        "transparent2"
    contains:
        "grime"
        
image nightmare3:
    contains:
        "nightmare_composite"
        xalign 0.9 yalign 0.05
        pause 1.0
        linear 5.0 xalign 1.0 yalign 1.0
    contains:
        "spark"
    contains:
        "transparent2"
    contains:
        "grime"
        
image nightmare4:
    contains:
        "nightmare2_composite"
        xalign 0.9 yalign 0.05
    contains:
        "spark"
    contains:
        "transparent2"
    contains:
        "grime"
        
image nightmare5:
    contains:
        "nightmare3_composite"
        xalign 0.9 yalign 0.05
    contains:
        "spark"
    contains:
        "transparent2"
    contains:
        "grime"
        
image flashback1:
    contains:
        im.Sepia("back/mansion2.jpg")
    contains:
        LiveComposite(
            (500, 950),
            (0, 0), im.Sepia(im.MatrixColor("character/general/kaiser_base1.png", im.matrix.brightness(-.2) * im.matrix.tint(0.9, 0.9, 1.0))),
            (0, 0), im.Sepia(im.MatrixColor("character/general/kaiser_determined1.png", im.matrix.brightness(-.2) * im.matrix.tint(0.9, 0.9, 1.0)))
            )
        xalign 0.5
        yalign 1.0
    contains:
        "heavyrain"
    contains:
        "grime"
    contains:
        "black_lines"
        
image flashback2:
    contains:
        im.Sepia("back/stadium.jpg")
    contains:
        LiveComposite(
            (670, 920),
            (0, 0), im.Sepia("character/man/man_base3.png"),
            (0, 0), im.Sepia("character/man/man_evil3.png")
            )
        xalign 0.3
        yalign 1.0
    contains:
        LiveComposite(
            (720, 909),
            (0, 0), im.Sepia("character/hitora/hitora_base2.png"),
            (0, 0), im.Sepia("character/hitora/hitora_happy1.png")
            )
        xalign 0.7
        yalign 1.0
    contains:
        "grime"
    contains:
        "black_lines"
        
image flashback3:
    contains:
        im.Sepia("back/armycamp.jpg")
    contains:
        LiveComposite(
            (616, 980),
            (40, 160), im.Sepia("character/guderian/guderian_base1.png"),
            (40, 160), im.Sepia("character/guderian/guderian_determined1.png")
            )
        xalign 0.3
        yalign 1.0
    contains:
        LiveComposite(
            (470, 919),
            (0, 0), im.Sepia("character/manstein/manstein_base1.png"),
            (0, 0), im.Sepia("character/manstein/manstein_moe1.png")
            )
        xalign 0.7
        yalign 1.0
    contains:
        "grime"
    contains:
        "black_lines"

image flashback4:
    contains:
        im.Sepia("back/woodland_day.jpg")
    contains:
        LiveComposite(
            (616, 980),
            (40, 160), im.Sepia("character/guderian/guderian_base1.png"),
            (40, 160), im.Sepia("character/guderian/guderian_shock1.png")
            )
        xalign 0.3
        yalign 1.0
    contains:
        LiveComposite(
            (470, 919),
            (0, 0), im.Sepia("character/manstein/manstein_base1.png"),
            (0, 0), im.Sepia("character/manstein/manstein_determined1.png")
            )
        xalign 0.7
        yalign 1.0
    contains:
        "grime"
    contains:
        "black_lines"
        

image field_day_tank:
    contains:
        "back/field_day.jpg"
    contains:
        "back/field_day.jpg" with vpunch
        0.1
        repeat

image snow_ski:
    contains:
        "back/snow_day.jpg"
    contains:
        "back/snow_day.jpg" with vpunch
        0.1
        repeat
        
image snow_slopes_ski:
    contains:
        "back/snow_slopes.jpg"
    contains:
        "back/snow_slopes.jpg" with vpunch
        0.1
        repeat
        
image woodland_tank:
    contains:
        "back/woodland_day.jpg"
    contains:
        "back/woodland_day.jpg" with vpunch
        0.1
        repeat
        
image woodland_clearing_tank:
    contains:
        "back/woodland_clearing.jpg"
    contains:
        "back/woodland_clearing.jpg" with vpunch
        0.1
        repeat

image farm_tanks:
    contains:
        "back/farm_tanks.jpg"
    contains:
        "back/farm_tanks.jpg" with vpunch
        0.1
        repeat
        
image countrylane_tanks:
    contains:
        "back/countrylane_day.jpg"
    contains:
        "back/countrylane_day.jpg" with vpunch
        0.1
        repeat
        
image carinterior:
    contains:
        "black"
    contains:
        "back/countrylane_day_notree.jpg"
        ypos 0.01
        linear 2.0 ypos 0.05
        linear 2.0 ypos 0.01
        repeat
    contains:
        "back/car_interior.png"
        ypos 0
        linear 0.1 ypos 0.01
        linear 0.1 ypos 0
        repeat

image carinteriorhalt:
    contains:
        "black"
    contains:
        "back/countrylane_day_notree.jpg"
    contains:
        "back/car_interior.png"
        
image savanna_battle:
    contains:
        "back/savanna.jpg"
    contains:
        alpha 1.0
        "back/savanna.jpg" with hpunch
        0.01
        "back/savanna.jpg" with vpunch
        0.1
        "back/savanna.jpg" with hpunch
        0.05
        "back/savanna.jpg" with hpunch
        0.1
        "back/savanna.jpg" with hpunch
        linear 0.5 alpha 0
        10.0
        repeat

image albion_day2:
    additive 0
    contains:
        "back/albion_day.jpg"
        alpha 0.2
        linear 2 zoom 1.0018
        linear 3 zoom 1.02
        repeat
    contains:
        "back/albion_day.jpg"
        alpha 0.4
        linear 2 zoom 1.011
        linear 3 zoom 1.001
        repeat
    contains:
        "back/albion_day.jpg"
        alpha 0.8
        linear 1 zoom 1.001
        linear 2 zoom 1.001
        alpha 0.3
        repeat
    contains:
        "back/albion_day.jpg"
        alpha 0.2
        linear 3 zoom 0.997
        linear 2 zoom 1
        repeat
    contains:
        alpha 1.0
        "back/albion_day.jpg" with hpunch
        0.01
        "back/albion_day.jpg" with vpunch
        0.1
        "back/albion_day.jpg" with hpunch
        0.05
        "back/albion_day.jpg" with hpunch
        0.1
        "back/albion_day.jpg" with hpunch
        linear 0.5 alpha 0
        15.0
        repeat

image stadiumfade:
    contains:
        "back/stadium2.jpg"
        alpha .4
        xalign 0.5
        yalign 0.5
        linear 2.0 xalign 0.7 yalign 0.7 zoom 1.1
        linear 2.0 xalign 0.9 yalign 0.5 zoom 1.2
        linear 2.0 xalign 0.7 yalign 0.3 zoom 1.1
        linear 2.0 xalign 0.5 yalign 0.5 zoom 1.0
        linear 2.0 xalign 0.3 yalign 0.7 zoom 1.1
        linear 2.0 xalign 0.1 yalign 0.5 zoom 1.2
        linear 2.0 xalign 0.3 yalign 0.3 zoom 1.1
        linear 2.0 xalign 0.5 yalign 0.5 zoom 1.0
        repeat
    contains:
        "back/stadium2.jpg"
        alpha .4
        xalign 0.3
        yalign 0.7
        linear 3.0 xalign 0.1 yalign 0.5 zoom 1.2
        linear 3.0 xalign 0.3 yalign 0.3 zoom 1.1
        linear 3.0 xalign 0.5 yalign 0.5 zoom 1.0
        linear 3.0 xalign 0.7 yalign 0.7 zoom 1.1
        linear 3.0 xalign 0.9 yalign 0.5 zoom 1.2
        linear 3.0 xalign 0.7 yalign 0.3 zoom 1.1
        linear 3.0 xalign 0.5 yalign 0.5 zoom 1.0
        linear 3.0 xalign 0.3 yalign 0.7 zoom 1.1
        repeat
        
image stadiumfight:
    contains:
        "back/stadium.jpg" with hpunch
        0.5
        "back/stadium.jpg" with vpunch
        0.5
        repeat    
        
image stadium2_run:
    contains:
        "back/stadium2.jpg"
    contains:
        "back/stadium2.jpg" with vpunch
        0.1
        repeat

image heavyrain:
    contains:
        "back/effects/heavyrain1.png"
        alpha 0
        linear 0.1 alpha 0.3
        linear 0.1 alpha 0
        linear 0.1 alpha 0
        linear 0.1 alpha 0
        repeat
    contains:
        "back/effects/heavyrain2.png"
        alpha 0.3
        linear 0.1 alpha 0
        linear 0.1 alpha 0
        linear 0.1 alpha 0
        linear 0.1 alpha 0.3
        repeat
    contains:
        "back/effects/heavyrain3.png"
        alpha 0
        linear 0.1 alpha 0
        linear 0.1 alpha 0.3
        linear 0.1 alpha 0
        linear 0.1 alpha 0
        repeat
    contains:
        "back/effects/heavyrain4.png"
        alpha 0
        linear 0.1 alpha 0
        linear 0.1 alpha 0
        linear 0.1 alpha 0.3
        linear 0.1 alpha 0
        repeat
    contains:
        "back/effects/heavyrain4.png"
        alpha 0
        additive 0
        linear 10.0
        linear 1.0 alpha 0.6 additive 1.0
        linear 1.0 alpha 0 additive 0
        repeat

image tornado:
    contains:
        "back/sky/day4.jpg"
        xalign 0.5 yalign 0.5 zoom 2.0 rotate 0
        linear 1.0 rotate 360
        repeat
    contains:
        "black"
        xalign 0.5 yalign 0.5 zoom 2.0 rotate 0 alpha 0.3
        linear 1.0 rotate 360
        repeat
        
image edoohbomb:
    additive 0.2
    contains:
        im.MatrixColor("back/edooh.jpg",
                                         im.matrix.brightness(-.5) * im.matrix.tint(0.9, 0.9, 1.0 ))
        alpha 0
        zoom 1.018
        linear 2.5 alpha 1.5
        linear 3.5 alpha 0
        repeat
    contains:
        im.MatrixColor("back/edooh.jpg",
                                         im.matrix.brightness(-.7) * im.matrix.tint(0.9, 0.9, 1.0 ))
        alpha 0
        zoom 1.015
        linear 2.5 alpha 1.5
        linear 2.5 alpha 0
        repeat
    contains:
        im.MatrixColor("back/edooh.jpg",
                                         im.matrix.brightness(-.5) * im.matrix.tint(0.9, 0.9, 1.0 ))
        alpha 0
        zoom 1.01
        linear 2.0 alpha 1.5
        linear 2.0 alpha 0
        repeat
    contains:
        im.MatrixColor("back/edooh.jpg",
                                         im.matrix.brightness(-.9) * im.matrix.tint(0.9, 0.9, 1.0 ))
        alpha 0
        zoom 1.013
        linear 3.0 alpha 1.5
        linear 2.0 alpha 0.1
        repeat
    
image bomb:
    additive 1.0
    contains:
        "back/effects/bomb.jpg"
        alpha 0                                                              
        linear 4.5 alpha 0.4
        linear 3.5 alpha 0
    contains:
        "back/effects/bomb.jpg"
        alpha 0
        linear 2.5 alpha 0.3
        linear 2.5 alpha 0
        repeat
    contains:
        "back/effects/bomb.jpg"
        alpha 0
        linear 2.0 alpha 0.3
        linear 2.0 alpha 0
    contains:
        "back/effects/bomb.jpg" 
        alpha 0
        linear 5.0 alpha 0.3
        linear 2.0 alpha 0
    contains:
        "back/effects/bomb.jpg"
        alpha 0
        linear 4.5 alpha 0.4
        linear 2.0 alpha 0     

image snow_tanks_battle:
    contains:
        "back/snow_tanks.jpg"
    contains:
        alpha 1.0
        "back/snow_tanks.jpg" with hpunch
        0.01
        "back/snow_tanks.jpg" with vpunch
        0.1
        "back/snow_tanks.jpg" with hpunch
        0.05
        "back/snow_tanks.jpg" with hpunch
        0.1
        "back/snow_tanks.jpg" with hpunch
        linear 0.5 alpha 0
        10.0
        repeat

image sea1 = "back/sea1.jpg"
image sea1_night = "back/sea1_night.jpg"
image sea2 = "back/sea2.jpg"
image sea3 = "back/sea3.jpg"

#Sky
image sky1:
    "back/sky/sky1.jpg"
    xalign 0.5
    yalign 0.5
    rotate 0
    linear 1.0 rotate 2.0
    linear 1.0 rotate 0
    linear 1.0 rotate -2.0
    linear 1.0 rotate 0
    repeat
    
image sky2:
    "back/sky/sky2.jpg"
    xalign 0.5
    yalign 0.5
    rotate 0
    linear 1.0 rotate 2.0
    linear 1.0 rotate 0
    linear 1.0 rotate -2.0
    linear 1.0 rotate 0
    repeat

image sky2train:
    contains:
        "back/sky/day3.jpg"
    contains:
        "back/sky/day3.jpg" with vpunch
        0.1
        repeat
        
image sky_train:
    contains:
        "back/sky/day2.jpg"
    contains:
        "back/sky/day2.jpg" with vpunch
        0.1
        repeat

image sky_snow:
    contains:
        "back/sky/day4.jpg"
    contains:
        "snow"
    contains:
        "mist"
        
image sky_snowtrain:
    contains:
        "back/sky/day4.jpg"
    contains:
        "back/sky/day4.jpg" with vpunch
        0.1
        repeat
    contains:
        "snow"
    contains:
        "mist"
        
image sky_night:
    contains:
        "back/sky/night.jpg"
    contains:
        "back/sky/night.jpg" with vpunch
        0.1
        repeat
        
image sky_dawn:
    "back/sky/sky3.jpg"
    xalign 0.5
    yalign 0.5
    rotate 0
    linear 1.0 rotate 2.0
    linear 1.0 rotate 0
    linear 1.0 rotate -2.0
    linear 1.0 rotate 0
    repeat
        
image day1 = "back/sky/day1.jpg"
image day2 = "back/sky/day2.jpg"
image day3 = "back/sky/day3.jpg"
image day4 = "back/sky/day4.jpg"
image day5 = "back/sky/day5.jpg"
image evening = "back/sky/evening.jpg"
image night = "back/sky/night.jpg"
image skyrain:
    contains:
        "back/sky/day4.jpg"
    contains:
        "heavyrain"
    
image cave = "back/sky/cave.jpg"

image day1_tank:
    contains:
        "back/sky/day1.jpg"
    contains:
        "back/sky/day1.jpg" with vpunch
        0.1
        repeat

image day4_tank:
    contains:
        "back/sky/day4.jpg"
    contains:
        "back/sky/day4.jpg" with vpunch
        0.1
        repeat

image day5_tank:
    contains:
        "back/sky/day5.jpg"
    contains:
        "back/sky/day5.jpg" with vpunch
        0.1
        repeat

image fireworks:
    contains:
        "back/sky/fireworks.jpg"
    contains:
        "white"
        alpha 0
        pause 5.0
        linear 0.1 alpha 1.0
        linear 1.0 alpha 0
        repeat
        

image junker1:
    "back/sky/junker1.png"
    yalign 0.525
    xalign 0.475
    linear 0.6 xalign 0.45 yalign 0.55 rotate 1
    linear 0.6 xalign 0.475 yalign 0.525
    linear 0.6 xalign 0.5 yalign 0.5 rotate 0
    linear 0.6 xalign 0.525 yalign 0.475
    linear 0.6 xalign 0.55 yalign 0.45 rotate -1
    linear 0.6 xalign 0.525 yalign 0.475
    linear 0.6 xalign 0.5 yalign 0.5 rotate 0
    linear 0.6 xalign 0.475 yalign 0.525
    linear 0.6 xalign 0.45 yalign 0.55 rotate 1
    linear 0.6 xalign 0.475 yalign 0.55
    linear 0.6 xalign 0.5 yalign 0.55 rotate 0
    linear 0.6 xalign 0.525 yalign 0.55
    linear 0.6 xalign 0.55 yalign 0.475 rotate -1
    linear 0.6 xalign 0.525 yalign 0.45
    linear 0.6 xalign 0.5 yalign 0.475
    linear 0.6 xalign 0.475 yalign 0.5
    linear 0.6 xalign 0.45 yalign 0.5
    linear 0.6 xalign 0.475 yalign 0.5
    linear 0.6 xalign 0.5 yalign 0.5
    linear 0.6 xalign 0.525 yalign 0.5
    linear 0.6 xalign 0.55 yalign 0.525
    linear 0.6 xalign 0.525 yalign 0.55
    linear 0.6 xalign 0.5 yalign 0.525
    linear 0.6 xalign 0.475 yalign 0.525
    repeat
    
image spitfire1:
    "back/sky/spitfire1.png"
    yalign 0.525
    xalign 0.475
    linear 0.6 xalign 0.45 yalign 0.55 rotate 1
    linear 0.6 xalign 0.475 yalign 0.525
    linear 0.6 xalign 0.5 yalign 0.5 rotate 0
    linear 0.6 xalign 0.525 yalign 0.475
    linear 0.6 xalign 0.55 yalign 0.45 rotate -1
    linear 0.6 xalign 0.525 yalign 0.475
    linear 0.6 xalign 0.5 yalign 0.5 rotate 0
    linear 0.6 xalign 0.475 yalign 0.525
    linear 0.6 xalign 0.45 yalign 0.55 rotate 1
    linear 0.6 xalign 0.475 yalign 0.55
    linear 0.6 xalign 0.5 yalign 0.55 rotate 0
    linear 0.6 xalign 0.525 yalign 0.55
    linear 0.6 xalign 0.55 yalign 0.475 rotate -1
    linear 0.6 xalign 0.525 yalign 0.45
    linear 0.6 xalign 0.5 yalign 0.475
    linear 0.6 xalign 0.475 yalign 0.5
    linear 0.6 xalign 0.45 yalign 0.5
    linear 0.6 xalign 0.475 yalign 0.5
    linear 0.6 xalign 0.5 yalign 0.5
    linear 0.6 xalign 0.525 yalign 0.5
    linear 0.6 xalign 0.55 yalign 0.525
    linear 0.6 xalign 0.525 yalign 0.55
    linear 0.6 xalign 0.5 yalign 0.525
    linear 0.6 xalign 0.475 yalign 0.525
    repeat
    
image junker1 pivot:
    "back/sky/junker1.png"
    yalign 0.525
    xalign 0.475
    linear 0.6 xalign 0.45 yalign 0.55 rotate 71
    linear 0.6 xalign 0.475 yalign 0.525
    linear 0.6 xalign 0.5 yalign 0.5 rotate 70
    linear 0.6 xalign 0.525 yalign 0.475
    linear 0.6 xalign 0.55 yalign 0.45 rotate 69
    linear 0.6 xalign 0.525 yalign 0.475
    linear 0.6 xalign 0.5 yalign 0.5 rotate 70
    linear 0.6 xalign 0.475 yalign 0.525
    linear 0.6 xalign 0.45 yalign 0.55 rotate 71
    linear 0.6 xalign 0.475 yalign 0.55
    linear 0.6 xalign 0.5 yalign 0.55 rotate 70
    linear 0.6 xalign 0.525 yalign 0.55
    linear 0.6 xalign 0.55 yalign 0.475 rotate 69
    linear 0.6 xalign 0.525 yalign 0.45
    linear 0.6 xalign 0.5 yalign 0.475
    linear 0.6 xalign 0.475 yalign 0.5
    linear 0.6 xalign 0.45 yalign 0.5
    linear 0.6 xalign 0.475 yalign 0.5
    linear 0.6 xalign 0.5 yalign 0.5
    linear 0.6 xalign 0.525 yalign 0.5
    linear 0.6 xalign 0.55 yalign 0.525
    linear 0.6 xalign 0.525 yalign 0.55
    linear 0.6 xalign 0.5 yalign 0.525
    linear 0.6 xalign 0.475 yalign 0.525
    repeat

image clouds:
    contains:
        "back/effects/cloud1.png"
        yalign 1.1
        xalign 8.0
        alpha 0.95
        linear 4.0 xalign -8.0
        7.0
        repeat
    contains:
        "back/effects/cloud2.png"
        yalign 0
        xalign 7.0
        alpha 0.95
        4.0
        linear 10.0 xalign -7.0
        3.0
        repeat
        
image cloudsflip:
    contains:
        "back/effects/cloud1.png"
        yalign 1.1
        xalign -8.0
        alpha 0.95
        linear 4.0 xalign 8.0
        7.0
        repeat
    contains:
        "back/effects/cloud2.png"
        yalign 0
        xalign -7.0
        alpha 0.95
        4.0
        linear 10.0 xalign 7.0
        3.0
        repeat
        
image clouds2:
    contains:
        im.MatrixColor("back/effects/cloud1.png",
                                         im.matrix.brightness(0) * im.matrix.tint(1.0, 0.7, 0.4))
        yalign 1.1
        xalign 8.0
        alpha 0.95
        linear 4.0 xalign -8.0
        7.0
        repeat
    contains:
        im.MatrixColor("back/effects/cloud2.png",
                                         im.matrix.brightness(0) * im.matrix.tint(1.0, 0.7, 0.4))
        yalign 0
        xalign 7.0
        alpha 0.95
        4.0
        linear 10.0 xalign -7.0
        3.0
        repeat        
        
image planeformation:
    contains:
        "back/sky/plane_formation.png"
        xalign 1.5
        yalign 0.4
        alpha 0.8
        linear 9.0 xalign 0.4 yalign -0.2 alpha 1.0
        pause 5.0
        repeat
    contains:
        "back/sky/plane_formation.png"
        xalign 0.6
        yalign 0.4
        alpha 0
        pause 5.0
        linear 9.0 xalign 0.1 yalign -0.1 alpha 1.0
        pause 3.3
        repeat
        
image planes:
    contains:
        "back/sky/spitfire1.png"
        zoom 0.02
        xalign 2.0
        yalign 0.9
        5.5
        linear 10.0 xalign -2.0 yalign 0.1
        4.5
        repeat
    contains:
        "back/sky/junker1.png"
        xzoom -1
        zoom 0.02
        xalign 2.0
        yalign 0.9
        5.0
        linear 10.0 xalign -2.0 yalign 0.1
        5.0
        repeat
    contains:
        "back/sky/junker1.png"
        xzoom -1
        zoom 0.03
        xalign 5.0
        yalign 0.3
        11.0
        linear 10.0 xalign -5.0 yalign 0.2
        9.0
        repeat
    contains:
        "back/sky/junker1.png"
        xzoom -1
        zoom 0.05
        xalign 5.0
        yalign 0.4
        4.0
        linear 8.0 xalign -5.0 yalign 0.2
        7.0
        repeat
    contains:
        "back/sky/junker1.png"
        xzoom -1
        zoom 0.2
        xalign 5.0
        yalign 0.1
        7.0
        linear 9.0 xalign -5.0 yalign 0.2
        4.0
        repeat
    contains:
        "back/sky/spitfire1.png"
        zoom 0.2
        xzoom -1
        xalign -5.0
        yalign 0.8
        9.0
        linear 9.0 xalign 5.0 yalign 0.3
        1.0
        repeat
    contains:
        "back/sky/spitfire1.png"
        zoom 0.3
        xzoom -1
        xalign -5.0
        yalign 0.8
        2.0
        linear 9.0 xalign 5.0 yalign 0.8
        8.0
        repeat
    contains:
        "back/sky/junker1.png"
        zoom 0.3
        xalign -5.0
        yalign 0.9
        7.0
        linear 6.0 xalign 5.0
        3.0
        repeat
    contains:
        "back/sky/spitfire2.png"
        zoom 0.3
        xalign -2.0
        yalign -3.0
        12.0
        linear 4.0 xalign 2.0 yalign 3.0
        8.0
        repeat
    contains:
        "back/sky/spitfire1.png"
        zoom 0.5
        xalign 5.0
        yalign 0.6
        10.0
        linear 4.0 xalign -5.0 yalign 0.6
        repeat
    contains:
        "back/sky/junker2.png"
        zoom 0.6
        xalign -2.0
        yalign 2.3
        15.0
        linear 2.0 xalign 3.0 yalign -3.3
        5.0
        repeat
        
image planes2:
    contains:
        "back/sky/spitfire1.png"
        zoom 0.02
        xalign 2.0
        yalign -0.4
        5.5
        linear 16.0 xalign -2.0 yalign 0.4
        6.5
        repeat
    contains:
        "back/sky/junker1.png"
        xzoom -1
        zoom 0.02
        xalign 2.0
        yalign -0.4
        5.0
        linear 16.0 xalign -2.0 yalign 0.4
        7.0
        repeat
    contains:
        "back/sky/junker1.png"
        xzoom -1
        zoom 0.03
        xalign 5.0
        yalign 0.2
        11.0
        linear 16.0 xalign -5.0 yalign 0.2
        1.0
        repeat
    contains:
        "back/sky/junker1.png"
        xzoom -1
        zoom 0.05
        xalign 5.0
        yalign 0.2
        4.0
        linear 12.0 xalign -5.0 yalign 0.2
        6.0
        repeat
    contains:
        "back/sky/junker1.png"
        xzoom -1
        zoom 0.1
        xalign 5.0
        yalign 0.1
        6.0
        linear 7.0 xalign -5.0 yalign 0.2
        4.0
        repeat
    contains:
        "back/sky/spitfire1.png"
        zoom 0.1
        xzoom -1
        xalign -5.0
        yalign 0.3
        9.0
        linear 7.0 xalign 5.0 yalign 0.3
        1.0
        repeat
    contains:
        "back/sky/spitfire1.png"
        zoom 0.2
        xzoom -1
        xalign -5.0
        yalign 0.25
        3.0
        linear 5.0 xalign 5.0 yalign 0.25
        8.0
        repeat
    contains:
        "back/sky/junker1.png"
        zoom 0.2
        xalign -5.0
        yalign 0.3
        7.0
        linear 5.0 xalign 5.0
        3.0
        repeat

image desert_smoke_tank:
    contains:
        "back/desert_smoke.jpg"
    contains:
        "back/desert_smoke.jpg" with vpunch
        0.1
        repeat
        
image bunker_day = "back/bunker_day.jpg"
        
image desert_bunker_night = "back/desert_bunker_night.jpg"
image desert_bunker = "back/desert_bunker.jpg"
image desert_bunker2:
    additive 0
    contains:
        "back/desert_bunker.jpg"
        alpha 0.2
        linear 2 zoom 1.0018
        linear 3 zoom 1.02
        repeat
    contains:
        "back/desert_bunker.jpg"
        alpha 0.4
        linear 2 zoom 1.011
        linear 3 zoom 1.001
        repeat
    contains:
        "back/desert_bunker.jpg"
        alpha 0.8
        linear 1 zoom 1.001
        linear 2 zoom 1.001
        alpha 0.3
        repeat
    contains:
        "back/desert_bunker.jpg"
        alpha 0.2
        linear 3 zoom 0.997
        linear 2 zoom 1
        repeat
    contains:
        alpha 1.0
        "back/desert_bunker.jpg" with hpunch
        0.01
        "back/desert_bunker.jpg" with vpunch
        0.1
        "back/desert_bunker.jpg" with hpunch
        0.05
        "back/desert_bunker.jpg" with hpunch
        0.1
        "back/desert_bunker.jpg" with hpunch
        linear 0.5 alpha 0
        10.0
        repeat

image desert_day_tank:
    contains:
        "back/desert_day.jpg"
    contains:
        "back/desert_day.jpg" with vpunch
        0.1
        repeat
        
image desert_tanks_tank:
    contains:
        "back/desert_tanks.jpg"
    contains:
        "back/desert_tanks.jpg" with vpunch
        0.1
        repeat

image pyramid_fight:
    contains:
        "back/pyramid.jpg" with hpunch
        0.5
        "back/pyramid.jpg" with vpunch
        0.5
        repeat 
        
image desert_tanks_fight:
    contains:
        "back/desert_tanks.jpg" with hpunch
        0.5
        "back/desert_tanks.jpg" with vpunch
        0.5
        repeat 
        
image desert_tanks2:
    contains:
        "back/desert_tanks.jpg"
    contains:
        alpha 1.0
        "back/desert_tanks.jpg" with hpunch
        0.01
        "back/desert_tanks.jpg" with vpunch
        0.1
        "back/desert_tanks.jpg" with hpunch
        0.05
        "back/desert_tanks.jpg" with hpunch
        0.1
        "back/desert_tanks.jpg" with hpunch
        linear 0.5 alpha 0
        10.0
        repeat
        
image desert_tanks3:
    additive 0.2
    contains:
        "back/desert_tanks.jpg"
        alpha 0.5
        linear 2 zoom 1.1
        linear 8 zoom 1.02 alpha 0.6
        linear 1 alpha 0.2
        repeat
    contains:
        "back/desert_tanks.jpg"
        alpha 0.4
        linear 12 zoom 1.11
        0.5
        linear 12 zoom 1.08
        repeat
    contains:
        "back/desert_tanks.jpg"
        alpha 0.5
        linear 2 zoom 1.011
        linear 13 zoom 1.001
        repeat
    contains:
        "back/desert_tanks.jpg"
        alpha 0.4
        linear 7 zoom 1.05
        linear 6 zoom 1.001
        alpha 0.3
        repeat
    contains:
        "back/desert_tanks.jpg"
        alpha 0.6
        linear 3 zoom 0.997
        linear 2 zoom 1
        repeat
    contains:
        alpha 0.5
        "back/desert_tanks.jpg" with hpunch
        0.01
        "back/desert_tanks.jpg" with vpunch
        0.1
        "back/desert_tanks.jpg" with hpunch
        0.05
        "back/desert_tanks.jpg" with hpunch
        0.1
        "back/desert_tanks.jpg" with hpunch
        linear 0.5 alpha 0
        15.0
        repeat

#####################################################################################################################################################
###  EVENT CGs
#####################################################################################################################################################
init:
    $ thumbnail_x = 400
    $ thumbnail_y = 225
    
    image cg_yamato:
        contains:
            "cg/cg_yamato.jpg"
            yalign 1.0
            linear 7.0 yalign 0.01
            
    image cg_yamato2:
        contains:
            "cg/cg_yamato2.jpg"
            yalign 1.0
            linear 7.0 yalign 0.01
            
    image cg_yamato_still:
        contains:
            "cg/cg_yamato.jpg"
            yalign 0.01
    
    image cg_hitora1_1 = "cg/cg_hitora1_1.jpg"
    image cg_hitora1_2 = "cg/cg_hitora1_2.jpg"
    image cg_hitora1_3 = "cg/cg_hitora1_3.jpg"
    image cg_hitora2:
        contains:
            "cg/cg_hitora2.jpg"
            xalign 0.3
            yalign 1.0
            linear 7.0 xalign 0.6 yalign 0.6
    image cg_hitora3:
        contains:
            "cg/cg_hitora3.jpg"
            xalign 0.3
            yalign 1.0
            linear 7.0 xalign 0.6 yalign 0.6
    image cg_hitora4 = "cg/cg_hitora4.jpg"
    image cg_hitora5_1 = "cg/cg_hitora5_1.jpg"
    image cg_hitora5_2 = "cg/cg_hitora5_2.jpg"
    image cg_hitora6_1 = "cg/cg_hitora6_1.jpg"
    image cg_hitora6_2 = "cg/cg_hitora6_2.jpg"
    image cg_hitora6_2_sepia = im.Sepia(im.MatrixColor("cg/cg_hitora6_2.jpg", im.matrix.brightness(0.3) * im.matrix.tint(1, 1, 1)))
            
    image cg_cyrano1 = "cg/cg_cyrano1.jpg"
    image cg_cyrano2_1:
        contains:
            "cg/cg_cyrano2_1.jpg"
            xalign 0.6
            yalign 1.0
            linear 7.0 xalign 0.3 yalign 0.4
    image cg_cyrano2_2:
        contains:
            "cg/cg_cyrano2_2.jpg"
            xalign 0.6
            yalign 1.0
            linear 7.0 xalign 0.3 yalign 0.4
    image cg_cyrano2_3:
        contains:
            "cg/cg_cyrano2_3.jpg"
            xalign 0.6
            yalign 1.0
            linear 7.0 xalign 0.3 yalign 0.4
    image cg_cyrano3 = "cg/cg_cyrano3.jpg"
        
    image cg_churchill1 = "cg/cg_churchill1.jpg"
    image cg_churchill1_sepia = im.Sepia(im.MatrixColor("cg/cg_churchill1.jpg", im.matrix.brightness(0.3) * im.matrix.tint(1, 1, 1)))
    image cg_churchill2:
        contains:
            "cg/cg_churchill2.jpg"
            xalign 0.6
            yalign 1.0
            linear 7.0 xalign 0.3 yalign 0.3
    image cg_churchill3 = "cg/cg_churchill3.jpg"
    
    image cg_starin1_1 = "cg/cg_starin1_1.jpg"
    image cg_starin1_2 = "cg/cg_starin1_2.jpg"
    image cg_starin1_3 = "cg/cg_starin1_3.jpg"
    image cg_starin1_4 = "cg/cg_starin1_4.jpg"
    image cg_starin1_5 = "cg/cg_starin1_5.jpg"
    image cg_starin1_6:
        contains:
            "cg_starin1_3"
        contains:
            "cg_starin1_4"
            alpha 0.3
            linear 0.5 alpha 1.0
            linear 0.5 alpha 0.3
            repeat
            
    image cg_starin2:
        contains:
            "cg/cg_starin2.jpg"
            xalign 0.6
            yalign 1.0
            linear 7.0 xalign 0.3 yalign 0.4
    
    image cg_starin3 = "cg/cg_starin3.jpg"
    
    image cg_starin4_1:
        contains:
            "cg/cg_starin4_1.jpg"
            xalign 0.6
            yalign 1.0
            linear 7.0 xalign 0.3 yalign 0.4
        
    image cg_starin4_2:
        contains:
            "cg/cg_starin4_1.jpg"
            xalign 0.5
            yalign 0.4
        contains:
            "cg/cg_starin4_1.jpg"
            xalign 0.4
            yalign 0.4
            parallel:
                alpha 0.4
                linear 1.5 alpha 0.3
                linear 1.5 alpha 0.4
                repeat
            parallel:
                xzoom 0.97
                linear 1.0 xzoom 1.1
                linear 1.0 xzoom 0.97
                repeat
    
    image cg_rinni1:
        contains:
            "cg/cg_rinni1.jpg"
            xalign 0.3
            yalign 1.0
            linear 7.0 xalign 0.6 yalign 0.4
        
    image cg_rinni2:
        contains:
            "cg/cg_rinni2.jpg"
            xalign 0.3
            yalign 1.0                       
            linear 7.0 xalign 0.6 yalign 0.4
        
    image cg_joebbels:
        contains:
            "cg/cg_joebbels.jpg"
            xalign 0.6
            yalign 1.0
            linear 7.0 xalign 0.3 yalign 0.4
        
    image cg_smigly:
        contains:
            "cg/cg_smigly.jpg"
            xalign 0.3
            yalign 1.0
            linear 7.0 xalign 0.6 yalign 0.4
        
    image cg_mannerheim:
        contains:
            "cg/cg_mannerheim.jpg"
            xalign 0.3
            yalign 1.0
            linear 7.0 xalign 0.6 yalign 0.4
        
    image cg_antoness:
        contains:
            "cg/cg_antoness.jpg"
            xalign 0.3
            yalign 1.0
            linear 7.0 xalign 0.6 yalign 0.4
        
    image cg_roijean:
        contains:
            "cg/cg_roijean.jpg"
            xalign 0.3
            yalign 1.0
            linear 7.0 xalign 0.6 yalign 0.4
        
    image cg_manstein:
        contains:
            "cg/cg_manstein.jpg"
            xalign 0.3
            yalign 1.0
            linear 7.0 xalign 0.7 yalign 0.2
        
    image cg_messe:
        contains:
            "cg/cg_messe.jpg"
            xalign 0.3
            yalign 1.0
            linear 7.0 xalign 0.6 yalign 0.4
        
    image cg_goring:
        contains:
            "cg/cg_goring.jpg"
            xalign 0.3
            yalign 1.0
            linear 7.0 xalign 0.6 yalign 0.4
        
    image cg_rommel1 = "cg/cg_rommel1.jpg"
    
    image cg_rommel2_1:
        contains:
            "cg/cg_rommel2_1.jpg"
            xalign 0.3
            yalign 1.0
            linear 7.0 xalign 0.6 yalign 0.4
            
    image cg_rommel2_2:
        contains:
            "cg/cg_rommel2_2.jpg"
            xalign 0.3
            yalign 1.0
            linear 7.0 xalign 0.6 yalign 0.4
            
    image cg_monty:
        contains:
            "cg/cg_monty.jpg"
            xalign 0.5
            yalign 1.0
            linear 7.0 yalign 0.4
        
    image cg_badoglio:
        contains:
            "cg/cg_badoglio.jpg"
            xalign 0.3
            yalign 1.0
            linear 7.0 xalign 0.6 yalign 0.4
        
    image cg_redgeneralissima:
        contains:
            "cg/cg_redgeneralissima.jpg"
            xalign 0.5
            yalign 1.0
            linear 2.4 yalign 0.3
    
    image cg_scarletrevolution:
        contains:
            "cg/cg_scarletrevolution.jpg"
            xalign 0.5
            yalign 1.0
            linear 2.4 yalign 0.3
        
    image cg_nyan:
        contains:
            "cg/cg_nyan.jpg"
            xalign 0.6
            yalign 1.0
            linear 7.0 xalign 0.3 yalign 0.4
            
    image cg_nyan_focus:
        contains:
            "cg/cg_nyan.jpg"
            xalign 0.3 
            yalign 0.4
        
    image cg_tito:
        contains:
            "cg/cg_tito.jpg"
            xalign 0.3
            yalign 1.0
            linear 7.0 xalign 0.6 yalign 0.4
    
    image cg_graziani:
        contains:
            "cg/cg_graziani.jpg"
            xalign 0.6
            yalign 1.0
            linear 7.0 xalign 0.3 yalign 0.4
        
    image cg_battenia:
        contains:
            "cg/cg_battenia.jpg"
            xalign 0.6
            yalign 1.0
            linear 7.0 xalign 0.3 yalign 0.4
            
    image cg_negahitora:
        contains:
            "cg/cg_negahitora.jpg"
            xalign 0.6
            yalign 1.0
            linear 7.0 xalign 0.3 yalign 0.4
        
    image cg_molotov:
        contains:
            "cg/cg_molotov.jpg"
            xalign 0.6
            yalign 1.0
            linear 7.0 xalign 0.3 yalign 0.2
        
    image cg_stuffy:
        contains:
            "cg/cg_stuffy.jpg"
            xalign 0.6
            yalign 1.0
            linear 7.0 xalign 0.3 yalign 0.4
        
    image cg_dunitz:
        contains:
            "cg/cg_dunitz.jpg"
            xalign 0.6
            yalign 1.0
            linear 7.0 xalign 0.3 yalign 0.4
        
    image cg_vasile:
        contains:
            "cg/cg_vasile.jpg"
            xalign 0.6
            yalign 1.0
            linear 7.0 xalign 0.3 yalign 0.4
        
    image cg_horthy:
        contains:
            "cg/cg_horthy.jpg"
            xalign 0.6
            yalign 1.0
            linear 7.0 xalign 0.3 yalign 0.4
        
    image cg_yamamoto:
        contains:
            "cg/cg_yamamoto.jpg"
            xalign 0.3
            yalign 1.0
            linear 7.0 xalign 0.6 yalign 0.4
            
    image cg_birthday:
        contains:
            "cg/cg_birthday.jpg"
            xalign 0.3
            yalign 1.0
            linear 7.0 xalign 0.6 yalign 0.6
            
    image cg_panzer:
        contains:
            "cg/cg_panzer.jpg"
            yalign 1.0
            linear 7.0 yalign 0.4
            
    image cg_panzer2:
        contains:
            "cg/cg_panzer2.jpg"
            yalign 1.0
            linear 7.0 yalign 0.4
        
    image cg_ending1:
        contains:
            "cg/cg_ending1.jpg"
            xalign 0.5
            yalign 1.0
            linear 7.5 yalign 0.2
        
    image cg_ending2 = "cg/cg_ending2.jpg"
    image cg_ending3 = "cg/cg_ending3.jpg"
    image cg_ending4 = "cg/cg_ending4.jpg"
        
    image cg_hirahita = "cg/cg_hirahita.jpg"
    image cg_guderian = "cg/cg_guderian.jpg"
    image cg_polix = "cg/cg_polix.jpg"
    image cg_barbarossa1_1 = "cg/cg_barbarossa1_1.jpg"
    image cg_barbarossa1_2 = "cg/cg_barbarossa1_2.jpg"
    image cg_barbarossa1_3 = "cg/cg_barbarossa1_3.jpg"
    image cg_zhukky = "cg/cg_zhukky.jpg"
    image cg_worldwar = "cg/cg_worldwar.jpg"
    image cg_totalwar = "cg/cg_totalwar.jpg"
    image cg_franzodefeated = "cg/cg_franzodefeated.jpg"
    image cg_greciadefeated = "cg/cg_greciadefeated.jpg"
    image cg_beach = "cg/cg_beach.jpg"
    image cg_onsen:
        contains:
            "cg/cg_onsen.jpg"
        contains:
            "snowlight"
    image cg_soldiers = "cg/cg_soldiers.jpg"
    image cg_bismarck = "cg/cg_bismarck.jpg"
    image cg_spitfire = "cg/cg_spitfire.jpg"
    image cg_junker = "cg/cg_junker.jpg"
    image cg_uboat = "cg/cg_uboat.jpg"
    image cg_posters = "cg/cg_posters.jpg"
    
#####################################################################################################################################################
### OBJECTS
#####################################################################################################################################################
image object_folder = "character/object/object_folder.png"
image object_art_bad = "character/object/object_art_bad.png"
image object_art_good = "character/object/object_art_good.png"
image object_books = "character/object/object_books.png"
image object_enigma = "character/object/object_enigma.png"
image object_palace = "character/object/object_palace.png"
image object_purple = "character/object/object_purple.png"
image object_purple_sepia = im.Sepia("character/object/object_purple.png")
image object_gramophone = "character/object/object_gramophone.png"
image object_bear = "character/object/object_bear.png"
image object_himmora = "character/object/object_himmora.png"
image object_serpana = "character/object/object_serpana.png"
image object_gamelin = "character/object/object_gamelin.png"
image object_chambers = "character/object/object_chambers.png"
image object_starin = "character/object/object_starin.png"
image object_smigly = "character/object/object_smigly.png"
image object_rinni = "character/object/object_rinni.png"
image object_blondi = "character/object/object_blondi.png"
image object_samovar = "character/object/object_samovar.png"
image object_newspaper = "character/object/object_newspaper.png"
image object_tabloid = "character/object/object_tabloid.png"
image object_bookburning = "character/object/object_bookburning.png"
image object_slums = "character/object/object_slums.png"
image object_pinball = "character/object/object_pinball.png"
image object_marching = "character/object/object_marching.png"
image object_address = "character/object/object_address.png"
image object_letter = "character/object/object_letter.png"
image object_envelope = "character/object/object_envelope.png"
image object_banners = "character/object/object_banners.png"
image object_axlealliance = "character/object/object_axlealliance.png"
image object_wintertimewar = "character/object/object_wintertimewar.png"
image object_explosive = "character/object/object_explosive.png"
image object_plan = "character/object/object_plan.png"
image object_vitaliangirls = "character/object/object_vitaliangirls.png"
image object_zidiparrani = "character/object/object_zidiparrani.png"
image object_kiinyaa = "character/object/object_kiinyaa.png"
image object_yamatodoll = "character/object/object_yamatodoll.png"
image object_autocarro = "character/object/object_autocarro.png"
image object_kabon = "character/object/object_kabon.png"
image object_lutetia = "character/object/object_lutetia.png"
image object_tiddylitovsk = "character/object/object_tiddylitovsk.png"
image object_afrikaakorps = "character/object/object_afrikaakorps.png"
image object_dianxia = "character/object/object_dianxia.png"
image object_wukou = "character/object/object_wukou.png"
image object_tobrunsk = "character/object/object_tobrunsk.png"
image object_kaptara = "character/object/object_kaptara.png"
image object_deserttanks = "character/object/object_deserttanks.png"
image object_rumanum = "character/object/object_rumanum.png"
image object_azadala = "character/object/object_azadala.png"
image object_levantcrisis = "character/object/object_levantcrisis.png"
image object_edooh = "character/object/object_edooh.png"
image object_shenzhenga = "character/object/object_shenzhenga.png"
image object_dustbowl = "character/object/object_dustbowl.png"
image object_reichsfire = "character/object/object_reichsfire.png"
image object_marchonrome = "character/object/object_marchonrome.png"
image object_wallstreet = "character/object/object_wallstreet.png"
image object_carrier = "character/object/object_carrier.png"
image object_steamer = "character/object/object_steamer.png"
image object_samurai = "character/object/object_samurai.png"
image object_occupation = "character/object/object_occupation.png"
image object_edoohpalace = "character/object/object_edoohpalace.png"
image object_exchange = "character/object/object_exchange.png"
image object_transferorder = "character/object/object_transferorder.png"
image object_polixinvasion = "character/object/object_polixinvasion.png"
image object_polixarmy = "character/object/object_polixarmy.png"
image object_varsaabattle = "character/object/object_varsaabattle.png"
image object_pow = "character/object/object_pow.png"
image object_polixcounterattack = "character/object/object_polixcounterattack.png"
image object_generalplan = "character/object/object_generalplan.png"
image object_redarmy = "character/object/object_redarmy.png"
image object_nordaship = "character/object/object_nordaship.png"
image object_knarravik = "character/object/object_knarravik.png"
image object_sunknavy = "character/object/object_sunknavy.png"
image object_nordabattle = "character/object/object_nordabattle.png"
image object_nordainvasion = "character/object/object_nordainvasion.png"
image object_oxloa = "character/object/object_oxloa.png"
image object_skilift = "character/object/object_skilift.png"
image object_mountain = "character/object/object_mountain.png"
image object_wiart = "character/object/object_wiart.png"
image object_amerikansea = "character/object/object_amerikansea.png"
image object_nordaretreat = "character/object/object_nordaretreat.png"
image object_ruftwaffe = "character/object/object_ruftwaffe.png"
image object_fortebin = "character/object/object_fortebin.png"
image object_xrebbeline = "character/object/object_xrebbeline.png"
image object_bataviabridges = "character/object/object_bataviabridges.png"
image object_rotte = "character/object/object_rotte.png"
image object_zeetopia = "character/object/object_zeetopia.png"
image object_belgae = "character/object/object_belgae.png"
image object_belgaeinvasion = "character/object/object_belgaeinvasion.png"
image object_paddle = "character/object/object_paddle.png"
image object_beef = "character/object/object_beef.png"
image object_dyelplan = "character/object/object_dyelplan.png"
image object_mintkornetto = "character/object/object_mintkornetto.png"
image object_billotteironside = "character/object/object_billotteironside.png"
image object_civilians = "character/object/object_civilians.png"
image object_alliancepush = "character/object/object_alliancepush.png"
image object_battle1 = "character/object/object_battle1.png"
image object_battle2 = "character/object/object_battle2.png"
image object_battle3 = "character/object/object_battle3.png"
image object_battle4 = "character/object/object_battle4.png"
image object_battle5 = "character/object/object_battle5.png"
image object_battle6 = "character/object/object_battle6.png"
image object_rivercrossing = "character/object/object_rivercrossing.png"
image object_canal = "character/object/object_canal.png"
image object_tankinvasion = "character/object/object_tankinvasion.png"
image object_ardennen = "character/object/object_ardennen.png"
image object_bononia = "character/object/object_bononia.png"
image object_dunkirch = "character/object/object_dunkirch.png"
image object_equipment = "character/object/object_equipment.png"
image object_shopfront = "character/object/object_shopfront.png"
image object_tornado = "character/object/object_tornado.png"
image object_fortkaputz = "character/object/object_fortkaputz.png"
image object_zuescanal = "character/object/object_zuescanal.png"
image object_battleofbritannia = "character/object/object_battleofbritannia.png"
image object_albionbombing = "character/object/object_albionbombing.png"
image object_epirus = "character/object/object_epirus.png"
image object_burninghouse = "character/object/object_burninghouse.png"
image object_desertbritannia = "character/object/object_desertbritannia.png"
image object_franzolibre = "character/object/object_franzolibre.png"
image object_vitalianprisoners = "character/object/object_vitalianprisoners.png"
image object_klisurapass = "character/object/object_klisurapass.png"
image object_vitalianreinforcements = "character/object/object_vitalianreinforcements.png"
image object_serpanacoup = "character/object/object_serpanacoup.png"
image object_vitalianretreat = "character/object/object_vitalianretreat.png"
image object_singidunbombed = "character/object/object_singidunbombed.png"
image object_serpanainvasion = "character/object/object_serpanainvasion.png"
image object_sunflower = "character/object/object_sunflower.png"
image object_vrhbosna = "character/object/object_vrhbosna.png"
image object_serpanadefeated = "character/object/object_serpanadefeated.png"
image object_thermomalis = "character/object/object_thermomalis.png"
image object_greciainvasion = "character/object/object_greciainvasion.png"
image object_grecianretreat = "character/object/object_grecianretreat.png"
image object_kaptaradefenses = "character/object/object_kaptaradefenses.png"
image object_kaptararetreat = "character/object/object_kaptararetreat.png"
image object_irajiairbattle = "character/object/object_irajiairbattle.png"
image object_irajivictory = "character/object/object_irajivictory.png"
image object_assyriacampaign = "character/object/object_assyriacampaign.png"
image object_berghof = "character/object/object_berghof.png"
image object_barbaraann = "character/object/object_barbaraann.png"
image object_sovianpush = "character/object/object_sovianpush.png"
image object_sovianinvasion = "character/object/object_sovianinvasion.png"
image object_sovianaircraft = "character/object/object_sovianaircraft.png"
image object_rumanumriver = "character/object/object_rumanumriver.png"
image object_sovianfightback = "character/object/object_sovianfightback.png"
image object_soviantrenches = "character/object/object_soviantrenches.png"
image object_haltorder = "character/object/object_haltorder.png"
image object_brody = "character/object/object_brody.png"
image object_reningrada = "character/object/object_reningrada.png"
image object_starinline = "character/object/object_starinline.png"
image object_continuancewar = "character/object/object_continuancewar.png"
image object_mud = "character/object/object_mud.png"
image object_khiava = "character/object/object_khiava.png"
image object_finbard = "character/object/object_finbard.png"
image object_moskva = "character/object/object_moskva.png"
image object_siege = "character/object/object_siege.png"
image object_clamharbor = "character/object/object_clamharbor.png"
image object_kharkova = "character/object/object_kharkova.png"
image object_winter = "character/object/object_winter.png"
image object_berlinbattle = "character/object/object_berlinbattle.png"
image object_stalingrad = "character/object/object_stalingrad.png"
image object_zhinarubble = "character/object/object_zhinarubble.png"
image object_ktttroops = "character/object/object_ktttroops.png"
image object_templerush = "character/object/object_templerush.png"
image object_legion = "character/object/object_legion.png"

image historyslideshow:
    contains:
        "object_wallstreet"
        alpha 0 zoom 0.4 xalign 0.7 yalign 0.5 xanchor 0.5 yanchor 0.5
        pause 4.0
        linear 2.5 zoom 0.6 alpha 0.3
        linear 2.5 zoom 0.8 alpha 0
    contains:
        "object_dustbowl"
        alpha 0 zoom 0.4 xalign 0.3 yalign 0.7 xanchor 0.5 yanchor 0.5
        pause 6.5
        linear 2.5 zoom 0.6 alpha 0.3
        linear 2.5 zoom 0.8 alpha 0
    contains:
        "object_marchonrome"
        alpha 0 zoom 0.4 xalign 0.7 yalign 0.3 xanchor 0.5 yanchor 0.5
        pause 9.0
        linear 2.5 zoom 0.6 alpha 0.3
        linear 2.5 zoom 0.8 alpha 0
    contains:
        "object_marching"
        alpha 0 zoom 0.4 xalign 0.3 yalign 0.4 xanchor 0.5 yanchor 0.5
        pause 11.5
        linear 2.5 zoom 0.6 alpha 0.3
        linear 2.5 zoom 0.8 alpha 0
    contains:
        "object_reichsfire"
        alpha 0 zoom 0.4 xalign 0.8 yalign 0.5 xanchor 0.5 yanchor 0.5
        pause 14.0
        linear 2.5 zoom 0.6 alpha 0.3
        linear 2.5 zoom 0.8 alpha 0
    contains:
        "object_bookburning"
        alpha 0 zoom 0.4 xalign 0.3 yalign 0.3 xanchor 0.5 yanchor 0.5
        pause 16.5
        linear 2.5 zoom 0.6 alpha 0.3
        linear 2.5 zoom 0.8 alpha 0
    contains:
        "object_dianxia"
        alpha 0 zoom 0.4 xalign 0.6 yalign 0.7 xanchor 0.5 yanchor 0.5
        pause 19.0
        linear 2.5 zoom 0.6 alpha 0.3
        linear 2.5 zoom 0.8 alpha 0
        

image object_tutorial1 = "character/object/object_tutorial1.png"
image object_tutorial2 = "character/object/object_tutorial2.png"
image object_tutorial3 = "character/object/object_tutorial3.png"
image object_tutorial4 = "character/object/object_tutorial4.png"
image object_tutorial5 = "character/object/object_tutorial5.png"
image object_tutorial6 = "character/object/object_tutorial6.png"
image object_tutorial7 = "character/object/object_tutorial7.png"
image object_tutorial8 = "character/object/object_tutorial8.png"

image architecture_gallery = "character/object/architecture_gallery.png"
image architecture_bridge = "character/object/architecture_bridge.png"
image architecture_moskva = "character/object/architecture_moskva.png"

image plane_a6mzero = "character/object/plane_a6mzero.png"
image plane_fw200condor = "character/object/plane_fw200condor.png"
image plane_wellington = "character/object/plane_wellington.png"

image tank_panzer1 = "character/object/tank_panzer1.png"
image tank_panzer2 = "character/object/tank_panzer2.png"
image tank_panzer3 = "character/object/tank_panzer3.png"
image tank_panzer4 = "character/object/tank_panzer4.png"
image tank_panzerjager1 = "character/object/tank_panzerjager1.png"
image tank_cv35 = "character/object/tank_cv35.png"
image tank_bt42 = "character/object/tank_bt42.png"
image tank_somuas35 = "character/object/tank_somuas35.png"
image tank_amr35 = "character/object/tank_amr35.png"
image tank_hotchkissh35 = "character/object/tank_hotchkissh35.png"
image tank_schwerergustav = "character/object/tank_schwerergustav.png"
image tank_kruppk5 = "character/object/tank_kruppk5.png"
image tank_karlgerat = "character/object/tank_karlgerat.png"
image tank_kv2 = "character/object/tank_kv2.png"
image tank_cruisermki = "character/object/tank_cruisermki.png"
image tank_crusaderpziv = "character/object/tank_crusaderpziv.png"
image tank_covenanter = "character/object/tank_covenanter.png"
image tank_churchill = "character/object/tank_churchill.png"
image tank_matildai = "character/object/tank_matildai.png"
image tank_matildaii = "character/object/tank_matildaii.png"
image tank_maus = "character/object/tank_maus.png"
image tank_sturmgeschutz3 = "character/object/tank_sturmgeschutz3.png"
image tank_kugelpanzer = "character/object/tank_kugelpanzer.png"
image tank_marder = "character/object/tank_marder.png"
image tank_tks = "character/object/tank_tks.png"
image tank_t35 = "character/object/tank_t35.png"
image tank_7tp = "character/object/tank_7tp.png"
image tank_jagdpanzer = "character/object/tank_jagdpanzer.png"
image tank_bishopsph = "character/object/tank_bishopsph.png"

image ship_courageous = "character/object/ship_courageous.png"
image ship_arkroyal = "character/object/ship_arkroyal.png"
image ship_calabria = "character/object/ship_calabria.png"
image ship_grafspee = "character/object/ship_grafspee.png"
image ship_marine = "character/object/ship_marine.png"
image ship_renown = "character/object/ship_renown.png"

image swimsuit_fukuryu = "character/object/swimsuit_fukuryu.png"
image swimsuit_onepiece = "character/object/swimsuit_onepiece.png"
image swimsuit_uominirana = "character/object/swimsuit_uominirana.png"
image swimsuit_variety = "character/object/swimsuit_variety.png"

image weapon_scr536 = "character/object/weapon_scr536.png"

