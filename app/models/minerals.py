# Handling minerals


# Imports
from typing import Dict, Any


print("hello")

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
        self._minerals: Dict[str, Mineral] = {}