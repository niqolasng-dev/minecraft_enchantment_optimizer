import heapq
from item import Item

def create_heap(items):
    
    item_heap = []

    for item in items:
        item_tuple = (item.calculate_work_penalty(), item)
        item_heap.append(item_tuple)
    
    heapq.heapify(item_heap)


