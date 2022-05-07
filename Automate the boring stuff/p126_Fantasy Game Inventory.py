inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory_dict):
    print("Inventory:")
    total_items = 0
    for i,k in inventory.items():
        print(k, i)
        total_items += k
    print("Total number of items:", total_items)

displayInventory(inventory)
