from psycopg2 import connect

conn = connect(
    dbname="study_managment",
    host="db",
    port=5432,
    user="admin",
    password="password"
)

ddl = open("ddl.sql")
dml = open("dml.sql")

with conn.cursor() as cursor:
    for ddl_query in ddl.read().split(';'):
        if not ddl_query:
            continue
        print(ddl_query)
        cursor.execute(ddl_query)
    for dml_query in dml.read().split(';'):
        if not dml_query:
            continue
        print(dml_query)
        cursor.execute(dml_query)

    print(f"{'-'*10} Setup is finished. {'-'*10}")
