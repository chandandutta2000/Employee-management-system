import sqlite3

def create_table():
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()

    cursor.execute('''
        create table if not exists Employees(
           Id number primary key,
           Name text(50),
           Role text(50),
           Gender text(20),
           Status text(20))''')
    conn.commit()
    conn.close()

def fetch_employees():
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute('select * from Employees')
    employees = cursor.fetchall()
    conn.close()
    return employees

def insert_employees(Id,Name,Role,Gender,Status):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute('insert into Employees(Id,Name,Role,Gender,Status) values (?, ?, ?, ?, ?)',
                (Id, Name, Role, Gender, Status))
    conn.commit()
    conn.close()

def delete_employees(Id):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute('delete from Employees where id = ?', (Id,),)
    conn.commit()
    conn.close()
def update_employees(new_name,new_role,new_gender,new_status,id):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute("update Employees set Name=?, Role=?, Gender = ?, Status = ? where Id = ?", (new_name, new_role, new_gender, new_status, id))
    conn.commit()
    conn.close()

def id_exists(Id):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute('select count(*) from Employees where Id=?', (Id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0

create_table()








