import requests
from bs4 import BeautifulSoup


# city = 'seattle'

# import seach query food, do_web_scraping(history[-1])
# item = 'italian'


def scrape_yelp(item):
    yelp_url = f'https://www.yelp.com/search?find_desc={item}&find_loc=seattle&ns=1'
    resposne = requests.get(yelp_url)
    content = resposne.content
    soup = BeautifulSoup(content, "html.parser")
  
    result = soup.find_all('li', class_="lemon--li__373c0__1r9wz border-color--default__373c0__3-ifU")

    with open('../assets/test-data', 'w+') as f:
        for item in result:

            # result_name = soup.find_all('a', class_="lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE")
            # print(result_name)
            
            item = item.text.strip()
            f.write(f"\n{'*'*50}\n")
            f.write(item)
            f.write(f"\n{'*'*50}\n")
            
            # f.write('\n*****\n')
            # f.write(str(item))
            # f.write('\n*****\n')
   

    # print(result[0].text.strip())
    # return len(result)

# print(test_list(yelp_url))

# i believe this link have all the restaurants options ....
# <ul class="lemon--ul__373c0__1_cxs undefined list__373c0__2G8oH">

# ********************************************************************

# def test_three(url):
#     response = requests.get(yelp_url)
#     full_content = response.content
#     soup = BeautifulSoup(content, "html.parser")


#     full_result = soup.find_all('li', class_="lemon--li__373c0__1r9wz border-color--default__373c0__3-ifU")

#     for item in full_result:
#         collection.append(item.div.text.strip())