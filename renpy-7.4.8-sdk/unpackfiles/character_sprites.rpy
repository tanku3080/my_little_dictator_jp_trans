#----------------------------------------------------------------------------------------------------------------------------------------------------------
###CHARACTERS
#----------------------------------------------------------------------------------------------------------------------------------------------------------
########################################################
# Expressions ############################################
########################################################
image ellipses_bubble = At("character/expressions/ellipses_bubble.png", sidetoside_anim)
image music_note = At("character/expressions/music_note.png", sidetoside_anim)
image hirahita_crown = At("character/expressions/hirahita_crown.png", crown_anim)
image hitora_crown = At("character/expressions/hitora_crown.png", crown_anim)
image roosevelt_crown = At("character/expressions/roosevelt_crown.png", crown_anim)
image rinni_crown = At("character/expressions/rinni_crown.png", crown_anim)
image churchill_crown = At("character/expressions/churchill_crown.png", crown_anim)
image roijean_crown = At("character/expressions/roijean_crown.png", crown_anim)
image rinni_bubble = At("character/expressions/question_bubble.png", questionbubble_anim)
image rommel_exclamation = At("character/expressions/rommel_exclamation.png", crown_anim)
image crowd = "character/special/crowd1.png"

########################################################
# Hitora #################################################
########################################################
image hitora hat angry = LiveComposite(
    (720, 1009),
    (0, 0), "character/hitora/hitora_base1.png",
    (0, 0), "character/hitora/hitora_angry1.png")

image hitora hat cry = LiveComposite(
    (720, 1009),
    (0, 0), "character/hitora/hitora_base2.png",
    (0, 0), "character/hitora/hitora_cry1.png")

image hitora hat happy = LiveComposite(
    (720, 1009),
    (0, 0), "character/hitora/hitora_base2.png",
    (0, 0), "character/hitora/hitora_happy1.png")

image hitora hat normal = LiveComposite(
    (720, 1009),
    (0, 0), "character/hitora/hitora_base2.png",
    (0, 0), "character/hitora/hitora_normal1.png")

image hitora hat moe1 = LiveComposite(
    (720, 1009),
    (0, 0), "character/hitora/hitora_base2.png",
    (0, 0), "character/hitora/hitora_moe11.png")

image hitora hat moe2 = LiveComposite(
    (720, 1009),
    (0, 0), "character/hitora/hitora_base2.png",
    (0, 0), "character/hitora/hitora_moe21.png")

image hitora hat moe3 = LiveComposite(
    (720, 1009),
    (0, 0), "character/hitora/hitora_base1.png",
    (0, 0), "character/hitora/hitora_moe31.png",
    (113, 131), "hitora_crown")

image hitora hat moe4 = LiveComposite(
    (720, 1009),
    (0, 0), "character/hitora/hitora_base2.png",
    (0, 0), "character/hitora/hitora_moe41.png",
    (100, 80), "music_note")

image hitora hat embarrassed = LiveComposite(
    (720, 1009),
    (0, 0), "character/hitora/hitora_base2.png",
    (0, 0), "character/hitora/hitora_embarrassed1.png")

image hitora hat worry = LiveComposite(
    (720, 1009),
    (0, 0), "character/hitora/hitora_base2.png",
    (0, 0), "character/hitora/hitora_worry1.png")

image hitora nohat angry = LiveComposite(
    (720, 1009),
    (0, 0), "character/hitora/hitora_base2.png",
    (0, 0), "character/hitora/hitora_angry2.png")

image hitora nohat cry = LiveComposite(
    (720, 1009),
    (0, 0), "character/hitora/hitora_base1.png",
    (0, 0), "character/hitora/hitora_cry2.png")

image hitora nohat happy = LiveComposite(
    (720, 1009),
    (0, 0), "character/hitora/hitora_base1.png",
    (0, 0), "character/hitora/hitora_happy2.png")

image hitora nohat normal = LiveComposite(
    (720, 1009),
    (0, 0), "character/hitora/hitora_base1.png",
    (0, 0), "character/hitora/hitora_normal2.png")

image hitora nohat moe1 = LiveComposite(
    (720, 1009),
    (0, 0), "character/hitora/hitora_base1.png",
    (0, 0), "character/hitora/hitora_moe12.png")

image hitora nohat moe2 = LiveComposite(
    (720, 1009),
    (0, 0), "character/hitora/hitora_base1.png",
    (0, 0), "character/hitora/hitora_moe22.png")

image hitora nohat moe3 = LiveComposite(
    (720, 1009),
    (0, 0), "character/hitora/hitora_base2.png",
    (0, 0), "character/hitora/hitora_moe32.png",
    (113, 131), "hitora_crown")

image hitora nohat moe4 = LiveComposite(
    (720, 1009),
    (0, 0), "character/hitora/hitora_base1.png",
    (0, 0), "character/hitora/hitora_moe42.png",
    (100, 80), "music_note")

image hitora nohat embarrassed = LiveComposite(
    (720, 1009),
    (0, 0), "character/hitora/hitora_base1.png",
    (0, 0), "character/hitora/hitora_embarrassed2.png")

image hitora nohat worry = LiveComposite(
    (720, 1009),
    (0, 0), "character/hitora/hitora_base1.png",
    (0, 0), "character/hitora/hitora_worry2.png")

image hitora swimsuit angry = LiveComposite(
    (720, 1009),
    (0, 0), "character/hitora/hitora_swimsuit_base2.png",
    (0, 0), "character/hitora/hitora_angry2.png")

image hitora swimsuit cry = LiveComposite(
    (720, 1009),
    (0, 0), "character/hitora/hitora_swimsuit_base1.png",
    (0, 0), "character/hitora/hitora_cry2.png")

image hitora swimsuit happy = LiveComposite(
    (720, 1009),
    (0, 0), "character/hitora/hitora_swimsuit_base1.png",
    (0, 0), "character/hitora/hitora_happy2.png")

image hitora swimsuit normal = LiveComposite(
    (720, 1009),
    (0, 0), "character/hitora/hitora_swimsuit_base1.png",
    (0, 0), "character/hitora/hitora_normal2.png")

image hitora swimsuit moe1 = LiveComposite(
    (720, 1009),
    (0, 0), "character/hitora/hitora_swimsuit_base1.png",
    (0, 0), "character/hitora/hitora_moe12.png")

image hitora swimsuit moe2 = LiveComposite(
    (720, 1009),
    (0, 0), "character/hitora/hitora_swimsuit_base1.png",
    (0, 0), "character/hitora/hitora_moe22.png")

image hitora swimsuit moe3 = LiveComposite(
    (720, 1009),
    (0, 0), "character/hitora/hitora_swimsuit_base2.png",
    (0, 0), "character/hitora/hitora_moe32.png",
    (113, 131), "hitora_crown")

image hitora swimsuit moe4 = LiveComposite(
    (720, 1009),
    (0, 0), "character/hitora/hitora_swimsuit_base1.png",
    (0, 0), "character/hitora/hitora_moe42.png",
    (100, 80), "music_note")

image hitora swimsuit embarrassed = LiveComposite(
    (720, 1009),
    (0, 0), "character/hitora/hitora_swimsuit_base1.png",
    (0, 0), "character/hitora/hitora_embarrassed2.png")

image hitora swimsuit worry = LiveComposite(
    (720, 1009),
    (0, 0), "character/hitora/hitora_swimsuit_base1.png",
    (0, 0), "character/hitora/hitora_worry2.png")

image hitora swimsuit worry3 = LiveComposite(
    (720, 1009),
    (0, 0), "character/hitora/hitora_swimsuit_base1.png",
    (0, 0), "character/hitora/hitora_worry3.png")

image hitora black = LiveComposite(
    (720, 1009),
    (0, 0), silhouetted("character/hitora/hitora_base2.png",0,0,0),
    (0, 0), silhouetted("character/hitora/hitora_normal1.png",0,0,0))
    
image hitora swimsuit fight:
    "hitora swimsuit angry"
    xalign 0.5 yalign 1.0
    linear 0.03 xalign 0.498
    linear 0.03 xalign 0.5
    linear 0.03 xalign 0.502
    linear 0.03 xalign 0.5
    repeat
    
image hitora hat ko:
    contains:
        "hitora hat angry large"
        alpha 0.8
        yalign 1.0
        xalign 0.5
        linear 1.0 xalign 0.55
        linear 2.0 xalign 0.45
        linear 1.0 xalign 0.5
        repeat
    contains:
        "hitora hat angry large"
        alpha .2
        xalign 0.5
        yalign 1.0
        linear 2.0 xalign 0.55
        linear 2.0 xalign 0.6
        linear 2.0 xalign 0.55
        linear 2.0 xalign 0.5
        linear 2.0 xalign 0.45
        linear 2.0 xalign 0.4
        linear 2.0 xalign 0.45
        linear 2.0 xalign 0.5
        repeat
    contains:
        "hitora hat angry large"
        alpha .2
        xalign 0.5
        yalign 1.0
        linear 2.0 xalign 0.45
        linear 2.0 xalign 0.4
        linear 2.0 xalign 0.45
        linear 2.0 xalign 0.5
        linear 2.0 xalign 0.55
        linear 2.0 xalign 0.6
        linear 2.0 xalign 0.55
        linear 2.0 xalign 0.5
        repeat

image negahitora:
    "character/hitora/negahitora.png"
    alpha 1.0
    linear 1.0 alpha 1.5
    linear 1.0 alpha 1.0
    repeat
    
image negahitora shake:
    "character/hitora/negahitora.png"
    xalign 0.5 yalign 1.0
    linear 0.03 xalign 0.498
    linear 0.03 xalign 0.5
    linear 0.03 xalign 0.502
    linear 0.03 xalign 0.5
    repeat

image side negahitora = LiveCrop((240, 175, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/negahitora.png")))
image side negahitora shake = LiveCrop((240, 175, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/negahitora.png")))    

image side hitora hat angry = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_angry1.png")))
image side hitora hat cry = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_cry1.png")))
image side hitora hat normal = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_normal1.png")))
image side hitora hat moe1 = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_moe11.png")))
image side hitora hat moe2 = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_moe21.png")))
image side hitora hat moe3 = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_moe31.png")))
image side hitora hat moe4 = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_moe41.png")))
image side hitora hat embarrassed = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_embarrassed1.png")))
image side hitora hat worry = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_worry1.png")))
image side hitora hat happy = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_happy1.png")))
image side hitora hat ko = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_angry1.png")))
image side hitora hat powers = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_angry1.png")))

image side hitora nohat angry = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_angry2.png")))
image side hitora nohat cry = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_cry2.png")))
image side hitora nohat normal = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_normal2.png")))
image side hitora nohat moe1 = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_moe12.png")))
image side hitora nohat moe2 = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_moe22.png")))
image side hitora nohat moe3 = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_moe32.png")))
image side hitora nohat moe4 = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_moe42.png")))
image side hitora nohat embarrassed = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_embarrassed2.png")))
image side hitora nohat worry = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_worry2.png")))
image side hitora nohat happy = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_happy2.png")))

image side hitora night angry = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_angry1.png")))

image side hitora swimsuit angry = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_swimsuit_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_angry2.png")))
image side hitora swimsuit cry = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_swimsuit_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_cry2.png")))
image side hitora swimsuit normal = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_swimsuit_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_normal2.png")))
image side hitora swimsuit moe1 = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_swimsuit_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_moe12.png")))
image side hitora swimsuit moe2 = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_swimsuit_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_moe22.png")))
image side hitora swimsuit moe3 = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_swimsuit_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_moe32.png")))
image side hitora swimsuit moe4 = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_swimsuit_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_moe42.png")))
image side hitora swimsuit embarrassed = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_swimsuit_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_embarrassed2.png")))
image side hitora swimsuit worry = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_swimsuit_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_worry2.png")))
image side hitora swimsuit worry3 = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_swimsuit_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_worry3.png")))
image side hitora swimsuit happy = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_swimsuit_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_happy2.png")))
image side hitora swimsuit fight = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_angry1.png")))

image side hitora bedroom angry = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_swimsuit_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_angry2.png")))
image side hitora bedroom cry = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_swimsuit_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_cry2.png")))
image side hitora bedroom normal = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_swimsuit_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_normal2.png")))
image side hitora bedroom moe1 = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_swimsuit_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_moe12.png")))
image side hitora bedroom moe2 = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_swimsuit_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_moe22.png")))
image side hitora bedroom moe3 = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_swimsuit_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_moe32.png")))
image side hitora bedroom moe4 = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_swimsuit_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_moe42.png")))
image side hitora bedroom embarrassed = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_swimsuit_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_embarrassed2.png")))
image side hitora bedroom worry = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_swimsuit_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_worry2.png")))
image side hitora bedroom worry3 = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_swimsuit_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_worry3.png")))
image side hitora bedroom happy = LiveCrop((195, 150, 350, 210), LiveComposite((720, 1009), (0, 0), im.Sepia("character/hitora/hitora_swimsuit_base1.png"), (0, 0), im.Sepia("character/hitora/hitora_happy2.png")))

image hitora hat angry large = "character/hitora/hitora_angry1_large.png"
image hitora hat happy large = "character/hitora/hitora_happy1_large.png"
image hitora hat embarrassed large = "character/hitora/hitora_embarrassed1_large.png"
image hitora hat cry large = "character/hitora/hitora_cry1_large.png"
image hitora hat normal large = "character/hitora/hitora_normal1_large.png"
image hitora hat worry large = "character/hitora/hitora_worry1_large.png"
image hitora hat moe1 large = "character/hitora/hitora_moe11_large.png"
image hitora hat moe2 large = "character/hitora/hitora_moe21_large.png"
image hitora hat moe3 large = "character/hitora/hitora_moe31_large.png"
image hitora hat moe4 large = "character/hitora/hitora_moe41_large.png"
image hitora hat powers large = "character/hitora/hitora_powers1_large.png"

image hitora hat powers large fade:
    contains:
        "hitora hat powers large"
        xalign 0.5
    contains:
        "hitora hat powers large"
        xalign 0.5
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
            

image hitora night angry large = im.MatrixColor("character/hitora/hitora_angry1_large.png", im.matrix.brightness(-.2) * im.matrix.tint(0.6, 0.7, 0.9) * im.matrix.saturation(0.7) * im.matrix.contrast(0.8))

image hitora bedroom angry large = im.MatrixColor("character/hitora/hitora_swimsuit_angry1_large.png", im.matrix.brightness(-.2) * im.matrix.tint(0.6, 0.7, 0.9) * im.matrix.saturation(0.7) * im.matrix.contrast(0.8))
image hitora bedroom happy large = im.MatrixColor("character/hitora/hitora_swimsuit_happy1_large.png", im.matrix.brightness(-.2) * im.matrix.tint(0.6, 0.7, 0.9) * im.matrix.saturation(0.7) * im.matrix.contrast(0.8))
image hitora bedroom embarrassed large = im.MatrixColor("character/hitora/hitora_swimsuit_embarrassed1_large.png", im.matrix.brightness(-.2) * im.matrix.tint(0.6, 0.7, 0.9) * im.matrix.saturation(0.7) * im.matrix.contrast(0.8))
image hitora bedroom cry large = im.MatrixColor("character/hitora/hitora_swimsuit_cry1_large.png", im.matrix.brightness(-.2) * im.matrix.tint(0.6, 0.7, 0.9) * im.matrix.saturation(0.7) * im.matrix.contrast(0.8))
image hitora bedroom normal large = im.MatrixColor("character/hitora/hitora_swimsuit_normal1_large.png", im.matrix.brightness(-.2) * im.matrix.tint(0.6, 0.7, 0.9) * im.matrix.saturation(0.7) * im.matrix.contrast(0.8))
image hitora bedroom worry large = im.MatrixColor("character/hitora/hitora_swimsuit_worry1_large.png", im.matrix.brightness(-.2) * im.matrix.tint(0.6, 0.7, 0.9) * im.matrix.saturation(0.7) * im.matrix.contrast(0.8))
image hitora bedroom moe1 large = im.MatrixColor("character/hitora/hitora_swimsuit_moe11_large.png", im.matrix.brightness(-.2) * im.matrix.tint(0.6, 0.7, 0.9) * im.matrix.saturation(0.7) * im.matrix.contrast(0.8))
image hitora bedroom moe2 large = im.MatrixColor("character/hitora/hitora_swimsuit_moe21_large.png", im.matrix.brightness(-.2) * im.matrix.tint(0.6, 0.7, 0.9) * im.matrix.saturation(0.7) * im.matrix.contrast(0.8))
image hitora bedroom moe3 large = im.MatrixColor("character/hitora/hitora_swimsuit_moe31_large.png", im.matrix.brightness(-.2) * im.matrix.tint(0.6, 0.7, 0.9) * im.matrix.saturation(0.7) * im.matrix.contrast(0.8))
image hitora bedroom moe4 large = im.MatrixColor("character/hitora/hitora_swimsuit_moe41_large.png", im.matrix.brightness(-.2) * im.matrix.tint(0.6, 0.7, 0.9) * im.matrix.saturation(0.7) * im.matrix.contrast(0.8))

image hitora swimsuit angry large = "character/hitora/hitora_swimsuit_angry1_large.png"
image hitora swimsuit happy large = "character/hitora/hitora_swimsuit_happy1_large.png"
image hitora swimsuit embarrassed large = "character/hitora/hitora_swimsuit_embarrassed1_large.png"
image hitora swimsuit cry large = "character/hitora/hitora_swimsuit_cry1_large.png"
image hitora swimsuit normal large = "character/hitora/hitora_swimsuit_normal1_large.png"
image hitora swimsuit worry large = "character/hitora/hitora_swimsuit_worry1_large.png"
image hitora swimsuit worry3 large = "character/hitora/hitora_swimsuit_worry3_large.png"
image hitora swimsuit moe1 large = "character/hitora/hitora_swimsuit_moe11_large.png"
image hitora swimsuit moe2 large = "character/hitora/hitora_swimsuit_moe21_large.png"
image hitora swimsuit moe3 large = "character/hitora/hitora_swimsuit_moe31_large.png"
image hitora swimsuit moe4 large = "character/hitora/hitora_swimsuit_moe41_large.png"

########################################################
# Churchill ###############################################
########################################################
image churchill hat determined = LiveComposite(
    (600, 970),
    (0, 0), "character/churchill/churchill_base1.png",
    (0, 0), "character/churchill/churchill_determined1.png")

image churchill hat happy = LiveComposite(
    (600, 970),
    (0, 0), "character/churchill/churchill_base2.png",
    (0, 0), "character/churchill/churchill_happy1.png")

image churchill hat moe1 = LiveComposite(
    (600, 970),
    (0, 0), "character/churchill/churchill_base2.png",
    (0, 0), "character/churchill/churchill_moe11.png")

image churchill hat moe2 = LiveComposite(
    (600, 970),
    (0, 0), "character/churchill/churchill_base2.png",
    (0, 0), "character/churchill/churchill_moe21.png")

image churchill hat moe3 = LiveComposite(
    (600, 970),
    (0, 0), "character/churchill/churchill_base1.png",
    (0, 0), "character/churchill/churchill_moe31.png",
    (94, 74), "churchill_crown")

image churchill hat moe4 = LiveComposite(
    (600, 970),
    (0, 0), "character/churchill/churchill_base2.png",
    (0, 0), "character/churchill/churchill_moe41.png")

image churchill hat normal = LiveComposite(
    (600, 970),
    (0, 0), "character/churchill/churchill_base2.png",
    (0, 0), "character/churchill/churchill_normal1.png")

image churchill hat sad = LiveComposite(
    (600, 970),
    (0, 0), "character/churchill/churchill_base2.png",
    (0, 0), "character/churchill/churchill_sad1.png")

image churchill hat shock = LiveComposite(
    (600, 970),
    (0, 0), "character/churchill/churchill_base2.png",
    (0, 0), "character/churchill/churchill_shock1.png")

image churchill nohat determined = LiveComposite(
    (600, 970),
    (0, 0), "character/churchill/churchill_base1.png",
    (0, 0), "character/churchill/churchill_determined2.png")

image churchill nohat happy = LiveComposite(
    (600, 970),
    (0, 0), "character/churchill/churchill_base2.png",
    (0, 0), "character/churchill/churchill_happy2.png")

image churchill nohat moe1 = LiveComposite(
    (600, 970),
    (0, 0), "character/churchill/churchill_base2.png",
    (0, 0), "character/churchill/churchill_moe12.png")

image churchill nohat moe2 = LiveComposite(
    (600, 970),
    (0, 0), "character/churchill/churchill_base2.png",
    (0, 0), "character/churchill/churchill_moe22.png")

image churchill nohat moe3 = LiveComposite(
    (600, 970),
    (0, 0), "character/churchill/churchill_base1.png",
    (0, 0), "character/churchill/churchill_moe32.png",
    (94, 74), "churchill_crown")

image churchill nohat moe4 = LiveComposite(
    (600, 970),
    (0, 0), "character/churchill/churchill_base2.png",
    (0, 0), "character/churchill/churchill_moe42.png")

image churchill nohat normal = LiveComposite(
    (600, 970),
    (0, 0), "character/churchill/churchill_base2.png",
    (0, 0), "character/churchill/churchill_normal2.png")

image churchill nohat sad = LiveComposite(
    (600, 970),
    (0, 0), "character/churchill/churchill_base2.png",
    (0, 0), "character/churchill/churchill_sad2.png")

image churchill nohat shock = LiveComposite(
    (600, 970),
    (0, 0), "character/churchill/churchill_base2.png",
    (0, 0), "character/churchill/churchill_shock2.png")

image churchill swimsuit determined = LiveComposite(
    (600, 970),
    (0, 0), "character/churchill/churchill_swimsuit_base1.png",
    (0, 0), "character/churchill/churchill_determined2.png")

image churchill swimsuit happy = LiveComposite(
    (600, 970),
    (0, 0), "character/churchill/churchill_swimsuit_base2.png",
    (0, 0), "character/churchill/churchill_happy2.png")

image churchill swimsuit moe1 = LiveComposite(
    (600, 970),
    (0, 0), "character/churchill/churchill_swimsuit_base2.png",
    (0, 0), "character/churchill/churchill_moe12.png")

image churchill swimsuit moe2 = LiveComposite(
    (600, 970),
    (0, 0), "character/churchill/churchill_swimsuit_base2.png",
    (0, 0), "character/churchill/churchill_moe22.png")

image churchill swimsuit moe3 = LiveComposite(
    (600, 970),
    (0, 0), "character/churchill/churchill_swimsuit_base1.png",
    (0, 0), "character/churchill/churchill_moe32.png",
    (94, 74), "churchill_crown")

image churchill swimsuit moe4 = LiveComposite(
    (600, 970),
    (0, 0), "character/churchill/churchill_swimsuit_base2.png",
    (0, 0), "character/churchill/churchill_moe42.png")

image churchill swimsuit normal = LiveComposite(
    (600, 970),
    (0, 0), "character/churchill/churchill_swimsuit_base2.png",
    (0, 0), "character/churchill/churchill_normal2.png")

image churchill swimsuit sad = LiveComposite(
    (600, 970),
    (0, 0), "character/churchill/churchill_swimsuit_base2.png",
    (0, 0), "character/churchill/churchill_sad2.png")

image churchill swimsuit shock = LiveComposite(
    (600, 970),
    (0, 0), "character/churchill/churchill_swimsuit_base2.png",
    (0, 0), "character/churchill/churchill_shock2.png")

image side churchill hat determined = LiveCrop((115, 140, 350, 210), LiveComposite((720, 970), (0, 0), im.Sepia("character/churchill/churchill_base1.png"), (0, 0), im.Sepia("character/churchill/churchill_determined1.png")))
image side churchill hat happy = LiveCrop((115, 140, 350, 210), LiveComposite((720, 970), (0, 0), im.Sepia("character/churchill/churchill_base1.png"), (0, 0), im.Sepia("character/churchill/churchill_happy1.png")))
image side churchill hat moe1 = LiveCrop((115, 140, 350, 210), LiveComposite((720, 970), (0, 0), im.Sepia("character/churchill/churchill_base1.png"), (0, 0), im.Sepia("character/churchill/churchill_moe11.png")))
image side churchill hat moe2 = LiveCrop((115, 140, 350, 210), LiveComposite((720, 970), (0, 0), im.Sepia("character/churchill/churchill_base1.png"), (0, 0), im.Sepia("character/churchill/churchill_moe21.png")))
image side churchill hat moe3 = LiveCrop((115, 140, 350, 210), LiveComposite((720, 970), (0, 0), im.Sepia("character/churchill/churchill_base1.png"), (0, 0), im.Sepia("character/churchill/churchill_moe31.png")))
image side churchill hat moe4 = LiveCrop((115, 140, 350, 210), LiveComposite((720, 970), (0, 0), im.Sepia("character/churchill/churchill_base1.png"), (0, 0), im.Sepia("character/churchill/churchill_moe41.png")))
image side churchill hat normal = LiveCrop((115, 140, 350, 210), LiveComposite((720, 970), (0, 0), im.Sepia("character/churchill/churchill_base1.png"), (0, 0), im.Sepia("character/churchill/churchill_normal1.png")))
image side churchill hat sad = LiveCrop((115, 140, 350, 210), LiveComposite((720, 970), (0, 0), im.Sepia("character/churchill/churchill_base1.png"), (0, 0), im.Sepia("character/churchill/churchill_sad1.png")))
image side churchill hat shock = LiveCrop((115, 140, 350, 210), LiveComposite((720, 970), (0, 0), im.Sepia("character/churchill/churchill_base1.png"), (0, 0), im.Sepia("character/churchill/churchill_shock1.png")))

image side churchill nohat determined = LiveCrop((115, 140, 350, 210), LiveComposite((720, 970), (0, 0), im.Sepia("character/churchill/churchill_base2.png"), (0, 0), im.Sepia("character/churchill/churchill_determined2.png")))
image side churchill nohat happy = LiveCrop((115, 140, 350, 210), LiveComposite((720, 970), (0, 0), im.Sepia("character/churchill/churchill_base2.png"), (0, 0), im.Sepia("character/churchill/churchill_happy2.png")))
image side churchill nohat moe1 = LiveCrop((115, 140, 350, 210), LiveComposite((720, 970), (0, 0), im.Sepia("character/churchill/churchill_base2.png"), (0, 0), im.Sepia("character/churchill/churchill_moe12.png")))
image side churchill nohat moe2 = LiveCrop((115, 140, 350, 210), LiveComposite((720, 970), (0, 0), im.Sepia("character/churchill/churchill_base2.png"), (0, 0), im.Sepia("character/churchill/churchill_moe22.png")))
image side churchill nohat moe3 = LiveCrop((115, 140, 350, 210), LiveComposite((720, 970), (0, 0), im.Sepia("character/churchill/churchill_base2.png"), (0, 0), im.Sepia("character/churchill/churchill_moe32.png")))
image side churchill nohat moe4 = LiveCrop((115, 140, 350, 210), LiveComposite((720, 970), (0, 0), im.Sepia("character/churchill/churchill_base2.png"), (0, 0), im.Sepia("character/churchill/churchill_moe42.png")))
image side churchill nohat normal = LiveCrop((115, 140, 350, 210), LiveComposite((720, 970), (0, 0), im.Sepia("character/churchill/churchill_base2.png"), (0, 0), im.Sepia("character/churchill/churchill_normal2.png")))
image side churchill nohat sad = LiveCrop((115, 140, 350, 210), LiveComposite((720, 970), (0, 0), im.Sepia("character/churchill/churchill_base2.png"), (0, 0), im.Sepia("character/churchill/churchill_sad2.png")))
image side churchill nohat shock = LiveCrop((115, 140, 350, 210), LiveComposite((720, 970), (0, 0), im.Sepia("character/churchill/churchill_base2.png"), (0, 0), im.Sepia("character/churchill/churchill_shock2.png")))

image side churchill swimsuit determined = LiveCrop((115, 140, 350, 210), LiveComposite((720, 970), (0, 0), im.Sepia("character/churchill/churchill_base2.png"), (0, 0), im.Sepia("character/churchill/churchill_determined2.png")))
image side churchill swimsuit happy = LiveCrop((115, 140, 350, 210), LiveComposite((720, 970), (0, 0), im.Sepia("character/churchill/churchill_base2.png"), (0, 0), im.Sepia("character/churchill/churchill_happy2.png")))
image side churchill swimsuit moe1 = LiveCrop((115, 140, 350, 210), LiveComposite((720, 970), (0, 0), im.Sepia("character/churchill/churchill_base2.png"), (0, 0), im.Sepia("character/churchill/churchill_moe12.png")))
image side churchill swimsuit moe2 = LiveCrop((115, 140, 350, 210), LiveComposite((720, 970), (0, 0), im.Sepia("character/churchill/churchill_base2.png"), (0, 0), im.Sepia("character/churchill/churchill_moe22.png")))
image side churchill swimsuit moe3 = LiveCrop((115, 140, 350, 210), LiveComposite((720, 970), (0, 0), im.Sepia("character/churchill/churchill_base2.png"), (0, 0), im.Sepia("character/churchill/churchill_moe32.png")))
image side churchill swimsuit moe4 = LiveCrop((115, 140, 350, 210), LiveComposite((720, 970), (0, 0), im.Sepia("character/churchill/churchill_base2.png"), (0, 0), im.Sepia("character/churchill/churchill_moe42.png")))
image side churchill swimsuit normal = LiveCrop((115, 140, 350, 210), LiveComposite((720, 970), (0, 0), im.Sepia("character/churchill/churchill_base2.png"), (0, 0), im.Sepia("character/churchill/churchill_normal2.png")))
image side churchill swimsuit sad = LiveCrop((115, 140, 350, 210), LiveComposite((720, 970), (0, 0), im.Sepia("character/churchill/churchill_base2.png"), (0, 0), im.Sepia("character/churchill/churchill_sad2.png")))
image side churchill swimsuit shock = LiveCrop((115, 140, 350, 210), LiveComposite((720, 970), (0, 0), im.Sepia("character/churchill/churchill_base2.png"), (0, 0), im.Sepia("character/churchill/churchill_shock2.png")))

image churchill hat determined large = "character/churchill/churchill_determined1_large.png"
image churchill hat happy large = "character/churchill/churchill_happy1_large.png"
image churchill hat sad large = "character/churchill/churchill_sad1_large.png"
image churchill hat normal large = "character/churchill/churchill_normal1_large.png"
image churchill hat shock large = "character/churchill/churchill_shock1_large.png"
image churchill hat moe1 large = "character/churchill/churchill_moe11_large.png"
image churchill hat moe2 large = "character/churchill/churchill_moe21_large.png"
image churchill hat moe3 large = "character/churchill/churchill_moe31_large.png"
image churchill hat moe4 large = "character/churchill/churchill_moe41_large.png"

image churchill swimsuit determined large = "character/churchill/churchill_swimsuit_determined1_large.png"
image churchill swimsuit happy large = "character/churchill/churchill_swimsuit_happy1_large.png"
image churchill swimsuit sad large = "character/churchill/churchill_swimsuit_sad1_large.png"
image churchill swimsuit normal large = "character/churchill/churchill_swimsuit_normal1_large.png"
image churchill swimsuit shock large = "character/churchill/churchill_swimsuit_shock1_large.png"
image churchill swimsuit moe1 large = "character/churchill/churchill_swimsuit_moe11_large.png"
image churchill swimsuit moe2 large = "character/churchill/churchill_swimsuit_moe21_large.png"
image churchill swimsuit moe3 large = "character/churchill/churchill_swimsuit_moe31_large.png"
image churchill swimsuit moe4 large = "character/churchill/churchill_swimsuit_moe41_large.png"

########################################################
# Starin ###############################################
########################################################
image starin hat angry = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base1.png",
    (0, 0), "character/starin/starin_angry1.png")

image starin hat happy = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base1.png",
    (0, 0), "character/starin/starin_happy1.png")

image starin hat insane = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base2.png",
    (0, 0), "character/starin/starin_insane2.png")

image starin hat insane2 = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_insane7.png")

image starin hat insane3 = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_insane7.png")

image starin hat cry = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base1.png",
    (0, 0), "character/starin/starin_cry1.png")

image starin hat normal = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base1.png",
    (0, 0), "character/starin/starin_normal1.png")

image starin hat moe1 = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base1.png",
    (0, 0), "character/starin/starin_moe11.png")

image starin hat moe2 = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base1.png",
    (0, 0), "character/starin/starin_moe21.png")

image starin hat moe3 = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base2.png",
    (0, 0), "character/starin/starin_moe32.png")

image starin hat moe4 = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base1.png",
    (0, 0), "character/starin/starin_moe41.png")


image starin nohat angry = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base1.png",
    (0, 0), "character/starin/starin_angry5.png")

image starin nohat happy = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base1.png",
    (0, 0), "character/starin/starin_happy5.png")

image starin nohat insane = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base2.png",
    (0, 0), "character/starin/starin_insane6.png")

image starin nohat cry = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base1.png",
    (0, 0), "character/starin/starin_cry5.png")

image starin nohat normal = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base1.png",
    (0, 0), "character/starin/starin_normal5.png")

image starin nohat moe1 = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base1.png",
    (0, 0), "character/starin/starin_moe15.png")

image starin nohat moe2 = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base1.png",
    (0, 0), "character/starin/starin_moe25.png")

image starin nohat moe3 = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base2.png",
    (0, 0), "character/starin/starin_moe36.png")

image starin nohat moe4 = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base1.png",
    (0, 0), "character/starin/starin_moe45.png")

image starin fur angry = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base3.png",
    (0, 0), "character/starin/starin_angry3.png")

image starin fur happy = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base3.png",
    (0, 0), "character/starin/starin_happy3.png")

image starin fur insane = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base4.png",
    (0, 0), "character/starin/starin_insane4.png")

image starin fur cry = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base3.png",
    (0, 0), "character/starin/starin_cry3.png")

image starin fur normal = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base3.png",
    (0, 0), "character/starin/starin_normal3.png")

image starin fur moe1 = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base3.png",
    (0, 0), "character/starin/starin_moe13.png")

image starin fur moe2 = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base3.png",
    (0, 0), "character/starin/starin_moe23.png")

image starin fur moe3 = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base4.png",
    (0, 0), "character/starin/starin_moe34.png")

image starin fur moe4 = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base3.png",
    (0, 0), "character/starin/starin_moe43.png")


image starin swimsuit angry = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base5.png",
    (0, 0), "character/starin/starin_angry5.png")

image starin swimsuit happy = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base5.png",
    (0, 0), "character/starin/starin_happy5.png")

image starin swimsuit insane = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base6.png",
    (0, 0), "character/starin/starin_insane6.png")

image starin swimsuit cry = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base5.png",
    (0, 0), "character/starin/starin_cry5.png")

image starin swimsuit normal = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base5.png",
    (0, 0), "character/starin/starin_normal5.png")

image starin swimsuit moe1 = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base5.png",
    (0, 0), "character/starin/starin_moe15.png")

image starin swimsuit moe2 = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base5.png",
    (0, 0), "character/starin/starin_moe25.png")

image starin swimsuit moe3 = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base6.png",
    (0, 0), "character/starin/starin_moe36.png")

image starin swimsuit moe4 = LiveComposite(
    (720, 900),
    (0, 0), "character/starin/starin_base5.png",
    (0, 0), "character/starin/starin_moe45.png")

