# Write a program to implement first-fit, best-fit and worst-fit allocation strategies. 

def first_fit(blocks, m, processes, n):
    allocation = [-1] * n
    for i in range(n):
        for j in range(m):
            if blocks[j] >= processes[i]:
                allocation[i] = j
                blocks[j] -= processes[i]
                break
    return allocation


def best_fit(blocks, m, processes, n):
    allocation = [-1] * n
    for i in range(n):
        best_index = -1
        for j in range(m):
            if blocks[j] >= processes[i]:
                if best_index == -1 or blocks[j] < blocks[best_index]:
                    best_index = j
        if best_index != -1:
            allocation[i] = best_index
            blocks[best_index] -= processes[i]
    return allocation


def worst_fit(blocks, m, processes, n):
    allocation = [-1] * n
    for i in range(n):
        worst_index = -1
        for j in range(m):
            if blocks[j] >= processes[i]:
                if worst_index == -1 or blocks[j] > blocks[worst_index]:
                    worst_index = j
        if worst_index != -1:
            allocation[i] = worst_index
            blocks[worst_index] -= processes[i]
    return allocation


# --------------------- DRIVER CODE ---------------------

# Input block sizes
m = int(input("Enter number of memory blocks: "))
blocks = []
print("Enter block sizes:")
for _ in range(m):
    blocks.append(int(input()))

# Input process sizes
n = int(input("\nEnter number of processes: "))
processes = []
print("Enter process sizes:")
for _ in range(n):
    processes.append(int(input()))

# Make copies for each strategy
blocks_ff = blocks.copy()
blocks_bf = blocks.copy()
blocks_wf = blocks.copy()

ff = first_fit(blocks_ff, m, processes, n)
bf = best_fit(blocks_bf, m, processes, n)
wf = worst_fit(blocks_wf, m, processes, n)

# Display results
def display(strategy_name, allocation):
    print(f"\n{strategy_name} Allocation:")
    print("Process Size → Block No.")
    for i in range(n):
        if allocation[i] != -1:
            print(f"P{i+1} ({processes[i]}) → Block {allocation[i]+1}")
        else:
            print(f"P{i+1} ({processes[i]}) → Not Allocated")

display("First-Fit", ff)
display("Best-Fit", bf)
display("Worst-Fit", wf)
