import webbrowser
webbrowser.open("url")

#list in reverse
data = [1, 2, 3]
print(data[::-1])

def move_pos():
    pass
#unpacking data
data = [10, 20 ,30]
move_pos(*data)

#sets no duplicates
pets = []
print(list(set(pets)))

#all() check or any()
conditions = [

]
if all(conditions):
    pass

#joining
names = ["first name", "last name"]
full_name = " ".join(names)

#list comprehension
pets = ["animals"]
cleaned = [pet for pet in pets if pet not in["conditions"]]

#get index
for i, pet in enumerate(pets):
    print(pet, i)

#flatten list
pairs = []
flat = [item for pair in pairs for item in pair]

#comparing objects override same value
class Container():
    def __init(self, data):
        self.data = data

def __eq__(self, other):
    return self.data == other.data

Container.__eq__ = __eq__
x = Container(5)
y = Container(5)
print(x == y)

#iterator
import itertools

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, b + a

print(list(itertools.islice(fib(), 20)))

#Linkedlists
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class LinkedList:
    def __init(self, start):
        self.start = start
    #iterating through
    def __iter__(self):
        node = self.start
        while node:
            yield node
            node = node.next
    #over riding empty list
    def __len__(self):
        count = 0
        for i in self:
            count += 1
        return count

ll = LinkedList(Node(5, Node(10, Node(15, Node(20)))))
for node in ll:
    print(node.data)

#reversed linked list
class Node1:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList1:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
        print("None")

    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

llist = LinkedList1()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)

print("original")
llist.print_list()

llist.reverse()

print("reversed")
llist.print_list()

#zipping
from itertools import zip_longest
names = []
points = []
#without itertools zip(), wont get extra items
zipped = [list(item) for item in zip_longest(names, points)]
print(zipped)

#method default parameters
def zip_lists(list1=[], list2 = [], longest= True):
    if longest:
        pass
    else:
        pass
#notice order doesnt matter with default
print(zip_lists(longest=True, list2 =[], list1 = []))