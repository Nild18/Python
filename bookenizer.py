#   Copyright (C) 2021 by
#   Nicklas Lindroth <nicklas.lindroth@ibuildit.nu>
#   All rights reserved.
#   BSD license.

"""This is a application that take booking items and store them in
the right row dependent on the size of the item and the reachability of the row and if there
is suitable rows fore the item.
It start by finding out what row item fits. If it is the first item in this row, dateIndex
of the item is set take this items dateIndex and brands this row with this dateIndex.
Then the item is saved in the correct row. Of the item don`t fit this Warehouse the
item_row and the row_list is returned unchanged. If the item fits the row is shorten with
the items length. And item_row and the row_list is returned with the changes."""


def find_right_row(rows: list, item: list) -> int:
    """Finds the right row for the item."""
    # How many rows_list do the storageplace got
    for index, row in enumerate(rows):
        # Is it a non restricted lane or is it the same date as item date
        if row[1] or row[3] == item[3]:
            # If the lane have no set date, set it. & Do item fit row
            if row[3] == -1 and item[1] <= row[2]:
                rows[index][3] = item[3]  # Set row dateIndex
                return index
            if item[1] <= row[2]:  # Do the vehicle fit in this row
                return index
        else:
            # If the row have set dateIndex & Do the vehicle fit in this row
            if item[1] <= row[2] and row[3] == -1:
                rows[index][3] = item[3]  # Set row dateIndex
                return index
    return -1

def find_booking(item: list, rows_list: list, items_row: list) -> list:
    """Parameters
        ----------
        item : list
            [itemIndex, float length, float width, int dDateIndex, string StoreID]
        rows_list : list
            [[total_row_length:float, reachable:bool,
            row_meter_space_left:float, row_date index:int]]
        item_row : list
            [[itemIndex]]
    Returns
        -------
        rows_list : list
            [[total_row_length:float, reachable:bool,
            row_meter_space_left:float, row_date index:int]]
        items_row : list
            [itemIndex, float length, float width, int dDateIndex, string StoreID]"""

    if not items_row:  # Add rows if items_row is empty
        items_row = [[]] * len(rows_list)
    row = find_right_row(rows_list, item)  # Find suitable row
    if row == -1:  # item didn't fit
        return (rows_list, items_row)
    items_row[row].append(item[0])  # Append item to row
    rows_list[row][2] = rows_list[row][2] - item[1]  # Remove item length from row
    return (rows_list, items_row)
