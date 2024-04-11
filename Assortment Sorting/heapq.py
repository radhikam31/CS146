import heapq

max_heap = [5, 3, 8, 2, 1]

min_heap = [-x for x in max_heap]
heapq.heapify(min_heap)

print("Max Heap:", max_heap)
print("Min Heap:", [-x for x in min_heap])
