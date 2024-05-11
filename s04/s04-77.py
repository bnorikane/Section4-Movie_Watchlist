"""
# Section 4-77 Exercise

Exercise

Your company has stopped using a few software vendors, so they want you to delete them from the vendors table. However, some still have a pending delivery.

These are the vendors your company has stopped doing business with:

- Strategical.ly
- Deliver.academy

This is what the vendors table looks like:

| id  | name            | next_delivery |
| --- | --------------- | ------------- |
| 1   | Strategical.ly  | pending       |
| 2   | Techvology      | done          |
| 3   | Deliver.academy | done          |
| 4   | Software house  | pending       |
| 5   | ideasservice    | done          |

Delete the vendors that don't have a pending delivery who your company has stopped doing business with.
"""

import sqlite3

#####     create database
conn = sqlite3.Connection("ex04-77.sqlite")

# create vendors table
conn.execute("CREATE TABLE IF NOT EXISTS vendors (id INTEGER, name TEXT, next_delivery TEXT);")

# add vendor data
# insert_vendor_data = """
# INSERT INTO vendors (id, name, next_delivery)
# VALUES 
#     (1, 'Strategical.ly', 'pending'),
#     (2, 'Techvology', 'done'),
#     (3, 'Deliver.academy', 'done'),
#     (4, 'Software house', 'pending'),
#     (5, 'ideasservice', 'done');
# """
# with conn:
#     conn.execute(insert_vendor_data)

#####    Delete dropped vendors withour a pending delivery

delete_vendors = """
DELETE FROM vendors WHERE 
    name in ('Strategical.ly', 'Deliver.academy') AND next_delivery != 'pending';
"""

with conn:
    conn.execute(delete_vendors)

