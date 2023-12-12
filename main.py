# Importazione delle librerie
import multiprocessing
import schedule
import time
from capacity_ledger import main as capacity_ledger_main
from item_ledger import main as item_ledger_main

# Funzione che crea due processi distinti per gli script di capacity_ledger e item_ledger
def run_jobs():
    # Script di capacity_ledger
    capacity_ledger_process = multiprocessing.Process(target=capacity_ledger_main)
    # Script di item_ledger
    item_ledger_process = multiprocessing.Process(target=item_ledger_main)

# Avvia entrambi i processi
    try:
        capacity_ledger_process.start()
        item_ledger_process.start()

        capacity_ledger_process.join()
        item_ledger_process.join()

# Inserimento di un comando da tastiera (CTRL + C) per interrompere entrambi i processi
    except KeyboardInterrupt:
        capacity_ledger_process.terminate()
        item_ledger_process.terminate()

# Chiusura dei processi
    finally:
        capacity_ledger_process.join()
        item_ledger_process.join()

# Schedule dell'esecuzione dello script ogni sabato alle ore 01:00
def main():
    # Schedule dell'esecuzione dello script ogni sabato alle ore 01:00
    schedule.every().wednesday.at("00:05").do(run_jobs)

    # Loop per eseguire il programma
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()