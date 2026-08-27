# Mutual Exclusion:
# Ensures only one thread can access a critical section of the program.

# Bank transfers will be used for this example.

# Imports
import threading
from time import sleep

# Variables
balance = 0
thread_count = 10
threads = []
thread_lock = threading.Lock() # lock instance

# Function to transfer funds to bank account.
def transfer_funds(amount: int):
    global balance
    # Non-critical operations can exist outside of the thread lock and still run concurrently.
    with thread_lock:
        # "CRITICAL" SECTION
        local_balance = balance
        sleep(0.1) # Simulate an operation
        balance = local_balance + amount

for i in range(1, thread_count + 1):
    amount = 100
    
    thread = threading.Thread(target=transfer_funds, args=(amount,))
    thread.start()
    threads.append(thread)

for t in threads:
    t.join()

print("\nBank transfers completed successfully.")
print(f"Your current account balance: ${balance}")