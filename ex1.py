class Node:
    def __init__(self, data):
        self.data = data
        self.nextLeft = None
        self.nextRight = None

def insertNode(headNode, insertedNode):
    searchNode = headNode
    while True:
        if(searchNode.data>insertedNode.data and searchNode.nextRight is not None):
            searchNode = searchNode.nextRight
        elif(searchNode.data>insertedNode.data and searchNode.nextRight is None):
            searchNode.nextRight = insertedNode
            break
        elif(searchNode.data<insertedNode.data and searchNode.nextLeft is not None):
            searchNode = searchNode.nextLeft
        elif(searchNode.data<insertedNode.data and searchNode.nextLeft is None):
            searchNode.nextLeft = insertedNode
            break
        elif(searchNode.data==insertedNode.data):
            if(searchNode.nextRight is not None):
                searchNode = searchNode.nextRight
            

        
def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")
