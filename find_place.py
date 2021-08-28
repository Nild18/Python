#   Copyright (C) 2021 by
#   Nicklas Lindroth <nicklas.lindroth@ibuildit.nu>
#   All rights reserved.
#   BSD license.

def find_place(rows: list, item: list, dates: list) -> list:
    
    """Function to check if this item can choose all or some dates or
    if there is no place for this item.
    
    Parameters
    ----------
    rows : list
        [[total_row_length: float, reachable: bool, 
        row_meter_space_left: float, row_date index: int]]
    item : list
        [itemIndex: str, length: float, width: float, dateIndex: int, storeID: str]
    
    Returns
    -------
    dates : list
        If thew first item in dates is -1 it means all dates are available.
    """

    removeddates = []
    appenddates = []

    for row in rows:
        if(item[{'length'}] >= row[{'spaceLeft'}]): # item don´t fit on this row
            if row[1]: # If row True
                dates.remove(rows[row[{'row_date'}]]) 
                return dates
            else:
                if (rows[row[{'row_date'}]] in removeddates) == False:
                    removeddates.append(rows[row[{'row_date'}]])
                    dates.remove(rows[row[{'row_date'}]])
                else:
                    if (rows[row[{'row_date'}]] in appenddates) == False:
                        appenddates.append(rows[row[{'row_date'}]])
                        dates.append(rows[row[{'row_date'}]])                
    return dates
     