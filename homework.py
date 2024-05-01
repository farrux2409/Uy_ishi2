from typing import List

import psycopg2

db_params = {
    'user': 'postgres',
    'host': 'localhost',
    'password': '123',
    'database': 'n42',
    'port': 5432
}


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


class Person:
    def __init__(self,
                 id: int | None = None,
                 full_name: str | None = None,
                 age: int | None = None,
                 email: str | None = None):
        self.id = id
        self.full_name = full_name
        self.age = age
        self.email = email

    def get_all_func(self):
        with DbConnect(db_params) as cur:
            select_query = 'select * from Person; '
            cur.execute(select_query)
            persons: List = []
            for row in cur.fetchall():
                persons.append(Person(id=row[0], full_name=row[1], age=row[2], email=row[3]))
            return persons

    def create_table_func(self):
        with DbConnect(db_params) as cur:
            create_table_query = '''create table if not exists Person
            (id serial primary key,
             full_name varchar(30) not null,
             age int not null,
             email varchar(30) not null
             );
             '''
            cur.execute(create_table_query)

    def insert_table_query(self):
        with DbConnect(db_params) as cur:
            insert_query = '''insert into Person(full_name,age,email)
            values(%s,%s,%s)'''
            insert_params = (self.full_name, self.age, self.email)
            cur.execute(insert_query,insert_params)
            print('INSERT 0 1')

    def __repr__(self):
        return f'Person({self.id} =>{self.full_name}=>{self.age},{self.email})'


print(Person().get_all_func())

person = Person(full_name='John Jons ', age=20, email='farrux123@gmail.com')
# person.create_table_func()
# person.insert_table_query()
