import pandas as pd
import psycopg2

from pipeline.config import host, db_name, user, password

try:
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
    )

    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT version();'
        )

        print(cursor.fetchone())
except Exception as _ex:
    pass
finally:
    pass