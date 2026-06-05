import heapq
from item import Item
import itertools
counter = itertools.count()
import calculator

def create_heap(items):
    
    item_heap = []

    for item in items:
        item_tuple = (item.calculate_work_penalty(), next(counter), item)
        item_heap.append(item_tuple)
    
    heapq.heapify(item_heap)
    return item_heap

def find_cheapest_cost(items, cache):
    if len(items) == 1:
        return (0, [])
    
    current_minimum = float('inf')
    for k in range(1, len(items)):
        for subset in itertools.combinations(items, k):
            left = subset
            right = tuple(item for item in items if item not in left)
            left_cost, left_steps = find_cheapest_cost(left, cache)
            right_cost, right_steps = find_cheapest_cost(right, cache)
            last_combination_cost = left_cost + right_cost
            total = left_cost + right_cost + last_combination_cost
            current_minimum = min(current_minimum, total)



def find_cheapest_prior_work(item_heap):
    if item_heap[0][2].name != 'book':
        left_item = heapq.heappop(item_heap)
        sac_item = heapq.heappop(item_heap)
    else:
        sac_item = heapq.heappop(item_heap)
        left_item = heapq.heappop(item_heap)
        

    print(f"Combine {left_item[2]} with {sac_item[2]}")
    print()
    #level_cost = calculator.find_cost(left_item[2], sac_item[2])
    

    new_item = left_item[2]
    new_item.add_enchantments(sac_item[2].enchantments)
    new_item.update_work(sac_item[2].prior_work)

    heapq.heappush(item_heap, (new_item.prior_work, next(counter), new_item))
    return new_item

def merge_loop(item_heap):
    total_work = 0
    final_item = None
    while len(item_heap) > 1:
        final_item = find_cheapest_prior_work(item_heap)

    print(f"{final_item}")

def run_optimizer(items):
    merge_loop(create_heap(items))