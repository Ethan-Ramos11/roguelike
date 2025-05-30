from .base_character import BaseCharacter


class Warrior(BaseCharacter):
    """
    Warrior class - focuses on high health, strength, and defense
    Specializes in melee combat and defensive abilities
    """

    def __init__(self, name=""):
        """Initialize warrior with starting stats and equipment"""
        pass

    def level_up(self):
        """Override base level_up to provide warrior-specific stat growth"""
        pass

    def modify_xp_gain(self, xp):
        """Override to provide warrior-specific XP bonuses/penalties"""
        pass

    def special_attack(self):
        """Warrior's special melee attack ability"""
        pass

    def shield_block(self):
        """Defensive ability to block incoming damage"""
        pass
