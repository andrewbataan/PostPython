import pandas as pd
import psycopg2

# Configurar conexión
conn = psycopg2.connect(
    dbname="clientes.p",
    user="postgres",
    password="admin",
    host="localhost",
    port="5432"
)

# Ejecutar consulta y cargar en DataFrame
query = "SELECT * FROM clientes"
df = pd.read_sql(query, conn)

# Cerrar conexión
conn.close()

# Mostrar datos
print(df.head())