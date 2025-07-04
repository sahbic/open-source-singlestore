HOST_DML = 'SVC-SAS-SINGLESTORE-CLUSTER-DML'
USERDB = '<yourS2user>'
PASSDB = '<yourS2password>'

import sqlalchemy

from sqlalchemy import create_engine, text

engine = create_engine(f'singlestoredb://{USERDB}:{PASSDB}@{HOST_DML}/tpch')
conn = engine.connect()
result = conn.execute(text("SELECT COUNT(*) FROM lineitem"))
for row in result:
    print(row)

