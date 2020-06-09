import requests
from bs4 import BeautifulSoup


def get_location():
    return 'seattle'


#this works
def scrape_yelp(item):

    area = get_location()
    # print (f"Searchig information of {item} in {area}...")
    yelp_url = f'https://www.yelp.com/search?find_desc={item}&find_loc={area}&ns=1'

    print(yelp_url)
    resposne = requests.get(yelp_url)
    content = resposne.content
    soup = BeautifulSoup(content, "html.parser")


    # with open('../assets/test-data.txt', 'w+') as f:    
    with open('./assets/test-data.txt', 'w+') as f:        
        for item in result[4:10]:

            
            # getting the names
            name = item.find('a', class_="lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE")
            print(name.next_element)
            # phone
            phone = item.find('p', class_="lemon--p__373c0__3Qnnj text__373c0__2Kxyz text-color--black-extra-light__373c0__2OyzO text-align--right__373c0__1f0KI text-size--small__373c0__3NVWO")
            print(phone.next_element)
             # address1
            address1 = item.find('span', class_="lemon--span__373c0__3997G raw__373c0__3rcx7")
            print(address1.next_element)
            # #  # address2 NOT ACCURATE: TODO: Find address2
            # address2 = item.find('p', class_="lemon--p__373c0__3Qnnj text__373c0__2Kxyz text-color--black-extra-light__373c0__2OyzO text-align--right__373c0__1f0KI text-size--small__373c0__3NVWO")
            # print(address2.next_element.next_element.text.strip())


            # reviews
            reviews = item.find('p', class_="lemon--p__373c0__3Qnnj text__373c0__2Kxyz text-color--black-extra-light__373c0__2OyzO text-align--left__373c0__2XGa-")
            print(reviews.next_element + "...\"")
            # price
            price = item.find('span', class_="lemon--span__373c0__3997G text__373c0__2Kxyz priceRange__373c0__2DY87 text-color--black-extra-light__373c0__2OyzO text-align--left__373c0__2XGa- text-bullet--after__373c0__3fS1Z")
            print(price.next_element)
            # html: TODO: find the url
            # yelp_url = item.find("a", class_="lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE")
            # print(yelp_url.next_element.href.text.strip())

            print("\n")

            item = str(item)
            f.write(f"\n{'*'*50}\n")
            f.write(item)
            f.write(f"\n{'*'*50}\n")
    
    #    1. Red Mill Burgers1267$$Burgers(206) 783-6362312 N 67th StPhinney Ridge“The hamburgers are good sized as the service was prompt. I did feel like the table and chairs were a bit "sticky", and I really wish they bad a kids menu.” more
   


"""
the name is inside :
<a class="lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE" href="/biz/red-mill-burgers-seattle?osq=hamburguers" name="Red Mill Burgers" rel="" target="">Red Mill Burgers</a>


price
<span class="lemon--span__373c0__3997G text__373c0__2Kxyz priceRange__373c0__2DY87 text-color--black-extra-light__373c0__2OyzO text-align--left__373c0__2XGa- text-bullet--after__373c0__3fS1Z">$$</span>


phone
<p class="lemon--p__373c0__3Qnnj text__373c0__2Kxyz text-color--black-extra-light__373c0__2OyzO text-align--right__373c0__1f0KI text-size--small__373c0__3NVWO">(206) 783-6362</p>

review, be careful , have more tags inside
<p class="lemon--p__373c0__3Qnnj text__373c0__2Kxyz text-color--black-extra-light__373c0__2OyzO text-align--left__373c0__2XGa-">“The <span class="lemon--span__373c0__3997G text__373c0__2Kxyz text-color--normal__373c0__3xep9 text-align--left__373c0__2XGa- text-weight--bold__373c0__1elNz text-size--inherit__373c0__2fB3p">hamburgers</span> are good sized as the service was prompt. I did feel like the table and chairs were a bit "sticky", and I really wish they bad a kids menu.”<span class="lemon--span__373c0__3997G text__373c0__2Kxyz text-color--inherit__373c0__1lczC text-align--left__373c0__2XGa- text-size--inherit__373c0__2fB3p"> 

address 1
<span class="lemon--span__373c0__3997G raw__373c0__3rcx7">312 N 67th St</span>

address 2
<p class="lemon--p__373c0__3Qnnj text__373c0__2Kxyz text-color--black-extra-light__373c0__2OyzO text-align--right__373c0__1f0KI text-size--small__373c0__3NVWO">Phinney Ridge</p>
<p class="lemon--p__373c0__3Qnnj text__373c0__2Kxyz text-color--black-extra-light__373c0__2OyzO text-align--right__373c0__1f0KI text-size--small__373c0__3NVWO">

reviews
<span class="lemon--span__373c0__3997G text__373c0__2Kxyz reviewCount__373c0__2r4xT text-color--black-extra-light__373c0__2OyzO text-align--left__373c0__2XGa-">1267</span>

"""

