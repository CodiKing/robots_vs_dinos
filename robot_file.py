from weapon import Weapon
from dinosaur_file import Dinosaur


class Robot:
    def __init__(self,robot_name):
        self.robot_name = robot_name
        self.robot_health = 50
        self.equiped_weapon = Weapon('Incinerator', 30)

    def attack_dino(self):
       self.equiped_weapon.attack_power -= 