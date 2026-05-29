from enchantment_data import ENCHANTMENTS
from item_data import ITEMS
from item import Item
import optimizer
import itertools

enchantment_counter = itertools.count()
enchantment_dict = {}

#show all items and get number that will correspond to the desired item
for index, item in enumerate(ITEMS):
    print(f"{index}. {item}")

print()
item_selection = list(ITEMS.keys())[int(input("Enter the number of the item you wish to enchant:"))]
print()

#dict holds the enchantments and the numbers that correspond to them
for enchantment in ENCHANTMENTS:
    enchantment_dict[next(enchantment_counter)] = enchantment
enchantment_dict[next(enchantment_counter)] = "Done"

enchantment_selection = 0
enchantments_list = []

#get all enchantments that the user wants to apply
while enchantment_dict[enchantment_selection] != "Done":
    for key, enchantment in enchantment_dict.items():
        print(f"{key}. {enchantment}")

    enchantment_selection = int(input("Enter the number of the enchantment you wish to add: "))
    if enchantment_dict[enchantment_selection] != "Done":
        enchantments_list.append(enchantment_dict[enchantment_selection])


item = Item(item_selection)
all_items = []
all_items.append(item)

for enchantment in enchantments_list:
    all_items.append(Item("book", {enchantment: ENCHANTMENTS[enchantment]["max_level"]}))
    

optimizer.run_optimizer(all_items)