import sqlite3
import os
import sys
import pandas as pd

def resource_path(relative_path):
    # Get absolute path to resource, works for dev and for PyInstaller.
    try:
        base_path = sys._MEIPASS  # Temp folder for PyInstaller
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

CHEMISTRY_LAB = resource_path("game_data.db")

def get_connection():
    # Create a connection to the SQLite database.
    return sqlite3.connect(CHEMISTRY_LAB)

def init_db():
    # Create tables if they don't exist.
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS anion (
            applicable TEXT NOT NULL,
            reaction_contents TEXT NOT NULL,
            output TEXT NOT NULL,
            stage INTEGER NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cation (
            applicable TEXT NOT NULL,
            reaction_contents TEXT NOT NULL,
            output TEXT NOT NULL,
            stage INTEGER NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS organic (
            applicable TEXT NOT NULL,
            reaction_contents TEXT NOT NULL,
            output TEXT NOT NULL,
            stage INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_anion_rection(applicable, reaction_contents, output, stage):
    # Insert a new anion reaction.
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO anion (applicable, reaction_contents, output, stage) VALUES (?, ?, ?, ?)", (applicable, reaction_contents, output, stage))
    conn.commit()
    conn.close()

def add_cation_rection(applicable, reaction_contents, output, stage):
    # Insert a new cation reaction.
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cation (applicable, reaction_contents, output, stage) VALUES (?, ?, ?, ?)", (applicable, reaction_contents, output, stage))
    conn.commit()
    conn.close()

def add_organic_rection(applicable, reaction_contents, output, stage):
    # Insert a new organic reaction.
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO organic (applicable, reaction_contents, output, stage) VALUES (?, ?, ?, ?)", (applicable, reaction_contents, output, stage))
    conn.commit()
    conn.close()

def get_anion_reactions(anion):
    # Retrieve all reaction that the given anion can do.
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT reaction_contents, output, stage from anion where applicable LIKE ? ORDER BY stage", (f"%{anion}%",))
    results = cursor.fetchall()
    conn.close()
    return results

def get_cation_reactions(cation):
    # Retrieve all reaction that the given cation can do.
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT reaction_contents, output, stage from cation where applicable LIKE ? ORDER BY stage", (f"%{cation}%",))
    results = cursor.fetchall()
    conn.close()
    return results

def get_organic_reactions(compound):
    # Retrieve all reaction that the given organic can do.
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT reaction_contents, output, stage from organic where applicable LIKE ? ORDER BY stage", (f"%{compound}%",))
    results = cursor.fetchall()
    conn.close()
    return results

def show_table(tablename):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * from {}".format(tablename))
    results = cursor.fetchall()
    conn.close()
    return results

# get_connection()
# init_db()
# flag = True
# counter = 0
# while flag:
#     counter += 1
#     print("Reaction number {}:".format(counter))
#     app, rc, out, stage = input().split()
#     stage = int(stage)
#     add_organic_rection(app, rc, out, stage)
#     flag = bool(input("Keep Going? : "))

# conn = get_connection()
# cursor = conn.cursor()
# cursor.execute("UPDATE organic SET applicable = 'o-h' where applicable = 'oh'")
# conn.commit()
# conn.close()

# df = pd.DataFrame(show_table('organic'))
# print(df)
# df = pd.DataFrame(get_cation_reactions('ni2+'))
# print(df)
# df = pd.DataFrame(get_anion_reactions('cl-'))
# print(df)
# df = pd.DataFrame(get_organic_reactions('ph'))
# print(df)