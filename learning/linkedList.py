##### node creation
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
    print("node created")
node=Node(5)
print(node.data)