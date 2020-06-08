# IRIS PLAYGROUND

import json

food_data = {}

food_data['cuisines'] = []
food_data['cuisines'].append({
  'cuisine' : 'american',
  'menu' : {
                'hamburguers' : ['meat hamburgers', 'Chicken hamburger', 'Fish hamburger'],
                'western' : 'tbd',
                'barbecue' : 'tbd',
                'pizza' : 'tbd',
                'fastfood' : 'tbd',
                }  })
food_data['cuisines'].append({
  'cuisine' : 'mexican',
  'menu' : {
                'tacos' : 'tbd',
                'enchiladas' : 'tbd',
                'soups' : 'tbd',
                'carne asada' : 'tbd',
                'fish tacos' : 'tbd',
                }  })
food_data['cuisines'].append({
  'cuisine' : 'japanese',
  'menu' : {
                'salads' : 'tbd',
                'appetizers' : 'tbd',
                'soups' : 'tbd',
                'sashimi' : 'tbd',
                'fried fish' : 'tbd',
                }  })


food_dict_tree = {}
food_dict_tree['options'] = []
food_dict_tree['options'].append( {
    'lunch': {'cold': { 'snack': 'snab obj', 'complete meal' : 'complete obj ' }, 
              'warm' : 'warm obj'}, 
    'dinner': 'sadsd'    }) 



if __name__ == "__main__":
    # print(food_dict_tree['options'][0])
    # print(food_dict_tree['options'][0]['lunch'])


    # print('So far, so good')
    # print('food_data: \n', food_data['cuisines'])
    # print('\n************')
    # print ('There are', len(food_data['cuisines']) , ' different cuisines in the system: ')
    # for option in food_data['cuisines']:
    #   print(option['cuisine'])
    
    # print('\n************')

    # print('Showing american food')

    # print(food_data['cuisines'][0])