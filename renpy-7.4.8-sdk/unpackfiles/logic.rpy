init python:

    class BaseTeam():

        def __init__(self, name, logo, limit):
            self.name = name
            self.logo = logo
            self.limit = limit

            self.store = []
            self.last_fighter = None

        def add_fighter(self, id, new_name=None):
            if id not in store.fighter_store:
                return "Invalid Fighter"

            fighter_dict = store.fighter_store[id]

            if new_name:
                old_name = fighter_dict["name"]
                fighter_dict["name"] = new_name

            fighter = BaseFighter(**fighter_dict)
            self.store.append(fighter)

            if new_name:
                fighter_dict["name"] = old_name

        def remove_fighter(self, fighter):
            self.last_fighter = fighter
            self.store.remove(fighter)

        def auto_switch(self, remove=None):
            if remove:
                self.remove_fighter(remove)
                
            if self.store:
                return self.store[0]
            return None
    
    class BaseFighter():

        def __init__(self, name, unit, image, walk_sprite, receive_sprite, main1_attack_sprite, main2_attack_sprite, special1_attack_sprite, special2_attack_sprite, special3_attack_sprite, main1_powerup_sprite, main2_powerup_sprite, heal_sprite, main1_attack_finalframe_sprite, main2_attack_finalframe_sprite, special1_attack_finalframe_sprite, special2_attack_finalframe_sprite, special3_attack_finalframe_sprite, main1_powerup_finalframe_sprite, main2_powerup_finalframe_sprite, heal_finalframe_sprite, animation, map_icon, level, cost, hp, attack, defense, accuracy, critical, speed, terrain, skill, fullname, description, primary_weapon, secondary_weapon, motto, perks, ai=False):
            """
            Base Class for all the fighters

            name: String. Name of the Fighter.
            unit: String. Type of Fighter.
            image: String. Image of the fighteer, to be shown in the different screens and UI boxes.
            sprite: String. Sprite of the fighter, to be shown during battle
            animation: Dict. Contains information about how to animate the sprite.
            map_icon: String. Name of the image of the map icon for this Fighter.
            level: Integer. Level of the Fighter. Purely for asthetic purpose as there is no Level Up mechanicsm.
            hp: Integer. Hit Points of the Fighter.
            attack: Integer. Determines how powerful attack moves are and the amount of damage they deal.
            defense: Integer. Determines how fighters can resist attacks by enemies and prevent damage.
            accuracy: Integer. Determines how often a fighter can attack an enemy successfully.
            critical: Integer. Determines how often a fighter can deliver critical damage within a successful attack.
            speed: Integer. Determines fighter order in battles.
            fullname: Detailed name and spec
            description: Full description of the fighter
            ai: Boolean. Should be True if fighting is done auto-magically.

            Attributes under this are internal

            max_stats: Dict. Contains the starting values of all the properties.
            last_move: Instance of Skill. The last move performed by the Fighter.
            attacking: Boolean. True if the Fighter is curently attacking.
            attack_store: Dict. Contains all the attack skills.
            heal_store: Dict. Contains all the healing skills.
            status_store: Dict. Contains all the status affecting the player.
            """

            self.name = name
            self.unit = unit
            self.image = image
            
            self.walk_sprite = walk_sprite
            self.receive_sprite = receive_sprite
            self.main1_attack_sprite = main1_attack_sprite
            self.main2_attack_sprite = main2_attack_sprite
            self.special1_attack_sprite = special1_attack_sprite
            self.special2_attack_sprite = special2_attack_sprite
            self.special3_attack_sprite = special3_attack_sprite
            self.main1_powerup_sprite = main1_powerup_sprite
            self.main2_powerup_sprite = main2_powerup_sprite
            self.heal_sprite = heal_sprite
            self.main1_attack_finalframe_sprite = main1_attack_finalframe_sprite
            self.main2_attack_finalframe_sprite = main2_attack_finalframe_sprite
            self.special1_attack_finalframe_sprite = special1_attack_finalframe_sprite
            self.special2_attack_finalframe_sprite = special2_attack_finalframe_sprite
            self.special3_attack_finalframe_sprite = special3_attack_finalframe_sprite
            self.main1_powerup_finalframe_sprite = main1_powerup_finalframe_sprite
            self.main2_powerup_finalframe_sprite = main2_powerup_finalframe_sprite
            self.heal_finalframe_sprite = heal_finalframe_sprite
            
            #self.walk_sprite = DynamicDisplayable(process_sprite_sheet, "{}".format(sprite), **animation)
            self.map_icon = map_icon
            self.level = int(level)
            self.cost = cost
            self.max_hp = float(hp)
            self.hp = int(hp)
            self.attack = int(attack)
            self.defense = int(defense)
            self.accuracy = int(accuracy)
            self.critical = int(critical)
            self.speed = int(speed)
            self.terrain = terrain
            self.description = description
            self.fullname = fullname
            self.primary_weapon = primary_weapon
            self.secondary_weapon = secondary_weapon
            self.motto = motto
            self.perks = perks

            if ai == "True":
                self.ai = True
            else:
                self.ai = False

            self.max_stats = {
                "attack": self.attack,
                "defense": self.defense,
                "accuracy": self.accuracy,
                "critical": self.critical,
                "speed": self.speed
            }

            self.second_last_move = None
            self.last_move = None
            self.last_missed = False
            self.no_moves = False
            self.last_critical = False
            self.last_damage = 0
            self.attacking = False

            self.power_up_in = -1
            self.enemy_analysed = False

            self.attack_store = {}
            self.heal_store = {}
            self.boost_id = ""

            self.status_store = {}

            for i in skill:
                get_skill = BaseSkill(**skill_store[i])
                
                if get_skill.kind == "attack":
                    self.add_attack(get_skill)
                else:
                    self.add_heal(get_skill)
                    if get_skill.kind == "boost":
                        self.boost_id = get_skill.id

                #if get_skill.kind == "heal":
                    #self.add_heal(get_skill)
                #else:
                    #self.add_attack(get_skill)
                    #if get_skill.kind == "boost":
                        #self.boost_id = get_skill.id

        def add_attack(self, attack):
            """
            Add a attack skill to the player attack skill set.

            skill: Instance of Skill.
            """
            
            self.attack_store[attack.id] = attack

        def add_heal(self, skill):
            """
            Add a heal skill to the player heal skill set.

            skill: Instance of Skill.
            """

            self.heal_store[skill.id] = skill

        def add_status(self, status_dict):
            """
            Adds a status to the fighter.

            staus_dict: Instance of Status.
            """

            # If the status can only be added randomly, find if we can add it.
            if "chance" in status_dict and "chance" > 0:
                if renpy.random.randint(0, 100) >  status_dict["chance"]:
                    return False
                #del status_dict["chance"]

            # If the status is already affecting the player, increase the turns remaining
            if status_dict["name"] in self.status_store:
                self.status_store[ status_dict["name"] ].add_turns(status_dict["turns_remaining"])

            self.status_store[ status_dict["name"] ] = Status(**status_dict)

        def use(self, skill, enemy):
            """
            Manage what the given skill will do.

            skill: Instance of Skill.
            enemy: Instance of BaseFighter. Enemy the current fighter is facing.
            """

            self.attacking = True
            self.second_last_move = self.last_move
            self.last_move = skill
            self.last_damage = 0

            if skill is None:
                battle_lines("{i}{color=#C6B483}" + self.name + "{/color}{/i}" + " tried to do something, but it failed.")
                self.no_moves = True
                
                return
            
            is_accurate = True if renpy.random.randint(0, int(self.accuracy*1.1)) < self.accuracy else False

            # If the player missed, return
            if not is_accurate:
                battle_lines("{i}{color=#C6B483}" + self.name + "{/color}{/i}" + " tried to use {i}{color=#FF7676}" + self.last_move.name + "{/color}{/i}, but it failed.")
                self.last_missed = True
                skill.pp -= 1

                return
                
            if skill.kind == "attack":
                self.hit(skill, enemy)
                
            if self.terrain == battle_terrain:
                self.last_damage = self.last_damage - (self.last_damage / 4)
                
            skill.use(self, enemy, self.last_damage)

        def hit(self, skill, enemy):
            """
            Calculates the probablity of the hit being a success and returns the total damage.

            enemy: Instance of BaseFighter. Enemy the current fighter is facing.
            """

            self.last_critical = True if renpy.random.randint(0, 100) < self.critical else False

            # Calculate by how much the enemy will reduce the attack
            blocked_by_enemy = enemy.block()

            # Calculate additional damage on enemy, based on any status the player has.
            attack_upgrade = self.get_status_effect("attack")
            attack_multiplier = random.uniform(1.1, 1.5) + (self.attack + attack_upgrade) / 100.0

            # Calculate damage on self, based on any status the player has.
            hp_change = self.get_status_effect("hp")

            # If this skill can damage hp, damage it.
            total_hp_damage = round(skill.base_hp * attack_multiplier) + blocked_by_enemy

            if total_hp_damage > 0:
                total_hp_damage = 0
            #enemy.change_hp(total_hp_damage)

            self.last_damage = total_hp_damage

        def block(self):
            """
            Calclates how much of the damage the player can block.
            """

            is_accurate = True if renpy.random.randint(0, int(self.accuracy*1.1)) < self.accuracy else False

            if not is_accurate:
                return 0

            defense_upgrade = self.get_status_effect("defense")
            defense_multiplier = 1 + (self.defense + defense_upgrade) / 100

            return renpy.random.randint(self.defense/4, self.defense*defense_multiplier)

        def change_hp(self, points, reduce=True):
            """
            Heals/Reduces HP

            points: Integer. The amount by which the HP is changed.
            """

            self.hp += normalise(self.hp, points, self.max_hp)

        def get_status_effect(self, property):
            _upgrade = 0

            for i in self.status_store.values():
                value = i.get_value(property)

                if value == "double":
                    _upgrade += self.attack
                elif value == "triple":
                    _upgrade += (self.attack * 2)
                elif value == "quadruple":
                    _upgrade += (self.attack * 3)
                elif value == "half":
                    _upgrade -= self.attack / 2
                else:
                    _upgrade += value

            return _upgrade

        def auto_fight(self, enemy):
            """
            Returns the best move to do.
            
            enemy: Instance of BaseFighter. Enemy (anyone the ai is fighting against).
            """

            self.attacking = True
            current = None

            if not self.enemy_analysed:
                probablity = 0
                self.enemy_analysed = True

                if enemy.attack - self.attack  >= 0:
                    probablity += 1
                elif self.attack / float(enemy.attack) > 0.7:
                    probablity += 0.5

                if enemy.defense - self.defense  >= 0:
                    probablity += 1
                elif self.defense / float(enemy.defense) > 0.7:
                    probablity += 0.5

                if probablity > 1:
                    current = self.do_special()

                elif probablity > 0:
                    self.power_up_in = renpy.random.randint(2, 4)

            if self.power_up_in > 0:
                self.power_up_in -= 1

                if self.power_up_in == 0:
                    current = self.do_special()

            # If Fighter hp is less than 25% of the orignal hp, heal.
            if not current:
                if self.hp / self.max_hp < 0.25 and enemy.hp / enemy.max_hp < 0.5:
                    current = self.best_heal()

            # Find out the best attack.
            if not current:
                current = self.best_attack()

            return current

        def do_special(self):
            """
            Return the special move to do
            """

            if not self.boost_id:
                return None
            #return self.attack_store[self.boost_id]
            return self.heal_store[self.boost_id]

        def best_heal(self):
            """
            Return the best possible healing spell possible based on the current need.
            """

            if not self.heal_store:
                return None

            doable_skills = []

            # Create a list of healing skills the Fighter can do
            for id, skill in self.heal_store.iteritems():
                if skill.can_do():
                    doable_skills.append(skill)

            # If no skills can be done at the current point, return
            if not doable_skills:
                return None

            # If there is only one doable skill, return it
            # Otherwse find out the skill which will heal most and return it
            if len(doable_skills) == 1:
                return doable_skills[0]
            else:
                return sorted(doable_skills, key=lambda x: x.base_hp)[0]

        def best_attack(self, filter="least pp"):
            """
            Return the best possible healing spell possible based on the current need.

            filter: Filter the attacks. Accepted values: "least pp", "best ratio"
            """
            if not self.attack_store and not self.pp:
                return None

            doable_skills = []

            # Create a list of attacks the Fighter can do
            for id, attack in self.attack_store.iteritems():
                if attack.can_do() and attack.base_hp:
                    doable_skills.append(attack)

            if not doable_skills:
                return None
                    
            # If there is only one doable skill, return it
            if len(doable_skills) == 1:
                return doable_skills[0]

            sorted_skills = sorted(doable_skills, key=lambda x: x.base_hp)
            first_pref = renpy.random.randint(0, 100)

            if self.last_move == sorted_skills[0]:
                first_pref -= 15
                if self.second_last_move == sorted_skills[0]:
                    first_pref -= 30
            elif self.second_last_move == sorted_skills[0]:
                first_pref -= 15
                if self.last_move == sorted_skills[0]:
                    first_pref -= 30

            if first_pref > 50:
                index = 0
            else:
                limit = (len(sorted_skills) - 1) * 2 - 1
                index = renpy.random.randint(1, limit)

                if index == limit:
                    index = len(sorted_skills) - 1
                else:
                    index /= 2

            return sorted_skills[index]

        def check_status(self):
            """
            Checks if a given status is still active in this turn or not.
            """

            for i in self.status_store.values():
                if not i.still_active():
                    del self.status_store[i.name]

                    continue

                # Check if the Fighter has any status which reduces hp/pp

        @property
        def get_hp(self):
            return str(self.hp) + " / " + str(int(self.max_hp))

        @property
        def can_attack(self):
            for i in self.status_store.values():
                if i.get_effect("skip"):
                    return False
            return True
