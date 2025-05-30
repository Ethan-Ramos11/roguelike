from .base_character import BaseCharacter

class Mage(BaseCharacter):
    """
    Mage class - focuses on agility and magical abilities
    Specializes in spellcasting and magical combat
    """
    
    def __init__(self, name=""):
        """Initialize mage with starting stats and spell list"""
        pass

    def level_up(self):
        """Override base level_up to provide mage-specific stat growth"""
        pass

    def modify_xp_gain(self, xp):
        """Override to provide mage-specific XP bonuses/penalties"""
        pass

    def cast_spell(self, spell_name):
        """Cast a spell from the mage's available spell list"""
        pass

    def meditate(self):
        """Restore mana or gain temporary stat bonuses"""
        pass
