# Handling minerals


# Imports
from typing import Dict, Any, List
import json 


print("hello from minerals.py\n")

class Mineral:
    """ Represents a mineral with its recommended daily amount (RDA). """

    def __init__(self, name: str, rda: float, unit: str):
        """
        Initialize a mineral instance.

        Args:
            name: Name of mineral (e.g. Calcium, Chloride)
            rda: Recommended daily amount (e.g. 200mg, 150µg)
            unit: Unit of measurement (g, mg, µg)
        """

        self.name = name
        self.rda = rda
        self.unit = unit
    

    def to_dict(self) -> Dict[str, Any]:
        """ Convert mineral to dictionary representation. """

        mineral_as_dict = {
            'name': self.name,
            'rda': self.rda,
            'unit': self.unit
        }

        return mineral_as_dict
    

    def calculate_percentage_rda(self, amount: float) -> float:
        """
        Calculate what percentage of RDA a given amount represents.
        
        Args:
            amount: Amount of mineral in the same unit as RDA.

        Returns:
            Percentage of RDA in percent.
        """

        percentage_rda = (amount / self.rda) * 100

        return percentage_rda
        


class MineralDB:
    """ Manages a collection of minerals and provides lookup functionality. """

    def __init__(self):
        """ Initialize a DB instance. The DB will contain minerals as dicts. """
        self._minerals: Dict[str, Mineral] = {}
    

    def add_mineral(self, mineral: Mineral) -> None:
        """ Add mineral do DB. """
        
        self._minerals[mineral.name] = mineral
    

    def remove_mineral(self, mineral: Mineral) -> None:
        """ Remove mineral from DB. """

        del self._minerals[mineral.name]

    
    def get_all_minerals(self) -> List[Mineral]:
        """ Get mineral by name. """

        return list(self._minerals.values())
    

    @classmethod
    def load_minerals_into_db(cls,  filepath: str) -> 'MineralDB':
        """
        Load minerals into DB from JSON file.
        
        Args:
            filepath: Path to JSON file containing mineral data.

        Returns:
            MineralDB instance.
        """

        database = cls()

        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                data = json.load(file)
                print(data)

        except FileNotFoundError:
            raise FileNotFoundError(f"Mineral data file not found: {filepath}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in file: {filepath}")
        
        return database