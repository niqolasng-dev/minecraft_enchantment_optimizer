import heapq
from item import Item
import itertools
counter = itertools.count()

def create_heap(items):
    
    item_heap = []

    for item in items:
        item_tuple = (item.calculate_work_penalty(),next(counter), item)
        item_heap.append(item_tuple)
    
    heapq.heapify(item_heap)
    return item_heap


def find_cheapest(item_heap):

    left_item = heapq.heappop(item_heap)
    sac_item = heapq.heappop(item_heap)

    print(f"Combine {left_item[2]} with {sac_item[2]}")
    print()

    new_item = left_item[2]
    new_item.add_enchantments(sac_item[2].enchantments)
    new_item.update_work(sac_item[2].prior_work)

    heapq.heappush(item_heap, (new_item.prior_work, next(counter), new_item))

def merge_loop(item_heap):
    while len(item_heap) > 1:
        find_cheapest(item_heap)

def run_optimizer(items):
    merge_loop(create_heap(items))