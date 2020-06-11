import requests
import time 
from bs4 import BeautifulSoup
from i_dont_care import main
from termcolor import cprint
# Resource / Inspiration for Getting location:
# Mad respect to :https://www.youtube.com/watch?v=OlSQ2TEP3oc



def get_location():

    # Backup option of getting location - manual prompt
    # city_prompt = input("What city do you live in?")
    
    # Main option of getting location - ip address
    res = requests.get('https://ipinfo.io/')
    data = res.json()
    city_prompt = data['city']

    print("\n\n")
    change = input("We are going to search for restaurants in " + city_prompt + " do you want to change location? (yes/no) ")
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

    response = requests.get(yelp_url)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")

    result = soup.find_all('li', class_="lemon--li__373c0__1r9wz border-color--default__373c0__3-ifU")

    cprint('*************** SEARCH RESULTS ***************', 'cyan', attrs=['bold'])
           
    for item in result[4:]:
        
        # Getting/Printing Restaurant Name
        name = item.find('a', class_="lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE")
        if not name : 
            continue
        
        cprint("\n***************", 'cyan', attrs=['bold'])

        print('RESTAURANT: ' + name.next_element)

        # Getting/Printing Phone Number
        phone = item.find('p', class_="lemon--p__373c0__3Qnnj text__373c0__2Kxyz text-color--black-extra-light__373c0__2OyzO text-align--right__373c0__1f0KI text-size--small__373c0__3NVWO")
        if not phone : 
            continue

        phone = phone.text.strip()
        print('PHONE: ' + phone)

        # Getting/Printing Address
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

        # Getting/Printing Area
        address2 = item.find_all('p', class_="lemon--p__373c0__3Qnnj text__373c0__2Kxyz text-color--black-extra-light__373c0__2OyzO text-align--right__373c0__1f0KI text-size--small__373c0__3NVWO")
        address2 = address2[-1].text.strip()
       
        if address1 not in address2:
            print('AREA: ' + address2)


        # Getting/Printing Reviews
        reviews = item.find('p', class_="lemon--p__373c0__3Qnnj text__373c0__2Kxyz text-color--black-extra-light__373c0__2OyzO text-align--left__373c0__2XGa-")
        if not reviews : 
            continue
        print('REVIEW: ' + reviews.next_element + "...\"") 

        # Getting/Printing Price
        price = item.find('span', class_="lemon--span__373c0__3997G text__373c0__2Kxyz priceRange__373c0__2DY87 text-color--black-extra-light__373c0__2OyzO text-align--left__373c0__2XGa- text-bullet--after__373c0__3fS1Z")
        if not price : 
            continue
        print('PRICE: ', price.next_element)

    # Return to main menu
    cprint("\n***************************************", color='red', attrs=['bold'])
    something = input('Press enter to return to the main menu.')

    if something or not something:
        main.start_app()


        

    
