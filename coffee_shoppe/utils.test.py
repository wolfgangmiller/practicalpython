# Program Name: Database Utilities Test
# Author Name: Maya Name
# Creation Date: '07/06/2023'
# Revision Date:
# Description: Tests functions in db_utils module 

import db_utils as dbu

def main():
    # Data
    user_list = [('maya', '123', 0), ('sue', '234', 1), ('bob', '345', 2)]

    # Create SQL Statements
    create_table_sql = """ CREATE TABLE IF NOT EXISTS "Users" (
                                "user_id" TEXT NOT NULL UNIQUE PRIMARY KEY,
                                "password" TEXT NOT NULL,
                                "emp_id" INTEGER NOT NULL);  
        """

    add_records_sql = """ INSERT INTO Users (user_id, password, emp_id) 
                                    VALUES(?, ?, ?);
    
    """

    get_records_sql = """ SELECT user_id, password FROM Users
    
    """

    get_specific_record_sql = """ SELECT user_id, password FROM Users WHERE user_id=?
    
    """

    # =========== Optional Code ===============================
    # Note: I'm using the db_file.db database to test so the table name is different

    update_specific_record_sql = """ UPDATE users SET password=? WHERE user_id=?

    """

    delete_specific_record_sql = """ DELETE FROM users WHERE user_id=?
    
    """



    # Test the create connection function
    conn = dbu.create_connection('coffee_shoppe\login.db')

    # Test create table function
    dbu.create_table(conn, create_table_sql, 'coffee_shoppe\login.db')

    # Test the add records function
    dbu.add_records(conn, add_records_sql, user_list, 'coffee_shoppe\login.db')

    #  Test get all records function
    all_records = dbu.get_all_records(conn, get_records_sql, 'coffee_shoppe\login.db')
    print(all_records)

    # Test get filtered records
    filter_records = dbu.get_filtered_records(conn, get_specific_record_sql, 
                                              'bob', 'coffee_shoppe\login.db')
    print(filter_records)

    # =========================================================================
    
    # Optional: Possible solutions for Update and Delete records functions
    # Important: I recommend not testing with the login database so as not to have problems later 
    # with the point of sales application

    # values = ('789', 'bob')
    # dbu.update_specific_record(conn, update_specific_record_sql, values, 'db_file.db')

    # user_name = 'bob'
    # dbu.delete_specific_record(conn, delete_specific_record_sql, user_name, 'db_file.db')

    # =========================================================================

    # Test the close connection function
    dbu.close_connection(conn, 'coffee_shoppe\login.db')


if __name__ == "__main__": 
    main()