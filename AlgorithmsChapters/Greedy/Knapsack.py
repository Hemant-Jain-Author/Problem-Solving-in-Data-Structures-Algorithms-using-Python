
class Item :
    def __init__(self, w,  c) :
        self.wt = w
        self.cost = c
        self.density = c/w

#  Approximate solution.
def knapsack_max_cost_greedy(wt,  cost,  capacity) :    
    n = len(wt)
    items = [None] * n
    for i in range(n) :
        items[i] = Item(wt[i], cost[i])    
    
    items.sort(key = lambda x: -x.density) # decreasing density sort

    i = 0
    profit = 0
    while (i < n and capacity > 0) :
        if (capacity - items[i].wt >= 0) :
            capacity -= items[i].wt
            profit += items[i].cost
        i += 1
    return  profit

wt = [10, 40, 20, 30]
cost = [60, 40, 90, 120]
capacity = 50
maxCost = knapsack_max_cost_greedy(wt, cost, capacity)
print("Maximum cost obtained = ", maxCost)

"""
Maximum cost obtained = 150
"""