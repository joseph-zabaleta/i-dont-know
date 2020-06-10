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


def add_order_to_history(user, food, order_date = None):
    if not order_date : order_date = date.today()

    # open the file and get the info
    order_history = get_history()
    # print(order_history)
    # return
    if not order_history:
        order_history = {} 
        order_history["orders"] = []
        order_history["orders"].append({
            "user" : user,
            "date" : str(order_date),
            "order" : food
        })
    else:
        # print (orders_file)
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


if __name__ == "__main__":
    # load_dummy_data()
    # print(get_history_list())
    # print("\n *********")
    # print(get_history_list(True))
    # display_orders_history()
    # print("\n")
    # display_orders_by_user()
    print(get_users())

