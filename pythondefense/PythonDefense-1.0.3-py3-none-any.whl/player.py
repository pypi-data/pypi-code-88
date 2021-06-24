class Player:
    def __init__(self, health, money):
        self.health = health
        self.money = money

    def add_money(self):
        self.money = self.money + 1

    def get_money(self):
        return self.money

    def take_damage(self):
        self.health = self.health - 1

    def get_health(self):
        return self.health
