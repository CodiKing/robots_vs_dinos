from robot_file import Robot

class Fleet:
    def __init__(self):
        self.robot_list = []

    def create_fleet(self):
        self.robot_one = Robot('R2D2')
        self.robot_two = Robot('R.O.B')
        self.robot_three = Robot('The Iron Giant')
        self.robot_list.append(self.robot_one, self.robot_two, self.robot_three)
        print(f'Your robot team includes: {self.robot_one.robot_name}, {self.robot_two.robot_name} and {self.robot_three.robot_name}.')
