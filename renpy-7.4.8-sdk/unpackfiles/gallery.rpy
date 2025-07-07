
########################################################################################################################
#### CG GALLERY #######################################################################################################
########################################################################################################################
init python:
    gallery_cg_items = [
        "cg_yamato",
        "cg_hirahita",
        "cg_hitora1_1",
        "cg_hitora2",
        "cg_hitora3",
        "cg_hitora4",
        "cg_hitora5_1",
        "cg_birthday",
        "cg_hitora6_1",
        "cg_cyrano1",
        "cg_cyrano2_1",
        "cg_cyrano3",
        "cg_churchill2",
        "cg_churchill1",
        "cg_churchill3",
        "cg_starin1_1",
        "cg_starin2",
        "cg_starin3",
        "cg_starin4_1",
        "cg_scarletrevolution",
        "cg_rinni1",
        "cg_beach",
        "cg_onsen",
        "cg_rommel1",
        "cg_rommel2_1",
        "cg_joebbels",
        "cg_goring",
        "cg_dunitz",
        "cg_roijean",
        "cg_monty",
        "cg_battenia",
        "cg_stuffy",
        "cg_molotov",
        "cg_vasile",
        "cg_badoglio",
        "cg_messe",
        "cg_graziani",
        "cg_mannerheim",
        "cg_horthy",
        "cg_antoness",
        "cg_smigly",
        "cg_tito",
        "cg_manstein",
        "cg_guderian",
        "cg_yamamoto",
        "cg_nyan",
        "cg_redgeneralissima",
        "cg_negahitora",
        "cg_ending1",
        "cg_soldiers",
        "cg_polix",
        "cg_barbarossa1_1",
        "cg_worldwar",
        "cg_totalwar",
        "cg_zhukky",
        "cg_franzodefeated",
        "cg_panzer",
        "cg_uboat",
        "cg_bismarck",
        "cg_junker",
        "cg_spitfire",
        "cg_posters"
    ]
    gal_rows = int(len(gallery_cg_items) / 3) + (len(gallery_cg_items) % 3 > 0)
    gal_cols = 3
    thumbnail_x = 400
    thumbnail_y = 225
    gal_cells = gal_rows * gal_cols    
    g_cg = Gallery()
    for gal_item in gallery_cg_items:
        g_cg.button(gal_item + " butt")
        g_cg.unlock_image(gal_item)
        if gal_item == "cg_yamato":
            g_cg.unlock_image("cg_yamato2")
        if gal_item == "cg_hitora1_1":
            g_cg.unlock_image("cg_hitora1_2")
            g_cg.unlock_image("cg_hitora1_3")
        if gal_item == "cg_hitora5_1":
            g_cg.unlock_image("cg_hitora5_2")
        if gal_item == "cg_hitora6_1":
            g_cg.unlock_image("cg_hitora6_2")
        if gal_item == "cg_cyrano2_1":
            g_cg.unlock_image("cg_cyrano2_2")
            g_cg.unlock_image("cg_cyrano2_3")
        if gal_item == "cg_starin1_1":
            g_cg.unlock_image("cg_starin1_5")
            g_cg.unlock_image("cg_starin1_2")
            g_cg.unlock_image("cg_starin1_3")
            g_cg.unlock_image("cg_starin1_6")
        if gal_item == "cg_starin4_1":
            g_cg.unlock_image("cg_starin4_2")
        if gal_item == "cg_rinni1":
            g_cg.unlock_image("cg_rinni2")
        if gal_item == "cg_barbarossa1_1":
            g_cg.unlock_image("cg_barbarossa1_2")
            g_cg.unlock_image("cg_barbarossa1_3")
        if gal_item == "cg_franzodefeated":
            g_cg.unlock_image("cg_greciadefeated")
        if gal_item == "cg_panzer":
            g_cg.unlock_image("cg_panzer2")
        if gal_item == "cg_rommel2_1":
            g_cg.unlock_image("cg_rommel2_2")
        if gal_item == "cg_ending1":
            g_cg.unlock_image("cg_ending2")
            g_cg.unlock_image("cg_ending3")
            g_cg.unlock_image("cg_ending4")
    g_cg.transition = fade
    cg_page=0
    
init +1 python:
    for gal_item in gallery_cg_items:
        if "cg_" in gal_item:
            renpy.image (gal_item + " butt", "cg/gallery/" + gal_item + ".jpg")
            #renpy.image (gal_item + " butt", im.Scale(im.Crop("cg/" + gal_item + ".jpg", (0, 0, 1920, 1080)), thumbnail_x, thumbnail_y))
        
