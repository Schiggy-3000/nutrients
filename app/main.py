# Placeholder
# Will import packages, e.g.:
# app/models/minerals.py --> import minerals
# app/models/supplements.py --> import supplements
# app/models/supplements.py --> from supplements import add_supplement


from models.nutrients import Nutrient

new_mineral = Nutrient(name="mymineral1", rda=1000, unit="mg")
new_vitamin = Nutrient(name="myvitamin1", rda=2000, unit="mg")
new_mineral_as_dict = new_mineral.to_dict()
new_mineral_perc_of_rda = new_mineral.calculate_percentage_rda(500)

print("New minearal as dict: ", new_mineral_as_dict, "\n")
print("New minearal percent of RDA: ", new_mineral_perc_of_rda, "\n")


print("#" * 100, "\n")



from models.nutrients import NutrientDB

db = NutrientDB()
db.add_nutrient(new_mineral)
db.add_nutrient(new_vitamin)

all_nutrients = db.get_all_nutrients()
for n in all_nutrients:
    print(n.name)

db.remove_nutrient(new_mineral)
all_nutrients = db.get_all_nutrients()
for n in all_nutrients:
    print(n.name)


print("#" * 100, "\n")


# Load minerals into DB from minerals.py
minerals_db = NutrientDB().load_nutrients_into_db(filepath='data/minerals.json')
all_nutrients = minerals_db.get_all_nutrients()
for n in all_nutrients:
    print(n.name, n.rda, n.unit, "---->", n.calculate_percentage_rda(100))


# Load vitamins into DB from vitamins.py
vitamins_db = NutrientDB().load_nutrients_into_db(filepath='data/vitamins.json')
all_nutrients = vitamins_db.get_all_nutrients()
for n in all_nutrients:
    print(n.name, n.rda, n.unit, "---->", n.calculate_percentage_rda(100))