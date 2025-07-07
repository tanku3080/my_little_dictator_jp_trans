#----------------------------------------------------------------------------------------------------------------------------------------------------------
###MAP GRAPHICS
#----------------------------------------------------------------------------------------------------------------------------------------------------------
########################################################
# Buttons #################################################
########################################################
image yesno_no_small_idle = "gui/yesno_no_small_idle.png"
image yesno_no_small_hover = "gui/yesno_no_small_hover.png"
    
image in_idle = "gui/map/invade.png"
image in_hover =  "gui/map/invade2.png"

image map_marker_idle = "gui/map/map_marker.png"
image map_marker_hover = im.MatrixColor("gui/map/map_marker.png", im.matrix.brightness(0.2) * im.matrix.opacity(1))
image map_marker_insensitive = im.MatrixColor("gui/map/map_marker.png", im.matrix.brightness(0) * im.matrix.opacity(0.2))

image pyramid_big_idle = "gui/map/pyramid_big.png"
image pyramid_big_hover = im.MatrixColor("gui/map/pyramid_big.png", im.matrix.brightness(0.2) * im.matrix.opacity(1))
image bigben_big_idle = "gui/map/bigben_big.png"
image bigben_big_hover = im.MatrixColor("gui/map/bigben_big.png", im.matrix.brightness(0.2) * im.matrix.opacity(1))
image eiffel_big_idle = "gui/map/eiffel_big.png"
image eiffel_big_hover = im.MatrixColor("gui/map/eiffel_big.png", im.matrix.brightness(0.2) * im.matrix.opacity(1))
image kremlin_big_idle = "gui/map/kremlin_big.png"
image kremlin_big_hover = im.MatrixColor("gui/map/kremlin_big.png", im.matrix.brightness(0.2) * im.matrix.opacity(1))
image villa_big_idle = "gui/map/villa_big.png"
image villa_big_hover = im.MatrixColor("gui/map/villa_big.png", im.matrix.brightness(0.2) * im.matrix.opacity(1))
image imperium_big_idle = "gui/map/imperium_big.png"
image imperium_big_hover = im.MatrixColor("gui/map/imperium_big.png", im.matrix.brightness(0.2) * im.matrix.opacity(1))

########################################################
# Icons #################################################
########################################################
image icon_farming_small = im.FactorScale("gui/map/icon_farming.png", 0.6)
image icon_mining_small = im.FactorScale("gui/map/icon_mining.png", 0.6)
image icon_industry_small = im.FactorScale("gui/map/icon_industry.png", 0.6)
image icon_trade_small = im.FactorScale("gui/map/icon_trade.png", 0.6)
image icon_entertainment_small = im.FactorScale("gui/map/icon_entertainment.png", 0.6)
image icon_military_small = im.FactorScale("gui/map/icon_military.png", 0.6)
image icon_corruption_small = im.FactorScale("gui/map/icon_corruption.png", 0.6)
image icon_command = "gui/map/icon_command.png"
image icon_management = "gui/map/icon_management.png"
image icon_influence = "gui/map/icon_influence.png"

