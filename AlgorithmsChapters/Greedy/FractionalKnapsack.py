
class Items:
    def __init__(self, w,  c) :
        self.wt = w
        self.cost = c
        self.density = c // w

def max_cost_fractional_knapsack(wt,  cost,  capacity) :
    n = len(wt)
    itemList = [None] * n
    for i in range(n) :
        itemList[i] = Items(wt[i], cost[i])    

    itemList.sort(key = lambda k : - k.density) # Sort decreasing.
    totalCost = 0
    for i in range(n) :
        if (capacity - itemList[i].wt >= 0) :
            capacity -= itemList[i].wt
            totalCost += itemList[i].cost
        else :
            totalCost += (itemList[i].density * capacity)
            break

    return  totalCost

wt = [10, 40, 20, 30]
cost = [60, 40, 90, 120]
capacity = 50
maxCost = max_cost_fractional_knapsack(wt, cost, capacity)
print("Maximum cost obtained = ", maxCost)

"""
Maximum cost obtained =  230
"""