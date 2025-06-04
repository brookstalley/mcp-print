from enum import Enum


class GetProductByIdSellingRegionName(str, Enum):
    ALL = "all"
    AUSTRALIA = "australia"
    BRAZIL = "brazil"
    CANADA = "canada"
    EUROPE = "europe"
    FRANCE = "france"
    GERMANY = "germany"
    ITALY = "italy"
    JAPAN = "japan"
    LATVIA = "latvia"
    NEW_ZEALAND = "new_zealand"
    NORTH_AMERICA = "north_america"
    REPUBLIC_OF_KOREA = "republic_of_korea"
    SOUTHEAST_ASIA = "southeast_asia"
    SPAIN = "spain"
    UK = "uk"
    WORLDWIDE = "worldwide"

    def __str__(self) -> str:
        return str(self.value)
