import heapq
from item import Item
import itertools
counter = itertools.count()
import calculator
import copy

def create_heap(items):
    
    item_heap = []

    for item in items:
        # Tuple structure: (work_penalty, unique_counter, item)
        # Counter breaks ties when penalties are equal, avoiding comparison of Item objects
        item_tuple = (item.calculate_work_penalty(), next(counter), item)
        item_heap.append(item_tuple)
    
    heapq.heapify(item_heap)
    return item_heap

def find_cheapest_cost(items, cache):
    # Base case: a single item requires no combination
    if len(items) == 1:
        return (0, [], items[0])
    
    # Return cached result if this subset has been computed before
    if items in cache:
        return cache[items]

    current_minimum = float('inf')
    best_steps = None
    best_item = None

    # Try every possible way to split items into two non-empty subsets
    for k in range(1, len(items)):
        for subset in itertools.combinations(items, k):
            left = subset
            # Right is everything not in left
            right = tuple(item for item in items if item not in left)
            
            if left not in cache:
                cost, steps, item = find_cheapest_cost(left, cache)
                cache[left] = cost, steps, item

            if right not in cache:
                cost, steps, item = find_cheapest_cost(right, cache)
                cache[right] = cost, steps, item

            left_cost, left_steps, left_item = cache[left]
            right_cost, right_steps, right_item = cache[right]

            # Gear item must always be the target, never the sacrifice
            if right_item.name != "book" :
                final_item, final_cost = combine_items(right_item, left_item)
            else:
                final_item, final_cost = combine_items(left_item, right_item)

            last_combination_cost = final_cost
            total = left_cost + right_cost + last_combination_cost
            
            if total < current_minimum:
                current_minimum = total
                best_steps = left_steps + right_steps + [(left_item, right_item, final_cost)]

                best_item = final_item
            
    return current_minimum, best_steps, best_item

def combine_items(target, sac):
    # Deep copy target so we don't mutate the original item during exploration
    new_item = copy.deepcopy(target)
    new_item.add_enchantments(sac.enchantments)
    new_item.update_work(sac.prior_work)

    return new_item, calculator.find_cost(target, sac)

def find_cheapest_prior_work(item_heap):
    # Gear item must always be the target — check the front of the heap first
    if item_heap[0][2].name != 'book':
        left_item = heapq.heappop(item_heap)
        sac_item = heapq.heappop(item_heap)
    else:
        sac_item = heapq.heappop(item_heap)
        left_item = heapq.heappop(item_heap)
        

    print(f"Combine {left_item[2]} with {sac_item[2]}")
    print()    

    new_item = combine_items(left_item, sac_item)
    heapq.heappush(item_heap, (new_item.prior_work, next(counter), new_item))
    return new_item

def merge_loop(item_heap):
    final_item = None
    while len(item_heap) > 1:
        final_item = find_cheapest_prior_work(item_heap)

    print(f"{final_item}")

def run_optimizer(items, approach):
    # DP approach: finds the globally optimal combination order
    if approach is True:
        final_cost, steps, final_item = find_cheapest_cost(tuple(items), {})
        for target, sacrifice, cost in steps:
            print(f"Combine {target} with {sacrifice}, cost is {cost} levels")
        print(f"Final item is {final_item} \nTotal cost is {final_cost}")
    else:
        # Greedy approach: minimizes prior work penalty at each step
        merge_loop(create_heap(items))