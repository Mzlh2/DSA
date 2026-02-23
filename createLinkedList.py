class Node:
    def __init__(self, mydata):
        self.data = mydata
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertatfirstposition(self, myData):
        newNode = Node(myData)
        newNode.address = self.head
        self.head = newNode

    def traversal(self):
        currentNode = self.head
        while currentNode !=None:
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.address
myLinkedList = LinkedList()
myLinkedList.insertatfirstposition(10)
myLinkedList.insertatfirstposition(20)
myLinkedList.insertatfirstposition(30)
myLinkedList.traversal()