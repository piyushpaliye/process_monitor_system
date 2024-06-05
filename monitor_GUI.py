import tkinter as tk
import psutil
import time
import threading
pid_count = {}
class ProcessMonitorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Process Monitor")
        self.pid_count = {}
        self.create_widgets()

    def create_widgets(self):
        self.output_text = tk.Text(self, height=10, width=50)
        self.output_text.pack(fill=tk.BOTH, expand=True)

        self.start_button = tk.Button(self, text="Start", command=self.start_monitoring)
        self.start_button.pack()

        self.stop_button = tk.Button(self, text="Stop", command=self.stop_monitoring)
        self.stop_button.pack()

    def start_monitoring(self):
        self.output_text.delete("1.0", tk.END)
        self.pid_count.clear()
        self.monitoring = True
        self.monitoring_thread = threading.Thread(target=self.monitor_processes)
        self.monitoring_thread.start()

    def stop_monitoring(self):
        self.monitoring = False
        self.monitoring_thread.join()

    def monitor_processes(self):
        while self.monitoring:
            self.get_running_executables()
            self.update_output()
            time.sleep(1)

    def get_running_executables(self):
        processes = psutil.process_iter()

        # Iterate over each process
        for process in processes:
            process_name = process.name()
            process_id = process.pid

            # Check if the process is already in the cache
            if process_id in self.pid_count:
                self.pid_count[process_id] += 1
            else:
                self.pid_count[process_id] = 1

            # Insert the output into the Text widget
            self.output_text.insert(tk.END, f"{process_id},{process_name}, {self.pid_count[process_id]}\n")
    def update_output(self):
        for process_id, process_name in self.pid_count.items():
            self.output_text.insert(tk.END, f"{process_id},{process_name}, {self.pid_count[process_id]}\n")
        
if __name__ == "__main__":
    app = ProcessMonitorApp()
    app.mainloop()