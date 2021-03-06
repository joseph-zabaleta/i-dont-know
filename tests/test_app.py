import pytest
from random import randint
from i_dont_care import (
    food_tree,
    history,
    intro,
    scraper,
    main
)


# Tree tests
def test_bst_create_root():
    # given        
    bst = food_tree.BinarySearchTree()
    expected = "The root is empty."
    # when
    actual = bst.__str__()
    # then
    assert actual == expected, 'Error creating an empty Binary Search Tree.'

def test_create_breakfast_tree():
    bst = food_tree.BinarySearchTree()
    food_tree.create_tree(bst, 'Breakfast')
    data = bst.pre_order()
    actual = data[-1]
    expected = 'Cafe'
    assert actual == expected

def test_create_breakfast_tree_length():
    bst = food_tree.BinarySearchTree()
    food_tree.create_tree(bst, 'Breakfast')
    data = bst.pre_order()
    actual = len(data)
    expected = 7
    assert actual == expected


def test_create_lunch_dinner_tree():
    bst = food_tree.BinarySearchTree()
    food_tree.create_tree(bst, 'Lunch/Dinner')
    data = bst.pre_order()
    actual = data[-1]
    expected = 'Seafood'
    assert actual == expected

def test_create_lunch_dinner_tree_length():
    bst = food_tree.BinarySearchTree()
    food_tree.create_tree(bst, 'Lunch/Dinner')
    data = bst.pre_order()
    actual = len(data)
    expected = 17
    assert actual == expected
    

# load_test_info() clears information and loads dummy data for testing
# History Tests
def test_get_history():
    history.load_test_info()
    data = history.get_history()
    actual = data['orders'][0]['user']
    expected = 'Skyler'
    assert actual == expected


def test_get_history_two():
    history.load_test_info()
    data = history.get_history()
    actual = data['orders'][3]['order']
    expected = 'Mexican'
    assert actual == expected


def test_get_users():
    history.load_test_info()
    data = history.get_users()
    actual = data[1]
    expected = 'JB'
    assert actual == expected


def test_get_users_two():
    history.load_test_info()
    data = history.get_users()
    actual = data[3]
    expected = 'Aliya'
    assert actual == expected
    
      
def test_history_del_add():
    history.load_test_info()    
    expected = "On 2020-03-29, Skyler ordered Indian" 
    list_history = history.get_history_list()
    actual = list_history[0]
    assert actual == expected

def test_history_del_add_two():
    history.load_test_info()    
    expected = "On 2020-06-09, Ahmad ordered Sushi" 
    list_history = history.get_history_list()
    actual = list_history[-1]
    assert actual == expected

# Main Tests
def test_random_food():
    actual = type(main.get_random_food())
    expected = type('')
    assert actual == expected
    
def test_random_food_two():
    food_list = ['Donuts', 'Hamburger', 'Pizza', 'Pastry', 'Italian', 'Tacos', 'Pasta', 'Meat', 'Fishfood', 'Fish tacos', 
        'Chicken', 'Lobster', 'Sandwich', 'BBQ', 'Mexican', 'Soup', 'Thai', 'Indian', 'Lebanese', 'Chinese', 'Japanese',
        'Noddle' ,'Wings' ,'Bakery' ,'Vegeratian' ,'American' ,'Ramen' ,'Korean' , 'Poke', 'Tex-Mex', 'Southern', 'Salad',
        'Noodles', 'Creperies' , 'Barbeque', 'Greek'] 
    random_index = randint(0,len(food_list)-1)
    actual = food_list[random_index]
    
    assert actual in food_list


# User Input test

def test_validate_answer_is_valid():
    bt = food_tree.BinaryTree()
    expected = True
    is_valid =  bt.validate_answer("Do you want A) Fast food or B) Sit down?", "A")
    actual = is_valid['is_valid']
    assert actual == expected

def test_validate_answer_is_valid_false():
    bt = food_tree.BinaryTree()
    expected = False
    is_valid =  bt.validate_answer("Do you want A) Fast food or B) Sit down?", "aa")
    actual = is_valid['is_valid']
    assert actual == expected
    
def test_validate_answer_selected_option():
    bt = food_tree.BinaryTree()
    expected = "A"
    dict_test =  bt.validate_answer("Do you want A) Fast food or B) Sit down?", "A")
    actual = dict_test['selected_option']
    assert actual == expected

def test_validate_answer_selected_option_false():
    bt = food_tree.BinaryTree()
    expected = False
    dict_test =  bt.validate_answer("Do you want A) Fast food or B) Sit down?", "aa")
    actual = dict_test['is_valid']
    assert actual == expected

def test_validate_answer_word_selected_option():
    bt = food_tree.BinaryTree()
    expected = "Fast food"
    dict_test =  bt.validate_answer("Do you want A) Fast food or B) Sit down?", "Fast food")
    actual = dict_test['word_selected_option']
    assert actual == expected

def test_validate_answer_word_selected_option_2():
    bt = food_tree.BinaryTree()
    expected = "Sit down"
    dict_test =  bt.validate_answer("Do you want A) Fast food or B) Sit down?", "B")
    actual = dict_test['word_selected_option']
    assert actual == expected