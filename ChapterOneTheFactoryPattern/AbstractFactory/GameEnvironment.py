# ______________ The Abstract Factory Implementations ______________
from FrogWorld import FrogWorld
from WizardWorld import WizardWorld


class GameEnvironment:
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


def validate_age(name):
    try:
        age = int(input(f"Welcome {name}. How old are you? "))
    except ValueError as e:
        print(f"Age {e} is invalid, please try again...")
        return (False, 0)
    return (True, age)


def main():
    name = input(f"Hello. What's your name? ")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
    game = FrogWorld if age < 18 else WizardWorld
    environment = GameEnvironment(game(name))
    environment.play()


if __name__ == "__main__":
    main()
