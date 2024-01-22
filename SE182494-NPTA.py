class Student:
    def __init__(self, id, name, mark):
        self.id = id
        self.name = name
        self.mark = mark

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Mark: {self.mark}"

class Node:
    def __init__(self, data=None):
        self.next = None
        self.prev = None
        self.data = data

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert_last(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print("Previous node cannot be null")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev = new_node

    def remove_first(self):
        if self.head is None:
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def remove_last(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        last = self.head
        while last.next:
            last = last.next
        last.prev.next = None

    def remove_after(self, prev_node):
        if prev_node is None or prev_node.next is None:
            return
        prev_node.next = prev_node.next.next
        if prev_node.next:
            prev_node.next.prev = prev_node

    def update(self, id, new_data):
        t = self.head
        while t:
            if t.data.id == id:
                t.data = new_data
                return
            t = t.next

    def display(self):
        t = self.head
        while t:
            print(t.data)
            t = t.next

    def search(self, id):
        t = self.head
        while t:
            if t.data.id == id:
                return t.data
            t = t.next
        return None


student1 = Student(1, "Tin", 85)
student2 = Student(2, "K", 90)
student3 = Student(3, "Z", 95)

dll = DoublyLinkedList()
dll.insert_first(student1)
dll.insert_last(student2)
dll.display()