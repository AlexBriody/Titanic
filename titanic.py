# First step: Import libraries
from dotenv import load_dotenv
from os import getenv
import psycopg2
import pandas as pd

# Step 2: We will load the .env file
load_dotenv()

# Step 3: Create a class
class Titanic:
    # Step 3a: Create a user, password, server variable by accessing the .env file
    # We will keep these items as a secret under our class by using the __ method
    __user = getenv("USER")
    __password = getenv("PASSWORD")
    __server = getenv("SERVER")
    
    # Step 3b: Connect to the database:
    __pg_con = psycopg2.connect(
        dbname = __user,
        user = __user,
        password = __password,
        host = __server
    )
    
    # Step 3c: Create a cursor object:
    __cur = __pg_con.cursor()
    
    # Step 5:
    def create_tables(self, sql_filepath:str):
        # Use the static method to create a string of the sql commands we wrote earlier
        start = self.create_file(sql_filepath)
        
        # Split based off the end of our query
        tables = start.split(';')
        
        # Iterate through a  list of queries
        for table in tables:
            try:
                print(table)
                # Execute the SQL Command
                self.__cur.execute(table)
                # Commit the changes to the database
                self.__pg_con.commit()
            # Except statement to catch any errors from psycopg2
            except psycopg2.ProgrammingError as msg:
                # Print the message that we skipped over
                print(f'Command Skipped: {msg}')
    
    # Step 6: Insert data:
    def insert_data(self, sql_filepath: str):
        start = self.create_file(sql_filepath)
        data_to_insert = start.split(';')
        for insert in data_to_insert:
            try:
                print(insert)
                self.__cur.execute(insert)
                self.__pg_con.commit()
            except psycopg2.ProgrammingError as msg:
                print(f'Command Skipped: {msg}\n{insert}')

        df.to_sql('titanic', con=self.__pg_con, if_exists='append', index=False) # con=self.__pg_con ~ The connection object to the PostgreSQL database. It tells the method which database to connect to for insertion.
                                                                                 # if_exists='append' ~ If the table already exists in the database, it will add the data to the existing table without replacing it.
                                                                                 # index=False ~ Drop the dataframe index - don't include as a separate column in the database table.
        self.__pg_con.commit()
       

    # Step 7: Insert data from queries.sql directly
    def insert_queries(self, sql_filepath: str):
        start = self.create_file(sql_filepath)
        queries = start.split(';')
        for query in queries:
            try:
                print(query)
                self.__cur.execute(query)
                self.__pg_con.commit()
            except psycopg2.ProgrammingError as msg:
                print(f'Command Skipped: {msg}\n{query}')

   
    # Step 4: Create static method
    @staticmethod
    def create_file(filepath: str):
        ''' Opens a file by the filepath and apply it to a SQL Server '''
        with open(filepath, 'r') as f:
            sql_file = f.read()
        return sql_file
    

if __name__ == '__main__':
    df = pd.read_csv(/Users/alexanderbriody/Desktop/Coding Temple/Data-Analytics-Projects/Week_5/Titanic/Titanic/titanic.csv)
    c = Titanic()
    c.create_tables('/Users/alexanderbriody/Desktop/Coding Temple/Data-Analytics-Projects/Week_5/Titanic/Titanic/titanic_create.sql')
    c.insert_data('/Users/alexanderbriody/Desktop/Coding Temple/Data-Analytics-Projects/Week_5/Titanic/Titanic/titanic_insert.sql')
    c.query_data('//Users/alexanderbriody/Desktop/Coding Temple/Data-Analytics-Projects/Week_5/Titanic/Titanic/titanic_ query.sql')