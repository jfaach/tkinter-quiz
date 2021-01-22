class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def isLeaf(self):
        if self.right is None and self.left is None:
            return True
        return False

    def insertLeftNode(self, node):
        node.right = self.left
        self.left = node

    def insertRightNode(self, node):
        node.right = self.right
        self.right = node

    """
    Iterate tree
    """

    def printTree(self):
        print(self.value)
        if self.left:
            self.left.printTree()
        if self.right:
            self.right.printTree()


if __name__ == "__main__":
    rootNode = Node(
        "Vive na agua?",
        Node("Jacare"),
        Node("Macaco"),
    )

    parentNode = rootNode
    node = rootNode
    direction = ""

    while True:
        if node.isLeaf():
            answer = input(f"O animal escolhido é {node.value} ? <Y/N>: ")
            if answer.upper() == "Y":
                print("Acertei !!")
                parentNode = rootNode
                node = rootNode
            elif answer.upper() == "N":
                animalName = input(f"Qual o animal? ")
                animalFeature = input(
                    f"O que {animalName} tem que {node.value} não tem ? "
                )
                animalNode = Node(animalFeature, Node(animalName))
                if direction == "left":
                    parentNode.insertLeftNode(animalNode)
                elif direction == "right":
                    parentNode.insertRightNode(animalNode)
                node = rootNode
                parentNode = rootNode
            else:
                print("Please enter yes or no.")
        else:
            answer = input(f"O animal escolhido {node.value} ? <Y/N>: ")
            if answer.upper() == "Y":
                parentNode = node
                node = node.left
                direction = "left"
            elif answer.upper() == "N":
                parentNode = node
                node = node.right
                direction = "right"
            else:
                print("Please enter yes or no.")