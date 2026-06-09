# ##### node creation
# class Node:
#     def __init__(self, data):
#         self.data=data
#         self.next=None
#         print("node created")
    
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
# #######Exercise4
# print("exercise4")
# class LinkedList:
#     def __init__(self):
#         self.head=None
    
#     def insert(self,data):
#         if self.head is None:
#             self.head=Node(data)
#         else:
#             current=self.head
#             while current.next:
#                 current=current.next
#                 current.next=Node(data)
    
#     def display(self):
#         current=self.head
#         while current:
#             print(current.data)
#             current=current.next
# nl=LinkedList(None)
# nl.insert(10)
# nl.insert(20)
# nl.insert(30)
# print(nl.head.data)
# print(f"displayyyyyyyyyy: {nl.display()}")