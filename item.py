class Item:

    def __init__(self, name, enchantments = None):
        self.name = name

        if enchantments is None:
            self.enchantments = {}
        else:
            self.enchantments = enchantments
        self.prior_work = 0



    def add_enchantments(self, new_enchantments):
        self.enchantments = self.enchantments | new_enchantments


    def update_work(self, sac_work):
        self.prior_work = max(self.prior_work, sac_work) + 1

    def calculate_work_penalty(self):
        return pow(2, self.prior_work) - 1
    
    def __str__(self):
        return f"Item: {self.name} \n Prior Work: {self.prior_work} \n Enchantments: {self.enchantments}"