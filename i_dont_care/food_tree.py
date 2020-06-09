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


    def validate_answer(self, prompt, answer):
        return_dict = {
            "is_valid": "",
            "selected_option": "",
            "word_selected_option": "",
            "prompt" : ""
            }

        original_prompt = prompt
        prompt = prompt.replace(' or ','')
        prompt = prompt.replace('?','')
        prompt = prompt.replace('.','')
        #obtain question A and B
        pos_opt_A = prompt.find("A)") + 2
        pos_opt_B = prompt.find("B)")
        question_A = prompt[pos_opt_A:pos_opt_B].strip()
        pos_opt_B += 2
        question_B = prompt[pos_opt_B:].strip()

        possible_answers_A = []
        possible_answers_A.append('a')
        possible_answers_A.append('A')
        possible_answers_A.append('1')
        possible_answers_A.append(question_A)
        possible_answers_A.append(question_A.upper())
        possible_answers_A.append(question_A.lower())
        possible_answers_A.append('Im leaf')
        possible_answers_B = []
        possible_answers_B.append('b')
        possible_answers_B.append('B')    
        possible_answers_B.append('2')
        possible_answers_B.append(question_B)
        possible_answers_B.append(question_B.upper())
        possible_answers_B.append(question_B.lower())

        answer = answer.strip()

        if answer in possible_answers_A or answer in possible_answers_B:
            return_dict["is_valid"] = True
            if answer in possible_answers_A:
                return_dict["selected_option"] = 'A'
                return_dict["word_selected_option"] = question_A
            else:
                return_dict["selected_option"] = 'B'
                return_dict["word_selected_option"] = question_B

            return_dict["prompt"] = original_prompt
        else:
            return_dict["is_valid"] = False

        return return_dict


    def prompt_questions(self, tree):
        """
        This method traverse the tree, prompting questions, and then moving depending on the answer to left or right,
        also saving a history on the visited nodes and user answers
        """
        history = []

        if tree.root == None : 
            raise Exception('The tree is empty')
            return 

        def traverse(current_node):
            if not current_node : return

            validate_answer = False
            while not validate_answer:
                answer = ''
                if current_node.left and current_node.right:
                    answer = input(current_node.question + '... ')
                else:
                    answer = "Im leaf"  # this is a system valid answer and will execute the while

                answer_list = self.validate_answer(current_node.question, answer)

                validate_answer = answer_list["is_valid"] # true or false

            history.append(answer_list["word_selected_option"])


            # selected_option = answer_list[1]    
            selected_option = answer_list["selected_option"]  # A or B
            if selected_option == 'A':
                traverse(current_node.left)
            if selected_option == 'B':
                traverse(current_node.right)

        traverse(tree.root)
        # clear the last inputs because the last one is not complete
        history.pop()
        
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
    # bst = BinarySearchTree()
    # print(bst)
    #  Left
    tree.add(1000, 'Do you want A) Fast food or B) Sit down')
    tree.add(500, 'A) Sandwich or B) Cheesburger')
    tree.add(450, 'Sandwich')
    tree.add(750, 'Cheesburger')

    #  right
    tree.add(1500, 'Do you want A) Mexican or B) French')
    tree.add(1250, 'Mexican')
    tree.add(1750, 'French')

    # tree = bst.BreadthFirst(bst)
    # for level in tree:
    #     print(level)



def start_app():
    bst = BinarySearchTree()
    create_tree(bst)
    history = bst.prompt_questions(bst)
    return history[-1]



# if __name__ == "__main__":
#     start_app()
    