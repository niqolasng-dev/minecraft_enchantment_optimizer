from enchantment_data import ENCHANTMENTS
def find_cost(item, sacrifice) :
    enchantment_cost = find_enchantment_cost(sacrifice)
    return item.calculate_work_penalty() + sacrifice.calculate_work_penalty() +  enchantment_cost


def find_enchantment_cost(item):
    enchantment_cost = 0
    for key in item.enchantments:
        enchantment_cost += ENCHANTMENTS[key]["book_multiplier"] * item.enchantments[key]
    return enchantment_cost