image side starin hat insane = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base1.png"), (0, 0), im.Sepia("character/starin/starin_insane1.png")))
image side starin hat power = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base1.png"), (0, 0), im.Sepia("character/starin/starin_insane1.png")))
image side starin hat angry = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base1.png"), (0, 0), im.Sepia("character/starin/starin_angry1.png")))
image side starin hat happy = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base1.png"), (0, 0), im.Sepia("character/starin/starin_happy1.png")))
image side starin hat moe1 = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base1.png"), (0, 0), im.Sepia("character/starin/starin_moe11.png")))
image side starin hat moe2 = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base1.png"), (0, 0), im.Sepia("character/starin/starin_moe21.png")))
image side starin hat moe3 = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base1.png"), (0, 0), im.Sepia("character/starin/starin_moe31.png")))
image side starin hat moe4 = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base1.png"), (0, 0), im.Sepia("character/starin/starin_moe41.png")))
image side starin hat normal = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base1.png"), (0, 0), im.Sepia("character/starin/starin_normal1.png")))
image side starin hat cry = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base1.png"), (0, 0), im.Sepia("character/starin/starin_cry1.png")))
image side starin nohat insane = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base1.png"), (0, 0), im.Sepia("character/starin/starin_insane5.png")))
image side starin nohat angry = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base1.png"), (0, 0), im.Sepia("character/starin/starin_angry5.png")))
image side starin nohat happy = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base1.png"), (0, 0), im.Sepia("character/starin/starin_happy5.png")))
image side starin nohat moe1 = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base1.png"), (0, 0), im.Sepia("character/starin/starin_moe15.png")))
image side starin nohat moe2 = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base1.png"), (0, 0), im.Sepia("character/starin/starin_moe25.png")))
image side starin nohat moe3 = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base1.png"), (0, 0), im.Sepia("character/starin/starin_moe35.png")))
image side starin nohat moe4 = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base1.png"), (0, 0), im.Sepia("character/starin/starin_moe45.png")))
image side starin nohat normal = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base1.png"), (0, 0), im.Sepia("character/starin/starin_normal5.png")))
image side starin nohat cry = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base1.png"), (0, 0), im.Sepia("character/starin/starin_cry5.png")))
image side starin fur insane = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base3.png"), (0, 0), im.Sepia("character/starin/starin_insane3.png")))
image side starin fur angry = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base3.png"), (0, 0), im.Sepia("character/starin/starin_angry3.png")))
image side starin fur happy = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base3.png"), (0, 0), im.Sepia("character/starin/starin_happy3.png")))
image side starin fur moe1 = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base3.png"), (0, 0), im.Sepia("character/starin/starin_moe13.png")))
image side starin fur moe2 = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base3.png"), (0, 0), im.Sepia("character/starin/starin_moe23.png")))
image side starin fur moe3 = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base3.png"), (0, 0), im.Sepia("character/starin/starin_moe33.png")))
image side starin fur moe4 = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base3.png"), (0, 0), im.Sepia("character/starin/starin_moe43.png")))
image side starin fur normal = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base3.png"), (0, 0), im.Sepia("character/starin/starin_normal3.png")))
image side starin fur cry = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base3.png"), (0, 0), im.Sepia("character/starin/starin_cry3.png")))
image side starin swimsuit angry = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base1.png"), (0, 0), im.Sepia("character/starin/starin_angry5.png")))
image side starin swimsuit insane = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base1.png"), (0, 0), im.Sepia("character/starin/starin_insane5.png")))
image side starin swimsuit happy = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base1.png"), (0, 0), im.Sepia("character/starin/starin_happy5.png")))
image side starin swimsuit moe1 = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base1.png"), (0, 0), im.Sepia("character/starin/starin_moe15.png")))
image side starin swimsuit moe2 = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base1.png"), (0, 0), im.Sepia("character/starin/starin_moe25.png")))
image side starin swimsuit moe3 = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base1.png"), (0, 0), im.Sepia("character/starin/starin_moe35.png")))
image side starin swimsuit moe4 = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base1.png"), (0, 0), im.Sepia("character/starin/starin_moe45.png")))
image side starin swimsuit normal = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base1.png"), (0, 0), im.Sepia("character/starin/starin_normal5.png")))
image side starin swimsuit cry = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base1.png"), (0, 0), im.Sepia("character/starin/starin_cry5.png")))
image side starin swimsuit fight = LiveCrop((195, 130, 350, 210), LiveComposite((700, 900), (0, 0), im.Sepia("character/starin/starin_base1.png"), (0, 0), im.Sepia("character/starin/starin_angry5.png")))

image starin hat power:
    contains:
        "starin hat insane3"
        xalign 0.5
        yalign 1.0
    contains:
        "starin hat insane2"
        alpha 0
        xalign 0.5
        yalign 1.0
        linear 1.0 alpha 0.5 xzoom 1.15
        linear 1.0 alpha 0 xzoom 1.05
        repeat

image starin swimsuit fight:
    "starin swimsuit angry"
    xalign 0.5 yalign 1.0
    linear 0.03 xalign 0.496
    linear 0.03 xalign 0.504
    linear 0.03 xalign 0.5
    repeat

########################################################
# Zhukky ###############################################
########################################################
image zhukky hat determined = LiveComposite(
    (405, 1010),
    (20, 0), "character/zhukky/zhukky_base1.png",
    (20, 0), "character/zhukky/zhukky_determined1.png")

image zhukky hat angry = LiveComposite(
    (405, 1010),
    (20, 0), "character/zhukky/zhukky_base1.png",
    (20, 0), "character/zhukky/zhukky_angry1.png")

image zhukky hat moe1 = LiveComposite(
    (405, 1010),
    (20, 0), "character/zhukky/zhukky_base1.png",
    (20, 0), "character/zhukky/zhukky_moe11.png")

image zhukky hat moe2 = LiveComposite(
    (405, 1010),
    (20, 0), "character/zhukky/zhukky_base1.png",
    (20, 0), "character/zhukky/zhukky_moe21.png")

image zhukky hat normal = LiveComposite(
    (405, 1010),
    (20, 0), "character/zhukky/zhukky_base1.png",
    (20, 0), "character/zhukky/zhukky_normal1.png")

image zhukky hat embarrassed = LiveComposite(
    (405, 1010),
    (20, 0), "character/zhukky/zhukky_base1.png",
    (20, 0), "character/zhukky/zhukky_embarrassed1.png")

image zhukky hat bored = LiveComposite(
    (405, 1010),
    (20, 0), "character/zhukky/zhukky_base1.png",
    (20, 0), "character/zhukky/zhukky_bored1.png")

image zhukky nohat determined = LiveComposite(
    (405, 1010),
    (20, 0), "character/zhukky/zhukky_base1.png",
    (20, 1), "character/zhukky/zhukky_determined2.png")

image zhukky nohat angry = LiveComposite(
    (405, 1010),
    (20, 0), "character/zhukky/zhukky_base1.png",
    (20, 1), "character/zhukky/zhukky_angry2.png")

image zhukky nohat moe1 = LiveComposite(
    (405, 1010),
    (20, 0), "character/zhukky/zhukky_base1.png",
    (20, 1), "character/zhukky/zhukky_moe12.png")

image zhukky nohat moe2 = LiveComposite(
    (405, 1010),
    (20, 0), "character/zhukky/zhukky_base1.png",
    (20, 1), "character/zhukky/zhukky_moe22.png")

image zhukky nohat normal = LiveComposite(
    (405, 1010),
    (20, 0), "character/zhukky/zhukky_base1.png",
    (20, 1), "character/zhukky/zhukky_normal2.png")

image zhukky nohat embarrassed = LiveComposite(
    (405, 1010),
    (20, 0), "character/zhukky/zhukky_base1.png",
    (20, 1), "character/zhukky/zhukky_embarrassed2.png")

image zhukky nohat bored = LiveComposite(
    (405, 1010),
    (20, 0), "character/zhukky/zhukky_base1.png",
    (20, 1), "character/zhukky/zhukky_bored2.png")

image zhukky swimsuit determined = LiveComposite(
    (405, 1010),
    (20, 1), "character/zhukky/zhukky_base2.png",
    (20, 1), "character/zhukky/zhukky_determined2.png")

image zhukky swimsuit angry = LiveComposite(
    (405, 1010),
    (20, 1), "character/zhukky/zhukky_base2.png",
    (20, 1), "character/zhukky/zhukky_angry2.png")

image zhukky swimsuit moe1 = LiveComposite(
    (405, 1010),
    (20, 1), "character/zhukky/zhukky_base2.png",
    (20, 1), "character/zhukky/zhukky_moe12.png")

image zhukky swimsuit moe2 = LiveComposite(
    (405, 1010),
    (20, 1), "character/zhukky/zhukky_base2.png",
    (20, 1), "character/zhukky/zhukky_moe22.png")

image zhukky swimsuit normal = LiveComposite(
    (405, 1010),
    (20, 1), "character/zhukky/zhukky_base2.png",
    (20, 1), "character/zhukky/zhukky_normal2.png")

image zhukky swimsuit embarrassed = LiveComposite(
    (405, 1010),
    (20, 1), "character/zhukky/zhukky_base2.png",
    (20, 1), "character/zhukky/zhukky_embarrassed2.png")

image zhukky swimsuit bored = LiveComposite(
    (405, 1010),
    (20, 1), "character/zhukky/zhukky_base2.png",
    (20, 1), "character/zhukky/zhukky_bored2.png")

image side zhukky hat determined = LiveCrop((30, 100, 350, 210), LiveComposite((405, 1010), (0, 0), im.Sepia("character/zhukky/zhukky_base1.png"), (0, 0), im.Sepia("character/zhukky/zhukky_determined1.png")))
image side zhukky hat angry = LiveCrop((30, 100, 350, 210), LiveComposite((405, 1010), (0, 0), im.Sepia("character/zhukky/zhukky_base1.png"), (0, 0), im.Sepia("character/zhukky/zhukky_angry1.png")))
image side zhukky hat moe1 = LiveCrop((30, 100, 350, 210), LiveComposite((405, 1010), (0, 0), im.Sepia("character/zhukky/zhukky_base1.png"), (0, 0), im.Sepia("character/zhukky/zhukky_moe11.png")))
image side zhukky hat moe2 = LiveCrop((30, 100, 350, 210), LiveComposite((405, 1010), (0, 0), im.Sepia("character/zhukky/zhukky_base1.png"), (0, 0), im.Sepia("character/zhukky/zhukky_moe21.png")))
image side zhukky hat normal = LiveCrop((30, 100, 350, 210), LiveComposite((405, 1010), (0, 0), im.Sepia("character/zhukky/zhukky_base1.png"), (0, 0), im.Sepia("character/zhukky/zhukky_normal1.png")))
image side zhukky hat embarrassed = LiveCrop((30, 100, 350, 210), LiveComposite((405, 1010), (0, 0), im.Sepia("character/zhukky/zhukky_base1.png"), (0, 0), im.Sepia("character/zhukky/zhukky_embarrassed1.png")))
image side zhukky hat bored = LiveCrop((30, 100, 350, 210), LiveComposite((405, 1010), (0, 0), im.Sepia("character/zhukky/zhukky_base1.png"), (0, 0), im.Sepia("character/zhukky/zhukky_bored1.png")))

image side zhukky nohat determined = LiveCrop((30, 100, 350, 210), LiveComposite((405, 1010), (0, 0), im.Sepia("character/zhukky/zhukky_base1.png"), (0, 0), im.Sepia("character/zhukky/zhukky_determined2.png")))
image side zhukky nohat angry = LiveCrop((30, 100, 350, 210), LiveComposite((405, 1010), (0, 0), im.Sepia("character/zhukky/zhukky_base1.png"), (0, 0), im.Sepia("character/zhukky/zhukky_angry2.png")))
image side zhukky nohat moe1 = LiveCrop((30, 100, 350, 210), LiveComposite((405, 1010), (0, 0), im.Sepia("character/zhukky/zhukky_base1.png"), (0, 0), im.Sepia("character/zhukky/zhukky_moe12.png")))
image side zhukky nohat moe2 = LiveCrop((30, 100, 350, 210), LiveComposite((405, 1010), (0, 0), im.Sepia("character/zhukky/zhukky_base1.png"), (0, 0), im.Sepia("character/zhukky/zhukky_moe22.png")))
image side zhukky nohat normal = LiveCrop((30, 100, 350, 210), LiveComposite((405, 1010), (0, 0), im.Sepia("character/zhukky/zhukky_base1.png"), (0, 0), im.Sepia("character/zhukky/zhukky_normal2.png")))
image side zhukky nohat embarrassed = LiveCrop((30, 100, 350, 210), LiveComposite((405, 1010), (0, 0), im.Sepia("character/zhukky/zhukky_base1.png"), (0, 0), im.Sepia("character/zhukky/zhukky_embarrassed2.png")))
image side zhukky nohat bored = LiveCrop((30, 100, 350, 210), LiveComposite((405, 1010), (0, 0), im.Sepia("character/zhukky/zhukky_base1.png"), (0, 0), im.Sepia("character/zhukky/zhukky_bored2.png")))

image side zhukky swimsuit determined = LiveCrop((30, 100, 350, 210), LiveComposite((405, 1010), (0, 0), im.Sepia("character/zhukky/zhukky_base2.png"), (0, 0), im.Sepia("character/zhukky/zhukky_determined2.png")))
image side zhukky swimsuit angry = LiveCrop((30, 100, 350, 210), LiveComposite((405, 1010), (0, 0), im.Sepia("character/zhukky/zhukky_base2.png"), (0, 0), im.Sepia("character/zhukky/zhukky_angry2.png")))
image side zhukky swimsuit moe1 = LiveCrop((30, 100, 350, 210), LiveComposite((405, 1010), (0, 0), im.Sepia("character/zhukky/zhukky_base2.png"), (0, 0), im.Sepia("character/zhukky/zhukky_moe12.png")))
image side zhukky swimsuit moe2 = LiveCrop((30, 100, 350, 210), LiveComposite((405, 1010), (0, 0), im.Sepia("character/zhukky/zhukky_base2.png"), (0, 0), im.Sepia("character/zhukky/zhukky_moe22.png")))
image side zhukky swimsuit normal = LiveCrop((30, 100, 350, 210), LiveComposite((405, 1010), (0, 0), im.Sepia("character/zhukky/zhukky_base2.png"), (0, 0), im.Sepia("character/zhukky/zhukky_normal2.png")))
image side zhukky swimsuit embarrassed = LiveCrop((30, 100, 350, 210), LiveComposite((405, 1010), (0, 0), im.Sepia("character/zhukky/zhukky_base2.png"), (0, 0), im.Sepia("character/zhukky/zhukky_embarrassed2.png")))
image side zhukky swimsuit bored = LiveCrop((30, 100, 350, 210), LiveComposite((405, 1010), (0, 0), im.Sepia("character/zhukky/zhukky_base2.png"), (0, 0), im.Sepia("character/zhukky/zhukky_bored2.png")))

image zhukky hat determined large = "character/zhukky/zhukky_determined1_large.png"
image zhukky hat angry large = "character/zhukky/zhukky_angry1_large.png"
image zhukky hat bored large = "character/zhukky/zhukky_bored1_large.png"
image zhukky hat normal large = "character/zhukky/zhukky_normal1_large.png"
image zhukky hat embarrassed large = "character/zhukky/zhukky_embarrassed1_large.png"
image zhukky hat moe1 large = "character/zhukky/zhukky_moe11_large.png"
image zhukky hat moe2 large = "character/zhukky/zhukky_moe21_large.png"

image zhukky swimsuit determined large = "character/zhukky/zhukky_swimsuit_determined1_large.png"
image zhukky swimsuit angry large = "character/zhukky/zhukky_swimsuit_angry1_large.png"
image zhukky swimsuit bored large = "character/zhukky/zhukky_swimsuit_bored1_large.png"
image zhukky swimsuit normal large = "character/zhukky/zhukky_swimsuit_normal1_large.png"
image zhukky swimsuit embarrassed large = "character/zhukky/zhukky_swimsuit_embarrassed1_large.png"
image zhukky swimsuit moe1 large = "character/zhukky/zhukky_swimsuit_moe11_large.png"
image zhukky swimsuit moe2 large = "character/zhukky/zhukky_swimsuit_moe21_large.png"

########################################################
# Rinni ###############################################
########################################################
image rinni hat worry = LiveComposite(
    (800, 1040),
    (0, 0), "character/rinni/rinni_base1.png",
    (0, 0), "character/rinni/rinni_worry1.png")

image rinni hat happy = LiveComposite(
    (800, 1040),
    (0, 0), "character/rinni/rinni_base1.png",
    (0, 0), "character/rinni/rinni_happy1.png")

image rinni hat determined = LiveComposite(
    (800, 1040),
    (0, 0), "character/rinni/rinni_base1.png",
    (0, 0), "character/rinni/rinni_determined1.png")

image rinni hat embarrassed = LiveComposite(
    (800, 1040),
    (0, 0), "character/rinni/rinni_base1.png",
    (0, 0), "character/rinni/rinni_embarrassed1.png")

image rinni hat shock = LiveComposite(
    (800, 1040),
    (0, 0), "character/rinni/rinni_base1.png",
    (0, 0), "character/rinni/rinni_shock1.png")

image rinni hat normal = LiveComposite(
    (800, 1040),
    (0, 0), "character/rinni/rinni_base1.png",
    (0, 0), "character/rinni/rinni_normal1.png")

image rinni hat moe1 = LiveComposite(
    (800, 1040),
    (0, 0), "character/rinni/rinni_base1.png",
    (0, 0), "character/rinni/rinni_moe11.png",
    (158, 170), "rinni_crown")

image rinni hat moe2 = LiveComposite(
    (800, 1040),
    (0, 0), "character/rinni/rinni_base1.png",
    (0, 0), "character/rinni/rinni_moe21.png")

image rinni hat moe3 = LiveComposite(
    (800, 1040),
    (0, 0), "character/rinni/rinni_base2.png",
    (0, 0), "character/rinni/rinni_moe31.png",
    (160, 100), "rinni dot")

image rinni hat moe4 = LiveComposite(
    (800, 1040),
    (0, 0), "character/rinni/rinni_base1.png",
    (0, 0), "character/rinni/rinni_moe41.png",
    (0, -120), "rinni_bubble")

image rinni swimsuit worry = LiveComposite(
    (800, 1040),
    (0, 0), "character/rinni/rinni_base3.png",
    (0, 0), "character/rinni/rinni_worry2.png")

image rinni swimsuit happy = LiveComposite(
    (800, 1040),
    (0, 0), "character/rinni/rinni_base3.png",
    (0, 0), "character/rinni/rinni_happy2.png")

image rinni swimsuit determined = LiveComposite(
    (800, 1040),
    (0, 0), "character/rinni/rinni_base3.png",
    (0, 0), "character/rinni/rinni_determined2.png")

image rinni swimsuit embarrassed = LiveComposite(
    (800, 1040),
    (0, 0), "character/rinni/rinni_base3.png",
    (0, 0), "character/rinni/rinni_embarrassed2.png")

image rinni swimsuit shock = LiveComposite(
    (800, 1040),
    (0, 0), "character/rinni/rinni_base3.png",
    (0, 0), "character/rinni/rinni_shock2.png")

image rinni swimsuit normal = LiveComposite(
    (800, 1040),
    (0, 0), "character/rinni/rinni_base3.png",
    (0, 0), "character/rinni/rinni_normal2.png")

image rinni swimsuit moe1 = LiveComposite(
    (800, 1040),
    (0, 0), "character/rinni/rinni_base3.png",
    (0, 0), "character/rinni/rinni_moe12.png",
    (158, 170), "rinni_crown")

image rinni swimsuit moe2 = LiveComposite(
    (800, 1040),
    (0, 0), "character/rinni/rinni_base4.png",
    (0, 0), "character/rinni/rinni_moe22.png")

image rinni swimsuit moe3 = LiveComposite(
    (800, 1040),
    (0, 0), "character/rinni/rinni_base3.png",
    (0, 0), "character/rinni/rinni_moe32.png",
    (160, 100), "rinni dot")

image rinni swimsuit moe4 = LiveComposite(
    (800, 1040),
    (0, 0), "character/rinni/rinni_base3.png",
    (0, 0), "character/rinni/rinni_moe42.png",
    (0, -120), "rinni_bubble")
    
image rinni dot:
    contains:
        LiveCrop((0, 0, 50, 26), "character/rinni/rinni_dot.png")
        alpha 0
        pause .5
        alpha 1.0
        pause .5
        alpha 0
        pause 2
        repeat
    contains:
        LiveCrop((0, 0, 200, 26), "character/rinni/rinni_dot.png")
        alpha 0
        pause 1
        alpha 1.0
        pause .5
        alpha 0
        pause 1.5
        repeat
    contains:
        LiveCrop((0, 0, 350, 26), "character/rinni/rinni_dot.png")
        alpha 0
        pause 1.5
        alpha 1.0
        pause .5
        alpha 0
        pause 1
        repeat
    contains:
        LiveCrop((0, 0, 433, 26), "character/rinni/rinni_dot.png")
        alpha 0
        pause 2
        alpha 1.0
        pause .5
        alpha 0
        pause .5
        repeat

image side rinni hat determined = LiveCrop((210, 190, 350, 210), LiveComposite((800, 1040), (0, 0), im.Sepia("character/rinni/rinni_base1.png"), (0, 0), im.Sepia("character/rinni/rinni_determined1.png")))
image side rinni hat happy = LiveCrop((210, 190, 350, 210), LiveComposite((800, 1040), (0, 0), im.Sepia("character/rinni/rinni_base1.png"), (0, 0), im.Sepia("character/rinni/rinni_happy1.png")))
image side rinni hat moe1 = LiveCrop((210, 190, 350, 210), LiveComposite((800, 1040), (0, 0), im.Sepia("character/rinni/rinni_base1.png"), (0, 0), im.Sepia("character/rinni/rinni_moe11.png")))
image side rinni hat moe2 = LiveCrop((210, 190, 350, 210), LiveComposite((800, 1040), (0, 0), im.Sepia("character/rinni/rinni_base1.png"), (0, 0), im.Sepia("character/rinni/rinni_moe21.png")))
image side rinni hat moe3 = LiveCrop((210, 190, 350, 210), LiveComposite((800, 1040), (0, 0), im.Sepia("character/rinni/rinni_base1.png"), (0, 0), im.Sepia("character/rinni/rinni_moe31.png")))
image side rinni hat moe4 = LiveCrop((210, 190, 350, 210), LiveComposite((800, 1040), (0, 0), im.Sepia("character/rinni/rinni_base1.png"), (0, 0), im.Sepia("character/rinni/rinni_moe41.png")))
image side rinni hat normal = LiveCrop((210, 190, 350, 210), LiveComposite((800, 1040), (0, 0), im.Sepia("character/rinni/rinni_base1.png"), (0, 0), im.Sepia("character/rinni/rinni_normal1.png")))
image side rinni hat worry = LiveCrop((210, 190, 350, 210), LiveComposite((800, 1040), (0, 0), im.Sepia("character/rinni/rinni_base1.png"), (0, 0), im.Sepia("character/rinni/rinni_worry1.png")))
image side rinni hat shock = LiveCrop((210, 190, 350, 210), LiveComposite((800, 1040), (0, 0), im.Sepia("character/rinni/rinni_base1.png"), (0, 0), im.Sepia("character/rinni/rinni_shock1.png")))
image side rinni hat embarrassed = LiveCrop((210, 190, 350, 210), LiveComposite((800, 1040), (0, 0), im.Sepia("character/rinni/rinni_base1.png"), (0, 0), im.Sepia("character/rinni/rinni_embarrassed1.png")))
image side rinni swimsuit determined = LiveCrop((210, 190, 350, 210), LiveComposite((800, 1040), (0, 0), im.Sepia("character/rinni/rinni_base3.png"), (0, 0), im.Sepia("character/rinni/rinni_determined2.png")))
image side rinni swimsuit happy = LiveCrop((210, 190, 350, 210), LiveComposite((800, 1040), (0, 0), im.Sepia("character/rinni/rinni_base3.png"), (0, 0), im.Sepia("character/rinni/rinni_happy2.png")))
image side rinni swimsuit moe1 = LiveCrop((210, 190, 350, 210), LiveComposite((800, 1040), (0, 0), im.Sepia("character/rinni/rinni_base3.png"), (0, 0), im.Sepia("character/rinni/rinni_moe12.png")))
image side rinni swimsuit moe2 = LiveCrop((210, 190, 350, 210), LiveComposite((800, 1040), (0, 0), im.Sepia("character/rinni/rinni_base3.png"), (0, 0), im.Sepia("character/rinni/rinni_moe22.png")))
image side rinni swimsuit moe3 = LiveCrop((210, 190, 350, 210), LiveComposite((800, 1040), (0, 0), im.Sepia("character/rinni/rinni_base3.png"), (0, 0), im.Sepia("character/rinni/rinni_moe32.png")))
image side rinni swimsuit moe4 = LiveCrop((210, 190, 350, 210), LiveComposite((800, 1040), (0, 0), im.Sepia("character/rinni/rinni_base3.png"), (0, 0), im.Sepia("character/rinni/rinni_moe42.png")))
image side rinni swimsuit normal = LiveCrop((210, 190, 350, 210), LiveComposite((800, 1040), (0, 0), im.Sepia("character/rinni/rinni_base3.png"), (0, 0), im.Sepia("character/rinni/rinni_normal2.png")))
image side rinni swimsuit worry = LiveCrop((210, 190, 350, 210), LiveComposite((800, 1040), (0, 0), im.Sepia("character/rinni/rinni_base3.png"), (0, 0), im.Sepia("character/rinni/rinni_worry2.png")))
image side rinni swimsuit shock = LiveCrop((210, 190, 350, 210), LiveComposite((800, 1040), (0, 0), im.Sepia("character/rinni/rinni_base3.png"), (0, 0), im.Sepia("character/rinni/rinni_shock2.png")))
image side rinni swimsuit embarrassed = LiveCrop((210, 190, 350, 210), LiveComposite((800, 1040), (0, 0), im.Sepia("character/rinni/rinni_base3.png"), (0, 0), im.Sepia("character/rinni/rinni_embarrassed2.png")))

########################################################
# Cyrano ###############################################
########################################################
image cyrano hat angry = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_angry1.png")

image cyrano hat determined = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base2.png",
    (0, 0), "character/cyrano/cyrano_determined3.png")

image cyrano hat happy = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_happy1.png")

image cyrano hat embarrassed = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_embarrassed1.png")

image cyrano hat sad = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_sad1.png")

image cyrano hat normal = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_normal1.png")

image cyrano hat shock = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_shock1.png")

image cyrano hat moe1 = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_moe11.png")

image cyrano hat moe2 = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_moe21.png")

image cyrano hat moe3 = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_moe31.png")

image cyrano hat moe4 = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_moe41.png")

image cyrano nohat angry = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_angry5.png")

image cyrano nohat determined = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base2.png",
    (0, 0), "character/cyrano/cyrano_determined7.png")

image cyrano nohat happy = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_happy2.png")

image cyrano nohat embarrassed = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_embarrassed2.png")

image cyrano nohat sad = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_sad5.png")

image cyrano nohat normal = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_normal5.png")

image cyrano nohat shock = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_shock5.png")

image cyrano nohat moe1 = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_moe15.png")

image cyrano nohat moe2 = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_moe25.png")

image cyrano nohat moe3 = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_moe35.png")

image cyrano nohat moe4 = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_moe45.png")


image cyrano swimsuit angry = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base3.png",
    (0, 0), "character/cyrano/cyrano_angry9.png")

image cyrano swimsuit determined = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base4.png",
    (0, 0), "character/cyrano/cyrano_determined11.png")

image cyrano swimsuit happy = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base3.png",
    (0, 0), "character/cyrano/cyrano_happy3.png")

image cyrano swimsuit embarrassed = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base3.png",
    (0, 0), "character/cyrano/cyrano_embarrassed3.png")

image cyrano swimsuit sad = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base3.png",
    (0, 0), "character/cyrano/cyrano_sad9.png")

image cyrano swimsuit normal = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base3.png",
    (0, 0), "character/cyrano/cyrano_normal9.png")

image cyrano swimsuit shock = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base3.png",
    (0, 0), "character/cyrano/cyrano_shock9.png")

image cyrano swimsuit moe1 = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base3.png",
    (0, 0), "character/cyrano/cyrano_moe19.png")

image cyrano swimsuit moe2 = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base3.png",
    (0, 0), "character/cyrano/cyrano_moe29.png")

image cyrano swimsuit moe3 = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base3.png",
    (0, 0), "character/cyrano/cyrano_moe39.png")

image cyrano swimsuit moe4 = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base3.png",
    (0, 0), "character/cyrano/cyrano_moe49.png")


image cyrano hat cig angry = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_angry2.png")

image cyrano hat cig determined = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base2.png",
    (0, 0), "character/cyrano/cyrano_determined4.png")

image cyrano hat cig happy = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_happy1.png")

image cyrano hat cig embarrassed = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_embarrassed1.png")

image cyrano hat cig sad = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_sad2.png")

image cyrano hat cig normal = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_normal2.png")

image cyrano hat cig shock = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_shock2.png")

image cyrano hat cig moe1 = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_moe12.png")

image cyrano hat cig moe2 = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_moe22.png")

image cyrano hat cig moe3 = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_moe32.png")

image cyrano hat cig moe4 = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_moe42.png")

image cyrano nohat cig angry = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_angry6.png")

image cyrano nohat cig determined = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base2.png",
    (0, 0), "character/cyrano/cyrano_determined8.png")

image cyrano nohat cig happy = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_happy2.png")

image cyrano nohat cig embarrassed = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_embarrassed2.png")

image cyrano nohat cig sad = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_sad6.png")

image cyrano nohat cig normal = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_normal6.png")

image cyrano nohat cig shock = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_shock6.png")

image cyrano nohat cig moe1 = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_moe16.png")

image cyrano nohat cig moe2 = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_moe26.png")

image cyrano nohat cig moe3 = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_moe36.png")

image cyrano nohat cig moe4 = LiveComposite(
    (960, 1010),
    (0, 0), "character/cyrano/cyrano_base1.png",
    (0, 0), "character/cyrano/cyrano_moe46.png")

image cyrano tank moe2:
    "cyrano hat cig moe2"
    ypos 1.0
    linear 0.5 ypos 1.05
    linear 0.5 ypos 1.0
    repeat
    
image cyrano tank angry:
    "cyrano hat cig angry"
    ypos 1.0
    linear 0.5 ypos 1.05
    linear 0.5 ypos 1.0
    repeat
    
image cyrano tank determined:
    "cyrano hat cig determined"
    ypos 1.0
    linear 0.5 ypos 1.05
    linear 0.5 ypos 1.0
    repeat

image side cyrano hat angry = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_angry1.png")))
image side cyrano hat determined = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_determined1.png")))
image side cyrano hat happy = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_happy1.png")))
image side cyrano hat moe1 = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_moe11.png")))
image side cyrano hat moe2 = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_moe21.png")))
image side cyrano hat moe3 = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_moe31.png")))
image side cyrano hat moe4 = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_moe41.png")))
image side cyrano hat normal = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_normal1.png")))
image side cyrano hat sad = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_sad1.png")))
image side cyrano hat shock = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_shock1.png")))
image side cyrano hat embarrassed = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_embarrassed1.png")))
image side cyrano nohat angry = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_angry5.png")))
image side cyrano nohat determined = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_determined5.png")))
image side cyrano nohat happy = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_happy2.png")))
image side cyrano nohat moe1 = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_moe15.png")))
image side cyrano nohat moe2 = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_moe25.png")))
image side cyrano nohat moe3 = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_moe35.png")))
image side cyrano nohat moe4 = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_moe45.png")))
image side cyrano nohat normal = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_normal5.png")))
image side cyrano nohat sad = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_sad5.png")))
image side cyrano nohat shock = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_shock5.png")))
image side cyrano nohat embarrassed = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_embarrassed2.png")))
image side cyrano hat cig angry = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_angry2.png")))
image side cyrano hat cig determined = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_determined2.png")))
image side cyrano hat cig happy = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_happy2.png")))
image side cyrano hat cig moe1 = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_moe12.png")))
image side cyrano hat cig moe2 = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_moe22.png")))
image side cyrano hat cig moe3 = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_moe32.png")))
image side cyrano hat cig moe4 = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_moe42.png")))
image side cyrano hat cig normal = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_normal2.png")))
image side cyrano hat cig sad = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_sad2.png")))
image side cyrano hat cig shock = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_shock2.png")))
image side cyrano hat cig embarrassed = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_embarrassed2.png")))
image side cyrano nohat cig angry = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_angry6.png")))
image side cyrano nohat cig determined = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_determined6.png")))
image side cyrano nohat cig happy = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_happy2.png")))
image side cyrano nohat cig moe1 = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_moe16.png")))
image side cyrano nohat cig moe2 = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_moe26.png")))
image side cyrano nohat cig moe3 = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_moe36.png")))
image side cyrano nohat cig moe4 = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_moe46.png")))
image side cyrano nohat cig normal = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_normal6.png")))
image side cyrano nohat cig sad = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_sad6.png")))
image side cyrano nohat cig shock = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_shock6.png")))
image side cyrano nohat cig embarrassed = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_embarrassed2.png")))
image side cyrano swimsuit angry = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_angry9.png")))
image side cyrano swimsuit determined = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_determined9.png")))
image side cyrano swimsuit happy = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_happy3.png")))
image side cyrano swimsuit moe1 = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_moe19.png")))
image side cyrano swimsuit moe2 = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_moe29.png")))
image side cyrano swimsuit moe3 = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_moe39.png")))
image side cyrano swimsuit moe4 = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_moe49.png")))
image side cyrano swimsuit normal = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_normal9.png")))
image side cyrano swimsuit sad = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_sad9.png")))
image side cyrano swimsuit shock = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_shock9.png")))
image side cyrano swimsuit embarrassed = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_embarrassed3.png")))
image side cyrano tank moe2 = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_moe21.png")))
image side cyrano tank angry = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_angry1.png")))
image side cyrano tank determined = LiveCrop((310, 150, 350, 210), LiveComposite((960, 1010), (0, 0), im.Sepia("character/cyrano/cyrano_base1.png"), (0, 0), im.Sepia("character/cyrano/cyrano_determined1.png")))

########################################################
# Reine Jean ###############################################
########################################################
image roijean hat angry = LiveComposite(
    (800, 940),
    (0, 0), "character/roijean/roijean_base1.png",
    (0, 0), "character/roijean/roijean_angry1.png")

image roijean hat determined = LiveComposite(
    (800, 940),
    (0, 0), "character/roijean/roijean_base1.png",
    (0, 0), "character/roijean/roijean_determined1.png")

image roijean hat happy = LiveComposite(
    (800, 940),
    (0, 0), "character/roijean/roijean_base1.png",
    (0, 0), "character/roijean/roijean_happy1.png")

image roijean hat sad = LiveComposite(
    (800, 940),
    (0, 0), "character/roijean/roijean_base1.png",
    (0, 0), "character/roijean/roijean_sad1.png")

image roijean hat normal = LiveComposite(
    (800, 940),
    (0, 0), "character/roijean/roijean_base1.png",
    (0, 0), "character/roijean/roijean_normal1.png")

image roijean hat moe1 = LiveComposite(
    (800, 940),
    (0, 0), "character/roijean/roijean_base1.png",
    (0, 0), "character/roijean/roijean_moe11.png",
    (570, 103), "roijean_crown")

image roijean hat moe2 = LiveComposite(
    (800, 940),
    (0, 0), "character/roijean/roijean_base1.png",
    (0, 0), "character/roijean/roijean_moe21.png")

image roijean nohat angry = LiveComposite(
    (800, 940),
    (0, 0), "character/roijean/roijean_base1.png",
    (0, 0), "character/roijean/roijean_angry2.png")

