# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import os
from typing import cast

import dotenv
import pymysql
import pymysql.cursors

TABLE_NAME = "customers"
CURRENT_CURSOR_CLASS = pymysql.cursors.DictCursor

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ["MYSQL_HOST"],
    user=os.environ["MYSQL_USER"],
    password=os.environ["MYSQL_PASSWORD"],
    database=os.environ["MYSQL_DATABASE"],
    cursorclass=CURRENT_CURSOR_CLASS,
)


with connection:
    with connection.cursor() as cursor:
        cursor.execute(  # type: ignore
            "CREATE TABLE IF NOT EXISTS customers ("
            "id INT NOT NULL AUTO_INCREMENT, "
            "nome VARCHAR(50) NOT NULL, "
            "idade INT NOT NULL, "
            "PRIMARY KEY (id)"
            ") "
        )
        # CUIDADO: ISSO LIMPA A TABELA
        cursor.execute(f"TRUNCATE TABLE {TABLE_NAME}")  # type: ignore
    connection.commit()

    # Começo a manipular dados a partir daqui

    # Inserindo um valor usando placeholder e um iterável
    with connection.cursor() as cursor:
        sql = f"INSERT INTO {TABLE_NAME} (nome, idade) VALUES (%s, %s) "
        data = ("Salmo", 23)
        result = cursor.execute(sql, data)  # type: ignore
    connection.commit()

    # Inserindo um valor usando placeholder e um dicionário

    with connection.cursor() as cursor:
        sql = (
            f"INSERT INTO {TABLE_NAME} "
            "(nome, idade) "
            "VALUES (%(name)s, %(age)s) "  # Add partes do dictionary
        )
        data_dict = {
            "name": "Ruan",
            "age": 18,
        }
        result = cursor.execute(sql, data_dict)  # type: ignore
    connection.commit()

    # Inserindo vários valores usando placeholder e uma tupla de dicionários

    with connection.cursor() as cursor:
        sql = (
            f"INSERT INTO {TABLE_NAME} "
            "(nome, idade) "
            "VALUES (%(name)s, %(age)s) "  # Add partes do dictionary
        )
        data_dict2 = (
            {"name": "Letícia", "age": 27},
            {"name": "Vinícius", "age": 15},
            {"name": "Sarah", "age": 33},
            {"name": "Luiz", "age": 24},
        )

        result = cursor.executemany(sql, data_dict2)  # type: ignore
    connection.commit()

    # Inserindo vários valores usando placeholder e uma tupla de tuplas

    with connection.cursor() as cursor:
        sql = (
            f"INSERT INTO {TABLE_NAME} "
            "(nome, idade) "
            "VALUES (%s, %s) "  # Add partes do dictionary
        )
        data_touple = (
            ("Siri", 29),
            ("Maicon", 13),
            ("Jorge", 72),
            ("Anízio", 99),
        )

        result = cursor.executemany(sql, data_touple)  # type: ignore
    connection.commit()

    # Lendo os valores com select

    with connection.cursor() as cursor:
        sql = f"SELECT * FROM {TABLE_NAME} "  # select id, nome, idade
        cursor.execute(sql)  # type: ignore

        data_select = cursor.fetchall()  # type: ignore

        # for row in data_select:
        #     print(row)

    # Lendo e filtrando os valores com select

    with connection.cursor() as cursor:
        # menor_id = int(input("Digite o menor id: "))
        # maior_id = int(input("Digite o maior id: "))
        menor_id = 2
        maior_id = 4
        sql = f"SELECT * FROM {TABLE_NAME} WHERE id BETWEEN %s AND %s "

        cursor.execute(sql, (menor_id, maior_id))  # type: ignore
        # print(cursor.mogrify(sql, (menor_id, maior_id)))
        data_select = cursor.fetchall()  # type: ignore

        # for row in data_select:
        #     print(row)

    # Apagando com DELETE, WHERE e placeholders no PyMySQL

    with connection.cursor() as cursor:
        # CUIDADO com DELETE sem WHERE

        sql = f"DELETE FROM {TABLE_NAME} WHERE id = %s"

        linhas_afetadas = cursor.execute(sql, (4))  # type: ignore

        l_alteradas = f"Foram afetadas {linhas_afetadas} linhas."
        # print(l_alteradas)
        connection.commit()

        cursor.execute(f"SELECT * FROM {TABLE_NAME}")  # type: ignore

        # for row in cursor.fetchall():
        #     print(row)

    # Atualizando com UPDATE, WHERE e placeholders no PyMySQL

    with connection.cursor() as cursor:
        cursor = cast(CURRENT_CURSOR_CLASS, cursor)

        # CUIDADO com UPDATE sem WHERE

        sql = f"UPDATE {TABLE_NAME} SET nome = %s, idade = %s WHERE id = %s"

        code = cursor.execute(sql, ("Aela", 102, 2))

        cursor.execute(f"SELECT * FROM {TABLE_NAME}")

        for row in cursor.fetchall():
            print(row)

    connection.commit()
