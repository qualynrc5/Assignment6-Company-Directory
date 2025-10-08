class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.
    '''
    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        # Handle if root does not exist
        if self.root is None:
            print("❌ Cannot insert. Please add a team lead first.")
            return

        if current_node is None:
            current_node = self.root

        # If current node matches manager name
        if current_node.name == manager_name:
            if side == "left":
                if current_node.left is None:
                    current_node.left = EmployeeNode(employee_name)
                    print(f"✅ {employee_name} added to the LEFT of {manager_name}")
                else:
                    print(f"❌ Left side of {manager_name} is already occupied.")
            elif side == "right":
                if current_node.right is None:
                    current_node.right = EmployeeNode(employee_name)
                    print(f"✅ {employee_name} added to the RIGHT of {manager_name}")
                else:
                    print(f"❌ Right side of {manager_name} is already occupied.")
            else:
                print("❌ Invalid side. Please choose 'left' or 'right'.")
            return

        # Recursively search through left and right branches
        if current_node.left:
            self.insert(manager_name, employee_name, side, current_node.left)
        if current_node.right:
            self.insert(manager_name, employee_name, side, current_node.right)

    def print_tree(self, node=None, level=0):
        # Handle empty tree
        if self.root is None:
            print("❌ The team structure is empty.")
            return

        if node is None:
            if level == 0:
                node = self.root
            else:
                return

        # Print current node with indentation based on level
        print("  " * level + f"- {node.name}")

        # Recurse through children
        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)


# Test your code here
# Example:
# company = TeamTree()
# company.root = EmployeeNode("Jordan")
# company.insert("Jordan", "Taylor", "right")
# company.insert("Jordan", "Riley", "left")
# company.insert("Riley", "Dana", "right")
# company.insert("Riley", "Morgan", "left")
# company.print_tree()


# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    company_directory()


"""
--- Design Memo ---
How did recursive insertion work?
Recursive insertion worked by checking each node repeatedly until the correct manager was found, then attaching the new employee as left or right child. The process begins 
at the root which is the team lead and moves downward. If current node matches manager, the new employee is placed in chosen side. If not, the function searches left and 
right subtrees unti manager is located. Eliminating a need for loops. 

What challenges did you face when finding the right spot for a new employee? I struggled with testing my code. At first, when I inserted a team lead, a manager, and a new employee, only the manager would appear in the output.
After re-reading how the team structure should be organized and what the printed result was supposed to look like, I was able to adjust my code and get it working correctly. 
Understanding how to manage these edge cases and make sure the recursive calls returned control at the right time took some experimenting. It was also tricky to prevent 
overwriting an existing left or right employee, but once I figured out how the recursive insertion worked, everything started to make more sense.

When might trees be preferable to other data structures in real-world systems?
Trees are useful when we need to show relationships that have different levels, like a company’s management structure, folders in a computer, or an organizational chart.
They make it easier to add, find, and display information in a way that shows who reports to whom or how items are grouped. Unlike lists or arrays, which store data in a
straight line, trees show connections between items in a branching structure. This makes them a good choice when one piece of data depends on or is connected to another.

"""