# TODO: Translation updated at 2022-06-07 01:45

init python:
  config.language = "Japanese"
  
translate Japanese python:
  gui.default_font = "tl/Japanese/font/MOBO.otf"
  gui.text_font = "tl/Japanese/font/MOBO.otf"
  gui.name_font = "tl/Japanese/font/MOBO.otf"
  gui.interface_font = "tl/Japanese/font/MOBO.otf"
  gui.button_text_font = gui.interface_font
  gui.choice_button_text_font = gui.default_font
  
translate Japanese style edited:
  font "tl/Japanese/font/MOBO.otf"
  
translate Japanese style default:
  font "tl/Japanese/font/MOBO.otf"
  
translate Japanese style cp_text:
  font "tl/Japanese/font/MOBO.otf"
  
translate Japanese style sovspeak:
  font "tl/Japanese/font/MOBO.otf"

  #font "tl/Japanese/font/MOBO.otf"
  #font "tl/Japanese/font/07LogoTypeGothic7.ttf"
  
style ruby_style is default:
  size 14
  yoffset -25
  
translate Japanese init:
  #default level_easy_tooltip_jp = "{color=#F35F5F}コマンドポイント (CP){/color}が増加した状態で始まり、戦闘後に受け取る{color=#F35F5F}CP{/color}が増加します。いつでも{color=#F35F5F}バトルのスキップ{/color}が可能です。"
  #default level_normal_tooltip_jp = "{color=#F35F5F}コマンドポイント (CP){/color}の増減は無く、一度戦闘に負けると{color=#F35F5F}バトルのスキップ{/color}が有効になります。"
  #default level_hard_tooltip_jp = "{color=#F35F5F}コマンドポイント (CP){/color}が少ない状態で始まり、戦闘後に受け取る{color=#F35F5F}CP{/color}も減少します。{color=#F35F5F}バトルのスキップ{/color}は常に無効化されます。"
  define level_easy_tooltip = "{color=#F35F5F}コマンドポイント (CP){/color}が増加した状態で始まり、戦闘後に受け取る{color=#F35F5F}CP{/color}が増加します。いつでも{color=#F35F5F}バトルのスキップ{/color}が可能です。"
  define level_normal_tooltip = "{color=#F35F5F}コマンドポイント (CP){/color}の増減は無く、一度戦闘に負けると{color=#F35F5F}バトルのスキップ{/color}が有効になります。"
  define level_hard_tooltip = "{color=#F35F5F}コマンドポイント (CP){/color}が少ない状態で始まり、戦闘後に受け取る{color=#F35F5F}CP{/color}も減少します。{color=#F35F5F}バトルのスキップ{/color}は常に無効化されます。"
  default TextBacklog_jp = "ログ"
  define config.window_title = u"私の小さな独裁者"

