"""
Communes attributes can be added but the str and eq methods must be changed too

"""

class Commune:
    def __init__(self, region, departement, commune):
        self.region = region
        self.departement = departement
        self.commune = commune
        self.hash = hash(region+"|"+departement+"|"+commune)

    def __eq__(self, other):
        if type(self) == type(other):
            if self.region == other.region and self.departement== other.departement and self.commune == other.commune:
                return True

        return False

    def __str__(self):
        return "{Region: \"" + str(self.region) + "\" ,  Departement: \"" + str(self.departement) + "\" , Commune: \"" + str(self.commune) + "\" }"
