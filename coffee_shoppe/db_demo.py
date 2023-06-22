import sqlite3



def main():
    print('Database Demo')

    # Data
    user_data_1 = ('maya', '123', 0)
    user_list = [('sue', '234', 1), ('bob', '345', 2)]

    user_name = 'bob'

    # Create SQL Statements
    create_table_sql = """ CREATE TABLE IF NOT EXISTS "users" (
                                "user_id" TEXT NOT NULL UNIQUE PRIMARY KEY,
                                "password" TEXT NOT NULL,
                                "emp_id" INTEGER NOT NULL);  
    """

    add_one_record_sql = """ INSERT INTO users (user_id, password, emp_id)
                                    VALUES(?, ?, ?);
    
    """

    add_many_records_sql = """ INSERT INTO users (user_id, password, emp_id) 
                                    VALUES(?, ?, ?);
    
    """

    get_records_sql = """ SELECT user_id, password FROM users
    
    """

    get_specific_record = """ SELECT user_id, password FROM users WHERE user_id=?
    
    """

    # Establish database connection
    conn = sqlite3.connect('./coffee_shoppe/db_file.db')

    # Create cursor to execute SQL commands
    cur = conn.cursor()

    # Execute SQL commands
    cur.execute(create_table_sql)

    # cur.execute(add_one_record_sql, user_data_1)
    # cur.executemany(add_many_records_sql, user_list)

    # Commits inserted data to table
    # conn.commit()

    # cur.execute(get_records_sql)
    # cur.execute(get_specific_record, (user_name,))

    # records = cur.fetchall()

    # for record in records:
    #     print(record)

    # Close database connection
    conn.close()

if __name__ == "__main__": 
    main()