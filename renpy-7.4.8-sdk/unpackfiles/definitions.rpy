#############################################################################################
# DEFINITIONS ################################################################################
#############################################################################################

#############################################################################################
# CHARACTERS ###############################################################################
#############################################################################################
#Zipangu
define narrator = Character(" ", color="#DCD3BB", show_two_window=True, image="logo_th", ctc="ctc1", ctc_position="fixed")
define me = Character('Yamato', color="#DCD3BB", show_two_window=True, image="yamato", ctc="ctc1", ctc_position="fixed")
define hirahita = Character('Hirahita', color="#DCD3BB", show_two_window=True, image="hirahita", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "hirahita"))
define hirahita_un = Character('Beauty', color="#DCD3BB", show_two_window=True, image="hirahita", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "hirahita"))
define tak = Character('Takeshi', color="#DCD3BB", show_two_window=True, image="takeshi", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "soldier"))
define tak_un = Character('Junior', color="#DCD3BB", show_two_window=True, image="takeshi", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "soldier"))
define yamamoto = Character('Yamamoto', color="#DCD3BB", show_two_window=True, image="yamamoto", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "oldman"))
define yamamoto_un = Character('Zipangu Admiral', color="#DCD3BB", show_two_window=True, image="yamamoto", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "oldman"))

