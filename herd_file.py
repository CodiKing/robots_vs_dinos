from dinosaur_file import Dinosaur

class Herd:
    def __init__(self):
        self.dino_list = []

    def create_herd(self):
        self.dinosaur_one = Dinosaur('Mr. T')
        self.dinosaur_two = Dinosaur('Godzilla')
        self.dinosaur_three = Dinosaur('Sinclair Jr.')
        self.dino_list.append(self.dinosaur_one,self.dinosaur_two, self.dinosaur_three)
        print(f'Your dinosaur team includes: {self.dinosaur_one.dino_name}, {self.dinosaur_two.dino_name} and {self.dinosaur_three.dino_name}.')
