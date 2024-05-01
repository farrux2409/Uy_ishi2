import psycopg2

db_params = {
    'user': 'postgres',
    'host': 'localhost',
    'password': '123',
    'database': 'n42',
    'port': 5432
}

user: str = 'postgres'
host: str = 'localhost'
password: str = '123'
database: str = 'n42'
port: int = 5432

''' 1-version
class DbConnect:
    def __init__(self, db_params):
        self.db_params = db_params

    def __enter__(self):
        # 1-version
        # self.conn = psycopg2.connect(user=user, host=host, password=password, database=database, port=port)
        self.conn = psycopg2.connect(**self.db_params)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.commit()
            self.conn.close()


# example select all
with DbConnect(db_params) as conn:
    with conn.cursor() as cur:
        select_all_query = 'select * from books; '
        cur.execute(select_all_query)
        for rows in cur.fetchall():
            print(rows)
'''


class DbConnect:
    def __init__(self, db_params):
        self.db_params = db_params
        self.conn = psycopg2.connect(**self.db_params)

    def __enter__(self):
        self.cur = self.conn.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn and self.cur:
            self.conn.commit()
            self.conn.close()
            self.cur.close()


with DbConnect(db_params) as cur:
    select_query = 'select * from  books; '
    cur.execute(select_query)
    for rows in cur.fetchall():
        print(rows)