translate Japanese strings:

    #old "Shingunto Blade"
    #new "新・軍刀ブレード"

    #old "A Zipanguese military sword."
    #new "ジパングの軍刀です。"
    
    old "[post_disclaimer_text]"
    new "[post_disclaimer_text!t]"

    old "Our story takes place in a world similar to our own yet vastly different.\n\nA world in which the figures of history are cute anime girls . . ."
    new "この物語は、私たちの世界と似ているようでいて、大きく異なる世界が舞台……。\n\nそう、歴史上の人物がかわいいアニメの女の子になった世界です！"

    old "[disclaimer_text]"
    new "[disclaimer_text!t]"

    old "{i}My Little Dictator{/i} is the intellectual and commercial property of {i}WarGirl Games{/i}. The fictional story, setting and characters contained within are the intellectual property of the developers.\n\nAll characters, names, businesses, places, products, events and incidents appearing in this work are fictional. Any resemblance to any real persons, living or dead, is purely coincidental. No identification with actual persons (living or deceased), names, businesses, places, products, events or incidents is intended or should be inferred. This game is a fictional work of parody, featuring caricature as well as satire, and contains suggestive content. This game was designed and developed by a global team of creatives of various beliefs, backgrounds and ethnicities.\n\nThe makers of this game do not condone, endorse or encourage engaging in any conduct depicted in this game. This game contains references to warfare and war crimes, violence, genocide, jingoism, imperialism, fascism, communism, dictatorship, racial and ethnic stereotyping, intolerance, propaganda, suicide, alcohol, tobacco, nudity and themes of a sexual nature. As such, player discretion is strongly advised."
    new "{i}My Little Dictator (私の小さな独裁者){/i}は、{i}WarGirl Games{/i}の知的財産および商業的財産です。\n\n本作品に登場する人物、名前、企業、場所、製品、イベント、事件などはすべてフィクションであり、実在の人物（生死を問わず）との類似性は、あくまでも偶然の産物です。実在の人物（生死を問わず）、名称、事業内容、場所、製品、出来事、事件等との同一性を意図するものではなく、またそのように推測されるものでもありません。このゲームは、風刺や風刺を含むパロディの架空の作品であり、示唆的な内容を含んでいます。このゲームは、様々な信条、背景、民族を持つクリエーターからなるグローバルチームによってデザイン、開発されました。このゲームには、戦争や戦争犯罪、暴力、大量虐殺、ジンゴイズム、帝国主義、ファシズム、共産主義、独裁主義、国民性、人種的不寛容、プロパガンダ、自殺、アルコール、タバコ、ヌード、性的なテーマが含まれます。そのため、プレイヤーの皆様には慎重な判断をお願いいたします。"

    old "Are you sure you want to return to the main menu?"
    new "タイトルに戻りますか？"

    #"Begin with increased {color=#F35F5F}Command Points (CP){/color} and receive more {color=#F35F5F}CP{/color} after battles as well. {color=#F35F5F}Skip Battle{/color} is always enabled."
    #"{color=#F35F5F}コマンドポイント (CP){/color}が増加した状態で始まり、戦闘後に受け取る{color=#F35F5F}CP{/color}が増加します。いつでも{color=#F35F5F}バトルのスキップ{/color}が可能です。"

    #"Begin with average {color=#F35F5F}Command Points (CP){/color} and receive regular {color=#F35F5F}CP{/color} after battles. {color=#F35F5F}Skip Battle{/color} is enabled after losing a battle once."
    #"{color=#F35F5Fコマンドポイント (CP){/color}の増減は無く、一度戦闘に負けると{color=#F35F5F}バトルのスキップ{/color}が有効になります。"

    #"Begin with fewer {color=#F35F5F}Command Points (CP){/color} and receive less {color=#F35F5F}CP{/color} after battles as well. {color=#F35F5F}Skip Battle{/color} is always disabled."
    #"{color=#F35F5F}コマンドポイント (CP){/color}が少ない状態で始まり、戦闘後に受け取る{color=#F35F5F}CP{/color}も減少します。{color=#F35F5F}バトルのスキップ{/color}は常に無効化されます。"

    old "Text Backlog"
    new "ログ"

    old "Auto-Forward"
    new "オート"

    old "Skip text"
    new "スキップ"

    old "silly SFX"
    new "効果音(爆発など)"

    old "Monty44"
    new "モンティ"

    # game/screens.rpy:219
    old "New Game"
    new "はじめから"

    # game/screens.rpy:220
    old "Load Data"
    new "つづきから"

    # game/screens.rpy:221
    old "Options"
    new "設定"

    # game/screens.rpy:224
    old "Bonus"
    new "おまけ"

    # game/screens.rpy:225
    old "Credits"
    new "クレジット"

    # game/screens.rpy:226
    old "Quit Game"
    new "終了"

    # game/screens.rpy:253
    old "Return"
    new "戻る"

    # game/screens.rpy:255
    old "Save Data"
    new "セーブ"

    # game/screens.rpy:259
    old "Main Menu"
    new "タイトルに戻る"

    # game/screens.rpy:261
    old "Gallery"
    new "CG鑑賞"

    # game/screens.rpy:262
    old "Jukebox"
    new "BGM鑑賞"

    # game/screens.rpy:276
    old "Q"
    new "Q"

    # game/screens.rpy:278
    old "A"
    new "A"

    # game/screens.rpy:302
    old "Empty Slot"
    new "空きスロット"

    # game/screens.rpy:386
    old "Fullscreen"
    new "フルスクリーン"

    # game/screens.rpy:387
    old "Large Window"
    new "ウィンドウ(大)"

    # game/screens.rpy:389
    old "Medium Window"
    new "ウィンドウ(中)"

    # game/screens.rpy:390
    old "Small Window"
    new "ウィンドウ(小)"

    # game/screens.rpy:404
    old "Skip Text"
    new "テキストのスキップ"

    # game/screens.rpy:413
    old "Skip Seen Text"
    new "既読のみ"

    # game/screens.rpy:414
    old "Skip All Text"
    new "全てスキップ"

    # game/screens.rpy:424
    old "After Choices"
    new "選択肢の後"

    # game/screens.rpy:433
    old "Stop Skipping"
    new "スキップを止める"

    # game/screens.rpy:434
    old "Keep Skipping"
    new "スキップを続ける"

    # game/screens.rpy:444
    old "Text Speed"
    new "文字速度"

    # game/screens.rpy:467
    old "Auto-Forward Time"
    new "オート速度"

    # game/screens.rpy:493
    old "Music Volume"
    new "ミュージック"

    # game/screens.rpy:518
    old "SFX Volume"
    new "効果音"

    # game/screens.rpy:549
    old "Voice Volume"
    new "ボイス"

    # game/screens.rpy:669
    old "{image=gui/undo_symbol.png}"
    new "{image=gui/undo_symbol.png}"

    old "Rommel"
    new "ロンメル"

    old "Sovian General"
    new "ソヴィア軍将校"

    old "Furry Girl"
    new "ケモノの少女"

    old "Ewalda"
    new "エワルダ"

    old "Eisenhoo"
    new "アイゼンフー"
    #ドワイト・D・アイゼンハワー

    old "Pattonko"
    new "パットンコ"

    old "MacArtha"
    new "マッカーサ"

    old "Leopold"
    new "レオポルド"

    old "Blondy"
    new "ブロンディ"

    old "Hoth"
    new "ホス"

    old "Wild Bear"
    new "野生のクマ"

    old "Revolutionary"
    new "革命家"

    old "Radish Ali"
    new "ラディッシュ・アリ"

    old "Ztauffenborg"
    new "シュタウフェンボルグ"
    #シュタウフェンベルク

    old "Yamamoto"
    new "山本"

    old "Zipangu Admiral"
    new "ジパング海軍提督"

    old "Metaxas"
    new "メタクサス"
    #イオアニス・メタクサス

    old "Wounded Soldier"
    new "負傷兵"

    old "Huntziger"
    new "アンツィジェール"
    #シャルル・アンツィジェール

    old "Hoppyner"
    new "ホピナー"
    #エーリヒ・ヘプナー?

    old "Petain"
    new "ペタン"
    #ピエール・ビヨット
    #フィリップ・ペタン

    old "Wavell"
    new "ウェーヴェル"
    #アーチボルド・ウェーヴェル

    old "Gariboldi"
    new "ガリボルディ"
    #イータロ・ガリボルディ

    old "Vinkelman"
    new "ヴィンケルマン"
    #ヘンリー・ヴィンケルマン

    old "Old General"
    new "老将軍"

    old "Keitel"
    new "カイテル"
    #ヴィルヘルム・カイテル

    old "Quisling"
    new "クヴィスリング"
    #ヴィドクン・クヴィスリング

    old "Older Man"
    new "年配の男性"

    old "Kanari"
    new "カナリ"

    old "Ooster"
    new "オスター"

    old "Beck"
    new "ベック"
    #ルートヴィヒ・ベック

    old "Mysterious General"
    new "謎の将軍"

    old "Evan Braun"
    new "エヴァン・ブラウン"
    #エヴァ・ブラウン

    old "Goosetapo Officer"
    new "グーセタポ士官"
    #Gestapo ゲシュタポ

    old "Handsome Stranger"
    new "見知らぬ美少年"

    old "Rude Ostralasian"
    new "荒くれ者のオストララシア人"

    #old "Rich Man"
    #new "富豪"

    old "Franzo Soldier"
    new "フランツォ兵士"

    old "Franco"
    new "フランコ"
    #フランシスコ・フランコ

    old "Pilot"
    new "パイロット"

    old "Major"
    new "空将"

    old "Jorge VI"
    new "ジョルジュ6世"
    #George VI

    old "Zorge"
    new "ゾルゲ"
    #リヒャルト・ゾルゲ

    old "Borkind"
    new "ボーキンド"

    old "Peasant Girl"
    new "農民の少女"

    old "Valkenhorst"
    new "ヴァルケンホルスト"
    #ニコラウス・フォン・ファルケンホルスト

    old "Zhina Soldier"
    new "ジャイナ兵"

    old "Young Secretary"
    new "若手書記"

    old "Nygaaaaardsvool"
    new "ニャガアアアアアルドバル"

    old "Hess"
    new "ヘス"
    #ルドルフ・ヘス

    old "Speaker"
    new "演説者"

    old "Hubala"
    new "フバル"
    #ヘンリク・ドブルザンスキー Henryk Dobrzański

    old "Linge"
    new "リンゲ"

    old "Luge"
    new "リュージュ"

    old "Ironsides"
    new "クロムウェル"

    old "Norda Soldier"
    new "ノルダ兵"

    old "Lammers"
    new "ラマー"

    old "Teleki"
    new "テレキ"
    #テレキ・パール

    old "Christian X"
    new "キリスト教徒"

    old "Prior"
    new "修道院長"

    old "Cshima"
    new "クシマ"

    old "Chambers"
    new "議会"

    old "Halifax"
    new "ハリファックス"
    #元インドの総督、エドワード・ウッド?

    old "Polix Soldier"
    new "ポリックス兵"
    #ポーランド兵

    old "Sikorskia"
    new "シコルスキア"
    #ヴワディスワフ・シコルスキ

    old "Gort"
    new "ゴート"
    #ジョン・ヴェレカー (第6代ゴート子爵)

    old "Dau"
    new "ダウ"

    old "Germanian Admiral"
    new "ゲルマニア海軍提督"

    old "Weygand"
    new "ウェイガン"
    #マキシム・ウェイガン

    old "Kirponos"
    new "キルポノス"
    #ミハイル・キルポノス

    old "Pavlov"
    new "パヴロフ"
    #ドミトリー・パヴロフ

    old "Dimashenka"
    new "ディマシェンカ"
    #Masha Bruskina マーシャ・ブルスキナ？

    old "Leynaud"
    new "レノー"
    #ポール・レノー

    old "Billotte"
    new "ビヨット"
    #ピエール・ビヨット

    old "Talatier"
    new "タラティエ"

    old "Dania Soldier"
    new "ダニア兵"
    #デンマーク兵？

    old "Yamato"
    new "ヤマト"

    old "Monty"
    new "モンティ"

    old "Hitora"
    new "ヒトラ"

    old "Antoness"
    new "アントネス"
    #アントン・ドストラー ドイツ
    #アントン・ミュッセルト オランダ

    old "Redhead Girl"
    new "赤毛の少女"

    old "Kalinesgu"
    new "カリネスグ"

    old "Finbardish Soldier"
    new "フィンバディッシュ兵"
    #フィンランド兵

    old "King Garol"
    new "ガロル2世"
    #カロル2世 (ルーマニア王)

    old "Rinni"
    new "リニー"

    old "Mussorinni"
    new "ムッソリニー"

    old "Starin"
    new "スタリン"

    old "Reine"
    new "レーヌ"

    old "Leclercia"
    new "レクレルシア"

    old "Goring"
    new "ジューキフ"

    old "Joebbels"
    new "ヨッベルス"

    old "Dunitz"
    new "デュニッツ"

    old "Nyan Katshex"
    new "Nyan Katshex"
    #猫沢東

    old "Roosevelt"
    new "ルーズベルト"

    old "Churchill"
    new "チャーチル"

    old "Cyrano"
    new "シラノ"

    old "Cute Girl"
    new "キュートガール"

    old "Hirahita"
    new "ヒラヒタ"

    old "Prince Paulie"
    new "ポーリー王子"

    old "Mannerheim"
    new "マンネルヘイム"
    #カール・グスタフ・エミール・マンネルヘイム

    old "Dresckow"
    new "ドレスコウ"
    #ヘニング・フォン・トレスコウ Tresckow ヒトラー暗殺計画の首謀者の一人。

    old "Mysterious Man"
    new "謎の男"

    old "Tito"
    new "チトー"
    #ヨシップ・ブロズ・チトー

    old "Scrappy Girl"
    new "喧嘩腰な少女"

    old "Wilhelmina"
    new "ヴィルヘルミナ"

    old "Badoglio"
    new "バドリオ"
    #ピエトロ・バドリオ

    old "Battenia"
    new "バテニア"
    #ダドリー・パウンド

    old "Stuffy"
    new "スタフィー"
    #Hugh Dowding ヒュー・ダウディング

    old "Manstein"
    new "マンシュタイン"
    #エーリッヒ・フォン・マンシュタイン

    old "Pretty Girl"
    new "可愛らしい少女"

    old "Smigly"
    new "シミグウィ"
    #エドヴァルト・リッツ＝シミグウィ

    old "Horthy"
    new "ホルティ"
    #ホルティ・ミクローシュ

    old "Guderian"
    new "グデーリアン"
    #ハインツ・グデーリアン

    old "Gamelin"
    new "ガムラン"
    #モーリス・ガムラン

    old "Molotov"
    new "モロトフ"
    #ヴャチェスラフ・モロトフ

    old "Graziani"
    new "グラツィアーニ"
    #ロドルフォ・グラツィアーニ

    old "Vitalian Officer"
    new "ヴィタリア軍元帥"

    old "Cavallero"
    new "カヴァッレーロ"
    #ウーゴ・カヴァッレーロ

    old "Messe"
    new "メッセ"
    #ジョヴァンニ・メッセ

    old "Vasile"
    new "ヴァシレ"
    #アレクサンドル・ヴァシレフスキー

    old "Maletti"
    new "マレッティ部隊"

    old "Vitalia Soldier"
    new "ヴィタリア兵"

    old "Brookie"
    new "ブルッキー"
    #アラン・ブルック

    old "Jumbo"
    new "ジャンボ"

    old "Haakon"
    new "ホーコン7世"
    #Haakon VII of Norway

    old "Mihaila"
    new "ミハイラ"

    old "Nega-Hitora"
    new "闇のヒトラ"

    old "Hitora?"
    new "ヒトラ?"

    old "Nurse"
    new "看護婦"

    old "Lieutenant"
    new "大尉"

    old "Shopkeep"
    new "店主"

    old "Doctor"
    new "医者"

    old "Politician"
    new "政治家"

    old "Short Girl"
    new "幼い少女"

    old "Voice"
    new "謎の声"

    old "Agent"
    new "諜報員"

    old "Attendant"
    new "従者"

    old "Stachie"
    new "スタチュー"

    old "Trainer"
    new "訓練指導者"

    old "Sonny"
    new "サニー"

    old "Engineer"
    new "工兵"

    old "Himmora"
    new "ヒモラー"
    #ハインリヒ・ヒムラー

    old "Crowd"
    new "群衆"

    old "Everyone"
    new "みんな"

    old "Daughter"
    new "娘"

    old "Freyaborg"
    new "亡霊"

    #old "Freyaborg"
    #new "フェインベルグ"

    old "GI Soldier"
    new "アメリカ兵"

    old "MIB Agent"
    new "MIB捜査官"

    old "King"
    new "国王"

    old "Dietling"
    new "ディートリング"

    old "Takeshi"
    new "タケシ"

    old "Youth"
    new "少年"

    old "Official"
    new "護衛官"

    old "Vleischer"
    new "フライシャー"

    old "Maid"
    new "侍女"

    old "Servant"
    new "使用人"

    old "Brother"
    new "兄"

    old "Fat Man"
    new "太った男"

    old "Polix Resister"
    new "ポリックスのレジスタンス"

    old "Girl"
    new "少女"

    old "Strange Girl"
    new "不思議な少女"

    old "Beauty"
    new "麗人"

    old "Old Man"
    new "老人"

    old "Old Woman"
    new "老婦"

    old "Man"
    new "男性"

    old "Gentleman"
    new "紳士"

    old "Woman"
    new "女性"

    old "Driver"
    new "運転手"

    old "Germanian General"
    new "ゲルマニア軍将官"

    old "Kaupisch"
    new "カウピッシュ"
    #レオンハルト・カウピッシュ

    old "Listte"
    new "リステ"

    old "Britannian General"
    new "ブリタニア軍将官"

    old "Bloody Vasey"
    new "血まみれのヴァシー"
    #ジョージ・アラン・ヴァシー George Alan Vasey

    old "Iraji General"
    new "イラジ軍将官"

    #old "Sovian General"
    #new "ソヴィア軍将官"

    old "Klima"
    new "クリーマ"

    old "ZZ Officer"
    new "ZZ 将官"

    old "ZZ Soldier"
    new "ZZ 隊員"

    old "Fake Polix Soldier"
    new "偽物のポリックス兵"

    old "Zchaal"
    new "ジャール"
    #フェルディナント・シャール

    old "Junior"
    new "新参兵"

    old "Soldier"
    new "兵士"

    old "Zipangu Soldier"
    new "ジパング兵"

    old "Zipanguese Soldier"
    new "ジパング兵士"

    old "Medic"
    new "衛生兵"

    old "Axle Soldier"
    new "枢軸兵"

    old "Germanian Soldier"
    new "ゲルマニア兵"

    old "Germanian Paratrooper"
    new "ゲルマニア空挺部隊"

    old "Alliance Soldier"
    new "連合兵"

    old "Sovian Soldier"
    new "ソヴィア兵"


