############
# Part 1   #
############

class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, name, first_harvest, color, is_seedless, is_bestseller = None):
        """Initialize a melon."""
        self.code = code
        self.name = name
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.pairings = []


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.extend([pairing])

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""
    
    all_melon_types = []

    musk = MelonType("musk", "Muskmelon", 1998, "green", True, True)
    musk.add_pairing("mint")

    casaba = MelonType('cas', "Casaba", 2003, "orange", False, False)
    casaba.add_pairing("strawberries, mint")

    crenshaw = MelonType('cren', "Crenshaw", 1996, 'green', False, False)
    crenshaw.add_pairing("proscuitto")

    yellow_watermelon = MelonType('yw', "Yellow Watermelon", 2013, 'yellow', False, True)
    yellow_watermelon.add_pairing("ice cream")

    all_melon_types.extend([musk, casaba, crenshaw, yellow_watermelon])

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for type in melon_types:
        print(f"{type.name} pairs well with:")
        print(f" -- {type.pairings}")

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_dict = {}

    for type in melon_types:
        melon_dict[type.code] = type.name

    return melon_dict


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, type, shape_rating, color_rating, harvest_location, harvest_person):
        self.type = type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvest_location = harvest_location
        self.harvest_person = harvest_person

    def is_sellable(self):
        if self.color_rating > 5 and self.shape_rating > 5 and self.harvest_location != 3:
            return True
        return False
        

def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melon_list = []
    melons_by_code = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melons_by_code["yw"], 8, 7, 2, "Sheila")
    melon_2 = Melon(melons_by_code["yw"], 3, 4, 2, "Sheila")
    melon_3 = Melon(melons_by_code["yw"], 9, 8, 3,'Sheila')

    melon_list.extend([melon_1, melon_2, melon_3])

    return melon_list

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        print(f"Harvested by {melon.harvest_person} from Field {melon.harvest_location}")


