HOST_DML = 'SVC-SAS-SINGLESTORE-CLUSTER-DML'
USERDB = '<yourS2user>'
PASSDB = '<yourS2password>'

import singlestoredb as s2
conn = s2.connect(host=HOST_DML, port='3306', user=USERDB, password=PASSDB, database='tpch')

with conn.cursor() as cur:
    cur.execute('SELECT COUNT(*) FROM lineitem limit 10')
    for row in cur.fetchall():
        print(row)