screen quick_menu():
    hbox:
        style_group "quick"
        grid 5 2:
            imagebutton auto "gui/quick_backlog_%s.png" action ShowMenu('text_history') at quick_eff hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True tooltip "ログ"
            imagebutton auto "gui/quick_auto_%s.png" action Preference("auto-forward", "toggle") at quick_eff hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True tooltip "オート"
            imagebutton auto "gui/quick_skip_%s.png" action Skip() at quick_eff hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True tooltip "スキップ"
            imagebutton auto "gui/quick_config_%s.png" action ShowMenu('preferences') at quick_eff hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True tooltip "設定"
            imagebutton auto "gui/quick_mainmenu_%s.png" action MainMenu() at quick_eff hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True tooltip "タイトルに戻る"
            imagebutton auto "gui/quick_qsave_%s.png" action QuickSave() at quick_eff hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True tooltip "クイックセーブ"
            imagebutton auto "gui/quick_save_%s.png" action ShowMenu('save') at quick_eff hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True tooltip "セーブ"
            imagebutton auto "gui/quick_qload_%s.png" action QuickLoad() at quick_eff hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True tooltip "クイックロード"
            imagebutton auto "gui/quick_load_%s.png" action ShowMenu('load') at quick_eff hover_sound "se/hover.ogg" activate_sound "se/click.ogg" focus_mask True tooltip "ロード"
            imagebutton auto "gui/quick_codex_%s.png" action [
                SensitiveIf(codex_unlocked), 
                ShowMenu("codex"), 
                SetVariable("codex_navchoice", "codex1"), 
                SetVariable("profile_name", profile_yamato_name), 
                SetVariable("profile_flag", profile_yamato_flag), 
                SetVariable("profile_birthplace", profile_yamato_birthplace), 
                SetVariable("profile_description", profile_yamato_description), 
                SetVariable("profile_type", profile_yamato_type), 
                SetVariable("profile_birthday", profile_yamato_birthday), 
                SetVariable("profile_zodiac", profile_yamato_zodiac), 
                SetVariable("profile_role", profile_yamato_role), 
                SetVariable("profile_height", profile_yamato_height), 
                SetVariable("profile_blood", profile_yamato_blood), 
                SetVariable("profile_drink", profile_yamato_drink), 
                SetVariable("profile_weight", profile_yamato_weight), 
                SetVariable("profile_food", profile_yamato_food), 
                SetVariable("profile_sprite", profile_yamato_sprite)
            ] at quick_eff hover_sound "se/hover.ogg" activate_sound "se/info.ogg" focus_mask True tooltip "Codex"



    $ tooltip = GetTooltip()

    if tooltip:
        frame:
            style_group "tooltip2_box"
            has vbox:
                xalign 0.5
                yalign 0.5
            text "[tooltip]"

