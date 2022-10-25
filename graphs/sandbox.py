from queue import PriorityQueue


q = PriorityQueue()
q.put([2, "a"])
q.put([1, "a"])
q.put([1, "a"])

# while q.not_empty():
    # print(q.get())

while not q.empty():
    next_item = q.get()
    print(next_item)


# import heapq
#
# # initializing list
# li = [["a", 2]]
#
# # using heapify to convert list into heap
# heapq.heapify(li)

