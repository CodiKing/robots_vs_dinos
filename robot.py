from weapon import Weapon
from dinosaur import Dinosaur

class Robot:
    def __init__(self,robot_name):
        self.robot_name = robot_name
        self.robot_health = 50
        self.equiped_weapon = Weapon()

    def attack_dino(self):
        pass