#Germania
define hit = Character('Hitora', color="#DCD3BB", show_two_window=True, image="hitora", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "hitora"))
define rom = Character('Rommel', color="#DCD3BB", show_two_window=True, image="rommel", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "rommel"))
define rom_un = Character('Furry Girl', color="#DCD3BB", show_two_window=True, image="rommel", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "rommel"))
define dresckow = Character('Dresckow', color="#DCD3BB", show_two_window=True, image="dresckow", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "dresckow"))
define dresckow_un = Character('Mysterious Man', color="#DCD3BB", show_two_window=True, image="dresckow", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "dresckow"))
define nhit = Character('Nega-Hitora', color="#DCD3BB", show_two_window=True, image="negahitora", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "hubala"))
define hittt = Character('Hitora?', color="#DCD3BB", show_two_window=True, image="negahitora", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "hubala"))
define gor = Character('Goring', color="#DCD3BB", show_two_window=True, image="goring", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "goring"))
define goeb = Character('Joebbels', color="#DCD3BB", show_two_window=True, image="joebbels", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "joebbels"))
define don = Character('Dunitz', color="#DCD3BB", show_two_window=True, image="dunitz", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "dunitz"))
define gud = Character('Guderian', color="#DCD3BB", show_two_window=True, image="guderian", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "guderian"))
define mans = Character('Manstein', color="#DCD3BB", show_two_window=True, image="manstein", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "manstein"))
define mans_un = Character('Pretty Girl', color="#DCD3BB", show_two_window=True, image="manstein", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "manstein"))
define kaupisch = Character('Kaupisch', color="#DCD3BB", show_two_window=True, image="germaniangeneraloberst", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "general"))
define listte = Character('Listte', color="#DCD3BB", show_two_window=True, image="germaniangeneraloberst", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "general"))
define borkind = Character('Borkind', color="#DCD3BB", show_two_window=True, image="borkind", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "youth"))
define borkind_un = Character('Young Secretary', color="#DCD3BB", show_two_window=True, image="borkind", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "youth"))
define hess = Character('Hess', color="#DCD3BB", show_two_window=True, image="hess", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "general"))
define hess_un = Character('Speaker', color="#DCD3BB", show_two_window=True, image="hess", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "general"))
define evan = Character('Evan Braun', color="#DCD3BB", show_two_window=True, image="evanbraun", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "man"))
define evan_un = Character('Handsome Stranger', color="#DCD3BB", show_two_window=True, image="evanbraun", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "man"))
define dau = Character('Dau', color="#DCD3BB", show_two_window=True, image="germanianadmiral", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "general"))
define major = Character('Major', color="#DCD3BB", show_two_window=True, image="germaniangeneral", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "general"))
define pilot = Character('Pilot', color="#DCD3BB", show_two_window=True, image="soldier", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "soldier"))
define kaiser = Character('Wilhelmina', color="#DCD3BB", show_two_window=True, image="kaiser", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "general"))
define beck = Character('Beck', color="#DCD3BB", show_two_window=True, image="beck", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "general"))
define beck_un = Character('Mysterious General', color="#DCD3BB", show_two_window=True, image="beck", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "general"))
define keitel = Character('Keitel', color="#DCD3BB", show_two_window=True,  show_side_image=Image(im.Sepia("character/side/keitel_th.png"), xalign=0.02, yalign=1.07), ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "sovian"))
define brauchitsch = Character('Brauchitsch', color="#DCD3BB", show_two_window=True,  show_side_image=Image(im.Sepia("character/side/brauchitsch_th.png"), xalign=0.02, yalign=1.07), ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "nyan"))
define gestapo = Character('Goosetapo Officer', color="#DCD3BB", show_two_window=True, image="gestapo", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "youth"))
define hoth = Character('Hoth', color="#DCD3BB", show_two_window=True, show_side_image=Image(im.Sepia("character/side/hoth_th.png"), xalign=0.02, yalign=1.07), ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "hoth"))
define hoth_un = Character('Wild Bear', color="#DCD3BB", show_two_window=True, show_side_image=Image(im.Sepia("character/side/hoth_th.png"), xalign=0.02, yalign=1.07), ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "hoth"))
define hoth_grrr = Character('Low Growling Voice', color="#DCD3BB", show_two_window=True, show_side_image=Image(im.Sepia("character/side/blank_th.png"), xalign=0.02, yalign=1.07), ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "hoth"))
define ewalda = Character('Ewalda', color="#DCD3BB", show_two_window=True, show_side_image=Image(im.Sepia("character/side/ewalda_th.png"), xalign=0.02, yalign=1.07), ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "joebbels"))
define linge = Character('Linge', color="#DCD3BB", show_two_window=True, image="germaniangeneral", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "general"))
define lammers = Character('Lammers', color="#DCD3BB", show_two_window=True, image="politician", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "politician"))
define kanari = Character('Kanari', color="#DCD3BB", show_two_window=True, show_side_image=Image(im.Sepia("character/side/kanari_th.png"), xalign=0.02, yalign=1.07), ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "starin"))
define ooster = Character('Ooster', color="#DCD3BB", show_two_window=True, show_side_image=Image(im.Sepia("character/side/ooster_th.png"), xalign=0.02, yalign=1.07), ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "youth"))
define valkenhorst = Character('Valkenhorst', color="#DCD3BB", show_two_window=True, image="valkenhorst", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "rommel"))
define dietling = Character('Dietling', color="#DCD3BB", show_two_window=True, image="dietling", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "youth"))
define hoppyner = Character('Hoppyner', color="#DCD3BB", show_two_window=True, image="hoppyner", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "axis"))
define zchaal = Character('Zchaal', color="#DCD3BB", show_two_window=True, image="zchaal", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "youth"))
define ztauffenborg = Character('Ztauffenborg', color="#DCD3BB", show_two_window=True, image="ztauffenborg", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "general"))
define himmora = Character('Himmora', color="#DCD3BB", show_two_window=True, show_side_image=Image(im.Sepia("character/side/himmora_th.png"), xalign=0.02, yalign=1.07), ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "hubala"))
define rantzau = Character('Prockdorff-Lantzau', color="#DCD3BB", show_two_window=True, image="reynaud", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "politician"))

