init python:

    import json
    
    def normalise(current, value, threshold):
        """
        Returns a integer which when added to the current will make sure it doesn't cross the threshold.

        current: Integer. Current value of the property.
        value: Integer. Value to be added to the property.
        threshold: Integer. Tha maximum value of the property.
        """

        if (current + value) > threshold:
            return threshold - current

        return value

    def bar_colour(path, value, max):
        """
        Returns the path of the bar image based on the HP

        path: String. Path to the folder containing the images.
        value: Integer. Current value.
        max: Integer. Maximum value.
        """

        _value = value / max

        if _value > 0.5:
            return path + "hp_bar_full.png"
        elif _value <= 0.5:
            return path + "hp_bar_half.png"
        elif _value <= 0.1:
            return path + "hp_bar_critical.png"

    def battle_lines(line="", append=""):
        store.gui_text.append(line)
        
    def battlestats_up():
        if battlestats_focus == "Power" and battlestats_attack_up < 4:
            global battlestats_attack_up
            battlestats_attack_up += 0.25
            
        elif battlestats_focus == "Armor" and battlestats_defense_up < 4:
            global battlestats_defense_up
            battlestats_defense_up += 0.25
            
        elif battlestats_focus == "Accuracy" and battlestats_accuracy_up < 4:
            global battlestats_accuracy_up
            battlestats_accuracy_up += 0.25
            
        elif battlestats_focus == "Critical" and battlestats_critical_up < 4:
            global battlestats_critical_up
            battlestats_critical_up += 0.25
            
        elif battlestats_focus == "Speed" and battlestats_speed_up < 4:
            global battlestats_speed_up
            battlestats_speed_up += 0.25
            
        else:
            pass
         
    def battlestats_research_check():
        global inactive_research_items, active_research_items
        global research_power1_completed, research_power1_current, research_power2_completed, research_power2_current, research_power3_completed, research_power3_current, research_power4_completed, research_power4_current, research_power5_completed, research_power5_current
        global research_armor1_completed, research_armor1_current, research_armor2_completed, research_armor2_current, research_armor3_completed, research_armor3_current, research_armor4_completed, research_armor4_current, research_armor5_completed, research_armor5_current
        global research_accuracy1_completed, research_accuracy1_current, research_accuracy2_completed, research_accuracy2_current, research_accuracy3_completed, research_accuracy3_current, research_accuracy4_completed, research_accuracy4_current
        global research_charm1_completed, research_charm1_current, research_charm2_completed, research_charm2_current, research_charm3_completed, research_charm3_current, research_charm4_completed, research_charm4_current
        global research_speed1_completed, research_speed1_current, research_speed2_completed, research_speed2_current, research_speed3_completed, research_speed3_current
        global research_power2_name, research_power3_name, research_power4_name, research_power5_name, research_armor2_name, research_armor3_name, research_armor4_name, research_armor5_name, research_accuracy2_name, research_accuracy3_name, research_accuracy4_name, research_charm2_name, research_charm3_name, research_charm4_name, research_speed2_name, research_speed3_name

        #Completed Check
        if battlestats_attack_up >= .75 and battlestats_attack_up < 1.5:
            research_power1_completed = True
            research_power2_name = research_power2_basename
            
        elif battlestats_attack_up >= 1.5 and battlestats_attack_up < 2.25:
            research_power1_completed = True
            research_power2_completed = True
            research_power2_name = research_power2_basename
            research_power3_name = research_power3_basename
            
        elif battlestats_attack_up >= 2.25 and battlestats_attack_up < 3:
            research_power1_completed = True
            research_power2_completed = True
            research_power3_completed = True
            research_power2_name = research_power2_basename
            research_power3_name = research_power3_basename
            research_power4_name = research_power4_basename
            
        elif battlestats_attack_up >= 3 and battlestats_attack_up < 3.75:
            research_power1_completed = True
            research_power2_completed = True
            research_power3_completed = True
            research_power4_completed = True
            research_power2_name = research_power2_basename
            research_power3_name = research_power3_basename
            research_power4_name = research_power4_basename
            research_power5_name = research_power5_basename
            
        elif battlestats_attack_up >= 3.75:
            research_power1_completed = True
            research_power2_completed = True
            research_power3_completed = True
            research_power4_completed = True
            research_power5_completed = True
            research_power2_name = research_power2_basename
            research_power3_name = research_power3_basename
            research_power4_name = research_power4_basename
            research_power5_name = research_power5_basename
            
            
        if battlestats_defense_up >= .75 and battlestats_defense_up < 1.5:
            research_armor1_completed = True
            research_armor2_name = research_armor2_basename
            
        elif battlestats_defense_up >= 1.5 and battlestats_defense_up < 2.25:
            research_armor1_completed = True
            research_armor2_completed = True
            research_armor2_name = research_armor2_basename
            research_armor3_name = research_armor3_basename
            
        elif battlestats_defense_up >= 2.25 and battlestats_defense_up < 3:
            research_armor1_completed = True
            research_armor2_completed = True
            research_armor3_completed = True
            research_armor2_name = research_armor2_basename
            research_armor3_name = research_armor3_basename
            research_armor4_name = research_armor4_basename
            
        elif battlestats_defense_up >= 3 and battlestats_defense_up < 3.75:
            research_armor1_completed = True
            research_armor2_completed = True
            research_armor3_completed = True
            research_armor4_completed = True
            research_armor2_name = research_armor2_basename
            research_armor3_name = research_armor3_basename
            research_armor4_name = research_armor4_basename
            research_armor5_name = research_armor5_basename
            
        elif battlestats_defense_up >= 3.75:
            research_armor1_completed = True
            research_armor2_completed = True
            research_armor3_completed = True
            research_armor4_completed = True
            research_armor5_completed = True
            research_armor2_name = research_armor2_basename
            research_armor3_name = research_armor3_basename
            research_armor4_name = research_armor4_basename
            research_armor5_name = research_armor5_basename
            
            
        if battlestats_accuracy_up >= .75 and battlestats_accuracy_up < 2.25:
            research_accuracy1_completed = True
            research_accuracy2_name = research_accuracy2_basename
            
        elif battlestats_accuracy_up >= 2.25 and battlestats_accuracy_up < 3:
            research_accuracy1_completed = True
            research_accuracy2_completed = True
            research_accuracy2_name = research_accuracy2_basename
            research_accuracy3_name = research_accuracy3_basename
            
        elif battlestats_accuracy_up >= 3 and battlestats_accuracy_up < 3.75:
            research_accuracy1_completed = True
            research_accuracy2_completed = True
            research_accuracy3_completed = True
            research_accuracy2_name = research_accuracy2_basename
            research_accuracy3_name = research_accuracy3_basename
            research_accuracy4_name = research_accuracy4_basename
            
        elif battlestats_accuracy_up >= 3.75:
            research_accuracy1_completed = True
            research_accuracy2_completed = True
            research_accuracy3_completed = True
            research_accuracy4_completed = True
            research_accuracy2_name = research_accuracy2_basename
            research_accuracy3_name = research_accuracy3_basename
            research_accuracy4_name = research_accuracy4_basename
            
            
        if battlestats_critical_up >= .75 and battlestats_critical_up < 1.5:
            research_charm1_completed = True
            research_charm2_name = research_charm2_basename
            
        elif battlestats_critical_up >= 1.5 and battlestats_critical_up < 3:
            research_charm1_completed = True
            research_charm2_completed = True
            research_charm2_name = research_charm2_basename
            research_charm3_name = research_charm3_basename
            
        elif battlestats_critical_up >= 3 and battlestats_critical_up < 3.75:
            research_charm1_completed = True
            research_charm2_completed = True
            research_charm3_completed = True
            research_charm2_name = research_charm2_basename
            research_charm3_name = research_charm3_basename
            research_charm4_name = research_charm4_basename
            
        elif battlestats_critical_up >= 3.75:
            research_charm1_completed = True
            research_charm2_completed = True
            research_charm3_completed = True
            research_charm4_completed = True
            research_charm2_name = research_charm2_basename
            research_charm3_name = research_charm3_basename
            research_charm4_name = research_charm4_basename
            
            
        if battlestats_speed_up >= .75 and battlestats_speed_up < 2.25:
            research_speed1_completed = True
            research_speed2_name = research_speed2_basename
            
        elif battlestats_speed_up >= 2.25 and battlestats_speed_up < 3.75:
            research_speed1_completed = True
            research_speed2_completed = True
            research_speed2_name = research_speed2_basename
            research_speed3_name = research_speed3_basename
            
        elif battlestats_speed_up >= 3.75:
            research_speed1_completed = True
            research_speed2_completed = True
            research_speed3_completed = True
            research_speed2_name = research_speed2_basename
            research_speed3_name = research_speed3_basename
            
        #Current Check
        research_power1_current = research_power2_current = research_power3_current = research_power4_current = research_power5_current = False
        research_armor1_current = research_armor2_current = research_armor3_current = research_armor4_current = research_armor5_current = False
        research_accuracy1_current = research_accuracy2_current = research_accuracy3_current = research_accuracy4_current = False
        research_charm1_current = research_charm2_current = research_charm3_current = research_charm4_current = False
        research_speed1_current = research_speed2_current = research_speed3_current = False
        
        if battlestats_focus == "Power":
            if battlestats_attack_up >= .75 and battlestats_attack_up < 1.5:
                research_power1_current = False
                research_power2_current = True
                active_research_items.update({
                    research_power1_name: ["research_power1_image", 270, 50, research_power1_completed, research_power1_current, research_power1_number],
                    research_power2_name: ["research_power2_researching", 270, 280, research_power2_completed, research_power2_current, research_power2_number]
                })
                
            elif battlestats_attack_up >= 1.5 and battlestats_attack_up < 2.25:
                research_power2_current = False
                research_power3_current = True
                active_research_items.update({
                    research_power2_name: ["research_power2_image", 270, 280, research_power2_completed, research_power2_current, research_power2_number],
                    research_power3_name: ["research_power3_researching", 270, 510, research_power3_completed, research_power3_current, research_power3_number]
                })
            
            elif battlestats_attack_up >= 2.25 and battlestats_attack_up < 3:
                research_power3_current = False
                research_power4_current = True
                active_research_items.update({
                    research_power3_name: ["research_power3_image", 270, 510, research_power3_completed, research_power3_current, research_power3_number],
                    research_power4_name: ["research_power4_researching", 270, 740, research_power4_completed, research_power4_current, research_power4_number]
                    })
                
            elif battlestats_attack_up >= 3 and battlestats_attack_up < 3.75:
                research_power4_current = False
                research_power5_current = True
                active_research_items.update({
                    research_power4_name: ["research_power4_image", 270, 740, research_power4_completed, research_power4_current, research_power4_number],
                    research_power5_name: ["research_power5_researching", 270, 970, research_power5_completed, research_power5_current, research_power5_number]
                })
                
            elif battlestats_attack_up >= 3.75:
                research_power5_current = False
                active_research_items.update({
                    research_power5_name: ["research_power5_image", 270, 970, research_power5_completed, research_power5_current, research_power5_number]
                })
                
            else:
                research_power1_current = True
                active_research_items.update({
                    research_power1_name: ["research_power1_researching", 270, 50, research_power1_completed, research_power1_current, research_power1_number]
                })
                
                
                
                
        elif battlestats_focus == "Armor":
            if battlestats_defense_up >= .75 and battlestats_defense_up < 1.5:
                research_armor1_current = False
                research_armor2_current = True
                active_research_items.update({
                    research_armor1_name: ["research_armor1_image", 520, 50, research_armor1_completed, research_armor1_current, research_armor1_number],
                    research_armor2_name: ["research_armor2_researching", 520, 280, research_armor2_completed, research_armor2_current, research_armor2_number]
                })
                
            elif battlestats_defense_up >= 1.5 and battlestats_defense_up < 2.25:
                research_armor2_current = False
                research_armor3_current = True
                active_research_items.update({
                    research_armor2_name: ["research_armor2_image", 520, 280, research_armor2_completed, research_armor2_current, research_armor2_number],
                    research_armor3_name: ["research_armor3_researching", 520, 510, research_armor3_completed, research_armor3_current, research_armor3_number]
                })
            
            elif battlestats_defense_up >= 2.25 and battlestats_defense_up < 3:
                research_armor3_current = False
                research_armor4_current = True
                active_research_items.update({
                    research_armor3_name: ["research_armor3_image", 520, 510, research_armor3_completed, research_armor3_current, research_armor3_number],
                    research_armor4_name: ["research_armor4_researching", 440, 970, research_armor4_completed, research_armor4_current, research_armor4_number]
                })
                
            elif battlestats_defense_up >= 3 and battlestats_defense_up < 3.75:
                research_armor4_current = False
                research_armor5_current = True
                active_research_items.update({
                    research_armor4_name: ["research_armor4_image", 520, 740, research_armor4_completed, research_armor4_current, research_armor4_number],
                    research_armor5_name: ["research_armor5_researching", 600, 970, research_armor5_completed, research_armor5_current, research_armor5_number]
                })
                
            elif battlestats_defense_up >= 3.75:
                research_armor5_current = False
                active_research_items.update({
                    research_armor5_name: ["research_armor5_image", 600, 970, research_armor5_completed, research_armor5_current, research_armor5_number]
                })
                
            else:
                research_armor1_current = True
                active_research_items.update({
                    research_armor1_name: ["research_armor1_researching", 520, 50, research_armor1_completed, research_armor1_current, research_armor1_number]
                })
                
                
                
                
        elif battlestats_focus == "Accuracy":
            if battlestats_accuracy_up >= .75 and battlestats_accuracy_up < 2.25:
                research_accuracy1_current = False
                research_accuracy2_current = True
                active_research_items.update({
                    research_accuracy1_name: ["research_accuracy1_image", 771, 50, research_accuracy1_completed, research_accuracy1_current, research_accuracy1_number],
                    research_accuracy2_name: ["research_accuracy2_researching", 771, 510, research_accuracy2_completed, research_accuracy2_current, research_accuracy2_number]
                })
                
            elif battlestats_accuracy_up >= 2.25 and battlestats_accuracy_up < 3:
                research_accuracy2_current = False
                research_accuracy3_current = True
                active_research_items.update({
                    research_accuracy2_name: ["research_accuracy2_image", 771, 510, research_accuracy2_completed, research_accuracy2_current, research_accuracy2_number],
                    research_accuracy3_name: ["research_accuracy3_researching", 771, 740, research_accuracy3_completed, research_accuracy3_current, research_accuracy3_number]
                })
            
            elif battlestats_accuracy_up >= 3 and battlestats_accuracy_up < 3.75:
                research_accuracy3_current = False
                research_accuracy4_current = True
                active_research_items.update({
                    research_accuracy3_name: ["research_accuracy3_image", 771, 740, research_accuracy3_completed, research_accuracy3_current, research_accuracy3_number],
                    research_accuracy4_name: ["research_accuracy4_researching", 771, 970, research_accuracy4_completed, research_accuracy4_current, research_accuracy4_number]
                    })
                
            elif battlestats_accuracy_up >= 3.75:
                research_accuracy4_current = False
                active_research_items.update({
                    research_accuracy4_name: ["research_accuracy4_image", 771, 970, research_accuracy4_completed, research_accuracy4_current, research_accuracy4_number]
                })
                
            else:
                research_accuracy1_current = True
                active_research_items.update({
                    research_accuracy1_name: ["research_accuracy1_researching", 771, 50, research_accuracy1_completed, research_accuracy1_current, research_accuracy1_number]
                })
                
                
                
                
        elif battlestats_focus == "Critical":
            if battlestats_critical_up >= .75 and battlestats_critical_up < 1.5:
                research_charm1_current = False
                research_charm2_current = True
                active_research_items.update({
                    research_charm1_name: ["research_charm1_image", 1023, 50, research_charm1_completed, research_charm1_current, research_charm1_number],
                    research_charm2_name: ["research_charm2_researching", 1023, 280, research_charm2_completed, research_charm2_current, research_charm2_number]
                })
                
            elif battlestats_critical_up >= 1.5 and battlestats_critical_up < 3:
                research_charm2_current = False
                research_charm3_current = True
                active_research_items.update({
                    research_charm2_name: ["research_charm2_image", 1023, 280, research_charm2_completed, research_charm2_current, research_charm2_number],
                    research_charm3_name: ["research_charm3_researching", 1023, 740, research_charm3_completed, research_charm3_current, research_charm3_number]
                })
            
            elif battlestats_critical_up >= 3 and battlestats_critical_up < 3.75:
                research_charm3_current = False
                research_charm4_current = True
                active_research_items.update({
                    research_charm3_name: ["research_charm3_image", 1023, 740, research_charm3_completed, research_charm3_current, research_charm3_number],
                    research_charm4_name: ["research_charm4_researching", 1023, 970, research_charm4_completed, research_charm4_current, research_charm4_number]
                    })
                
            elif battlestats_critical_up >= 3.75:
                research_charm4_current = False
                active_research_items.update({
                    research_charm4_name: ["research_charm4_image", 1023, 970, research_charm4_completed, research_charm4_current, research_charm4_number]
                })
                
            else:
                research_charm1_current = True
                active_research_items.update({
                    research_charm1_name: ["research_charm1_researching", 1023, 50, research_charm1_completed, research_charm1_current, research_charm1_number]
                })
                
                
                
                
        elif battlestats_focus == "Speed":
            if battlestats_speed_up >= .75 and battlestats_speed_up < 2.25:
                research_speed1_current = False
                research_speed2_current = True
                active_research_items.update({
                    research_speed1_name: ["research_speed1_image", 1276, 50, research_speed1_completed, research_speed1_current, research_speed1_number],
                    research_speed2_name: ["research_speed2_researching", 1276, 510, research_speed2_completed, research_speed2_current, research_speed2_number]
                })
                
            elif battlestats_speed_up >= 2.25 and battlestats_speed_up < 3.75:
                research_speed2_current = False
                research_speed3_current = True
                active_research_items.update({
                    research_speed2_name: ["research_speed2_image", 1276, 510, research_speed2_completed, research_speed2_current, research_speed2_number],
                    research_speed3_name: ["research_speed3_researching", 1276, 970, research_speed3_completed, research_speed3_current, research_speed3_number]
                })
                
            elif battlestats_speed_up >= 3.75:
                research_speed3_current = False
                active_research_items.update({
                    research_speed3_name: ["research_speed3_image", 1276, 970, research_speed3_completed, research_speed3_current, research_speed3_number]
                })
                
            else:
                research_speed1_current = True
                active_research_items.update({
                    research_speed1_name: ["research_speed1_researching", 1276, 50, research_speed1_completed, research_speed1_current, research_speed1_number]
                })
                
                
                
        active_research_items = {
            research_power1_name: ["research_power1_image", 270, 50, research_power1_completed, research_power1_current, research_power1_number],
            research_power2_name: ["research_power2_image", 270, 280, research_power2_completed, research_power2_current, research_power2_number],
            research_power3_name: ["research_power3_image", 270, 510, research_power3_completed, research_power3_current, research_power3_number],
            research_power4_name: ["research_power4_image", 270, 740, research_power4_completed, research_power4_current, research_power4_number],
            research_power5_name: ["research_power5_image", 270, 970, research_power5_completed, research_power5_current, research_power5_number],
            research_armor1_name: ["research_armor1_image", 520, 50, research_armor1_completed, research_armor1_current, research_armor1_number],
            research_armor2_name: ["research_armor2_image", 520, 280, research_armor2_completed, research_armor2_current, research_armor2_number],
            research_armor3_name: ["research_armor3_image", 520, 510, research_armor3_completed, research_armor3_current, research_armor3_number],
            research_armor4_name: ["research_armor4_image", 440, 970, research_armor4_completed, research_armor4_current, research_armor4_number],
            research_armor5_name: ["research_armor5_image", 600, 970, research_armor5_completed, research_armor5_current, research_armor5_number],
            research_accuracy1_name: ["research_accuracy1_image", 771, 50, research_accuracy1_completed, research_accuracy1_current, research_accuracy1_number],
            research_accuracy2_name: ["research_accuracy2_image", 771, 510, research_accuracy2_completed, research_accuracy2_current, research_accuracy2_number],
            research_accuracy3_name: ["research_accuracy3_image", 771, 740, research_accuracy3_completed, research_accuracy3_current, research_accuracy3_number],
            research_accuracy4_name: ["research_accuracy4_image", 771, 970, research_accuracy4_completed, research_accuracy4_current, research_accuracy4_number],
            research_charm1_name: ["research_charm1_image", 1023, 50, research_charm1_completed, research_charm1_current, research_charm1_number],
            research_charm2_name: ["research_charm2_image", 1023, 280, research_charm2_completed, research_charm2_current, research_charm2_number],
            research_charm3_name: ["research_charm3_image", 1023, 740, research_charm3_completed, research_charm3_current, research_charm3_number],
            research_charm4_name: ["research_charm4_image", 1023, 970, research_charm4_completed, research_charm4_current, research_charm4_number],
            research_speed1_name: ["research_speed1_image", 1276, 50, research_speed1_completed, research_speed1_current, research_speed1_number],
            research_speed2_name: ["research_speed2_image", 1276, 510, research_speed2_completed, research_speed2_current, research_speed2_number],
            research_speed3_name: ["research_speed3_image", 1276, 970, research_speed3_completed, research_speed3_current, research_speed3_number]
        }
        
        
        
    def load_data(list, sub):
        """
        Loads the required data

        list: List. A list of fighters to be loaded
        sub: String. Name of the subfolder
        """
        
        for filename in list:
            try:
                data = json.load( renpy.file("data/{}/{}.json".format(sub, filename)) )
            except IOError:
                return None

            if sub == "fighter":
                store.fighter_store[filename] = data
                
                if not data["unit"] == "enemysection" or data["unit"] != "enemyboss" and data["unit"] not in available_section:

                    data["attack"] += battlestats_attack_up
                    data["defense"] += battlestats_defense_up
                    data["accuracy"] += battlestats_accuracy_up
                    data["critical"] += battlestats_critical_up
                    data["speed"] += battlestats_speed_up
                        
                    if data["name"] == "Yamato":
                        data["level"] += int(yamato_levels)
                        available_section.append(data["unit"])
                    else:    
                        available_section.append(data["unit"])
                    
            elif sub == "skill":
                store.skill_store[filename] = data
                
    def unload_data(list, sub):
        """
        Unloads the required data - custom made to unload data
        list: List. A list of fighters to be loaded
        sub: String. Name of the subfolder
        """
        
        for filename in list:
            if sub == "fighter":
                if filename in fighter_store:
                    fighter_store.pop(filename)
                    
            elif sub == "skill":
                if filename in skill_store:
                    skill_store.pop(filename)
                    
            else:
                return None
                
    def empty_data(sub):
        """
        Empties the required data - custom made to unload data
        list: List. A list of fighters to be loaded
        sub: String. Name of the subfolder
        """
        
        list = fighter_store.keys()
        
        for filename in list:
            if sub == "fighter":
                if levelup_okay:
                    if not "enemy_" in filename:
                        fighter_store.pop(filename)
                else:
                    if not "enemy_" in filename and not "yamato_" in filename:
                        fighter_store.pop(filename)
            else:
                return None

    def show_section(barrack=None):
        _temp = {}

        if not barrack:
            return fighter_store

        for i, fighter in fighter_store.iteritems():
            if fighter["unit"] == barrack:
                _temp[i] = fighter
        return _temp

    def return_var(name):
        if name:
            return getattr(store, name)
        return None
        
    def yamato_lvlcheck():
        global levelup_okay
        global yamato_levels
        
        for fighter in player_team.store:
            if "Yamato" in fighter.name:
                levelup_okay = True
                yamato_levels +=1
        
    def yamato_unload():
        unload_data([
            "commander_yamato_heer1",
            "commander_yamato_heer2",
            "commander_yamato_heer3",
            "commander_yamato_heer4",
            "commander_yamato_heer5",
            "commander_yamato_heer6",
            "commander_yamato_heer7",
            "commander_yamato_heer8"
            ], "fighter")

    def yamato_lvlup():
        unload_data([
            "commander_yamato_heer1",
            "commander_yamato_heer2",
            "commander_yamato_heer3",
            "commander_yamato_heer4",
            "commander_yamato_heer5",
            "commander_yamato_heer6",
            "commander_yamato_heer7",
            "commander_yamato_heer8"
            ], "fighter")
        if yamato_levels <= 4:
            load_data(["commander_yamato_heer1"], "fighter")
            
        elif yamato_levels <= 8:
            load_data(["commander_yamato_heer2"], "fighter")

        elif yamato_levels <= 15:
            load_data(["commander_yamato_heer3"], "fighter")
            
        elif yamato_levels <= 23:
            load_data(["commander_yamato_heer4"], "fighter")
            
        elif yamato_levels <= 31:
            load_data(["commander_yamato_heer5"], "fighter")
            
        elif yamato_levels <= 39:
            load_data(["commander_yamato_heer6"], "fighter")
            
        elif yamato_levels <= 47:
            load_data(["commander_yamato_heer7"], "fighter")
            
        elif yamato_levels > 47:
            load_data(["commander_yamato_heer8"], "fighter")
            
        else:
            load_data(["commander_yamato_heer1"], "fighter")
            
        
            
    def return_perks(value):
        if value == "perk_firepower":
            return "battle/ui/perk_firepower.png"
        elif value == "perk_speed":
            return "battle/ui/perk_speed.png"
        elif value == "perk_explosive":
            return "battle/ui/perk_explosive.png"
        elif value == "perk_spacedarmor":
            return "battle/ui/perk_spacedarmor.png"
        elif value == "perk_slopedarmor":
            return "battle/ui/perk_slopedarmor.png"
        elif value == "perk_heal":
            return "battle/ui/perk_heal.png"
        elif value == "perk_stealth":
            return "battle/ui/perk_stealth.png"
        elif value == "perk_lightweight":
            return "battle/ui/perk_lightweight.png"
        elif value == "perk_bruteforce":
            return "battle/ui/perk_bruteforce.png"
        elif value == "perk_dark":
            return "battle/ui/perk_dark.png"
        elif value == "perk_electric":
            return "battle/ui/perk_electric.png"
        elif value == "perk_flame":
            return "battle/ui/perk_flame.png"
        elif value == "perk_ice":
            return "battle/ui/perk_ice.png"
        elif value == "perk_slash":
            return "battle/ui/perk_slash.png"
        elif value == "perk_wind":
            return "battle/ui/perk_wind.png"
        elif value == "perk_valkyrie":
            return "battle/ui/perk_valkyrie.png"
        elif value == "perk_angel":
            return "battle/ui/perk_angel.png"
        else:
            return "battle/ui/perk_blank.png"
        
    def return_skilltype(value):
        if value == "skilltype_mana":
            return "battle/ui/skilltype_mana.png"
        elif value == "skilltype_fire":
            return "battle/ui/skilltype_fire.png"
        elif value == "skilltype_ice":
            return "battle/ui/skilltype_ice.png"
        elif value == "skilltype_dark":
            return "battle/ui/skilltype_dark.png"
        elif value == "skilltype_electric":
            return "battle/ui/skilltype_electric.png"
        elif value == "skilltype_wind":
            return "battle/ui/skilltype_wind.png"
        elif value == "skilltype_ground":
            return "battle/ui/skilltype_ground.png"
        elif value == "skilltype_metal":
            return "battle/ui/skilltype_metal.png"
        elif value == "skilltype_heal":
            return "battle/ui/skilltype_heal.png"
        elif value == "skilltype_boost":
            return "battle/ui/skilltype_boost.png"
        else:
            return None
    
            
    def process_sprite_sheet(st, at, img, total_cells, column, row, cell, cell_y=0, hz=10, **useles):
        if not cell_y:
            cell_y = cell
        number = int(st*hz) % total_cells
        column, row = divmod(number, column)
        return Transform("{}".format(img), crop=(row*cell, column*cell_y, cell, cell_y)), 1.0/hz

    def damage_red(d):
        return AlphaBlend(damaged(d), blank(d), Solid("#CB3F23"), True)

    def flash_stat(d):
        return Fixed(flash_stat_trans(d), xsize=840, ysize=840)
        
    def heal_green(d):
        return AlphaBlend(glowfade(d), blank(d), Solid("#5DFF4B"), True)

    def boost_white(d):
        return AlphaBlend(glowfade(d), blank(d), Solid("#EFEFEF"), True)
        
    def death_fade(d):
        return LiveComposite((840, 840), (0, 0), deathfade(d), (0, 0), deathskulls)
        
    def launch_attack(d):
        return At(d)
        
    def anim_flip(d):
        return Fixed(At(d, flip_horizontal), xsize=840, ysize=840, xpos=-0.02)
        
    def anim_regular(d):
        return Fixed(d, xsize=840, ysize=840, xpos=0.02)
        
    def battle_start(bg, disc, dec_1=None, dec_2=None):
        game.pause_game()
        renpy.call_screen("battle_screen", bg=bg, disc=disc, dec_1=dec_1, dec_2=dec_2)
        
