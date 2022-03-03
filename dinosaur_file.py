from robot_file import Robot

class Dinosaur:
    def __init__(self,dino_name):
        self.dino_name = dino_name
        self.attack_power = 25
        self.health = 70

    def attack_robot(self,robo_health, dino_attack_power):
        self.robo_leftover_hp = robo_health - dino_attack_power