image roijean nohat determined = LiveComposite(
    (800, 940),
    (0, 0), "character/roijean/roijean_base1.png",
    (0, 0), "character/roijean/roijean_determined2.png")

image roijean nohat happy = LiveComposite(
    (800, 940),
    (0, 0), "character/roijean/roijean_base1.png",
    (0, 0), "character/roijean/roijean_happy2.png")

image roijean nohat sad = LiveComposite(
    (800, 940),
    (0, 0), "character/roijean/roijean_base1.png",
    (0, 0), "character/roijean/roijean_sad2.png")

image roijean nohat normal = LiveComposite(
    (800, 940),
    (0, 0), "character/roijean/roijean_base1.png",
    (0, 0), "character/roijean/roijean_normal2.png")

image roijean nohat moe1 = LiveComposite(
    (800, 940),
    (0, 0), "character/roijean/roijean_base1.png",
    (0, 0), "character/roijean/roijean_moe12.png",
    (570, 103), "roijean_crown")

image roijean nohat moe2 = LiveComposite(
    (800, 940),
    (0, 0), "character/roijean/roijean_base1.png",
    (0, 0), "character/roijean/roijean_moe22.png")

image side roijean hat angry = LiveCrop((250, 120, 350, 210), LiveComposite((700, 940), (0, 0), im.Sepia("character/roijean/roijean_base1.png"), (0, 0), im.Sepia("character/roijean/roijean_angry1.png")))
image side roijean hat determined = LiveCrop((250, 120, 350, 210), LiveComposite((700, 940), (0, 0), im.Sepia("character/roijean/roijean_base1.png"), (0, 0), im.Sepia("character/roijean/roijean_determined1.png")))
image side roijean hat happy = LiveCrop((250, 120, 350, 210), LiveComposite((700, 940), (0, 0), im.Sepia("character/roijean/roijean_base1.png"), (0, 0), im.Sepia("character/roijean/roijean_happy1.png")))
image side roijean hat moe1 = LiveCrop((250, 120, 350, 210), LiveComposite((700, 940), (0, 0), im.Sepia("character/roijean/roijean_base1.png"), (0, 0), im.Sepia("character/roijean/roijean_moe11.png")))
image side roijean hat moe2 = LiveCrop((250, 120, 350, 210), LiveComposite((700, 940), (0, 0), im.Sepia("character/roijean/roijean_base1.png"), (0, 0), im.Sepia("character/roijean/roijean_moe21.png")))
image side roijean hat normal = LiveCrop((250, 120, 350, 210), LiveComposite((700, 940), (0, 0), im.Sepia("character/roijean/roijean_base1.png"), (0, 0), im.Sepia("character/roijean/roijean_normal1.png")))
image side roijean hat sad = LiveCrop((250, 120, 350, 210), LiveComposite((700, 940), (0, 0), im.Sepia("character/roijean/roijean_base1.png"), (0, 0), im.Sepia("character/roijean/roijean_sad1.png")))
image side roijean hat weak = LiveCrop((250, 120, 350, 210), LiveComposite((700, 940), (0, 0), im.Sepia("character/roijean/roijean_base1.png"), (0, 0), im.Sepia("character/roijean/roijean_moe11.png")))
image side roijean nohat angry = LiveCrop((250, 120, 350, 210), LiveComposite((700, 940), (0, 0), im.Sepia("character/roijean/roijean_base1.png"), (0, 0), im.Sepia("character/roijean/roijean_angry2.png")))
image side roijean nohat determined = LiveCrop((250, 120, 350, 210), LiveComposite((700, 940), (0, 0), im.Sepia("character/roijean/roijean_base1.png"), (0, 0), im.Sepia("character/roijean/roijean_determined2.png")))
image side roijean nohat happy = LiveCrop((250, 120, 350, 210), LiveComposite((700, 940), (0, 0), im.Sepia("character/roijean/roijean_base1.png"), (0, 0), im.Sepia("character/roijean/roijean_happy2.png")))
image side roijean nohat moe1 = LiveCrop((250, 120, 350, 210), LiveComposite((700, 940), (0, 0), im.Sepia("character/roijean/roijean_base1.png"), (0, 0), im.Sepia("character/roijean/roijean_moe12.png")))
image side roijean nohat moe2 = LiveCrop((250, 120, 350, 210), LiveComposite((700, 940), (0, 0), im.Sepia("character/roijean/roijean_base1.png"), (0, 0), im.Sepia("character/roijean/roijean_moe22.png")))
image side roijean nohat normal = LiveCrop((250, 120, 350, 210), LiveComposite((700, 940), (0, 0), im.Sepia("character/roijean/roijean_base1.png"), (0, 0), im.Sepia("character/roijean/roijean_normal2.png")))
image side roijean nohat sad = LiveCrop((250, 120, 350, 210), LiveComposite((700, 940), (0, 0), im.Sepia("character/roijean/roijean_base1.png"), (0, 0), im.Sepia("character/roijean/roijean_sad2.png")))

########################################################
# Monty ###############################################
########################################################
image monty happy = LiveComposite(
    (620, 1030),
    (0, 0), "character/monty/monty_base1.png",
    (0, 0), "character/monty/monty_happy1.png")

image monty determined = LiveComposite(
    (620, 1030),
    (0, 0), "character/monty/monty_base1.png",
    (0, 0), "character/monty/monty_determined1.png")

image monty bored = LiveComposite(
    (620, 1030),
    (0, 0), "character/monty/monty_base1.png",
    (0, 0), "character/monty/monty_bored1.png")

image monty sad = LiveComposite(
    (620, 1030),
    (0, 0), "character/monty/monty_base1.png",
    (0, 0), "character/monty/monty_sad1.png")

image monty normal = LiveComposite(
    (620, 1030),
    (0, 0), "character/monty/monty_base1.png",
    (0, 0), "character/monty/monty_normal1.png")

image monty moe1 = LiveComposite(
    (620, 1030),
    (0, 0), "character/monty/monty_base1.png",
    (0, 0), "character/monty/monty_moe11.png")

image monty moe2 = LiveComposite(
    (620, 1030),
    (0, 0), "character/monty/monty_base1.png",
    (0, 0), "character/monty/monty_moe21.png")

image monty power = LiveComposite(
    (620, 1030),
    (0, 0), "character/monty/monty_base2.png",
    (0, 0), "character/monty/monty_power1.png")

image monty beginning large = "character/monty/monty_beginning_large.png"

image side monty beginning large = LiveCrop((150, 90, 350, 210), LiveComposite((620, 1030), (0, 0), im.Sepia("character/monty/monty_base1.png"), (0, 0), im.Sepia("character/monty/monty_determined1.png")))
image side monty bored = LiveCrop((150, 90, 350, 210), LiveComposite((620, 1030), (0, 0), im.Sepia("character/monty/monty_base1.png"), (0, 0), im.Sepia("character/monty/monty_bored1.png")))
image side monty determined = LiveCrop((150, 90, 350, 210), LiveComposite((620, 1030), (0, 0), im.Sepia("character/monty/monty_base1.png"), (0, 0), im.Sepia("character/monty/monty_determined1.png")))
image side monty happy = LiveCrop((150, 90, 350, 210), LiveComposite((620, 1030), (0, 0), im.Sepia("character/monty/monty_base1.png"), (0, 0), im.Sepia("character/monty/monty_happy1.png")))
image side monty moe1 = LiveCrop((150, 90, 350, 210), LiveComposite((620, 1030), (0, 0), im.Sepia("character/monty/monty_base1.png"), (0, 0), im.Sepia("character/monty/monty_moe11.png")))
image side monty moe2 = LiveCrop((150, 90, 350, 210), LiveComposite((620, 1030), (0, 0), im.Sepia("character/monty/monty_base1.png"), (0, 0), im.Sepia("character/monty/monty_moe21.png")))
image side monty normal = LiveCrop((150, 90, 350, 210), LiveComposite((620, 1030), (0, 0), im.Sepia("character/monty/monty_base1.png"), (0, 0), im.Sepia("character/monty/monty_normal1.png")))
image side monty sad = LiveCrop((150, 90, 350, 210), LiveComposite((620, 1030), (0, 0), im.Sepia("character/monty/monty_base1.png"), (0, 0), im.Sepia("character/monty/monty_sad1.png")))
image side monty power = LiveCrop((150, 90, 350, 210), LiveComposite((620, 1030), (0, 0), im.Sepia("character/monty/monty_base2.png"), (0, 0), im.Sepia("character/monty/monty_power1.png")))


########################################################
# Rommel ###############################################
########################################################
image rommel tank annoyed:
    "rommel annoyed"
    ypos 1.0
    linear 0.5 ypos 1.02
    linear 0.5 ypos 1.0
    repeat

image rommel tank determined:
    "rommel determined"
    ypos 1.0
    linear 0.5 ypos 1.02
    linear 0.5 ypos 1.0
    repeat
    
image rommel tank moe1:
    "rommel moe1"
    ypos 1.0
    linear 0.5 ypos 1.02
    linear 0.5 ypos 1.0
    repeat
    
image rommel tank moe2:
    "rommel moe2"
    ypos 1.0
    linear 0.5 ypos 1.02
    linear 0.5 ypos 1.0
    repeat
    
image rommel ski determined:
    "rommel determined"
    xalign 0.75 yalign 1.0
    linear 0.15 yalign 1.2
    linear 0.15 yalign 1.0
    repeat

image rommel annoyed = LiveComposite(
    (800, 1000),
    (0, 0), "character/rommel/rommel_base1.png",
    (0, 0), "character/rommel/rommel_annoyed1.png")

image rommel determined = LiveComposite(
    (800, 1000),
    (0, 0), "character/rommel/rommel_base1.png",
    (0, 0), "character/rommel/rommel_determined1.png")

image rommel embarrassed = LiveComposite(
    (800, 1000),
    (0, 0), "character/rommel/rommel_base1.png",
    (0, 0), "character/rommel/rommel_embarrassed1.png")

image rommel sad = LiveComposite(
    (800, 1000),
    (0, 0), "character/rommel/rommel_base1.png",
    (0, 0), "character/rommel/rommel_sad1.png")

image rommel normal = LiveComposite(
    (800, 1000),
    (0, 0), "character/rommel/rommel_base1.png",
    (0, 0), "character/rommel/rommel_normal1.png")

image rommel moe1 = LiveComposite(
    (800, 1000),
    (0, 0), "character/rommel/rommel_base1.png",
    (0, 0), "character/rommel/rommel_moe11.png")

image rommel moe2 = LiveComposite(
    (800, 1000),
    (0, 0), "character/rommel/rommel_base1.png",
    (0, 0), "character/rommel/rommel_moe21.png",
    (169, 200), "rommel_exclamation")

image rommel shock = LiveComposite(
    (800, 1000),
    (0, 0), "character/rommel/rommel_base1.png",
    (0, 0), "character/rommel/rommel_shock1.png")

image rommel beginning large = "character/rommel/rommel_beginning_large.png"

image side rommel beginning = LiveCrop((230, 190, 350, 210), LiveComposite((800, 1000), (0, 0), im.Sepia("character/rommel/rommel_base1.png"), (0, 0), im.Sepia("character/rommel/rommel_annoyed1.png")))
image side rommel annoyed = LiveCrop((230, 190, 350, 210), LiveComposite((800, 1000), (0, 0), im.Sepia("character/rommel/rommel_base1.png"), (0, 0), im.Sepia("character/rommel/rommel_annoyed1.png")))
image side rommel determined = LiveCrop((230, 190, 350, 210), LiveComposite((800, 1000), (0, 0), im.Sepia("character/rommel/rommel_base1.png"), (0, 0), im.Sepia("character/rommel/rommel_determined1.png")))
image side rommel moe1 = LiveCrop((230, 190, 350, 210), LiveComposite((800, 1000), (0, 0), im.Sepia("character/rommel/rommel_base1.png"), (0, 0), im.Sepia("character/rommel/rommel_moe11.png")))
image side rommel moe2 = LiveCrop((230, 190, 350, 210), LiveComposite((800, 1000), (0, 0), im.Sepia("character/rommel/rommel_base1.png"), (0, 0), im.Sepia("character/rommel/rommel_moe21.png")))
image side rommel shock = LiveCrop((230, 190, 350, 210), LiveComposite((800, 1000), (0, 0), im.Sepia("character/rommel/rommel_base1.png"), (0, 0), im.Sepia("character/rommel/rommel_shock1.png")))
image side rommel normal = LiveCrop((230, 190, 350, 210), LiveComposite((800, 1000), (0, 0), im.Sepia("character/rommel/rommel_base1.png"), (0, 0), im.Sepia("character/rommel/rommel_normal1.png")))
image side rommel sad = LiveCrop((230, 190, 350, 210), LiveComposite((800, 1000), (0, 0), im.Sepia("character/rommel/rommel_base1.png"), (0, 0), im.Sepia("character/rommel/rommel_sad1.png")))
image side rommel embarrassed = LiveCrop((230, 190, 350, 210), LiveComposite((800, 1000), (0, 0), im.Sepia("character/rommel/rommel_base1.png"), (0, 0), im.Sepia("character/rommel/rommel_embarrassed1.png")))
image side rommel ski determined = LiveCrop((230, 190, 350, 210), LiveComposite((800, 1000), (0, 0), im.Sepia("character/rommel/rommel_base1.png"), (0, 0), im.Sepia("character/rommel/rommel_determined1.png")))


########################################################
# Nyan ###############################################
#####################################################
image nyan powers large = "character/nyan/nyan_powers_large.png"
        
image nyan angry = LiveComposite(
    (650, 880),
    (0, 0), "character/nyan/nyan_base1.png",
    (0, 0), "character/nyan/nyan_angry1.png")

image nyan determined = LiveComposite(
    (650, 880),
    (0, 0), "character/nyan/nyan_base1.png",
    (0, 0), "character/nyan/nyan_determined1.png") 

image nyan normal = LiveComposite(
    (650, 880),
    (0, 0), "character/nyan/nyan_base1.png",
    (0, 0), "character/nyan/nyan_normal1.png")

image nyan happy = LiveComposite(
    (650, 880),
    (0, 0), "character/nyan/nyan_base1.png",
    (0, 0), "character/nyan/nyan_happy1.png")

image nyan moe1 = LiveComposite(
    (650, 880),
    (0, 0), "character/nyan/nyan_base1.png",
    (0, 0), "character/nyan/nyan_moe11.png")

image nyan moe2 = LiveComposite(
    (650, 880),
    (0, 0), "character/nyan/nyan_base1.png",
    (0, 0), "character/nyan/nyan_moe21.png")

image nyan sad = LiveComposite(                                               
    (650, 880),
    (0, 0), "character/nyan/nyan_base1.png",
    (0, 0), "character/nyan/nyan_sad1.png")

image nyan smirk = LiveComposite(                                               
    (650, 880),
    (0, 0), "character/nyan/nyan_base1.png",
    (0, 0), "character/nyan/nyan_smirk1.png")

image side nyan angry = LiveCrop((140, 110, 350, 210), LiveComposite((650, 880), (0, 0), im.Sepia("character/nyan/nyan_base1.png"), (0, 0), im.Sepia("character/nyan/nyan_angry1.png")))
image side nyan determined = LiveCrop((140, 110, 350, 210), LiveComposite((650, 880), (0, 0), im.Sepia("character/nyan/nyan_base1.png"), (0, 0), im.Sepia("character/nyan/nyan_determined1.png")))
image side nyan powers = LiveCrop((140, 110, 350, 210), LiveComposite((650, 880), (0, 0), im.Sepia("character/nyan/nyan_base1.png"), (0, 0), im.Sepia("character/nyan/nyan_determined1.png")))
image side nyan moe1 = LiveCrop((140, 110, 350, 210), LiveComposite((650, 880), (0, 0), im.Sepia("character/nyan/nyan_base1.png"), (0, 0), im.Sepia("character/nyan/nyan_moe11.png")))
image side nyan moe2 = LiveCrop((140, 110, 350, 210), LiveComposite((650, 880), (0, 0), im.Sepia("character/nyan/nyan_base1.png"), (0, 0), im.Sepia("character/nyan/nyan_moe21.png")))
image side nyan happy = LiveCrop((140, 110, 350, 210), LiveComposite((650, 880), (0, 0), im.Sepia("character/nyan/nyan_base1.png"), (0, 0), im.Sepia("character/nyan/nyan_happy1.png")))
image side nyan normal = LiveCrop((140, 110, 350, 210), LiveComposite((650, 880), (0, 0), im.Sepia("character/nyan/nyan_base1.png"), (0, 0), im.Sepia("character/nyan/nyan_normal1.png")))
image side nyan sad = LiveCrop((140, 110, 350, 210), LiveComposite((650, 880), (0, 0), im.Sepia("character/nyan/nyan_base1.png"), (0, 0), im.Sepia("character/nyan/nyan_sad1.png")))
image side nyan smirk = LiveCrop((140, 110, 350, 210), LiveComposite((650, 880), (0, 0), im.Sepia("character/nyan/nyan_base1.png"), (0, 0), im.Sepia("character/nyan/nyan_smirk1.png")))

########################################################
# Roosevelt ###############################################
########################################################
image roosevelt annoyed = LiveComposite(
    (900, 1020),
    (0, 0), "character/roosevelt/roosevelt_base1.png",
    (0, 0), "character/roosevelt/roosevelt_annoyed1.png")

image roosevelt evil = LiveComposite(
    (900, 1020),
    (0, 0), "character/roosevelt/roosevelt_base1.png",
    (0, 0), "character/roosevelt/roosevelt_evil1.png")

image roosevelt bored = LiveComposite(
    (900, 1020),
    (0, 0), "character/roosevelt/roosevelt_base1.png",
    (0, 0), "character/roosevelt/roosevelt_bored1.png")

image roosevelt happy = LiveComposite(
    (900, 1020),
    (0, 0), "character/roosevelt/roosevelt_base1.png",
    (0, 0), "character/roosevelt/roosevelt_happy1.png")

image roosevelt normal = LiveComposite(
    (900, 1020),
    (0, 0), "character/roosevelt/roosevelt_base1.png",
    (0, 0), "character/roosevelt/roosevelt_normal1.png")

image roosevelt moe1 = LiveComposite(
    (900, 1020),
    (0, 0), "character/roosevelt/roosevelt_base1.png",
    (0, 0), "character/roosevelt/roosevelt_moe11.png")

image roosevelt moe2 = LiveComposite(
    (900, 1020),
    (0, 0), "character/roosevelt/roosevelt_base1.png",
    (0, 0), "character/roosevelt/roosevelt_moe21.png",
    (248, 59), "roosevelt_crown")

image roosevelt annoyed large = "character/roosevelt/roosevelt_annoyed1_large.png"
image roosevelt bored large = "character/roosevelt/roosevelt_bored1_large.png"
image roosevelt happy large = "character/roosevelt/roosevelt_happy1_large.png"
image roosevelt normal large = "character/roosevelt/roosevelt_normal1_large.png"
image roosevelt evil large = "character/roosevelt/roosevelt_evil1_large.png"
image roosevelt moe1 large = "character/roosevelt/roosevelt_moe11_large.png"
image roosevelt moe2 large = "character/roosevelt/roosevelt_moe21_large.png"

image side roosevelt annoyed = LiveCrop((250, 90, 350, 210), LiveComposite((900, 1020), (0, 0), im.Sepia("character/roosevelt/roosevelt_base1.png"), (0, 0), im.Sepia("character/roosevelt/roosevelt_annoyed1.png")))
image side roosevelt bored = LiveCrop((250, 90, 350, 210), LiveComposite((900, 1020), (0, 0), im.Sepia("character/roosevelt/roosevelt_base1.png"), (0, 0), im.Sepia("character/roosevelt/roosevelt_bored1.png")))
image side roosevelt moe1 = LiveCrop((250, 90, 350, 210), LiveComposite((900, 1020), (0, 0), im.Sepia("character/roosevelt/roosevelt_base1.png"), (0, 0), im.Sepia("character/roosevelt/roosevelt_moe11.png")))
image side roosevelt moe2 = LiveCrop((250, 90, 350, 210), LiveComposite((900, 1020), (0, 0), im.Sepia("character/roosevelt/roosevelt_base1.png"), (0, 0), im.Sepia("character/roosevelt/roosevelt_moe21.png")))
image side roosevelt happy = LiveCrop((250, 90, 350, 210), LiveComposite((900, 1020), (0, 0), im.Sepia("character/roosevelt/roosevelt_base1.png"), (0, 0), im.Sepia("character/roosevelt/roosevelt_happy1.png")))
image side roosevelt normal = LiveCrop((250, 90, 350, 210), LiveComposite((900, 1020), (0, 0), im.Sepia("character/roosevelt/roosevelt_base1.png"), (0, 0), im.Sepia("character/roosevelt/roosevelt_normal1.png")))
image side roosevelt evil = LiveCrop((250, 90, 350, 210), LiveComposite((900, 1020), (0, 0), im.Sepia("character/roosevelt/roosevelt_base1.png"), (0, 0), im.Sepia("character/roosevelt/roosevelt_evil1.png")))

########################################################
# Hirahita ###############################################
########################################################
image hirahita angry = LiveComposite(
    (891, 1190),
    (30, 0), "character/hirahita/hirahita_base1.png",
    (30, 0), "character/hirahita/hirahita_angry1.png")

image hirahita annoyed = LiveComposite(
    (891, 1190),
    (30, 0), "character/hirahita/hirahita_base1.png",
    (30, 0), "character/hirahita/hirahita_annoyed1.png")

image hirahita happy = LiveComposite(
    (891, 1190),
    (30, 0), "character/hirahita/hirahita_base1.png",
    (30, 0), "character/hirahita/hirahita_happy1.png")

image hirahita moe1 = LiveComposite(
    (891, 1190),
    (30, 0), "character/hirahita/hirahita_base1.png",
    (30, 0), "character/hirahita/hirahita_moe11.png",
    (230, 350), "hirahita_crown")

image hirahita moe2 = LiveComposite(
    (891, 1190),
    (30, 0), "character/hirahita/hirahita_base1.png",
    (30, 0), "character/hirahita/hirahita_moe21.png")

image hirahita shock = LiveComposite(
    (891, 1190),
    (30, 0), "character/hirahita/hirahita_base1.png",
    (30, 0), "character/hirahita/hirahita_shock1.png")

image hirahita normal = LiveComposite(
    (891, 1190),
    (30, 0), "character/hirahita/hirahita_base1.png",
    (30, 0), "character/hirahita/hirahita_normal1.png")

image side hirahita annoyed = LiveCrop((235, 320, 350, 210), LiveComposite((891, 1190), (0, 0), im.Sepia("character/hirahita/hirahita_base1.png"), (0, 0), im.Sepia("character/hirahita/hirahita_annoyed1.png")))
image side hirahita happy = LiveCrop((235, 320, 350, 210), LiveComposite((891, 1190), (0, 0), im.Sepia("character/hirahita/hirahita_base1.png"), (0, 0), im.Sepia("character/hirahita/hirahita_happy1.png")))
image side hirahita moe1 = LiveCrop((235, 320, 350, 210), LiveComposite((891, 1190), (0, 0), im.Sepia("character/hirahita/hirahita_base1.png"), (0, 0), im.Sepia("character/hirahita/hirahita_moe11.png")))
image side hirahita moe2 = LiveCrop((235, 320, 350, 210), LiveComposite((891, 1190), (0, 0), im.Sepia("character/hirahita/hirahita_base1.png"), (0, 0), im.Sepia("character/hirahita/hirahita_moe21.png")))
image side hirahita shock = LiveCrop((235, 320, 350, 210), LiveComposite((891, 1190), (0, 0), im.Sepia("character/hirahita/hirahita_base1.png"), (0, 0), im.Sepia("character/hirahita/hirahita_shock1.png")))
image side hirahita normal = LiveCrop((235, 320, 350, 210), LiveComposite((891, 1190), (0, 0), im.Sepia("character/hirahita/hirahita_base1.png"), (0, 0), im.Sepia("character/hirahita/hirahita_normal1.png")))
image side hirahita angry = LiveCrop((235, 320, 350, 210), LiveComposite((891, 1190), (0, 0), im.Sepia("character/hirahita/hirahita_base1.png"), (0, 0), im.Sepia("character/hirahita/hirahita_angry1.png")))

########################################################
# Joebbels ###############################################
########################################################
image joebbels evil = LiveComposite(
    (500, 890),
    (40, 0), "character/joebbels/joebbels_base1.png",
    (40, 0), "character/joebbels/joebbels_evil1.png")

image joebbels normal = LiveComposite(
    (500, 890),
    (40, 0), "character/joebbels/joebbels_base1.png",
    (40, 0), "character/joebbels/joebbels_normal1.png")

image joebbels happy = LiveComposite(
    (500, 890),
    (40, 0), "character/joebbels/joebbels_base1.png",
    (40, 0), "character/joebbels/joebbels_happy1.png")

image joebbels sad = LiveComposite(
    (500, 890),
    (40, 0), "character/joebbels/joebbels_base1.png",
    (40, 0), "character/joebbels/joebbels_sad1.png")

image joebbels scared = LiveComposite(
    (500, 890),
    (40, 0), "character/joebbels/joebbels_base2.png",
    (40, 0), "character/joebbels/joebbels_scared1.png")

image joebbels scared large = "character/joebbels/joebbels_scared1_large.png"

image joebbels ko:
    contains:
        "joebbels scared large"
        alpha 0.8
        yalign 1.0
        xalign 0.5
        linear 1.0 xalign 0.55
        linear 2.0 xalign 0.45
        linear 1.0 xalign 0.5
        repeat
    contains:
        "joebbels scared large"
        alpha .2
        xalign 0.5
        yalign 1.0
        linear 2.0 xalign 0.55
        linear 2.0 xalign 0.6
        linear 2.0 xalign 0.55
        linear 2.0 xalign 0.5
        linear 2.0 xalign 0.45
        linear 2.0 xalign 0.4
        linear 2.0 xalign 0.45
        linear 2.0 xalign 0.5
        repeat
    contains:
        "joebbels scared large"
        alpha .2
        xalign 0.5
        yalign 1.0
        linear 2.0 xalign 0.45
        linear 2.0 xalign 0.4
        linear 2.0 xalign 0.45
        linear 2.0 xalign 0.5
        linear 2.0 xalign 0.55
        linear 2.0 xalign 0.6
        linear 2.0 xalign 0.55
        linear 2.0 xalign 0.5
        repeat

image side joebbels evil = LiveCrop((20, 140, 350, 210), LiveComposite((500, 890), (0, 0), im.Sepia("character/joebbels/joebbels_base1.png"), (0, 0), im.Sepia("character/joebbels/joebbels_evil1.png")))
image side joebbels normal = LiveCrop((20, 140, 350, 210), LiveComposite((500, 890), (0, 0), im.Sepia("character/joebbels/joebbels_base1.png"), (0, 0), im.Sepia("character/joebbels/joebbels_normal1.png")))
image side joebbels happy = LiveCrop((20, 140, 350, 210), LiveComposite((500, 890), (0, 0), im.Sepia("character/joebbels/joebbels_base1.png"), (0, 0), im.Sepia("character/joebbels/joebbels_happy1.png")))
image side joebbels sad = LiveCrop((20, 140, 350, 210), LiveComposite((500, 890), (0, 0), im.Sepia("character/joebbels/joebbels_base1.png"), (0, 0), im.Sepia("character/joebbels/joebbels_sad1.png")))
image side joebbels scared = LiveCrop((20, 140, 350, 210), LiveComposite((500, 890), (0, 0), im.Sepia("character/joebbels/joebbels_base2.png"), (0, 0), im.Sepia("character/joebbels/joebbels_scared1.png")))
image side joebbels ko = LiveCrop((20, 140, 350, 210), LiveComposite((500, 890), (0, 0), im.Sepia("character/joebbels/joebbels_base1.png"), (0, 0), im.Sepia("character/joebbels/joebbels_sad1.png")))

########################################################
# Goring ###############################################
########################################################
image goring pout = LiveComposite(
    (600, 990),
    (0, 0), "character/goring/goring_base1.png",
    (0, 0), "character/goring/goring_pout1.png")

image goring determined = LiveComposite(
    (600, 990),
    (0, 0), "character/goring/goring_base1.png",
    (0, 0), "character/goring/goring_determined1.png")

image goring happy = LiveComposite(
    (600, 990),
    (0, 0), "character/goring/goring_base1.png",
    (0, 0), "character/goring/goring_happy1.png")

image goring confused = LiveComposite(
    (600, 990),
    (0, 0), "character/goring/goring_base1.png",
    (0, 0), "character/goring/goring_confused1.png")

image goring ko:
    contains:
        "goring confused"
        yalign 1.0
        xalign 0.5
        linear 3.0 xalign 0.6
        linear 6.0 xalign 0.4
        linear 3.0 xalign 0.5
        repeat
    contains:
        "goring confused"
        alpha .2
        xalign 0.5
        yalign 1.0
        linear 2.0 xalign 0.7 zoom 1.1
        linear 2.0 xalign 0.9 zoom 1.2
        linear 2.0 xalign 0.7 zoom 1.1
        linear 2.0 xalign 0.5 zoom 1.0
        linear 2.0 xalign 0.3 zoom 1.1
        linear 2.0 xalign 0.1 zoom 1.2
        linear 2.0 xalign 0.3 zoom 1.1
        linear 2.0 xalign 0.5 zoom 1.0
        repeat
    contains:
        "goring confused"
        alpha .2
        xalign 0.5
        yalign 1.0
        linear 2.0 xalign 0.3 zoom 1.2
        linear 2.0 xalign 0.1 zoom 1.1
        linear 2.0 xalign 0.3 zoom 1.0
        linear 2.0 xalign 0.5 zoom 1.1
        linear 2.0 xalign 0.7 zoom 1.2
        linear 2.0 xalign 0.9 zoom 1.1
        linear 2.0 xalign 0.7 zoom 1.0
        linear 2.0 xalign 0.5 zoom 1.1
        repeat

image side goring pout = LiveCrop((140, 80, 350, 210), LiveComposite((600, 990), (0, 0), im.Sepia("character/goring/goring_base1.png"), (0, 0), im.Sepia("character/goring/goring_pout1.png")))
image side goring determined = LiveCrop((140, 80, 350, 210), LiveComposite((600, 990), (0, 0), im.Sepia("character/goring/goring_base1.png"), (0, 0), im.Sepia("character/goring/goring_determined1.png")))
image side goring happy = LiveCrop((140, 80, 350, 210), LiveComposite((600, 990), (0, 0), im.Sepia("character/goring/goring_base1.png"), (0, 0), im.Sepia("character/goring/goring_happy1.png")))
image side goring confused = LiveCrop((140, 80, 350, 210), LiveComposite((600, 990), (0, 0), im.Sepia("character/goring/goring_base1.png"), (0, 0), im.Sepia("character/goring/goring_confused1.png")))
image side goring ko = LiveCrop((140, 80, 350, 210), LiveComposite((600, 990), (0, 0), im.Sepia("character/goring/goring_base1.png"), (0, 0), im.Sepia("character/goring/goring_confused1.png")))


########################################################
# Dunitz ###############################################
########################################################
image dunitz bored = LiveComposite(
    (580, 990),
    (0, 0), "character/dunitz/dunitz_base1.png",
    (0, 0), "character/dunitz/dunitz_bored1.png")

image dunitz happy = LiveComposite(
    (580, 990),
    (0, 0), "character/dunitz/dunitz_base1.png",
    (0, 0), "character/dunitz/dunitz_happy1.png")

image dunitz determined = LiveComposite(
    (580, 990),
    (0, 0), "character/dunitz/dunitz_base1.png",
    (0, 0), "character/dunitz/dunitz_determined1.png")

image dunitz angry = LiveComposite(
    (580, 990),
    (0, 0), "character/dunitz/dunitz_base1.png",
    (0, 0), "character/dunitz/dunitz_angry1.png")

image dunitz shiver:
    contains:
        "dunitz angry"
        xalign 0.5
        yalign 1.0
        linear 0.03 xalign 0.498
        linear 0.03 xalign 0.5
        linear 0.03 xalign 0.502
        linear 0.03 xalign 0.5
        repeat

image side dunitz determined = LiveCrop((120, 60, 350, 210), LiveComposite((900, 1060), (0, 0), im.Sepia("character/dunitz/dunitz_base1.png"), (0, 0), im.Sepia("character/dunitz/dunitz_determined1.png")))
image side dunitz happy = LiveCrop((120, 60, 350, 210), LiveComposite((900, 1060), (0, 0), im.Sepia("character/dunitz/dunitz_base1.png"), (0, 0), im.Sepia("character/dunitz/dunitz_happy1.png")))
image side dunitz bored = LiveCrop((120, 60, 350, 210), LiveComposite((900, 1060), (0, 0), im.Sepia("character/dunitz/dunitz_base1.png"), (0, 0), im.Sepia("character/dunitz/dunitz_bored1.png")))
image side dunitz angry = LiveCrop((120, 60, 350, 210), LiveComposite((900, 1060), (0, 0), im.Sepia("character/dunitz/dunitz_base1.png"), (0, 0), im.Sepia("character/dunitz/dunitz_angry1.png")))
image side dunitz shiver = LiveCrop((120, 60, 350, 210), LiveComposite((900, 1060), (0, 0), im.Sepia("character/dunitz/dunitz_base1.png"), (0, 0), im.Sepia("character/dunitz/dunitz_angry1.png")))
    
########################################################
# Guderian ###############################################
########################################################    
image guderian moe = LiveComposite(
    (616, 920),
    (40, 0), "character/guderian/guderian_base1.png",
    (40, 0), "character/guderian/guderian_moe1.png")

image guderian normal = LiveComposite(
    (616, 920),
    (40, 0), "character/guderian/guderian_base1.png",
    (40, 0), "character/guderian/guderian_normal1.png")

image guderian happy = LiveComposite(
    (616, 920),
    (40, 0), "character/guderian/guderian_base1.png",
    (40, 0), "character/guderian/guderian_happy1.png")

image guderian determined = LiveComposite(
    (616, 920),
    (40, 0), "character/guderian/guderian_base1.png",
    (40, 0), "character/guderian/guderian_determined1.png")

image guderian shock = LiveComposite(
    (616, 920),
    (40, 0), "character/guderian/guderian_base1.png",
    (40, 0), "character/guderian/guderian_shock1.png")

image guderian tank determined:
    "guderian determined"
    ypos 1.0
    linear 0.5 ypos 1.02
    linear 0.5 ypos 1.0
    repeat
    
image guderian tank normal:
    "guderian normal"
    ypos 1.0
    linear 0.5 ypos 1.02
    linear 0.5 ypos 1.0
    repeat
    
image guderian tank happy:
    "guderian happy"
    ypos 1.0
    linear 0.5 ypos 1.02
    linear 0.5 ypos 1.0
    repeat
    
image guderian tank moe:
    "guderian moe"
    ypos 1.0
    linear 0.5 ypos 1.02
    linear 0.5 ypos 1.0
    repeat
    
image guderian tank shock:
    "guderian shock"
    ypos 1.0
    linear 0.5 ypos 1.02
    linear 0.5 ypos 1.0
    repeat
    
image guderian ski happy:
    "guderian happy"
    xalign 0.25 yalign 1.0
    linear 0.15 yalign 1.2
    linear 0.15 yalign 1.0
    repeat

