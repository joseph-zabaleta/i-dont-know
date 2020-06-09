from collections import deque
class Node:
    def __init__(self, value, question, left = None,  right = None):
        self.value = value
        self.left = left
        self.right = right
        self.question = question

    def __str__(self):
        return f"Node: {self.value}"

class BinaryTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        if not self.root : return 'The root is empty.'

        return f'The root is {self.root.value}'

    def preOrder(self):
        list_return = []

        if self.root == None : return list_return

        def traverse(current_node):
            if not current_node : return

            list_return.append(current_node.food)
            traverse(current_node.left)
            traverse(current_node.right)

        traverse(self.root)

        return list_return

    def inOrder(self):
        list_return = []

        if self.root == None : return list_return

        def traverse(current_node):
            if not current_node : return

            traverse(current_node.left)
            list_return.append(current_node.food)
            traverse(current_node.right)


        traverse(self.root)
        return list_return

    def postOrder(self):
        list_return = []

        if not self.root :  return list_return

        def traverse(current_node):
            if not current_node : return

            traverse(current_node.left)
            traverse(current_node.right)
            list_return.append(current_node.food)

        traverse(self.root)

        return list_return

    # added
    def BreadthFirst(self,tree):
        list_return = []

        if not tree.root : return 'The Tree is empty.'

        breadth = Queue()

        breadth.enqueue(tree.root)

        while not breadth.is_empty():
            front = breadth.dequeue()
            list_return.append(front.question)

            if front.left:
                breadth.enqueue(front.left)

            if front.right:
                breadth.enqueue(front.right)

        return list_return

    # added Jun 3rd, Challenge 18
    def FindMaximumValue(self):
        if self.root == None : return None

        current_max_value = self.root.value

        def traverse(current_node):
            nonlocal current_max_value
            if not current_node : return

            if current_node.value > current_max_value:
                current_max_value = current_node.value

            traverse(current_node.left)
            traverse(current_node.right)

        traverse(self.root)


        return current_max_value


    def prompt_questions(self, tree):
        """
        This method traverse the tree, prompting questions, and then moving depending on the answer to left or right
        """
        history = []

        if tree.root == None : return 'Empty' # TODO: put a better return

        def traverse(current_node):
            if not current_node : return

            # list_return.append(current_node.food)
            history.append(current_node.question)
            answer = ''
            if current_node.left and current_node.right:
                answer = input(current_node.question + '... ')

            # todo: uppercase, lowercase... validate input..
            if answer == 'A':
                traverse(current_node.left)
            else:
                traverse(current_node.right)

        final_op = traverse(tree.root)
        # print('The final option is', history)

        return history # the last position is the selected option
        
    
class BinarySearchTree(BinaryTree):
    def __str__(self):
        if not self.root : return 'The root is empty.'

        return f'The root is {self.root.value}, and value is {self.root.food}'


    def add(self, value, question):
        new_node = Node(value, question)

        if self.root == None :
            self.root = new_node
            return

        def traverse(current_node, new_node):

            if not current_node : return

            if new_node.value < current_node.value:
                if current_node.left == None :
                    current_node.left = new_node
                else:
                    traverse(current_node.left, new_node)
            else:
                if current_node.right == None :
                    current_node.right = new_node
                else:
                    traverse(current_node.right, new_node)


        traverse(self.root, new_node)


    def contains(self, value):
        if not self.root: return False

        def traverse(current_node, value_to_search):
            if not current_node : return False
            if current_node.value == value_to_search :
                return True
            else:
                if value_to_search < current_node.value :
                    return traverse(current_node.left, value_to_search)
                else:
                    return traverse(current_node.right, value_to_search)

        return traverse(self.root, value)

# added
class Queue:
    def __init__(self):
        self.storage = deque()

    def enqueue(self, value):
        self.storage.appendleft(value)

    def dequeue(self):
        if not self.is_empty():
            return self.storage.pop()

    def peek(self):
        return self.storage[-1]

    def is_empty(self):
        return len(self.storage) == 0


def create_tree(tree):

# Breakfast Tree
    tree.add(100, 'Do you want A) Fast food or B) Sit down?')
    # Sit Down
    tree.add(150, 'Cafe')
    # Fast Food
    tree.add(50, 'Do you want something sweet? A) Yes or B) No?')
    # No to Sweet
    tree.add(75, 'Coffee')
    # Yes to Sweet
    tree.add(25, 'Do you want want something A) Cheap or B) Fancy?')
    # Cheap
    tree.add(20, 'Donuts')
    # Fancy
    tree.add(75, 'Bakery')

# Lunch/Dinner Tree
    tree.add(500, 'Do you want A) Meat or B) Seafood?')
    
    ### Seafood
    tree.add(675, 'Do you want A) Fast food or B) Sit down?')
    # Fast
    tree.add(670, 'Poke')
    # Sit Down
    tree.add(685, 'Do you want your seafood A) raw or B) cooked?')
    # Raw
    tree.add(680, 'Sushi')
    # Cooked
    tree.add(690, 'Seafood')

    
    ### Meat ###
    tree.add(450, 'Do you want your meat A) Spicy or B) not Spicy?')
    ## Spicy ##
    tree.add(460, 'Do you like curry A) Yes or B) No?')
    # Yes to curry
    tree.add(455, 'Indian')
    # No to curry
    tree.add(465, 'Do you like soup/broth A) Yes or B) No?')
    # Yes to Soup/Broth
    tree.add(464, 'Asian')
    # No to Soupl/Broth
    tree.add(466, 'Mexican')
    ## No Spicy ##
    tree.add(425, 'Do you want A) Fast food or B) Sit down?')
    # Sit Down
    tree.add(435, 'Diner')
    # Fast
    tree.add(410, 'Do you want a A) Sandwich or B) Burger?')
    # Sandwich
    tree.add(405, 'Delicatessen')
    # Burger
    tree.add(415, 'Burger')



#### 6/8 Original
    # #  Left
    # tree.add(1000, 'Do you want A) Fast food or B) Sit down')
    # tree.add(500, 'A) Sandwich or B) Cheesburger')
    # tree.add(450, 'Sandwich')
    # tree.add(750, 'Cheesburger')

    # #  right
    # tree.add(1500, 'Do you want A) Mexican or B) French')
    # tree.add(1250, 'Mexican')
    # tree.add(1750, 'French')


def start_app():
    bst = BinarySearchTree()
    create_tree(bst)
    history = bst.prompt_questions(bst)
    return history[-1]



# if __name__ == "__main__":
#     start_app()
    