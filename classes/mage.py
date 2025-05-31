from .base_character import BaseCharacter
from ..items.weapons import SpellBook, BasicWand


class Mage(BaseCharacter):
    """
    Mage class - focuses on agility and magical abilities
    Specializes in spellcasting and magical combat
    """

    def __init__(self, name=""):
        """Initialize mage with starting stats and spell list"""
        super().__init__(name)
        self.curr_health = 40
        self.max_health = 40
        self.curr_mana = 20
        self.max_mana = 20

        self.strength = 4
        self.defense = 8
        self.agility = 12
        self.wand = BasicWand()
        self.spellbook = SpellBook()

        self.add_item(self.wand)
        self.add_item(self.spellbook)

    def level_up(self):
        """Override base level_up to provide mage-specific stat growth"""
        self.level += 1
        self.max_health += 5
        self.strength += 1
        self.defense += 1
        self.max_mana += 2
        self.curr_health = self.max_health

    def modify_xp_gain(self, xp, source="combat"):
        """Override to provide mage-specific XP bonuses/penalties"""
        if source == "spell_kill":
            return int(xp * 1.25)
        elif source == "combat":
            return int(xp * 1.1)
        return xp

    def cast_spell(self, spell_name):
        """Cast a spell from the mage's available spell list"""
        

    def meditate(self):
        """Restore mana or gain temporary stat bonuses"""
        pass