#Franzo
define roijean = Character('Reine', color="#DCD3BB", show_two_window=True, image="roijean", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "roijean"))
define cyr = Character('Cyrano', color="#DCD3BB", show_two_window=True, image="cyrano", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "cyrano"))
define cyr_un = Character('Cute Girl', color="#DCD3BB", show_two_window=True, image="cyrano", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "cyrano"))
define gam = Character('Gamelin', color="#DCD3BB", show_two_window=True, image="gamelin", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "gamelin"))
define gam_un = Character('General', color="#DCD3BB", show_two_window=True, image="gamelin", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "gamelin"))
define reynaud = Character('Leynaud', color="#DCD3BB", show_two_window=True, image="reynaud", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "politician"))
define daladier = Character('Talatier', color="#DCD3BB", show_two_window=True, image="reynaud", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "politician"))
define weygand = Character('Weygand', color="#DCD3BB", show_two_window=True, image="weygand", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "general"))
define franzosol = Character('Franzo Soldier', color="#DCD3BB", show_two_window=True, image="franzo", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "soldier"))
define brioche = Character('Brioche', color="#DCD3BB", show_two_window=True, image="oriasiangeneral", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "general"))
define huntziger = Character('Huntziger', color="#DCD3BB", show_two_window=True, image="franzo", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "soldier"))
define petain = Character('Petain', color="#DCD3BB", show_two_window=True, image="billotte", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "oldman"))
define billotte = Character('Billotte', color="#DCD3BB", show_two_window=True, image="billotte", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "oldman"))

#Britannia
define monty = Character('Monty', color="#DCD3BB", show_two_window=True, image="monty", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "monty"))
define ch = Character('Churchill', color="#DCD3BB", show_two_window=True, image="churchill", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "churchill"))
define chambers = Character('Chambers', color="#DCD3BB", show_two_window=True, image="chambers", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "oldman"))
define batt = Character('Battenia', color="#DCD3BB", show_two_window=True, image="battenia", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "battenia"))
define brookie = Character('Brookie', color="#DCD3BB", show_two_window=True, image="brookie", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "soldier"))
define jumbo = Character('Jumbo', color="#DCD3BB", show_two_window=True, image="jumbo", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "fatman"))
define stuffy = Character('Stuffy', color="#DCD3BB", show_two_window=True, image="stuffy", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "stuffy"))
define gort = Character('Gort', color="#DCD3BB", show_two_window=True, image="gort", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "general"))
define freyaborg = Character('Freyaborg', color="#DCD3BB", show_two_window=True,  show_side_image=Image(im.Sepia("character/side/freyaborg_th.png"), xalign=0.02, yalign=1.07), ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "general"))
define halifax = Character('Halifax', color="#DCD3BB", show_two_window=True, image="halifax", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "youth"))
define wavell = Character('Wavell', color="#DCD3BB", show_two_window=True, image="wavell", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "allied"))
define george = Character('Jorge VI', color="#DCD3BB", show_two_window=True, image="politician2", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "politician"))
define logue = Character('Rude Ostralasian', color="#DCD3BB", show_two_window=True, image="aussieman", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "man"))
define ironsides = Character('Ironsides', color="#DCD3BB", show_two_window=True, image="basicgeneral", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "general"))
define bound = Character('Bound', color="#DCD3BB", show_two_window=True, image="oldwoman", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "oldwoman"))
define sonny = Character('Sonny', color="#DCD3BB", show_two_window=True, image="politician", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "politician"))
define vasey = Character('Bloody Vasey', color="#DCD3BB", show_two_window=True, image="vasey", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "youth"))

#Sovia
define zh = Character('Zhukky', color="#DCD3BB", show_two_window=True, image="zhukky", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "zhukky"))
define zhukky_un = Character('Strange Girl', color="#DCD3BB", show_two_window=True, image="zhukky", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "zhukky"))
define star = Character('Starin', color="#DCD3BB", show_two_window=True, image="starin", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "starin"))
define star_un= Character('Short Girl', color="#DCD3BB", show_two_window=True, image="starin", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "starin"))
define molotov = Character('Molotov', color="#DCD3BB", show_two_window=True, image="molotov", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "molotov"))
define vas = Character('Vasile', color="#DCD3BB", show_two_window=True, image="vasile", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "vasile"))
define klima = Character('Klima', color="#DCD3BB", show_two_window=True, image="klima", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "allied"))
define pavlov = Character('Pavlov', color="#DCD3BB", show_two_window=True, image="pavlov", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "youth"))
define kirponos = Character('Kirponos', color="#DCD3BB", show_two_window=True, image="kirponos", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "general"))
define dimashenka = Character('Dimashenka', color="#DCD3BB", show_two_window=True, image="dimashenka", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "general"))
define zorge = Character('Zorge', color="#DCD3BB", show_two_window=True, image="politician2", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "politician"))
define soviangeneral = Character('Sovian General', color="#DCD3BB", show_two_window=True, image="soviangeneral", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "general"))

