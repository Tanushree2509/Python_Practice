import time
class Timer:
    def __init__(self):
        self.start_time = 0 #None
        self.elapsed_time = 0 #None
    def start(self):
        self._start_time = time.pref_counter()
    def stop(self):
        self.elapsed_time = time.pref_counter() - self._start_time 
    def elapsed(self):
        return (self._elapsed_time)