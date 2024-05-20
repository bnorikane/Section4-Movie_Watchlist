"""
Relational data exercise
Exercise
For this exercise I've created a db fiddle that sets up a departments table for you:

| id INTEGER PRIMARY KEY | name TEXT | department_lead TEXT |
| ---------------------- | --------- | -------------------- |


Create another table for employees that references the one I've created.

The new table should have these columns:

- id, which should be a primary key.
- first_name.
- surname.
- department_id, which should be a foreign key to the departments.id column.
"""

import sqlite3

conn = sqlite3.Connection('s04-80.sqlite')

# Create departments table
with conn:
    conn.execute("""CREATE TABLE IF NOT EXISTS departments ( 
        id INTEGER PRIMARY KEY,
        name TEXT,
        department_lead TEXT        
        );""")

# Create employees table
with conn:
    conn.execute("""CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        surname TEXT,
        department_id INTEGER,
        FOREIGN KEY (department_id) REFERENCES departments(id)
    );""")