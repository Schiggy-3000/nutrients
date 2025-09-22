# Placeholder
# Will import packages, e.g.:
# app/models/minerals.py --> import minerals
# app/models/supplements.py --> import supplements
# app/models/supplements.py --> from supplements import add_supplement


from models.nutrients import Nutrient

new_mineral = Nutrient(nutrient_type="Mineral", name="mymineral1", amount=1000, unit="mg")
new_vitamin = Nutrient(nutrient_type="Vitamin", name="myvitamin1", amount=2000, unit="mg")
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



print("Nutrients ", "#" * 100, "\n")

# Load vitamins into DB from vitamins.py
nutrients_db = NutrientDB().load_nutrients_into_db(filepath='data/nutrients.json')
all_nutrients = nutrients_db.get_all_nutrients()
for n in all_nutrients:
    print(n.nutrient_type, n.name, n.amount, n.unit, "---->", n.calculate_percentage_rda(100))


print("AG1 ", "#" * 100, "\n")

# Load vitamins into DB from vitamins.py
ag1_db = NutrientDB().load_nutrients_into_db(filepath='data/supplement_ag1.json')
all_nutrients = ag1_db.get_all_nutrients()
for n in all_nutrients:
    print(n.nutrient_type, n.name, n.amount, n.unit, "---->", n.calculate_percentage_rda(100))