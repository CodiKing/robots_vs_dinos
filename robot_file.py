
from weapon import Weapon


class Robot:
    def __init__(self,robot_name):
        self.robot_name = robot_name
        self.robot_health = 60
        self.equiped_weapon = Weapon('Incinerator', 30)

    def attack_dino(self,dino_to_attack):
        dino_to_attack.health -= self.equiped_weapon.attack_power
        print(f'{dino_to_attack.dino_name} has {dino_to_attack.health} remaining')

    def __str__(self):
        return self.robot_name