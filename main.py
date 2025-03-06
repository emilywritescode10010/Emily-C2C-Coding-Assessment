
# Level 1: Returns a list of table IDs that are unoccupied
def free_tables(tables):
    f_tables = []
    for t in tables:
        if t["occupied"] == False:
            f_tables.append(t["table_id"])
    return f_tables


# Level 2: Returns the first table ID that can seat 'party_size' and is unoccupied or None if not found
def find_table_for_size(tables, party_size):
    for t in tables:
        if t["occupied"] == False and t["capacity"] >= party_size:
            return t["table_id"]
    return None


# Level 3: Returns a list of all table IDs that seat 'party_size' and are unoccupied
def find_tables_for_size(tables, party_size):
    s_tables = []
    for t in tables:
        if t["occupied"] == False and t["capacity"] >= party_size:
            s_tables.append(t["table_id"])
    return s_tables


# Returns list of table or table combinations that seat 'party_size'
def find_tables_including_combos(tables, party_size):
    table_s = []
    for t in tables:
        if t["occupied"] == False and t["capacity"] >= party_size:
            table_s.append(t["table_id"])
    return table_s


# -----------------------------------------------------------------------------
# Main / testing:

tables_data = [
    {"table_id": 1, "capacity": 2, "occupied": False, "neighbors": [2]},
    {"table_id": 2, "capacity": 4, "occupied": True,  "neighbors": [1, 3]},
    {"table_id": 3, "capacity": 2, "occupied": False, "neighbors": [2, 4]},
    {"table_id": 4, "capacity": 6, "occupied": False, "neighbors": [3]}
    ]

print("LEVEL 1: Free Tables =", free_tables(tables_data))

size = int(input("What is the size of your party? "))
print("LEVEL 2: One table for party size", size,"= Table", find_table_for_size(tables_data, size))

print("LEVEL 3: All tables for party size", size,"=", find_tables_for_size(tables_data, size))

combos = find_tables_including_combos(tables_data, 5)
print("LEVEL 4: Single or combined tables for party size", size,"=", combos)


