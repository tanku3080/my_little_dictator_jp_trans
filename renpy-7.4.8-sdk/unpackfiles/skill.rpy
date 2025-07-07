init python:
    class BaseSkill():

        def __init__(self, id, kind, name, desc, skilltype, pp, image, sound, animation, base_hp=0, user_hp_change=0, status_self=None, status_enemy=None, osd=0.0, line=""):
            """
            Base class for all Attacks/Heals

            id: String. Unique Id of the skill.
            kind: String. Kind of spell.
            name: String. Name of the skill.
            desc: String. Details of the skill.
            skilltype: Elemental type of move
            image: String. Main image of the skill.
            animation: ATL.
            base_hp: Integer. Damange/heal to be done on HP to the enemy. Default is 0.
            user_hp_change: Integer. Damange/heal to be done on HP on the user. Default is 0.
            status_self: Dict. Contains the information about the status that will apply on the user.
            status_enemy: Dict. Contains the information about the status that will apply on the enemy.
            osd: On screen display time for the skill.
            line: String. The status line to be displayed.
            """

            self.id = id
            self.kind = kind
            
            self.name = name
            self.desc = desc
            self.skilltype = skilltype
            
            self.pp = int(pp)
            self.max_pp = self.pp
            
            self.image = At(image)
            self.sound = "se/" + sound
            self.animation = animation

            self.base_hp = int(base_hp)
            self.user_hp_change = int(user_hp_change)
            self.status_self = return_var(status_self)
            self.status_enemy = return_var(status_enemy)
            self.osd = float(osd)
            self.line = line

        def can_do(self):
            """
            Returns True if the Fighter has enough PP to do the attack
            """

            if self.pp > 0:
                return True
            return False

        def use(self, attacker, enemy, change):
            """
            Performs a skill.

            attacker: Instance of BaseFighter. Combatant who is using the skill.
            enemy: Instance of BaseFighter. Combatant on which the skill is going to be used.
            change: Integer. The change in hp.
            """

            player_hp_change = self.user_hp_change
            player_status = self.status_self["name"] if self.status_self else ""
            enemy_status = self.status_enemy["name"] if self.status_enemy else ""

            self.pp -= 1

            if change <= 0:
                enemy.change_hp(change)

                if player_hp_change:
                    change = int(change)
                    if player_hp_change == 99999: #generic absorb number
                        player_hp_change = -(renpy.random.randint(change, change/2))
                    attacker.change_hp(player_hp_change)

            if self.status_self:
                attacker.add_status(self.status_self)

            if self.status_enemy:
                enemy.add_status(self.status_enemy)

            if self.kind == "heal":
                attacker.change_hp(self.base_hp)
                change = int(renpy.random.randint((self.base_hp / 2), self.base_hp))

            # The status line for the attack
            if self.line:
                if attacker != enemy:
                    if enemy.hp < 1:
                        damage_effective = "It's a critical hit!"
                    elif abs(change) >= (enemy.hp * 0.75):
                        damage_effective = "It's super effective!"
                    elif abs(change) >= (enemy.hp * 0.5) and abs(change) < (enemy.hp * 0.75):
                        damage_effective = "It causes major damage."  
                    elif abs(change) >= (enemy.hp * 0.25) and abs(change) < (enemy.hp * 0.5):
                        damage_effective = "It inflicts minor damage."
                    elif abs(change) >= (enemy.hp * 0.05) and abs(change) < (enemy.hp * 0.25):
                        damage_effective = "It's not very effective . . ."
                    elif abs(change) >= (enemy.hp * 0.01) and abs(change) < (enemy.hp * 0.05):
                        damage_effective = "It's not effective at all."
                    else:
                        damage_effective = ""
                else:
                    if player.hp < 1:
                        damage_effective = "It's a critical hit!"
                    elif abs(change) >= (player.hp * 0.75):
                        damage_effective = "It's super effective!"
                    elif abs(change) >= (player.hp * 0.5) and abs(change) < (player.hp * 0.75):
                        damage_effective = "It causes major damage."  
                    elif abs(change) >= (player.hp * 0.25) and abs(change) < (player.hp * 0.5):
                        damage_effective = "It inflicts minor damage."
                    elif abs(change) >= (player.hp * 0.1) and abs(change) < (player.hp * 0.25):
                        damage_effective = "It's not very effective . . ."
                    elif abs(change) >= (player.hp * 0.01) and abs(change) < (player.hp * 0.1):
                        damage_effective = "It's not effective at all."
                    else:
                        damage_effective = ""
                _line = self.line.replace("_name_", "{i}{color=#C6B483}" + attacker.name + "{/color}{/i}").replace("_skill_", "{i}{color=#FF7676}" + self.name + "{/color}{/i}").replace("_damage_", str(damage_effective)).replace("_enemy_", enemy.name).replace("_absorb_", str(player_hp_change)).replace("_status_self_", player_status).replace("_status_enemy_", enemy_status)
                battle_lines(_line)

        @property
        def use_text(self):
            return str(self.base_hp) + " damage to hp"
            
        @property
        def get_pp(self):
            return str(self.pp) + " / " + str(int(self.max_pp))

    class Status():

        def __init__(self, name, colour, desc, boost, chance, turns_remaining=0):
            self.name = name
            self.colour = colour
            self.desc = desc
            self.boost = boost
            self.chance = chance
            self.turns_remaining = turns_remaining

        def still_active(self):
            self.turns_remaining -= 1

            if self.turns_remaining < 0:
                return False
            return True

        def add_turns(self, turns):
            self.turns_remaining += turns

        def get_effect(self, effect):
            self.turns_remaining -= 1
            if "effect" in self.boost:
                return effect in self.boost["effect"]
            return False

        def get_value(self, attr):
            if attr in self.boost:
                return self.boost[attr]
            return 0

