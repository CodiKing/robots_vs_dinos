from battlefield_file import Battlefield
from fleet_file import Fleet
from herd_file import Herd



fleet_one = Fleet()
fleet_one.create_fleet()
print()
herd_one = Herd()
herd_one.create_herd()
fleet_one.robot_one.attack_dino(herd_one.dinosaur_one.health,fleet_one.robot_one.equiped_weapon.attack_power)
herd_one.dinosaur_one.attack_robot(fleet_one.robot_one.robot_health,herd_one.dinosaur_one.attack_power)
print(fleet_one.robot_one.robot_health)