image side guderian moe = LiveCrop((105, 100, 350, 210), LiveComposite((616, 920), (0, 0), im.Sepia("character/guderian/guderian_base1.png"), (0, 0), im.Sepia("character/guderian/guderian_moe1.png")))
image side guderian normal = LiveCrop((105, 100, 350, 210), LiveComposite((616, 920), (0, 0), im.Sepia("character/guderian/guderian_base1.png"), (0, 0), im.Sepia("character/guderian/guderian_normal1.png")))
image side guderian happy = LiveCrop((105, 100, 350, 210), LiveComposite((616, 920), (0, 0), im.Sepia("character/guderian/guderian_base1.png"), (0, 0), im.Sepia("character/guderian/guderian_happy1.png")))
image side guderian determined = LiveCrop((105, 100, 350, 210), LiveComposite((616, 920), (0, 0), im.Sepia("character/guderian/guderian_base1.png"), (0, 0), im.Sepia("character/guderian/guderian_determined1.png")))
image side guderian shock = LiveCrop((105, 100, 350, 210), LiveComposite((616, 920), (0, 0), im.Sepia("character/guderian/guderian_base1.png"), (0, 0), im.Sepia("character/guderian/guderian_shock1.png")))
image side guderian tank moe = LiveCrop((105, 100, 350, 210), LiveComposite((616, 920), (0, 0), im.Sepia("character/guderian/guderian_base1.png"), (0, 0), im.Sepia("character/guderian/guderian_moe1.png")))
image side guderian tank normal = LiveCrop((105, 100, 350, 210), LiveComposite((616, 920), (0, 0), im.Sepia("character/guderian/guderian_base1.png"), (0, 0), im.Sepia("character/guderian/guderian_normal1.png")))
image side guderian tank happy = LiveCrop((105, 100, 350, 210), LiveComposite((616, 920), (0, 0), im.Sepia("character/guderian/guderian_base1.png"), (0, 0), im.Sepia("character/guderian/guderian_happy1.png")))
image side guderian tank determined = LiveCrop((105, 100, 350, 210), LiveComposite((616, 920), (0, 0), im.Sepia("character/guderian/guderian_base1.png"), (0, 0), im.Sepia("character/guderian/guderian_determined1.png")))
image side guderian tank shock = LiveCrop((105, 100, 350, 210), LiveComposite((616, 920), (0, 0), im.Sepia("character/guderian/guderian_base1.png"), (0, 0), im.Sepia("character/guderian/guderian_shock1.png")))
image side guderian ski happy = LiveCrop((105, 100, 350, 210), LiveComposite((616, 920), (0, 0), im.Sepia("character/guderian/guderian_base1.png"), (0, 0), im.Sepia("character/guderian/guderian_happy1.png")))

########################################################
# Tito ###############################################
########################################################
image tito normal = LiveComposite(
    (600, 820),
    (50, 0), "character/tito/tito_base1.png",
    (50, 0), "character/tito/tito_normal1.png")

image tito happy = LiveComposite(
    (600, 820),
    (50, 0), "character/tito/tito_base1.png",
    (50, 0), "character/tito/tito_happy1.png")

image tito determined = LiveComposite(
    (600, 820),
    (50, 0), "character/tito/tito_base1.png",
    (50, 0), "character/tito/tito_determined1.png")

image tito moe = LiveComposite(
    (600, 820),
    (50, 0), "character/tito/tito_base1.png",
    (50, 0), "character/tito/tito_moe1.png")

image tito shock = LiveComposite(
    (600, 820),
    (50, 0), "character/tito/tito_base1.png",
    (50, 0), "character/tito/tito_shock1.png")

image side tito determined = LiveCrop((80, 34, 350, 210), LiveComposite((600, 820), (0, 0), im.Sepia("character/tito/tito_base1.png"), (0, 0), im.Sepia("character/tito/tito_determined1.png")))
image side tito happy = LiveCrop((80, 34, 350, 210), LiveComposite((600, 820), (0, 0), im.Sepia("character/tito/tito_base1.png"), (0, 0), im.Sepia("character/tito/tito_happy1.png")))
image side tito normal = LiveCrop((80, 34, 350, 210), LiveComposite((600, 820), (0, 0), im.Sepia("character/tito/tito_base1.png"), (0, 0), im.Sepia("character/tito/tito_normal1.png")))
image side tito moe = LiveCrop((80, 34, 350, 210), LiveComposite((600, 820), (0, 0), im.Sepia("character/tito/tito_base1.png"), (0, 0), im.Sepia("character/tito/tito_moe1.png")))
image side tito shock = LiveCrop((80, 34, 350, 210), LiveComposite((600, 820), (0, 0), im.Sepia("character/tito/tito_base1.png"), (0, 0), im.Sepia("character/tito/tito_shock1.png")))

########################################################
# Mannerheim ###############################################
########################################################
image mannerheim normal = LiveComposite(
    (750, 990),
    (0, 0), "character/mannerheim/mannerheim_base1.png",
    (0, 0), "character/mannerheim/mannerheim_normal1.png")

image mannerheim happy = LiveComposite(
    (750, 990),
    (0, 0), "character/mannerheim/mannerheim_base1.png",
    (0, 0), "character/mannerheim/mannerheim_happy1.png")

image mannerheim determined = LiveComposite(
    (750, 990),
    (0, 0), "character/mannerheim/mannerheim_base1.png",
    (0, 0), "character/mannerheim/mannerheim_determined1.png")

image mannerheim moe = LiveComposite(
    (750, 990),
    (0, 0), "character/mannerheim/mannerheim_base1.png",
    (0, 0), "character/mannerheim/mannerheim_moe1.png")

image mannerheim shock = LiveComposite(
    (750, 990),
    (0, 0), "character/mannerheim/mannerheim_base1.png",
    (0, 0), "character/mannerheim/mannerheim_shock1.png")

image side mannerheim determined = LiveCrop((190, 120, 350, 210), LiveComposite((620, 960), (0, 0), im.Sepia("character/mannerheim/mannerheim_base1.png"), (0, 0), im.Sepia("character/mannerheim/mannerheim_determined1.png")))
image side mannerheim happy = LiveCrop((190, 120, 350, 210), LiveComposite((620, 960), (0, 0), im.Sepia("character/mannerheim/mannerheim_base1.png"), (0, 0), im.Sepia("character/mannerheim/mannerheim_happy1.png")))
image side mannerheim normal = LiveCrop((190, 120, 350, 210), LiveComposite((620, 960), (0, 0), im.Sepia("character/mannerheim/mannerheim_base1.png"), (0, 0), im.Sepia("character/mannerheim/mannerheim_normal1.png")))
image side mannerheim moe = LiveCrop((190, 120, 350, 210), LiveComposite((620, 960), (0, 0), im.Sepia("character/mannerheim/mannerheim_base1.png"), (0, 0), im.Sepia("character/mannerheim/mannerheim_moe1.png")))
image side mannerheim shock = LiveCrop((190, 120, 350, 210), LiveComposite((620, 960), (0, 0), im.Sepia("character/mannerheim/mannerheim_base1.png"), (0, 0), im.Sepia("character/mannerheim/mannerheim_shock1.png")))

########################################################
# Badoglio ###############################################
########################################################
image badoglio hat determined = LiveComposite(
    (488, 1023),
    (-10, 0), "character/badoglio/badoglio_base1.png",
    (-10, 0), "character/badoglio/badoglio_determined1.png")

image badoglio hat happy = LiveComposite(
    (488, 1023),
    (-10, 0), "character/badoglio/badoglio_base1.png",
    (-10, 0), "character/badoglio/badoglio_happy1.png")

image badoglio hat moe = LiveComposite(
    (488, 1023),
    (-10, 0), "character/badoglio/badoglio_base1.png",
    (-10, 0), "character/badoglio/badoglio_moe1.png")

image badoglio hat shock = LiveComposite(
    (488, 1023),
    (-10, 0), "character/badoglio/badoglio_base1.png",
    (-10, 0), "character/badoglio/badoglio_shock1.png")

image badoglio hat normal = LiveComposite(
    (488, 1023),
    (-10, 0), "character/badoglio/badoglio_base1.png",
    (-10, 0), "character/badoglio/badoglio_normal1.png")

image side badoglio hat determined = LiveCrop((75, 110, 350, 210), LiveComposite((488, 1023), (0, 0), im.Sepia("character/badoglio/badoglio_base1.png"), (0, 0), im.Sepia("character/badoglio/badoglio_determined1.png")))
image side badoglio hat happy = LiveCrop((75, 110, 350, 210), LiveComposite((488, 1023), (0, 0), im.Sepia("character/badoglio/badoglio_base1.png"), (0, 0), im.Sepia("character/badoglio/badoglio_happy1.png")))
image side badoglio hat moe = LiveCrop((75, 110, 350, 210), LiveComposite((488, 1023), (0, 0), im.Sepia("character/badoglio/badoglio_base1.png"), (0, 0), im.Sepia("character/badoglio/badoglio_moe1.png")))
image side badoglio hat shock = LiveCrop((75, 110, 350, 210), LiveComposite((488, 1023), (0, 0), im.Sepia("character/badoglio/badoglio_base1.png"), (0, 0), im.Sepia("character/badoglio/badoglio_shock1.png")))
image side badoglio hat normal = LiveCrop((75, 110, 350, 210), LiveComposite((488, 1023), (0, 0), im.Sepia("character/badoglio/badoglio_base1.png"), (0, 0), im.Sepia("character/badoglio/badoglio_normal1.png")))

########################################################
# Dresckow ###############################################
########################################################
image dresckow normal = LiveComposite(
    (691, 1019),
    (15, 0), "character/dresckow/dresckow_base1.png",
    (15, 0), "character/dresckow/dresckow_normal1.png")

image dresckow angry = LiveComposite(
    (691, 1019),
    (15, 0), "character/dresckow/dresckow_base1.png",
    (15, 0), "character/dresckow/dresckow_angry1.png")

image dresckow determined = LiveComposite(
    (691, 1019),
    (15, 0), "character/dresckow/dresckow_base1.png",
    (15, 0), "character/dresckow/dresckow_determined1.png")

image dresckow happy = LiveComposite(
    (691, 1019),
    (15, 0), "character/dresckow/dresckow_base1.png",
    (15, 0), "character/dresckow/dresckow_happy1.png")

image dresckow shock = LiveComposite(
    (691, 1019),
    (15, 0), "character/dresckow/dresckow_base1.png",
    (15, 0), "character/dresckow/dresckow_shock1.png")

image dresckow spin = At("dresckow shock", rotater_anim2)

image side dresckow normal = LiveCrop((140, 60, 350, 210), LiveComposite((691, 1019), (0, 0), im.Sepia("character/dresckow/dresckow_base1.png"), (0, 0), im.Sepia("character/dresckow/dresckow_normal1.png")))
image side dresckow angry = LiveCrop((140, 60, 350, 210), LiveComposite((691, 1019), (0, 0), im.Sepia("character/dresckow/dresckow_base1.png"), (0, 0), im.Sepia("character/dresckow/dresckow_angry1.png")))
image side dresckow determined = LiveCrop((140, 60, 350, 210), LiveComposite((691, 1019), (0, 0), im.Sepia("character/dresckow/dresckow_base1.png"), (0, 0), im.Sepia("character/dresckow/dresckow_determined1.png")))
image side dresckow happy = LiveCrop((140, 60, 350, 210), LiveComposite((691, 1019), (0, 0), im.Sepia("character/dresckow/dresckow_base1.png"), (0, 0), im.Sepia("character/dresckow/dresckow_happy1.png")))
image side dresckow shock = LiveCrop((140, 60, 350, 210), LiveComposite((691, 1019), (0, 0), im.Sepia("character/dresckow/dresckow_base1.png"), (0, 0), im.Sepia("character/dresckow/dresckow_shock1.png")))


########################################################
# Kalinesgu ###############################################
########################################################
image side kalinesgu normal = LiveCrop((110, 70, 350, 210), LiveComposite((560, 970), (0, 0), im.Sepia("character/politician/politician_normal2.png")))
image side kalinesgu happy = LiveCrop((110, 70, 350, 210), LiveComposite((560, 970), (0, 0), im.Sepia("character/politician/politician_happy2.png")))
image side kalinesgu determined = LiveCrop((110, 70, 350, 210), LiveComposite((560, 970), (0, 0), im.Sepia("character/politician/politician_determined2.png")))
image side kalinesgu shock = LiveCrop((110, 70, 350, 210), LiveComposite((560, 970), (0, 0), im.Sepia("character/politician/politician_shock2.png")))

########################################################
# Horthy ###############################################
########################################################
image horthy normal = LiveComposite(
    (620, 950),
    (0, 0), "character/horthy/horthy_base1.png",
    (0, 0), "character/horthy/horthy_normal1.png")

image horthy happy = LiveComposite(
    (620, 950),
    (0, 0), "character/horthy/horthy_base1.png",
    (0, 0), "character/horthy/horthy_happy1.png")

image horthy determined = LiveComposite(
    (620, 950),
    (0, 0), "character/horthy/horthy_base1.png",
    (0, 0), "character/horthy/horthy_determined1.png")

image horthy moe = LiveComposite(
    (620, 950),
    (0, 0), "character/horthy/horthy_base1.png",
    (0, 0), "character/horthy/horthy_moe1.png")

image horthy shock = LiveComposite(
    (620, 950),
    (0, 0), "character/horthy/horthy_base1.png",
    (0, 0), "character/horthy/horthy_shock1.png")

image side horthy determined = LiveCrop((90, 220, 350, 210), LiveComposite((620, 950), (0, 0), im.Sepia("character/horthy/horthy_base1.png"), (0, 0), im.Sepia("character/horthy/horthy_determined1.png")))
image side horthy happy = LiveCrop((90, 220, 350, 210), LiveComposite((620, 950), (0, 0), im.Sepia("character/horthy/horthy_base1.png"), (0, 0), im.Sepia("character/horthy/horthy_happy1.png")))
image side horthy normal = LiveCrop((90, 220, 350, 210), LiveComposite((620, 950), (0, 0), im.Sepia("character/horthy/horthy_base1.png"), (0, 0), im.Sepia("character/horthy/horthy_normal1.png")))
image side horthy moe = LiveCrop((90, 220, 350, 210), LiveComposite((620, 950), (0, 0), im.Sepia("character/horthy/horthy_base1.png"), (0, 0), im.Sepia("character/horthy/horthy_moe1.png")))
image side horthy shock = LiveCrop((90, 220, 350, 210), LiveComposite((620, 950), (0, 0), im.Sepia("character/horthy/horthy_base1.png"), (0, 0), im.Sepia("character/horthy/horthy_shock1.png")))

########################################################
# Smigly ###############################################
########################################################
image smigly normal = LiveComposite(
    (720, 990),
    (0, 0), "character/smigly/smigly_base1.png",
    (0, 0), "character/smigly/smigly_normal1.png")

image smigly happy = LiveComposite(
    (720, 990),
    (0, 0), "character/smigly/smigly_base1.png",
    (0, 0), "character/smigly/smigly_happy1.png")

image smigly determined = LiveComposite(
    (720, 990),
    (0, 0), "character/smigly/smigly_base1.png",
    (0, 0), "character/smigly/smigly_determined1.png")

image smigly moe = LiveComposite(
    (720, 990),
    (0, 0), "character/smigly/smigly_base1.png",
    (0, 0), "character/smigly/smigly_moe1.png")

image smigly shock = LiveComposite(
    (720, 990),
    (0, 0), "character/smigly/smigly_base1.png",
    (0, 0), "character/smigly/smigly_shock1.png")

image side smigly determined = LiveCrop((200, 120, 350, 210), LiveComposite((700, 990), (0, 0), im.Sepia("character/smigly/smigly_base1.png"), (0, 0), im.Sepia("character/smigly/smigly_determined1.png")))
image side smigly happy = LiveCrop((200, 120, 350, 210), LiveComposite((700, 990), (0, 0), im.Sepia("character/smigly/smigly_base1.png"), (0, 0), im.Sepia("character/smigly/smigly_happy1.png")))
image side smigly normal = LiveCrop((200, 120, 350, 210), LiveComposite((700, 990), (0, 0), im.Sepia("character/smigly/smigly_base1.png"), (0, 0), im.Sepia("character/smigly/smigly_normal1.png")))
image side smigly moe = LiveCrop((200, 120, 350, 210), LiveComposite((700, 990), (0, 0), im.Sepia("character/smigly/smigly_base1.png"), (0, 0), im.Sepia("character/smigly/smigly_moe1.png")))
image side smigly shock = LiveCrop((200, 120, 350, 210), LiveComposite((700, 990), (0, 0), im.Sepia("character/smigly/smigly_base1.png"), (0, 0), im.Sepia("character/smigly/smigly_shock1.png")))

########################################################
# Stuffy ###############################################
########################################################
image stuffy normal = LiveComposite(
    (570, 930),
    (0, 0), "character/stuffy/stuffy_base1.png",
    (0, 0), "character/stuffy/stuffy_normal1.png")

image stuffy determined = LiveComposite(
    (570, 930),
    (0, 0), "character/stuffy/stuffy_base1.png",
    (0, 0), "character/stuffy/stuffy_determined1.png")

image stuffy happy = LiveComposite(
    (570, 930),
    (0, 0), "character/stuffy/stuffy_base1.png",
    (0, 0), "character/stuffy/stuffy_happy1.png")

image stuffy moe = LiveComposite(
    (570, 930),
    (0, 0), "character/stuffy/stuffy_base1.png",
    (0, 0), "character/stuffy/stuffy_moe1.png")

image stuffy shock = LiveComposite(
    (570, 930),
    (0, 0), "character/stuffy/stuffy_base1.png",
    (0, 0), "character/stuffy/stuffy_shock1.png")

image side stuffy normal = LiveCrop((120, 110, 350, 210), LiveComposite((570, 930), (0, 0), im.Sepia("character/stuffy/stuffy_base1.png"), (0, 0), im.Sepia("character/stuffy/stuffy_normal1.png")))
image side stuffy determined = LiveCrop((120, 110, 350, 210), LiveComposite((570, 930), (0, 0), im.Sepia("character/stuffy/stuffy_base1.png"), (0, 0), im.Sepia("character/stuffy/stuffy_determined1.png")))
image side stuffy happy = LiveCrop((120, 110, 350, 210), LiveComposite((570, 930), (0, 0), im.Sepia("character/stuffy/stuffy_base1.png"), (0, 0), im.Sepia("character/stuffy/stuffy_happy1.png")))
image side stuffy moe = LiveCrop((120, 110, 350, 210), LiveComposite((570, 930), (0, 0), im.Sepia("character/stuffy/stuffy_base1.png"), (0, 0), im.Sepia("character/stuffy/stuffy_moe1.png")))
image side stuffy shock = LiveCrop((120, 110, 350, 210), LiveComposite((570, 930), (0, 0), im.Sepia("character/stuffy/stuffy_base1.png"), (0, 0), im.Sepia("character/stuffy/stuffy_shock1.png")))

########################################################
# Battenia ###############################################
########################################################
image battenia normal = LiveComposite(
    (640, 1019),
    (0, 0), "character/battenia/battenia_base1.png",
    (0, 0), "character/battenia/battenia_normal1.png")

image battenia angry = LiveComposite(
    (640, 1019),
    (0, 0), "character/battenia/battenia_base1.png",
    (0, 0), "character/battenia/battenia_angry1.png")

image battenia happy = LiveComposite(
    (640, 1019),
    (0, 0), "character/battenia/battenia_base1.png",
    (0, 0), "character/battenia/battenia_happy1.png")

image battenia moe = LiveComposite(
    (640, 1019),
    (0, 0), "character/battenia/battenia_base1.png",
    (0, 0), "character/battenia/battenia_moe1.png")

image battenia shock = LiveComposite(
    (640, 1019),
    (0, 0), "character/battenia/battenia_base1.png",
    (0, 0), "character/battenia/battenia_shock1.png")

image side battenia normal = LiveCrop((130, 150, 350, 210), LiveComposite((640, 1019), (0, 0), im.Sepia("character/battenia/battenia_base1.png"), (0, 0), im.Sepia("character/battenia/battenia_normal1.png")))
image side battenia angry = LiveCrop((130, 150, 350, 210), LiveComposite((640, 1019), (0, 0), im.Sepia("character/battenia/battenia_base1.png"), (0, 0), im.Sepia("character/battenia/battenia_angry1.png")))
image side battenia happy = LiveCrop((130, 150, 350, 210), LiveComposite((640, 1019), (0, 0), im.Sepia("character/battenia/battenia_base1.png"), (0, 0), im.Sepia("character/battenia/battenia_happy1.png")))
image side battenia moe = LiveCrop((130, 150, 350, 210), LiveComposite((640, 1019), (0, 0), im.Sepia("character/battenia/battenia_base1.png"), (0, 0), im.Sepia("character/battenia/battenia_moe1.png")))
image side battenia shock = LiveCrop((130, 150, 350, 210), LiveComposite((640, 1019), (0, 0), im.Sepia("character/battenia/battenia_base1.png"), (0, 0), im.Sepia("character/battenia/battenia_shock1.png")))

########################################################
# Manstein ###############################################
########################################################
image manstein normal = LiveComposite(
    (470, 1019),
    (0, 0), "character/manstein/manstein_base1.png",
    (0, 0), "character/manstein/manstein_normal1.png")

image manstein determined = LiveComposite(
    (470, 1019),
    (0, 0), "character/manstein/manstein_base1.png",
    (0, 0), "character/manstein/manstein_determined1.png")

image manstein happy = LiveComposite(
    (470, 1019),
    (0, 0), "character/manstein/manstein_base1.png",
    (0, 0), "character/manstein/manstein_happy1.png")

image manstein moe = LiveComposite(
    (470, 1019),
    (0, 0), "character/manstein/manstein_base1.png",
    (0, 0), "character/manstein/manstein_moe1.png")

image manstein shock = LiveComposite(
    (470, 1019),
    (0, 0), "character/manstein/manstein_base1.png",
    (0, 0), "character/manstein/manstein_shock1.png")

image side manstein normal = LiveCrop((55, 130, 350, 210), LiveComposite((470, 1019), (0, 0), im.Sepia("character/manstein/manstein_base1.png"), (0, 0), im.Sepia("character/manstein/manstein_normal1.png")))
image side manstein determined = LiveCrop((55, 130, 350, 210), LiveComposite((470, 1019), (0, 0), im.Sepia("character/manstein/manstein_base1.png"), (0, 0), im.Sepia("character/manstein/manstein_determined1.png")))
image side manstein happy = LiveCrop((55, 130, 350, 210), LiveComposite((470, 1019), (0, 0), im.Sepia("character/manstein/manstein_base1.png"), (0, 0), im.Sepia("character/manstein/manstein_happy1.png")))
image side manstein moe = LiveCrop((55, 130, 350, 210), LiveComposite((470, 1019), (0, 0), im.Sepia("character/manstein/manstein_base1.png"), (0, 0), im.Sepia("character/manstein/manstein_moe1.png")))
image side manstein shock = LiveCrop((55, 130, 350, 210), LiveComposite((470, 1019), (0, 0), im.Sepia("character/manstein/manstein_base1.png"), (0, 0), im.Sepia("character/manstein/manstein_shock1.png")))

########################################################
# Gamelin ###############################################
########################################################
image gamelin angry = LiveComposite(
    (944, 1076),
    (-20, 0), "character/gamelin/gamelin_base1.png",
    (-20, 0), "character/gamelin/gamelin_angry1.png")

image gamelin determined = LiveComposite(
    (944, 1076),
    (-20, 0), "character/gamelin/gamelin_base1.png",
    (-20, 0), "character/gamelin/gamelin_determined1.png")

image gamelin happy = LiveComposite(
    (944, 1076),
    (-20, 0), "character/gamelin/gamelin_base1.png",
    (-20, 0), "character/gamelin/gamelin_happy1.png")

image gamelin moe = LiveComposite(
    (944, 1076),
    (-20, 0), "character/gamelin/gamelin_base1.png",
    (-20, 0), "character/gamelin/gamelin_moe1.png",
    (110, 90), "ellipses_bubble")

image gamelin shock = LiveComposite(
    (944, 1076),
    (-20, 0), "character/gamelin/gamelin_base1.png",
    (-20, 0), "character/gamelin/gamelin_shock1.png")

image gamelin normal = LiveComposite(
    (944, 1076),
    (-20, 0), "character/gamelin/gamelin_base1.png",
    (-20, 0), "character/gamelin/gamelin_normal1.png")

image gamelin red = LiveComposite(
    (944, 1076),
    (-20, 0), im.MatrixColor("character/gamelin/gamelin_base1.png", im.matrix.brightness(0) * im.matrix.tint(1.0, 0.5, 0.5)),
    (-20, 0), im.MatrixColor("character/gamelin/gamelin_angry1.png", im.matrix.brightness(0) * im.matrix.tint(1.0, 0.5, 0.5)))

image gamelin fuming:
    contains:
        "gamelin angry"
        xalign 0.5
        yalign 1.0
        linear 0.03 xalign 0.498
        linear 0.03 xalign 0.5
        linear 0.03 xalign 0.502
        linear 0.03 xalign 0.5
        repeat

image side gamelin determined = LiveCrop((320, 80, 350, 210), LiveComposite((944, 1076), (0, 0), im.Sepia("character/gamelin/gamelin_base1.png"), (0, 0), im.Sepia("character/gamelin/gamelin_determined1.png")))
image side gamelin happy = LiveCrop((320, 80, 350, 210), LiveComposite((944, 1076), (0, 0), im.Sepia("character/gamelin/gamelin_base1.png"), (0, 0), im.Sepia("character/gamelin/gamelin_happy1.png")))
image side gamelin moe = LiveCrop((320, 80, 350, 210), LiveComposite((944, 1076), (0, 0), im.Sepia("character/gamelin/gamelin_base1.png"), (0, 0), im.Sepia("character/gamelin/gamelin_moe1.png")))
image side gamelin shock = LiveCrop((320, 80, 350, 210), LiveComposite((944, 1076), (0, 0), im.Sepia("character/gamelin/gamelin_base1.png"), (0, 0), im.Sepia("character/gamelin/gamelin_shock1.png")))
image side gamelin normal = LiveCrop((320, 80, 350, 210), LiveComposite((944, 1076), (0, 0), im.Sepia("character/gamelin/gamelin_base1.png"), (0, 0), im.Sepia("character/gamelin/gamelin_normal1.png")))
image side gamelin angry = LiveCrop((320, 80, 350, 210), LiveComposite((944, 1076), (0, 0), im.Sepia("character/gamelin/gamelin_base1.png"), (0, 0), im.Sepia("character/gamelin/gamelin_angry1.png")))
image side gamelin fuming = LiveCrop((320, 80, 350, 210), LiveComposite((944, 1076), (0, 0), im.Sepia("character/gamelin/gamelin_base1.png"), (0, 0), im.Sepia("character/gamelin/gamelin_angry1.png")))
        
########################################################
# Molotov ###############################################
########################################################
image molotov normal = LiveComposite(
    (620, 880),
    (0, 0), "character/molotov/molotov_base1.png",
    (0, 0), "character/molotov/molotov_normal1.png")

image molotov happy = LiveComposite(
    (620, 880),
    (0, 0), "character/molotov/molotov_base1.png",
    (0, 0), "character/molotov/molotov_happy1.png")

image molotov determined = LiveComposite(
    (620, 880),
    (0, 0), "character/molotov/molotov_base1.png",
    (0, 0), "character/molotov/molotov_determined1.png")

image molotov moe = LiveComposite(
    (620, 880),
    (0, 0), "character/molotov/molotov_base1.png",
    (0, 0), "character/molotov/molotov_moe1.png")

image molotov sad = LiveComposite(
    (620, 880),
    (0, 0), "character/molotov/molotov_base1.png",
    (0, 0), "character/molotov/molotov_sad1.png")

image molotov shock = LiveComposite(
    (620, 880),
    (0, 0), "character/molotov/molotov_base1.png",
    (0, 0), "character/molotov/molotov_shock1.png")

image side molotov determined = LiveCrop((130, 70, 350, 210), LiveComposite((620, 880), (0, 0), im.Sepia("character/molotov/molotov_base1.png"), (0, 0), im.Sepia("character/molotov/molotov_determined1.png")))
image side molotov happy = LiveCrop((130, 70, 350, 210), LiveComposite((620, 880), (0, 0), im.Sepia("character/molotov/molotov_base1.png"), (0, 0), im.Sepia("character/molotov/molotov_happy1.png")))
image side molotov normal = LiveCrop((130, 70, 350, 210), LiveComposite((620, 880), (0, 0), im.Sepia("character/molotov/molotov_base1.png"), (0, 0), im.Sepia("character/molotov/molotov_normal1.png")))
image side molotov shock = LiveCrop((130, 70, 350, 210), LiveComposite((620, 880), (0, 0), im.Sepia("character/molotov/molotov_base1.png"), (0, 0), im.Sepia("character/molotov/molotov_shock1.png")))
image side molotov moe = LiveCrop((130, 70, 350, 210), LiveComposite((620, 880), (0, 0), im.Sepia("character/molotov/molotov_base1.png"), (0, 0), im.Sepia("character/molotov/molotov_moe1.png")))
image side molotov sad= LiveCrop((130, 70, 350, 210), LiveComposite((620, 880), (0, 0), im.Sepia("character/molotov/molotov_base1.png"), (0, 0), im.Sepia("character/molotov/molotov_sad1.png")))

########################################################
# Vasile ###############################################
########################################################
image vasile normal = LiveComposite(
    (530, 970),
    (0, 0), "character/vasile/vasile_base1.png",
    (0, 0), "character/vasile/vasile_normal1.png")

image vasile determined = LiveComposite(
    (530, 970),
    (0, 0), "character/vasile/vasile_base1.png",
    (0, 0), "character/vasile/vasile_determined1.png")

image vasile moe = LiveComposite(
    (530, 970),
    (0, 0), "character/vasile/vasile_base1.png",
    (0, 0), "character/vasile/vasile_moe1.png")

image vasile shock = LiveComposite(
    (530, 970),
    (0, 0), "character/vasile/vasile_base1.png",
    (0, 0), "character/vasile/vasile_shock1.png")

image side vasile determined = LiveCrop((100, 105, 350, 210), LiveComposite((530, 970), (0, 0), im.Sepia("character/vasile/vasile_base1.png"), (0, 0), im.Sepia("character/vasile/vasile_determined1.png")))
image side vasile normal = LiveCrop((100, 105, 350, 210), LiveComposite((530, 970), (0, 0), im.Sepia("character/vasile/vasile_base1.png"), (0, 0), im.Sepia("character/vasile/vasile_normal1.png")))
image side vasile shock = LiveCrop((100, 105, 350, 210), LiveComposite((530, 970), (0, 0), im.Sepia("character/vasile/vasile_base1.png"), (0, 0), im.Sepia("character/vasile/vasile_shock1.png")))
image side vasile moe = LiveCrop((100, 105, 350, 210), LiveComposite((530, 970), (0, 0), im.Sepia("character/vasile/vasile_base1.png"), (0, 0), im.Sepia("character/vasile/vasile_moe1.png")))

########################################################
# Antoness ###############################################
########################################################
image antoness angry = LiveComposite(
    (600, 860),
    (0, 0), "character/antoness/antoness_base1.png",
    (0, 0), "character/antoness/antoness_angry1.png")

image antoness insane = LiveComposite(
    (600, 860),
    (0, 0), "character/antoness/antoness_base1.png",
    (0, 0), "character/antoness/antoness_insane1.png")

image antoness normal = LiveComposite(
    (600, 860),
    (0, 0), "character/antoness/antoness_base1.png",
    (0, 0), "character/antoness/antoness_normal1.png")

image antoness happy = LiveComposite(
    (600, 860),
    (0, 0), "character/antoness/antoness_base1.png",
    (0, 0), "character/antoness/antoness_happy1.png")

image antoness moe = LiveComposite(
    (600, 860),
    (0, 0), "character/antoness/antoness_base1.png",
    (0, 0), "character/antoness/antoness_moe1.png")

image antoness shock = LiveComposite(                                               
    (600, 860),
    (0, 0), "character/antoness/antoness_base1.png",
    (0, 0), "character/antoness/antoness_shock1.png")

image side antoness angry = LiveCrop((110, 90, 350, 210), LiveComposite((600, 860), (0, 0), im.Sepia("character/antoness/antoness_base1.png"), (0, 0), im.Sepia("character/antoness/antoness_angry1.png")))
image side antoness insane = LiveCrop((110, 90, 350, 210), LiveComposite((600, 860), (0, 0), im.Sepia("character/antoness/antoness_base1.png"), (0, 0), im.Sepia("character/antoness/antoness_insane1.png")))
image side antoness moe = LiveCrop((110, 90, 350, 210), LiveComposite((600, 860), (0, 0), im.Sepia("character/antoness/antoness_base1.png"), (0, 0), im.Sepia("character/antoness/antoness_moe1.png")))
image side antoness happy = LiveCrop((110, 90, 350, 210), LiveComposite((600, 860), (0, 0), im.Sepia("character/antoness/antoness_base1.png"), (0, 0), im.Sepia("character/antoness/antoness_happy1.png")))
image side antoness normal = LiveCrop((110, 90, 350, 210), LiveComposite((600, 860), (0, 0), im.Sepia("character/antoness/antoness_base1.png"), (0, 0), im.Sepia("character/antoness/antoness_normal1.png")))
image side antoness shock = LiveCrop((110, 90, 350, 210), LiveComposite((600, 860), (0, 0), im.Sepia("character/antoness/antoness_base1.png"), (0, 0), im.Sepia("character/antoness/antoness_shock1.png")))

########################################################
# Messe ###############################################
########################################################
image messe normal = LiveComposite(
    (580, 920),
    (0, 0), "character/messe/messe_base1.png",
    (0, 0), "character/messe/messe_normal1.png")

image messe happy = LiveComposite(
    (580, 920),
    (0, 0), "character/messe/messe_base1.png",
    (0, 0), "character/messe/messe_happy1.png")

image messe determined = LiveComposite(
    (580, 920),
    (0, 0), "character/messe/messe_base1.png",
    (0, 0), "character/messe/messe_determined1.png")

image messe moe = LiveComposite(
    (580, 920),
    (0, 0), "character/messe/messe_base1.png",
    (0, 0), "character/messe/messe_moe1.png")

image messe shock = LiveComposite(
    (580, 920),
    (0, 0), "character/messe/messe_base1.png",
    (0, 0), "character/messe/messe_shock1.png")

image side messe determined = LiveCrop((130, 110, 350, 210), LiveComposite((580, 920), (0, 0), im.Sepia("character/messe/messe_base1.png"), (0, 0), im.Sepia("character/messe/messe_determined1.png")))
image side messe happy = LiveCrop((130, 110, 350, 210), LiveComposite((580, 920), (0, 0), im.Sepia("character/messe/messe_base1.png"), (0, 0), im.Sepia("character/messe/messe_happy1.png")))
image side messe normal = LiveCrop((130, 110, 350, 210), LiveComposite((580, 920), (0, 0), im.Sepia("character/messe/messe_base1.png"), (0, 0), im.Sepia("character/messe/messe_normal1.png")))
image side messe moe = LiveCrop((130, 110, 350, 210), LiveComposite((580, 920), (0, 0), im.Sepia("character/messe/messe_base1.png"), (0, 0), im.Sepia("character/messe/messe_moe1.png")))
image side messe shock = LiveCrop((130, 110, 350, 210), LiveComposite((580, 920), (0, 0), im.Sepia("character/messe/messe_base1.png"), (0, 0), im.Sepia("character/messe/messe_shock1.png")))

