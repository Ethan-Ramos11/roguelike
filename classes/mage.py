from .base_character import BaseCharacter


class Mage(BaseCharacter):
    """
    Mage character class that inherits from BaseCharacter.

    Mages are spellcasters who rely on magical abilities and mana to deal damage
    and support allies. They typically have high intelligence and mana but lower
    physical defense and health.
    """

    def __init__(self, name: str, level: int = 1):
        """
        Initialize a new Mage character.

        Args:
            name (str): The name of the mage
            level (int): Starting level of the mage (default: 1)
        """
        super().__init__(name)
        self.curr_health = 40
        self.max_health = 40
        self.curr_mana = 20
        self.max_mana = 20
        self.level = level

    def cast_spell(self, spell_name: str, target=None):
        """
        Cast a spell on a target or area.

        Args:
            spell_name (str): Name of the spell to cast
            target: Target for the spell (can be enemy, ally, or None for self-cast)

        Returns:
            dict: Result of the spell casting (damage dealt, healing done, etc.)
        """
        pass

    def learn_spell(self, spell_name: str):
        """
        Learn a new spell if the mage meets the requirements.

        Args:
            spell_name (str): Name of the spell to learn

        Returns:
            bool: True if spell was learned successfully, False otherwise
        """
        pass

    def meditate(self):
        """
        Restore mana through meditation.

        Returns:
            int: Amount of mana restored
        """
        pass

    def get_spell_list(self):
        """
        Get list of all known spells.

        Returns:
            list: List of spell names the mage knows
        """
        pass

    def get_mana_cost(self, spell_name: str):
        """
        Get the mana cost for a specific spell.

        Args:
            spell_name (str): Name of the spell

        Returns:
            int: Mana cost of the spell, or None if spell is unknown
        """
        pass

    def can_cast_spell(self, spell_name: str):
        """
        Check if the mage can cast a specific spell.

        Args:
            spell_name (str): Name of the spell to check

        Returns:
            bool: True if spell can be cast, False otherwise
        """
        pass

    def enchant_item(self, item, enchantment_type: str):
        """
        Enchant an item with magical properties.

        Args:
            item: Item to enchant
            enchantment_type (str): Type of enchantment to apply

        Returns:
            bool: True if enchantment was successful, False otherwise
        """
        pass

    def summon_familiar(self, familiar_type: str):
        """
        Summon a magical familiar to assist in battle.

        Args:
            familiar_type (str): Type of familiar to summon

        Returns:
            object: Familiar object if summoned successfully, None otherwise
        """
        pass

    def dispel_magic(self, target):
        """
        Remove magical effects from a target.

        Args:
            target: Target to dispel magic from

        Returns:
            bool: True if dispel was successful, False otherwise
        """
        pass

    def get_spell_power(self):
        """
        Calculate the current spell power based on stats and equipment.

        Returns:
            int: Current spell power value
        """
        pass

    def level_up(self):
        """
        Override the base level up method to include mage-specific bonuses.

        Returns:
            dict: Stats gained from leveling up
        """
        pass

    def get_character_info(self):
        """
        Get detailed information about the mage character.

        Returns:
            dict: Complete character information including spells and mana
        """
        pass
