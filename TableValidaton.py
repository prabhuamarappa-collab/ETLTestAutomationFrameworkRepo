#employees, departments, regions
import configparser

import oracledb


def table_exists(cursor,table_name,schema_name):
    query = f"select count(*) from all_tables where table_name= '{table_name.upper()}' and owner= '{schema_name.upper()}'"
    print(query)
    cursor.execute(query)
    return cursor.fetchone()[0]>0

def check_tables(tables, schemas, cursor):
    for table in tables:
        if table_exists(cursor,table,schemas):
            print(f"table '{table}' exists in schema '{schemas}'")
        else:
            print(f"table '{table}' does not exists in schema '{schemas}'")

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    username = config['database']['username']
    password = config['database']['password']
    dsn = config['database']['dsn']

    source_tables = config['tables']['source_tables'].split(',')
    target_tables = config['tables']['target_tables'].split(',')
    source_schema = config['tables']['source_schema']
    target_schema = config['tables']['target_schema']

    connection = oracledb.connect(user=username, password=password, dsn=dsn)
    cursor = connection.cursor()

    print("checking source tables:")
    check_tables(source_tables,source_schema,cursor)

    print("checking target tables:")
    check_tables(target_tables,target_schema,cursor)

    cursor.close()
    connection.close()

if __name__=="__main__":
    main()

