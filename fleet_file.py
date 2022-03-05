from robot_file import Robot

class Fleet:
    def __init__(self):
        self.robot_list = []
        self.create_fleet()
        self.fleets_health = [self.robot_one.robot_health,self.robot_two.robot_health,self.robot_three.robot_health]
    def create_fleet(self):
        self.robot_one = Robot('R2D2')
        self.robot_list.append(self.robot_one.robot_name)
        self.robot_two = Robot('R.O.B')
        self.robot_list.append(self.robot_two.robot_name)
        self.robot_three = Robot('The Iron Giant')
        self.robot_list.append(self.robot_three.robot_name)

    
        