image starinbasesmall = im.Sepia(im.Crop(im.FactorScale("back/starinbase.jpg", 0.76), (10, 0, 1435, 400)))
image albionsmall = im.Sepia(im.Crop(im.FactorScale("back/albion_day.jpg", 0.76), (10, 100, 1435, 400)))
image lutetiasmall = im.Sepia(im.Crop(im.FactorScale("back/lutetia.jpg", 0.76), (10, 0, 1435, 400)))
image imperiumsmall = im.Sepia(im.Crop(im.FactorScale("back/imperium.jpg", 0.76), (10, 0, 1435, 400)))
image rinnimansionsmall = im.Sepia(im.Crop(im.FactorScale("back/mansion3.jpg", 0.76), (10, 0, 1435, 400)))
image conquestsmall = im.Sepia(im.Crop(im.FactorScale("cg/cg_soldiers.jpg", 0.76), (10, 140, 1435, 400)))
image pyramidsmall = im.Sepia(im.Crop(im.FactorScale("back/pyramid.jpg", 0.76), (10, 0, 1435, 400)))
image mayraicon = im.Sepia(im.Crop(im.FactorScale("back/field_day.jpg", 0.395), (260, 100, 240, 213)))
image spruiticon = im.Sepia(im.Crop(im.FactorScale("back/farm_tanks.jpg", 0.395), (260, 100, 240, 213)))
image ancyraicon = im.Sepia(im.Crop(im.FactorScale("back/temple.jpg", 0.395), (260, 100, 240, 213)))
image bucharexicon = im.Sepia(im.Crop(im.FactorScale("back/countrylane_day_notree_night.jpg", 0.395), (260, 100, 240, 213)))
image atheniaicon = im.Sepia(im.Crop(im.FactorScale("back/temple.jpg", 0.395), (260, 50, 240, 213)))
image iraklionicon = im.Sepia(im.Crop(im.FactorScale("back/temple.jpg", 0.395), (260, 50, 240, 213)))
image zaarkrautenicon = im.Sepia(im.Crop(im.FactorScale("back/woodland_day.jpg", 0.395), (260, 100, 240, 213)))
image serdicaicon = im.Sepia(im.Crop(im.FactorScale("back/forest_day.jpg", 0.395), (260, 100, 240, 213)))
image singidunicon = im.Sepia(im.Crop(im.FactorScale("back/woodland_clearing.jpg", 0.395), (260, 100, 240, 213)))
image rotteicon = im.Sepia(im.Crop(im.FactorScale("back/village2.jpg", 0.395), (260, 100, 240, 213)))
image amstelicon = im.Sepia(im.Crop(im.FactorScale("back/city3.jpg", 0.395), (260, 100, 240, 213)))
image rijaicon = im.Sepia(im.Crop(im.FactorScale("back/city2.jpg", 0.395), (260, 100, 240, 213)))
image helsinicon = im.Sepia(im.Crop(im.FactorScale("back/snow_day.jpg", 0.395), (260, 100, 240, 213)))
image zuriicon = im.Sepia(im.Crop(im.FactorScale("back/snow_day.jpg", 0.395), (260, 100, 240, 213)))
image syndromeicon = im.Sepia(im.Crop(im.FactorScale("back/village1.jpg", 0.395), (260, 100, 240, 213)))
image oxloaicon = im.Sepia(im.Crop(im.FactorScale("back/snow_tanks.jpg", 0.395), (260, 100, 240, 213)))
image hafnicon = im.Sepia(im.Crop(im.FactorScale("back/countrylane_day.jpg", 0.395), (260, 100, 240, 213)))
image balstogeicon = im.Sepia(im.Crop(im.FactorScale("back/city2.jpg", 0.395), (260, 100, 240, 213)))
image varsaaicon = im.Sepia(im.Crop(im.FactorScale("back/city1.jpg", 0.395), (260, 100, 240, 213)))
image romeicon = im.Sepia(im.Crop(im.FactorScale("back/mansion3.jpg", 0.395), (260, 100, 240, 213)))
image torinoicon = im.Sepia(im.Crop(im.FactorScale("back/port.jpg", 0.395), (260, 100, 240, 213)))
image eideannicon = im.Sepia(im.Crop(im.FactorScale("back/port.jpg", 0.395), (260, 100, 240, 213)))
image freevilleicon = im.Sepia(im.Crop(im.FactorScale("back/desert_day.jpg", 0.395), (260, 100, 240, 213)))
image koufraicon = im.Sepia(im.Crop(im.FactorScale("back/desert_night.jpg", 0.395), (260, 100, 240, 213)))
image tobrunskicon = im.Sepia(im.Crop(im.FactorScale("back/desert_town.jpg", 0.395), (260, 100, 240, 213)))
image bulaggnaicon = im.Sepia(im.Crop(im.FactorScale("back/port.jpg", 0.395), (260, 100, 240, 213)))
image salernumicon = im.Sepia(im.Crop(im.FactorScale("back/port.jpg", 0.395), (260, 100, 240, 213)))
image palmaaicon = im.Sepia(im.Crop(im.FactorScale("back/desert_smoke.jpg", 0.395), (260, 100, 240, 213)))
image benghatzaicon = im.Sepia(im.Crop(im.FactorScale("back/desert_day.jpg", 0.395), (260, 100, 240, 213)))
image damascaicon = im.Sepia(im.Crop(im.FactorScale("back/desert_town.jpg", 0.395), (260, 100, 240, 213)))
image nanzigicon = im.Sepia(im.Crop(im.FactorScale("back/field_day.jpg", 0.395), (260, 100, 240, 213)))
image vicheiicon = im.Sepia(im.Crop(im.FactorScale("back/field_day.jpg", 0.395), (260, 100, 240, 213)))
image taigaicon = im.Sepia(im.Crop(im.FactorScale("back/woodland_night.jpg", 0.395), (260, 100, 240, 213)))
image ruinicon = im.Sepia(im.Crop(im.FactorScale("back/woodland_night.jpg", 0.395), (260, 100, 240, 213)))
image dunkirchicon = im.Sepia(im.Crop(im.FactorScale("back/beach_trees.jpg", 0.395), (260, 100, 240, 213)))
image lutetiaicon = im.Sepia(im.Crop(im.FactorScale("back/lutetia.jpg", 0.395), (20, 20, 240, 213)))
image kairicon = im.Sepia(im.Crop(im.FactorScale("back/pyramid.jpg", 0.395), (260, 100, 240, 213)))
image burburraicon = im.Sepia(im.Crop(im.FactorScale("back/desert_day.jpg", 0.395), (260, 100, 240, 213)))
image vaghdadicon = im.Sepia(im.Crop(im.FactorScale("back/desert_town.jpg", 0.395), (260, 100, 240, 213)))
image castelicon = im.Sepia(im.Crop(im.FactorScale("back/desert_town.jpg", 0.395), (260, 100, 240, 213)))
image dovertownicon = im.Sepia(im.Crop(im.FactorScale("back/port.jpg", 0.395), (260, 100, 240, 213)))
image aeliaicon = im.Sepia(im.Crop(im.FactorScale("back/desert_bunker.jpg", 0.395), (260, 100, 240, 213)))
image moskvaicon = im.Sepia(im.Crop(im.FactorScale("back/starinbase.jpg", 0.395), (260, 100, 240, 213)))
image kharkovaicon = im.Sepia(im.Crop(im.FactorScale("back/tunnel.jpg", 0.395), (260, 100, 240, 213)))
image minxicon = im.Sepia(im.Crop(im.FactorScale("back/field_day_notree.jpg", 0.395), (260, 100, 240, 213)))
image konigicon = im.Sepia(im.Crop(im.FactorScale("back/altberlin.jpg", 0.395), (260, 100, 240, 213)))
image altendresdenicon = im.Sepia(im.Crop(im.FactorScale("back/alley1.jpg", 0.395), (260, 100, 240, 213)))
image wienicon = im.Sepia(im.Crop(im.FactorScale("back/altberlin.jpg", 0.395), (260, 100, 240, 213)))
image trevaicon = im.Sepia(im.Crop(im.FactorScale("back//altberlin.jpg", 0.395), (260, 100, 240, 213)))
image bratiburgicon = im.Sepia(im.Crop(im.FactorScale("back/altberlin.jpg", 0.395), (260, 100, 240, 213)))
image budasticon = im.Sepia(im.Crop(im.FactorScale("back/altberlin.jpg", 0.395), (260, 100, 240, 213)))
image altberlinicon = im.Sepia(im.Crop(im.FactorScale("back/balcony.jpg", 0.395), (260, 100, 240, 213)))
image albionicon = im.Sepia(im.Crop(im.FactorScale("back/albion_day.jpg", 0.395), (500, 20, 240, 213)))
image khiavaicon = im.Sepia(im.Crop(im.FactorScale("back/field_day.jpg", 0.395), (260, 100, 240, 213)))
image staringradaicon = im.Sepia(im.Crop(im.FactorScale("back/staringrada.jpg", 0.395), (260, 100, 240, 213)))
image smolenxicon = im.Sepia(im.Crop(im.FactorScale("back/city4.jpg", 0.395), (260, 100, 240, 213)))
image reningradaicon = im.Sepia(im.Crop(im.FactorScale("back/city1.jpg", 0.395), (260, 100, 240, 213)))

