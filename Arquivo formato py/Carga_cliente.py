# %%
"""
create table Clientes(
id			int,
created_at datetime,
first_name nvarchar(255),
last_name  nvarchar(255),
email nvarchar(255),
cell_phone nvarchar(255),
country nvarchar(255),
state nvarchar(255),
street nvarchar(255),
number  nvarchar(255),
additionals  nvarchar(255)
)

"""

# %%

import pandas as pd
import pyodbc 

server = 'LETICIA' # Substitua pelo nome do servidor SQL Server
database = 'Python'  # Substitua pelo nome do banco de dados
conexaoDB = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      f'SERVER={server};'
                      f'DATABASE={database};'
                      'Trusted_Connection=yes;'
                      #'charset=UTF-16'
                      
                      )

cursor = conexaoDB.cursor()   # criando cursor de comando 

# %%
dados = pd.read_csv(r"C:\Users\Leticia\Desktop\Python-Banco de Dados\Banco de dados\Origem\arquivos_csv\Clientes.csv",delimiter=',')
#str(dados.columns).replace("'","") 
dados.head(5)


# %%
for coluna in dados.columns:
    print(f"Coluna: {coluna}, Tipo de dados: {dados[coluna].dtypes}")

# %%
# Converter a coluna 'created_at' para o formato de data e hora
dados['created_at'] = pd.to_datetime(dados['created_at'])
dados['email'] = dados['email'].fillna('Sem registro') # para colocar dados na coluna vazia, com null
dados['street'] = dados['street'].fillna('Sem Info')# para colocar dados na coluna vazia, com null
dados['number'] = dados['number'].fillna('Sem Numero')# para colocar dados na coluna vazia, com null
dados['additionals'] = dados['additionals'].fillna('Sem Info')# para colocar dados na coluna vazia, com null


# %%
for coluna in dados.columns:
    print(f"Coluna: {coluna}, Tipo de dados: {dados[coluna].dtypes}")

# %% [markdown]
# 

# %%
str(dados.columns).replace("'","")  # coluna de origem 

# %%
cursor.execute('truncate table  [Clientes]')   #executa tarefa de  apagar dados
cursor.commit()

# %%
dados

# %%
# import pyodbc
# import pandas as pd

# # Supondo que 'dados' é um DataFrame do pandas contendo os dados a serem inseridos
# # Supondo que você já tenha uma conexão aberta com o SQL Server
# # conexaoDB = pyodbc.connect('sua conexão aqui')

# cursor = conexaoDB.cursor()

# try:
#     for index, linha in dados.iterrows():
#         try:
#             # Converta os tipos de dados se necessário
#             id = int(linha.id)
#             created_at = linha.created_at  # Certifique-se de que este campo está no formato datetime
#             first_name = str(linha.first_name)
#             last_name = str(linha.last_name)
#             email = str(linha.email)
#             cell_phone = str(linha.cell_phone)  # Converter para string se necessário
#             country = str(linha.country)
#             state = str(linha.state)
#             street = str(linha.street)
#             number = str(linha.number)  # Converter para string se necessário
#             additionals = str(linha.additionals)

#             print(f"Inserindo linha {index}: {id}, {created_at}, {first_name}, {last_name}, {email}, {cell_phone}, {country}, {state}, {street}, {number}, {additionals}")

#             # Insira os dados
#             cursor.execute("""
#                 INSERT INTO [Clientes] 
#                 (id, created_at, first_name, last_name, email, cell_phone, country, state, street, number, additionals) 
#                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
#                 (id, created_at, first_name, last_name, email, cell_phone, country, state, street, number, additionals))
#         except Exception as e:
#             print(f"Erro ao inserir linha {index}: {e}")

#     # Commit após inserir todos os dados
#     cursor.commit()
# except Exception as e:
#     print(f"Erro geral durante a inserção: {e}")
# finally:
    # Assegure-se de fechar o cursor e a conexão no bloco finally
    #cursor.close()
    #conexaoDB.close()


# %%
# Exemplo de inserção usando tupla de parâmetros
for index, linha in dados.iterrows():   
    linha.email = str(linha.email)  # Converter para o tipo 'str' antes da inserção
    linha.country = str(linha.country)
    linha.state = str(linha.state)
    linha.street = str(linha.street)
    linha.number = str(linha.number)
    linha.additionals = str(linha.additionals)
    
    #linha.cell_phone = str(linha.cell_phone)
    cursor.execute("INSERT INTO [Clientes] (id, created_at,first_name, last_name,email,cell_phone,country, state,street, number, additionals) VALUES (?,?,?,?,?,?,?,?,?,?,?)",linha.id, linha.created_at,linha.first_name,
                   linha.last_name,linha.email,linha.cell_phone,linha.country,linha.state,linha.street,linha.number,linha.additionals)
cursor.commit()   # validar dados no SQL Server
cursor.close()    #Fechar Cursor
conexaoDB.close() #Fechar Conexao


