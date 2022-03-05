from fleet_file import Fleet
from herd_file import Herd

class Battlefield:
    def __init__(self,):
        self.fleet = Fleet()
        self.herd = Herd()
    
    def run_game(self):
        self.display_welcome()
        self.battle()
        self.display_winners()
    def display_welcome(self):
        print('Welcome ladies and gentlemen to the collisuem of blood and oil!')
        # print('Choose your champions!')
        # self.users_team_choice = input('Would you like to fight with the robots or the dinosaurs?: ')
        # if self.users_team_choice == 'robots':
        #     print(f'Your robot team includes: {self.fleet.robot_one.robot_name}, {self.fleet.robot_two.robot_name} and {self.fleet.robot_three.robot_name}.')
        # elif self.users_team_choice == 'dinosaurs':
        #     print(f'Your dinosaur team includes: {self.herd.dinosaur_one.dino_name}, {self.herd.dinosaur_two.dino_name} and {self.herd.dinosaur_three.dino_name}.')
        # else:
        #     print('Oops! Lets choose again.')
        #     self.users_team_choice = print('Would you like to fight with the robots or the dinosaurs?: ')

    def battle(self):
        while len(self.fleet.robot_list) > 0 and len(self.herd.dino_list) > 0:
            self.show_robo_opponent_options()
            self.show_dino_opponent_options()
            # if self.users_team_choice =='robots':
            #     self.show_robo_opponent_options()
            # elif self.users_team_choice == 'dinosaurs':
            #     self.show_dino_opponent_options()

    def dino_turn(self,dinosaur_turn):
        pass

    def robo_turn(self):
        pass

    def show_dino_opponent_options(self):
        self.attacking = input(f'Who would you like to attack with{self.herd.dino_list}: ')
        self.defending = input(f'Who would you like to attack{self.fleet.robot_list}: ')
        if self.defending == 'R2D2':
            self.defending = self.fleet.robot_one
        elif self.defending == 'R.O.B':
            self.defending = self.fleet.robot_two
        elif self.defending =='The Iron Giant':
            self.defending == self.fleet.robot_three
        if self.attacking == 'Mr. T':
            self.herd.dinosaur_one.attack_robot(self.defending)
        elif self.attacking == 'Godzilla':
            self.herd.dinosaur_two.attack_robot(self.defending)
        elif self.attacking == 'Sinclair Jr.':
            self.herd.dinosaur_three.attack_robot(self.defending)
        else:
            print('We didnt recognize those. please type the names exactly as you see them.')
            self.attacking = input(f'Who would you like to attack with{self.herd.dino_list}: ')
            self.defending = input(f'Who would you like to attack{self.fleet.robot_list}: ')
        if self.defending.robot_health <= 0:
            self.fleet.robot_list.remove(self.defending.robot_name)
        

    def show_robo_opponent_options(self):
        self.attacking = input(f'Who would you like to attack with{self.fleet.robot_list}: ')
        self.defending = input(f'Who would you like to attack{self.herd.dino_list}: ')
        if self.defending == 'Mr. T':
            self.defending = self.herd.dinosaur_one
        elif self.defending == 'Godzilla':
            self.defending = self.herd.dinosaur_two
        elif self.defending =='Sinclair Jr.':
            self.defending == self.herd.dinosaur_three
            self.fleet.robot_one.attack_dino(self.defending)
        if self.attacking == 'R.O.B':
            self.fleet.robot_two.attack_dino(self.defending)
        elif self.attacking == 'The Iron Giant':
            self.fleet.robot_three.attack_dino(self.defending)
        elif self.attacking == 'R2D2':
            self.fleet.robot_one.attack_dino(self.defending)
        else:
            print('We didnt recognize those. please type the names exactly as you see them.')
            self.attacking = input(f'Who would you like to attack with{self.fleet.robot_list}: ')
            self.defending = input(f'Who would you like to attack{self.herd.dino_list}: ')
        if self.defending.health <= 0:
            self.herd.dino_list.remove(self.defending.dino_name)
    def display_winners(self):
        if len(self.fleet.robot_list) == 0:
            print ('The dinosaurs have won! Looks like they will be ruling these lands a little longer.')
        if len(self.herd.dino_list) == 0:
            print('The robots have won! Hopefully Skynet isnt in these robots code...')