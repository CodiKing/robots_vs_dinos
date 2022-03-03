
from weapon import Weapon


class Robot:
    def __init__(self,robot_name):
        self.robot_name = robot_name
        self.robot_health = 50
        self.equiped_weapon = Weapon('Incinerator', 30)

    def attack_dino(self,dino_health,robo_weapon):
        dino_health -= robo_weapon 