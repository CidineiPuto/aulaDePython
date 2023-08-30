import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = "db.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "customers"

# connection ou con
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CRUD = Create Read   Update Delete
# SQL  = INSERT SELECT UPDATE DELETE

# CUIDADO: fazendo delete sem where
cursor.execute(f"DELETE FROM {TABLE_NAME}")

# DELETE mais cuidadoso
cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"')
connection.commit()


# Cria a tabela
cursor.execute(
    f"CREATE TABLE IF NOT EXISTS {TABLE_NAME}"
    "("
    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
    "name TEXT,"
    "weight REAL"
    ")"
)
connection.commit()


# Registrar valores nas colunas da tabela

sql = f"INSERT INTO {TABLE_NAME} (name, weight) VALUES (:name, :weight)"

# cursor.execute(sql, ["Joana", 4])
# cursor.executemany(sql, (("Joana", 4), ("Luiz", 5)))
cursor.execute(sql, {"name": "Rondinelli", "weight": 3})
cursor.executemany(
    sql,
    (
        {"name": "Jailson", "weight": 93.43},
        {"name": "Kevin", "weight": 62.50},
        {"name": "Mislene", "weight": 42.20},
        {"name": "Nonstar", "weight": 102.10},
    ),
)
connection.commit()

if __name__ == "__main__":
    print(sql)

    # DELETE
    cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE id = 3")

    cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE id = 1")
    connection.commit()

    # UPDATE
    cursor.execute(
        f'UPDATE {TABLE_NAME} SET name="Rosenilda", weight=68.98 WHERE id = 2'
    )

    # SELECT
    cursor.execute(f"SELECT * FROM {TABLE_NAME}")
    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)
    connection.commit()

    # Fecha a conexão.
    cursor.close()
    connection.close()
