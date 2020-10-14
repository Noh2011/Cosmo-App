# Welcome to EPYTHON LAB
# Creating a Cosmo App[Cosmotics shopping app]

# Cosmo app is a Python based application
# which can enable to 
# - Register new items
# - Update sold items
# - Delete items
# - Store recorded information into JSON file

# Step 1: We have to create an empty json file
# to store our data for later use


# Step 2: Read a json file and check the items available
#Import json library
import json
with open('cosmo.json') as f:
    cosmo = json.load(f)

# For first time, your dictionary look a like cosmo = {}
print(cosmo)

# Step 3: Create a user menu

print("""
|--------------------------------
|\t Select the menu             |    
|\t 1. Add new items            |
|\t 2. Update sold items           |
|\t 3. Delete item              |
|\t 0 . Exit application        |
|-------------------------------|
""")
menu = int(input("Enter menu:"))
# Step 4: Create a while loop
# Check the while loop if menu selected is different from 0
# Else exit the application
while menu != 0:
    # Step 1: Check condition 1
    if menu == 1:
        # Step 1: Register new tems 
        item_name = input("Enter item name:")
        qty = int(input("Enter amount of an item:"))
        price = float(input("Enter unit price:"))

        # Step 2: Update the dictionary

        # {item_name: {item_name:name, 
        # qauntity: qty, unit_price:price, 
        # quantity_sold:qty_sold}}
        cosmo[item_name] = {} # Create empty sub dictionary
        cosmo[item_name]['name'] = item_name
        cosmo[item_name]['quantity'] = qty
        cosmo[item_name]['unit_price'] = price
        cosmo[item_name]['quantity_sold'] = 0
        print(cosmo)
    # Step 2: check condition 2
    elif menu == 2:
        # Step 1: Update the sold item
        item_sold = input("Enter item name:")
        qty_sold = int(input("Enter quantity sold:"))
        # Step 2: Check the item is vailable in the dictionary
        if item_sold in cosmo:
            # Update the quantity_sold item
            cosmo[item_sold]['quantity_sold'] = qty_sold
        print(cosmo)

    # Step 3: Check condition 3
    elif menu == 3:
        # Step 1: Delete item from dictionary
        item_del = input("Enter item name to delete:")
        del(cosmo[item_del])

        print("Item is successfuly deleted.")

    # Step 4: Check condition 4
    elif menu != 0:
        # Step 1: Print error message
        print("You didn't select a valid menu. Please try again.")
    
    # Step 5: Enter the user menu agian
    menu = int(input("""You wanna continue? 
    Please select the menu again:"""))

#-----------------------------------------

# Step 5: Update the json file 
import json
with open("cosmo.json", 'w') as cos:
    json.dump(cosmo, cos)
