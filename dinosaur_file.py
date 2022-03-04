from robot_file import Robot

class Dinosaur:
    def __init__(self,dino_name):
        self.dino_name = dino_name
        self.attack_power = 25
        self.health = 70

    def attack_robot(self,robo_to_attack):
        self.attack_power -= robo_to_attack