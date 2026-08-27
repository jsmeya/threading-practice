# threading-practice
A repo for personal practice of threading concepts.
* Basic Threading: Allows a program to run multiple tasks concurrently.
* Mutual Exclusion: Ensures only one thread can access a critical section at any given time.
* Thread Pooling: Maintains a preset pool of worker threads that can be reused for concurrent tasks.

<br>

### Basic Threading
* Utilizes Python's ```threading``` module for multithreading.
* Implements basic print functions for testing. No additional functionality or checks.

### Mutual Exclusion
* Introduces the concept of mutual exclusion through a banking transfer program.
* Isolates a critical section and applies a thread lock (```threading.Lock()```).

### Thread Pooling
* Introduces thread pooling through a ***fake*** sequential TCP port scanner.
* Utilizes ```ThreadPoolExecutor``` to distribute port scans to a fixed pool of worker threads.