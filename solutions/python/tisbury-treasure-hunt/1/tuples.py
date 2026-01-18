"""Functions to help Azara and Rui locate pirate treasure."""
AZARA = (
    ('Amethyst Octopus', '1F'),
    ('Angry Monkey Figurine', '5B'),
    ('Antique Glass Fishnet Float', '3D'),
    ('Brass Spyglass', '4B'),
    ('Carved Wooden Elephant', '8C'),
    ('Crystal Crab', '6A'),
    ('Glass Starfish', '6D'),
    ('Model Ship in Large Bottle', '8A'),
    ('Pirate Flag', '7F'),
    ('Robot Parrot', '1C'),
    ('Scrimshawed Whale Tooth', '2A'),
    ('Silver Seahorse', '4E'),
    ('Vintage Pirate Hat', '7E')
    )

RUI = (
    ('Seaside Cottages', ("1", "C"), 'Blue'),
    ('Aqua Lagoon (Island of Mystery)', ("1", "F"), 'Yellow'),
    ('Deserted Docks', ("2", "A"), 'Blue'),
    ('Spiky Rocks', ("3", "D"), 'Yellow'),
    ('Abandoned Lighthouse' , ("4", "B"), 'Blue'),
    ('Hidden Spring (Island of Mystery)', ("4", "E"), 'Yellow'),
    ('Stormy Breakwater', ("5", "B"), 'Purple'),
    ('Old Schooner', ("6", "A"), 'Purple'),
    ('Tangled Seaweed Patch', ("6", "D"), 'Orange'),
    ('Quiet Inlet (Island of Mystery)', ("7", "E"), 'Orange'),
    ('Windswept Hilltop (Island of Mystery)', ("7", "F"), 'Orange'),
    ('Harbor Managers Office', ("8", "A"), 'Purple'),
    ('Foggy Seacave', ("7", "E"), 'Purple')
    )

def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    local, coordinate = record
    return coordinate

def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    return tuple(list(coordinate))

def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    local, azara_coordinate = azara_record # unpack azara_record

    place, num_letter, quadrant = rui_record # unpack rui_record

    num, letter = num_letter # unpack rui_coordinate

    rui_coordinate = f'{num}{letter}' # join rui_coordinate

    if azara_coordinate == rui_coordinate: # compares coordinates
        return True
    return False

def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    local, azara_coordinate = azara_record # unpack azara_record

    place, num_letter, quadrant = rui_record # unpack rui_record

    num, letter = num_letter # unpack rui_coordinate

    rui_coordinate = f'{num}{letter}' # join rui_coordinate

    if azara_coordinate == rui_coordinate:
        return azara_record + rui_record
    return 'not a match'

def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """
    clean_hunt = []
    for group in combined_record_group:
        group_list = list(group)
        group_list.pop(1)
        group_tuple = tuple(group_list)
        clean_hunt.append(group_tuple)
    multi_line = ''
    for treasure in clean_hunt:
        string = f'{treasure}\n'
        multi_line += string
    return multi_line