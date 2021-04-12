# This is a sample Python script.

# ==========================================
# functions:
# ==========================================
def show_menu():
    menu = ["Hot Drinks", hotDrinks, "Cold Drinks", coldDrinks, "Fast Food", fastFood, "Dessert", desserts]
    for i, menu in enumerate(menu, 1):
        print(*menu)


def insert_item(item_name, price, category):
    if category == 1:
        # "Hot Drinks"
        new_item = [item_name, price]
        hotDrinks.append(new_item)
    elif category == 2:
        # "coldDrinks"
        new_item = [item_name, price]
        coldDrinks.append(new_item)
    elif category == 3:
        # "fastFood"
        new_item = [item_name, price]
        fastFood.append(new_item)
    elif category == 4:
        # "desserts"
        new_item = [item_name, price]
        desserts.append(new_item)


def delete_item(item_name, category):
    if category == 1:
        # "Hot Drinks"
        for item in hotDrinks:
            if item[0] == item_name:
                hotDrinks.remove(item)
    elif category == 2:
        # "coldDrinks"
        for item in coldDrinks:
            if item[0] == item_name:
                coldDrinks.remove(item)
    elif category == 3:
        # "fastFood"
        for item in fastFood:
            if item[0] == item_name:
                fastFood.remove(item)
    elif category == 4:
        # "desserts"
        for item in desserts:
            if item[0] == item_name:
                desserts.remove(item)


def put_item_inactive(item_name, category):
    if category == 1:
        # "Hot Drinks"
        for item in hotDrinks:
            if item[0] == item_name:
                new_item_inactive = [item[0], item[1], 1]
                hotDrinks.remove(item)
                inactivate_items.append(new_item_inactive)
    elif category == 2:
        # "coldDrinks"
        for item in coldDrinks:
            if item[0] == item_name:
                new_item_inactive = [item[0], item[1], 2]
                coldDrinks.remove(item)
                inactivate_items.append(new_item_inactive)
    elif category == 3:
        # "fastFood"
        for item in fastFood:
            if item[0] == item_name:
                new_item_inactive = [item[0], item[1], 3]
                fastFood.remove(item)
                inactivate_items.append(new_item_inactive)
    elif category == 4:
        # "desserts"
        for item in desserts:
            if item[0] == item_name:
                new_item_inactive = [item[0], item[1], 4]
                desserts.remove(item)
                inactivate_items.append(new_item_inactive)


def show_inactive():
    inactive_items = ["Inactive Items", inactivate_items]
    print(*inactive_items)


def put_item_inactive_back(item_name):
    for item in inactivate_items:
        if item[0] == item_name:
            insert_item(item[0], item[1], item[2])
            inactivate_items.remove(item)


def getcode_category(category):
    if category.lower().strip() == "hot drinks":
        return 1
    elif category.lower().strip() == "cold drinks":
        return 2
    elif category.lower().strip() == "fast food":
        return 3
    elif category.lower().strip() == "desserts":
        return 4
    else:
        print("category not found")


def contextual_menu():
    exit_program = 0

    while exit_program == 0:
        print(41 * "*")
        print(10 * "*" + " Welcome to the SHOP " + 10 * "*")
        print(17 * "*" + " Menu " + 18 * "*")
        print(2 * "*" + " 1. Show Cafe Menu")
        print(2 * "*" + " 2. Show Inactive")
        print(2 * "*" + " 3. Insert Item")
        print(2 * "*" + " 4. Put Inactive Item")
        print(2 * "*" + " 5. Put Inactive Item Back")
        print(2 * "*" + " 6. Delete Item")
        print(2 * "*" + " 0. exit")
        option = input("Insert the number of the option: ")

        if option == "1":
            show_menu()
        elif option == "2":
            show_inactive()
        elif option == "3":
            item_name = input("Insert item name: ")
            price = input("Insert price: ")
            category = input("Insert category name: ")
            code_category = getcode_category(category)
            insert_item(item_name, price, code_category)
        elif option == "4":
            category = input("Insert category name: ")
            put_item_inactive(input("Insert name of active item: "), getcode_category(category))
        elif option == "5":
            put_item_inactive_back(input("Insert name of inactive item to put it active: "))
        elif option == "6":
            item_name = input("Insert item name: ")
            category = input("Insert category name: ")
            delete_item(item_name, getcode_category(category))
        elif option == "0":
            exit_program = 1


# ==========================================
# Global variable: list of category.
# ==========================================
hotDrinks = []
coldDrinks = []
fastFood = []
desserts = []
inactivate_items = []

if __name__ == '__main__':
    # examples Category 1: hot drinks
    insert_item("Green tea", "3.50£", 1)
    insert_item("Peppermint tea", "4.75£", 1)
    insert_item("Chamomile tea", "4.85£", 1)
    insert_item("Latte", "5.50£", 1)
    insert_item("Cappuccino", "3.55£", 1)
    insert_item("Espresso", "1.50£", 1)

    # examples Category 2: cold drinks
    insert_item("Orange juice", "4.25£", 2)
    insert_item("Pineapple juice", "4.35£", 2)
    insert_item("Coca-cola", "1.59£", 2)
    insert_item("Fanta", "1.58£", 2)
    insert_item("Sparkling", "1.50£", 2)
    insert_item("Still water", "1.50£", 2)

    # examples Category 3: fast food
    insert_item("Margarita", "6.50£", 3)
    insert_item("Hawaiian", "7.50£", 3)
    insert_item("Cheese burger", "8.50£", 3)
    insert_item("Chicken burger", "9.50£", 3)

    # examples Category 4: desserts
    insert_item("Banana bread", "4.50£", 4)
    insert_item("Floating islands", "4.50£", 4)
    insert_item("Damson crumble", "4.50£", 4)

    contextual_menu()
