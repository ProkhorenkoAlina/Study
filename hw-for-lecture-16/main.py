from psycopg2 import connect

conn = connect(
    dbname="air_bnb_data",
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

    cursor.execute(
        """
        SELECT g.guest_id, g.name
        FROM reservations AS r
        LEFT JOIN guests AS g ON g.guest_id = r.guest_id
        GROUP BY g.guest_id, g.name
        ORDER BY COUNT(*) DESC
        LIMIT 1;
        """
    )

    print(f"Guest with most visits: {cursor.fetchone()}")

    cursor.execute(
        """
        SELECT h.host_id, h.name, SUM(p.amount) AS money
        FROM reservations AS r
        LEFT JOIN payments AS p ON p.reservation_id = r.reservation_id
        LEFT JOIN hosts AS h ON h.host_id = r.host_id
        WHERE r.payment_status = 'Paid'
        GROUP BY h.host_id, h.name, DATE_TRUNC('month', p.payment_date)
        HAVING DATE_TRUNC('month', p.payment_date) = MAX(DATE_TRUNC('month', p.payment_date))
        ORDER BY money DESC
        LIMIT 1
        """
    )

    print(f"Host with most income in latest month: {cursor.fetchone()}")