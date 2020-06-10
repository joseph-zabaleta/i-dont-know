import json
from datetime import date


# function to get unique values 
def get_unique_list_values(list_to_review):     
    unique_list = [] 
      
    # traverse for all elements 
    for item in list_to_review: 
        # check if exists in unique_list or not 
        if item not in unique_list: 
            unique_list.append(item) 

    return unique_list
      

def display_orders_by_user():
    list_users = []
    list_orders = []
    order_history = get_history()
    # print(order_history["orders"])
    
    if len(order_history) == 0:
        print('There are not orders saved yet....')
        return
    
    for order in order_history["orders"]:
        list_users.append(order["user"])
        list_orders.append(order["order"])
    
    unique_users_names = get_unique_list_values(list_users)
    unique_food_names = get_unique_list_values(list_orders)
    print(unique_users_names)
    print(unique_food_names)

    # x = (list_users)
    # print(x.count("Erich"))
    # print(list_orders)



def display_orders_history():
    order_list = get_history_list(True)

    if len(order_list) == 0:
        print('There are not orders saved yet....')
        return
    
    print('These are the orders so far...\n\n')
    for order in order_list:
        print(order + "\n")



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


def add_order_to_history(user, food):
    today = date.today()
    # open the file and get the info
    order_history = get_history()
    if not order_history:
        order_history = {} 
        order_history["orders"] = []
        order_history["orders"].append({
            "user" : user,
            "date" : str(today),
            "order" : food
        })
    else:
        # print (orders_file)
        order_history["orders"].append({
            "user" : user,
            "date" : str(today),
            "order" : food
        })

    with open('./assets/orders_history.txt', 'w') as outfile:
      json.dump(order_history, outfile)

def load_dummy_data():
    add_order_to_history('John', 'Indian')
    add_order_to_history('Erich', 'Tai')
    add_order_to_history('Gabriela', 'Mexican')
    add_order_to_history('Marie', 'Italian')
    add_order_to_history('Jonh', 'Hamburguers')
    add_order_to_history('Erich', 'Carne Asada')
    add_order_to_history('Erich', 'Hotcakes')
    add_order_to_history('Marie', 'Tacos')



if __name__ == "__main__":
    # load_dummy_data()
    # print(get_history_list())
    # print("\n *********")
    # print(get_history_list(True))
    # display_orders_history()
    display_orders_by_user()


