from enchantment_data import ENCHANTMENTS
def find_cost(item, sacrifice) :
    
    enchantment_cost = 0
    for key in sacrifice.enchantments:
        enchantment_cost += ENCHANTMENTS[key]["book_multiplier"] * sacrifice.enchantments[key]
    
    return item.calculate_work_penalty() + sacrifice.calculate_work_penalty() +  enchantment_cost