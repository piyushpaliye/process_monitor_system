import psutil
import time

pid_count = {}
def get_running_executables():
    # Get all running processes
    processes = psutil.process_iter()
    
    # Iterate over each process
    for process in processes:
        process_name = process.name()

        process_id = process.pid

        # Check if the process is already in the cache
        if process_id in pid_count:
            
            pid_count[process_id] += 1
        else:
            #
            pid_count[process_id] = 1

        
        print(f"{process_id},{process_name}, {pid_count[process_id]}")
        
        
def repeat_fun():
    t_end = time.time() + 60
    while time.time() < t_end:
        get_running_executables()
while True:
    repeat_fun()
    pid_count.clear()