########################################################
# Allegiance Icons #################################################
########################################################
image flag_afrikaa_idle = im.FactorScale("gui/flag_afrikaa.png", 0.72)
image flag_assyria_idle = im.FactorScale("gui/flag_assyria.png", 0.72)
image flag_batavia_idle = im.FactorScale("gui/flag_batavia.png", 0.72)
image flag_occbatavia_idle = im.FactorScale("gui/flag_germania.png", 0.72)
image flag_belgae_idle = im.FactorScale("gui/flag_belgae.png", 0.72)
image flag_occbelgae_idle = im.FactorScale("gui/flag_germania.png", 0.72)
image flag_bolga_idle = im.FactorScale("gui/flag_bolga.png", 0.72)
image flag_borussia_idle = im.FactorScale("gui/flag_borussia.png", 0.72)
image flag_britannia_idle = im.FactorScale("gui/flag_britannia.png", 0.72)
image flag_cilly_idle = im.FactorScale("gui/flag_vitalia.png", 0.72)
image flag_xorsa_idle = im.FactorScale("gui/flag_franzo.png", 0.72)
image flag_cyracana_idle = im.FactorScale("gui/flag_cyracana.png", 0.72)
image flag_czexa_idle = im.FactorScale("gui/flag_czexa.png", 0.72)
image flag_dania_idle = im.FactorScale("gui/flag_dania.png", 0.72)
image flag_occdania_idle = im.FactorScale("gui/flag_germania.png", 0.72)
image flag_ogygia_idle = im.FactorScale("gui/flag_ogygia.png", 0.72)
image flag_epirus_idle = im.FactorScale("gui/flag_epirus.png", 0.72)
image flag_finbard_idle = im.FactorScale("gui/flag_finbard.png", 0.72)
image flag_franzo_idle = im.FactorScale("gui/flag_franzo.png", 0.72)
image flag_occfranzo_idle = im.FactorScale("gui/flag_germania.png", 0.72)
image flag_vicheifranzo_idle = im.FactorScale("gui/flag_franzo.png", 0.72)
image flag_galatia_idle = im.FactorScale("gui/flag_galatia.png", 0.72)
image flag_germania_idle = im.FactorScale("gui/flag_germania.png", 0.72)
image flag_gibrata_idle = im.FactorScale("gui/flag_gibrata.png", 0.72)
image flag_grecia_idle = im.FactorScale("gui/flag_grecia.png", 0.72)
image flag_occgrecia_idle = im.FactorScale("gui/flag_germania.png", 0.72)
image flag_gypta_idle = im.FactorScale("gui/flag_gypta.png", 0.72)
image flag_hang_idle = im.FactorScale("gui/flag_hang.png", 0.72)
image flag_iberia_idle = im.FactorScale("gui/flag_iberia.png", 0.72)
image flag_vitalia_idle = im.FactorScale("gui/flag_vitalia.png", 0.72)
image flag_iraji_idle = im.FactorScale("gui/flag_iraji.png", 0.72)
image flag_kaptara_idle = im.FactorScale("gui/flag_grecia.png", 0.72)
image flag_occkaptara_idle = im.FactorScale("gui/flag_germania.png", 0.72)
image flag_kyprosa_idle = im.FactorScale("gui/flag_kyprosa.png", 0.72)
image flag_livonia_idle = im.FactorScale("gui/flag_livonia.png", 0.72)
image flag_sovlivonia_idle = im.FactorScale("gui/flag_sovia.png", 0.72)
image flag_occlivonia_idle = im.FactorScale("gui/flag_germania.png", 0.72)
image flag_maltana_idle = im.FactorScale("gui/flag_britannia.png", 0.72)
image flag_zipangu_idle = im.FactorScale("gui/flag_zipangu.png", 0.72)
image flag_norda_idle = im.FactorScale("gui/flag_norda.png", 0.72)
image flag_occnorda_idle = im.FactorScale("gui/flag_germania.png", 0.72)
image flag_osta_idle = im.FactorScale("gui/flag_germania.png", 0.72)
image flag_palesta_idle = im.FactorScale("gui/flag_palesta.png", 0.72)
image flag_polix_idle = im.FactorScale("gui/flag_polix.png", 0.72)
image flag_gerpolix_idle = im.FactorScale("gui/flag_germania.png", 0.72)
image flag_sovpolix_idle = im.FactorScale("gui/flag_sovia.png", 0.72)
image flag_occsovpolix_idle = im.FactorScale("gui/flag_germania.png", 0.72)
image flag_rumanum_idle = im.FactorScale("gui/flag_rumanum.png", 0.72)
image flag_zardina_idle = im.FactorScale("gui/flag_vitalia.png", 0.72)
image flag_serpana_idle = im.FactorScale("gui/flag_serpana.png", 0.72)
image flag_soviamajor_idle = im.FactorScale("gui/flag_sovia.png", 0.72)
image flag_soviaminor_idle = im.FactorScale("gui/flag_sovia.png", 0.72)
image flag_svenda_idle = im.FactorScale("gui/flag_svenda.png", 0.72)
image flag_swizi_idle = im.FactorScale("gui/flag_swizi.png", 0.72)
image flag_trevera_idle = im.FactorScale("gui/flag_germania.png", 0.72)
image flag_tripolita_idle = im.FactorScale("gui/flag_tripolita.png", 0.72)
image flag_unitedamerika_idle = im.FactorScale("gui/flag_amerika.png", 0.72)
image flag_zhina_idle = im.FactorScale("gui/flag_zhina.png", 0.72)
image flag_zomali_idle = im.FactorScale("gui/flag_britannia.png", 0.72)
image flag_occzomali_idle = im.FactorScale("gui/flag_vitalia.png", 0.72)
image flag_zudanea_idle = im.FactorScale("gui/flag_gypta.png", 0.72)
image flag_niker_idle = im.FactorScale("gui/flag_franzo.png", 0.72)
image flag_brad_idle = im.FactorScale("gui/flag_franzo.png", 0.72)
image flag_eva_idle = im.FactorScale("gui/flag_vitalia.png", 0.72)
image flag_erebiensands_idle = im.FactorScale("gui/flag_erebiensands.png", 0.72)
image flag_banki_idle = im.FactorScale("gui/flag_franzo.png", 0.72)
image flag_franzogonko_idle = im.FactorScale("gui/flag_franzo.png", 0.72)
image flag_britnigella_idle = im.FactorScale("gui/flag_britannia.png", 0.72)
image flag_kamrun_idle = im.FactorScale("gui/flag_franzo.png", 0.72)
image flag_westafrikaa_idle = im.FactorScale("gui/flag_franzo.png", 0.72)
image flag_bradlib_idle = im.FactorScale("gui/flag_franzolibre.png", 0.72)
image flag_kamrunlib_idle = im.FactorScale("gui/flag_franzolibre.png", 0.72)
image flag_bankilib_idle = im.FactorScale("gui/flag_franzolibre.png", 0.72)
image flag_fgonkolib_idle = im.FactorScale("gui/flag_franzolibre.png", 0.72)
image flag_xrovat_idle = im.FactorScale("gui/flag_xrovat.png", 0.72)
image flag_cervetiis_idle = im.FactorScale("gui/flag_germania.png", 0.72)
image flag_sovxarelia_idle = im.FactorScale("gui/flag_sovia.png", 0.72)

