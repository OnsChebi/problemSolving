##### node creation
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        #print("node created")
    
# n1=Node(10)
# n2=Node(20)
# n3=Node(30)
# print(n1.data)
# print(n2.data)
# print(n3.data)
# ###exercise3
# n1.next=n2
# n2.next=n3
# print(n1.data)
# print(n1.next.data)
# print(n1.next.next.data)
#######Exercise4
print("exercise4")
class LinkedList:
    def __init__(self):
        self.head=None
    
    def insert(self,data):
        if self.head is None:
            self.head=Node(data)
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=Node(data)
    
    def display(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next
        return
    
    def count(self):
        current=self.head
        num=0
        while current:
            num+=1
            current=current.next
        return num
    
    def sum(self):
        current=self.head
        som=0
        while current:
            som+=current.data
            current=current.next   
        return som 
    
    def findMax(self):
        if self.head is None:
            return None
        current=self.head
        max=current.data
        while current:
            if current.data>=max:
                max=current.data
            current=current.next
        return max 
    
    
    def findMin(self):
        if self.head is None:
            return None
        current=self.head
        min=current.data
        while current:
            if current.data<=min:
                min=current.data
            current=current.next
        return min
    
nl=LinkedList()
x=int(input("enter the number of nodes you want to create"))
for i in range(x):
    data=int(input(f"enter data for node {i+1}: "))
    nl.insert(data)
#print(nl.head.data)
nl.display()
print("Number of nodes in the linked list:", nl.count())
print("Sum of all node data in the linked list:", nl.sum())
print("Maximum value in the linked list:", nl.findMax())

    