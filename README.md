# process_monitor_system
This repository demonstrates monitoring all running processes using psutil and provides a GUI version for ease of using.

## Installation
git clone https://github.com/piyushpaliye/process_monitor_system.git
pip install -r requirements.txt
## Usage

```python
python process_monitor.py
# returns all running processes with process ID, process name and count
1,systemd, 71
2,kthreadd, 71
3,rcu_gp, 71
4,rcu_par_gp, 71
5,slub_flushwq, 71
6,netns, 71
8,kworker/0:0H-events_highpri, 71
11,mm_percpu_wq, 71
12,rcu_tasks_kthread, 71
13,rcu_tasks_rude_kthread, 71
14,rcu_tasks_trace_kthread, 71

python monitor_GUI.py
# returns graphical user interface
#start stop buttons are used to monitor processes.
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

This code is freely distributed for coding enthusiasts
