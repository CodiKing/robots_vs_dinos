

class Dinosaur:
    def __init__(self,dino_name):
        self.dino_name = dino_name
        self.attack_power = 25
        self.health = 70

    def attack_robot(self,robo_to_attack):
        robo_to_attack.robot_health -= self.attack_power
        print(f'{robo_to_attack.robot_name} has {robo_to_attack.robot_health}')
       

    def __str__(self):
        return self.dino_name