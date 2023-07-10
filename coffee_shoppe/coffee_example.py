# Program Name: Coffee Example
# Author Name: Maya Name
# Creation Date: '07/06/2023'
# Revision Date:
# Description: Create the coffee_example database

import db_utils as dbu

def main():

    DATABASE = 'coffee_shoppe\coffee_example.db'

    # Data - employee_id field will automatically create the id number as each record is added.
    emp_list = [('Maya', 'Name'), ('Sue', 'Schmitt'), ('Bob', 'Jones')]

    # Create SQL Statements
    create_table_sql = """ CREATE TABLE IF NOT EXISTS "Employees" (
                                "employee_id" INTEGER NOT NULL UNIQUE,
                                "f_name" TEXT NOT NULL,
                                "l_name" TEXT NOT NULL,
                                PRIMARY KEY("employee_id" AUTOINCREMENT));  
        """

    add_records_sql = """ INSERT INTO Employees (f_name, l_name) 
                                    VALUES(?, ?);
    
    """
    # Displays all field in table
    get_records_sql = """ SELECT * FROM Employees;
    
    """


    # Create connection to coffee database
    conn = dbu.create_connection(DATABASE)

    # Create Employees table
    dbu.create_table(conn, create_table_sql, DATABASE)

    # Add employee data to table
    dbu.add_records(conn, add_records_sql, emp_list, DATABASE)

    # Display all records in table
    all_records = dbu.get_all_records(conn, get_records_sql, DATABASE)
    print(all_records)

    # Close connection function
    dbu.close_connection(conn, DATABASE)


if __name__ == "__main__": 
    main()