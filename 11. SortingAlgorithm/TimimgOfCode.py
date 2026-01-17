import time
class Timer:
    def __init__(self):
        self.start_time = 0
        self.elapsed_time = 0   
    def start(self):
        """Start a new timer."""
        if self.start_time != 0:
            raise Exception("Timer is already running. Use .stop() to stop it before starting again.")
        self.start_time = time.perf_counter()
    def stop(self):
        """Stop the timer, and report the elapsed time."""
        if self.start_time == 0:
            raise Exception("Timer is not running. Use .start() to start it.")
        self.elapsed_time = time.perf_counter() - self.start_time
        self.start_time = 0
    def elapsed(self):
        """Return the total elapsed time in seconds."""
        if self.elapsed_time == 0:
            raise Exception("Timer has not been run yet. Use .start().")  
        return self.elapsed_time
    def __str__(self):
        """print () prints elapsed time"""
        return (str(self.elapsed_time))
t = Timer()
for j in range(4,9):
    t.start()
    n = 0
    for i in range(10**j):
        n += i
    t.stop()
    print(j,t)