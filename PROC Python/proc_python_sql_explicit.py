# Define a SingleStore SQL query to summarize order data by year
query_sql = """
    SELECT YEAR(o_orderdate) AS order_year,
           COUNT(*) AS order_count,
           SUM(o_totalprice) AS total_spent
    FROM tpch.orders
    WHERE o_orderdate >= '1995-01-01'
    GROUP BY YEAR(o_orderdate)
"""

# Output table name where query results will be stored in SingleStore
output_table = "order_summary_proc_python"

# Build the PROC SQL block with SingleStore native SQL, executed via SAS SQL pass-through:
# - Connect to SingleStore database using SAS libname engine (cmp_dtm)
# - Drop the output table if it exists to avoid conflicts
# - Create a new table with the summarized data using the defined SQL query
# - Disconnect from the SingleStore connection
sql_code = f"""
proc sql;
   connect using cmp_dtm;
   execute(drop table IF EXISTS {output_table}) by cmp_dtm;
   execute(
       create table {output_table} as {query_sql}
   ) by cmp_dtm;
   disconnect from cmp_dtm;
quit;
"""

# Submit the PROC SQL code through SAS to run the SingleStore SQL commands
SAS.submit(sql_code)

# (Optional) Retrieve the resulting SingleStore table back into a SAS data frame in Python
# WARNING: Ensure the result set fits into available memory and container size, as large tables may cause performance issues or memory errors.
df = SAS.sd2df('cmp_dtm.order_summary_proc_python')

# Print the retrieved summarized data
print(df)