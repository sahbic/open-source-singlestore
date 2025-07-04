# Define a simple PROC SQL block executed implicitly by SAS:
# - Create a table in the SAS WORK library named 'example'
# - Store the count of rows from the 'tpch.customer' table
sql_code = """
proc sql;
    create table work.example as
    select count(*)
    from tpch.customer;
quit;
"""

# Submit the PROC SQL code to SAS for execution
SAS.submit(sql_code)

# Retrieve the resulting SAS table into a pandas DataFrame in Python
df = SAS.sd2df('work.example')

# Print the retrieved data
print(df)