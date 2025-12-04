# Write a program to implement Shortest Job First (SJF) scheduling algorithm. 

def find_waiting_time(processes, n, at, bt, wt):
    completed = 0
    current_time = 0
    is_done = [False] * n

    while completed != n:
        # Find process with minimum burst time among available ones
        min_bt = float('inf')
        shortest = -1

        for i in range(n):
            if at[i] <= current_time and not is_done[i] and bt[i] < min_bt:
                min_bt = bt[i]
                shortest = i

        # If no process has arrived yet
        if shortest == -1:
            current_time += 1
            continue

        # Calculate waiting time
        wt[shortest] = current_time - at[shortest]

        # Update current time
        current_time += bt[shortest]

        # Mark process as completed
        is_done[shortest] = True
        completed += 1


def find_turnaround_time(n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]


def sjf_scheduling(processes, n, at, bt):
    wt = [0] * n
    tat = [0] * n

    # Find waiting times
    find_waiting_time(processes, n, at, bt, wt)

    # Find turnaround times
    find_turnaround_time(n, bt, wt, tat)

    # Print results
    print("\nProcess\tArrival\tBurst\tWaiting\tTurnaround")
    total_wt = 0
    total_tat = 0

    for i in range(n):
        total_wt += wt[i]
        total_tat += tat[i]
        print(f"{processes[i]}\t{at[i]}\t{bt[i]}\t{wt[i]}\t{tat[i]}")

    print(f"\nAverage Waiting Time: {total_wt / n:.2f}")
    print(f"Average Turnaround Time: {total_tat / n:.2f}")


# ------------------ DRIVER CODE ------------------

n = int(input("Enter number of processes: "))

processes = []
arrival_time = []
burst_time = []

for i in range(n):
    processes.append(f"P{i+1}")
    arrival_time.append(int(input(f"Enter arrival time of P{i+1}: ")))
    burst_time.append(int(input(f"Enter burst time of P{i+1}: ")))

sjf_scheduling(processes, n, arrival_time, burst_time)





