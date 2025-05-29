class BaseCharacter:
    def __init__(self, name=""):
        self.curr_health = 50
        self.max_health = 50
        self.inventory = {}
        self.alive = True
        self.name = name

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
