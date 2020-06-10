from random import randint
import curses
from i_dont_care import (
    intro,
    food_tree,
    scraper,
    history
    # show_results,
    # exit
)


def show_last_orders():
    order_list = history.get_history_list(True)

    if len(order_list) == 0 : return
    print("\n\nThese are some of the last orders...")
    print('************************************\n')

    if len(order_list) >= 5:
        max = 5
    else:
        max = len(order_list)



    for i in range(0,max):
        print(order_list[i])



def promp_user():
    user = ""
    user_list = history.get_users()

    names = ''
    for user_names in user_list:
        names += user_names + ", "

    names += ' or new user?'

    if len(user_list) > 0 :
        print("\n\nWho is ordering today", names)

    while user == "":
        user = input('\nPlease enter the name of the person who is choosing today... ')
    
    return(user)


def get_random_food():
    food_list = ['Donuts', 'Hamburger', 'Pizza', 'Pastry', 'Italian', 'Tacos', 'Pasta', 'Meat', 'Fishfood', 'Fish tacos', 
        'Chicken', 'Lobster', 'Sandwich', 'BBQ', 'Mexican', 'Soup', 'Thai', 'Indian', 'Lebanese', 'Chinese', 'Japanese',
        'Noddle' ,'Wings' ,'Bakery' ,'Vegeratian' ,'American' ,'Ramen' ,'Korean' , 'Poke', 'Tex-Mex', 'Southern', 'Salad',
        'Noodles', 'Creperies' , 'Barbeque', 'Greek']

    random_index = randint(0,len(food_list))
    
    return food_list[random_index]



if __name__ == "__main__":
    status = curses.wrapper(intro.main)

    if status == 0:

        show_last_orders()
        user = promp_user()
        search_query = (food_tree.start_app())  # make sure there is a return at the end of one value
        results = scraper.scrape_yelp(search_query)  # searches yelp and gets/returns results
        history.add_order_to_history(user, search_query)

    elif status == 3:
        show_last_orders()
        user = promp_user()
        search_query =  get_random_food()
        results = scraper.scrape_yelp(search_query)  # searches yelp and gets/returns results
        history.add_order_to_history(user, search_query)

    # exit.goodbye() which runs the thank you message / closes program
