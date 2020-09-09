
class Node:
    def __init__(self, value, question, left=None, right=None):
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
        if not self.root:
            return "The root is empty."

        return f"The root is {self.root.value}"

    def pre_order(self):
        """This is a Depth First traversal method. It prioritizes printing the `root` first, then looks to print `left` if left is not `None`, and lastly looks `right`."""
        collection = []

        def walk(root):
            if not root:
                return

            # <<< root >>>
            collection.append(root.question)

            # <<< left
            walk(root.left)

            # right >>>
            walk(root.right)

        # end
        walk(self.root)

        return collection
 
    def validate_answer(self, prompt, answer):
        return_dict = {
            "is_valid": "",
            "selected_option": "",
            "word_selected_option": "",
            "prompt": "",
        }


        original_prompt = prompt

        prompt = prompt.replace(" or ", "")
        prompt = prompt.replace("?", "")
        prompt = prompt.replace(".", "")

        # obtain question A and B
        pos_opt_A = prompt.find("A)") + 2
        pos_opt_B = prompt.find("B)")

        if len(original_prompt.split()) == 1:
            question_A = question_B = original_prompt
        else:
            question_A = prompt[pos_opt_A:pos_opt_B].strip()
            pos_opt_B += 2
            question_B = prompt[pos_opt_B:].strip()

        # all A answers
        possible_answers_A = []
        possible_answers_A.append("a")
        possible_answers_A.append("A")
        possible_answers_A.append("1")
        possible_answers_A.append(question_A)
        possible_answers_A.append(question_A.upper())
        possible_answers_A.append(question_A.lower())
        possible_answers_A.append("Im leaf")

        # all B answers
        possible_answers_B = []
        possible_answers_B.append("b")
        possible_answers_B.append("B")
        possible_answers_B.append("2")
        possible_answers_B.append(question_B)
        possible_answers_B.append(question_B.upper())
        possible_answers_B.append(question_B.lower())

        answer = answer.strip()

        if answer in possible_answers_A or answer in possible_answers_B:
            return_dict["is_valid"] = True
            if answer in possible_answers_A:
                return_dict["selected_option"] = "A"
                return_dict["word_selected_option"] = question_A
            else:
                return_dict["selected_option"] = "B"
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

        if tree.root == None:
            raise Exception("The tree is empty")
            return

        def traverse(current_node):
            if not current_node:
                return

            validate_answer = False
            while not validate_answer:
                answer = ""
                if current_node.left and current_node.right:
                    answer = input(current_node.question + "... ")
                else:
                    answer = "Im leaf"  # this is a system valid answer and will execute the while

                answer_list = self.validate_answer(current_node.question, answer)

                validate_answer = answer_list["is_valid"]  # true or false

            history.append(answer_list["word_selected_option"])

            selected_option = answer_list["selected_option"]  # A or B
            if selected_option == "A":
                traverse(current_node.left)
            if selected_option == "B":
                traverse(current_node.right)

        traverse(tree.root)

        return history  # the last position is the selected option


class BinarySearchTree(BinaryTree):
    def __str__(self):
        if not self.root:
            return "The root is empty."

        return f"The root is {self.root.value}, and value is {self.root.food}"

    def add(self, value, question):
        new_node = Node(value, question)

        if self.root == None:
            self.root = new_node
            return

        def traverse(current_node, new_node):

            if not current_node:
                return

            if new_node.value < current_node.value:
                if current_node.left == None:
                    current_node.left = new_node
                else:
                    traverse(current_node.left, new_node)
            else:
                if current_node.right == None:
                    current_node.right = new_node
                else:
                    traverse(current_node.right, new_node)

        traverse(self.root, new_node)

 
def create_tree(tree, pref):
    """This will create the initial tree for the application to run off. It has two required arguments, a Binary Search Tree and a preference of breakfast or lunch/dinner.
    """

    if pref == "Breakfast":
        # Breakfast Tree
        tree.add(100, "Do you want A) Fast food or B) Sit down?")
        # Sit Down
        tree.add(150, "Cafe")
        # Fast Food
        tree.add(50, "Do you want something sweet? A) Yes or B) No?")
        # No to Sweet
        tree.add(75, "Coffee")
        # Yes to Sweet
        tree.add(25, "Do you want want something A) Cheap or B) Fancy?")
        # Cheap
        tree.add(20, "Donuts")
        # Fancy
        tree.add(30, "Bakery")

    if pref == "Lunch/Dinner":
        # Lunch/Dinner Tree
        tree.add(500, "Do you want A) Meat or B) Seafood?")

        ### Seafood
        tree.add(675, "Do you want A) Fast food or B) Sit down?")
        # Fast
        tree.add(670, "Poke")
        # Sit Down
        tree.add(685, "Do you want your seafood A) raw or B) cooked?")
        # Raw
        tree.add(680, "Sushi")
        # Cooked
        tree.add(690, "Seafood")

        ### Meat ###
        tree.add(450, "Do you want your meat with A) No Spice or B) Spicy?")
        ## Spicy ##
        tree.add(460, "Do you like curry A) Yes or B) No?")
        # Yes to curry
        tree.add(455, "Indian")
        # No to curry
        tree.add(465, "Do you like soup/broth A) Yes or B) No?")
        # Yes to Soup/Broth
        tree.add(464, "Asian")
        # No to Soupl/Broth
        tree.add(466, "Mexican")
        ## No Spicy ##
        tree.add(425, "Do you want A) Fast food or B) Sit down?")
        # Sit Down
        tree.add(435, "Diner")
        # Fast
        tree.add(410, "Do you want a A) Sandwich or B) Burger?")
        # Sandwich
        tree.add(405, "Delicatessen")
        # Burger
        tree.add(415, "Burger")


def start_app():
    """ Initializing the tree the Application will utilze, Launches the series of questions to be asked, and returns the value to be passed to the web scrapper module.
    """
    bst = BinarySearchTree()
    validate_answer = False
    
    prompt = "Is this for A) Breakfast B) Lunch/Dinner? "
    while not validate_answer:    
        preference = input(prompt)    
        preference_validation =  bst.validate_answer(prompt, preference)
        validate_answer = preference_validation["is_valid"]
    
    create_tree(bst, preference_validation["word_selected_option"])
    history = bst.prompt_questions(bst)
    return history[-1]

