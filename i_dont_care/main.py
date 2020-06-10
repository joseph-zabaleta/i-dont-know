import curses
from i_dont_care import (
    intro,
    food_tree,
    scraper,
    history
    # show_results,
    # exit
)

def promp_user():
    user = ""
    # all_users =  history.get_users()

    while user == "":
        user = input('Please enter the user who is going to choose today... ')

    return(user)

if __name__ == "__main__":

    # if curses.wrapper(intro.main): # TODO: IRIS, un comment this
    user = promp_user()
    # print(user)
    search_query = (food_tree.start_app())  # make sure there is a return at the end of one value
    results = scraper.scrape_yelp(search_query)  # searches yelp and gets/returns results

        # show_results.show() which renders all the results of the search
    # print('the food to order is ', search_query)

    history.add_order_to_history(user, search_query)
    # history.display_orders_history()
    # exit.goodbye() which runs the thank you message / closes program
