# Handling minerals


# Imports
from typing import Dict, Any, List
import json 


print("hello from nutrients.py\n")

class Nutrient:
    """ Represents a nutrient (mineral, vitamin) with its recommended daily amount (RDA). """

    def __init__(self, nutrient_type: str, name: str, amount: int, unit: str):
        """
        Initialize a nutrient instance.

        Args:
            nutrient type: Mineral, Vitamin
            name: Name of nutrient (e.g. Calcium, Chloride)
            amount: Recommended daily amount or amount contained in supplement (e.g. 200mg, 150µg)
            unit: Unit of measurement (g, mg, µg)
        """

        self.nutrient_type = nutrient_type
        self.name = name
        self.amount = amount
        self.unit = unit
    

    def to_dict(self) -> Dict[str, Any]:
        """ Convert nutrient to dictionary representation. """

        nutrient_as_dict = {
            'nutrient_type': self.nutrient_type,
            'name': self.name,
            'amount': self.amount,
            'unit': self.unit
        }

        return nutrient_as_dict
    

    def calculate_percentage_rda(self, amount: int) -> int:
        """
        Calculate what percentage of RDA a given amount represents.
        
        Args:
            amount: Amount of nutrient in the same unit as RDA.

        Returns:
            Percentage of RDA, rounded to whole number.
        """

        if self.amount > 0:
            percentage_rda = int(round((amount / self.amount) * 100, 0))
        else:
            percentage_rda = 0

        return percentage_rda
        


class NutrientDB:
    """ Manages a collection of nutrients and provides lookup functionality. """

    def __init__(self):
        """ Initialize a DB instance. The DB will contain nutrients as dicts. """
        self._nutrients: Dict[str, Nutrient] = {}
    

    def add_nutrient(self, nutrient: Nutrient) -> None:
        """ Add nutrient do DB. """
        
        self._nutrients[nutrient.name] = nutrient
    

    def remove_nutrient(self, nutrient: Nutrient) -> None:
        """ Remove nutrient from DB. """

        del self._nutrients[nutrient.name]

    
    def get_all_nutrients(self) -> List[Nutrient]:
        """ Get nutrients as list. """

        return list(self._nutrients.values())
    

    @classmethod
    def load_nutrients_into_db(cls,  filepath: str) -> 'NutrientDB':
        """
        Load nutrients into DB from JSON file.
        
        Args:
            filepath: Path to JSON file containing nutrient data.

        Returns:
            NutrientDB instance.
        """

        database = cls()

        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            for d in data:
                nutrient_type = d['nutrient_type']
                nutrient_name = d['name']
                nutrient_amount = d['amount']
                nutrient_unit = d['unit']
                nutrient = Nutrient(nutrient_type=nutrient_type, name=nutrient_name, amount=nutrient_amount, unit=nutrient_unit)
                database.add_nutrient(nutrient)
                

        except FileNotFoundError:
            raise FileNotFoundError(f"Nutrient data file not found: {filepath}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in file: {filepath}")
        
        return database