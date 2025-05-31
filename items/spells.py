from ..classes.base_character import BaseCharacter
import random


class BaseSpell:
    def __init__(self):
        self.name = ""
        self.damage = 0
        self.mana_cost = 0
        self.description = ""

    def cast(self, caster, target=None):
        """Main spell casting logic - override in subclasses"""
        if not self.can_cast(caster):
            return False

        caster.curr_mana -= self.mana_cost

        return True

    def can_cast(self, caster: BaseCharacter):
        """Check if caster has enough mana"""
        return self.mana_cost <= caster.curr_mana

    def roll_effect(self, chance):
        return random.randint(1, 100) <= chance


class Fireball(BaseSpell):
    def __init__(self):
        super().__init__()
        self.name = "Fireball"
        self.damage = 12
        self.mana_cost = 8
        self.effect = "damage_spell"
        self.description = "Classic fire spell with a 60% chance of burn"
        self.status = {
            "name": "burn",
            "chance": 60,
            "turns": 2,
            "damage": 3
        }

    def cast(self, caster, target):
        if not self.can_cast(caster):
            return False

        caster.curr_mana -= self.mana_cost

        target.take_damage(self.damage)

        if self.roll_effect(self.status["chance"]):
            self.do_status(target)

        return True

    def do_status(self, target):
        if target.applied_status == {}:
            target.applied_status = self.status.copy()

