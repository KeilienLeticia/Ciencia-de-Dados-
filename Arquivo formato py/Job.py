import schedule  # Importa agendamento de tarefas
import time  # Importa a biblioteca 'time' para pausas de tempo
def job():  # Definição de uma função chamada 'job'
    print("estou funcionando")  # Imprime uma mensagem indicando (Trocar pelo seu script)
 
# Agendando tarefas com diferentes intervalos e horários
schedule.every(10).minutes.do(job)                              # Executa a cada 10 minutos
schedule.every().hour.do(job)                                   # Executa a cada hora
schedule.every().day.at("10:30").do(job)                        # Executa diariamente às 10:30
schedule.every().monday.do(job)                                 # Executa toda segunda-feira
schedule.every().wednesday.at("13:15").do(job)                  # Executa toda quarta-feira às 13:15
schedule.every().day.at("12:42", "Europe/Amsterdam").do(job)    # Executa diariamente às 12:42 (usando fuso horário Europe/Amsterdam)
schedule.every().day.at("12:42").do(job)                        # Executa diariamente às 12:42 (usando fuso horário Seu PC)
schedule.every().minute.at(":17").do(job)                       # Executa a cada minuto quando o segundo é 17

# Executar as tarefas agendadas em um loop contínuo
while True:  # loop contínuo
    schedule.run_pending()  # Executa tarefas agendadas que estão prontas para serem executadas
    time.sleep(1)  # Pausa por 1 segundo antes de verificar novamente