#Vitalia
define rin = Character('Rinni', color="#DCD3BB", show_two_window=True, image="rinni", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "rinni"))
define mussorin = Character('Mussorinni', color="#DCD3BB", show_two_window=True, image="rinni", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "rinni"))
define bad = Character('Badoglio', color="#DCD3BB", show_two_window=True, image="badoglio", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "badoglio"))
define messe = Character('Messe', color="#DCD3BB", show_two_window=True, image="messe", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "messe"))
define graz = Character('Graziani', color="#DCD3BB", show_two_window=True, image="graziani", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "graziani"))
define graz_un = Character('Vitalian Officer', color="#DCD3BB", show_two_window=True, image="graziani", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "graziani"))
define maletti = Character('Maletti', color="#DCD3BB", show_two_window=True, image="vitalia", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "soldier"))
define vitaliasol = Character('Vitalian Soldier', color="#DCD3BB", show_two_window=True, image="vitalia", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "soldier"))
define gariboldi = Character('Gariboldi', color="#DCD3BB", show_two_window=True, image="gariboldi", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "oldman"))
define gariboldi_un = Character('Old General', color="#DCD3BB", show_two_window=True, image="gariboldi", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "oldman"))
define cavallero = Character('Cavallero', color="#DCD3BB", show_two_window=True, image="cavallero", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "youth"))

#Amerika
define fdr = Character('Roosevelt', color="#DCD3BB", show_two_window=True, image="roosevelt", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "roosevelt"))
define gi = Character('GI Soldier', color="#DCD3BB", show_two_window=True, image="amerika", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "soldier"))
define agent = Character('Agent', color="#DCD3BB", show_two_window=True, image="agent", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "fatman"))
define eisenhoo = Character('Eisenhoo', color="#DCD3BB", show_two_window=True,  show_side_image=Image(im.Sepia("character/side/eisenhoo_th.png"), xalign=0.02, yalign=1.07), ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "sovian"))
define patton = Character('Pattonko', color="#DCD3BB", show_two_window=True,  show_side_image=Image(im.Sepia("character/side/patton_th.png"), xalign=0.02, yalign=1.07), ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "axis"))
define macartha = Character('MacArtha', color="#DCD3BB", show_two_window=True,  show_side_image=Image(im.Sepia("character/side/macartha_th.png"), xalign=0.02, yalign=1.07), ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "allied"))

#Zhina
define nyan = Character('Nyan Katshex', color="#DCD3BB", show_two_window=True, image="nyan", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "nyan"))
define zhinasol = Character('Zhina Soldier', color="#DCD3BB", show_two_window=True, image="oriasiangeneral", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "general"))
define zhinawom = Character('Peasant Girl', color="#DCD3BB", show_two_window=True, image="woman", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "woman"))

#Norda
define quisling = Character('Quisling', color="#DCD3BB", show_two_window=True, image="quisling", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "politician"))
define quisling_un = Character('Older Man', color="#DCD3BB", show_two_window=True, image="quisling", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "politician"))
define haakon = Character('Haakon', color="#DCD3BB", show_two_window=True, image="haakon", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "man"))
define luge = Character('Luge', color="#DCD3BB", show_two_window=True, image="luge", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "man"))
define vleischer = Character('Vleischer', color="#DCD3BB", show_two_window=True, image="vleischer", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "molotov"))
define nygaaaaardsvool = Character('Nygaaaaardsvool', color="#DCD3BB", show_two_window=True, image="politician2", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "politician"))
define nordasol = Character('Norda Soldier', color="#DCD3BB", show_two_window=True, image="norda", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "allied"))