image flag_afrikaa_hover = im.MatrixColor(im.FactorScale("gui/flag_afrikaa.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_assyria_hover = im.MatrixColor(im.FactorScale("gui/flag_assyria.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_batavia_hover = im.MatrixColor(im.FactorScale("gui/flag_batavia.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_occbatavia_hover = im.MatrixColor(im.FactorScale("gui/flag_germania.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_belgae_hover = im.MatrixColor(im.FactorScale("gui/flag_belgae.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_occbelgae_hover = im.MatrixColor(im.FactorScale("gui/flag_germania.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_bolga_hover = im.MatrixColor(im.FactorScale("gui/flag_bolga.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_borussia_hover = im.MatrixColor(im.FactorScale("gui/flag_borussia.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_britannia_hover = im.MatrixColor(im.FactorScale("gui/flag_britannia.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_cilly_hover = im.MatrixColor(im.FactorScale("gui/flag_vitalia.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_xorsa_hover = im.MatrixColor(im.FactorScale("gui/flag_franzo.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_cyracana_hover = im.MatrixColor(im.FactorScale("gui/flag_cyracana.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_czexa_hover = im.MatrixColor(im.FactorScale("gui/flag_czexa.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_dania_hover = im.MatrixColor(im.FactorScale("gui/flag_dania.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_occdania_hover = im.MatrixColor(im.FactorScale("gui/flag_germania.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_ogygia_hover = im.MatrixColor(im.FactorScale("gui/flag_ogygia.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_epirus_hover = im.MatrixColor(im.FactorScale("gui/flag_epirus.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_finbard_hover = im.MatrixColor(im.FactorScale("gui/flag_finbard.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_franzo_hover = im.MatrixColor(im.FactorScale("gui/flag_franzo.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_occfranzo_hover = im.MatrixColor(im.FactorScale("gui/flag_germania.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_vicheifranzo_hover = im.MatrixColor(im.FactorScale("gui/flag_franzo.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_galatia_hover = im.MatrixColor(im.FactorScale("gui/flag_galatia.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_germania_hover = im.MatrixColor(im.FactorScale("gui/flag_germania.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_gibrata_hover = im.MatrixColor(im.FactorScale("gui/flag_gibrata.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_grecia_hover = im.MatrixColor(im.FactorScale("gui/flag_grecia.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_occgrecia_hover = im.MatrixColor(im.FactorScale("gui/flag_germania.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_gypta_hover = im.MatrixColor(im.FactorScale("gui/flag_gypta.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_hang_hover = im.MatrixColor(im.FactorScale("gui/flag_hang.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_iberia_hover = im.MatrixColor(im.FactorScale("gui/flag_iberia.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_vitalia_hover = im.MatrixColor(im.FactorScale("gui/flag_vitalia.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_iraji_hover = im.MatrixColor(im.FactorScale("gui/flag_iraji.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_kaptara_hover = im.MatrixColor(im.FactorScale("gui/flag_grecia.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_occkaptara_hover = im.MatrixColor(im.FactorScale("gui/flag_germania.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_kyprosa_hover = im.MatrixColor(im.FactorScale("gui/flag_kyprosa.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_livonia_hover = im.MatrixColor(im.FactorScale("gui/flag_livonia.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_sovlivonia_hover = im.MatrixColor(im.FactorScale("gui/flag_sovia.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_occlivonia_hover = im.MatrixColor(im.FactorScale("gui/flag_germania.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_maltana_hover = im.MatrixColor(im.FactorScale("gui/flag_britannia.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_zipangu_hover = im.MatrixColor(im.FactorScale("gui/flag_zipangu.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_norda_hover = im.MatrixColor(im.FactorScale("gui/flag_norda.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_occnorda_hover = im.MatrixColor(im.FactorScale("gui/flag_germania.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_osta_hover = im.MatrixColor(im.FactorScale("gui/flag_germania.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_palesta_hover = im.MatrixColor(im.FactorScale("gui/flag_palesta.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_polix_hover = im.MatrixColor(im.FactorScale("gui/flag_polix.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_gerpolix_hover = im.MatrixColor(im.FactorScale("gui/flag_germania.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_sovpolix_hover = im.MatrixColor(im.FactorScale("gui/flag_sovia.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_occsovpolix_hover = im.MatrixColor(im.FactorScale("gui/flag_germania.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_rumanum_hover = im.MatrixColor(im.FactorScale("gui/flag_rumanum.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_zardina_hover = im.MatrixColor(im.FactorScale("gui/flag_vitalia.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_serpana_hover = im.MatrixColor(im.FactorScale("gui/flag_serpana.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_soviamajor_hover = im.MatrixColor(im.FactorScale("gui/flag_sovia.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_soviaminor_hover = im.MatrixColor(im.FactorScale("gui/flag_sovia.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_svenda_hover = im.MatrixColor(im.FactorScale("gui/flag_svenda.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_swizi_hover = im.MatrixColor(im.FactorScale("gui/flag_swizi.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_trevera_hover = im.MatrixColor(im.FactorScale("gui/flag_germania.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_tripolita_hover = im.MatrixColor(im.FactorScale("gui/flag_tripolita.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_unitedamerika_hover = im.MatrixColor(im.FactorScale("gui/flag_amerika.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_zhina_hover = im.MatrixColor(im.FactorScale("gui/flag_zhina.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_zomali_hover = im.MatrixColor(im.FactorScale("gui/flag_britannia.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_occzomali_hover = im.MatrixColor(im.FactorScale("gui/flag_vitalia.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_zudanea_hover = im.MatrixColor(im.FactorScale("gui/flag_gypta.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_niker_hover = im.MatrixColor(im.FactorScale("gui/flag_franzo.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_brad_hover = im.MatrixColor(im.FactorScale("gui/flag_franzo.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_eva_hover = im.MatrixColor(im.FactorScale("gui/flag_vitalia.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_erebiensands_hover = im.MatrixColor(im.FactorScale("gui/flag_erebiensands.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_banki_hover = im.MatrixColor(im.FactorScale("gui/flag_franzo.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_franzogonko_hover = im.MatrixColor(im.FactorScale("gui/flag_franzo.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_britnigella_hover = im.MatrixColor(im.FactorScale("gui/flag_britannia.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_kamrun_hover = im.MatrixColor(im.FactorScale("gui/flag_franzo.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_westafrikaa_hover = im.MatrixColor(im.FactorScale("gui/flag_franzo.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_bradlib_hover = im.MatrixColor(im.FactorScale("gui/flag_franzolibre.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_kamrunlib_hover = im.MatrixColor(im.FactorScale("gui/flag_franzolibre.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_bankilib_hover = im.MatrixColor(im.FactorScale("gui/flag_franzolibre.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_fgonkolib_hover = im.MatrixColor(im.FactorScale("gui/flag_franzolibre.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_xrovat_hover = im.MatrixColor(im.FactorScale("gui/flag_xrovat.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_cervetiis_hover = im.MatrixColor(im.FactorScale("gui/flag_germania.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))
image flag_sovxarelia_hover = im.MatrixColor(im.FactorScale("gui/flag_sovia.png", 0.72), im.matrix.brightness(0.2) * im.matrix.opacity(1))

image militarycircle001_brauchitsch = "character/side/brauchitsch_th.png"
image militarycircle002_keitel = "character/side/keitel_th.png"
image militarycircle003_dunitz = "side dunitz bored"
image militarycircle004_goring = "side goring happy"
image militarycircle005_blank = "character/side/blank_th.png"
image militarycircle006_blank = "character/side/blank_th.png"
image militarycircle007_krancke = "side desertgeneral normal"
image militarycircle008_sperrle = "side politician2 determined"
image zinnercircle_blank = "character/side/blank_th.png"
image zinnercircle_blank2 = "character/side/blank_th.png"
image zinnercircle_blank3 = "character/side/blank_th.png"

########################################################
# Local Companies ########################################
########################################################
image company_albioncornexchange = "gui/companies/company_albioncornexchange.png"
image company_axemann = "gui/companies/company_axemann.png"
image company_caveavin = "gui/companies/company_caveavin.png"
image company_dokuk = "gui/companies/company_dokuk.png"
image company_ducepasta = "gui/companies/company_ducepasta.png"
image company_freedomburger = "gui/companies/company_freedomburger.png"
image company_fuuhbarcakes = "gui/companies/company_fuuhbarcakes.png"
image company_ghoulish = "gui/companies/company_ghoulish.png"
image company_grupp = "gui/companies/company_grupp.png"
image company_guptatours = "gui/companies/company_guptatours.png"
image company_handlarz = "gui/companies/company_handlarz.png"
image company_iorginaicecream = "gui/companies/company_iorginaicecream.png"
image company_lugobust = "gui/companies/company_lugobust.png"
image company_magische = "gui/companies/company_magische.png"
image company_molkereiwagen = "gui/companies/company_molkereiwagen.png"
image company_motherofnationspelts = "gui/companies/company_motherofnationspelts.png"
image company_ottoflugzeugwerke = "gui/companies/company_ottoflugzeugwerke.png"
image company_panpanpan = "gui/companies/company_panpanpan.png"
image company_penguinironworks = "gui/companies/company_penguinironworks.png"
image company_petwelt = "gui/companies/company_petwelt.png"
image company_pizzahaus = "gui/companies/company_pizzahaus.png"
image company_sakurawhale = "gui/companies/company_sakurawhale.png"
image company_southernmining = "gui/companies/company_southernmining.png"
image company_sovianpotato = "gui/companies/company_sovianpotato.png"
image company_tanfa = "gui/companies/company_tanfa.png"
image company_teaempire = "gui/companies/company_teaempire.png"
image company_toothhurty = "gui/companies/company_toothhurty.png"
image company_victorrubber = "gui/companies/company_victorrubber.png"
image company_woodyslogging = "gui/companies/company_woodyslogging.png"
image company_zippilen = "gui/companies/company_zippilen.png"

########################################################
# Captured Füühbarmuseum ##################################
########################################################
image captured_arch = "gui/captured/captured_arch.png"
image captured_bank = "gui/captured/captured_bank.png"
image captured_barmaleyfountain = "gui/captured/captured_barmaleyfountain.png"
image captured_beerhall = "gui/captured/captured_beerhall.png"
image captured_woodenbench = "gui/captured/captured_woodenbench.png"
image captured_bigben = "gui/captured/captured_bigben.png"
image captured_bollard = "gui/captured/captured_bollard.png"
image captured_bones = "gui/captured/captured_bones.png"
image captured_brandenburggate = "gui/captured/captured_brandenburggate.png"
image captured_brickhouse = "gui/captured/captured_brickhouse.png"
image captured_bunker = "gui/captured/captured_bunker.png"
image captured_bush = "gui/captured/captured_bush.png"
image captured_cafe = "gui/captured/captured_cafe.png"
image captured_zhinahouse = "gui/captured/captured_zhinahouse.png"
image captured_zhinatemple = "gui/captured/captured_zhinatemple.png"
image captured_zhinathrone = "gui/captured/captured_zhinathrone.png"
image captured_church = "gui/captured/captured_church.png"
image captured_cottage = "gui/captured/captured_cottage.png"
image captured_crate = "gui/captured/captured_crate.png"
image captured_debris = "gui/captured/captured_debris.png"
image captured_deserthouse = "gui/captured/captured_deserthouse.png"
image captured_desertrocks = "gui/captured/captured_desertrocks.png"
image captured_desertruins = "gui/captured/captured_desertruins.png"
image captured_deserttower = "gui/captured/captured_deserttower.png"
image captured_dragonteeth = "gui/captured/captured_dragonteeth.png"
image captured_eiffel = "gui/captured/captured_eiffel.png"
image captured_factory = "gui/captured/captured_factory.png"
image captured_farmhousesnow = "gui/captured/captured_farmhousesnow.png"
image captured_flat = "gui/captured/captured_flat.png"
image captured_forest = "gui/captured/captured_forest.png"
image captured_fountainbig = "gui/captured/captured_fountainbig.png"
image captured_fountainsmall = "gui/captured/captured_fountainsmall.png"
image captured_gear = "gui/captured/captured_gear.png"
image captured_guardtower = "gui/captured/captured_guardtower.png"
image captured_hangar = "gui/captured/captured_hangar.png"
image captured_hedgehog = "gui/captured/captured_hedgehog.png"
image captured_hut = "gui/captured/captured_hut.png"
image captured_iceberg = "gui/captured/captured_iceberg.png"
image captured_kremlin = "gui/captured/captured_kremlin.png"
image captured_lamppost = "gui/captured/captured_lamppost.png"
image captured_machinegunnest = "gui/captured/captured_machinegunnest.png"
image captured_mansion = "gui/captured/captured_mansion.png"
image captured_market = "gui/captured/captured_market.png"
image captured_mosque = "gui/captured/captured_mosque.png"
image captured_palace = "gui/captured/captured_palace.png"
image captured_palmtree = "gui/captured/captured_palmtree.png"
image captured_pillbox = "gui/captured/captured_pillbox.png"
image captured_postbox = "gui/captured/captured_postbox.png"
image captured_pyramid = "gui/captured/captured_pyramid.png"
image captured_radiotower = "gui/captured/captured_radiotower.png"
image captured_sandbag = "gui/captured/captured_sandbag.png"
image captured_shrub = "gui/captured/captured_shrub.png"
image captured_snowyrocks = "gui/captured/captured_snowyrocks.png"
image captured_stalagmite = "gui/captured/captured_stalagmite.png"
image captured_statueeagle = "gui/captured/captured_statueeagle.png"
image captured_statuekaiser = "gui/captured/captured_statuekaiser.png"
image captured_statueman = "gui/captured/captured_statueman.png"
image captured_statuewoman = "gui/captured/captured_statuewoman.png"
image captured_sweat = "gui/captured/captured_sweat.png"
image captured_table = "gui/captured/captured_table.png"
image captured_temple = "gui/captured/captured_temple.png"
image captured_tent = "gui/captured/captured_tent.png"
image captured_terrace = "gui/captured/captured_terrace.png"
image captured_theater = "gui/captured/captured_theater.png"
image captured_train = "gui/captured/captured_train.png"
image captured_vases = "gui/captured/captured_vases.png"
image captured_wheat = "gui/captured/captured_wheat.png"
image captured_woodland = "gui/captured/captured_woodland.png"
image captured_x = "gui/captured/captured_x.png"

########################################################
# Exhibits Füühbarmuseum ###################################
########################################################
image museum_arch = ConditionSwitch(
    "museum_arch_unlocked == True", "gui/museum/museum_arch.png",
    "True", im.MatrixColor("gui/museum/museum_arch.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_bank = ConditionSwitch(
    "museum_bank_unlocked == True", "gui/museum/museum_bank.png",
    "True", im.MatrixColor("gui/museum/museum_bank.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_barmaleyfountain = ConditionSwitch(
    "museum_barmaleyfountain_unlocked == True", "gui/museum/museum_barmaleyfountain.png",
    "True", im.MatrixColor("gui/museum/museum_barmaleyfountain.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_beerhall = ConditionSwitch(
    "museum_beerhall_unlocked == True", "gui/museum/museum_beerhall.png",
    "True", im.MatrixColor("gui/museum/museum_beerhall.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_woodenbench = ConditionSwitch(
    "museum_woodenbench_unlocked == True", "gui/museum/museum_woodenbench.png",
    "True", im.MatrixColor("gui/museum/museum_woodenbench.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_bigben = ConditionSwitch(
    "museum_bigben_unlocked == True", "gui/museum/museum_bigben.png",
    "True", im.MatrixColor("gui/museum/museum_bigben.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_bollard = ConditionSwitch(
    "museum_bollard_unlocked == True", "gui/museum/museum_bollard.png",
    "True", im.MatrixColor("gui/museum/museum_bollard.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_bones = ConditionSwitch(
    "museum_bones_unlocked == True", "gui/museum/museum_bones.png",
    "True", im.MatrixColor("gui/museum/museum_bones.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_brandenburggate = ConditionSwitch(
    "museum_brandenburggate_unlocked == True", "gui/museum/museum_brandenburggate.png",
    "True", im.MatrixColor("gui/museum/museum_brandenburggate.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_brickhouse = ConditionSwitch(
    "museum_brickhouse_unlocked == True", "gui/museum/museum_brickhouse.png",
    "True", im.MatrixColor("gui/museum/museum_brickhouse.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_bunker = ConditionSwitch(
    "museum_bunker_unlocked == True", "gui/museum/museum_bunker.png",
    "True", im.MatrixColor("gui/museum/museum_bunker.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_bush = ConditionSwitch(
    "museum_bush_unlocked == True", "gui/museum/museum_bush.png",
    "True", im.MatrixColor("gui/museum/museum_bush.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_cafe = ConditionSwitch(
    "museum_cafe_unlocked == True", "gui/museum/museum_cafe.png",
    "True", im.MatrixColor("gui/museum/museum_cafe.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_zhinahouse = ConditionSwitch(
    "museum_zhinahouse_unlocked == True", "gui/museum/museum_zhinahouse.png",
    "True", im.MatrixColor("gui/museum/museum_zhinahouse.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_zhinatemple = ConditionSwitch(
    "museum_zhinatemple_unlocked == True", "gui/museum/museum_zhinatemple.png",
    "True", im.MatrixColor("gui/museum/museum_zhinatemple.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_zhinathrone = ConditionSwitch(
    "museum_zhinathrone_unlocked == True", "gui/museum/museum_zhinathrone.png",
    "True", im.MatrixColor("gui/museum/museum_zhinathrone.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_church = ConditionSwitch(
    "museum_church_unlocked == True", "gui/museum/museum_church.png",
    "True", im.MatrixColor("gui/museum/museum_church.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_cottage = ConditionSwitch(
    "museum_cottage_unlocked == True", "gui/museum/museum_cottage.png",
    "True", im.MatrixColor("gui/museum/museum_cottage.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_crate = ConditionSwitch(
    "museum_crate_unlocked == True", "gui/museum/museum_crate.png",
    "True", im.MatrixColor("gui/museum/museum_crate.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_debris = ConditionSwitch(
    "museum_debris_unlocked == True", "gui/museum/museum_debris.png",
    "True", im.MatrixColor("gui/museum/museum_debris.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_deserthouse = ConditionSwitch(
    "museum_deserthouse_unlocked == True", "gui/museum/museum_deserthouse.png",
    "True", im.MatrixColor("gui/museum/museum_deserthouse.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_desertrocks = ConditionSwitch(
    "museum_desertrocks_unlocked == True", "gui/museum/museum_desertrocks.png",
    "True", im.MatrixColor("gui/museum/museum_desertrocks.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_desertruins = ConditionSwitch(
    "museum_desertruins_unlocked == True", "gui/museum/museum_desertruins.png",
    "True", im.MatrixColor("gui/museum/museum_desertruins.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_deserttower = ConditionSwitch(
    "museum_deserttower_unlocked == True", "gui/museum/museum_deserttower.png",
    "True", im.MatrixColor("gui/museum/museum_deserttower.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_dragonteeth = ConditionSwitch(
    "museum_dragonteeth_unlocked == True", "gui/museum/museum_dragonteeth.png",
    "True", im.MatrixColor("gui/museum/museum_dragonteeth.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_eiffel = ConditionSwitch(
    "museum_eiffel_unlocked == True", "gui/museum/museum_eiffel.png",
    "True", im.MatrixColor("gui/museum/museum_eiffel.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_factory = ConditionSwitch(
    "museum_factory_unlocked == True", "gui/museum/museum_factory.png",
    "True", im.MatrixColor("gui/museum/museum_factory.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_farmhousesnow = ConditionSwitch(
    "museum_farmhousesnow_unlocked == True", "gui/museum/museum_farmhousesnow.png",
    "True", im.MatrixColor("gui/museum/museum_farmhousesnow.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_flat = ConditionSwitch(
    "museum_flat_unlocked == True", "gui/museum/museum_flat.png",
    "True", im.MatrixColor("gui/museum/museum_flat.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_forest = ConditionSwitch(
    "museum_forest_unlocked == True", "gui/museum/museum_forest.png",
    "True", im.MatrixColor("gui/museum/museum_forest.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_fountainbig = ConditionSwitch(
    "museum_fountainbig_unlocked == True", "gui/museum/museum_fountainbig.png",
    "True", im.MatrixColor("gui/museum/museum_fountainbig.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_fountainsmall = ConditionSwitch(
    "museum_fountainsmall_unlocked == True", "gui/museum/museum_fountainsmall.png",
    "True", im.MatrixColor("gui/museum/museum_fountainsmall.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_gear = ConditionSwitch(
    "museum_gear_unlocked == True", "gui/museum/museum_gear.png",
    "True", im.MatrixColor("gui/museum/museum_gear.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_guardtower = ConditionSwitch(
    "museum_guardtower_unlocked == True", "gui/museum/museum_guardtower.png",
    "True", im.MatrixColor("gui/museum/museum_guardtower.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_hangar = ConditionSwitch(
    "museum_hangar_unlocked == True", "gui/museum/museum_hangar.png",
    "True", im.MatrixColor("gui/museum/museum_hangar.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_hedgehog = ConditionSwitch(
    "museum_hedgehog_unlocked == True", "gui/museum/museum_hedgehog.png",
    "True", im.MatrixColor("gui/museum/museum_hedgehog.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_hut = ConditionSwitch(
    "museum_hut_unlocked == True", "gui/museum/museum_hut.png",
    "True", im.MatrixColor("gui/museum/museum_hut.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_iceberg = ConditionSwitch(
    "museum_iceberg_unlocked == True", "gui/museum/museum_iceberg.png",
    "True", im.MatrixColor("gui/museum/museum_iceberg.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_kremlin = ConditionSwitch(
    "museum_kremlin_unlocked == True", "gui/museum/museum_kremlin.png",
    "True", im.MatrixColor("gui/museum/museum_kremlin.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_lamppost = ConditionSwitch(
    "museum_lamppost_unlocked == True", "gui/museum/museum_lamppost.png",
    "True", im.MatrixColor("gui/museum/museum_lamppost.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_machinegunnest = ConditionSwitch(
    "museum_machinegunnest_unlocked == True", "gui/museum/museum_machinegunnest.png",
    "True", im.MatrixColor("gui/museum/museum_machinegunnest.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_mansion = ConditionSwitch(
    "museum_mansion_unlocked == True", "gui/museum/museum_mansion.png",
    "True", im.MatrixColor("gui/museum/museum_mansion.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_market = ConditionSwitch(
    "museum_market_unlocked == True", "gui/museum/museum_market.png",
    "True", im.MatrixColor("gui/museum/museum_market.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_mosque = ConditionSwitch(
    "museum_mosque_unlocked == True", "gui/museum/museum_mosque.png",
    "True", im.MatrixColor("gui/museum/museum_mosque.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_palace = ConditionSwitch(
    "museum_palace_unlocked == True", "gui/museum/museum_palace.png",
    "True", im.MatrixColor("gui/museum/museum_palace.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_palmtree = ConditionSwitch(
    "museum_palmtree_unlocked == True", "gui/museum/museum_palmtree.png",
    "True", im.MatrixColor("gui/museum/museum_palmtree.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_pillbox = ConditionSwitch(
    "museum_pillbox_unlocked == True", "gui/museum/museum_pillbox.png",
    "True", im.MatrixColor("gui/museum/museum_pillbox.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_postbox = ConditionSwitch(
    "museum_postbox_unlocked == True", "gui/museum/museum_postbox.png",
    "True", im.MatrixColor("gui/museum/museum_postbox.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_pyramid = ConditionSwitch(
    "museum_pyramid_unlocked == True", "gui/museum/museum_pyramid.png",
    "True", im.MatrixColor("gui/museum/museum_pyramid.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_radiotower = ConditionSwitch(
    "museum_radiotower_unlocked == True", "gui/museum/museum_radiotower.png",
    "True", im.MatrixColor("gui/museum/museum_radiotower.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_sandbag = ConditionSwitch(
    "museum_sandbag_unlocked == True", "gui/museum/museum_sandbag.png",
    "True", im.MatrixColor("gui/museum/museum_sandbag.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_shrub = ConditionSwitch(
    "museum_shrub_unlocked == True", "gui/museum/museum_shrub.png",
    "True", im.MatrixColor("gui/museum/museum_shrub.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_snowyrocks = ConditionSwitch(
    "museum_snowyrocks_unlocked == True", "gui/museum/museum_snowyrocks.png",
    "True", im.MatrixColor("gui/museum/museum_snowyrocks.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_stalagmite = ConditionSwitch(
    "museum_stalagmite_unlocked == True", "gui/museum/museum_stalagmite.png",
    "True", im.MatrixColor("gui/museum/museum_stalagmite.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_statueeagle = ConditionSwitch(
    "museum_statueeagle_unlocked == True", "gui/museum/museum_statueeagle.png",
    "True", im.MatrixColor("gui/museum/museum_statueeagle.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_statuekaiser = ConditionSwitch(
    "museum_statuekaiser_unlocked == True", "gui/museum/museum_statuekaiser.png",
    "True", im.MatrixColor("gui/museum/museum_statuekaiser.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_statueman = ConditionSwitch(
    "museum_statueman_unlocked == True", "gui/museum/museum_statueman.png",
    "True", im.MatrixColor("gui/museum/museum_statueman.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_statuewoman = ConditionSwitch(
    "museum_statuewoman_unlocked == True", "gui/museum/museum_statuewoman.png",
    "True", im.MatrixColor("gui/museum/museum_statuewoman.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_sweat = ConditionSwitch(
    "museum_sweat_unlocked == True", "gui/museum/museum_sweat.png",
    "True", im.MatrixColor("gui/museum/museum_sweat.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_table = ConditionSwitch(
    "museum_table_unlocked == True", "gui/museum/museum_table.png",
    "True", im.MatrixColor("gui/museum/museum_table.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_temple = ConditionSwitch(
    "museum_temple_unlocked == True", "gui/museum/museum_temple.png",
    "True", im.MatrixColor("gui/museum/museum_temple.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_tent = ConditionSwitch(
    "museum_tent_unlocked == True", "gui/museum/museum_tent.png",
    "True", im.MatrixColor("gui/museum/museum_tent.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_terrace = ConditionSwitch(
    "museum_terrace_unlocked == True", "gui/museum/museum_terrace.png",
    "True", im.MatrixColor("gui/museum/museum_terrace.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_theater = ConditionSwitch(
    "museum_theater_unlocked == True", "gui/museum/museum_theater.png",
    "True", im.MatrixColor("gui/museum/museum_theater.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_train = ConditionSwitch(
    "museum_train_unlocked == True", "gui/museum/museum_train.png",
    "True", im.MatrixColor("gui/museum/museum_train.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_vases = ConditionSwitch(
    "museum_vases_unlocked == True", "gui/museum/museum_vases.png",
    "True", im.MatrixColor("gui/museum/museum_vases.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_wheat = ConditionSwitch(
    "museum_wheat_unlocked == True", "gui/museum/museum_wheat.png",
    "True", im.MatrixColor("gui/museum/museum_wheat.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_woodland = ConditionSwitch(
    "museum_woodland_unlocked == True", "gui/museum/museum_woodland.png",
    "True", im.MatrixColor("gui/museum/museum_woodland.png", im.matrix.colorize("#000", "#000") * im.matrix.opacity(0.5)))

image museum_levelb = LiveComposite(
    (1664, 1100),
    (0, 0), "gui/museum/museum_levelb.png",
    (738, 303), "museum_bollard",
    (720, 377), "museum_debris",
    (872, 237), "museum_flat",
    (1063, 416), "museum_hangar",
    (248, 155), "museum_factory",
    (581, 479), "museum_crate",
    (477, 578), "museum_hedgehog",
    (718, 533), "museum_bunker",
    (575, 678), "museum_dragonteeth",
    (727, 752), "museum_bones",
    (847, 801), "museum_sweat",
    (956, 667), "museum_machinegunnest")

image museum_level1 = LiveComposite(
    (1664, 1100),
    (0, 0), "gui/museum/museum_level1.png",
    (596, 214), "museum_brandenburggate",
    (959, 421), "museum_beerhall",
    (477, 470), "museum_statuekaiser",
    (613, 594), "museum_statueman",
    (733, 648), "museum_statuewoman",
    (850, 677), "museum_statueeagle")

image museum_level2 = LiveComposite(
    (1664, 1100),
    (0, 0), "gui/museum/museum_level2.png",
    (357, 17), "museum_farmhousesnow",
    (980, 242), "museum_church",
    (1184, 446), "museum_cottage",
    (780, 527), "museum_tent",
    (993, 653), "museum_iceberg",
    (273, 384), "museum_forest",
    (424, 590), "museum_snowyrocks",
    (637, 669), "museum_sandbag",
    (820, 647), "museum_guardtower")

image museum_level3 = LiveComposite(
    (1664, 1100),
    (0, 0), "gui/museum/museum_level3.png",
    (625, 172), "museum_theater",
    (870, 236), "museum_eiffel",
    (1066, 415), "museum_arch",
    (497, 518), "museum_train",
    (1055, 765), "museum_shrub",
    (1124, 854), "museum_bush",
    (228, 491), "museum_cafe",
    (500, 726), "museum_pillbox",
    (677, 663), "museum_palace")

image museum_level4 = LiveComposite(
    (1664, 1100),
    (0, 0), "gui/museum/museum_level4.png",
    (517, 195), "museum_market",
    (848, 308), "museum_desertruins",
    (1028, 424), "museum_pyramid",
    (244, 79), "museum_deserttower",
    (432, 434), "museum_deserthouse",
    (590, 673), "museum_desertrocks",
    (678, 609), "museum_palmtree",
    (764, 524), "museum_mosque")

image museum_level5 = LiveComposite(
    (1664, 1100),
    (0, 0), "gui/museum/museum_level5.png",
    (640, 86), "museum_bigben",
    (941, 417), "museum_temple",
    (1127, 413), "museum_mansion",
    (583, 415), "museum_lamppost",
    (1116, 694), "museum_postbox",
    (1117, 834), "museum_table",
    (233, 401), "museum_brickhouse",
    (457, 622), "museum_bank",
    (692, 646), "museum_fountainbig")

image museum_level6 = LiveComposite(
    (1664, 1100),
    (0, 0), "gui/museum/museum_level6.png",
    (552, 190), "museum_hut",
    (679, 6), "museum_kremlin",
    (1123, 154), "museum_radiotower",
    (246, 201), "museum_terrace",
    (586, 465), "museum_stalagmite",
    (547, 588), "museum_gear",
    (1034, 685), "museum_wheat",
    (740, 669), "museum_barmaleyfountain")

image museum_level7 = LiveComposite(
    (1664, 1100),
    (0, 0), "gui/museum/museum_level7.png",
    (514, 244), "museum_zhinatemple",
    (820, 455), "museum_zhinahouse",
    (553, 607), "museum_woodenbench",
    (775, 720), "museum_zhinathrone",
    (871, 766), "museum_vases",
    (312, 604), "museum_fountainsmall",
    (570, 785), "museum_woodland")

########################################################
# Tactical Map ############################################
########################################################
image map_tactical1 = "back/map/map_tactical1.png"
image map_tactical2 = "back/map/map_tactical2.png"
image map_tactical3 = "back/map/map_tactical3.png"
image map_tactical4 = "back/map/map_tactical4.png"
image map_tactical5 = "back/map/map_tactical5.png"
image map_tactical6 = "back/map/map_tactical6.png"
image map_tactical7 = "back/map/map_tactical7.png"
image map_tactical8 = "back/map/map_tactical8.png"
image map_tactical9 = "back/map/map_tactical9.png"
image map_tactical10 = "back/map/map_tactical10.png"
image map_tactical11 = "back/map/map_tactical11.png"
image map_tactical12 = "back/map/map_tactical12.png"
image map_tactical13 = "back/map/map_tactical13.png"
image map_tactical14 = "back/map/map_tactical14.png"
image map_tactical15 = "back/map/map_tactical15.png"
image map_tactical16 = "back/map/map_tactical16.png"
image map_tactical17 = "back/map/map_tactical17.png"
image map_tactical18 = "back/map/map_tactical18.png"
image map_tactical19 = "back/map/map_tactical19.png"
image map_tactical20 = "back/map/map_tactical20.png"
image map_tactical21 = "back/map/map_tactical21.png"
image map_tactical22 = "back/map/map_tactical22.png"

image map_germania = "back/map/map_germania.png"
image map_europa = "back/map/map_europa.png"
image map_europa2 = "back/map/map_europa2.png"
image map_rumanum = "back/map/map_rumanum.png"
image map_zipangu = "back/map/map_zipangu.png"
image map_zipangunorth = "back/map/map_zipangunorth.png"
image map_zipangusouth = "back/map/map_zipangusouth.png"

########################################################
# Map #################################################
########################################################
image easternmap = "back/map/map_eastern.jpg"
image easternmap_small = "back/map/easternmap.jpg"
image geomap1 = "back/map/map_geographic_summer.jpg"
image geomap2 = "back/map/map_geographic_winter.jpg"
image map1 = "back/map/map_political_1.jpg"
image map2 = "back/map/map_political_2.jpg"
image map3 = "back/map/map_political_3.jpg"
image map4 = "back/map/map_political_4.jpg"
image map5 = "back/map/map_political_5.jpg"
image map6 = "back/map/map_political_6.jpg"
image map7 = "back/map/map_political_7.jpg"
image map8 = "back/map/map_political_8.jpg"
image map9 = "back/map/map_political_9.jpg"
image map10 = "back/map/map_political_10.jpg"
image map11 = "back/map/map_political_11.jpg"
image map12 = "back/map/map_political_12.jpg"
image map13 = "back/map/map_political_13.jpg"
image map14 = "back/map/map_political_14.jpg"
image map15 = "back/map/map_political_15.jpg"
image map16 = "back/map/map_political_16.jpg"
image map17 = "back/map/map_political_17.jpg"
image map18 = "back/map/map_political_18.jpg"

