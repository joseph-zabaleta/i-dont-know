import json
from datetime import date

def get_full_info():
    """
    This method return a array with 3 elements, each element is a list, 
    where possition 0 is the title of the list: 
    array in position 0:  Number of orders by user
    array in position 1:  List of orders by food category
    array in position 2:  These are all the orders realizaded
    """
    list_return = []
    list_users = [] # internal working list
    list_orders = []  #i nternal working list
    list_users_return = [] # this is the returning array, in list_return, at position 0. Number of orders by user
    list_orders_return = [] # this is the returning array, list_return, at position 1. List of orders by food category
    list_history_return = [] # this is the returning array, list_return, at position 2. These are all the orders realizaded

    order_history = get_history()
    
    if not order_history :
        return list_return
    

    for order in order_history["orders"]:
        list_users.append(order["user"])
        list_orders.append(order["order"])
    
    unique_users_names = get_unique_list_values(list_users)
    unique_food_names = get_unique_list_values(list_orders)

    # Filling list_users_return
    tupple_users = (list_users)  # create tupples to use count method
    list_users_return.append('Number of orders by user')
    for user in unique_users_names:
        list_users_return.append(user + " has ordered " + str(tupple_users.count(user)) + " times.")


    # Filling list_orders_return
    list_orders_return.append("Orders by food category")    
    tupple_orders = (list_orders) # create tupples to use count method
    for food in unique_food_names:
        list_orders_return.append(food + " has been ordered " + str(tupple_orders.count(food)) + " times.")

    # Filling list_history_return
    list_history_return = get_history_list(True)
    list_history_return.insert(0, "History of all the orders")

    list_return.append(list_users_return)
    list_return.append(list_orders_return)
    list_return.append(list_history_return)

    return list_return


# function to get unique values 
def get_unique_list_values(list_to_review):     
    unique_list = [] 
      
    # traverse for all elements 
    for item in list_to_review: 
        # check if exists in unique_list or not 
        if item not in unique_list: 
            unique_list.append(item) 

    return unique_list


def get_users():
    """
    This function returns a list with the names of the users who have placed orders.
    """
    list_users = []
    order_history = get_history()
    if not order_history : 
        return list_users

    for order in order_history["orders"]:
        list_users.append(order["user"])
    
    return get_unique_list_values(list_users)


def display_orders_by_user():
    """
    Function which displays the numbers of orders by users, and the number of times
    a specific food have been ordered.
    """
    list_users = []
    list_orders = []
    order_history = get_history()
    
    if not order_history :
        print('There are not orders saved yet....')
        return
    
    for order in order_history["orders"]:
        list_users.append(order["user"])
        list_orders.append(order["order"])
    
    unique_users_names = get_unique_list_values(list_users)
    unique_food_names = get_unique_list_values(list_orders)

    # create tupples to use count method
    tupple_users = (list_users)
    print("Number of order by user... \n")
    for user in unique_users_names:
        print("     " + user + " has ordered " + str(tupple_users.count(user)) + " times.")

    # create tupples to use count method
    tupple_orders = (list_orders)
    print("\n\n")
    print("Number of orders by type... \n")
    for food in unique_food_names:
        print("     " + food + " has been ordered " + str(tupple_orders.count(food)) + " times.")


def display_orders_history():
    order_list = get_history_list(True)

    if len(order_list) == 0:
        print('There are not orders saved yet....')
        return
    
    print("\n\n")
    print('These are the orders so far...\n\n')
    for order in order_list:
        print(order)


def get_history_list(reversed = None):
    """
    This method returns all the orders in a list, where each order is in one position on the array.
    And returns in in the indicated order
    """
    try:
        order_list = []
        with open('./assets/orders_history.txt') as json_file:
            history = json.load(json_file)        

        for order in history["orders"]:
            order_info = "On " + order['date'] + ", " + order['user'] + " ordered " + order['order']
            order_list.append(order_info)        
        
        if reversed : order_list.reverse()
        
        return order_list
    except:
        return []


def get_history():
    """
    Returns all the ordering information in json style
    """
    try:
        with open('./assets/orders_history.txt') as json_file:
            history = json.load(json_file)
            return history
    except:
        return None


def add_order_to_history(user, food, order_date = None):
    if not order_date : order_date = date.today()

    order_history = get_history()
    if not order_history:
        order_history = {} 
        order_history["orders"] = []
        order_history["orders"].append({
            "user" : user,
            "date" : str(order_date),
            "order" : food
        })
    else:
        order_history["orders"].append({
            "user" : user,
            "date" : str(order_date),
            "order" : food
        })

    with open('./assets/orders_history.txt', 'w') as outfile:
      json.dump(order_history, outfile)


def load_dummy_data():
    add_order_to_history('Skyler', 'Indian','2020-03-29')
    add_order_to_history('JB', 'Tai','2020-04-15')
    add_order_to_history('JB', 'Pizza','2020-04-15')
    add_order_to_history('Ahmad', 'Mexican','2020-04-18')
    add_order_to_history('Skyler', 'Italian','2020-05-03')
    add_order_to_history('JB', 'Hamburguers','2020-05-14')
    add_order_to_history('Aliya', 'Carne Asada','2020-05-19')
    add_order_to_history('Skyler', 'Sushi','2020-05-22')
    add_order_to_history('JB', 'Pizza','2020-05-24')
    add_order_to_history('Ahmad', 'Tacos','2020-05-29')
    add_order_to_history('JB', 'Tacos','2020-06-02')
    add_order_to_history('Skyler', 'Hamburguers','2020-06-07')
    add_order_to_history('Ahmad', 'Sushi','2020-06-09')

