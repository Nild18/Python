import random

def randomlist_booking_object() -> list:
    # Create a random bookingObject (will not be uses in real program only for testing)
    # list_booking_object = [ObjectIndex, float length, float width, int dDateIndex, string StoreID]
    list_reglist = []
    var = ''
    for i in range(3):
        var += chr(random.randint(ord('a'), ord('z'))) 
    for i in range(3):
        var += chr(random.randint(ord('0'), ord('9')))
    list_reglist.append(var)
    var = ''
    var = round(random.uniform(3, 9), 1)
    list_reglist.append(var)
    var = ''
    var = round(random.uniform(3, 4), 1)
    list_reglist.append(var)
    list_reglist.append(random.randint(0, 3))
    list_reglist.append("OB0001")

    """path = "C:/Users/nickl/Python/Python files/bObjekts.csv"
    list_list1 = [list_reglist]
    with open(path, 'a+', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(list_list1)"""
    return list_reglist