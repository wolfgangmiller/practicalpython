# Program Name: Database Utilities
# Author Name: Maya Name
# Creation Date: '07/06/2023'
# Revision Date:
# Description: Utilities for working with SQLite3

import sqlite3
from sqlite3 import Error

def create_connection(db_file:str) -> sqlite3.Connection:
    """ Description: Create a database connection to a SQLite database 
        Param: db_file - Name of database
        Return:        - Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f'Connection to {db_file} created')
        print(f'Using SQLite3 ver: {sqlite3.version}')
    except Error as e:
        conn = None
        print(e)

    return conn

def close_connection(conn:sqlite3.Connection, db_file:str) -> None:
    """ Description: Closes a database connection to a SQLite database 
        Param: conn     - connection object
        Param: db_file  - Name of database
        Return: None
    """
    if conn != None:
        # Display number of db row changes made
        print(f'Database changes: {conn.total_changes}')
        conn.close()
        print(f'Closed connection to {db_file}')
    else:
        print(f'No connection to {db_file} found')

def create_table(conn:sqlite3.Connection, sql_statement:str, 
                 db_file:str) -> None:
    """ 
    Description: Create a table from the create_table_sql statement
    Param conn:          - Connection object
    Param sql_statement: - The CREATE TABLE statement
    Param: db_file       - Name of database
    Return: - None
    """
    if conn != None:
        try:
            cur = conn.cursor()
            cur.execute(sql_statement)
        except Error as e:
            print(e)
            if conn:
                conn.rollback()
                print('Rolled back last command.')  
    else:
        print(f'No connection to {db_file} found')

def add_records(conn:sqlite3.Connection, sql_statement:str, 
                list:list[tuple], db_file:str) -> None:
    """
    Description: add record(s) to table specified in SQL statement
    Param conn:     - Connection object
    Param sql:      - SQL INSERT statement for specific table
    Param list:     - List of record(s) as tuples
    Param: db_file  - Name of database
    Return: None
    """
    if conn != None:
        try:
            cur = conn.cursor()
            cur.executemany(sql_statement, list)
            conn.commit()
        except Error as e:
            print(e)
            if conn:
                conn.rollback()
                print('Rolled back last command.')  
    else:
        print(f'No connection to {db_file} found')

def get_all_records(conn:sqlite3.Connection, sql_statement:str, db_file:str) -> list[tuple]:
    """
    Description: get record(s) from table specified in SQL statement
    Param conn:     - Connection object
    Param sql:      - SQL SELECT statement for specific table
    Param: db_file  - Name of database
    Return: List of record(s) as tuples or empty list if no records
    """
    if conn != None:
        try:
            cursor = conn.cursor() 
            cursor.execute(sql_statement)
            data = cursor.fetchall()  
            return data
        except Error as e:
            print(e)
            if conn:
                conn.rollback()
                print('Rolled back last command.') 
            return list() 
    else:
        print(f'No connection to {db_file} found')

def get_filtered_records(conn:sqlite3.Connection, sql_statement:str,
                          filter:str, db_file:str) -> list[tuple]:
    """
    Description: get record(s) from table specified in SQL statement and single filter
    Param conn:     - Connection object
    Param sql:      - SQL SELECT statement for specific table
    Param filter:   - WHERE clause filter
    Param: db_file  - Name of database
    Return: List of record(s) as tuples or empty list if no records
    """
    if conn != None:
        try:
            cursor = conn.cursor() 
            cursor.execute(sql_statement, (filter,))
            data = cursor.fetchall()  
            return data
        except Error as e:
            print(e)
            if conn:
                conn.rollback()
                print('Rolled back last command.') 
            return list() 
    else:
        print(f'No connection to {db_file} found')

# ==================== Optional Functions ========================

def update_specific_record(conn:sqlite3.Connection, sql_statement:str, 
                           values:tuple, db_file:str) ->None:
    """
    Description: updates field in record from table specified in SQL statement 
                and matches single filter
    Param conn:     - Connection object
    Param sql:      - SQL UPDATE statement for specific table
    Param value:    - SQL statement binding value(s)
    Param: db_file  - Name of database
    Return: None
    """
    if conn != None:
        try:
            cursor = conn.cursor() 
            cursor.execute(sql_statement, values)
            conn.commit()
        except Error as e:
            print(e)
            if conn:
                conn.rollback()
                print('Rolled back last command.') 
    else:
        print(f'No connection to {db_file} found')

def delete_specific_record(conn:sqlite3.Connection, sql_statement:str,
                           filter:str, db_file:str) ->None:
    """
    Description: get record(s) from table specified in SQL statement and single filter
    Param conn:     - Connection object
    Param sql:      - SQL DELETE statement for specific table
    Param filter:   - WHERE clause filter
    Param: db_file  - Name of database
    Return: None
    """
    if conn != None:
        try:
            cursor = conn.cursor() 
            cursor.execute(sql_statement, (filter, ))
            conn.commit()
        except Error as e:
            print(e)
            if conn:
                conn.rollback()
                print('Rolled back last command.') 
    else:
        print(f'No connection to {db_file} found')





