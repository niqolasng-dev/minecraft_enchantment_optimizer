# Minecraft Enchantment Optimizer

A command-line tool that finds the optimal order to apply enchantments to items in Minecraft, minimizing total XP cost.

## How It Works

The optimizer uses dynamic programming to evaluate every possible combination order. Items are recursively split into smaller subsets, and the cheapest way to combine each subset is found before working up to the full solution. Results are cached so repeated subsets are never recomputed. This guarantees the globally optimal combination order, unlike a greedy approach which can miss cheaper solutions.

## How to Run

```bash
python main.py
```

Follow the command-line prompts to select your item and enchantments. The program will output the optimal combination order, the XP cost of each step, and the total cost.

## Known Limitations

- All enchantments are assumed to be at their maximum level — custom levels are not currently supported
- No validation for incompatible enchantments (e.g. Sharpness and Smite on the same item)
- Books only — item-to-item combinations are not supported
- Assumes the target item has no prior work penalty