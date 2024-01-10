class Human:
    def __init__(self):
        self.name = "Joel"
        self.age = "ten"
        self.leg = "two"
        self.mouth = "eat"
        self.color = "green"

    def change_color(self, color):
        self.color = color
        notify_that = f"{self.name} best color is {self.color}"
        return notify_that
    
    def talk(self):
        talk = f"{self.name} talks a lot."
        return talk
    
    def walk(self):
        walk = f"{self.name} plays around."
        return walk