#Dania
define christian = Character('Christian X', color="#DCD3BB", show_two_window=True, image="christian", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "youth"))
define prior = Character('Prior', color="#DCD3BB", show_two_window=True, image="prior", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "youth"))
define daniayouth = Character('Dania Soldier', color="#DCD3BB", show_two_window=True, image="daniayouth", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "youth"))

#Serpana
define tito = Character('Tito', color="#DCD3BB", show_two_window=True, image="tito", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "tito"))
define tito_un = Character('Scrappy Girl', color="#DCD3BB", show_two_window=True, image="tito", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "tito"))
define cvetkovic = Character('Cvetkovic', color="#DCD3BB", show_two_window=True, image="cvetkovic", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "gamelin"))
define paul = Character('Prince Paulie', color="#DCD3BB", show_two_window=True, image="politician", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "politician"))
define simovic = Character('Simovic', color="#DCD3BB", show_two_window=True, image="simovic", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "oldwoman"))
define miha = Character('Mihaila', color="#DCD3BB", show_two_window=True, image="mihaila", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "oldman"))

#Finbard
define mann = Character('Mannerheim', color="#DCD3BB", show_two_window=True, image="mannerheim", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "mannerheim"))
define fin = Character('Finbardish Soldier', color="#DCD3BB", show_two_window=True, image="finbard", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "axis"))

#Hang
define hor = Character('Horthy', color="#DCD3BB", show_two_window=True, image="horthy", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "horthy"))
define teleki = Character('Teleki', color="#DCD3BB", show_two_window=True, image="cvetkovic", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "man"))
define dossy = Character('Dossy', color="#DCD3BB", show_two_window=True, image="politician", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "politician"))

#Rumanum
define anton = Character('Antoness', color="#DCD3BB", show_two_window=True, image="antoness", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "antoness"))
define anton_un = Character('Redhead Girl', color="#DCD3BB", show_two_window=True, image="antoness", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "antoness"))
define carol = Character('King Garol', color="#DCD3BB", show_two_window=True, image="king", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "man"))
define calin = Character('Kalinesgu', color="#DCD3BB", show_two_window=True, image="kalinesgu", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "dresckow"))
define sima = Character('Cshima', color="#DCD3BB", show_two_window=True, image="sima", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "woman"))

#Polix
define smig = Character('Smigly', color="#DCD3BB", show_two_window=True, image="smigly", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "smigly"))
define stach = Character('Stachie', color="#DCD3BB", show_two_window=True, image="stachie", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "fatman"))
define sikorski = Character('Sikorskia', color="#DCD3BB", show_two_window=True, image="sikorski", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "sovian"))
define polixsol = Character('Polix Soldier', color="#DCD3BB", show_two_window=True, image="polix", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "soldier"))
define hubal = Character('Hubala', color="#DCD3BB", show_two_window=True, image="hubal", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "hubala"))
define hubal_un = Character('Polix Resister', color="#DCD3BB", show_two_window=True, image="hubal", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "hubala"))
define polixfake = Character('Fake Polix Soldier', color="#DCD3BB", show_two_window=True, image="polixfake", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "hubala"))

#Batavia
define vinkelman = Character('Vinkelman', color="#DCD3BB", show_two_window=True, image="soldier", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "soldier"))

#Belgae
define leopold = Character('Leopold', color="#DCD3BB", show_two_window=True,  show_side_image=Image(im.Sepia("character/side/leopold_th.png"), xalign=0.02, yalign=1.07), ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "youth"))

#Other Named Figures
define franco = Character('Franco', color="#DCD3BB", show_two_window=True, image="basicgeneral", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "general"))
define metaxas = Character('Metaxas', color="#DCD3BB", show_two_window=True, image="metaxas", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "man"))
define rashidali = Character('Radish Ali', color="#DCD3BB", show_two_window=True, image="desertman", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "man"))
define smart = Character('Smart', color="#DCD3BB", show_two_window=True, image="soldier", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "soldier"))

