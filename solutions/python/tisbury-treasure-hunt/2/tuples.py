"""Functions to help Azara and Rui locate pirate treasure."""

def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    # local, coordinate = record
    # return coordinate
    return record[1]

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
    azara_coordinate = azara_record[1] # slice azara_record

    rui_coordinate = f'{rui_record[1][0]}{rui_record[1][1]}' # join rui_coordinate

    if azara_coordinate == rui_coordinate: # compares coordinates
        return True
    return False

def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    azara_coordinate = azara_record[1] # slice azara_record

    rui_coordinate = f'{rui_record[1][0]}{rui_record[1][1]}' # join rui_coordinate

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