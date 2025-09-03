import snowflake.connector
import os

# Connect to Snowflake using GitHub Secrets stored in ENV variables
conn = snowflake.connector.connect(
    user=os.environ['SNOWFLAKE_USER'],
    password=os.environ['SNOWFLAKE_PASSWORD'],
    account=os.environ['SNOWFLAKE_ACCOUNT'],
    warehouse=os.environ['SNOWFLAKE_WAREHOUSE'],
    database=os.environ['SNOWFLAKE_DATABASE'],
    schema=os.environ['SNOWFLAKE_SCHEMA'],
    role=os.environ['SNOWFLAKE_ROLE']
)

cursor = conn.cursor()

# Read and execute the SQL file
with open('sql/create_table.sql', 'r') as file:
    sql_script = file.read()

# Execute each statement
for statement in sql_script.strip().split(';'):
    if statement.strip():
        cursor.execute(statement)

print("✅ Table created in Snowflake.")
cursor.close()
conn.close()