#Soldiers
define sov = Character('Sovian Soldier', color="#DCD3BB", show_two_window=True, image="sovian", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "sovian"))
define woundedsoldier = Character('{size=25}Wounded Soldier{/size}', color="#DCD3BB", show_two_window=True, image="aussieman", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "man"))
define axis = Character('{size=25}Germanian Soldier{/size}', color="#DCD3BB", show_two_window=True, image="axis", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "axis"))
define winteraxis = Character('{size=25}Germanian Paratrooper{/size}', color="#DCD3BB", show_two_window=True, image="winteraxis", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "axis"))
define allied = Character('{size=25}Alliance Soldier{/size}', color="#DCD3BB", show_two_window=True, image="allied", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "allied"))
define irajigen = Character('Iraji General', color="#DCD3BB", show_two_window=True, image="desertgeneral", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "general"))
define germaniangeneral = Character('Germanian General', color="#DCD3BB", show_two_window=True, image="germaniangeneral", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "general"))
define britanniangen = Character('Britannian General', color="#DCD3BB", show_two_window=True, image="britanniangeneral", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "general"))
define zombiegen = Character('ZZ Officer', color="#DCD3BB", show_two_window=True, image="zombiegeneral", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "hubala"))
define zombiesol = Character('ZZ Soldier', color="#DCD3BB", show_two_window=True, image="zombiesoldier", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "hubala"))
define guard = Character('Guard', color="#DCD3BB", show_two_window=True, image="zipangu", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "general"))
define guard2 = Character('Guard', color="#DCD3BB", show_two_window=True, image="desertgeneral", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "general"))
define eng = Character('Engineer', color="#DCD3BB", show_two_window=True, image="axis", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "axis"))
define med = Character('Medic', color="#DCD3BB", show_two_window=True, image="axis", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "axis"))
define germanianadmiral = Character('Germanian Admiral', color="#DCD3BB", show_two_window=True, image="germanianadmiral", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "general"))
define germaniansailor = Character('Officer Stratton', color="#DCD3BB", show_two_window=True, image="germanianadmiral", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "general"))
define revolutionary = Character('Revolutionary', color="#DCD3BB", show_two_window=True, image="desertaxis", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "axis"))
define zipangusol = Character('Zipangu Soldier', color="#DCD3BB", show_two_window=True, image="zipangu", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "soldier"))
define norda = Character('Norda Soldier', color="#DCD3BB", show_two_window=True, image="norda", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "sovian"))
define zipangusolwom = Character('{size=25}Zipanguese Soldier{/size}', color="#DCD3BB", show_two_window=True, image="axis", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "axis"))

