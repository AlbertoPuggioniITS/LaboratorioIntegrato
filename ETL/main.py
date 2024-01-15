                                        ## Main process ##

# Import necessary libraries
import multiprocessing
import schedule
import time
from capacity_ledger import main as capacity_ledger_main
from item_ledger import main as item_ledger_main

# Function that creates two distinct processes to run the capacity_ledger.py script and item_ledger.py script
def run_jobs():
    # Capacity_ledger script
    capacity_ledger_process = multiprocessing.Process(target=capacity_ledger_main)
    # Item_ledger script
    item_ledger_process = multiprocessing.Process(target=item_ledger_main)

    # Start both processes
    try:
        capacity_ledger_process.start()
        item_ledger_process.start()

        capacity_ledger_process.join()
        item_ledger_process.join()

    # Keyboard command (CTRL + C) to stop both processes
    except KeyboardInterrupt:
        capacity_ledger_process.terminate()
        item_ledger_process.terminate()

    # Close both processes
    finally:
        capacity_ledger_process.join()
        item_ledger_process.join()

# Program schedule
def main():
    # Run both scripts every Saturday at 01:00 AM
    schedule.every().saturday.at("01:00:00").do(run_jobs)

    # Loop to execute the program
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()