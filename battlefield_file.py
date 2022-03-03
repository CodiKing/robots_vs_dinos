from fleet_file import Fleet
from herd_file import Herd

class Battlefield:
    def __init__(self,):
        self.fleet = Fleet()
        self.herd = Herd()
        

    def run_game(self):
        self.display_welcome()

    def display_welcome(self):
        print('Welcome ladies and gentlemen to the collisuem of blood and oil!')

    def battle(self):
        pass

    def dino_turn(self):
        pass

    def robo_turn(self):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass 
    