########################################################
# Graziani ###############################################
########################################################
image graziani normal = LiveComposite(
    (500, 900),
    (0, 0), "character/graziani/graziani_base1.png",
    (0, 0), "character/graziani/graziani_normal1.png")

image graziani happy = LiveComposite(
    (500, 900),
    (0, 0), "character/graziani/graziani_base1.png",
    (0, 0), "character/graziani/graziani_happy1.png")

image graziani determined = LiveComposite(
    (500, 900),
    (0, 0), "character/graziani/graziani_base1.png",
    (0, 0), "character/graziani/graziani_determined1.png")

image graziani moe = LiveComposite(
    (500, 900),
    (0, 0), "character/graziani/graziani_base1.png",
    (0, 0), "character/graziani/graziani_moe1.png")

image graziani shock = LiveComposite(
    (500, 900),
    (0, 0), "character/graziani/graziani_base1.png",
    (0, 0), "character/graziani/graziani_shock1.png")

image graziani tank normal:
    "graziani normal"
    xalign 0.5  yalign 1.0
    linear 0.1 yalign 1.1
    linear 0.1 yalign 1.0
    repeat
    
image graziani tank happy:
    "graziani happy"
    xalign 0.5  yalign 1.0
    linear 0.1 yalign 1.1
    linear 0.1 yalign 1.0
    repeat
    
image graziani tank determined:
    "graziani determined"
    xalign 0.5  yalign 1.0
    linear 0.1 yalign 1.1
    linear 0.1 yalign 1.0
    repeat

image graziani tank moe:
    "graziani moe"
    xalign 0.5  yalign 1.0
    linear 0.1 yalign 1.1
    linear 0.1 yalign 1.0
    repeat
    
image graziani tank shock:
    "graziani shock"
    xalign 0.5  yalign 1.0
    linear 0.1 yalign 1.1
    linear 0.1 yalign 1.0
    repeat

image side graziani determined = LiveCrop((50, 110, 350, 210), LiveComposite((500, 900), (0, 0), im.Sepia("character/graziani/graziani_base1.png"), (0, 0), im.Sepia("character/graziani/graziani_determined1.png")))
image side graziani happy = LiveCrop((50, 110, 350, 210), LiveComposite((500, 900), (0, 0), im.Sepia("character/graziani/graziani_base1.png"), (0, 0), im.Sepia("character/graziani/graziani_happy1.png")))
image side graziani normal = LiveCrop((50, 110, 350, 210), LiveComposite((500, 900), (0, 0), im.Sepia("character/graziani/graziani_base1.png"), (0, 0), im.Sepia("character/graziani/graziani_normal1.png")))
image side graziani moe = LiveCrop((50, 110, 350, 210), LiveComposite((500, 900), (0, 0), im.Sepia("character/graziani/graziani_base1.png"), (0, 0), im.Sepia("character/graziani/graziani_moe1.png")))
image side graziani shock = LiveCrop((50, 110, 350, 210), LiveComposite((500, 900), (0, 0), im.Sepia("character/graziani/graziani_base1.png"), (0, 0), im.Sepia("character/graziani/graziani_shock1.png")))

########################################################
# General ###############################################
########################################################
image oriasiangeneral normal = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/oriasiangeneral_base1.png",
    (0, 0), "character/general/oriasiangeneral_normal1.png")

image oriasiangeneral happy = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/oriasiangeneral_base1.png",
    (0, 0), "character/general/oriasiangeneral_happy1.png")

image oriasiangeneral determined = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/oriasiangeneral_base1.png",
    (0, 0), "character/general/oriasiangeneral_determined1.png")

image oriasiangeneral shock = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/oriasiangeneral_base1.png",
    (0, 0), "character/general/oriasiangeneral_shock1.png")

image soviangeneral normal = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/soviangeneral_base1.png",
    (0, 0), "character/general/soviangeneral_normal1.png")

image soviangeneral happy = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/soviangeneral_base1.png",
    (0, 0), "character/general/soviangeneral_happy1.png")

image soviangeneral determined = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/soviangeneral_base1.png",
    (0, 0), "character/general/soviangeneral_determined1.png")

image soviangeneral shock = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/soviangeneral_base1.png",
    (0, 0), "character/general/soviangeneral_shock1.png")

image germaniangeneral normal = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/germaniangeneral_base1.png",
    (0, 0), "character/general/germaniangeneral_normal1.png")

image germaniangeneral happy = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/germaniangeneral_base1.png",
    (0, 0), "character/general/germaniangeneral_happy1.png")

image germaniangeneral determined = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/germaniangeneral_base1.png",
    (0, 0), "character/general/germaniangeneral_determined1.png")

image germaniangeneral shock = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/germaniangeneral_base1.png",
    (0, 0), "character/general/germaniangeneral_shock1.png")

image germaniangeneraloberst normal = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/germaniangeneraloberst_base1.png",
    (0, 0), "character/general/germaniangeneraloberst_normal1.png")

image germaniangeneraloberst happy = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/germaniangeneraloberst_base1.png",
    (0, 0), "character/general/germaniangeneraloberst_happy1.png")

image germaniangeneraloberst determined = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/germaniangeneraloberst_base1.png",
    (0, 0), "character/general/germaniangeneraloberst_determined1.png")

image germaniangeneraloberst shock = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/germaniangeneraloberst_base1.png",
    (0, 0), "character/general/germaniangeneraloberst_shock1.png")

image desertgeneral normal = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/desertgeneral_base1.png",
    (0, 0), "character/general/desertgeneral_normal1.png")

image desertgeneral happy = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/desertgeneral_base1.png",
    (0, 0), "character/general/desertgeneral_happy1.png")

image desertgeneral determined = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/desertgeneral_base1.png",
    (0, 0), "character/general/desertgeneral_determined1.png")

image desertgeneral shock = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/desertgeneral_base1.png",
    (0, 0), "character/general/desertgeneral_shock1.png")

image zombiegeneral determined = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/zombiegeneral_base1.png",
    (0, 0), "character/general/zombiegeneral_determined1.png")

image britanniangeneral normal = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/britanniangeneral_base1.png",
    (0, 0), "character/general/britanniangeneral_normal1.png")

image britanniangeneral happy = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/britanniangeneral_base1.png",
    (0, 0), "character/general/britanniangeneral_happy1.png")

image britanniangeneral determined = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/britanniangeneral_base1.png",
    (0, 0), "character/general/britanniangeneral_determined1.png")

image britanniangeneral shock = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/britanniangeneral_base1.png",
    (0, 0), "character/general/britanniangeneral_shock1.png")

image weygand normal = LiveComposite(
    (500, 976),
    (0, 0), "character/general/weygand_base1.png",
    (0, 0), "character/general/weygand_normal1.png")

image weygand happy = LiveComposite(
    (500, 976),
    (0, 0), "character/general/weygand_base1.png",
    (0, 0), "character/general/weygand_happy1.png")

image weygand determined = LiveComposite(
    (500, 976),
    (0, 0), "character/general/weygand_base1.png",
    (0, 0), "character/general/weygand_determined1.png")

image weygand shock = LiveComposite(
    (500, 976),
    (0, 0), "character/general/weygand_base1.png",
    (0, 0), "character/general/weygand_shock1.png")

image gort normal = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/gort_base1.png",
    (0, 0), "character/general/gort_normal1.png")

image gort happy = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/gort_base1.png",
    (0, 0), "character/general/gort_happy1.png")

image gort determined = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/gort_base1.png",
    (0, 0), "character/general/gort_determined1.png")

image gort shock = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/gort_base1.png",
    (0, 0), "character/general/gort_shock1.png")

image hess normal = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/hess_base1.png",
    (0, 0), "character/general/hess_normal1.png")

image hess happy = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/hess_base1.png",
    (0, 0), "character/general/hess_happy1.png")

image hess determined = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/hess_base1.png",
    (0, 0), "character/general/hess_determined1.png")

image hess shock = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/hess_base1.png",
    (0, 0), "character/general/hess_shock1.png")

image hess scared:
    "hess shock" with ease
    xalign 0.5
    yalign 1.0
    linear 0.03 xalign 0.498
    linear 0.03 xalign 0.5
    linear 0.03 xalign 0.502
    linear 0.03 xalign 0.5
    repeat

image germanianadmiral normal = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/germanianadmiral_base1.png",
    (0, 0), "character/general/germanianadmiral_normal1.png")

image germanianadmiral happy = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/germanianadmiral_base1.png",
    (0, 0), "character/general/germanianadmiral_happy1.png")

image germanianadmiral determined = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/germanianadmiral_base1.png",
    (0, 0), "character/general/germanianadmiral_determined1.png")

image germanianadmiral shock = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/germanianadmiral_base1.png",
    (0, 0), "character/general/germanianadmiral_shock1.png")

image basicgeneral normal = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/basicgeneral_base1.png",
    (0, 0), "character/general/basicgeneral_normal1.png")

image basicgeneral happy = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/basicgeneral_base1.png",
    (0, 0), "character/general/basicgeneral_happy1.png")

image basicgeneral determined = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/basicgeneral_base1.png",
    (0, 0), "character/general/basicgeneral_determined1.png")

image basicgeneral shock = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/basicgeneral_base1.png",
    (0, 0), "character/general/basicgeneral_shock1.png")

image kaiser normal = LiveComposite(
    (500, 1069),
    (0, 0), "character/general/kaiser_base1.png",
    (0, 0), "character/general/kaiser_normal1.png")

image kaiser happy = LiveComposite(
    (500, 1069),
    (0, 0), "character/general/kaiser_base1.png",
    (0, 0), "character/general/kaiser_happy1.png")

image kaiser determined = LiveComposite(
    (500, 1069),
    (0, 0), "character/general/kaiser_base1.png",
    (0, 0), "character/general/kaiser_determined1.png")

image kaiser shock = LiveComposite(
    (500, 1069),
    (0, 0), "character/general/kaiser_base1.png",
    (0, 0), "character/general/kaiser_shock1.png")

image beck normal = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/beck_base1.png",
    (0, 0), "character/general/beck_normal1.png")

image beck happy = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/beck_base1.png",
    (0, 0), "character/general/beck_happy1.png")

image beck determined = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/beck_base1.png",
    (0, 0), "character/general/beck_determined1.png")

image beck shock = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/beck_base1.png",
    (0, 0), "character/general/beck_shock1.png")

image dimashenka normal = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/dimashenka_base1.png",
    (0, 0), "character/general/dimashenka_normal1.png")

image dimashenka happy = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/dimashenka_base1.png",
    (0, 0), "character/general/dimashenka_happy1.png")

image dimashenka determined = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/dimashenka_base1.png",
    (0, 0), "character/general/dimashenka_determined1.png")

image dimashenka shock = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/dimashenka_base1.png",               
    (0, 0), "character/general/dimashenka_shock1.png")

image ztauffenborg normal = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/ztauffenborg_base1.png",
    (0, 0), "character/general/ztauffenborg_normal1.png")

image ztauffenborg happy = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/ztauffenborg_base1.png",
    (0, 0), "character/general/ztauffenborg_happy1.png")

image ztauffenborg determined = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/ztauffenborg_base1.png",
    (0, 0), "character/general/ztauffenborg_determined1.png")

image ztauffenborg shock = LiveComposite(
    (500, 1000),
    (0, 0), "character/general/ztauffenborg_base1.png",               
    (0, 0), "character/general/ztauffenborg_shock1.png")

image side oriasiangeneral determined = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/oriasiangeneral_base1.png"), (0, 0), im.Sepia("character/general/oriasiangeneral_determined1.png")))
image side oriasiangeneral happy = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/oriasiangeneral_base1.png"), (0, 0), im.Sepia("character/general/oriasiangeneral_happy1.png")))
image side oriasiangeneral normal = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/oriasiangeneral_base1.png"), (0, 0), im.Sepia("character/general/oriasiangeneral_normal1.png")))
image side oriasiangeneral shock = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/oriasiangeneral_base1.png"), (0, 0), im.Sepia("character/general/oriasiangeneral_shock1.png")))

image side soviangeneral determined = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/soviangeneral_base1.png"), (0, 0), im.Sepia("character/general/soviangeneral_determined1.png")))
image side soviangeneral happy = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/soviangeneral_base1.png"), (0, 0), im.Sepia("character/general/soviangeneral_happy1.png")))
image side soviangeneral normal = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/soviangeneral_base1.png"), (0, 0), im.Sepia("character/general/soviangeneral_normal1.png")))
image side soviangeneral shock = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/soviangeneral_base1.png"), (0, 0), im.Sepia("character/general/soviangeneral_shock1.png")))

image side germaniangeneral determined = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/germaniangeneral_base1.png"), (0, 0), im.Sepia("character/general/germaniangeneral_determined1.png")))
image side germaniangeneral happy = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/germaniangeneral_base1.png"), (0, 0), im.Sepia("character/general/germaniangeneral_happy1.png")))
image side germaniangeneral normal = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/germaniangeneral_base1.png"), (0, 0), im.Sepia("character/general/germaniangeneral_normal1.png")))
image side germaniangeneral shock = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/germaniangeneral_base1.png"), (0, 0), im.Sepia("character/general/germaniangeneral_shock1.png")))

image side desertgeneral determined = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/desertgeneral_base1.png"), (0, 0), im.Sepia("character/general/desertgeneral_determined1.png")))
image side desertgeneral happy = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/desertgeneral_base1.png"), (0, 0), im.Sepia("character/general/desertgeneral_happy1.png")))
image side desertgeneral normal = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/desertgeneral_base1.png"), (0, 0), im.Sepia("character/general/desertgeneral_normal1.png")))
image side desertgeneral shock = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/desertgeneral_base1.png"), (0, 0), im.Sepia("character/general/desertgeneral_shock1.png")))

image side zombiegeneral determined = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/zombiegeneral_base1.png"), (0, 0), im.Sepia("character/general/zombiegeneral_determined1.png")))

image side britanniangeneral determined = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/britanniangeneral_base1.png"), (0, 0), im.Sepia("character/general/britanniangeneral_determined1.png")))
image side britanniangeneral happy = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/britanniangeneral_base1.png"), (0, 0), im.Sepia("character/general/britanniangeneral_happy1.png")))
image side britanniangeneral normal = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/britanniangeneral_base1.png"), (0, 0), im.Sepia("character/general/britanniangeneral_normal1.png")))
image side britanniangeneral shock = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/britanniangeneral_base1.png"), (0, 0), im.Sepia("character/general/britanniangeneral_shock1.png")))

image side germaniangeneraloberst determined = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/germaniangeneraloberst_base1.png"), (0, 0), im.Sepia("character/general/germaniangeneraloberst_determined1.png")))
image side germaniangeneraloberst happy = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/germaniangeneraloberst_base1.png"), (0, 0), im.Sepia("character/general/germaniangeneraloberst_happy1.png")))
image side germaniangeneraloberst normal = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/germaniangeneraloberst_base1.png"), (0, 0), im.Sepia("character/general/germaniangeneraloberst_normal1.png")))
image side germaniangeneraloberst shock = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/germaniangeneraloberst_base1.png"), (0, 0), im.Sepia("character/general/germaniangeneraloberst_shock1.png")))

image side weygand determined = LiveCrop((75, 76, 350, 210), LiveComposite((500, 976), (0, 0), im.Sepia("character/general/weygand_base1.png"), (0, 0), im.Sepia("character/general/weygand_determined1.png")))
image side weygand happy = LiveCrop((75, 76, 350, 210), LiveComposite((500, 976), (0, 0), im.Sepia("character/general/weygand_base1.png"), (0, 0), im.Sepia("character/general/weygand_happy1.png")))
image side weygand normal = LiveCrop((75, 76, 350, 210), LiveComposite((500, 976), (0, 0), im.Sepia("character/general/weygand_base1.png"), (0, 0), im.Sepia("character/general/weygand_normal1.png")))
image side weygand shock = LiveCrop((75, 76, 350, 210), LiveComposite((500, 976), (0, 0), im.Sepia("character/general/weygand_base1.png"), (0, 0), im.Sepia("character/general/weygand_shock1.png")))

image side gort determined = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/gort_base1.png"), (0, 0), im.Sepia("character/general/gort_determined1.png")))
image side gort happy = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/gort_base1.png"), (0, 0), im.Sepia("character/general/gort_happy1.png")))
image side gort normal = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/gort_base1.png"), (0, 0), im.Sepia("character/general/gort_normal1.png")))
image side gort shock = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/gort_base1.png"), (0, 0), im.Sepia("character/general/gort_shock1.png")))

image side hess determined = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/hess_base1.png"), (0, 0), im.Sepia("character/general/hess_determined1.png")))
image side hess happy = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/hess_base1.png"), (0, 0), im.Sepia("character/general/hess_happy1.png")))
image side hess normal = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/hess_base1.png"), (0, 0), im.Sepia("character/general/hess_normal1.png")))
image side hess shock = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/hess_base1.png"), (0, 0), im.Sepia("character/general/hess_shock1.png")))
image side hess scared = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/hess_base1.png"), (0, 0), im.Sepia("character/general/hess_shock1.png")))

image side germanianadmiral determined = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/germanianadmiral_base1.png"), (0, 0), im.Sepia("character/general/germanianadmiral_determined1.png")))
image side germanianadmiral happy = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/germanianadmiral_base1.png"), (0, 0), im.Sepia("character/general/germanianadmiral_happy1.png")))
image side germanianadmiral normal = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/germanianadmiral_base1.png"), (0, 0), im.Sepia("character/general/germanianadmiral_normal1.png")))
image side germanianadmiral shock = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/germanianadmiral_base1.png"), (0, 0), im.Sepia("character/general/germanianadmiral_shock1.png")))

image side basicgeneral determined = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/basicgeneral_base1.png"), (0, 0), im.Sepia("character/general/basicgeneral_determined1.png")))
image side basicgeneral happy = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/basicgeneral_base1.png"), (0, 0), im.Sepia("character/general/basicgeneral_happy1.png")))
image side basicgeneral normal = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/basicgeneral_base1.png"), (0, 0), im.Sepia("character/general/basicgeneral_normal1.png")))
image side basicgeneral shock = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/basicgeneral_base1.png"), (0, 0), im.Sepia("character/general/basicgeneral_shock1.png")))

