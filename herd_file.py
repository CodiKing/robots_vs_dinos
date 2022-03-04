from dinosaur_file import Dinosaur

class Herd:
    def __init__(self):
        self.dino_list = []
        self.create_herd()

    def create_herd(self):
        self.dinosaur_one = Dinosaur('Mr. T')
        self.dino_list.append(self.dinosaur_one.dino_name)
        self.dinosaur_two = Dinosaur('Godzilla')
        self.dino_list.append(self.dinosaur_two.dino_name)
        self.dinosaur_three = Dinosaur('Sinclair Jr.')
        self.dino_list.append(self.dinosaur_three.dino_name)
        
