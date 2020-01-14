import psycopg2
from WalkMart.settings import DATABASES


def call_sproc(db_name, name, parameters):
    conn = None
    cur = None
    result = None
    try:
        db_configs = DATABASES.get(db_name)
        conn_params = {
            'user': db_configs['USER'],
            'password': db_configs['PASSWORD'],
            'host': "127.0.0.1",
            'port': "5432",
            'database': db_name
        }

        conn = psycopg2.connect(**conn_params)
        cur = conn.cursor()
        cur.callproc(f'{name}', [])
        result = cur.fetchone()
    except Exception:
        print("Error while connecting to PostgreSQL")

    finally:
        if (conn):
            cur.close()
            conn.close()
    result_json = {}
    for dict in result[0]:      # Todo: Find a better way to do this.
        for k, v in dict.items():
            result_json[k] = v
    return result_json

    # use fetchone(), fetchall(),fetchmany() methods

