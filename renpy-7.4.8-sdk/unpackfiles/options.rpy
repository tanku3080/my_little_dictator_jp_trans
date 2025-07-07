
init -1 python hide:
    config.developer = False
    config.new_translate_order = False
    config.screen_width = 1920
    config.screen_height = 1080
    config.window_title = u"My Little Dictator"
    config.window_icon = "icon.png"
    config.mouse = {"default": [("gui/mouse_cursor.png", 27, 27)]}
    config.name = "My Little Dictator"
    config.version = "1.0"
    config.quit_action = Quit(confirm=True)
    config.emphasize_audio_channels = [ 'voice' ]
    config.emphasize_audio_channels = [ 'mapsfx' ]
    config.thumbnail_width = config.screen_width
    config.thumbnail_height = config.screen_height
    config.enter_sound = "se/click.ogg"
    config.exit_sound = "se/click.ogg"
    config.sample_sound = "se/click.ogg"
    config.main_menu_music = "music/theme.ogg" 
    config.help = "README.html"
    config.enter_transition = None
    config.exit_transition = dissolve
    config.intra_transition = dissolve
    config.main_game_transition = dissolve
    config.game_main_transition = dissolve
    config.end_splash_transition = dissolve
    config.end_game_transition = dissolve
    config.after_load_transition = dissolve
    config.window_show_transition = None
    config.window_hide_transition = None
    config.has_sound = True
    config.has_music = True
    config.has_voice = True
    config.default_fullscreen = False
    config.transition_screens = False
    preferences.text_cps = 110
    config.narrator_menu = True
    config.default_afm_time = 10
    config.default_afm_enable = False
    
    config.atl_one_frame = False
    config.keep_show_layer_state = False
    config.dismiss_blocking_transitions = False
    config.dissolve_force_alpha = False
    config.atl_start_on_show = False
    config.keep_running_transform = False
    config.default_music_volume = 0.5
    config.default_sfx_volume = 0.65
    config.default_voice_volume = 1.0
    config.has_autosave = True
    config.autosave_on_quit = False
    
    layout.ARE_YOU_SURE = "Are you sure?"
    layout.DELETE_SAVE = "Are you sure you want to delete this save?"
    layout.OVERWRITE_SAVE = "Are you sure you want to overwrite your save?"
    layout.LOADING = "Loading will lose unsaved progress. Are you sure?"
    layout.QUIT = "Are you sure you want to quit?"
    layout.MAIN_MENU = "Are you sure you want to return to the main menu?"
    layout.END_REPLAY = "Are you sure you want to end the replay?"
    layout.SLOW_SKIP = "Are you sure you want to begin skipping?"
    layout.FAST_SKIP_SEEN = "Are you sure you want to skip to the next choice?"
    layout.FAST_SKIP_UNSEEN = "Are you sure you want to skip unseen dialogue?"
    theme.bordered(
        mm_root = "menuback",
        gm_root = "gmroot",
        rounded_window = False,
        )

    
python early:
    config.save_directory = "My Little Dictator-1324912024"
    
default mmboomsound = True
define build.include_i686 = False
define config.steam_appid = 1882820

init python:
    build.directory_name = "My_Little_Dictator-1.0"
    build.executable_name = "My Little Dictator"
    build.include_update = False
    
    ## Classify files as None to exclude them from the built distributions.
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    
    ## To archive files, classify them as 'archive'.
    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.ogg', 'archive')
    build.classify('game/**.rpy', 'archive')
    build.classify('game/**.rpyc', 'archive')
    build.classify('game/**.json', 'archive')
    build.classify('game/**.ttf', 'archive')
    build.classify('game/**.otf', 'archive')
    
    ## Files matching documentation patterns are duplicated in a mac app
    ## build, so they appear in both the app and the zip file.
    build.documentation('*.html')
    build.documentation('*.txt')