screen campaign_selection():
    tag menu
    add "campaignselection_back"
    vbox:
        xalign 0.177
        yalign 0.59
        viewport:
            scrollbars "vertical"
            xmaximum 820
            xminimum 820
            ymaximum 670
            yminimum 670
            yalign 0.5
            side_yalign .5
            side_ymaximum 600
            side_spacing 0
            draggable True
            mousewheel True
            arrowkeys True
            has vbox:
                xalign 0.5
                yalign 0.5
            add "gui/campaign_main_bar.png"
            frame:
                background None
                xsize 780
                xpadding 20
                ypadding 16
                xalign 0.5
                yalign 0.5
                #text "The main story, detailing the exploits of Commander Yamato Yamamoto as he battles his way across Europa.":
                text "メインストーリー。ヨーロパ大陸を舞台に戦う山本ヤマトの活躍を描く。":
                    size 20
                    text_align 0.5
            if not conquest_campaign_completed:
                imagebutton idle "gui/campaign_conquest.png" insensitive "gui/campaign_insensitive.png" action [Show("level_selection")] at campaign_eff hover_sound "se/hover.ogg" activate_sound "se/equip.ogg" hovered [Show("campaign_hitora_rinni"), Hide("campaign_yamato")] unhovered [Hide("campaign_hitora_rinni"), Show("campaign_yamato")]
            else:
                add "campaign_conquest_complete"
            null height 5
            if not resistance_campaign_completed:
                imagebutton idle "gui/campaign_resistance.png" insensitive "gui/campaign_insensitive.png" action [SensitiveIf(resistance_campaign_unlocked), SetVariable("current_campaign", "campaign_resistance"), Jump("campaign_resistance")] at campaign_eff hover_sound "se/hover.ogg" activate_sound "se/fightui.ogg" hovered [Show("campaign_cyrano_churchill"), Hide("campaign_yamato")] unhovered [Hide("campaign_cyrano_churchill"), Show("campaign_yamato")]
            else:
                add "campaign_resistance_complete"
            null height 5
            imagebutton idle "gui/campaign_totalwar.png" insensitive "gui/campaign_insensitive.png" action [SensitiveIf(totalwar_campaign_unlocked), SetVariable("current_campaign", "campaign_totalwar"), Jump("campaign_totalwar")] at campaign_eff hover_sound "se/hover.ogg" activate_sound "se/fightui.ogg" hovered [Show("campaign_starin"), Hide("campaign_yamato")] unhovered [Hide("campaign_starin"), Show("campaign_yamato")]
            null height 10
            add "gui/campaign_side_bar.png"
            frame:
                background None
                xsize 780
                xpadding 20
                ypadding 16
                xalign 0.5
                yalign 0.5
                text "ゲームを進めることでアンロックされる追加のキャンペーン。ゲーム本編のプロットやゲームプレイをより充実させるためにプレイしてください。":
                    size 20
                    text_align 0.5
            if not evan_campaign_completed:
                imagebutton idle "gui/campaign_evan.png" insensitive "gui/campaign_insensitive.png" action [SensitiveIf(evan_campaign_unlocked), SetVariable("current_campaign", "campaign_evan"), Jump("campaign_evan")] at campaign_eff hover_sound "se/hover.ogg" activate_sound "se/fightui.ogg" hovered [Show("campaign_hitora_yamato"), Hide("campaign_yamato")] unhovered [Hide("campaign_hitora_yamato"), Show("campaign_yamato")]
            else:
                add "campaign_evan_complete"
            null height 5
            if not tito_campaign_completed:
                imagebutton idle "gui/campaign_tito.png" insensitive "gui/campaign_insensitive.png" action [SensitiveIf(tito_campaign_unlocked), SetVariable("current_campaign", "campaign_tito"), Jump("campaign_tito")] at campaign_eff hover_sound "se/hover.ogg" activate_sound "se/fightui.ogg" hovered [Show("campaign_churchill_rinni"), Hide("campaign_yamato")] unhovered [Hide("campaign_churchill_rinni"), Show("campaign_yamato")]
            else:
                add "campaign_tito_complete"
    vbox:
        xalign 0.543
        yalign 0.107
        imagebutton idle "yesno_no_small_idle" hover "yesno_no_small_hover" action MainMenu() focus_mask True hover_sound "se/hover.ogg" activate_sound "se/click.ogg" at mapicon_eff

    on "show" action Show("campaign_yamato")
    on "replace" action Show("campaign_yamato")
    on "hide" action [Hide("campaign_yamato"), Hide("campaign_starin"), Hide("campaign_hitora_rinni"), Hide("campaign_cyrano_churchill"), Hide("campaign_hitora_yamato"), Hide("campaign_churchill_rinni")]
    on "replaced" action [Hide("campaign_yamato"), Hide("campaign_starin"), Hide("campaign_hitora_rinni"), Hide("campaign_cyrano_churchill"), Hide("campaign_hitora_yamato"), Hide("campaign_churchill_rinni")]

