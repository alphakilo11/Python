inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory_dict):
    print("Inventory:")
    total_items = 0
    for i,k in inventory.items():
        print(k, i)
        total_items += k
    print("Total number of items:", total_items)

displayInventory(inventory)

dragonLoot = ['gold coin', 'gold coin', 'dagger', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory:
            old_value = inventory.get(i)
            new_value = old_value + 1
            inventory[i] = new_value
        else:
            inventory.setdefault(i, 1)
    return inventory

addToInventory(inventory, dragonLoot)
displayInventory(inventory)
