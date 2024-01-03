import psycopg2

hostname='localhost'
database='Fitness'
username='postgres'
pwd='2138'
port_id=5432
conn=None
cur=None
try:
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)

    cur=conn.cursor()

    create_script = '''CREATE TABLE IF NOT EXISTS users (
                        id serial PRIMARY KEY,
                        email VARCHAR(150) UNIQUE,
                        password VARCHAR(150),
                        first_name VARCHAR(150)
                    )'''

    cur.execute(create_script)

    conn.commit()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        cur.close()

