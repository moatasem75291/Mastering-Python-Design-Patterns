class Wizard:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f"{self} the Wizard battels against {obstacle} and {act}!"
        print(msg)


class Ork:
    def __str__(self):
        return "an evil ork"

    def action(self):
        return "kills it"


class WizardWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return "\n\n\t------ Wizard World ------"

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()