image side kaiser determined = LiveCrop((75, 169, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/kaiser_base1.png"), (0, 0), im.Sepia("character/general/kaiser_determined1.png")))
image side kaiser happy = LiveCrop((75, 169, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/kaiser_base1.png"), (0, 0), im.Sepia("character/general/kaiser_happy1.png")))
image side kaiser normal = LiveCrop((75, 169, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/kaiser_base1.png"), (0, 0), im.Sepia("character/general/kaiser_normal1.png")))
image side kaiser shock = LiveCrop((75, 169, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/kaiser_base1.png"), (0, 0), im.Sepia("character/general/kaiser_shock1.png")))

image side beck determined = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/beck_base1.png"), (0, 0), im.Sepia("character/general/beck_determined1.png")))
image side beck happy = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/beck_base1.png"), (0, 0), im.Sepia("character/general/beck_happy1.png")))
image side beck normal = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/beck_base1.png"), (0, 0), im.Sepia("character/general/beck_normal1.png")))
image side beck shock = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/beck_base1.png"), (0, 0), im.Sepia("character/general/beck_shock1.png")))

image side dimashenka determined = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/dimashenka_base1.png"), (0, 0), im.Sepia("character/general/dimashenka_determined1.png")))
image side dimashenka happy = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/dimashenka_base1.png"), (0, 0), im.Sepia("character/general/dimashenka_happy1.png")))
image side dimashenka normal = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/dimashenka_base1.png"), (0, 0), im.Sepia("character/general/dimashenka_normal1.png")))
image side dimashenka shock = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/dimashenka_base1.png"), (0, 0), im.Sepia("character/general/dimashenka_shock1.png")))

image side ztauffenborg determined = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/ztauffenborg_base1.png"), (0, 0), im.Sepia("character/general/ztauffenborg_determined1.png")))
image side ztauffenborg happy = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/ztauffenborg_base1.png"), (0, 0), im.Sepia("character/general/ztauffenborg_happy1.png")))
image side ztauffenborg normal = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/ztauffenborg_base1.png"), (0, 0), im.Sepia("character/general/ztauffenborg_normal1.png")))
image side ztauffenborg shock = LiveCrop((75, 100, 350, 210), LiveComposite((500, 1000), (0, 0), im.Sepia("character/general/ztauffenborg_base1.png"), (0, 0), im.Sepia("character/general/ztauffenborg_shock1.png")))

########################################################
# Axle Soldier ###############################################
########################################################
image axis normal = LiveComposite(
    (1100, 930),
    (0, 0), "character/axis/axis_base1.png",
    (0, 0), "character/axis/axis_normal1.png")

image axis happy = LiveComposite(
    (1100, 930),
    (0, 0), "character/axis/axis_base1.png",
    (0, 0), "character/axis/axis_happy1.png")

image axis determined = LiveComposite(
    (1100, 930),
    (0, 0), "character/axis/axis_base1.png",
    (0, 0), "character/axis/axis_determined1.png")

image axis shock = LiveComposite(
    (1100, 930),
    (0, 0), "character/axis/axis_base1.png",
    (0, 0), "character/axis/axis_shock1.png")

image desertaxis normal = LiveComposite(
    (1100, 930),
    (0, 0), "character/axis/desertaxis_base1.png",
    (0, 0), "character/axis/desertaxis_normal1.png")

image desertaxis happy = LiveComposite(
    (1100, 930),
    (0, 0), "character/axis/desertaxis_base1.png",
    (0, 0), "character/axis/desertaxis_happy1.png")

image desertaxis determined = LiveComposite(
    (1100, 930),
    (0, 0), "character/axis/desertaxis_base1.png",
    (0, 0), "character/axis/desertaxis_determined1.png")

image desertaxis shock = LiveComposite(
    (1100, 930),
    (0, 0), "character/axis/desertaxis_base1.png",
    (0, 0), "character/axis/desertaxis_shock1.png")

image winteraxis normal = LiveComposite(
    (1100, 930),
    (0, 0), "character/axis/winteraxis_base1.png",
    (0, 0), "character/axis/winteraxis_normal1.png")

image winteraxis happy = LiveComposite(
    (1100, 930),
    (0, 0), "character/axis/winteraxis_base1.png",
    (0, 0), "character/axis/winteraxis_happy1.png")

image winteraxis determined = LiveComposite(
    (1100, 930),
    (0, 0), "character/axis/winteraxis_base1.png",
    (0, 0), "character/axis/winteraxis_determined1.png")

image winteraxis shock = LiveComposite(
    (1100, 930),
    (0, 0), "character/axis/winteraxis_base1.png",
    (0, 0), "character/axis/winteraxis_shock1.png")

image camoaxis normal = LiveComposite(
    (1100, 930),
    (0, 0), "character/axis/camoaxis_base1.png",
    (0, 0), "character/axis/camoaxis_normal1.png")

image camoaxis happy = LiveComposite(
    (1100, 930),
    (0, 0), "character/axis/camoaxis_base1.png",
    (0, 0), "character/axis/camoaxis_happy1.png")

image camoaxis determined = LiveComposite(
    (1100, 930),
    (0, 0), "character/axis/camoaxis_base1.png",
    (0, 0), "character/axis/camoaxis_determined1.png")

image camoaxis shock = LiveComposite(
    (1100, 930),
    (0, 0), "character/axis/camoaxis_base1.png",
    (0, 0), "character/axis/camoaxis_shock1.png")

image kirponos normal = LiveComposite(
    (600, 935),
    (0, 0), "character/axis/kirponos_base1.png",
    (0, 0), "character/axis/kirponos_normal1.png")

image kirponos happy = LiveComposite(
    (600, 935),
    (0, 0), "character/axis/kirponos_base1.png",
    (0, 0), "character/axis/kirponos_happy1.png")

image kirponos determined = LiveComposite(
    (600, 935),
    (0, 0), "character/axis/kirponos_base1.png",
    (0, 0), "character/axis/kirponos_determined1.png")

image kirponos shock = LiveComposite(
    (600, 935),
    (0, 0), "character/axis/kirponos_base1.png",
    (0, 0), "character/axis/kirponos_shock1.png")

image vleischer normal = LiveComposite(
    (600, 935),
    (0, 0), "character/axis/vleischer_base1.png",
    (0, 0), "character/axis/vleischer_normal1.png")

image vleischer happy = LiveComposite(
    (600, 935),
    (0, 0), "character/axis/vleischer_base1.png",
    (0, 0), "character/axis/vleischer_happy1.png")

image vleischer determined = LiveComposite(
    (600, 935),
    (0, 0), "character/axis/vleischer_base1.png",
    (0, 0), "character/axis/vleischer_determined1.png")

image vleischer shock = LiveComposite(
    (600, 935),
    (0, 0), "character/axis/vleischer_base1.png",
    (0, 0), "character/axis/vleischer_shock1.png")

image hoppyner normal = LiveComposite(
    (600, 935),
    (0, 0), "character/axis/hoppyner_base1.png",
    (0, 0), "character/axis/hoppyner_normal1.png")

image hoppyner happy = LiveComposite(
    (600, 935),
    (0, 0), "character/axis/hoppyner_base1.png",
    (0, 0), "character/axis/hoppyner_happy1.png")

image hoppyner determined = LiveComposite(
    (600, 935),
    (0, 0), "character/axis/hoppyner_base1.png",
    (0, 0), "character/axis/hoppyner_determined1.png")

image hoppyner shock = LiveComposite(
    (600, 935),
    (0, 0), "character/axis/hoppyner_base1.png",
    (0, 0), "character/axis/hoppyner_shock1.png")

image zombiesoldier determined = LiveComposite(
    (1100, 930),
    (0, 0), "character/axis/zombieaxis_base1.png",
    (0, 0), "character/axis/zombieaxis_determined1.png")

image axis tank happy:
    "axis happy"
    xalign 0.5  yalign 1.0
    linear 0.1 yalign 1.1
    linear 0.1 yalign 1.0
    repeat
    
image axis tank normal:
    "axis normal"
    xalign 0.5  yalign 1.0
    linear 0.1 yalign 1.1
    linear 0.1 yalign 1.0
    repeat
    
image axis tank determined:
    "axis determined"
    xalign 0.5  yalign 1.0
    linear 0.1 yalign 1.1
    linear 0.1 yalign 1.0
    repeat

image axis tank shock:
    "axis shock"
    xalign 0.5  yalign 1.0
    linear 0.1 yalign 1.1
    linear 0.1 yalign 1.0
    repeat

image side axis determined = LiveCrop((380, 100, 350, 210), LiveComposite((1100, 930), (0, 0), im.Sepia("character/axis/axis_base1.png"), (0, 0), im.Sepia("character/axis/axis_determined1.png")))
image side axis happy = LiveCrop((380, 100, 350, 210), LiveComposite((1100, 930), (0, 0), im.Sepia("character/axis/axis_base1.png"), (0, 0), im.Sepia("character/axis/axis_happy1.png")))
image side axis normal = LiveCrop((380, 100, 350, 210), LiveComposite((1100, 930), (0, 0), im.Sepia("character/axis/axis_base1.png"), (0, 0), im.Sepia("character/axis/axis_normal1.png")))
image side axis shock = LiveCrop((380, 100, 350, 210), LiveComposite((1100, 930), (0, 0), im.Sepia("character/axis/axis_base1.png"), (0, 0), im.Sepia("character/axis/axis_shock1.png")))

image side desertaxis determined = LiveCrop((380, 100, 350, 210), LiveComposite((1100, 930), (0, 0), im.Sepia("character/axis/desertaxis_base1.png"), (0, 0), im.Sepia("character/axis/desertaxis_determined1.png")))
image side desertaxis happy = LiveCrop((380, 100, 350, 210), LiveComposite((1100, 930), (0, 0), im.Sepia("character/axis/desertaxis_base1.png"), (0, 0), im.Sepia("character/axis/desertaxis_happy1.png")))
image side desertaxis normal = LiveCrop((380, 100, 350, 210), LiveComposite((1100, 930), (0, 0), im.Sepia("character/axis/desertaxis_base1.png"), (0, 0), im.Sepia("character/axis/desertaxis_normal1.png")))
image side desertaxis shock = LiveCrop((380, 100, 350, 210), LiveComposite((1100, 930), (0, 0), im.Sepia("character/axis/desertaxis_base1.png"), (0, 0), im.Sepia("character/axis/desertaxis_shock1.png")))

image side winteraxis determined = LiveCrop((380, 100, 350, 210), LiveComposite((1100, 930), (0, 0), im.Sepia("character/axis/winteraxis_base1.png"), (0, 0), im.Sepia("character/axis/winteraxis_determined1.png")))
image side winteraxis happy = LiveCrop((380, 100, 350, 210), LiveComposite((1100, 930), (0, 0), im.Sepia("character/axis/winteraxis_base1.png"), (0, 0), im.Sepia("character/axis/winteraxis_happy1.png")))
image side winteraxis normal = LiveCrop((380, 100, 350, 210), LiveComposite((1100, 930), (0, 0), im.Sepia("character/axis/winteraxis_base1.png"), (0, 0), im.Sepia("character/axis/winteraxis_normal1.png")))
image side winteraxis shock = LiveCrop((380, 100, 350, 210), LiveComposite((1100, 930), (0, 0), im.Sepia("character/axis/winteraxis_base1.png"), (0, 0), im.Sepia("character/axis/winteraxis_shock1.png")))

image side camoaxis determined = LiveCrop((380, 100, 350, 210), LiveComposite((1100, 930), (0, 0), im.Sepia("character/axis/camoaxis_base1.png"), (0, 0), im.Sepia("character/axis/camoaxis_determined1.png")))
image side camoaxis happy = LiveCrop((380, 100, 350, 210), LiveComposite((1100, 930), (0, 0), im.Sepia("character/axis/camoaxis_base1.png"), (0, 0), im.Sepia("character/axis/camoaxis_happy1.png")))
image side camoaxis normal = LiveCrop((380, 100, 350, 210), LiveComposite((1100, 930), (0, 0), im.Sepia("character/axis/camoaxis_base1.png"), (0, 0), im.Sepia("character/axis/camoaxis_normal1.png")))
image side camoaxis shock = LiveCrop((380, 100, 350, 210), LiveComposite((1100, 930), (0, 0), im.Sepia("character/axis/camoaxis_base1.png"), (0, 0), im.Sepia("character/axis/camoaxis_shock1.png")))

image side axis tank determined = LiveCrop((380, 100, 350, 210), LiveComposite((1100, 930), (0, 0), im.Sepia("character/axis/axis_base1.png"), (0, 0), im.Sepia("character/axis/axis_determined1.png")))
image side axis tank happy = LiveCrop((380, 100, 350, 210), LiveComposite((1100, 930), (0, 0), im.Sepia("character/axis/axis_base1.png"), (0, 0), im.Sepia("character/axis/axis_happy1.png")))
image side axis tank normal = LiveCrop((380, 100, 350, 210), LiveComposite((1100, 930), (0, 0), im.Sepia("character/axis/axis_base1.png"), (0, 0), im.Sepia("character/axis/axis_normal1.png")))
image side axis tank shock = LiveCrop((380, 100, 350, 210), LiveComposite((1100, 930), (0, 0), im.Sepia("character/axis/axis_base1.png"), (0, 0), im.Sepia("character/axis/axis_shock1.png")))

image side kirponos determined = LiveCrop((110, 70, 350, 210), LiveComposite((600, 930), (0, 0), im.Sepia("character/axis/kirponos_base1.png"), (0, 0), im.Sepia("character/axis/kirponos_determined1.png")))
image side kirponos happy = LiveCrop((110, 70, 350, 210), LiveComposite((600, 930), (0, 0), im.Sepia("character/axis/kirponos_base1.png"), (0, 0), im.Sepia("character/axis/kirponos_happy1.png")))
image side kirponos normal = LiveCrop((110, 70, 350, 210), LiveComposite((600, 930), (0, 0), im.Sepia("character/axis/kirponos_base1.png"), (0, 0), im.Sepia("character/axis/kirponos_normal1.png")))
image side kirponos shock = LiveCrop((110, 70, 350, 210), LiveComposite((600, 930), (0, 0), im.Sepia("character/axis/kirponos_base1.png"), (0, 0), im.Sepia("character/axis/kirponos_shock1.png")))

image side vleischer determined = LiveCrop((110, 70, 350, 210), LiveComposite((600, 930), (0, 0), im.Sepia("character/axis/vleischer_base1.png"), (0, 0), im.Sepia("character/axis/vleischer_determined1.png")))
image side vleischer happy = LiveCrop((110, 70, 350, 210), LiveComposite((600, 930), (0, 0), im.Sepia("character/axis/vleischer_base1.png"), (0, 0), im.Sepia("character/axis/vleischer_happy1.png")))
image side vleischer normal = LiveCrop((110, 70, 350, 210), LiveComposite((600, 930), (0, 0), im.Sepia("character/axis/vleischer_base1.png"), (0, 0), im.Sepia("character/axis/vleischer_normal1.png")))
image side vleischer shock = LiveCrop((110, 70, 350, 210), LiveComposite((600, 930), (0, 0), im.Sepia("character/axis/vleischer_base1.png"), (0, 0), im.Sepia("character/axis/vleischer_shock1.png")))

image side hoppyner determined = LiveCrop((110, 100, 350, 210), LiveComposite((600, 930), (0, 0), im.Sepia("character/axis/hoppyner_base1.png"), (0, 0), im.Sepia("character/axis/hoppyner_determined1.png")))
image side hoppyner happy = LiveCrop((110, 100, 350, 210), LiveComposite((600, 930), (0, 0), im.Sepia("character/axis/hoppyner_base1.png"), (0, 0), im.Sepia("character/axis/hoppyner_happy1.png")))
image side hoppyner normal = LiveCrop((110, 100, 350, 210), LiveComposite((600, 930), (0, 0), im.Sepia("character/axis/hoppyner_base1.png"), (0, 0), im.Sepia("character/axis/hoppyner_normal1.png")))
image side hoppyner shock = LiveCrop((110, 100, 350, 210), LiveComposite((600, 930), (0, 0), im.Sepia("character/axis/hoppyner_base1.png"), (0, 0), im.Sepia("character/axis/hoppyner_shock1.png")))

image side zombiesoldier determined = LiveCrop((380, 100, 350, 210), LiveComposite((1100, 930), (0, 0), im.Sepia("character/axis/zombieaxis_base1.png"), (0, 0), im.Sepia("character/axis/zombieaxis_determined1.png")))

########################################################
# Sovian Soldier ###############################################
########################################################
image sovian normal = LiveComposite(
    (570, 920),
    (0, 0), "character/sovian/sovian_base1.png",
    (0, 0), "character/sovian/sovian_normal1.png")

image sovian happy = LiveComposite(
    (570, 920),
    (0, 0), "character/sovian/sovian_base1.png",
    (0, 0), "character/sovian/sovian_happy1.png")

image sovian determined = LiveComposite(
    (570, 920),
    (0, 0), "character/sovian/sovian_base1.png",
    (0, 0), "character/sovian/sovian_determined1.png")

image sovian shock = LiveComposite(
    (570, 920),
    (0, 0), "character/sovian/sovian_base1.png",
    (0, 0), "character/sovian/sovian_shock1.png")

image hubal normal = LiveComposite(
    (570, 920),
    (0, 0), "character/sovian/hubal_base1.png",
    (0, 0), "character/sovian/hubal_normal1.png")

image hubal determined = LiveComposite(
    (570, 920),
    (0, 0), "character/sovian/hubal_base1.png",
    (0, 0), "character/sovian/hubal_determined1.png")

image hubal shock = LiveComposite(
    (570, 920),
    (0, 0), "character/sovian/hubal_base1.png",
    (0, 0), "character/sovian/hubal_shock1.png")

image sovian shiver:
    "sovian shock"
    xalign 0.7
    linear 0.03 xalign 0.698
    linear 0.03 xalign 0.7
    linear 0.03 xalign 0.702
    linear 0.03 xalign 0.7
    repeat

image finbard normal = LiveComposite(
    (570, 915),
    (0, 0), "character/sovian/finbard_base1.png",
    (0, 0), "character/sovian/finbard_normal1.png")

image finbard happy = LiveComposite(
    (570, 915),
    (0, 0), "character/sovian/finbard_base1.png",
    (0, 0), "character/sovian/finbard_happy1.png")

image finbard determined = LiveComposite(
    (570, 915),
    (0, 0), "character/sovian/finbard_base1.png",
    (0, 0), "character/sovian/finbard_determined1.png")

image finbard shock = LiveComposite(
    (570, 915),
    (0, 0), "character/sovian/finbard_base1.png",
    (0, 0), "character/sovian/finbard_shock1.png")

image sikorski normal = LiveComposite(
    (570, 936),
    (0, 0), "character/sovian/sikorski_base1.png",
    (0, 0), "character/sovian/sikorski_normal1.png")

image sikorski happy = LiveComposite(
    (570, 936),
    (0, 0), "character/sovian/sikorski_base1.png",
    (0, 0), "character/sovian/sikorski_happy1.png")

image sikorski determined = LiveComposite(
    (570, 936),
    (0, 0), "character/sovian/sikorski_base1.png",
    (0, 0), "character/sovian/sikorski_determined1.png")

image sikorski shock = LiveComposite(
    (570, 936),
    (0, 0), "character/sovian/sikorski_base1.png",
    (0, 0), "character/sovian/sikorski_shock1.png")

image side sovian determined = LiveCrop((110, 85, 350, 210), LiveComposite((570, 920), (0, 0), im.Sepia("character/sovian/sovian_base1.png"), (0, 0), im.Sepia("character/sovian/sovian_determined1.png")))
image side sovian happy = LiveCrop((110, 85, 350, 210), LiveComposite((570, 920), (0, 0), im.Sepia("character/sovian/sovian_base1.png"), (0, 0), im.Sepia("character/sovian/sovian_happy1.png")))
image side sovian normal = LiveCrop((110, 85, 350, 210), LiveComposite((570, 920), (0, 0), im.Sepia("character/sovian/sovian_base1.png"), (0, 0), im.Sepia("character/sovian/sovian_normal1.png")))
image side sovian shock = LiveCrop((110, 85, 350, 210), LiveComposite((570, 920), (0, 0), im.Sepia("character/sovian/sovian_base1.png"), (0, 0), im.Sepia("character/sovian/sovian_shock1.png")))
image side sovian shiver = LiveCrop((110, 85, 350, 210), LiveComposite((570, 920), (0, 0), im.Sepia("character/sovian/sovian_base1.png"), (0, 0), im.Sepia("character/sovian/sovian_shock1.png")))

image side finbard determined = LiveCrop((110, 80, 350, 210), LiveComposite((570, 915), (0, 0), im.Sepia("character/sovian/finbard_base1.png"), (0, 0), im.Sepia("character/sovian/finbard_determined1.png")))
image side finbard happy = LiveCrop((110, 80, 350, 210), LiveComposite((570, 915), (0, 0), im.Sepia("character/sovian/finbard_base1.png"), (0, 0), im.Sepia("character/sovian/finbard_happy1.png")))
image side finbard normal = LiveCrop((110, 80, 350, 210), LiveComposite((570, 915), (0, 0), im.Sepia("character/sovian/finbard_base1.png"), (0, 0), im.Sepia("character/sovian/finbard_normal1.png")))
image side finbard shock = LiveCrop((110, 80, 350, 210), LiveComposite((570, 915), (0, 0), im.Sepia("character/sovian/finbard_base1.png"), (0, 0), im.Sepia("character/sovian/finbard_shock1.png")))

image side sikorski determined = LiveCrop((110, 101, 350, 210), LiveComposite((570, 936), (0, 0), im.Sepia("character/sovian/sikorski_base1.png"), (0, 0), im.Sepia("character/sovian/sikorski_determined1.png")))
image side sikorski happy = LiveCrop((110, 101, 350, 210), LiveComposite((570, 936), (0, 0), im.Sepia("character/sovian/sikorski_base1.png"), (0, 0), im.Sepia("character/sovian/sikorski_happy1.png")))
image side sikorski normal = LiveCrop((110, 101, 350, 210), LiveComposite((570, 936), (0, 0), im.Sepia("character/sovian/sikorski_base1.png"), (0, 0), im.Sepia("character/sovian/sikorski_normal1.png")))
image side sikorski shock = LiveCrop((110, 101, 350, 210), LiveComposite((570, 936), (0, 0), im.Sepia("character/sovian/sikorski_base1.png"), (0, 0), im.Sepia("character/sovian/sikorski_shock1.png")))

image side hubal determined = LiveCrop((110, 85, 350, 210), LiveComposite((570, 920), (0, 0), im.Sepia("character/sovian/hubal_base1.png"), (0, 0), im.Sepia("character/sovian/hubal_determined1.png")))
image side hubal normal = LiveCrop((110, 85, 350, 210), LiveComposite((570, 920), (0, 0), im.Sepia("character/sovian/hubal_base1.png"), (0, 0), im.Sepia("character/sovian/hubal_normal1.png")))
image side hubal shock = LiveCrop((110, 85, 350, 210), LiveComposite((570, 920), (0, 0), im.Sepia("character/sovian/hubal_base1.png"), (0, 0), im.Sepia("character/sovian/hubal_shock1.png")))


########################################################
# Alliance Soldier ###############################################
########################################################
image allied normal = LiveComposite(
    (710, 920),
    (0, 0), "character/allied/allied_base1.png",
    (0, 0), "character/allied/allied_normal1.png")

image allied happy = LiveComposite(
    (710, 920),
    (0, 0), "character/allied/allied_base1.png",
    (0, 0), "character/allied/allied_happy1.png")

image allied determined = LiveComposite(
    (710, 920),
    (0, 0), "character/allied/allied_base1.png",
    (0, 0), "character/allied/allied_determined1.png")

image allied shock = LiveComposite(
    (710, 920),
    (0, 0), "character/allied/allied_base1.png",
    (0, 0), "character/allied/allied_shock1.png")

image wavell normal = LiveComposite(
    (710, 920),
    (0, 0), "character/allied/wavell_base1.png",
    (0, 0), "character/allied/wavell_normal1.png")

image wavell happy = LiveComposite(
    (710, 920),
    (0, 0), "character/allied/wavell_base1.png",
    (0, 0), "character/allied/wavell_happy1.png")

image wavell determined = LiveComposite(
    (710, 920),
    (0, 0), "character/allied/wavell_base1.png",
    (0, 0), "character/allied/wavell_determined1.png")

image wavell shock = LiveComposite(
    (710, 920),
    (0, 0), "character/allied/wavell_base1.png",
    (0, 0), "character/allied/wavell_shock1.png")

image klima normal = LiveComposite(
    (710, 920),
    (0, 0), "character/allied/klima_base1.png",
    (0, 0), "character/allied/klima_normal1.png")

image klima happy = LiveComposite(
    (710, 920),
    (0, 0), "character/allied/klima_base1.png",
    (0, 0), "character/allied/klima_happy1.png")

image klima determined = LiveComposite(
    (710, 920),
    (0, 0), "character/allied/klima_base1.png",
    (0, 0), "character/allied/klima_determined1.png")

image klima shock = LiveComposite(
    (710, 920),
    (0, 0), "character/allied/klima_base1.png",
    (0, 0), "character/allied/klima_shock1.png")

image norda normal = LiveComposite(
    (710, 920),
    (0, 0), "character/allied/norda_base1.png",
    (0, 0), "character/allied/norda_normal1.png")

image norda happy = LiveComposite(
    (710, 920),
    (0, 0), "character/allied/norda_base1.png",
    (0, 0), "character/allied/norda_happy1.png")

image norda determined = LiveComposite(
    (710, 920),
    (0, 0), "character/allied/norda_base1.png",
    (0, 0), "character/allied/norda_determined1.png")

image norda shock = LiveComposite(
    (710, 920),
    (0, 0), "character/allied/norda_base1.png",
    (0, 0), "character/allied/norda_shock1.png")

image side allied determined = LiveCrop((195, 110, 350, 210), LiveComposite((710, 920), (0, 0), im.Sepia("character/allied/allied_base1.png"), (0, 0), im.Sepia("character/allied/allied_determined1.png")))
image side allied happy = LiveCrop((195, 110, 350, 210), LiveComposite((710, 920), (0, 0), im.Sepia("character/allied/allied_base1.png"), (0, 0), im.Sepia("character/allied/allied_happy1.png")))
image side allied normal = LiveCrop((195, 110, 350, 210), LiveComposite((710, 920), (0, 0), im.Sepia("character/allied/allied_base1.png"), (0, 0), im.Sepia("character/allied/allied_normal1.png")))
image side allied shock = LiveCrop((195, 110, 350, 210), LiveComposite((710, 920), (0, 0), im.Sepia("character/allied/allied_base1.png"), (0, 0), im.Sepia("character/allied/allied_shock1.png")))

image side wavell determined = LiveCrop((195, 100, 350, 210), LiveComposite((710, 920), (0, 0), im.Sepia("character/allied/wavell_base1.png"), (0, 0), im.Sepia("character/allied/wavell_determined1.png")))
image side wavell happy = LiveCrop((195, 100, 350, 210), LiveComposite((710, 920), (0, 0), im.Sepia("character/allied/wavell_base1.png"), (0, 0), im.Sepia("character/allied/wavell_happy1.png")))
image side wavell normal = LiveCrop((195, 100, 350, 210), LiveComposite((710, 920), (0, 0), im.Sepia("character/allied/wavell_base1.png"), (0, 0), im.Sepia("character/allied/wavell_normal1.png")))
image side wavell shock = LiveCrop((195, 100, 350, 210), LiveComposite((710, 920), (0, 0), im.Sepia("character/allied/wavell_base1.png"), (0, 0), im.Sepia("character/allied/wavell_shock1.png")))

image side klima determined = LiveCrop((195, 100, 350, 210), LiveComposite((710, 920), (0, 0), im.Sepia("character/allied/klima_base1.png"), (0, 0), im.Sepia("character/allied/klima_determined1.png")))
image side klima happy = LiveCrop((195, 100, 350, 210), LiveComposite((710, 920), (0, 0), im.Sepia("character/allied/klima_base1.png"), (0, 0), im.Sepia("character/allied/klima_happy1.png")))
image side klima normal = LiveCrop((195, 100, 350, 210), LiveComposite((710, 920), (0, 0), im.Sepia("character/allied/klima_base1.png"), (0, 0), im.Sepia("character/allied/klima_normal1.png")))
image side klima shock = LiveCrop((195, 100, 350, 210), LiveComposite((710, 920), (0, 0), im.Sepia("character/allied/klima_base1.png"), (0, 0), im.Sepia("character/allied/klima_shock1.png")))

image side norda determined = LiveCrop((195, 100, 350, 210), LiveComposite((710, 920), (0, 0), im.Sepia("character/allied/norda_base1.png"), (0, 0), im.Sepia("character/allied/norda_determined1.png")))
image side norda happy = LiveCrop((195, 100, 350, 210), LiveComposite((710, 920), (0, 0), im.Sepia("character/allied/norda_base1.png"), (0, 0), im.Sepia("character/allied/norda_happy1.png")))
image side norda normal = LiveCrop((195, 100, 350, 210), LiveComposite((710, 920), (0, 0), im.Sepia("character/allied/norda_base1.png"), (0, 0), im.Sepia("character/allied/norda_normal1.png")))
image side norda shock = LiveCrop((195, 100, 350, 210), LiveComposite((710, 920), (0, 0), im.Sepia("character/allied/norda_base1.png"), (0, 0), im.Sepia("character/allied/norda_shock1.png")))

########################################################
# Fat Man ###############################################
########################################################
image fatman normal = LiveComposite(
    (700, 990),
    (0, 0), "character/fatman/fatman_base1.png",
    (0, 0), "character/fatman/fatman_normal1.png")

image fatman happy = LiveComposite(
    (700, 990),
    (0, 0), "character/fatman/fatman_base1.png",
    (0, 0), "character/fatman/fatman_happy1.png")

image fatman determined = LiveComposite(
    (700, 990),
    (0, 0), "character/fatman/fatman_base1.png",
    (0, 0), "character/fatman/fatman_determined1.png")

image fatman shock = LiveComposite(
    (700, 990),
    (0, 0), "character/fatman/fatman_base1.png",
    (0, 0), "character/fatman/fatman_shock1.png")

image stachie normal = LiveComposite(
    (700, 990),
    (0, 0), "character/fatman/stachie_base1.png",
    (0, 0), "character/fatman/stachie_normal1.png")

image stachie happy = LiveComposite(
    (700, 990),
    (0, 0), "character/fatman/stachie_base1.png",
    (0, 0), "character/fatman/stachie_happy1.png")

image stachie determined = LiveComposite(
    (700, 990),
    (0, 0), "character/fatman/stachie_base1.png",
    (0, 0), "character/fatman/stachie_determined1.png")

image stachie shock = LiveComposite(
    (700, 990),
    (0, 0), "character/fatman/stachie_base1.png",
    (0, 0), "character/fatman/stachie_shock1.png")

image jumbo normal = LiveComposite(
    (700, 987),
    (0, 0), "character/fatman/jumbo_base1.png",
    (0, 0), "character/fatman/jumbo_normal1.png")

image jumbo happy = LiveComposite(
    (700, 987),
    (0, 0), "character/fatman/jumbo_base1.png",
    (0, 0), "character/fatman/jumbo_happy1.png")

image jumbo determined = LiveComposite(
    (700, 987),
    (0, 0), "character/fatman/jumbo_base1.png",
    (0, 0), "character/fatman/jumbo_determined1.png")

image jumbo shock = LiveComposite(
    (700, 987),
    (0, 0), "character/fatman/jumbo_base1.png",
    (0, 0), "character/fatman/jumbo_shock1.png")

image side fatman determined = LiveCrop((180, 85, 350, 210), LiveComposite((700, 990), (0, 0), im.Sepia("character/fatman/fatman_base1.png"), (0, 0), im.Sepia("character/fatman/fatman_determined1.png")))
image side fatman happy = LiveCrop((180, 85, 350, 210), LiveComposite((700, 990), (0, 0), im.Sepia("character/fatman/fatman_base1.png"), (0, 0), im.Sepia("character/fatman/fatman_happy1.png")))
image side fatman normal = LiveCrop((180, 85, 350, 210), LiveComposite((700, 990), (0, 0), im.Sepia("character/fatman/fatman_base1.png"), (0, 0), im.Sepia("character/fatman/fatman_normal1.png")))
image side fatman shock = LiveCrop((180, 85, 350, 210), LiveComposite((700, 990), (0, 0), im.Sepia("character/fatman/fatman_base1.png"), (0, 0), im.Sepia("character/fatman/fatman_shock1.png")))

image side stachie determined = LiveCrop((180, 85, 350, 210), LiveComposite((700, 990), (0, 0), im.Sepia("character/fatman/stachie_base1.png"), (0, 0), im.Sepia("character/fatman/stachie_determined1.png")))
image side stachie happy = LiveCrop((180, 85, 350, 210), LiveComposite((700, 990), (0, 0), im.Sepia("character/fatman/stachie_base1.png"), (0, 0), im.Sepia("character/fatman/stachie_happy1.png")))
image side stachie normal = LiveCrop((180, 85, 350, 210), LiveComposite((700, 990), (0, 0), im.Sepia("character/fatman/stachie_base1.png"), (0, 0), im.Sepia("character/fatman/stachie_normal1.png")))
image side stachie shock = LiveCrop((180, 85, 350, 210), LiveComposite((700, 990), (0, 0), im.Sepia("character/fatman/stachie_base1.png"), (0, 0), im.Sepia("character/fatman/stachie_shock1.png")))

image side jumbo determined = LiveCrop((180, 85, 350, 210), LiveComposite((700, 987), (0, 0), im.Sepia("character/fatman/jumbo_base1.png"), (0, 0), im.Sepia("character/fatman/jumbo_determined1.png")))
image side jumbo happy = LiveCrop((180, 85, 350, 210), LiveComposite((700, 987), (0, 0), im.Sepia("character/fatman/jumbo_base1.png"), (0, 0), im.Sepia("character/fatman/jumbo_happy1.png")))
image side jumbo normal = LiveCrop((180, 85, 350, 210), LiveComposite((700, 987), (0, 0), im.Sepia("character/fatman/jumbo_base1.png"), (0, 0), im.Sepia("character/fatman/jumbo_normal1.png")))
image side jumbo shock = LiveCrop((180, 85, 350, 210), LiveComposite((700, 987), (0, 0), im.Sepia("character/fatman/jumbo_base1.png"), (0, 0), im.Sepia("character/fatman/jumbo_shock1.png")))

########################################################
# Official ###############################################
########################################################
image official normal = LiveComposite(
    (577, 990),
    (0, 0), "character/official/official_normal.png")

image official happy = LiveComposite(
    (577, 990),
    (0, 0), "character/official/official_happy.png")

image official annoyed = LiveComposite(
    (577, 990),
    (0, 0), "character/official/official_annoyed.png")

image cvetkovic normal = LiveComposite(
    (577, 990),
    (0, 0), "character/official/cvetkovic_normal.png")

image cvetkovic happy = LiveComposite(
    (577, 990),
    (0, 0), "character/official/cvetkovic_happy.png")

image cvetkovic annoyed = LiveComposite(
    (577, 990),
    (0, 0), "character/official/cvetkovic_annoyed.png")

image servant1 normal = LiveComposite(
    (577, 990),
    (0, 0), "character/official/servant_normal1.png")

image servant1 happy = LiveComposite(
    (577, 990),
    (0, 0), "character/official/servant_happy1.png")

image servant1 annoyed = LiveComposite(
    (577, 990),
    (0, 0), "character/official/servant_annoyed1.png")

image servant2 normal = LiveComposite(
    (577, 990),
    (0, 0), "character/official/servant_normal2.png")

image servant2 happy = LiveComposite(
    (577, 990),
    (0, 0), "character/official/servant_happy2.png")

image servant2 annoyed = LiveComposite(
    (577, 990),
    (0, 0), "character/official/servant_annoyed2.png")

image agent normal = LiveComposite(
    (577, 990),
    (0, 0), "character/official/agent_normal.png")

image side official normal = LiveCrop((130, 85, 350, 210), LiveComposite((577, 990), (0, 0), im.Sepia("character/official/official_normal.png")))
image side official happy = LiveCrop((130, 85, 350, 210), LiveComposite((577, 990), (0, 0), im.Sepia("character/official/official_happy.png")))
image side official annoyed = LiveCrop((130, 85, 350, 210), LiveComposite((577, 990), (0, 0), im.Sepia("character/official/official_annoyed.png")))

image side cvetkovic normal = LiveCrop((130, 85, 350, 210), LiveComposite((577, 990), (0, 0), im.Sepia("character/official/cvetkovic_normal.png")))
image side cvetkovic happy = LiveCrop((130, 85, 350, 210), LiveComposite((577, 990), (0, 0), im.Sepia("character/official/cvetkovic_happy.png")))
image side cvetkovic annoyed = LiveCrop((130, 85, 350, 210), LiveComposite((577, 990), (0, 0), im.Sepia("character/official/cvetkovic_annoyed.png")))

image side servant1 normal = LiveCrop((130, 85, 350, 210), LiveComposite((577, 990), (0, 0), im.Sepia("character/official/servant_normal1.png")))
image side servant1 happy = LiveCrop((130, 85, 350, 210), LiveComposite((577, 990), (0, 0), im.Sepia("character/official/servant_happy1.png")))
image side servant1 annoyed = LiveCrop((130, 85, 350, 210), LiveComposite((577, 990), (0, 0), im.Sepia("character/official/servant_annoyed1.png")))

image side servant2 normal = LiveCrop((130, 85, 350, 210), LiveComposite((577, 990), (0, 0), im.Sepia("character/official/servant_normal2.png")))
image side servant2 happy = LiveCrop((130, 85, 350, 210), LiveComposite((577, 990), (0, 0), im.Sepia("character/official/servant_happy2.png")))
image side servant2 annoyed = LiveCrop((130, 85, 350, 210), LiveComposite((577, 990), (0, 0), im.Sepia("character/official/servant_annoyed2.png")))

image side agent normal = LiveCrop((110, 75, 350, 210), LiveComposite((577, 990), (0, 0), im.Sepia("character/official/agent_normal.png")))

########################################################
# Politician ###############################################
########################################################
image politician normal = LiveComposite(
    (560, 970),
    (0, 0), "character/politician/politician_normal.png")

image politician happy = LiveComposite(
    (560, 970),
    (0, 0), "character/politician/politician_happy.png")

image politician determined = LiveComposite(
    (560, 970),
    (0, 0), "character/politician/politician_determined.png")

image politician shock = LiveComposite(
    (560, 970),
    (0, 0), "character/politician/politician_shock.png")

image politician2 normal = LiveComposite(
    (560, 970),
    (0, 0), "character/politician/politician_normal2.png")

image politician2 happy = LiveComposite(
    (560, 970),
    (0, 0), "character/politician/politician_happy2.png")

image politician2 determined = LiveComposite(
    (560, 970),
    (0, 0), "character/politician/politician_determined2.png")

image politician2 shock = LiveComposite(
    (560, 970),
    (0, 0), "character/politician/politician_shock2.png")

image reynaud normal = LiveComposite(
    (560, 970),
    (0, 0), "character/politician/reynaud_normal.png")

image reynaud happy = LiveComposite(
    (560, 970),
    (0, 0), "character/politician/reynaud_happy.png")

image reynaud determined = LiveComposite(
    (560, 970),
    (0, 0), "character/politician/reynaud_determined.png")

image reynaud shock = LiveComposite(
    (560, 970),
    (0, 0), "character/politician/reynaud_shock.png")

image quisling normal = LiveComposite(
    (560, 985),
    (0, 0), "character/politician/quisling_normal.png")

image quisling happy = LiveComposite(
    (560, 985),
    (0, 0), "character/politician/quisling_happy.png")

image quisling determined = LiveComposite(
    (560, 985),
    (0, 0), "character/politician/quisling_determined.png")

image quisling shock = LiveComposite(
    (560, 985),
    (0, 0), "character/politician/quisling_shock.png")

image side politician normal = LiveCrop((110, 70, 350, 210), LiveComposite((560, 970), (0, 0), im.Sepia("character/politician/politician_normal.png")))
image side politician happy = LiveCrop((110, 70, 350, 210), LiveComposite((560, 970), (0, 0), im.Sepia("character/politician/politician_happy.png")))
image side politician determined = LiveCrop((110, 70, 350, 210), LiveComposite((560, 970), (0, 0), im.Sepia("character/politician/politician_determined.png")))
image side politician shock = LiveCrop((110, 70, 350, 210), LiveComposite((560, 970), (0, 0), im.Sepia("character/politician/politician_shock.png")))

image side politician2 normal = LiveCrop((110, 70, 350, 210), LiveComposite((560, 970), (0, 0), im.Sepia("character/politician/politician_normal2.png")))
image side politician2 happy = LiveCrop((110, 70, 350, 210), LiveComposite((560, 970), (0, 0), im.Sepia("character/politician/politician_happy2.png")))
image side politician2 determined = LiveCrop((110, 70, 350, 210), LiveComposite((560, 970), (0, 0), im.Sepia("character/politician/politician_determined2.png")))
image side politician2 shock = LiveCrop((110, 70, 350, 210), LiveComposite((560, 970), (0, 0), im.Sepia("character/politician/politician_shock2.png")))

image side reynaud normal = LiveCrop((110, 70, 350, 210), LiveComposite((560, 970), (0, 0), im.Sepia("character/politician/reynaud_normal.png")))
image side reynaud happy = LiveCrop((110, 70, 350, 210), LiveComposite((560, 970), (0, 0), im.Sepia("character/politician/reynaud_happy.png")))
image side reynaud determined = LiveCrop((110, 70, 350, 210), LiveComposite((560, 970), (0, 0), im.Sepia("character/politician/reynaud_determined.png")))
image side reynaud shock = LiveCrop((110, 70, 350, 210), LiveComposite((560, 970), (0, 0), im.Sepia("character/politician/reynaud_shock.png")))

image side quisling normal = LiveCrop((110, 85, 350, 210), LiveComposite((560, 970), (0, 0), im.Sepia("character/politician/quisling_normal.png")))
image side quisling happy = LiveCrop((110, 85, 350, 210), LiveComposite((560, 970), (0, 0), im.Sepia("character/politician/quisling_happy.png")))
image side quisling determined = LiveCrop((110, 85, 350, 210), LiveComposite((560, 970), (0, 0), im.Sepia("character/politician/quisling_determined.png")))
image side quisling shock = LiveCrop((110, 85, 350, 210), LiveComposite((560, 970), (0, 0), im.Sepia("character/politician/quisling_shock.png")))

########################################################
# Woman ###############################################
########################################################
image woman normal = LiveComposite(
    (570, 950),
    (0, 0), "character/woman/woman_base1.png",
    (0, 0), "character/woman/woman_normal1.png")

image woman happy = LiveComposite(
    (570, 950),
    (0, 0), "character/woman/woman_base1.png",
    (0, 0), "character/woman/woman_happy1.png")

image woman determined = LiveComposite(
    (570, 950),
    (0, 0), "character/woman/woman_base1.png",
    (0, 0), "character/woman/woman_determined1.png")

image woman shock = LiveComposite(
    (570, 950),
    (0, 0), "character/woman/woman_base1.png",
    (0, 0), "character/woman/woman_shock1.png")

image nurse normal = LiveComposite(
    (570, 950),
    (0, 0), "character/woman/nurse_base1.png",
    (0, 0), "character/woman/nurse_normal1.png")

image nurse happy = LiveComposite(
    (570, 950),
    (0, 0), "character/woman/nurse_base1.png",
    (0, 0), "character/woman/nurse_happy1.png")

image nurse determined = LiveComposite(
    (570, 950),
    (0, 0), "character/woman/nurse_base1.png",
    (0, 0), "character/woman/nurse_determined1.png")

image nurse shock = LiveComposite(
    (570, 950),
    (0, 0), "character/woman/nurse_base1.png",
    (0, 0), "character/woman/nurse_shock1.png")

image maid normal = LiveComposite(
    (570, 950),
    (0, 0), "character/woman/maid_base1.png",
    (0, 0), "character/woman/maid_normal1.png")

image maid happy = LiveComposite(
    (570, 950),
    (0, 0), "character/woman/maid_base1.png",
    (0, 0), "character/woman/maid_happy1.png")

image maid determined = LiveComposite(
    (570, 950),
    (0, 0), "character/woman/maid_base1.png",
    (0, 0), "character/woman/maid_determined1.png")
                                                           
image maid shock = LiveComposite(
    (570, 950),
    (0, 0), "character/woman/maid_base1.png",
    (0, 0), "character/woman/maid_shock1.png")

image sima normal = LiveComposite(
    (570, 950),
    (0, 0), "character/woman/sima_base1.png",
    (0, 0), "character/woman/sima_normal1.png")

image sima happy = LiveComposite(
    (570, 950),
    (0, 0), "character/woman/sima_base1.png",
    (0, 0), "character/woman/sima_happy1.png")

image sima determined = LiveComposite(
    (570, 950),
    (0, 0), "character/woman/sima_base1.png",
    (0, 0), "character/woman/sima_determined1.png")

image sima shock = LiveComposite(
    (570, 950),
    (0, 0), "character/woman/sima_base1.png",
    (0, 0), "character/woman/sima_shock1.png")

image valkenhorst normal = LiveComposite(
    (570, 950),
    (0, 0), "character/woman/valkenhorst_base1.png",
    (0, 0), "character/woman/valkenhorst_normal1.png")

image valkenhorst happy = LiveComposite(
    (570, 950),
    (0, 0), "character/woman/valkenhorst_base1.png",
    (0, 0), "character/woman/valkenhorst_happy1.png")

image valkenhorst determined = LiveComposite(
    (570, 950),
    (0, 0), "character/woman/valkenhorst_base1.png",
    (0, 0), "character/woman/valkenhorst_determined1.png")

image valkenhorst shock = LiveComposite(
    (570, 950),
    (0, 0), "character/woman/valkenhorst_base1.png",
    (0, 0), "character/woman/valkenhorst_shock1.png")

image side woman determined = LiveCrop((115, 85, 350, 210), LiveComposite((500, 950), (0, 0), im.Sepia("character/woman/woman_base1.png"), (0, 0), im.Sepia("character/woman/woman_determined1.png")))
image side woman happy = LiveCrop((115, 85, 350, 210), LiveComposite((500, 950), (0, 0), im.Sepia("character/woman/woman_base1.png"), (0, 0), im.Sepia("character/woman/woman_happy1.png")))
image side woman normal = LiveCrop((115, 85, 350, 210), LiveComposite((500, 950), (0, 0), im.Sepia("character/woman/woman_base1.png"), (0, 0), im.Sepia("character/woman/woman_normal1.png")))
image side woman shock = LiveCrop((115, 85, 350, 210), LiveComposite((500, 950), (0, 0), im.Sepia("character/woman/woman_base1.png"), (0, 0), im.Sepia("character/woman/woman_shock1.png")))

image side nurse determined = LiveCrop((115, 85, 350, 210), LiveComposite((500, 950), (0, 0), im.Sepia("character/woman/nurse_base1.png"), (0, 0), im.Sepia("character/woman/nurse_determined1.png")))
image side nurse happy = LiveCrop((115, 85, 350, 210), LiveComposite((500, 950), (0, 0), im.Sepia("character/woman/nurse_base1.png"), (0, 0), im.Sepia("character/woman/nurse_happy1.png")))
image side nurse normal = LiveCrop((115, 85, 350, 210), LiveComposite((500, 950), (0, 0), im.Sepia("character/woman/nurse_base1.png"), (0, 0), im.Sepia("character/woman/nurse_normal1.png")))
image side nurse shock = LiveCrop((115, 85, 350, 210), LiveComposite((500, 950), (0, 0), im.Sepia("character/woman/nurse_base1.png"), (0, 0), im.Sepia("character/woman/nurse_shock1.png")))

image side maid determined = LiveCrop((115, 85, 350, 210), LiveComposite((500, 950), (0, 0), im.Sepia("character/woman/maid_base1.png"), (0, 0), im.Sepia("character/woman/maid_determined1.png")))
image side maid happy = LiveCrop((115, 85, 350, 210), LiveComposite((500, 950), (0, 0), im.Sepia("character/woman/maid_base1.png"), (0, 0), im.Sepia("character/woman/maid_happy1.png")))
image side maid normal = LiveCrop((115, 85, 350, 210), LiveComposite((500, 950), (0, 0), im.Sepia("character/woman/maid_base1.png"), (0, 0), im.Sepia("character/woman/maid_normal1.png")))
image side maid shock = LiveCrop((115, 85, 350, 210), LiveComposite((500, 950), (0, 0), im.Sepia("character/woman/maid_base1.png"), (0, 0), im.Sepia("character/woman/maid_shock1.png")))

image side sima determined = LiveCrop((115, 85, 350, 210), LiveComposite((500, 950), (0, 0), im.Sepia("character/woman/sima_base1.png"), (0, 0), im.Sepia("character/woman/sima_determined1.png")))
image side sima happy = LiveCrop((115, 85, 350, 210), LiveComposite((500, 950), (0, 0), im.Sepia("character/woman/sima_base1.png"), (0, 0), im.Sepia("character/woman/sima_happy1.png")))
image side sima normal = LiveCrop((115, 85, 350, 210), LiveComposite((500, 950), (0, 0), im.Sepia("character/woman/sima_base1.png"), (0, 0), im.Sepia("character/woman/sima_normal1.png")))
image side sima shock = LiveCrop((115, 85, 350, 210), LiveComposite((500, 950), (0, 0), im.Sepia("character/woman/sima_base1.png"), (0, 0), im.Sepia("character/woman/sima_shock1.png")))

image side valkenhorst determined = LiveCrop((115, 115, 350, 210), LiveComposite((500, 950), (0, 0), im.Sepia("character/woman/valkenhorst_base1.png"), (0, 0), im.Sepia("character/woman/valkenhorst_determined1.png")))
image side valkenhorst happy = LiveCrop((115, 115, 350, 210), LiveComposite((500, 950), (0, 0), im.Sepia("character/woman/valkenhorst_base1.png"), (0, 0), im.Sepia("character/woman/valkenhorst_happy1.png")))
image side valkenhorst normal = LiveCrop((115, 115, 350, 210), LiveComposite((500, 950), (0, 0), im.Sepia("character/woman/valkenhorst_base1.png"), (0, 0), im.Sepia("character/woman/valkenhorst_normal1.png")))
image side valkenhorst shock = LiveCrop((115, 115, 350, 210), LiveComposite((500, 950), (0, 0), im.Sepia("character/woman/valkenhorst_base1.png"), (0, 0), im.Sepia("character/woman/valkenhorst_shock1.png")))

########################################################
# Old Woman ###############################################
########################################################
image oldwoman determined = LiveComposite(
    (400, 870),
    (0, 0), "character/oldwoman/oldwoman_base1.png",
    (0, 0), "character/oldwoman/oldwoman_determined1.png")

image oldwoman normal = LiveComposite(
    (400, 870),
    (0, 0), "character/oldwoman/oldwoman_base1.png",
    (0, 0), "character/oldwoman/oldwoman_normal1.png")

image oldwoman happy = LiveComposite(
    (400, 870),
    (0, 0), "character/oldwoman/oldwoman_base1.png",
    (0, 0), "character/oldwoman/oldwoman_happy1.png")

image oldwoman shock = LiveComposite(
    (400, 870),
    (0, 0), "character/oldwoman/oldwoman_base1.png",
    (0, 0), "character/oldwoman/oldwoman_shock1.png")

image desertoldwoman determined = LiveComposite(
    (400, 870),
    (0, 0), "character/oldwoman/oldwoman_base2.png",
    (0, 0), "character/oldwoman/oldwoman_determined2.png")

image desertoldwoman normal = LiveComposite(
    (400, 870),
    (0, 0), "character/oldwoman/oldwoman_base2.png",
    (0, 0), "character/oldwoman/oldwoman_normal2.png")

image desertoldwoman happy = LiveComposite(
    (400, 870),
    (0, 0), "character/oldwoman/oldwoman_base2.png",
    (0, 0), "character/oldwoman/oldwoman_happy2.png")

image desertoldwoman shock = LiveComposite(
    (400, 870),
    (0, 0), "character/oldwoman/oldwoman_base2.png",
    (0, 0), "character/oldwoman/oldwoman_shock2.png")

image simovic determined = LiveComposite(
    (400, 894),
    (0, 0), "character/oldwoman/simovic_base1.png",
    (0, 0), "character/oldwoman/simovic_determined1.png")

image simovic normal = LiveComposite(
    (400, 894),
    (0, 0), "character/oldwoman/simovic_base1.png",
    (0, 0), "character/oldwoman/simovic_normal1.png")

image simovic happy = LiveComposite(
    (400, 894),
    (0, 0), "character/oldwoman/simovic_base1.png",
    (0, 0), "character/oldwoman/simovic_happy1.png")

image simovic shock = LiveComposite(
    (400, 894),
    (0, 0), "character/oldwoman/simovic_base1.png",
    (0, 0), "character/oldwoman/simovic_shock1.png")

image side oldwoman determined = LiveCrop((40, 60, 350, 210), LiveComposite((400, 870), (0, 0), im.Sepia("character/oldwoman/oldwoman_base1.png"), (0, 0), im.Sepia("character/oldwoman/oldwoman_determined1.png")))
image side oldwoman happy = LiveCrop((40, 60, 350, 210), LiveComposite((400, 870), (0, 0), im.Sepia("character/oldwoman/oldwoman_base1.png"), (0, 0), im.Sepia("character/oldwoman/oldwoman_happy1.png")))
image side oldwoman normal = LiveCrop((40, 60, 350, 210), LiveComposite((400, 870), (0, 0), im.Sepia("character/oldwoman/oldwoman_base1.png"), (0, 0), im.Sepia("character/oldwoman/oldwoman_normal1.png")))
image side oldwoman shock = LiveCrop((40, 60, 350, 210), LiveComposite((400, 870), (0, 0), im.Sepia("character/oldwoman/oldwoman_base1.png"), (0, 0), im.Sepia("character/oldwoman/oldwoman_shock1.png")))

image side desertoldwoman determined = LiveCrop((40, 60, 350, 210), LiveComposite((400, 870), (0, 0), im.Sepia("character/oldwoman/oldwoman_base2.png"), (0, 0), im.Sepia("character/oldwoman/oldwoman_determined2.png")))
image side desertoldwoman happy = LiveCrop((40, 60, 350, 210), LiveComposite((400, 870), (0, 0), im.Sepia("character/oldwoman/oldwoman_base2.png"), (0, 0), im.Sepia("character/oldwoman/oldwoman_happy2.png")))
image side desertoldwoman normal = LiveCrop((40, 60, 350, 210), LiveComposite((400, 870), (0, 0), im.Sepia("character/oldwoman/oldwoman_base2.png"), (0, 0), im.Sepia("character/oldwoman/oldwoman_normal2.png")))
image side desertoldwoman shock = LiveCrop((40, 60, 350, 210), LiveComposite((400, 870), (0, 0), im.Sepia("character/oldwoman/oldwoman_base2.png"), (0, 0), im.Sepia("character/oldwoman/oldwoman_shock2.png")))

image side simovic determined = LiveCrop((40, 80, 350, 210), LiveComposite((400, 894), (0, 0), im.Sepia("character/oldwoman/simovic_base1.png"), (0, 0), im.Sepia("character/oldwoman/simovic_determined1.png")))
image side simovic happy = LiveCrop((40, 80, 350, 210), LiveComposite((400, 894), (0, 0), im.Sepia("character/oldwoman/simovic_base1.png"), (0, 0), im.Sepia("character/oldwoman/simovic_happy1.png")))
image side simovic normal = LiveCrop((40, 80, 350, 210), LiveComposite((400, 894), (0, 0), im.Sepia("character/oldwoman/simovic_base1.png"), (0, 0), im.Sepia("character/oldwoman/simovic_normal1.png")))
image side simovic shock = LiveCrop((40, 80, 350, 210), LiveComposite((400, 894), (0, 0), im.Sepia("character/oldwoman/simovic_base1.png"), (0, 0), im.Sepia("character/oldwoman/simovic_shock1.png")))

########################################################
# Youth ###############################################
########################################################
image youth determined = LiveComposite(
    (440, 800),
    (0, 0), "character/youth/youth_base1.png",
    (0, 0), "character/youth/youth_determined1.png")

image youth normal = LiveComposite(
    (440, 800),
    (0, 0), "character/youth/youth_base1.png",
    (0, 0), "character/youth/youth_normal1.png")

image youth happy = LiveComposite(
    (440, 800),
    (0, 0), "character/youth/youth_base1.png",
    (0, 0), "character/youth/youth_happy1.png")

image youth shock = LiveComposite(
    (440, 800),
    (0, 0), "character/youth/youth_base1.png",
    (0, 0), "character/youth/youth_shock1.png")

image desertyouth determined = LiveComposite(
    (440, 800),
    (0, 0), "character/youth/desertyouth_base1.png",
    (0, 0), "character/youth/desertyouth_determined1.png")

image desertyouth normal = LiveComposite(
    (440, 800),
    (0, 0), "character/youth/desertyouth_base1.png",
    (0, 0), "character/youth/desertyouth_normal1.png")

image desertyouth happy = LiveComposite(
    (440, 800),
    (0, 0), "character/youth/desertyouth_base1.png",
    (0, 0), "character/youth/desertyouth_happy1.png")

image desertyouth shock = LiveComposite(
    (440, 800),
    (0, 0), "character/youth/desertyouth_base1.png",
    (0, 0), "character/youth/desertyouth_shock1.png")

image daniayouth determined = LiveComposite(
    (440, 869),
    (0, 0), "character/youth/daniayouth_base1.png",
    (0, 0), "character/youth/daniayouth_determined1.png")

image daniayouth normal = LiveComposite(
    (440, 869),
    (0, 0), "character/youth/daniayouth_base1.png",
    (0, 0), "character/youth/daniayouth_normal1.png")

image daniayouth happy = LiveComposite(
    (440, 869),
    (0, 0), "character/youth/daniayouth_base1.png",
    (0, 0), "character/youth/daniayouth_happy1.png")

image daniayouth shock = LiveComposite(
    (440, 869),
    (0, 0), "character/youth/daniayouth_base1.png",
    (0, 0), "character/youth/daniayouth_shock1.png")

image zipanguyouth determined = LiveComposite(
    (440, 800),
    (0, 0), "character/youth/zipanguyouth_base1.png",
    (0, 0), "character/youth/zipanguyouth_determined1.png")

image zipanguyouth normal = LiveComposite(
    (440, 800),
    (0, 0), "character/youth/zipanguyouth_base1.png",
    (0, 0), "character/youth/zipanguyouth_normal1.png")

image zipanguyouth happy = LiveComposite(
    (440, 800),
    (0, 0), "character/youth/zipanguyouth_base1.png",
    (0, 0), "character/youth/zipanguyouth_happy1.png")

image zipanguyouth shock = LiveComposite(
    (440, 800),
    (0, 0), "character/youth/zipanguyouth_base1.png",
    (0, 0), "character/youth/zipanguyouth_shock1.png")

image prior determined = LiveComposite(
    (440, 900),
    (0, 0), "character/youth/prior_base1.png",
    (0, 0), "character/youth/prior_determined1.png")

image prior normal = LiveComposite(
    (440, 900),
    (0, 0), "character/youth/prior_base1.png",
    (0, 0), "character/youth/prior_normal1.png")

image prior happy = LiveComposite(
    (440, 900),
    (0, 0), "character/youth/prior_base1.png",
    (0, 0), "character/youth/prior_happy1.png")

image prior shock = LiveComposite(
    (440, 900),
    (0, 0), "character/youth/prior_base1.png",
    (0, 0), "character/youth/prior_shock1.png")

image christian determined = LiveComposite(
    (606, 830),
    (0, 0), "character/youth/christian_base1.png",
    (0, 0), "character/youth/christian_determined1.png")

image christian normal = LiveComposite(
    (606, 830),
    (0, 0), "character/youth/christian_base1.png",
    (0, 0), "character/youth/christian_normal1.png")

image christian happy = LiveComposite(
    (606, 830),
    (0, 0), "character/youth/christian_base1.png",
    (0, 0), "character/youth/christian_happy1.png")

image christian shock = LiveComposite(
    (606, 830),
    (0, 0), "character/youth/christian_base1.png",
    (0, 0), "character/youth/christian_shock1.png")

image borkind determined = LiveComposite(
    (468, 800),
    (0, 0), "character/youth/borkind_base1.png",
    (0, 0), "character/youth/borkind_determined1.png")

image borkind normal = LiveComposite(
    (468, 800),
    (0, 0), "character/youth/borkind_base1.png",
    (0, 0), "character/youth/borkind_normal1.png")

image borkind happy = LiveComposite(
    (468, 800),
    (0, 0), "character/youth/borkind_base1.png",
    (0, 0), "character/youth/borkind_happy1.png")

image borkind shock = LiveComposite(
    (468, 800),
    (0, 0), "character/youth/borkind_base1.png",
    (0, 0), "character/youth/borkind_shock1.png")

image halifax determined = LiveComposite(
    (367, 810),
    (0, 0), "character/youth/halifax_base1.png",
    (0, 0), "character/youth/halifax_determined1.png")

image halifax normal = LiveComposite(
    (367, 810),
    (0, 0), "character/youth/halifax_base1.png",
    (0, 0), "character/youth/halifax_normal1.png")

image halifax happy = LiveComposite(
    (367, 810),
    (0, 0), "character/youth/halifax_base1.png",
    (0, 0), "character/youth/halifax_happy1.png")

image halifax shock = LiveComposite(
    (367, 810),
    (0, 0), "character/youth/halifax_base1.png",
    (0, 0), "character/youth/halifax_shock1.png")

image cavallero determined = LiveComposite(
    (468, 843),
    (0, 0), "character/youth/cavallero_base1.png",
    (0, 0), "character/youth/cavallero_determined1.png")

image cavallero normal = LiveComposite(
    (468, 843),
    (0, 0), "character/youth/cavallero_base1.png",
    (0, 0), "character/youth/cavallero_normal1.png")

image cavallero happy = LiveComposite(
    (468, 843),
    (0, 0), "character/youth/cavallero_base1.png",
    (0, 0), "character/youth/cavallero_happy1.png")

image cavallero shock = LiveComposite(
    (468, 843),
    (0, 0), "character/youth/cavallero_base1.png",
    (0, 0), "character/youth/cavallero_shock1.png")

image gestapo determined = LiveComposite(
    (468, 800),
    (0, 0), "character/youth/gestapo_base1.png",
    (0, 0), "character/youth/gestapo_determined1.png")

image gestapo normal = LiveComposite(
    (468, 800),
    (0, 0), "character/youth/gestapo_base1.png",
    (0, 0), "character/youth/gestapo_normal1.png")

image gestapo happy = LiveComposite(
    (468, 800),
    (0, 0), "character/youth/gestapo_base1.png",
    (0, 0), "character/youth/gestapo_happy1.png")

image gestapo shock = LiveComposite(
    (468, 800),
    (0, 0), "character/youth/gestapo_base1.png",
    (0, 0), "character/youth/gestapo_shock1.png")

image pavlov determined = LiveComposite(
    (440, 810),
    (0, 0), "character/youth/pavlov_base1.png",
    (0, 0), "character/youth/pavlov_determined1.png")

image pavlov normal = LiveComposite(
    (440, 810),
    (0, 0), "character/youth/pavlov_base1.png",
    (0, 0), "character/youth/pavlov_normal1.png")

image pavlov happy = LiveComposite(
    (440, 810),
    (0, 0), "character/youth/pavlov_base1.png",
    (0, 0), "character/youth/pavlov_happy1.png")

image pavlov shock = LiveComposite(
    (440, 810),
    (0, 0), "character/youth/pavlov_base1.png",
    (0, 0), "character/youth/pavlov_shock1.png")

image vasey determined = LiveComposite(
    (440, 810),
    (0, 0), "character/youth/vasey_base1.png",
    (0, 0), "character/youth/vasey_determined1.png")

image vasey normal = LiveComposite(
    (440, 810),
    (0, 0), "character/youth/vasey_base1.png",
    (0, 0), "character/youth/vasey_normal1.png")

image vasey happy = LiveComposite(
    (440, 810),
    (0, 0), "character/youth/vasey_base1.png",
    (0, 0), "character/youth/vasey_happy1.png")

image vasey shock = LiveComposite(
    (440, 810),
    (0, 0), "character/youth/vasey_base1.png",
    (0, 0), "character/youth/vasey_shock1.png")

image dietling determined = LiveComposite(
    (440, 810),
    (0, 0), "character/youth/dietling_base1.png",
    (0, 0), "character/youth/dietling_determined1.png")

image dietling normal = LiveComposite(
    (440, 810),
    (0, 0), "character/youth/dietling_base1.png",
    (0, 0), "character/youth/dietling_normal1.png")

image dietling happy = LiveComposite(
    (440, 810),
    (0, 0), "character/youth/dietling_base1.png",
    (0, 0), "character/youth/dietling_happy1.png")

image dietling shock = LiveComposite(
    (440, 810),
    (0, 0), "character/youth/dietling_base1.png",
    (0, 0), "character/youth/dietling_shock1.png")

image zchaal determined = LiveComposite(
    (440, 810),
    (0, 0), "character/youth/zchaal_base1.png",
    (0, 0), "character/youth/zchaal_determined1.png")

image zchaal normal = LiveComposite(
    (440, 810),
    (0, 0), "character/youth/zchaal_base1.png",
    (0, 0), "character/youth/zchaal_normal1.png")

image zchaal happy = LiveComposite(
    (440, 810),
    (0, 0), "character/youth/zchaal_base1.png",
    (0, 0), "character/youth/zchaal_happy1.png")

image zchaal shock = LiveComposite(
    (440, 810),
    (0, 0), "character/youth/zchaal_base1.png",
    (0, 0), "character/youth/zchaal_shock1.png")

image side youth determined = LiveCrop((40, 30, 350, 210), LiveComposite((440, 800), (0, 0), im.Sepia("character/youth/youth_base1.png"), (0, 0), im.Sepia("character/youth/youth_determined1.png")))
image side youth happy = LiveCrop((40, 30, 350, 210), LiveComposite((440, 800), (0, 0), im.Sepia("character/youth/youth_base1.png"), (0, 0), im.Sepia("character/youth/youth_happy1.png")))
image side youth normal = LiveCrop((40, 30, 350, 210), LiveComposite((440, 800), (0, 0), im.Sepia("character/youth/youth_base1.png"), (0, 0), im.Sepia("character/youth/youth_normal1.png")))
image side youth shock = LiveCrop((40, 30, 350, 210), LiveComposite((440, 800), (0, 0), im.Sepia("character/youth/youth_base1.png"), (0, 0), im.Sepia("character/youth/youth_shock1.png")))

image side desertyouth determined = LiveCrop((40, 30, 350, 210), LiveComposite((440, 800), (0, 0), im.Sepia("character/youth/desertyouth_base1.png"), (0, 0), im.Sepia("character/youth/desertyouth_determined1.png")))
image side desertyouth happy = LiveCrop((40, 30, 350, 210), LiveComposite((440, 800), (0, 0), im.Sepia("character/youth/desertyouth_base1.png"), (0, 0), im.Sepia("character/youth/desertyouth_happy1.png")))
image side desertyouth normal = LiveCrop((40, 30, 350, 210), LiveComposite((440, 800), (0, 0), im.Sepia("character/youth/desertyouth_base1.png"), (0, 0), im.Sepia("character/youth/desertyouth_normal1.png")))
image side desertyouth shock = LiveCrop((40, 30, 350, 210), LiveComposite((440, 800), (0, 0), im.Sepia("character/youth/desertyouth_base1.png"), (0, 0), im.Sepia("character/youth/desertyouth_shock1.png")))

image side daniayouth determined = LiveCrop((40, 99, 350, 210), LiveComposite((440, 869), (0, 0), im.Sepia("character/youth/daniayouth_base1.png"), (0, 0), im.Sepia("character/youth/daniayouth_determined1.png")))
image side daniayouth happy = LiveCrop((40, 99, 350, 210), LiveComposite((440, 869), (0, 0), im.Sepia("character/youth/daniayouth_base1.png"), (0, 0), im.Sepia("character/youth/daniayouth_happy1.png")))
image side daniayouth normal = LiveCrop((40, 99, 350, 210), LiveComposite((440, 869), (0, 0), im.Sepia("character/youth/daniayouth_base1.png"), (0, 0), im.Sepia("character/youth/daniayouth_normal1.png")))
image side daniayouth shock = LiveCrop((40, 99, 350, 210), LiveComposite((440, 869), (0, 0), im.Sepia("character/youth/daniayouth_base1.png"), (0, 0), im.Sepia("character/youth/daniayouth_shock1.png")))

image side zipanguyouth determined = LiveCrop((40, 30, 350, 210), LiveComposite((440, 800), (0, 0), im.Sepia("character/youth/zipanguyouth_base1.png"), (0, 0), im.Sepia("character/youth/zipanguyouth_determined1.png")))
image side zipanguyouth happy = LiveCrop((40, 30, 350, 210), LiveComposite((440, 800), (0, 0), im.Sepia("character/youth/zipanguyouth_base1.png"), (0, 0), im.Sepia("character/youth/zipanguyouth_happy1.png")))
image side zipanguyouth normal = LiveCrop((40, 30, 350, 210), LiveComposite((440, 800), (0, 0), im.Sepia("character/youth/zipanguyouth_base1.png"), (0, 0), im.Sepia("character/youth/zipanguyouth_normal1.png")))
image side zipanguyouth shock = LiveCrop((40, 30, 350, 210), LiveComposite((440, 800), (0, 0), im.Sepia("character/youth/zipanguyouth_base1.png"), (0, 0), im.Sepia("character/youth/zipanguyouth_shock1.png")))

image side prior determined = LiveCrop((40, 99, 350, 210), LiveComposite((440, 900), (0, 0), im.Sepia("character/youth/prior_base1.png"), (0, 0), im.Sepia("character/youth/prior_determined1.png")))
image side prior happy = LiveCrop((40, 99, 350, 210), LiveComposite((440, 900), (0, 0), im.Sepia("character/youth/prior_base1.png"), (0, 0), im.Sepia("character/youth/prior_happy1.png")))
image side prior normal = LiveCrop((40, 99, 350, 210), LiveComposite((440, 900), (0, 0), im.Sepia("character/youth/prior_base1.png"), (0, 0), im.Sepia("character/youth/prior_normal1.png")))
image side prior shock = LiveCrop((40, 99, 350, 210), LiveComposite((440, 900), (0, 0), im.Sepia("character/youth/prior_base1.png"), (0, 0), im.Sepia("character/youth/prior_shock1.png")))

image side christian determined = LiveCrop((123, 30, 350, 210), LiveComposite((440, 869), (0, 0), im.Sepia("character/youth/christian_base1.png"), (0, 0), im.Sepia("character/youth/christian_determined1.png")))
image side christian happy = LiveCrop((123, 30, 350, 210), LiveComposite((440, 869), (0, 0), im.Sepia("character/youth/christian_base1.png"), (0, 0), im.Sepia("character/youth/christian_happy1.png")))
image side christian normal = LiveCrop((123, 30, 350, 210), LiveComposite((440, 869), (0, 0), im.Sepia("character/youth/christian_base1.png"), (0, 0), im.Sepia("character/youth/christian_normal1.png")))
image side christian shock = LiveCrop((123, 30, 350, 210), LiveComposite((440, 869), (0, 0), im.Sepia("character/youth/christian_base1.png"), (0, 0), im.Sepia("character/youth/christian_shock1.png")))

image side borkind determined = LiveCrop((40, 30, 350, 210), LiveComposite((468, 800), (0, 0), im.Sepia("character/youth/borkind_base1.png"), (0, 0), im.Sepia("character/youth/borkind_determined1.png")))
image side borkind happy = LiveCrop((40, 30, 350, 210), LiveComposite((468, 800), (0, 0), im.Sepia("character/youth/borkind_base1.png"), (0, 0), im.Sepia("character/youth/borkind_happy1.png")))
image side borkind normal = LiveCrop((40, 30, 350, 210), LiveComposite((468, 800), (0, 0), im.Sepia("character/youth/borkind_base1.png"), (0, 0), im.Sepia("character/youth/borkind_normal1.png")))
image side borkind shock = LiveCrop((40, 30, 350, 210), LiveComposite((468, 800), (0, 0), im.Sepia("character/youth/borkind_base1.png"), (0, 0), im.Sepia("character/youth/borkind_shock1.png")))

image side halifax determined = LiveCrop((10, 30, 350, 210), LiveComposite((440, 869), (0, 0), im.Sepia("character/youth/halifax_base1.png"), (0, 0), im.Sepia("character/youth/halifax_determined1.png")))
image side halifax happy = LiveCrop((10, 30, 350, 210), LiveComposite((440, 869), (0, 0), im.Sepia("character/youth/halifax_base1.png"), (0, 0), im.Sepia("character/youth/halifax_happy1.png")))
image side halifax normal = LiveCrop((10, 30, 350, 210), LiveComposite((440, 869), (0, 0), im.Sepia("character/youth/halifax_base1.png"), (0, 0), im.Sepia("character/youth/halifax_normal1.png")))
image side halifax shock = LiveCrop((10, 30, 350, 210), LiveComposite((440, 869), (0, 0), im.Sepia("character/youth/halifax_base1.png"), (0, 0), im.Sepia("character/youth/halifax_shock1.png")))

image side cavallero determined = LiveCrop((40, 70, 350, 210), LiveComposite((468, 843), (0, 0), im.Sepia("character/youth/cavallero_base1.png"), (0, 0), im.Sepia("character/youth/cavallero_determined1.png")))
image side cavallero happy = LiveCrop((40, 70, 350, 210), LiveComposite((468, 843), (0, 0), im.Sepia("character/youth/cavallero_base1.png"), (0, 0), im.Sepia("character/youth/cavallero_happy1.png")))
image side cavallero normal = LiveCrop((40, 70, 350, 210), LiveComposite((468, 843), (0, 0), im.Sepia("character/youth/cavallero_base1.png"), (0, 0), im.Sepia("character/youth/cavallero_normal1.png")))
image side cavallero shock = LiveCrop((40, 70, 350, 210), LiveComposite((468, 843), (0, 0), im.Sepia("character/youth/cavallero_base1.png"), (0, 0), im.Sepia("character/youth/cavallero_shock1.png")))

image side gestapo determined = LiveCrop((40, 30, 350, 210), LiveComposite((468, 800), (0, 0), im.Sepia("character/youth/gestapo_base1.png"), (0, 0), im.Sepia("character/youth/gestapo_determined1.png")))
image side gestapo happy = LiveCrop((40, 30, 350, 210), LiveComposite((468, 800), (0, 0), im.Sepia("character/youth/gestapo_base1.png"), (0, 0), im.Sepia("character/youth/gestapo_happy1.png")))
image side gestapo normal = LiveCrop((40, 30, 350, 210), LiveComposite((468, 800), (0, 0), im.Sepia("character/youth/gestapo_base1.png"), (0, 0), im.Sepia("character/youth/gestapo_normal1.png")))
image side gestapo shock = LiveCrop((40, 30, 350, 210), LiveComposite((468, 800), (0, 0), im.Sepia("character/youth/gestapo_base1.png"), (0, 0), im.Sepia("character/youth/gestapo_shock1.png")))

image side pavlov determined = LiveCrop((40, 70, 350, 210), LiveComposite((440, 843), (0, 0), im.Sepia("character/youth/pavlov_base1.png"), (0, 0), im.Sepia("character/youth/pavlov_determined1.png")))
image side pavlov happy = LiveCrop((40, 70, 350, 210), LiveComposite((440, 843), (0, 0), im.Sepia("character/youth/pavlov_base1.png"), (0, 0), im.Sepia("character/youth/pavlov_happy1.png")))
image side pavlov normal = LiveCrop((40, 70, 350, 210), LiveComposite((440, 843), (0, 0), im.Sepia("character/youth/pavlov_base1.png"), (0, 0), im.Sepia("character/youth/pavlov_normal1.png")))
image side pavlov shock = LiveCrop((40, 70, 350, 210), LiveComposite((440, 843), (0, 0), im.Sepia("character/youth/pavlov_base1.png"), (0, 0), im.Sepia("character/youth/pavlov_shock1.png")))

image side vasey determined = LiveCrop((40, 70, 350, 210), LiveComposite((440, 843), (0, 0), im.Sepia("character/youth/vasey_base1.png"), (0, 0), im.Sepia("character/youth/vasey_determined1.png")))
image side vasey happy = LiveCrop((40, 70, 350, 210), LiveComposite((440, 843), (0, 0), im.Sepia("character/youth/vasey_base1.png"), (0, 0), im.Sepia("character/youth/vasey_happy1.png")))
image side vasey normal = LiveCrop((40, 70, 350, 210), LiveComposite((440, 843), (0, 0), im.Sepia("character/youth/vasey_base1.png"), (0, 0), im.Sepia("character/youth/vasey_normal1.png")))
image side vasey shock = LiveCrop((40, 70, 350, 210), LiveComposite((440, 843), (0, 0), im.Sepia("character/youth/vasey_base1.png"), (0, 0), im.Sepia("character/youth/vasey_shock1.png")))

image side dietling determined = LiveCrop((40, 70, 350, 210), LiveComposite((440, 843), (0, 0), im.Sepia("character/youth/dietling_base1.png"), (0, 0), im.Sepia("character/youth/dietling_determined1.png")))
image side dietling happy = LiveCrop((40, 70, 350, 210), LiveComposite((440, 843), (0, 0), im.Sepia("character/youth/dietling_base1.png"), (0, 0), im.Sepia("character/youth/dietling_happy1.png")))
image side dietling normal = LiveCrop((40, 70, 350, 210), LiveComposite((440, 843), (0, 0), im.Sepia("character/youth/dietling_base1.png"), (0, 0), im.Sepia("character/youth/dietling_normal1.png")))
image side dietling shock = LiveCrop((40, 70, 350, 210), LiveComposite((440, 843), (0, 0), im.Sepia("character/youth/dietling_base1.png"), (0, 0), im.Sepia("character/youth/dietling_shock1.png")))

image side zchaal determined = LiveCrop((40, 70, 350, 210), LiveComposite((440, 843), (0, 0), im.Sepia("character/youth/zchaal_base1.png"), (0, 0), im.Sepia("character/youth/zchaal_determined1.png")))
image side zchaal happy = LiveCrop((40, 70, 350, 210), LiveComposite((440, 843), (0, 0), im.Sepia("character/youth/zchaal_base1.png"), (0, 0), im.Sepia("character/youth/zchaal_happy1.png")))
image side zchaal normal = LiveCrop((40, 70, 350, 210), LiveComposite((440, 843), (0, 0), im.Sepia("character/youth/zchaal_base1.png"), (0, 0), im.Sepia("character/youth/zchaal_normal1.png")))
image side zchaal shock = LiveCrop((40, 70, 350, 210), LiveComposite((440, 843), (0, 0), im.Sepia("character/youth/zchaal_base1.png"), (0, 0), im.Sepia("character/youth/zchaal_shock1.png")))

########################################################
# Man ###############################################
########################################################
image man normal = LiveComposite(
    (670, 1020),
    (0, 0), "character/man/man_base1.png",
    (0, 0), "character/man/man_normal1.png")

image man happy = LiveComposite(
    (670, 1020),
    (0, 0), "character/man/man_base1.png",
    (0, 0), "character/man/man_happy1.png")

image man determined = LiveComposite(
    (670, 1020),
    (0, 0), "character/man/man_base1.png",
    (0, 0), "character/man/man_determined1.png")

image man shock = LiveComposite(
    (670, 1020),
    (0, 0), "character/man/man_base1.png",
    (0, 0), "character/man/man_shock1.png")

image desertman normal = LiveComposite(
    (670, 1020),
    (0, 0), "character/man/man_base2.png",
    (0, 0), "character/man/man_normal2.png")

image desertman happy = LiveComposite(
    (670, 1020),
    (0, 0), "character/man/man_base2.png",
    (0, 0), "character/man/man_happy2.png")

image desertman determined = LiveComposite(
    (670, 1020),
    (0, 0), "character/man/man_base2.png",
    (0, 0), "character/man/man_determined2.png")

image desertman shock = LiveComposite(
    (670, 1020),
    (0, 0), "character/man/man_base2.png",
    (0, 0), "character/man/man_shock2.png")

image evanbraun normal = LiveComposite(
    (670, 1020),
    (0, 0), "character/man/man_base3.png",
    (0, 0), "character/man/man_normal3.png")

image evanbraun happy = LiveComposite(
    (670, 1020),
    (0, 0), "character/man/man_base3.png",
    (0, 0), "character/man/man_happy3.png")

image evanbraun determined = LiveComposite(
    (670, 1020),
    (0, 0), "character/man/man_base3.png",
    (0, 0), "character/man/man_determined3.png")

image evanbraun shock = LiveComposite(
    (670, 1020),
    (0, 0), "character/man/man_base3.png",
    (0, 0), "character/man/man_shock3.png")

image evanbraun evil = LiveComposite(
    (670, 1020),
    (0, 0), "character/man/man_base3.png",
    (0, 0), "character/man/man_evil3.png")

image aussieman normal = LiveComposite(
    (670, 1020),
    (0, 0), "character/man/man_base4.png",
    (0, 0), "character/man/man_normal4.png")

image aussieman happy = LiveComposite(
    (670, 1020),
    (0, 0), "character/man/man_base4.png",
    (0, 0), "character/man/man_happy4.png")

image aussieman determined = LiveComposite(
    (670, 1020),
    (0, 0), "character/man/man_base4.png",
    (0, 0), "character/man/man_determined4.png")

image aussieman shock = LiveComposite(
    (670, 1020),
    (0, 0), "character/man/man_base4.png",
    (0, 0), "character/man/man_shock4.png")

image haakon normal = LiveComposite(
    (706, 1070),
    (0, 0), "character/man/man_base5.png",
    (0, 0), "character/man/man_normal5.png")

image haakon happy = LiveComposite(
    (706, 1070),
    (0, 0), "character/man/man_base5.png",
    (0, 0), "character/man/man_normal5.png")

image haakon determined = LiveComposite(
    (706, 1070),
    (0, 0), "character/man/man_base5.png",
    (0, 0), "character/man/man_determined5.png")

image haakon shock = LiveComposite(
    (706, 1070),
    (0, 0), "character/man/man_base5.png",
    (0, 0), "character/man/man_shock5.png")

image metaxas normal = LiveComposite(
    (670, 1035),
    (0, 0), "character/man/man_base6.png",
    (0, 0), "character/man/man_normal6.png")

image metaxas happy = LiveComposite(
    (670, 1035),
    (0, 0), "character/man/man_base6.png",
    (0, 0), "character/man/man_happy6.png")

image metaxas determined = LiveComposite(
    (670, 1035),
    (0, 0), "character/man/man_base6.png",
    (0, 0), "character/man/man_determined6.png")

image metaxas shock = LiveComposite(
    (670, 1035),
    (0, 0), "character/man/man_base6.png",
    (0, 0), "character/man/man_shock6.png")

image side man determined = LiveCrop((160, 75, 350, 210), LiveComposite((670, 1020), (0, 0), im.Sepia("character/man/man_base1.png"), (0, 0), im.Sepia("character/man/man_determined1.png")))
image side man happy = LiveCrop((160, 75, 350, 210), LiveComposite((670, 1020), (0, 0), im.Sepia("character/man/man_base1.png"), (0, 0), im.Sepia("character/man/man_happy1.png")))
image side man normal = LiveCrop((160, 75, 350, 210), LiveComposite((670, 1020), (0, 0), im.Sepia("character/man/man_base1.png"), (0, 0), im.Sepia("character/man/man_normal1.png")))
image side man shock = LiveCrop((160, 75, 350, 210), LiveComposite((670, 1020), (0, 0), im.Sepia("character/man/man_base1.png"), (0, 0), im.Sepia("character/man/man_shock1.png")))

image side desertman determined = LiveCrop((160, 75, 350, 210), LiveComposite((670, 1020), (0, 0), im.Sepia("character/man/man_base2.png"), (0, 0), im.Sepia("character/man/man_determined2.png")))
image side desertman happy = LiveCrop((160, 75, 350, 210), LiveComposite((670, 1020), (0, 0), im.Sepia("character/man/man_base2.png"), (0, 0), im.Sepia("character/man/man_happy2.png")))
image side desertman normal = LiveCrop((160, 75, 350, 210), LiveComposite((670, 1020), (0, 0), im.Sepia("character/man/man_base2.png"), (0, 0), im.Sepia("character/man/man_normal2.png")))
image side desertman shock = LiveCrop((160, 75, 350, 210), LiveComposite((670, 1020), (0, 0), im.Sepia("character/man/man_base2.png"), (0, 0), im.Sepia("character/man/man_shock2.png")))

image side evanbraun determined = LiveCrop((160, 75, 350, 210), LiveComposite((670, 1020), (0, 0), im.Sepia("character/man/man_base3.png"), (0, 0), im.Sepia("character/man/man_determined3.png")))
image side evanbraun happy = LiveCrop((160, 75, 350, 210), LiveComposite((670, 1020), (0, 0), im.Sepia("character/man/man_base3.png"), (0, 0), im.Sepia("character/man/man_happy3.png")))
image side evanbraun normal = LiveCrop((160, 75, 350, 210), LiveComposite((670, 1020), (0, 0), im.Sepia("character/man/man_base3.png"), (0, 0), im.Sepia("character/man/man_normal3.png")))
image side evanbraun shock = LiveCrop((160, 75, 350, 210), LiveComposite((670, 1020), (0, 0), im.Sepia("character/man/man_base3.png"), (0, 0), im.Sepia("character/man/man_shock3.png")))
image side evanbraun evil = LiveCrop((160, 75, 350, 210), LiveComposite((670, 1020), (0, 0), im.Sepia("character/man/man_base3.png"), (0, 0), im.Sepia("character/man/man_evil3.png")))

image side aussieman determined = LiveCrop((160, 75, 350, 210), LiveComposite((670, 1020), (0, 0), im.Sepia("character/man/man_base4.png"), (0, 0), im.Sepia("character/man/man_determined4.png")))
image side aussieman happy = LiveCrop((160, 75, 350, 210), LiveComposite((670, 1020), (0, 0), im.Sepia("character/man/man_base4.png"), (0, 0), im.Sepia("character/man/man_happy4.png")))
image side aussieman normal = LiveCrop((160, 75, 350, 210), LiveComposite((670, 1020), (0, 0), im.Sepia("character/man/man_base4.png"), (0, 0), im.Sepia("character/man/man_normal4.png")))
image side aussieman shock = LiveCrop((160, 75, 350, 210), LiveComposite((670, 1020), (0, 0), im.Sepia("character/man/man_base4.png"), (0, 0), im.Sepia("character/man/man_shock4.png")))

image side haakon determined = LiveCrop((190, 125, 350, 210), LiveComposite((706, 1070), (0, 0), im.Sepia("character/man/man_base5.png"), (0, 0), im.Sepia("character/man/man_determined5.png")))
image side haakon happy = LiveCrop((190, 125, 350, 210), LiveComposite((706, 1070), (0, 0), im.Sepia("character/man/man_base5.png"), (0, 0), im.Sepia("character/man/man_normal5.png")))
image side haakon normal = LiveCrop((190, 125, 350, 210), LiveComposite((706, 1070), (0, 0), im.Sepia("character/man/man_base5.png"), (0, 0), im.Sepia("character/man/man_normal5.png")))
image side haakon shock = LiveCrop((190, 125, 350, 210), LiveComposite((706, 1070), (0, 0), im.Sepia("character/man/man_base5.png"), (0, 0), im.Sepia("character/man/man_shock5.png")))

image side metaxas determined = LiveCrop((155, 90, 350, 210), LiveComposite((670, 1020), (0, 0), im.Sepia("character/man/man_base6.png"), (0, 0), im.Sepia("character/man/man_determined6.png")))
image side metaxas happy = LiveCrop((155, 90, 350, 210), LiveComposite((670, 1020), (0, 0), im.Sepia("character/man/man_base6.png"), (0, 0), im.Sepia("character/man/man_happy6.png")))
image side metaxas normal = LiveCrop((155, 90, 350, 210), LiveComposite((670, 1020), (0, 0), im.Sepia("character/man/man_base6.png"), (0, 0), im.Sepia("character/man/man_normal6.png")))
image side metaxas shock = LiveCrop((155, 90, 350, 210), LiveComposite((670, 1020), (0, 0), im.Sepia("character/man/man_base6.png"), (0, 0), im.Sepia("character/man/man_shock6.png")))


########################################################
# Old Man ###############################################
########################################################
image oldman determined = LiveComposite(
    (560, 900),
    (40, 0), "character/oldman/oldman_base1.png",
    (40, 0), "character/oldman/oldman_determined1.png")

image oldman normal = LiveComposite(
    (560, 900),
    (40, 0), "character/oldman/oldman_base1.png",
    (40, 0), "character/oldman/oldman_normal1.png")

image oldman happy = LiveComposite(
    (560, 900),
    (40, 0), "character/oldman/oldman_base1.png",
    (40, 0), "character/oldman/oldman_happy1.png")

image oldman shock = LiveComposite(
    (560, 900),
    (40, 0), "character/oldman/oldman_base1.png",
    (40, 0), "character/oldman/oldman_shock1.png")

image desertoldman determined = LiveComposite(
    (560, 900),
    (40, 0), "character/oldman/oldman_base2.png",
    (40, 0), "character/oldman/oldman_determined2.png")

image desertoldman normal = LiveComposite(
    (560, 900),
    (40, 0), "character/oldman/oldman_base2.png",
    (40, 0), "character/oldman/oldman_normal2.png")

image desertoldman happy = LiveComposite(
    (560, 900),
    (40, 0), "character/oldman/oldman_base2.png",
    (40, 0), "character/oldman/oldman_happy2.png")

image desertoldman shock = LiveComposite(
    (560, 900),
    (40, 0), "character/oldman/oldman_base2.png",
    (40, 0), "character/oldman/oldman_shock2.png")

image chambers determined = LiveComposite(
    (480, 950),
    (0, 0), "character/oldman/chambers_base1.png",
    (0, 0), "character/oldman/chambers_determined1.png")

image chambers normal = LiveComposite(
    (480, 950),
    (0, 0), "character/oldman/chambers_base1.png",
    (0, 0), "character/oldman/chambers_normal1.png")

image chambers happy = LiveComposite(
    (480, 950),
    (0, 0), "character/oldman/chambers_base1.png",
    (0, 0), "character/oldman/chambers_happy1.png")

image chambers shock = LiveComposite(
    (480, 950),
    (0, 0), "character/oldman/chambers_base1.png",
    (0, 0), "character/oldman/chambers_shock1.png")

image yamamoto determined = LiveComposite(
    (800, 950),
    (137, 0), "character/oldman/yamamoto_base1.png",
    (137, 0), "character/oldman/yamamoto_determined1.png")

image yamamoto normal = LiveComposite(
    (800, 950),
    (137, 0), "character/oldman/yamamoto_base1.png",
    (137, 0), "character/oldman/yamamoto_normal1.png")

image yamamoto happy = LiveComposite(
    (800, 950),
    (137, 0), "character/oldman/yamamoto_base1.png",
    (137, 0), "character/oldman/yamamoto_happy1.png")

image yamamoto shock = LiveComposite(
    (800, 950),
    (137, 0), "character/oldman/yamamoto_base1.png",
    (137, 0), "character/oldman/yamamoto_shock1.png")

image yamamoto car determined:
    "yamamoto determined"
    ypos 1.0
    linear 0.1 ypos 1.01
    linear 0.1 ypos 1.0
    repeat

image yamamoto car normal:
    "yamamoto normal"
    ypos 1.0
    linear 0.1 ypos 1.01
    linear 0.1 ypos 1.0
    repeat

image yamamoto car happy:
    "yamamoto happy"
    ypos 1.0
    linear 0.1 ypos 1.01
    linear 0.1 ypos 1.0
    repeat
    
image yamamoto car shock:
    "yamamoto shock"
    ypos 1.0
    linear 0.1 ypos 1.01
    linear 0.1 ypos 1.0
    repeat
    
image gariboldi determined = LiveComposite(
    (560, 921),
    (40, 0), "character/oldman/gariboldi_base1.png",
    (40, 0), "character/oldman/gariboldi_determined1.png")

image gariboldi normal = LiveComposite(
    (560, 921),
    (40, 0), "character/oldman/gariboldi_base1.png",
    (40, 0), "character/oldman/gariboldi_normal1.png")

image gariboldi happy = LiveComposite(
    (560, 921),
    (40, 0), "character/oldman/gariboldi_base1.png",
    (40, 0), "character/oldman/gariboldi_happy1.png")

image gariboldi shock = LiveComposite(
    (560, 921),
    (40, 0), "character/oldman/gariboldi_base1.png",
    (40, 0), "character/oldman/gariboldi_shock1.png")

image billotte determined = LiveComposite(
    (560, 892),
    (40, 0), "character/oldman/billotte_base1.png",
    (40, 0), "character/oldman/billotte_determined1.png")

image billotte normal = LiveComposite(
    (560, 892),
    (40, 0), "character/oldman/billotte_base1.png",
    (40, 0), "character/oldman/billotte_normal1.png")

image billotte happy = LiveComposite(
    (560, 892),
    (40, 0), "character/oldman/billotte_base1.png",
    (40, 0), "character/oldman/billotte_happy1.png")

image billotte shock = LiveComposite(
    (560, 892),
    (40, 0), "character/oldman/billotte_base1.png",
    (40, 0), "character/oldman/billotte_shock1.png")

image billotte car determined:
    "billotte determined"
    ypos 1.0
    linear 0.1 ypos 1.01
    linear 0.1 ypos 1.0
    repeat
    
image billotte car normal:
    "billotte normal"
    ypos 1.0
    linear 0.1 ypos 1.01
    linear 0.1 ypos 1.0
    repeat
    
image billotte car happy:
    "billotte happy"
    ypos 1.0
    linear 0.1 ypos 1.01
    linear 0.1 ypos 1.0
    repeat
    
image billotte car shock:
    "billotte shock"
    ypos 1.0
    linear 0.1 ypos 1.01
    linear 0.1 ypos 1.0
    repeat
    
image mihaila determined = LiveComposite(
    (560, 875),
    (40, 0), "character/oldman/mihaila_base1.png",
    (40, 0), "character/oldman/mihaila_determined1.png")

image mihaila normal = LiveComposite(
    (560, 875),
    (40, 0), "character/oldman/mihaila_base1.png",
    (40, 0), "character/oldman/mihaila_normal1.png")

image mihaila happy = LiveComposite(
    (560, 875),
    (40, 0), "character/oldman/mihaila_base1.png",
    (40, 0), "character/oldman/mihaila_happy1.png")

image mihaila shock = LiveComposite(
    (560, 875),
    (40, 0), "character/oldman/mihaila_base1.png",
    (40, 0), "character/oldman/mihaila_shock1.png")

image side chambers determined = LiveCrop((70, 70, 350, 210), LiveComposite((480, 700), (0, 0), im.Sepia("character/oldman/chambers_base1.png"), (0, 0), im.Sepia("character/oldman/chambers_determined1.png")))
image side chambers happy = LiveCrop((70, 70, 350, 210), LiveComposite((480, 700), (0, 0), im.Sepia("character/oldman/chambers_base1.png"), (0, 0), im.Sepia("character/oldman/chambers_happy1.png")))
image side chambers normal = LiveCrop((70, 70, 350, 210), LiveComposite((480, 700), (0, 0), im.Sepia("character/oldman/chambers_base1.png"), (0, 0), im.Sepia("character/oldman/chambers_normal1.png")))
image side chambers shock = LiveCrop((70, 70, 350, 210), LiveComposite((480, 700), (0, 0), im.Sepia("character/oldman/chambers_base1.png"), (0, 0), im.Sepia("character/oldman/chambers_shock1.png")))

image side oldman determined = LiveCrop((60, 70, 350, 210), LiveComposite((580, 700), (0, 0), im.Sepia("character/oldman/oldman_base1.png"), (0, 0), im.Sepia("character/oldman/oldman_determined1.png")))
image side oldman happy = LiveCrop((60, 70, 350, 210), LiveComposite((580, 700), (0, 0), im.Sepia("character/oldman/oldman_base1.png"), (0, 0), im.Sepia("character/oldman/oldman_happy1.png")))
image side oldman normal = LiveCrop((60, 70, 350, 210), LiveComposite((580, 700), (0, 0), im.Sepia("character/oldman/oldman_base1.png"), (0, 0), im.Sepia("character/oldman/oldman_normal1.png")))
image side oldman shock = LiveCrop((60, 70, 350, 210), LiveComposite((580, 700), (0, 0), im.Sepia("character/oldman/oldman_base1.png"), (0, 0), im.Sepia("character/oldman/oldman_shock1.png")))

image side desertoldman determined = LiveCrop((60, 70, 350, 210), LiveComposite((580, 700), (0, 0), im.Sepia("character/oldman/oldman_base2.png"), (0, 0), im.Sepia("character/oldman/oldman_determined2.png")))
image side desertoldman happy = LiveCrop((60, 70, 350, 210), LiveComposite((580, 700), (0, 0), im.Sepia("character/oldman/oldman_base2.png"), (0, 0), im.Sepia("character/oldman/oldman_happy2.png")))
image side desertoldman normal = LiveCrop((60, 70, 350, 210), LiveComposite((580, 700), (0, 0), im.Sepia("character/oldman/oldman_base2.png"), (0, 0), im.Sepia("character/oldman/oldman_normal2.png")))
image side desertoldman shock = LiveCrop((60, 70, 350, 210), LiveComposite((580, 700), (0, 0), im.Sepia("character/oldman/oldman_base2.png"), (0, 0), im.Sepia("character/oldman/oldman_shock2.png")))

image side yamamoto determined = LiveCrop((65, 50, 350, 210), LiveComposite((510, 700), (0, 0), im.Sepia("character/oldman/yamamoto_base1.png"), (0, 0), im.Sepia("character/oldman/yamamoto_determined1.png")))
image side yamamoto normal = LiveCrop((65, 50, 350, 210), LiveComposite((510, 700), (0, 0), im.Sepia("character/oldman/yamamoto_base1.png"), (0, 0), im.Sepia("character/oldman/yamamoto_normal1.png")))
image side yamamoto happy = LiveCrop((65, 50, 350, 210), LiveComposite((510, 700), (0, 0), im.Sepia("character/oldman/yamamoto_base1.png"), (0, 0), im.Sepia("character/oldman/yamamoto_happy1.png")))
image side yamamoto shock = LiveCrop((65, 50, 350, 210), LiveComposite((510, 700), (0, 0), im.Sepia("character/oldman/yamamoto_base1.png"), (0, 0), im.Sepia("character/oldman/yamamoto_shock1.png")))
image side yamamoto car determined = LiveCrop((65, 50, 350, 210), LiveComposite((510, 700), (0, 0), im.Sepia("character/oldman/yamamoto_base1.png"), (0, 0), im.Sepia("character/oldman/yamamoto_determined1.png")))
image side yamamoto car normal = LiveCrop((65, 50, 350, 210), LiveComposite((510, 700), (0, 0), im.Sepia("character/oldman/yamamoto_base1.png"), (0, 0), im.Sepia("character/oldman/yamamoto_normal1.png")))
image side yamamoto car happy = LiveCrop((65, 50, 350, 210), LiveComposite((510, 700), (0, 0), im.Sepia("character/oldman/yamamoto_base1.png"), (0, 0), im.Sepia("character/oldman/yamamoto_happy1.png")))
image side yamamoto car shock = LiveCrop((65, 50, 350, 210), LiveComposite((510, 700), (0, 0), im.Sepia("character/oldman/yamamoto_base1.png"), (0, 0), im.Sepia("character/oldman/yamamoto_shock1.png")))

image side gariboldi determined = LiveCrop((60, 90, 350, 210), LiveComposite((580, 700), (0, 0), im.Sepia("character/oldman/gariboldi_base1.png"), (0, 0), im.Sepia("character/oldman/gariboldi_determined1.png")))
image side gariboldi happy = LiveCrop((60, 90, 350, 210), LiveComposite((580, 700), (0, 0), im.Sepia("character/oldman/gariboldi_base1.png"), (0, 0), im.Sepia("character/oldman/gariboldi_happy1.png")))
image side gariboldi normal = LiveCrop((60, 90, 350, 210), LiveComposite((580, 700), (0, 0), im.Sepia("character/oldman/gariboldi_base1.png"), (0, 0), im.Sepia("character/oldman/gariboldi_normal1.png")))
image side gariboldi shock = LiveCrop((60, 90, 350, 210), LiveComposite((580, 700), (0, 0), im.Sepia("character/oldman/gariboldi_base1.png"), (0, 0), im.Sepia("character/oldman/gariboldi_shock1.png")))

image side billotte determined = LiveCrop((60, 61, 350, 210), LiveComposite((580, 700), (0, 0), im.Sepia("character/oldman/billotte_base1.png"), (0, 0), im.Sepia("character/oldman/billotte_determined1.png")))
image side billotte happy = LiveCrop((60, 61, 350, 210), LiveComposite((580, 700), (0, 0), im.Sepia("character/oldman/billotte_base1.png"), (0, 0), im.Sepia("character/oldman/billotte_happy1.png")))
image side billotte normal = LiveCrop((60, 61, 350, 210), LiveComposite((580, 700), (0, 0), im.Sepia("character/oldman/billotte_base1.png"), (0, 0), im.Sepia("character/oldman/billotte_normal1.png")))
image side billotte shock = LiveCrop((60, 61, 350, 210), LiveComposite((580, 700), (0, 0), im.Sepia("character/oldman/billotte_base1.png"), (0, 0), im.Sepia("character/oldman/billotte_shock1.png")))
image side billotte car determined = LiveCrop((60, 61, 350, 210), LiveComposite((580, 700), (0, 0), im.Sepia("character/oldman/billotte_base1.png"), (0, 0), im.Sepia("character/oldman/billotte_determined1.png")))
image side billotte car happy = LiveCrop((60, 61, 350, 210), LiveComposite((580, 700), (0, 0), im.Sepia("character/oldman/billotte_base1.png"), (0, 0), im.Sepia("character/oldman/billotte_happy1.png")))
image side billotte car normal = LiveCrop((60, 61, 350, 210), LiveComposite((580, 700), (0, 0), im.Sepia("character/oldman/billotte_base1.png"), (0, 0), im.Sepia("character/oldman/billotte_normal1.png")))
image side billotte car shock = LiveCrop((60, 61, 350, 210), LiveComposite((580, 700), (0, 0), im.Sepia("character/oldman/billotte_base1.png"), (0, 0), im.Sepia("character/oldman/billotte_shock1.png")))

image side mihaila determined = LiveCrop((60, 44, 350, 210), LiveComposite((580, 700), (0, 0), im.Sepia("character/oldman/mihaila_base1.png"), (0, 0), im.Sepia("character/oldman/mihaila_determined1.png")))
image side mihaila happy = LiveCrop((60, 44, 350, 210), LiveComposite((580, 700), (0, 0), im.Sepia("character/oldman/mihaila_base1.png"), (0, 0), im.Sepia("character/oldman/mihaila_happy1.png")))
image side mihaila normal = LiveCrop((60, 44, 350, 210), LiveComposite((580, 700), (0, 0), im.Sepia("character/oldman/mihaila_base1.png"), (0, 0), im.Sepia("character/oldman/mihaila_normal1.png")))
image side mihaila shock = LiveCrop((60, 44, 350, 210), LiveComposite((580, 700), (0, 0), im.Sepia("character/oldman/mihaila_base1.png"), (0, 0), im.Sepia("character/oldman/mihaila_shock1.png")))

########################################################
# Soldier ###############################################
########################################################
image soldier normal = LiveComposite(
    (740, 1000),
    (0, 0), "character/soldier/soldier_base1.png",
    (0, 0), "character/soldier/soldier_normal1.png")

image soldier happy = LiveComposite(
    (740, 1000),
    (0, 0), "character/soldier/soldier_base1.png",
    (0, 0), "character/soldier/soldier_happy1.png")

image soldier determined = LiveComposite(
    (740, 1000),
    (0, 0), "character/soldier/soldier_base1.png",
    (0, 0), "character/soldier/soldier_determined1.png")

image soldier shock = LiveComposite(
    (740, 1000),
    (0, 0), "character/soldier/soldier_base1.png",
    (0, 0), "character/soldier/soldier_shock1.png")

image vitalia normal = LiveComposite(
    (740, 1032),
    (0, 0), "character/soldier/vitalia_base1.png",
    (0, 0), "character/soldier/vitalia_normal1.png")

image vitalia happy = LiveComposite(
    (740, 1032),
    (0, 0), "character/soldier/vitalia_base1.png",
    (0, 0), "character/soldier/vitalia_happy1.png")

image vitalia determined = LiveComposite(
    (740, 1032),
    (0, 0), "character/soldier/vitalia_base1.png",
    (0, 0), "character/soldier/vitalia_determined1.png")

image vitalia shock = LiveComposite(
    (740, 1032),
    (0, 0), "character/soldier/vitalia_base1.png",
    (0, 0), "character/soldier/vitalia_shock1.png")

image vitalia tank happy:
    "vitalia happy"
    xalign 0.5  yalign 1.0
    linear 0.1 yalign 1.1
    linear 0.1 yalign 1.0
    repeat
    
image vitalia tank normal:
    "vitalia normal"
    xalign 0.5  yalign 1.0
    linear 0.1 yalign 1.1
    linear 0.1 yalign 1.0
    repeat
    
image vitalia tank determined:
    "vitalia determined"
    xalign 0.5  yalign 1.0
    linear 0.1 yalign 1.1
    linear 0.1 yalign 1.0
    repeat

image vitalia tank shock:
    "vitalia shock"
    xalign 0.5  yalign 1.0
    linear 0.1 yalign 1.1
    linear 0.1 yalign 1.0
    repeat

image polix normal = LiveComposite(
    (740, 1032),
    (0, 0), "character/soldier/polix_base1.png",
    (0, 0), "character/soldier/polix_normal1.png")

image polix happy = LiveComposite(
    (740, 1032),
    (0, 0), "character/soldier/polix_base1.png",
    (0, 0), "character/soldier/polix_happy1.png")

image polix determined = LiveComposite(
    (740, 1032),
    (0, 0), "character/soldier/polix_base1.png",
    (0, 0), "character/soldier/polix_determined1.png")

image polix shock = LiveComposite(
    (740, 1032),
    (0, 0), "character/soldier/polix_base1.png",
    (0, 0), "character/soldier/polix_shock1.png")

image polixfake determined = LiveComposite(
    (740, 1032),
    (0, 0), "character/soldier/polixfake_base1.png")

image zipangu normal = LiveComposite(
    (740, 1032),
    (0, 0), "character/soldier/zipangu_base1.png",
    (0, 0), "character/soldier/zipangu_normal1.png")

image zipangu happy = LiveComposite(
    (740, 1032),
    (0, 0), "character/soldier/zipangu_base1.png",
    (0, 0), "character/soldier/zipangu_happy1.png")

image zipangu determined = LiveComposite(
    (740, 1032),
    (0, 0), "character/soldier/zipangu_base1.png",
    (0, 0), "character/soldier/zipangu_determined1.png")

image zipangu shock = LiveComposite(
    (740, 1032),
    (0, 0), "character/soldier/zipangu_base1.png",
    (0, 0), "character/soldier/zipangu_shock1.png")

image amerika normal = LiveComposite(
    (740, 1032),
    (0, 0), "character/soldier/amerika_base1.png",
    (0, 0), "character/soldier/amerika_normal1.png")

image franzo normal = LiveComposite(
    (740, 1054),
    (0, 0), "character/soldier/franzo_base1.png",
    (0, 0), "character/soldier/franzo_normal1.png")

image franzo happy = LiveComposite(
    (740, 1054),
    (0, 0), "character/soldier/franzo_base1.png",
    (0, 0), "character/soldier/franzo_happy1.png")

image franzo determined = LiveComposite(
    (740, 1054),
    (0, 0), "character/soldier/franzo_base1.png",
    (0, 0), "character/soldier/franzo_determined1.png")

image franzo shock = LiveComposite(
    (740, 1054),
    (0, 0), "character/soldier/franzo_base1.png",
    (0, 0), "character/soldier/franzo_shock1.png")

image brookie normal = LiveComposite(
    (740, 1030),
    (0, 0), "character/soldier/brookie_base1.png",
    (0, 0), "character/soldier/brookie_normal1.png")

image brookie happy = LiveComposite(
    (740, 1030),
    (0, 0), "character/soldier/brookie_base1.png",
    (0, 0), "character/soldier/brookie_happy1.png")

image brookie determined = LiveComposite(
    (740, 1030),
    (0, 0), "character/soldier/brookie_base1.png",
    (0, 0), "character/soldier/brookie_determined1.png")

image brookie shock = LiveComposite(
    (740, 1030),
    (0, 0), "character/soldier/brookie_base1.png",
    (0, 0), "character/soldier/brookie_shock1.png")

image luge normal = LiveComposite(
    (740, 1005),
    (0, 0), "character/soldier/luge_base1.png",
    (0, 0), "character/soldier/luge_normal1.png")

image luge happy = LiveComposite(
    (740, 1005),
    (0, 0), "character/soldier/luge_base1.png",
    (0, 0), "character/soldier/luge_happy1.png")

image luge determined = LiveComposite(
    (740, 1005),
    (0, 0), "character/soldier/luge_base1.png",
    (0, 0), "character/soldier/luge_determined1.png")

image luge shock = LiveComposite(
    (740, 1005),
    (0, 0), "character/soldier/luge_base1.png",
    (0, 0), "character/soldier/luge_shock1.png")

image side soldier determined = LiveCrop((175, 70, 350, 210), LiveComposite((740, 1000), (0, 0), im.Sepia("character/soldier/soldier_base1.png"), (0, 0), im.Sepia("character/soldier/soldier_determined1.png")))
image side soldier happy = LiveCrop((175, 70, 350, 210), LiveComposite((740, 1000), (0, 0), im.Sepia("character/soldier/soldier_base1.png"), (0, 0), im.Sepia("character/soldier/soldier_happy1.png")))
image side soldier normal = LiveCrop((175, 70, 350, 210), LiveComposite((740, 1000), (0, 0), im.Sepia("character/soldier/soldier_base1.png"), (0, 0), im.Sepia("character/soldier/soldier_normal1.png")))
image side soldier shock = LiveCrop((175, 70, 350, 210), LiveComposite((740, 1000), (0, 0), im.Sepia("character/soldier/soldier_base1.png"), (0, 0), im.Sepia("character/soldier/soldier_shock1.png")))

image side vitalia determined = LiveCrop((175, 102, 350, 210), LiveComposite((740, 1032), (0, 0), im.Sepia("character/soldier/vitalia_base1.png"), (0, 0), im.Sepia("character/soldier/vitalia_determined1.png")))
image side vitalia happy = LiveCrop((175, 102, 350, 210), LiveComposite((740, 1032), (0, 0), im.Sepia("character/soldier/vitalia_base1.png"), (0, 0), im.Sepia("character/soldier/vitalia_happy1.png")))
image side vitalia normal = LiveCrop((175, 102, 350, 210), LiveComposite((740, 1032), (0, 0), im.Sepia("character/soldier/vitalia_base1.png"), (0, 0), im.Sepia("character/soldier/vitalia_normal1.png")))
image side vitalia shock = LiveCrop((175, 102, 350, 210), LiveComposite((740, 1032), (0, 0), im.Sepia("character/soldier/vitalia_base1.png"), (0, 0), im.Sepia("character/soldier/vitalia_shock1.png")))

image side polix determined = LiveCrop((175, 102, 350, 210), LiveComposite((740, 1032), (0, 0), im.Sepia("character/soldier/polix_base1.png"), (0, 0), im.Sepia("character/soldier/polix_determined1.png")))
image side polix happy = LiveCrop((175, 102, 350, 210), LiveComposite((740, 1032), (0, 0), im.Sepia("character/soldier/polix_base1.png"), (0, 0), im.Sepia("character/soldier/polix_happy1.png")))
image side polix normal = LiveCrop((175, 102, 350, 210), LiveComposite((740, 1032), (0, 0), im.Sepia("character/soldier/polix_base1.png"), (0, 0), im.Sepia("character/soldier/polix_normal1.png")))
image side polix shock = LiveCrop((175, 102, 350, 210), LiveComposite((740, 1032), (0, 0), im.Sepia("character/soldier/polix_base1.png"), (0, 0), im.Sepia("character/soldier/polix_shock1.png")))

image side polixfake determined = LiveCrop((175, 102, 350, 210), LiveComposite((740, 1032), (0, 0), im.Sepia("character/soldier/polixfake_base1.png")))

image side zipangu determined = LiveCrop((175, 102, 350, 210), LiveComposite((740, 1032), (0, 0), im.Sepia("character/soldier/zipangu_base1.png"), (0, 0), im.Sepia("character/soldier/zipangu_determined1.png")))
image side zipangu happy = LiveCrop((175, 102, 350, 210), LiveComposite((740, 1032), (0, 0), im.Sepia("character/soldier/zipangu_base1.png"), (0, 0), im.Sepia("character/soldier/zipangu_happy1.png")))
image side zipangu normal = LiveCrop((175, 102, 350, 210), LiveComposite((740, 1032), (0, 0), im.Sepia("character/soldier/zipangu_base1.png"), (0, 0), im.Sepia("character/soldier/zipangu_normal1.png")))
image side zipangu shock = LiveCrop((175, 102, 350, 210), LiveComposite((740, 1032), (0, 0), im.Sepia("character/soldier/zipangu_base1.png"), (0, 0), im.Sepia("character/soldier/zipangu_shock1.png")))

image side amerika normal = LiveCrop((175, 102, 350, 210), LiveComposite((740, 1032), (0, 0), im.Sepia("character/soldier/amerika_base1.png"), (0, 0), im.Sepia("character/soldier/amerika_normal1.png")))

image side franzo determined = LiveCrop((175, 102, 350, 210), LiveComposite((740, 1054), (0, 0), im.Sepia("character/soldier/franzo_base1.png"), (0, 0), im.Sepia("character/soldier/franzo_determined1.png")))
image side franzo happy = LiveCrop((175, 102, 350, 210), LiveComposite((740, 1054), (0, 0), im.Sepia("character/soldier/franzo_base1.png"), (0, 0), im.Sepia("character/soldier/franzo_happy1.png")))
image side franzo normal = LiveCrop((175, 102, 350, 210), LiveComposite((740, 1054), (0, 0), im.Sepia("character/soldier/franzo_base1.png"), (0, 0), im.Sepia("character/soldier/franzo_normal1.png")))
image side franzo shock = LiveCrop((175, 102, 350, 210), LiveComposite((740, 1054), (0, 0), im.Sepia("character/soldier/franzo_base1.png"), (0, 0), im.Sepia("character/soldier/franzo_shock1.png")))

image side brookie determined = LiveCrop((175, 100, 350, 210), LiveComposite((740, 1030), (0, 0), im.Sepia("character/soldier/brookie_base1.png"), (0, 0), im.Sepia("character/soldier/brookie_determined1.png")))
image side brookie happy = LiveCrop((175, 100, 350, 210), LiveComposite((740, 1030), (0, 0), im.Sepia("character/soldier/brookie_base1.png"), (0, 0), im.Sepia("character/soldier/brookie_happy1.png")))
image side brookie normal = LiveCrop((175, 100, 350, 210), LiveComposite((740, 1030), (0, 0), im.Sepia("character/soldier/brookie_base1.png"), (0, 0), im.Sepia("character/soldier/brookie_normal1.png")))
image side brookie shock = LiveCrop((175, 100, 350, 210), LiveComposite((740, 1030), (0, 0), im.Sepia("character/soldier/brookie_base1.png"), (0, 0), im.Sepia("character/soldier/brookie_shock1.png")))

image side luge determined = LiveCrop((175, 80, 350, 210), LiveComposite((740, 1005), (0, 0), im.Sepia("character/soldier/luge_base1.png"), (0, 0), im.Sepia("character/soldier/luge_determined1.png")))
image side luge happy = LiveCrop((175, 80, 350, 210), LiveComposite((740, 1005), (0, 0), im.Sepia("character/soldier/luge_base1.png"), (0, 0), im.Sepia("character/soldier/luge_happy1.png")))
image side luge normal = LiveCrop((175, 80, 350, 210), LiveComposite((740, 1005), (0, 0), im.Sepia("character/soldier/luge_base1.png"), (0, 0), im.Sepia("character/soldier/luge_normal1.png")))
image side luge shock = LiveCrop((175, 80, 350, 210), LiveComposite((740, 1005), (0, 0), im.Sepia("character/soldier/luge_base1.png"), (0, 0), im.Sepia("character/soldier/luge_shock1.png")))

########################################################
# Takeshi ###############################################
########################################################
image takeshi normal = LiveComposite(
    (740, 1000),
    (0, 0), "character/soldier/takeshi_base1.png",
    (0, 0), "character/soldier/takeshi_normal1.png")

image takeshi happy = LiveComposite(
    (740, 1000),
    (0, 0), "character/soldier/takeshi_base1.png",
    (0, 0), "character/soldier/takeshi_happy1.png")

image takeshi determined = LiveComposite(
    (740, 1000),
    (0, 0), "character/soldier/takeshi_base1.png",
    (0, 0), "character/soldier/takeshi_determined1.png")

image takeshi shock = LiveComposite(
    (740, 1000),
    (0, 0), "character/soldier/takeshi_base1.png",
    (0, 0), "character/soldier/takeshi_shock1.png")

image side takeshi determined = LiveCrop((175, 70, 350, 210), LiveComposite((740, 1000), (0, 0), im.Sepia("character/soldier/takeshi_base1.png"), (0, 0), im.Sepia("character/soldier/takeshi_determined1.png")))
image side takeshi happy = LiveCrop((175, 70, 350, 210), LiveComposite((740, 1000), (0, 0), im.Sepia("character/soldier/takeshi_base1.png"), (0, 0), im.Sepia("character/soldier/takeshi_happy1.png")))
image side takeshi normal = LiveCrop((175, 70, 350, 210), LiveComposite((740, 1000), (0, 0), im.Sepia("character/soldier/takeshi_base1.png"), (0, 0), im.Sepia("character/soldier/takeshi_normal1.png")))
image side takeshi shock = LiveCrop((175, 70, 350, 210), LiveComposite((740, 1000), (0, 0), im.Sepia("character/soldier/takeshi_base1.png"), (0, 0), im.Sepia("character/soldier/takeshi_shock1.png")))

########################################################
# King ###############################################
########################################################
image king normal = LiveComposite(
    (950, 1060),
    (-20, 0), "character/king/king_base1.png",
    (-20, 0), "character/king/king_normal1.png")

image king happy = LiveComposite(
    (950, 1060),
    (-20, 0), "character/king/king_base1.png",
    (-20, 0), "character/king/king_happy1.png")

image king determined = LiveComposite(
    (950, 1060),
    (-20, 0), "character/king/king_base1.png",
    (-20, 0), "character/king/king_determined1.png")

image king shock = LiveComposite(
    (950, 1060),
    (-20, 0), "character/king/king_base1.png",
    (-20, 0), "character/king/king_shock1.png")

image side king determined = LiveCrop((320, 120, 350, 210), LiveComposite((950, 1060), (0, 0), im.Sepia("character/king/king_base1.png"), (0, 0), im.Sepia("character/king/king_determined1.png")))
image side king happy = LiveCrop((320, 120, 350, 210), LiveComposite((950, 1060), (0, 0), im.Sepia("character/king/king_base1.png"), (0, 0), im.Sepia("character/king/king_happy1.png")))
image side king normal = LiveCrop((320, 120, 350, 210), LiveComposite((950, 1060), (0, 0), im.Sepia("character/king/king_base1.png"), (0, 0), im.Sepia("character/king/king_normal1.png")))
image side king shock = LiveCrop((320, 120, 350, 210), LiveComposite((950, 1060), (0, 0), im.Sepia("character/king/king_base1.png"), (0, 0), im.Sepia("character/king/king_shock1.png")))
    
########################################################
# Yamato ###############################################
########################################################
image side yamato = LiveCrop((450, 270, 350, 210), im.Sepia("character/yamato.png"))

#################################################
#CODEX#########################################
#################################################
image yamato codex = "side yamato"
image hitora codex = "side hitora hat normal"
image joebbels codex = "side joebbels normal"
image goring codex = "side goring determined"
image cyrano codex = "side cyrano hat normal"
image churchill codex = "side churchill hat normal"
image dunitz codex = "side dunitz bored"
image zhukky codex = "side zhukky hat normal"
image roijean codex = "side roijean hat normal"
image monty codex = "side monty normal"
image starin codex = "side starin hat normal"
image hirahita codex = "side hirahita normal"
image roosevelt codex = "side roosevelt normal"
image manstein codex = "side manstein normal"
image mannerheim codex = "side mannerheim normal"
image rinni codex = "side rinni hat normal"
image rommel codex = "side rommel normal"
image gamelin codex = "side gamelin normal"
image badoglio codex = "side badoglio hat normal"
image messe codex = "side messe normal"
image graziani codex = "side graziani normal"
image antoness codex = "side antoness normal"
image tito codex = "side tito normal"
image molotov codex = "side molotov normal"
image vasile codex = "side vasile normal"
image stuffy codex = "side stuffy normal"
image battenia codex = "side battenia normal"
image guderian codex = "side guderian normal"
image horthy codex = "side horthy normal"
image smigly codex = "side smigly normal"
image dresckow codex = "side dresckow normal"
image nyan codex = "side nyan normal"

image yamato codex flag = "gui/flag_zipangu.png"
image hitora codex flag = "gui/flag_germania.png"
image joebbels codex flag = "gui/flag_germania.png"
image goring codex flag = "gui/flag_germania.png"
image cyrano codex flag = "gui/flag_franzo.png"
image churchill codex flag = "gui/flag_britannia.png"
image dunitz codex flag = "gui/flag_germania.png"
image zhukky codex flag = "gui/flag_sovia.png"
image roijean codex flag = "gui/flag_franzo.png"
image monty codex flag = "gui/flag_britannia.png"
image starin codex flag = "gui/flag_sovia.png"
image hirahita codex flag = "gui/flag_zipangu.png"
image roosevelt codex flag = "gui/flag_amerika.png"
image manstein codex flag = "gui/flag_germania.png"
image mannerheim codex flag = "gui/flag_finbard.png"
image rinni codex flag = "gui/flag_vitalia.png"
image rommel codex flag = "gui/flag_germania.png"
image gamelin codex flag = "gui/flag_franzo.png"
image badoglio codex flag = "gui/flag_vitalia.png"
image messe codex flag = "gui/flag_vitalia.png"
image graziani codex flag = "gui/flag_vitalia.png"
image antoness codex flag = "gui/flag_rumanum.png"
image tito codex flag = "gui/flag_serpana.png"
image molotov codex flag = "gui/flag_sovia.png"
image vasile codex flag = "gui/flag_sovia.png"
image stuffy codex flag = "gui/flag_britannia.png"
image battenia codex flag = "gui/flag_britannia.png"
image guderian codex flag = "gui/flag_germania.png"
image horthy codex flag = "gui/flag_hang.png"
image smigly codex flag = "gui/flag_polix.png"
image dresckow codex flag = "gui/flag_germania.png"
image nyan codex flag = "gui/flag_zhina.png"

image franzolibre codex flag = "gui/flag_franzolibre.png"
