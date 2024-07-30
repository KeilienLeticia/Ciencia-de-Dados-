import schedule
import time
import pandas as pd
import pyodbc 



def job():  
    server = 'LETICIA' 
    database = 'Python' 
    conexaoDB = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                        f'SERVER={server};'
                        f'DATABASE={database};'
                        'Trusted_Connection=yes;')

    cursor = conexaoDB.cursor()   # criando cursor de comando 

    dados = pd.read_excel(r"C:\Users\Leticia\Desktop\Python-Banco de Dados\Banco de dados\Origem\arquivos_excel\Categoria.xlsx")
    dados.rename(columns={'name': 'Nome'}, inplace=True)
   

    # faz carga no banco de dados
    for index, linha in dados.iterrows():
        
        cursor.execute("Insert into [Categoria](Id,Nome)values(?,?)", (linha ['id'],linha ['Nome'])) 
        
    cursor.commit()   
    cursor.close() 
    conexaoDB.close() 
schedule.every(10).seconds.do(job) # escolher a frequencia 
execution_count =0
while True: # loop contínuo
    schedule.run_pending()  # Executa tarefas agendadas que estão prontas para serem executadas
    time.sleep(1)  # Pausa por 1 segundo antes de verificar novamente as tarefas agendadas  
    execution_count +=1
    
    if execution_count > 120: #  # Condição para limpar as tarefas, por exemplo, após 50 execuções e para o loop
        schedule.clear() 
        print("Tarefas limpas!!!!")
        break   
print("Loop encerrado")


