import pandas as pd
import pyodbc 

server = 'LETICIA' # Substitua pelo nome do servidor SQL Server
database = 'Python'  # Substitua pelo nome do banco de dados
conexaoDB = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      f'SERVER={server};'
                      f'DATABASE={database};'
                      'Trusted_Connection=yes;')

cursor = conexaoDB.cursor()   # criando cursor de comando 

# %%
dados = pd.read_excel(r"C:\Users\Leticia\Desktop\Python-Banco de Dados\Banco de dados\Origem\arquivos_excel\items.xlsx")
#str(dados.columns).replace("'","") 
#dados.head(5)


# %%
dados

# %%
#apagar somente uma coluna no python
#cursor.execute("ALTER TABLE nome_da_tabela DROP COLUMN nome_da_coluna")
#cursor.commit()

# %%
#Para apagar somente uma linha em Python de uma tabela de banco de dados, você pode usar uma instrução SQL DELETE 
# combinada com uma condição WHERE para identificar a linha a ser apagada. Veja um exemplo abaixo:
#cursor.execute("DELETE FROM nome_da_tabela WHERE condição_para_identificar_a_linha")
#cursor.commit()
#tenho que olhar dentro do banco para verificar!
#cursor.execute("DELETE FROM items WHERE id = 158")
#cursor.commit()


# %%
#dados

# %%
#cursor.execute('delete from [Items]')   #executa tarefa de  apagar dados 
#cursor.commit()

# %%
#dados

# %%
#str(dados.columns).replace("'","")  # coluna de origem somente ver as colunas

# %%
str(dados.columns).replace("'","")  # coluna de origem 


# %%
#dados.head(5)

# %%
print(dados['id'].dtype)
print(dados['total_price'].dtype)


# %%
dados['total_price'] = dados['total_price'].astype(float)

# %%
#inserção no banco de dados 
for index, linha in dados.iterrows():
    
    cursor.execute("Insert into [Items](id,order_id,product_id,quantity,total_price)values(?,?,?,?,?)",linha.id,linha.order_id,linha.product_id,linha.quantity,linha.total_price) 
     # inserir colunas e quantas colunas tiver passar quantidade de ??
cursor.commit()   # validar dados no SQL Server
cursor.close()    #Fechar Cursor
conexaoDB.close() #Fechar Conexao

# %% [markdown]
# 


