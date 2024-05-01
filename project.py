import psycopg2

user: str = 'postgres'
host: str = 'localhost'
password: str = '123'
database: str = 'n42'
port: int = 5432

conn = psycopg2.connect(host=host,
                        password=password,
                        user=user,
                        database=database,
                        port=port)
cur = conn.cursor()


def create_table():
    create_table_query = '''create table  if not exists Books 
    (id serial primary key, 
    name varchar(30) not null,
    author varchar(30)) not null)'''
    cur.execute(create_table_query)
    conn.commit()
    print('successfully created')


def insert_table():
    name: str = str(input('Enter book name: '))
    author: str = str(input('Enter book author : '))
    insert_table_query = ''' insert into Books(name  , author  )
    values(%s,%s)
    '''
    insert_params = (name, author)
    cur.execute(insert_table_query, insert_params)
    conn.commit()
    print('Successfully inserted')


# insert_table()


def select_all():
    select_all_query = ''' select * from Books '''
    cur.execute(select_all_query)
    rows = cur.fetchall()
    for books in rows:
        print(books)


# select_all()

def select_one():
    select_all()
    _id: int = int(input('Enter book id : '))
    select_one_query = ''' select * from Books where id = %s'''
    cur.execute(select_one_query, (_id,))
    row = cur.fetchone()
    for book in row:
        print(book)


# select_one()


def update_table():
    select_all()
    _id: int = int(input('Enter book id: '))
    name: str = str(input('Enter book name: '))
    author: str = str(input('Enter book  author: '))
    update_table_query = ''' update Books set name = %s, author = %s where id = %s'''
    update_params = (name, author, _id)
    cur.execute(update_table_query, update_params)
    conn.commit()
    print('Successfully updated')


# update_table()


def delete_table():
    select_all()
    _id: int = int(input('Enter book id: '))
    delete_table_query = ''' delete  from Books where  id = %s;'''
    cur.execute(delete_table_query, (_id,))
    conn.commit()
    print('Successfully  deleted book')


# delete_table()

def menu():
    try:
        print('Insert book     => 1')
        print('Select all book => 2')
        print('Delete book     => 3')
        print('Select one book => 4')
        print('Update book     => 5')
        choice: int = int(input('Enter your choice: '))

    except ValueError as e:
        choice = -1

    return choice


# 1-version
# def run():
#     while True:
#         choice = menu()
#         if choice == 1:
#             insert_table()
#         elif choice == 2:
#             select_all()
#         elif choice == 3:
#             delete_table()
#         elif choice == 4:
#             select_one()
#         elif choice == 5:
#              update_table()
#         else:
#             break

def run():
    while True:
        choice = menu()
        match choice:
            case 1:
                insert_table()
            case 2:
                select_all()
            case 3:
                delete_table()
            case 4:
                select_one()
            case 5:
                update_table()
            case _:
                break

# if __name__ == "__main__":
# run()
