# Placeholder
# Will import packages, e.g.:
# app/models/minerals.py --> import minerals
# app/models/supplements.py --> import supplements
# app/models/supplements.py --> from supplements import add_supplement


from models.minerals import Mineral

new_mineral_1 = Mineral(name="mymineral1", rda=1000, unit="mg")
new_mineral_2 = Mineral(name="mymineral2", rda=2000, unit="mg")
new_mineral_as_dict = new_mineral_1.to_dict()
new_mineral_perc_of_rda = new_mineral_1.calculate_percentage_rda(500)

print("New minearal as dict: ", new_mineral_as_dict, "\n")
print("New minearal percent of RDA: ", new_mineral_perc_of_rda, "\n")



from models.minerals import MineralDB

db = MineralDB()
db.add_mineral(new_mineral_1)
db.add_mineral(new_mineral_2)

all_minerals = db.get_all_minerals()
for m in all_minerals:
    print(m.name)

db.remove_mineral(new_mineral_2)
all_minerals = db.get_all_minerals()
for m in all_minerals:
    print(m.name)


### ERROR: models/minerals.py > load_minerals_into_db(data/minerals.json)
### findet minerals.json nicht, da dieser Pfad relativ von minerals.py nicht korrekt ist.  
db2 = MineralDB().load_minerals_into_db(filepath='data/minerals.json')