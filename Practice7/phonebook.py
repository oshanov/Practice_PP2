from connect import get_connection
import csv


#create table
def create_table():
    sql = '''CREATE TABLE IF NOT EXISTS contacts(
                id     SERIAL PRIMARY KEY,
                name   VARCHAR(100) UNIQUE,
                number VARCHAR(20)  UNIQUE
             );'''
    try:
        conn = get_connection()
        if conn is None:
            return
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print('Table has been created')
    except Exception as e:
        print(f'Error: {e}')
    finally:
        cur.close()
        conn.close()


#insert

def insert_console():
    sql = '''INSERT INTO contacts(name, number)
             VALUES (%s, %s)
             ON CONFLICT (name, number) DO NOTHING
             RETURNING id;'''

    name   = input('Write name: ')
    number = input('Write number: ')

    try:
        conn = get_connection()
        cur  = conn.cursor()
        cur.execute(sql, (name, number))
        conn.commit()
        print('New contact has been saved')
    except Exception as e:
        print(f'Error: {e}')
    finally:
        cur.close()
        conn.close()


def insert_csv(filepath: str):
    sql = '''INSERT INTO contacts(name, number)
             VALUES (%s, %s)
             ON CONFLICT (name, number) DO NOTHING
             RETURNING id;'''
    try:
        conn = get_connection()
        cur  = conn.cursor()
        with open(filepath, encoding='UTF-8') as f:
            reader = csv.reader(f)
            for line in reader:
                cur.execute(sql, (line[0], line[1]))
        conn.commit()
        print('Updates committed')
    except Exception as e:
        print(f'Error: {e}')
    finally:
        cur.close()
        conn.close()


#update
def update_name_by_num(number, new_name):
    sql = '''UPDATE contacts SET name = %s WHERE number = %s;'''
    try:
        conn = get_connection()
        cur  = conn.cursor()
        cur.execute(sql, (new_name, number))
        conn.commit()
        print('Name has been changed by existing number')
    except Exception as e:
        print(f'Error: {e}')
    finally:
        cur.close()
        conn.close()


def update_num_by_name(name, new_number):
    sql = '''UPDATE contacts SET number = %s WHERE name = %s;'''
    try:
        conn = get_connection()
        cur  = conn.cursor()
        cur.execute(sql, (new_number, name))
        conn.commit()
        print('Number has been changed by existing name')
    except Exception as e:
        print(f'Error: {e}')
    finally:
        cur.close()
        conn.close()

def update():
    print('-----Choose a function-----')
    print('1. Update name by phone number')
    print('2. Update phone number by name')
    n = input('1/2: ')

    if n == '1':
        number   = input('Write your phone number: ')
        new_name = input('Write your new name: ')
        update_name_by_num(number, new_name)
    elif n == '2':
        name       = input('Write your name: ')
        new_number = input('Write your new phone number: ')
        update_num_by_name(name, new_number)
    else:
        print('Incorrect')


#query
def query_data():
    sql = '''SELECT * FROM contacts WHERE name ILIKE %s'''
    try:
        conn = get_connection()
        cur  = conn.cursor()
        name = input('Write name to get the phone number: ')
        cur.execute(sql, ('%' + name + '%',))
        rows = cur.fetchall()
        if rows:
            for row in rows:
                print(f'Name: {row[1]}, phone number: {row[2]}')
        else:
            print('No contacts found')
    except Exception as e:
        print(f'Error: {e}')
    finally:
        cur.close()
        conn.close()


#delete

def delete():
    n = input('Delete by name (1) or by phone number (2): ')

    try:
        conn = get_connection()
        cur  = conn.cursor()

        if n == '1':
            name = input('Enter name: ')
            cur.execute('DELETE FROM contacts WHERE name = %s', (name,))
            print('Person deleted')
        elif n == '2':
            num = input('Enter number: ')
            cur.execute('DELETE FROM contacts WHERE number = %s', (num,))
            print('Person deleted')
        else:
            print('Incorrect choice')
            return

        conn.commit()

    except Exception as e:
        print(f'Error: {e}')
    finally:
        cur.close()
        conn.close()


#main
def main():
    create_table()
    print('\n' + '=' * 40)
    print('Welcome to main menu!')

    while True:
        print('=' * 40)
        print('1. Insert from console')
        print('2. Insert from CSV')
        print('3. Update info')
        print('4. Get info')
        print('5. Delete info')
        print('0. Exit')
        print('=' * 40)

        n = input('Enter the action: ')

        if n == '1':
            insert_console()
        elif n == '2':
            insert_csv('contacts.csv')
        elif n == '3':
            update()
        elif n == '4':
            query_data()
        elif n == '5':
            delete()
        elif n == '0':
            print('Closing the app... Goodbye!')
            break
        else:
            print('Incorrect. Try again.')


if __name__ == '__main__':
    main()