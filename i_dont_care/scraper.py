import requests
import time 
from bs4 import BeautifulSoup


def get_location():

    # # City/Area location

    # # option 1 - manual prompt
    # # city_prompt = "What city do you live in?"
    
    # # option 2 - ip address
    # # Mad respect to :https://www.youtube.com/watch?v=OlSQ2TEP3oc
    res = requests.get('https://ipinfo.io/')
    # # print(res.text)
    data = res.json()
    city_prompt = data['city']

    print("\n\n")
    change = input("We are going to search for restaurants in " + city_prompt + " do you whant to change location? (yes/no) ")
    if change.upper() == 'YES' or change.upper() == 'Y':
        city_prompt = ""
        while city_prompt == "":
            city_prompt = input("Please enter the location to search in... ")        

    return (city_prompt)



def scrape_yelp(item):

    area = get_location()
    print (f"\nSearching information of {item} in {area}...\n")
    time.sleep(1)
    yelp_url = f'https://www.yelp.com/search?find_desc={item}&find_loc={area}&ns=1'

    # print(yelp_url)
    resposne = requests.get(yelp_url)
    content = resposne.content
    soup = BeautifulSoup(content, "html.parser")

    result = soup.find_all('li', class_="lemon--li__373c0__1r9wz border-color--default__373c0__3-ifU")


    print('************ SEARCH RESULTS....\n')
    # with open('./assets/test-data.txt', 'w+') as f:        
    for item in result[4:]:
        
        # getting the names
        name = item.find('a', class_="lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE")
        if not name : 
            continue
        print("\n")
        print("***************")
        print('RESTAURANT: ' + name.next_element)
        # phone
        phone = item.find('p', class_="lemon--p__373c0__3Qnnj text__373c0__2Kxyz text-color--black-extra-light__373c0__2OyzO text-align--right__373c0__1f0KI text-size--small__373c0__3NVWO")
        if not phone : 
            continue

        phone = phone.text.strip()
        print(phone)


            # address1
        address1 = item.find('span', class_="lemon--span__373c0__3997G raw__373c0__3rcx7")
        if not address1 : 
            continue

        address1 = address1.next_element 
        address1 = str(address1)  

        if address1[0] == '<':
            start_idx = address1.find('>') + 1
            end_idx = address1[1].find('<') - 3
            address1 = address1[start_idx:end_idx]

        print('ADDRESS: ' + address1)

        # address2 NOT ACCURATE: TODO: Find address2
        address2 = item.find_all('p', class_="lemon--p__373c0__3Qnnj text__373c0__2Kxyz text-color--black-extra-light__373c0__2OyzO text-align--right__373c0__1f0KI text-size--small__373c0__3NVWO")
        address2 = address2[-1].text.strip()
       

        if address1 not in address2:
            print('AREA: ' + address2)


        # reviews
        reviews = item.find('p', class_="lemon--p__373c0__3Qnnj text__373c0__2Kxyz text-color--black-extra-light__373c0__2OyzO text-align--left__373c0__2XGa-")
        if not reviews : 
            continue
        print('REVIEW: ' + reviews.next_element + "...\"")   
        # price
        price = item.find('span', class_="lemon--span__373c0__3997G text__373c0__2Kxyz priceRange__373c0__2DY87 text-color--black-extra-light__373c0__2OyzO text-align--left__373c0__2XGa- text-bullet--after__373c0__3fS1Z")
        if not price : 
            continue
        print('PRICE: ', price.next_element)

        # html: TODO: find the url
        # yelp_url = item.find("a", class_="lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE")
        # print(yelp_url.next_element.href.text.strip())

        

    
