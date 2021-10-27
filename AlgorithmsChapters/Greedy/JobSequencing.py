class Job :
    def __init__(self, id,  deadline,  profit) :
        self.id = id
        self.deadline = deadline
        self.profit = profit

def job_sequencing(ids,  deadlines,  profits,  n) :
    maxDL = deadlines[0]
    for i in range(n) :
        if (deadlines[i] > maxDL) : 
            maxDL = deadlines[i]

    jobs = [None] * n
    for i in range(n) :
        jobs[i] = Job(ids[i], deadlines[i], profits[i])
    jobs.sort(key = lambda j : -j.profit) # decreasing profit.

    job = [-1] * maxDL # job id -1 indicate no job selected for this slot.
    profit = 0

    for i in range(n) : #  Iterate through all given jobs
        for j in  range(jobs[i].deadline - 1, -1, -1) :
            if (job[j] == -1) :
                job[j] = jobs[i].id  # Slot booked
                profit += jobs[i].profit
                break
    
    print("Profit is ::", profit)
    print("Jobs selected are::", end =" ")
    for i in range(maxDL) :
        if (job[i] != -1) : 
            print(job[i], end =" ")    

id = ['a', 'b', 'c', 'd', 'e', 'f']
deadline = [3, 1, 2, 4, 4, 1]
profit = [50, 40, 27, 31, 30, 60]
js = job_sequencing(id, deadline, profit, 6)

"""
Profit is :: 171
Jobs selected are:: f e a d
"""