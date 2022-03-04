
from weapon import Weapon


class Robot:
    def __init__(self,robot_name):
        self.robot_name = robot_name
        self.robot_health = 60
        self.equiped_weapon = Weapon('Incinerator', 30)

    def attack_dino(self,dino_to_attack):
        self.equiped_weapon -= dino_to_attack