#Non-specific Characters
define lef = Character('Lieutenant', color="#DCD3BB", show_two_window=True, image="oriasiangeneral", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "general"))
define nurse = Character('Nurse', color="#DCD3BB", show_two_window=True, image="nurse", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "woman"))
define youth = Character('Youth', color="#DCD3BB", show_two_window=True, image="youth", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "youth"))
define zipanguyouth = Character('Youth', color="#DCD3BB", show_two_window=True, image="zipanguyouth", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "youth"))
define desertyouth = Character('Youth', color="#DCD3BB", show_two_window=True, image="desertyouth", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "youth"))
define om = Character('Old Man', color="#DCD3BB", show_two_window=True, image="oldman", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "oldman"))
define desertom = Character('Old Man', color="#DCD3BB", show_two_window=True, image="desertoldman", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "oldman"))
define ow = Character('Old Woman', color="#DCD3BB", show_two_window=True, image="oldwoman", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "oldwoman"))
define desertow = Character('Old Woman', color="#DCD3BB", show_two_window=True, image="desertoldwoman", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "oldwoman"))
define man = Character('Man', color="#DCD3BB", show_two_window=True, image="man", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "man"))
define desertman = Character('Man', color="#DCD3BB", show_two_window=True, image="desertman", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "man"))
define impman = Character('Gentleman', color="#DCD3BB", show_two_window=True, image="official", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "politician"))
define sol = Character('Soldier', color="#DCD3BB", show_two_window=True, image="soldier", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "soldier"))
define driver = Character('Driver', color="#DCD3BB", show_two_window=True, image="soldier", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "soldier"))
define pol = Character('Politician', color="#DCD3BB", show_two_window=True, image="politician", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "politician"))
define richman = Character('Rich Man', color="#DCD3BB", show_two_window=True, image="politician", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "politician"))
define sk = Character('Shopkeep', color="#DCD3BB", show_two_window=True, image="fatman", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "fatman"))
define doc = Character('Doctor', color="#DCD3BB", show_two_window=True, image="politician", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "politician"))
define wom = Character('Woman', color="#DCD3BB", show_two_window=True, image="woman", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "woman"))
define bro = Character('Brother', color="#DCD3BB", show_two_window=True, image="oldman", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "oldman"))
define off = Character('Official', color="#DCD3BB", show_two_window=True, image="official", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "politician"))
define informant = Character('Informant', color="#DCD3BB", show_two_window=True, image="desertman", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "politician"))
define maid = Character('Maid', color="#DCD3BB", show_two_window=True, image="maid", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "woman"))
define servant = Character('Servant', color="#DCD3BB", show_two_window=True, image="servant1", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "politician"))
define servant2 = Character('Servant', color="#DCD3BB", show_two_window=True, image="servant2", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "politician"))
define girl = Character('Girl', color="#DCD3BB", show_two_window=True, image="woman", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "woman"))
define younggirl = Character('Daughter', color="#DCD3BB", show_two_window=True, show_side_image=Image("character/side/blank_th.png", xalign=0.02, yalign=1.07), ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "youth"))
define v = Character('Voice', color="#DCD3BB", show_two_window=True, show_side_image=Image("character/side/blank_th.png", xalign=0.02, yalign=1.07), ctc="ctc1", ctc_position="fixed")
define deepv = Character('Voice', color="#DCD3BB", show_two_window=True, show_side_image=Image("character/side/blank_th.png", xalign=0.02, yalign=1.07), ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "oldman"))
define highv = Character('Voice', color="#DCD3BB", show_two_window=True, show_side_image=Image("character/side/blank_th.png", xalign=0.02, yalign=1.07), ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "starin"))
define eve = Character('Everyone', color="#DCD3BB", show_two_window=True, show_side_image=Image("character/side/blank_th.png", xalign=0.02, yalign=1.07), ctc="ctc1", ctc_position="fixed")
define att = Character('Attendant', color="#DCD3BB", show_two_window=True, image="official", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "politician"))
define fat = Character('Fat Man', color="#DCD3BB", show_two_window=True, image="fatman", ctc="ctc1", ctc_position="fixed", callback=partial(char_chat, "fatman"))
define crowd = Character('Crowd', color="#DCD3BB", show_two_window=True, show_side_image=Image("character/side/blank_th.png", xalign=0.02, yalign=1.07), ctc="ctc1", ctc_position="fixed")

#############################################################################################                
# POSITIONS #################################################################################
#############################################################################################
define layover = Position(xpos=0.51, ypos=0.5, xanchor='center', yanchor='center')
define right05 = Position(xpos=0.92)
define right1 = Position(xpos=0.9)
define right15 = Position(xpos=0.85)
define right2 = Position(xpos=0.8)
define right25 = Position(xpos=0.75)
define right27 = Position(xpos=0.725)
define right3 = Position(xpos=0.7)
define right37 = Position(xpos=0.625)
define right35 = Position(xpos=0.65)
define right4 = Position(xpos=0.6)
define right45 = Position(xpos=0.55)
define horizontalcenter = Position(xpos=0.5)
define pickup = Position(xpos=0.5, ypos=1.1)
define pickupleft = Position(xpos=0.3, ypos=1.1)
define pickupright = Position(xpos=0.7, ypos=1.1)
define left05 = Position(xpos=0.08)
define left1 = Position(xpos=0.1)
define left15 = Position(xpos=0.15)
define left17 = Position(xpos=0.17)
define left2 = Position(xpos=0.2)
define left25 = Position(xpos=0.25)
define left3 = Position(xpos=0.3, ypos=1.0)
define left35 = Position(xpos=0.35)
define left4 = Position(xpos=0.4)
define left45 = Position(xpos=0.45)
define tacticalpos = Position(xalign=0.05, yalign=0.01)
define tankpos = Position(xalign=0.5, yalign=0.01)