screen choice(items):
    tag menu
    if voxpopmode_enabled:
        modal True
        add Solid("#000000") alpha 0.6
        add "gear2" xalign 0.685 yalign 0.785
        add "gear" xalign 0.315 yalign 0.785
        frame:
            style_group "voxpopouter"
            frame:
                style_group "voxpopmiddle"
                has vbox:
                    xalign 0.5
                    yalign 0.5
                    yfill False
                    xfill False
                vbox:
                    xalign 0.5
                    yalign 0.7
                    text "誰の話を聞こうか……"
                frame:
                    style_group "voxpopinner"
                    has vbox:
                        xalign 0.5
                        yalign 0.5
                    grid 3 3:
                        xfill False
                        style_group "vp"
                        for caption, action, chosen in items:
                            if action:
                                button:
                                    action action hover_sound "se/hover.ogg" activate_sound "se/click.ogg"
                                    text caption style "menu_choice"
                            else:
                                text caption style "menu_caption"
                        for j in range(0, 9 - len(items)):
                            null
            hbox:
                xalign 0.5
                yalign 1.019
                xfill False
                style_group "vp"
                textbutton "去る" action [Jump(voxpopjump), SensitiveIf(voxpopleave_sensitive)]
        use voxpop_overlay_frame

    else:
        add "gear2" xalign 0.685 yalign 0.71
        add "gear" xalign 0.315 yalign 0.71
        frame:
            background "gui/overlay_choice_back.png"
            xalign .5
            yalign .5
            xmaximum 1300
            xminimum 1300
            ymaximum 487
            yminimum 487
            yfill False
            xfill False
        vbox:
            style_group "menu"
            xalign .5
            if len(items) > 3:
                if len(items) > 4:
                    yalign .59
                else:
                    yalign .63
                grid 2 3:
                    xfill False
                    style_group "choicegrid"
                    for caption, action, chosen in items:
                        if action:
                            button:
                                action action hover_sound "se/hover.ogg" activate_sound "se/click.ogg"
                                text caption style "menu_choice"
                        else:
                            text caption style "menu_caption"
                    for j in range(0, 6 - len(items)):
                        null
            else:
                if len(items) > 2:
                    yalign .583
                else:
                    yalign .573
                for caption, action, chosen in items:
                    if action:
                        button:
                            action action hover_sound "se/hover.ogg" activate_sound "se/click.ogg"
                            style "menu_choice_button"
                            text caption style "menu_choice"
                    else:
                        text caption style "menu_caption"
        add "gui/overlay_frame_back2.png":
            xalign 0.5
            yalign 0.32
        add "gui/overlay_title_choice.png":
            xalign 0.5
            yalign 0.352

