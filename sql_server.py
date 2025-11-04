import pyodbc

driver = "SQL Server"
server = "de-nss-bootcamp.database.windows.net"
port = 1433
database = "de_bootcamp"
username = "devadmin"
password = "Bootcamp1433!"

sql_server_conn_string = (
    f"DRIVER={{{driver}}};"
    f"SERVER={server},{port};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    f"Encrypt=no;"
    f"TrustServerCertificate=yes;"
)

conn = pyodbc.connect(sql_server_conn_string)
print("Connected to SQL server!")