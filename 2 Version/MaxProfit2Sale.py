def maxProfit(price):
    size = len(price)
    profit = [0]*size
     
    maxPrice=price[size - 1]
    for i in range( size-2, -1 ,-1):
        if price[i]> maxPrice:
            maxPrice = price[i]
             
        profit[i] = max(profit[i+1], maxPrice - price[i])
    print profit
    minPrice=price[0]
    for i in range(1,size):
        if price[i] < minPrice:
            minPrice = price[i]

        profit[i] = max(profit[i-1], profit[i]+(price[i]-minPrice))
    print profit
    result = profit[size-1]
     
    return result


price = [2, 30, 15, 10, 8, 25, 80]
print "Maximum profit is", maxProfit(price)