#############################################################################################                         
# MUSIC CHANNELS AND OTHER DEFINITIONS ####################################################
#############################################################################################
define config.new_translate_order = False
define config.enforce_window_max_size = False

init python:    
    renpy.music.register_channel("soundfx", "sfx", True)
    renpy.music.register_channel("soundfx2", "sfx", True)
    renpy.music.register_channel("soundfx3", "sfx", True)
    renpy.music.register_channel("soundfx4", "sfx", True)
    renpy.music.register_channel("soundfx5", "sfx", True)
    renpy.music.register_channel("soundfx6", "sfx", True)
    renpy.music.register_channel("sound2", "sfx", False)
    renpy.music.register_channel("sound3", "sfx", False)
    renpy.music.register_channel("sound4", "sfx", False)
    renpy.music.register_channel("sound5", "sfx", False)
    renpy.music.register_channel("sound6", "sfx", False)
    renpy.music.register_channel("sound7", "sfx", False)
    renpy.music.register_channel("sound8", "sfx", False)
    renpy.music.register_channel("mapsfx", "sfx", False)
    renpy.music.register_channel("mmsound", "sfx", False)
    renpy.music.register_channel("mmsound2", "sfx", False)
    renpy.music.register_channel("mmsound3", "sfx", False)
    renpy.music.register_channel("battlesound1", "sfx", False)
    renpy.music.register_channel("battlesound2", "sfx", False)
    renpy.music.register_channel("battleattack", "sfx", False)
    renpy.music.register_channel("battlevoice", "voice", False)
    renpy.music.register_channel("battlemusic", "music", True)
    renpy.music.register_channel("battlesfx", "sfx", True)
    renpy.music.register_channel("victorymusic", "music", True)
    renpy.music.register_channel("tickersound", "sfx", True)
    renpy.music.register_channel("truevoice", "voice", False)
    renpy.music.register_channel("silsound2", "sfx", False)
    renpy.music.register_channel("silsound3", "sfx", False)
    renpy.music.register_channel("silsound4", "sfx", False)
    renpy.music.register_channel("silsound5", "sfx", False)
    renpy.music.register_channel("silsound6", "sfx", False)
    renpy.music.register_channel("silsound7", "sfx", False)
    renpy.music.register_channel("silsound8", "sfx", False)
    
    def silhouette_matrix (r,g,b,a=1.0):
        return im.matrix((0, 0, 0, 0, r, 
                               0, 0, 0, 0, g,
                               0, 0, 0, 0, b,
                               0, 0, 0, a, 0,))
        
    def silhouetted (filename, r,g,b, a = 1.0):
        return im.MatrixColor (Image (filename), silhouette_matrix (r,g,b,a))
    
    def play_sound_when_clicked():
        renpy.music.play("se/click.ogg","sound")
        
    def play_sound_when_dragged(a,b):
        renpy.music.play("se/click.ogg","sound")
    
    show_window_trans = MoveTransition(0.25,
                                       enter_factory=MoveIn((None, 
                                       1.0, None, 0.0)))

    hide_window_trans = MoveTransition(0.25,
                                       leave_factory=MoveOut((None, 
                                       1.0, None, 0.0)))
        
    def hide_window():
        store._window_during_transitions = False
        narrator("", interact=False)
        renpy.with_statement(None)
        renpy.with_statement(hide_window_trans)

    def show_window():
        narrator("", interact=False)
        renpy.with_statement(show_window_trans)
        store._window_during_transitions = True
        
#############################################################################################
# TRANSITIONS ###############################################################################
#############################################################################################
define dissolve2 = Dissolve(4.0)
define dissolve3 = Dissolve(10.0)
define dissolve4 = Dissolve(2.0)
define dissolve5 = Dissolve(8.0)
define dissolve6 = Dissolve(0.2)
define flash = Fade(.25, 0, .75, color="#fff")
define circleirisout = ImageDissolve("back/effects/id_circleiris.png", .2, 8)