screen skill_fullscreen(details, direction):
    zorder 102
    default show_image = False
    timer details[1] action SetScreenVariable(name='show_image', value=True)
    if show_image:
        add (details[0] + direction) xalign 0.5 yalign 0.5
        
screen fighter_intro(profile, name):
    modal True
    zorder 12
    timer 3.5 action [With(pixellate), Hide("fighter_intro"), SetVariable("battle_enemyintro", True), SetVariable("deadplayerfighter", False), Function(game.resume_game)]
    add Solid("#000000") alpha 0.95
    add At("background_block", intro_fade) xalign 0.5 yalign 0.4
    add At("nameintro_block", intro_fade) xalign 0.5 yalign 0.8
    add At(profile, intro_trans) yalign 0.25
    add At(Text(name + " enters the field."), intro_reverse_trans) yalign 0.78
    frame:
        background Frame(im.Sepia("gui/outer_frame.png"), 200, 200)
        xminimum 1922
        yminimum 1082
    
screen fighter_switch(profile, name, last_profile, last_name):
    modal True
    zorder 12
    timer 7.3 action [With(pixellate), Hide("fighter_switch"), Function(game.resume_game)]
    add Solid("#000000") alpha 0.95
    add At("background_block", intro_fade) xalign 0.5 yalign 0.4
    add At("nameintro_block", intro_fade) xalign 0.5 yalign 0.8
    add At(last_profile, intro_reverse_trans) yalign 0.25
    add At(Text(last_name + ", that's enough."), intro_trans) yalign 0.78
    add At(profile, switch_trans) yalign 0.25
    add At(Text(name + " enters the field."), switch_reverse_trans) yalign 0.78
    frame:
        background Frame(im.Sepia("gui/outer_frame.png"), 200, 200)
        xminimum 1922
        yminimum 1082
    
image background_block = "battle/ui/fighter_intro_overlay.png"
image nameintro_block = "battle/ui/fighter_intro_name_overlay.png"

screen death_scene(profile, name):
    modal True
    zorder 12
    timer 3.0 action [Hide("death_scene"), With(pixellate), Function(game.resume_game)]
    add Solid("#000000") alpha 0.9
    add At("background_block", intro_fade)
    add At(profile, intro_trans) yalign 0.35
    add At(Text(name + " death scene."), intro_reverse_trans) yalign 0.65
    
