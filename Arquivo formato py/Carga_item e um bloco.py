import pandas as pd
import pyodbc

# Configurações de conexão
server = 'LETICIA'  # Substitua pelo nome do servidor SQL Server
database = 'Python'  # Substitua pelo nome do banco de dados

# Criar a string de conexão
conexaoDB = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                           f'SERVER={server};'
                           f'DATABASE={database};'
                           'Trusted_Connection=yes;')

cursor = conexaoDB.cursor()

# Ler dados do Excel
file_path = r"C:\Users\Leticia\Desktop\Python-Banco de Dados\Banco de dados\Origem\arquivos_excel\items.xlsx"
dados = pd.read_excel(file_path)

# Exibir as primeiras linhas para verificação
print(dados.head())

# Garantir que a coluna total_price seja do tipo float
dados['total_price'] = dados['total_price'].astype(float)

# Inserção no banco de dados
for index, linha in dados.iterrows():
    cursor.execute("INSERT INTO [Items] (id, order_id, product_id, quantity, total_price) VALUES (?, ?, ?, ?, ?)",
                   linha['id'], linha['order_id'], linha['product_id'], linha['quantity'], linha['total_price'])

# Confirmar a transação e fechar conexões
conexaoDB.commit()
cursor.close()
conexaoDB.close()

print("Dados inseridos com sucesso!")





