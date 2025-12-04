# Write a program to implement non-preemptive priority-based scheduling algorithm. 

def priority_scheduling(processes, n, burst_time, priority, waiting_time, turnaround_time):
    # Sort processes by priority (lower value = higher priority)
    for i in range(n):
        for j in range(i + 1, n):
            if priority[j] < priority[i]:
                # Swap all related information
                priority[i], priority[j] = priority[j], priority[i]
                burst_time[i], burst_time[j] = burst_time[j], burst_time[i]
                processes[i], processes[j] = processes[j], processes[i]

    # First process has 0 waiting time
    waiting_time[0] = 0

    # Calculate waiting time for each process
    for i in range(1, n):
        waiting_time[i] = burst_time[i - 1] + waiting_time[i - 1]

    # Calculate turnaround time
    for i in range(n):
        turnaround_time[i] = burst_time[i] + waiting_time[i]


# -------------------- DRIVER CODE --------------------

n = int(input("Enter number of processes: "))

processes = []
burst_time = []
priority = []

for i in range(n):
    processes.append(f"P{i+1}")
    burst_time.append(int(input(f"Enter burst time of P{i+1}: ")))
    priority.append(int(input(f"Enter priority of P{i+1} (lower = higher priority): ")))

waiting_time = [0] * n
turnaround_time = [0] * n

priority_scheduling(processes, n, burst_time, priority, waiting_time, turnaround_time)

# Print output
print("\nProcess\tBurst\tPriority\tWaiting\tTurnaround")
total_wt = 0
total_tat = 0

for i in range(n):
    total_wt += waiting_time[i]
    total_tat += turnaround_time[i]
    print(f"{processes[i]}\t{burst_time[i]}\t{priority[i]}\t\t{waiting_time[i]}\t{turnaround_time[i]}")

print(f"\nAverage Waiting Time: {total_wt / n:.2f}")
print(f"Average Turnaround Time: {total_tat / n:.2f}")
