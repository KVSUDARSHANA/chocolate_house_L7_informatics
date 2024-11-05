import sqlite3

# Establish a connection to the database
def connect_db():
    conn = sqlite3.connect('chocolate_house.db')
    return conn

# Create tables for SeasonalFlavors, IngredientInventory, and CustomerSuggestions
def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS SeasonalFlavors (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      flavor_name TEXT NOT NULL,
                      description TEXT,
                      season TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS IngredientInventory (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      ingredient_name TEXT NOT NULL,
                      quantity INTEGER,
                      unit TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS CustomerSuggestions (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      customer_name TEXT,
                      suggested_flavor TEXT,
                      allergy_concern TEXT)''')
    conn.commit()

# Abstraction functions for each CRUD operation
def add_seasonal_flavor(conn, flavor_name, description, season):
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO SeasonalFlavors (flavor_name, description, season)
                      VALUES (?, ?, ?)''', (flavor_name, description, season))
    conn.commit()

def add_ingredient(conn, ingredient_name, quantity, unit):
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO IngredientInventory (ingredient_name, quantity, unit)
                      VALUES (?, ?, ?)''', (ingredient_name, quantity, unit))
    conn.commit()

def add_customer_suggestion(conn, customer_name, suggested_flavor, allergy_concern):
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO CustomerSuggestions (customer_name, suggested_flavor, allergy_concern)
                      VALUES (?, ?, ?)''', (customer_name, suggested_flavor, allergy_concern))
    conn.commit()

def view_seasonal_flavors(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM SeasonalFlavors")
    return cursor.fetchall()

def view_ingredients(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM IngredientInventory")
    return cursor.fetchall()

def view_customer_suggestions(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM CustomerSuggestions")
    return cursor.fetchall()
