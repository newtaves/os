from typing import List

class Process:
    def __init__(self, processName:str, arrivalTime:int, burstTime:int)->None:
        self.name:str=processName
        self.arrivalTime:int=arrivalTime
        self.burstTime:int=burstTime
        self.startTime:int
        self.completionTime:int
        self.waitingTime:int
        self.turnAroundTime:int

class SJF:
    def __init__(self, procesList:List[Process]):
        self.processList=procesList
        self.avgWaitingTime:float
        self.avgTAT:float

    def schedule(self):
        
        #Short by arrival Time
        self.processList.sort(key=lambda p: p.arrivalTime)

        readyQueue:List[Process] = []
        pendingQueue:List[Process] = self.processList[:]
        completedProcess:List[Process] = []
        currentTime:int=0
        
        
        while readyQueue or pendingQueue:
            #All the processes needed to be executed now
            arrivedNow = [p for p in pendingQueue if p.arrivalTime<=currentTime]
            for p in arrivedNow:
                readyQueue.append(p)
                pendingQueue.remove(p)

            #if CPU is idle proceed to next process
            if not readyQueue:
                if pendingQueue:
                    currentTime = pendingQueue[0].arrivalTime
                    continue
                else:
                    break
            
            #sort readyQueue according to burst time
            readyQueue = sorted(readyQueue, key=lambda p: p.burstTime)

            selectedProcess = readyQueue.pop(0)
            selectedProcess.startTime = currentTime
            currentTime+=selectedProcess.burstTime
            selectedProcess.completionTime = currentTime


            selectedProcess.turnAroundTime = selectedProcess.completionTime - selectedProcess.arrivalTime
            selectedProcess.waitingTime = selectedProcess.turnAroundTime - selectedProcess.burstTime

            completedProcess.append(selectedProcess)
        
        totalWaitingTime = sum([p.waitingTime for p in completedProcess])
        totalTurnAroundTime  = sum([p.turnAroundTime for p in completedProcess])
        n = len(completedProcess)

        if n>0:
            self.avgWaitingTime = totalWaitingTime/n
            self.avgTAT = totalTurnAroundTime/n
        
        self.processList = completedProcess

        return completedProcess
    
    def __repr__(self):
        # Initialize the output string
        header = "="*15+"SJF Scheduling"+"="*15+"\n"
        output_string = "" + header
        
        # 1. Add the header row
        header = f"Name\tAT\tBT\tCT\tWT\tTAT\n"
        output_string += header
        
        # 2. Add data for each process
        for process in self.processList:
            process_line = f"{process.name:<8}{process.arrivalTime:<8}{process.burstTime:<8}{process.completionTime:<8}{process.waitingTime:<8}{process.turnAroundTime}\n"
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
    bt=[4,3,6,5,2]
    at=[1,2,3,3,200]

    # for i in range(n):
    #     processName=input("Enter the name of the process: ")
    #     arrivalTime=int(input("Enter the arrival time of the process: "))
    #     burstTime=int(input("Enter the burst time: "))
    #     processList.append(Process(processName, arrivalTime, burstTime))

    for i in range(n):
        processList.append(Process(pname[i], at[i], bt[i]))


    scheduler=SJF(processList)
    scheduler.schedule()
    print(scheduler)




    
