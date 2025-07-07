

init python:
    import time
    from time import sleep
    
    class ChangeFighter(Action):

        def __init__(self, fighter=None, shown=False):
            self.fighter = fighter
            self.shown = shown

        def __call__(self):
            if self.fighter:
                player_team.last_fighter = current_player
                store.current_player = self.fighter

            if self.shown:
                game.change_player()
                renpy.hide_screen("battle_party_screen")
            else:
                return

    class AddToParty(Action):

        def __init__(self, name, cost):
            self.name = name
            self.cost = cost

        def __call__(self):
            player_team.add_fighter(self.name)
            store.cp -= self.cost
            renpy.restart_interaction()

        def get_sensitive(self):
            if len(player_team.store) >= 8 or self.cost > store.cp:
                return False
            for fighter in player_team.store:
                if "commander_" in self.name and str(self.name) in str(fighter.image):
                    return False
            return True

    class RemoveFromParty(Action):

        def __init__(self, fighter):
            self.fighter = fighter

        def __call__(self):
            player_team.remove_fighter(self.fighter)
            store.cp += self.fighter.cost
            renpy.restart_interaction()

    class Battleground(renpy.Displayable):

        def __init__(self, name, player, enemy, capture):
            """
            Battleground.

            name: String. Name of the ground.
            player: Instance of BaseFigher. Player's combatant.
            enemy: Instance of BaseFigher. Enemy's combatant.
            """

            super(Battleground, self).__init__()

            self.name = name
            self.player = player
            self.enemy = enemy
            self.capture = capture

            store.current_player = player
            
            self.player_counter = {
                "critical": 0,
                "missed": 0,
                "total_damage": 0
            }

            self.enemy_counter = {
                "critical": 0,
                "missed": 0,
                "total_damage": 0
            }

            self.queue = []
            self.attacker = False

            self.image = None
            self.animation = None
            self.id = None
            self.wait = 2.5
            self.st = 0
            self.remaining_wait = 0.0
            self.game_paused = True
            self.can_hide_fighter = False
            battle_lines("{i}{color=#C6B483}" + self.enemy.name + "{/color}{/i}" + " wants to fight!")
            
            self.animation_details = None
            
            self.fighter_dead = False
            self.game_end = False
            
            #test_case.change("test", "reset")

            # Find the que of attacks and ready the first combatant for attack
            self.attack_que()
            #self.ready_attacker()

        def render(self, width, height, st, at):
            render = renpy.Render(width, height)
            self.st = st

            # Render the player
            if self.player:
                if self.can_hide_fighter and self.attacker != self.player:
                    render.place(At((self.player.receive_sprite + "_back"), death_fade), *player_pos) #death animation
                elif self.animation and not self.attacker.last_missed and self.wait - st < 0.5 :
                    if self.attacker != self.player:
                        render.place(At(self.player.walk_sprite + "_back"), *player_pos) #happens at end of enemy attack
                    else:
                        if self.enemy.hp >= 1:
                            pass
                        elif not self.enemy.hp >= 1 and not battlesprite_overlaying:
                            #render.place(At(self.player.__dict__[self.animation["finalframe"] + "_sprite"] + "_back"), *player_pos) #happens at end of player attack
                            render.place(At(self.player.walk_sprite + "_back"), *player_pos)
                        else:
                            pass
                        
                elif self.animation and abs(int(self.attacker.last_damage)) == 0 and self.wait - st < 1.5 :
                    if self.animation["kind"] == "attack" and self.attacker != self.player:
                        render.place(At(self.player.walk_sprite + "_back"), *player_pos) #appears at end when missed shot from enemy
                        render.place(At(Text("{image=readyfight_text_miss}", xalign=0.75, yalign=0.45), flash_stat), *player_pos)
                    elif self.animation["kind"] == "self" and self.attacker == self.player:
                        if self.animation["listing"] == "heal":
                            pass
                    elif self.animation["kind"] == "self" and self.attacker != self.player:
                        if self.animation["listing"] == "heal":
                            render.place(At(self.player.walk_sprite + "_back"), *player_pos)
                        elif self.animation["listing"] == "main1_powerup" or self.animation["listing"] == "main2_powerup":
                            render.place(At(self.player.walk_sprite + "_back"), *player_pos)
                    else:
                        pass #during player missing a shot
                        
                elif self.animation and gui_text[0] == ("{i}{color=#C6B483}" + self.attacker.name + "{/color}{/i}" + " dealt a fatal blow. " + "{i}{color=#C6B483}" + self.player.name + "{/color}{/i}" + " has fallen on the battlefield.") and not self.attacker.last_missed and self.wait - st < 1.5: #KO flash before death
                    if self.animation["kind"] == "attack" and self.attacker != self.player:
                        render.place(At((self.player.receive_sprite + "_back"), damage_red), *player_pos)
                        render.place(At(Text("{image=readyfight_text_knockout}", size=70, text_align=0.5, xalign=0.5, yalign=0.45, font="font/cmsquish.ttf", kerning=-18, color="#f62626", outlines=[(2, "#793F09", 0, 0)], drop_shadow_color="#3F2104"), flash_stat), *player_pos)
                    elif not battlesprite_overlaying: 
                        render.place(At(self.player.__dict__[self.animation["finalframe"] + "_sprite"] + "_back"), *player_pos)
                    else:
                        pass
                    
                elif self.animation and not self.attacker.last_missed and self.wait - st < 1.5 : #displays the amount of damage done
                    if self.animation["kind"] == "attack" and self.attacker != self.player:
                        render.place(At((self.player.receive_sprite + "_back"), damage_red), *player_pos)
                        render.place(At(Text(str(abs(int(self.attacker.last_damage))) + "{image=readyfight_text_damage}", size=70, text_align=0.5, xalign=0.5, yalign=0.45, font="font/cmsquish.ttf", kerning=-18, color="#f62626", outlines=[(2, "#793F09", 0, 0)], drop_shadow_color="#3F2104"), flash_stat), *player_pos)
                    elif not battlesprite_overlaying: 
                        #render.place(At(self.player.__dict__[self.animation["finalframe"] + "_sprite"] + "_back"), *player_pos) #happens at KO for bulk of time before switching to earlier one
                        render.place(At(self.player.walk_sprite + "_back"), *player_pos)
                    else:
                        pass
                    
                elif self.animation and not self.attacker.last_missed and self.image and self.enemy.hp >= 1 :
                    if self.animation["kind"] == "attack" and self.attacker == self.player:
                        pass
                    elif self.animation["kind"] == "self" and self.attacker == self.player and self.animation["listing"] == "main1_powerup":
                        pass
                    elif self.animation["kind"] == "self" and self.attacker == self.player and self.animation["listing"] == "main2_powerup":
                        pass
                    elif self.animation["kind"] == "self" and self.attacker == self.player and self.animation["listing"] == "heal":
                        pass
                    else:
                        render.place(At(self.player.walk_sprite + "_back"), *player_pos) #appears when hit
                        
                elif self.animation and not self.attacker.last_missed and self.enemy.hp < 1 and not battlesprite_overlaying :
                    render.place(At(self.player.walk_sprite + "_back"), *player_pos) #can't find out what this is doing, if anything
                elif self.animation and not self.attacker.last_missed:
                    if self.animation["kind"] == "attack" and self.attacker == self.player:
                        pass
                    elif self.animation["kind"] == "self" and self.attacker == self.player:
                        pass #prevents walk sprite under heal/powerup
                    else:
                        render.place(At(self.player.walk_sprite + "_back"), *player_pos) #appears at start of missed shot from enemy
                else:
                    render.place(At(self.player.walk_sprite + "_back"), *player_pos) #static, shows most of the time
                    

            # Render the enemy
            if self.enemy:
                if self.can_hide_fighter and self.attacker != self.enemy:
                    render.place(At((self.enemy.receive_sprite + "_front"), death_fade), *enemy_pos) #death animation
                elif self.animation and not self.attacker.last_missed and self.wait - st < 0.5 :
                    if self.attacker != self.enemy:
                        render.place(At(self.enemy.walk_sprite + "_front"), *enemy_pos) #happens at end of player attack
                    else:
                        if self.player.hp >= 1:
                            pass
                        elif not self.player.hp >= 1 and not battlesprite_overlaying:
                            #render.place(At(self.enemy.__dict__[self.animation["finalframe"] + "_sprite"] + "_front"), *enemy_pos) #happens at end of enemy attack
                            render.place(At(self.enemy.walk_sprite + "_front"), *enemy_pos)
                        else:
                            pass
                        
                elif self.animation and abs(int(self.attacker.last_damage)) == 0 and self.wait - st < 1.5 :
                    if self.animation["kind"] == "attack" and self.attacker != self.enemy:
                        render.place(At(self.enemy.walk_sprite + "_front"), *enemy_pos) #appears at end when missed shot from player
                        render.place(At(Text("{image=readyfight_text_miss}", xalign=0.75, yalign=0.45), flash_stat), *enemy_pos)
                    elif self.animation["kind"] == "self" and self.attacker == self.enemy:
                        if self.animation["listing"] == "heal":
                            pass
                    elif self.animation["kind"] == "self" and self.attacker != self.enemy:
                        if self.animation["listing"] == "heal":
                            render.place(At(self.enemy.walk_sprite + "_front"), *enemy_pos)
                        elif self.animation["listing"] == "main1_powerup" or self.animation["listing"] == "main2_powerup":
                            render.place(At(self.enemy.walk_sprite + "_front"), *enemy_pos)
                    else:
                        pass #during enemy missing a shot
                        
                elif self.animation and gui_text[0] == ("{i}{color=#C6B483}" + self.attacker.name + "{/color}{/i}" + " dealt a fatal blow. " + "{i}{color=#C6B483}" + self.enemy.name + "{/color}{/i}" + " has fallen on the battlefield.") and not self.attacker.last_missed and self.wait - st < 1.5: #KO flash before death
                    if self.animation["kind"] == "attack" and self.attacker != self.enemy:
                        render.place(At((self.enemy.receive_sprite + "_front"), damage_red), *enemy_pos)
                        render.place(At(Text("{image=readyfight_text_knockout}", size=70, text_align=0.5, xalign=0.5, yalign=0.45, font="font/cmsquish.ttf", kerning=-18, color="#f62626", outlines=[(2, "#793F09", 0, 0)], drop_shadow_color="#3F2104"), flash_stat), *enemy_pos)
                    elif not battlesprite_overlaying:
                        render.place(At(self.enemy.__dict__[self.animation["finalframe"] + "_sprite"] + "_front"), *enemy_pos)
                    else:
                        pass
                        
                elif self.animation and not self.attacker.last_missed and self.wait - st < 1.5 :
                    if self.animation["kind"] == "attack" and self.attacker != self.enemy:
                        render.place(At((self.enemy.receive_sprite + "_front"), damage_red), *enemy_pos)
                        render.place(At(Text(str(abs(int(self.attacker.last_damage))) + "{image=readyfight_text_damage}", size=70, text_align=0.5, xalign=0.5, yalign=0.45, font="font/cmsquish.ttf", kerning=-18, color="#f62626", outlines=[(2, "#793F09", 0, 0)], drop_shadow_color="#3F2104"), flash_stat), *enemy_pos)
                    elif not battlesprite_overlaying:
                        #render.place(At(self.enemy.__dict__[self.animation["finalframe"] + "_sprite"] + "_front"), *enemy_pos) #happens at KO for bulk of time before switching to earlier one
                        render.place(At(self.enemy.walk_sprite + "_front"), *enemy_pos)
                    else:
                        pass
                    
                elif self.animation and not self.attacker.last_missed and self.image and self.player.hp >= 1 :
                    if self.animation["kind"] == "attack" and self.attacker == self.enemy:
                        pass
                    elif self.animation["kind"] == "self" and self.attacker == self.enemy and self.animation["listing"] == "main1_powerup":
                        pass
                    elif self.animation["kind"] == "self" and self.attacker == self.enemy and self.animation["listing"] == "main2_powerup":
                        pass
                    elif self.animation["kind"] == "self" and self.attacker == self.enemy and self.animation["listing"] == "heal":
                        pass
                    else:
                        render.place(At(self.enemy.walk_sprite + "_front"), *enemy_pos) #appears when hit
                        
                elif self.animation and not self.attacker.last_missed and self.player.hp < 1 and not battlesprite_overlaying :
                    render.place(At(self.enemy.walk_sprite + "_front"), *enemy_pos) #can't find out what this is doing, if anything
                elif self.animation and not self.attacker.last_missed:
                    if self.animation["kind"] == "attack" and self.attacker == self.enemy:
                        pass
                    elif self.animation["kind"] == "self" and self.attacker == self.enemy:
                        pass #prevents walk sprite under heal/powerup
                    else:
                        render.place(At(self.enemy.walk_sprite + "_front"), *enemy_pos) #appears at start of missed shot from player
                else:
                    render.place(At(self.enemy.walk_sprite + "_front"), *enemy_pos) #static, shows most of the time
                    

            # This checks if an action has happened on screen.
            # (action in this context any sequence where player shouldn't be able to interact with the game)

            if not self.game_paused:
                if self.wait > st:
                    # If there is an image to be shown/animation to be played, do so.
                    if self.image and not self.wait - st < 1.3 and not self.attacker.last_missed:
                        if self.animation_details == enemy_pos:
                            if self.animation["kind"] == "self":
                                render.place(At(self.image, anim_regular), *player_pos)
                            else:
                                render.place(At(self.image, anim_flip), *self.animation_details)
                        else:
                            if self.animation["kind"] == "self":
                                render.place(At(self.image, anim_flip), *enemy_pos)
                            else:
                                render.place(At(self.image, anim_regular), *self.animation_details)
                    
                elif self.wait:
                    renpy.hide_screen("skill_fullscreen")
                    renpy.hide_screen("battle_sprites")
                    renpy.restart_interaction()

                    if len(store.gui_text) > 1:
                        self.wait = self.st + 2.5
                        del store.gui_text[0]
                        
                        renpy.restart_interaction()
                    else:
                        store.gui_text = []
                        self.wait = 0
                        self.image = None
                        self.animation = None
                        self.animation_details = None

                        renpy.timeout(0)

                        if not self.fighter_dead:
                            self.ready_attacker()

            renpy.redraw(self, 0)
            return render

        def event(self, ev, x, y, st):
            global bar_delay
            global skip_battle_happen

            bar_delay = 1.5
            
            if renpy.map_event(ev, "dismiss") and self.wait and store.click_to_proceed:
                self.wait = st - 0.1

            # GAME OVER
            if self.game_end and self.wait == 0:
                renpy.music.stop(channel="battlemusic", fadeout=3.0)
                renpy.music.stop(channel="battlesfx", fadeout=1.0)
                if skip_battle_happen:
                    skip_battle_happen = False
                    renpy.jump(fight_end)
                else:
                    renpy.jump("gameover_trigger")

            # DEATH ANIMATION
            if self.wait == 0 and self.fighter_dead and not self.can_hide_fighter:
                self.wait = 2.5 + st
                self.can_hide_fighter = True
                battlesprite_overlaying = False
                renpy.play("se/battle/death.ogg", "battlesound2")
                
            if self.wait == 0 and self.can_hide_fighter:
                self.can_hide_fighter = False
                self.fighter_dead = False
                if self.enemy.hp < 1:
                    new_enemy = enemy_team.auto_switch(remove=self.enemy)
                    if not new_enemy:
                        if not novictoryscreen_enabled:
                            #VICTORY SCREEN
                            active_fuuhbarmuseum_items.update({"captured_" + game.capture: [eval("captured_" + game.capture + "_name"), eval("captured_" + game.capture + "_description")]})
                            postbattle_museum_unlocked = "museum_" + game.capture + "_unlocked"
                            globals()[postbattle_museum_unlocked] = True
                            renpy.play("se/win.ogg", "battlesound1")
                            renpy.music.stop(channel="battlemusic", fadeout=3.0)
                            renpy.music.stop(channel="battlesfx", fadeout=1.0)
                            renpy.music.play("music/map4.ogg", channel="victorymusic", fadein=3.0)
                            renpy.show_screen("victory_screen", won="player")
                        else:
                            renpy.music.stop(channel="battlemusic", fadeout=3.0)
                            renpy.music.stop(channel="battlesfx", fadeout=1.0)
                            renpy.jump(fight_end)
                    else:
                        self.enemy = new_enemy
                        #bar_delay = 4.9
                        self.attack_que()
                        renpy.show_screen("fighter_intro", profile=(self.enemy.walk_sprite + "_front"), name=self.enemy.name)
                        self.pause_game()
                        renpy.restart_interaction()
                        battle_lines("{i}{color=#C6B483}" + self.enemy.name + "{/color}{/i}" + " enters the field.")
                        self.wait = 7.0 + self.st
                        
                if self.player.hp < 1:
                    player_team.remove_fighter(self.player)
        
                    if not player_team.store:
                        #game over
                        renpy.music.stop(channel="battlemusic", fadeout=3.0)
                        renpy.music.stop(channel="battlesfx", fadeout=1.0)
                        renpy.jump("gameover_trigger")
                    else:
                        #new player enters
                        renpy.show_screen("battle_party_screen", mid_game=True)
                        self.pause_game()
                        renpy.restart_interaction()
                        self.wait = 3.0 + self.st
                        
                renpy.restart_interaction()

        def attack_que(self):
            """
            Set the order in which the battle will happen.
            """

            self.queue = []

            if self.player.speed > self.enemy.speed:
                self.queue.extend( [self.player, self.enemy] )
            else:
                self.queue.extend( [self.enemy, self.player] )

        def ready_attacker(self):
            # Mark the attacker as dorment
            renpy.hide_screen("battle_sprites")
            renpy.restart_interaction()

            if self.game_end:
                return

            if self.attacker:
                self.attacker.attacking = False

            self.attacker = self.queue.pop(0)
            self.queue.append(self.attacker)

            renpy.restart_interaction()

            # Check what status affects the player and the enemy
            self.attacker.check_status()
            self.queue[0].check_status()

            # If attacker is paralysed, move on
            if not self.attacker.can_attack:
                if "panzer" in self.attacker.walk_sprite or self.attacker.walk_sprite.startswith("antitank_"): 
                    myList = ["broken down on the battlefield", "severely damaged", "doing a crew headcount"]
                elif "airsupport" in self.attacker.walk_sprite:
                    myList = ["beginning to smoke", "severely damaged", "trying to manoeuvre"]
                else:
                    myList = ["stunned", "suffering from shell shock", "weary from battle fatigue", "recovering", "blinded in the heat of battle", "taking a moment to rest", "slow to react", "feeling sleepy"]
                battle_lines("{i}{color=#C6B483}" + self.attacker.name + "{/color}{/i}" + " is " + random.choice(myList) + " and cannot move.")
                self.wait = 2.5 + self.st
            else:
                # Calculates the best attack to do and how to do.
                if self.attacker.ai:
                    skill = self.attacker.auto_fight(self.player)
                    self.chosen_skill(skill)
                else:
                    battle_lines("What will " + "{i}{color=#C6B483}" + self.attacker.name + "{/color}{/i}" + " do?")

        def chosen_skill(self, skill):
            """
            Actually performs the chosen skill.

            skill: Instance of Skill.
            """
            
            # If an animation is in progress, do nothing
            if self.animation_details:
                return
            
            store.gui_text = []
            self.attacker.use(skill, self.queue[0])
            self.update_counter()

            # If the attacker missed, pause the game to show the lines.
            if self.attacker.last_missed:
                self.attacker.last_missed = False
                self.animation = skill.animation
                self.wait = skill.osd + self.st
                
                if self.attacker.ai:
                    self.animation_details = player_pos
                else:
                    self.animation_details = enemy_pos
                    
                if "full_screen" in self.animation:
                    if self.attacker == self.player:
                        #renpy.show_screen("skill_fullscreen", details=self.animation["full_screen"])
                        renpy.show_screen("skill_fullscreen", details=self.animation["full_screen"], direction="_back")
                    else:
                        renpy.show_screen("skill_fullscreen", details=self.animation["full_screen"], direction="_front")
                    
                if not self.fighter_dead:
                    renpy.play(skill.sound, "battleattack")
                    
            elif self.attacker.no_moves:
                self.wait = 3.0 + self.st
                
            else:
                self.image = skill.image
                self.animation = skill.animation
                self.wait = skill.osd + self.st
                
                if self.attacker.ai:
                    self.animation_details = player_pos
                else:
                    self.animation_details = enemy_pos
                    
                if "full_screen" in self.animation:
                    if self.attacker == self.player:
                        renpy.show_screen("skill_fullscreen", details=self.animation["full_screen"], direction="_back")
                    else:
                        renpy.show_screen("skill_fullscreen", details=self.animation["full_screen"], direction="_front")
                    
                if not self.fighter_dead:
                    renpy.play(skill.sound, "battleattack")
                    
                    if skill.kind == "attack":
                        if self.attacker.unit == "commander" or self.attacker.unit == "enemyboss":
                            if self.attacker.fullname != "Commander Yamato Yamamoto" and self.attacker.fullname != "Nega-Hitora":
                                t = (globals()[(self.attacker.name.lower().replace(" ", "")) + "_battle_voiceset"])
                                renpy.play(random.choice(t), "battlevoice")
        
            if self.player.hp < 1:
                self.fighter_dead = True
                battle_lines("{i}{color=#C6B483}" + self.attacker.name + "{/color}{/i}" + " dealt a fatal blow. " + "{i}{color=#C6B483}" + self.player.name + "{/color}{/i}" + " has fallen on the battlefield.")
                self.wait = 3.0 + self.st

            if self.enemy.hp < 1:
                self.fighter_dead = True
                battle_lines("{i}{color=#C6B483}" + self.attacker.name + "{/color}{/i}" + " dealt a fatal blow. " + "{i}{color=#C6B483}" + self.enemy.name + "{/color}{/i}" + " has fallen on the battlefield.")
                self.wait = 3.0 + self.st
                
            if self.attacker == self.player and not self.attacker.no_moves:
                image_name = self.attacker.__dict__[self.animation["listing"] + "_sprite"] + "_back"
                renpy.show_screen("battle_sprites", im=image_name, xypos=player_pos)
                
            if self.attacker == self.enemy and not self.attacker.no_moves:
                image_name = self.attacker.__dict__[self.animation["listing"] + "_sprite"] + "_front"
                renpy.show_screen("battle_sprites", im=image_name, xypos=enemy_pos)
                
            if self.attacker.no_moves:
                self.attacker.no_moves = False
                
            
                
            renpy.restart_interaction()

        def player_turn(self):
            if not self.attacker or self.game_end or self.wait:
                return False
            return self.attacker.ai == False and self.attacker.attacking == False

        def change_player(self):
            self.player = current_player
            self.attack_que()
            if not player_team.last_fighter.hp < 1:
                renpy.show_screen("fighter_switch", profile=(self.player.walk_sprite + "_front"), name=self.player.name, last_profile=(player_team.last_fighter.walk_sprite + "_front"), last_name=player_team.last_fighter.name)
            else:
                renpy.show_screen("fighter_intro", profile=(self.player.walk_sprite + "_front"), name=self.player.name)
            self.pause_game()
            renpy.restart_interaction()
            battle_lines("{i}{color=#C6B483}" + self.player.name + "{/color}{/i}" + " enters the field.")
            self.wait = 7.0 + self.st
            
        def can_run_away(self):
            renpy.play("se/dash.ogg", "battlesound2")
            battle_lines("Your party has deserted the battlefield.")
            global skip_battle_happen
            skip_battle_happen = True
            self.wait = 0.5
            self.game_end = True

        def update_counter(self):
            critical = 1 if self.attacker.last_critical else 0
            missed = 1 if self.attacker.last_missed else 0
            damage = 0 if not self.attacker.last_damage else self.attacker.last_damage

            if self.attacker.ai:
                self.enemy_counter["critical"] += critical
                self.enemy_counter["missed"] += missed
                self.enemy_counter["total_damage"] += damage
            else:
                self.player_counter["critical"] += critical
                self.player_counter["missed"] += missed
                self.player_counter["total_damage"] += damage
                
        def pause_game(self):
            self.game_paused = True
            self.remaining_wait = self.wait - self.st

        def resume_game(self):
            global battle_enemyintro
            self.game_paused = False
            if battle_enemyintro:
                self.remaining_wait = 3
            self.wait = self.st + self.remaining_wait
            battle_enemyintro = False