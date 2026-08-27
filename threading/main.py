# Basic threading

# Imports
import threading
from time import sleep

# Variables
thread_count = 5 # Desired number of threads for testing
threads = [] # A list to store each thread

def print_thread(i: int):
    print(f"This function is running on thread: {str(i)}")

for i in range(1, thread_count + 1):
    # target represents the desired function to run on the specified thread
    # args are the arguments passed to the target function
    thread = threading.Thread(target=print_thread, args=(i,)) # creates a new thread
    thread.start() # runs the thread
    threads.append(thread) # adds the thread to the list

# Threads are joined outside of the creation loop
for t in threads:
    t.join() # Runs sequentially
    # Pauses the main thread until this thread completes

print("\nAll threads have finished executing successfully.")