from typing import List
class Process:
    def __init__(self, processName:str, arrivalTime:int, burstTime:int)->None:
        self.processName:str=processName
        self.arrivalTime:int=arrivalTime
        self.burstTime:int=burstTime
        self.startTime:int
        self.completionTime:int
        self.waitingTime:int
        self.turnAroundTime:int

class FCFS:
    def __init__(self, processList:List[Process])->None:
        self.processList:List[Process]=processList
        self.avgWaitingTime:float
        self.avgTAT:float
        self.sortProcess()
        self.scheduler()

    def sortProcess(self):
        self.processList=sorted(self.processList, key=lambda x: x.arrivalTime)

    def scheduler(self)->None:
        currentTime=0
        totalWaitingTime=0
        totalTAT=0
        for process in self.processList:
            process.startTime=max(currentTime, process.arrivalTime)
            process.completionTime=process.startTime+process.burstTime
            process.turnAroundTime=process.completionTime-process.arrivalTime
            process.waitingTime=process.turnAroundTime-process.burstTime
            totalWaitingTime+=process.waitingTime
            totalTAT+=process.turnAroundTime
            currentTime=process.completionTime
        self.avgWaitingTime=totalWaitingTime/len(self.processList)        
        self.avgTAT=totalTAT/len(self.processList)

    
    def __repr__(self):
        # Initialize the output string
        header = "="*15+"FCFS Scheduling"+"="*15+"\n"
        output_string = "" + header
        
        # 1. Add the header row
        header = f"Name\tAT\tBT\tCT\tWT\tTAT\n"
        output_string += header
        
        # 2. Add data for each process
        for process in self.processList:
            process_line = f"{process.processName:<8}{process.arrivalTime:<8}{process.burstTime:<8}{process.completionTime:<8}{process.waitingTime:<8}{process.turnAroundTime}\n"
            output_string += process_line
        
        # 3. Add averages
        output_string += f"Average Waiting Time: {self.avgWaitingTime:.2f}\n"
        output_string += f"Average Turn Around Time: {self.avgTAT:.2f}"
        
        # Return the collected string
        return output_string



if __name__=="__main__":
    # n=int(input("Enter the number of processes: "))
    n=5
    processList=[]
    pname=["P1","P2", "P3", "P4", "P5"]
    bt=[4,3,5,6,2]
    at=[1,2,3,3,200]

    # for i in range(n):
    #     processName=input("Enter the name of the process: ")
    #     arrivalTime=int(input("Enter the arrival time of the process: "))
    #     burstTime=int(input("Enter the burst time: "))
    #     processList.append(Process(processName, arrivalTime, burstTime))

    for i in range(n):
        processList.append(Process(pname[i], at[i], bt[i]))


    scheduler=FCFS(processList)
    print(scheduler)




    
