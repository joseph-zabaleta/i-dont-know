import curses
from i_dont_care import (
    intro,
    food_tree,
    scraper,
    # show_results,
    # exit
)


if __name__ == "__main__":

    # if curses.wrapper(intro.main):
        search_query = (food_tree.start_app())  # make sure there is a return at the end of one value

        results = scraper.scrape_yelp(search_query)  # searches yelp and gets/returns results

        # show_results.show() which renders all the results of the search

    # exit.goodbye() which runs the thank you message / closes program
