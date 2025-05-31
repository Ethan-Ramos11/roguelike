class BasicWand:
    def __init__(self):
        self.name = "Basic Wand"
        self.damage = 3
        self.effect = "weapon"
        self.mana_cost = 0


class SpellBook:
    def __init__(self):
        self.name = "Basic Spell Book"
        self.spells = ["Fireball"]
        self.effect = "spellbook"

    def contains_spell(self, spell_name):
        return spell_name in self.spells


