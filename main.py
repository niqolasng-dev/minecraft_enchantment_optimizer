from enchantment_data import ENCHANTMENTS
from item_data import ITEMS
from item import Item
import optimizer
import itertools
import os
import time

enchantment_counter = itertools.count()
enchantment_dict = {}
item_selection = None
enchantment_selection = 0

while True:
    
    try: 
        #show all items and get number that will correspond to the desired item
        for index, item in enumerate(ITEMS):
            print(f"{index}. {item}")

        print()
        item_selection = list(ITEMS.keys())[int(input("Enter the number of the item you wish to enchant: "))]
        print()
        break
    except (ValueError, KeyError, IndexError):
        print("Please enter a valid number between 0-15")
        print()
        time.sleep(1.5)  # pause for 1.5 seconds before clearing
        os.system('cls' if os.name == 'nt' else 'clear')



#dict holds the enchantments and the numbers that correspond to them
for enchantment in ITEMS[item_selection]["compatible_enchantments"]:
    enchantment_dict[next(enchantment_counter)] = enchantment
enchantment_dict[next(enchantment_counter)] = "Done"

#get all enchantments that the user wants to apply
enchantments_list = []
while enchantment_dict[enchantment_selection] != "Done":
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        for key, enchantment in enchantment_dict.items():
            print(f"{key}. {enchantment}")

        enchantment_selection = int(input("Enter the number of the enchantment you wish to add: "))
        if enchantment_dict[enchantment_selection] != "Done":
            
            if enchantment_dict[enchantment_selection] in enchantments_list:
                raise RuntimeError("Repeat Enchantments")
            
            enchantments_list.append(enchantment_dict[enchantment_selection])
    except (ValueError, KeyError, IndexError):
        print("Please enter a valid number")
        time.sleep(1.5)
    except RuntimeError:
        print("Enchantment Already Added To List")
        time.sleep(1.5)





item = Item(item_selection)
all_items = []
all_items.append(item)

for enchantment in enchantments_list:
    all_items.append(Item("book", {enchantment: ENCHANTMENTS[enchantment]["max_level"]}))
    

optimizer.run_optimizer(all_items, True)