screen cg_gallery():
    tag menu
    use navigation id "navi_navigation"
    frame:
        background "gui/load_back.png"
        yalign 0.5
        xalign 0.1
        ysize 1016
        xsize 1369
        viewport:
            scrollbars "vertical"
            xmaximum 1330
            xminimum 1330
            ymaximum 795
            yminimum 795
            yalign 0.55
            xalign 0.15
            side_yalign .58
            side_ymaximum 712
            side_spacing -30
            draggable False
            mousewheel True
            vbox:
                xalign 0.5
                grid gal_cols gal_rows:
                    xpos 30
                    for gal_item in gallery_cg_items:
                        add g_cg.make_button(gal_item + " butt", gal_item + " butt", im.Scale("gui/gallocked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=Image("gui/gallery_border.png", xalign=0.5, yalign=0.5), background=Frame("gui/frame.png",24,24), xmargin=3, ymargin=3, xpadding=8, ypadding=8, hover_sound="se/hover.ogg", activate_sound="se/click.ogg") 
                    for j in range(0, gal_cells - len(gallery_cg_items)):   
                        null
    vbox:
        xalign 0.37
        yalign 0.065
        add "gui/overlay_title_gallery.png"
    frame:
        background Frame(im.Sepia("gui/outer_frame.png"), 200, 200)
        
                    
########################################################################################################################
#### MUSIC ROOM #######################################################################################################
########################################################################################################################
init python:
    mr = MusicRoom(fadeout=0.3, loop=True, single_track=True)
    current_song = "Battlefield of Love (Inst.)"
    current_duration = "3.30"
    mr.add("music/apology.ogg")
    mr.add("music/bagpipes.ogg")
    mr.add("music/bravery.ogg")
    mr.add("music/chill.ogg")
    mr.add("music/churchill.ogg")
    mr.add("music/cosmos.ogg")
    mr.add("music/cyrano.ogg")
    mr.add("music/defeat.ogg")
    mr.add("music/desert.ogg")
    mr.add("music/drama.ogg")
    mr.add("music/empress.ogg")
    mr.add("music/evil.ogg")
    mr.add("music/facepalm.ogg")
    mr.add("music/freedomfries.ogg")
    mr.add("music/fun.ogg")
    mr.add("music/fury.ogg")
    mr.add("music/glory.ogg")
    mr.add("music/history.ogg")
    mr.add("music/savetheday.ogg")
    mr.add("music/holiday.ogg")
    mr.add("music/horror.ogg")
    mr.add("music/joinparty.ogg")
    mr.add("music/soviagrad.ogg")
    mr.add("music/love.ogg")
    mr.add("music/nyan.ogg")
    mr.add("music/map.ogg")
    mr.add("music/messing.ogg")
    mr.add("music/monty.ogg")
    mr.add("music/nemesis.ogg")
    mr.add("music/zipangu.ogg")
    mr.add("music/oohlala.ogg")
    mr.add("music/pantsu.ogg")
    mr.add("music/wonderweapon.ogg")
    mr.add("music/rally.ogg")
    mr.add("music/relax.ogg")
    mr.add("music/requiem.ogg")
    mr.add("music/rinni.ogg")
    mr.add("music/rinnirun.ogg")
    mr.add("music/rise.ogg")
    mr.add("music/roijean.ogg")
    mr.add("music/starin.ogg")
    mr.add("music/teatime.ogg")
    mr.add("music/theme.ogg", always_unlocked=True)
    mr.add("music/theme2.ogg")
    mr.add("music/waltz.ogg")
    mr.add("music/winter.ogg")
    mr.add("music/yandere.ogg")
    mr.add("music/zhukky.ogg")
    
screen music_room():
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
        add "gui/overlay_title_jukebox.png"
    frame:
        style_group "music_frame"
        xalign 0.18
        yalign 0
        hbox:
            vbox:
                style_group "song_frame"
                textbutton "Entschuldigt" action [mr.Play("music/apology.ogg"), SetVariable("current_song", "Entshuldigt"), SetVariable("current_duration", "2.32")]
                textbutton "Bagpipes" action [mr.Play("music/bagpipes.ogg"), SetVariable("current_song", "Bagpipes"), SetVariable("current_duration", "1.12")]
                textbutton "For The Brave" action [mr.Play("music/bravery.ogg"), SetVariable("current_song", "For The Brave"), SetVariable("current_duration", "1.46")]
                textbutton "Chilling Indoors" action [mr.Play("music/chill.ogg"), SetVariable("current_song", "Chilling Indoors"), SetVariable("current_duration", "2.20")]
                textbutton "An Icy Chill" action [mr.Play("music/winter.ogg"), SetVariable("current_song", "An Icy Chill"), SetVariable("current_duration", "1.49")]
                textbutton "Cosmos" action [mr.Play("music/cosmos.ogg"), SetVariable("current_song", "Cosmos"), SetVariable("current_duration", "2.15")]
                textbutton "Requiem" action [mr.Play("music/requiem.ogg"), SetVariable("current_song", "Requiem"), SetVariable("current_duration", "0.57")] 
                textbutton "Yandere" action [mr.Play("music/yandere.ogg"), SetVariable("current_song", "Yandere"), SetVariable("current_duration", "1.30")]
                textbutton "Defeated" action [mr.Play("music/defeat.ogg"), SetVariable("current_song", "Defeated"), SetVariable("current_duration", "2.13")]
                textbutton "Desert Plains" action [mr.Play("music/desert.ogg"), SetVariable("current_song", "Desert Plains"), SetVariable("current_duration", "1.39")]
                textbutton "Dramatic Scene" action [mr.Play("music/drama.ogg"), SetVariable("current_song", "Dramatic Scene"), SetVariable("current_duration", "1.21")]
                textbutton "Lotus Blossom" action [mr.Play("music/empress.ogg"), SetVariable("current_song", "Lotus Blossom"), SetVariable("current_duration", "1.25")] 
                textbutton "Evil Thoughts" action [mr.Play("music/evil.ogg"), SetVariable("current_song", "Evil Thoughts"), SetVariable("current_duration", "2.21")]
                
            null width 10
            vbox:
                frame:
                    style_group "soundwave_frame"
                    frame:
                        background None
                        top_padding 24
                        hbox:
                            vbox:
                                xalign 0
                                xminimum 490
                                xmaximum 490
                                text current_song:
                                    text_align 0
                                    xalign 0
                            vbox:
                                xminimum 60
                                xmaximum 60
                                xalign 1
                                text current_duration:
                                    text_align 1
                                    xalign 1
                                
                null height 10
                hbox:
                    vbox:
                        style_group "song_frame"
                        textbutton "Facepalm" action [mr.Play("music/facepalm.ogg"), SetVariable("current_song", "Facepalm"), SetVariable("current_duration", "1.16")]
                        textbutton "Freedom Fries" action [mr.Play("music/freedomfries.ogg"), SetVariable("current_song", "Freedom Fries"), SetVariable("current_duration", "2.05")]
                        textbutton "Fun and Games" action [mr.Play("music/fun.ogg"), SetVariable("current_song", "Fun and Games"), SetVariable("current_duration", "1.13")]
                        textbutton "Fury" action [mr.Play("music/fury.ogg"), SetVariable("current_song", "Fury"), SetVariable("current_duration", "2.30")]
                        textbutton "Glory" action [mr.Play("music/glory.ogg"), SetVariable("current_song", "Glory"), SetVariable("current_duration", "1.47")]
                        textbutton "Die Versammlung" action [mr.Play("music/rally.ogg"), SetVariable("current_song", "Die Versammlung"), SetVariable("current_duration", "2.04")]
                        textbutton "Scars of History" action [mr.Play("music/history.ogg"), SetVariable("current_song", "Scars of History"), SetVariable("current_duration", "2.18")]
                        textbutton "Waltz" action [mr.Play("music/waltz.ogg"), SetVariable("current_song", "Waltz"), SetVariable("current_duration", "2.00")]
                        textbutton "Bikini Girls" action [mr.Play("music/holiday.ogg"), SetVariable("current_song", "Bikini Girls"), SetVariable("current_duration", "2.10")]
                        textbutton "Horror" action [mr.Play("music/horror.ogg"), SetVariable("current_song", "Horror"), SetVariable("current_duration", "1.07")]
                        textbutton "Join Party" action [mr.Play("music/joinparty.ogg"), SetVariable("current_song", "Join Party"), SetVariable("current_duration", "1.19")]
                        
                    null width 10
                    vbox:
                        style_group "song_frame"
                        textbutton "Anthem of Sovia" action [mr.Play("music/soviagrad.ogg"), SetVariable("current_song", "Anthem of Sovia"), SetVariable("current_duration", "1.37")]
                        textbutton "Love Letter" action [mr.Play("music/love.ogg"), SetVariable("current_song", "Love Letter"), SetVariable("current_duration", "1.50")]
                        textbutton "Shore Leave" action [mr.Play("music/relax.ogg"), SetVariable("current_song", "Shore Leave"), SetVariable("current_duration", "1.45")]
                        textbutton "Goofing Around" action [mr.Play("music/messing.ogg"), SetVariable("current_song", "Goofing Around"), SetVariable("current_duration", "1.20")]
                        textbutton "Maps" action [mr.Play("music/map.ogg"), SetVariable("current_song", "Maps"), SetVariable("current_duration", "1.04")]
                        textbutton "Teatime" action [mr.Play("music/teatime.ogg"), SetVariable("current_song", "Teatime"), SetVariable("current_duration", "1.06")]
                        textbutton "Il Douché" action [mr.Play("music/rinni.ogg"), SetVariable("current_song", "Il Douché"), SetVariable("current_duration", "1.48")]
                        textbutton "Run Il Douché" action [mr.Play("music/rinnirun.ogg"), SetVariable("current_song", "Run Il Douché"), SetVariable("current_duration", "1.11")]
                        textbutton "Eastern Lands" action [mr.Play("music/zipangu.ogg"), SetVariable("current_song", "Eastern Lands"), SetVariable("current_duration", "2.09")]
                        textbutton "La Mayonnaise" action [mr.Play("music/oohlala.ogg"), SetVariable("current_song", "La Mayonnaise"), SetVariable("current_duration", "1.31")]
                        textbutton "Pantsu" action [mr.Play("music/pantsu.ogg"), SetVariable("current_song", "Pantsu"), SetVariable("current_duration", "1.18")]
                        
            null width 10
            vbox:
                style_group "song_frame"
                textbutton "Save The Day" action [mr.Play("music/savetheday.ogg"), SetVariable("current_song", "Save The Day"), SetVariable("current_duration", "2.24")]
                textbutton "Nemesis" action [mr.Play("music/nemesis.ogg"), SetVariable("current_song", "Nemesis"), SetVariable("current_duration", "1.52")]
                textbutton "Queen Jean" action [mr.Play("music/roijean.ogg"), SetVariable("current_song", "Queen Jean"), SetVariable("current_duration", "1.53")]
                textbutton "La Revolution" action [mr.Play("music/cyrano.ogg"), SetVariable("current_song", "La Revolution"), SetVariable("current_duration", "1.51")]
                textbutton "Desert Rat" action [mr.Play("music/monty.ogg"), SetVariable("current_song", "Desert Rat"), SetVariable("current_duration", "1.43")]
                textbutton "The Bulldog" action [mr.Play("music/churchill.ogg"), SetVariable("current_song", "The Bulldog"), SetVariable("current_duration", "2.47")]
                textbutton "Wintertime War" action [mr.Play("music/zhukky.ogg"), SetVariable("current_song", "Wintertime War"), SetVariable("current_duration", "3.00")]
                textbutton "Mother of Nations" action [mr.Play("music/starin.ogg"), SetVariable("current_song", "Mother of Nations"), SetVariable("current_duration", "1.55")]
                textbutton "Wonderweapon" action [mr.Play("music/wonderweapon.ogg"), SetVariable("current_song", "Wonderweapon"), SetVariable("current_duration", "2.07")]
                textbutton "Red Generalissima" action [mr.Play("music/nyan.ogg"), SetVariable("current_song", "Red Generalissima"), SetVariable("current_duration", "1.38")]
                textbutton "Battlefield of Love" action [mr.Play("music/theme2.ogg"), SetVariable("current_song", "Battlefield of Love"), SetVariable("current_duration", "3.31")]
                textbutton "Battlefield of Love (Inst.)" action [mr.Play("music/theme.ogg"), SetVariable("current_song", "Battlefield of Love (Inst.)"), SetVariable("current_duration", "3.30")]
                textbutton "Rise (Credits)" action [mr.Play("music/rise.ogg"), SetVariable("current_song", "Rise (Credits)"), SetVariable("current_duration", "4.23")]
                
    on "replace" action mr.Play()
    on "replaced" action Play("music", "music/theme.ogg")
    frame:
        background Frame(im.Sepia("gui/outer_frame.png"), 200, 200)
        