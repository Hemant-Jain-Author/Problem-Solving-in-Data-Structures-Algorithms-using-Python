from collections import deque

que = deque([])
que.append(1)
que.append(2)
que.append(3)
print("Queue : ", que)
print("Queue size : ", len(que))
print("Queue peek : ", que[0])
print("Queue remove : ",  que.popleft())
print("Queue : ", que)
print("Queue isEmpty : ", (len(que) == 0))
        

"""
Queue :  deque([1, 2, 3])
Queue size :  3
Queue peek :  1
Queue remove :  1
Queue :  deque([2, 3])
Queue isEmpty :  False
"""