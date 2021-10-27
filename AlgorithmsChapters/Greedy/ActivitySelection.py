class Activity :
    def __init__(self, s,  f) :
        self.start = s
        self.stop = f

def maxActivities(s,  f) :
    n = len(s)
    act = [None] * n
    
    for i in range(n) :
        act[i] = Activity(s[i], f[i])    

    act.sort(key = lambda k : k.stop) #  sort according to finish time.
    i = 0  #  The first activity at index 0 is always gets selected.
    print("Activities are : (" + str(act[i].start) + "," + str(act[i].stop) + ")", end ="")

    for j in range(n) :
        #  Find next activity whose start time is greater than or equal
        #  to the finish time of previous activity.
        if (act[j].start >= act[i].stop) :
            print(", (" + str(act[j].start) + "," + str(act[j].stop) + ")", end ="")
            i = j

s = [1, 5, 0, 3, 5, 6, 8]
f = [2, 6, 5, 4, 9, 7, 9]
maxActivities(s, f)

"""
Activities are : (1,2), (3,4), (5,6), (6,7), (8,9)
"""