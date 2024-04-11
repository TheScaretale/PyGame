class Player:
    def __init__(self):
        self.hp = 30
        self.level = 1
        self.strength = 1
        self.intel = 1
        self.vigor = 1
        self.faith = 1
        self.xp = 0
        self.xpNeeded = 100

    def gainXP(self, amount):
        self.xp += amount
        if self.xp >= self.xpNeeded:
            self.levelUp()

    def levelUp(self):
        self.level += 1
        self.xp -=  self.xpNeeded
        self.xpNeeded *= 2
        self.hp = int(self.hp*1.3)

    def attack(self):
        danoBase = 10
        danoTotal = danoBase + (self.strength* 1.8)
        return danoTotal