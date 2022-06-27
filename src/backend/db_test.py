import psycopg2

# Connect to your postgres DB
# conn = psycopg2.connect("dbname=test user=postgres")
# conn = psycopg2.connect("dbname='postgres' user='postgres' host='172.24.0.2' password='postgres' port='5432'")
conn = psycopg2.connect("dbname='postgres' user='postgres' host='db' password='postgres' port='5432'")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
# cur.execute("SELECT * FROM my_data")
# cur.execute("SELECT * FROM *")

# table_name = 'tasks_task'

def select_tables(table_name):
    return cur.execute(f"SELECT * FROM {table_name};")

def list_tables():
    cur.execute("""SELECT table_name FROM information_schema.tables
           WHERE table_schema = 'public'""")
    print("*"*20, "\n * List of tables", "\n", "*"*20)
    for table in cur.fetchall(): print(table)

# table_name = 'analyses_analyses'
table_name = 'tasks_task'
select_tables(table_name)
print(f"Records:{cur.fetchall()}")


list_tables()
# Retrieve query results
records = cur.fetchall()
print("Records:", records)