init -4 python:
    store.text_history_enabled = False
    config.locked = False 
    config.readback_buffer_length = 100 

    config.readback_disallowed_tags = ["size"] 
    config.readback_choice_prefix = ">> "   

    config.locked = True
    NameList = {
        "ロンメル": "side rommel normal",
        "ソヴィア軍将校": "side soviangeneral normal",
        "ケモノの少女": "side rommel normal",
        "エワルダ": im.Sepia("character/side/ewalda_th.png"),
        "アイゼンフー": im.Sepia("character/side/eisenhoo_th.png"),
        "パットンコ": im.Sepia("character/side/patton_th.png"),
        "マッカーサ": im.Sepia("character/side/macartha_th.png"),
        "レオポルド": im.Sepia("character/side/leopold_th.png"),
        "ブロンディ": im.Sepia("character/side/blondi_th.png"),
        "ホス": im.Sepia("character/side/hoth_th.png"),
        "野生のクマ": im.Sepia("character/side/hoth_th.png"),
        "革命": "side desertaxis normal",
        "ラディッシュ・アリ": "side desertman normal",
        "シュタウフェンボルグ": "side ztauffenborg normal",
        "山本": "side yamamoto determined",
        "ジパング海軍提督": "side yamamoto determined",
        "メタクサス": "side metaxas normal",
        "負傷兵": "side man normal",
        "アンツィジェール": "side franzo normal",
        "ホピナー": "side hoppyner normal",
        "ペタン": "side billotte normal",
        "ウェーヴェル": "side wavell normal",
        "ガリボルディ": "side gariboldi normal",
        "ヴィンケルマン": "side soldier normal",
        "老将軍": "side gariboldi normal",
        "カイテル": im.Sepia("character/side/keitel_th.png"),
        "クヴィスリング": "side quisling normal",
        "年配の男性": "side quisling normal",
        "カナリ": im.Sepia("character/side/kanari_th.png"),
        "オスター": im.Sepia("character/side/ooster_th.png"),
        "ベック": "side beck normal",
        "謎の将軍": "side beck normal",
        "エヴァン・ブラウン": "side evanbraun evil",
        "グーセタポ士官": "side gestapo normal",
        "見知らぬ美少年": "side evanbraun evil",
        "荒くれ者のオストララシア人": "side aussieman normal",
        "富豪": "side politician normal",
        "フランツォ兵士": "side franzo normal",
        "フランコ": "side basicgeneral happy",
        "パイロット": "side soldier normal",
        "空将": "side germaniangeneral normal",
        "ジョルジュ6世": "side politician2 normal",
        "ゾルゲ": "side politician2 normal",
        "ボーキンド": "side borkind normal",
        "農民の少女": "side woman normal",
        "ヴァルケンホルスト": "side valkenhorst normal",
        "ジャイナ兵": "side oriasiangeneral normal",
        "若手書記": "side borkind normal",
        "ニャガアアアアアルドバル": "side politician2 normal",
        "ヘス": "side hess normal",
        "演説者": "side hess normal",
        "フバル": "side hubal determined",
        "リンゲ": "side germaniangeneral normal",
        "リュージュ": "side luge normal",
        "クロムウェル": "side basicgeneral normal",
        "Bound": "side oldwoman normal",
        "ノルダ兵": "side norda normal",
        "ラマー": "side politician normal",
        "テレキ": "side official normal",
        "キリスト教徒": "side christian normal",
        "修道院長": "side prior normal",
        "クシマ": "side sima normal",
        "議会": "side chambers normal",
        "ハリファックス": "side halifax normal",
        "ポリックス兵": "side polix normal",
        "シコルスキア": "side sikorski normal",
        "ゴート": "side gort normal",
        "ダウ": "side germanianadmiral normal",
        "ゲルマニア海軍提督": "side germanianadmiral normal",
        "ウェイガン": "side weygand normal",
        "キルポノス": "side kirponos normal",
        "パヴロフ": "side pavlov normal",
        "ディマシェンカ": "side dimashenka normal",
        "レノー": "side reynaud normal",
        "ビヨット": "side billotte normal",
        "タラティエ": "side reynaud normal",
        "ダニア兵": "side daniayouth normal",
        "モンティ": "side monty normal",
        "ヤマト": "side yamato",
        "ヒトラ": "side hitora hat angry",
        "アントネス": "side antoness normal",
        "赤毛の少女": "side antoness normal",
        "カリネスグ": "side kalinesgu normal",
        "フィンバディッシュ兵": "side finbard normal",
        "ガロル2世": "side king normal",
        "リニー": "side rinni hat normal",
        "ムッソリニー": "side rinni hat normal",
        "スタリン": "side starin hat normal",
        "レーヌ": "side roijean hat normal",
        "レクレルシア": "side roijean hat normal",
        "ジューキフ": "side zhukky hat normal",
        "ゴーリング": "side goring determined",
        "ヨッベルス": "side joebbels normal",
        "デュニッツ": "side dunitz bored",
        "Nyan Katshex": "side nyan normal",
        "ルーズベルト": "side roosevelt normal",
        "チャーチル": "side churchill hat normal",
        "シラノ": "side cyrano hat normal",
        "キュートガール": "side cyrano hat normal",
        "ヒラヒタ": "side hirahita normal",
        "ポーリー王子": "side politician determined",
        "マンネルヘイム": "side mannerheim normal",
        "ドレスコウ": "side dresckow normal",
        "謎の男": "side dresckow normal",
        "チトー": "side tito normal",
        "喧嘩腰な少女": "side tito normal",
        "ヴィルヘルミナ": "side kaiser normal",
        "バドリオ": "side badoglio hat normal",
        "バテニア": "side battenia normal",
        "スタフィー": "side stuffy normal",
        "マンシュタイン": "side manstein normal",
        "可愛らしい少女": "side manstein normal",
        "シミグウィ": "side smigly normal",
        "ホルティ": "side horthy normal",
        "グデーリアン": "side guderian normal",
        "ガムラン": "side gamelin normal",
        "モロトフ": "side molotov normal",
        "グラツィアーニ": "side graziani normal",
        "ヴィタリア軍元帥": "side graziani normal",
        "カヴァッレーロ": "side cavallero normal",
        "メッセ": "side messe normal",
        "ヴァシレ": "side vasile normal",
        "マレッティ部隊": "side vitalia normal",
        "ヴィタリア兵": "side vitalia normal",
        "ブルッキー": "side brookie normal",
        "ジャンボ": "side jumbo normal",
        "ホーコン7世": "side haakon normal",
        "Simovic": "side simovic normal",
        "ミハイラ": "side mihaila normal",
        "闇のヒトラ": "side negahitora",
        "ヒトラ?": "side negahitora",
        " ": "character/side/narrator_th.png",
        "看護婦": "side nurse normal",
        "大尉": "side oriasiangeneral normal",
        "店主": "side fatman normal",
        "医者": "side politician normal",
        "政治家": "side politician normal",
        "幼い少女": "side starin hat normal",
        "謎の声": "character/side/blank_th.png",
        "諜報員": "side agent normal",
        "従者": "side official normal",
        "スタチュー": "side stachie normal",
        "訓練指導者": "side fatman normal",
        "サニー": "side politician normal",
        "工兵": "side axis normal",
        "ヒモラー": "character/side/himmora_th.png",
        "群衆": "character/side/blank_th.png",
        "みんな": "character/side/blank_th.png",
        "娘": "character/side/blank_th.png",
        "亡霊": "character/side/blank_th.png",
        "フェインベルグ": im.Sepia("character/side/freyaborg_th.png"),
        "アメリカ兵": "side amerika normal",
        "MIB捜査官": "side agent normal",
        "国王": "side king normal",
        "ディートリング": "side dietling normal",
        "タケシ": "side takeshi normal",
        "少年": "side youth normal",
        "護衛官": "side official normal",
        "フライシャー": "side vleischer normal",
        "侍女": "side maid normal",
        "使用人": "side servant1 normal",
        "兄": "side oldman normal",
        "太った男": "side fatman normal",
        "ポリックスのレジスタンス": "side hubal normal",
        "少女": "side woman normal",
        "不思議な少女": "side zhukky hat moe2",
        "麗人": "side hirahita normal",
        "老人": "side oldman normal",
        "老婦": "side oldwoman normal",
        "男性": "side man normal",
        "紳士": "side official normal",
        "女性": "side woman normal",
        "運転手": "side soldier normal",
        "ゲルマニア軍将官": "side germaniangeneral normal",
        "カウピッシュ": "side germaniangeneraloberst normal",
        "リステ": "side germaniangeneraloberst normal",
        "ブリタニア軍将官": "side britanniangeneral normal",
        "血まみれのヴァシー": "side vasey determined",
        "イラジ軍将官": "side desertgeneral normal",
        "ソヴィア軍将官": "side soviangeneral normal",
        "クリーマ": "side klima normal",
        "ZZ 将官": "side zombiegeneral determined",
        "ZZ 隊員": "side zombiesoldier determined",
        "偽物のポリックス兵": "side polixfake determined",
        "ジャール": "side zchaal normal",
        "新参兵": "side takeshi normal",
        "兵士": "side soldier normal",
        "ジパング兵": "side zipangu normal",
        "ジパング兵士": "side axis normal",
        "衛生兵": "side axis normal",
        "枢軸兵": "side axis normal",
        "ゲルマニア兵": "side axis normal",
        "ゲルマニア空挺部隊": "side winteraxis normal",
        "連合兵": "side allied normal",
        "ソヴィア兵": "side sovian normal",
        None: "character/side/narrator_th.png"
    }

    def HistoryImage(name = None):
        if name in NameList:
            return NameList[name]
        else:
            
            return "character/side/blank_th.png"

