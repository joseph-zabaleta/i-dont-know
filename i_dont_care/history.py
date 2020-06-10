import json
from datetime import date


def get_history():
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



if __name__ == "__main__":
    # add_order_to_history('John', 'Indian')
    add_order_to_history('Erich', 'Tai')
    add_order_to_history('Gabriela', 'Mexican')
    add_order_to_history('Marie', 'Italian')
    add_order_to_history('Jonh', 'Hamburguer')
    


