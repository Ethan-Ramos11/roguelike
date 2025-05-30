class BaseCharacter:
    def __init__(self, name=""):
        self.curr_health = 50
        self.max_health = 50
        self.inventory = {}
        self.alive = True
        self.name = name

        self.level = 1
        self.current_xp = 0
        self.strength = 10
        self.defense = 10
        self.agility = 10

    def gain_xp(self, base_xp, enemy_level=1, mult=1.0):
        xp_earned = base_xp * enemy_level * mult

        xp_earned = self.modify_xp_gain(xp_earned)
        self.current_xp += xp_earned
        self.check_level_up()
        return xp_earned

    def modify_xp_gain(self, xp):
        return xp

    def xp_required_for_next_level(self):
        return int(100 * (self.level ** 1.3))

    def check_level_up(self):
        while self.current_xp >= self.xp_required_for_next_level():
            self.current_xp -= self.xp_required_for_next_level()
            self.level_up()

    def level_up(self):
        self.level += 1
        self.max_health += 5
        self.strength += 1
        self.defense += 1
        # Heal to full on level up
        self.curr_health = self.max_health

    def take_damage(self, amount):
        self.curr_health -= amount
        if self.curr_health <= 0:
            self.curr_health = 0
            self.alive = False

    def heal(self, amount):
        if amount + self.curr_health > self.max_health:
            self.curr_health = self.max_health
            return
        self.curr_health += amount

    def is_alive(self):
        return self.alive

    def use_item(self, item):
        if item.effect == "heal":
            self.heal(item.amount)
            if self.inventory[item] > 1:
                self.inventory[item] -= 1
            else:
                del self.inventory[item]

    def add_item(self, item):
        if item in self.inventory:
            self.inventory[item] += 1
            return
        self.inventory[item] = 1
