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
    print("\n\nThese are some of the last orders...")
    print('************************************\n')
    order_list = history.get_history_list(True)
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

    print("\n\nWho is ordering today", names)
    while user == "":
        user = input('\nPlease enter the user name who is going to choose today... ')
    
    return(user)



if __name__ == "__main__":

    # if curses.wrapper(intro.main): # TODO: IRIS, un comment this
    show_last_orders()
    user = promp_user()
    search_query = (food_tree.start_app())  # make sure there is a return at the end of one value
    results = scraper.scrape_yelp(search_query)  # searches yelp and gets/returns results

    #     # show_results.show() which renders all the results of the search

    history.add_order_to_history(user, search_query)
    # history.display_orders_history()
    # exit.goodbye() which runs the thank you message / closes program
