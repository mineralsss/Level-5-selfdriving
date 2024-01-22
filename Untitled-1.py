class Student:
    def __init__(self,id,name,mark):
        self.id = id
        self.name = name
        self.mark = mark
    def __str__(self):
        return f"Student(id={self.id}, name={self.name}, mark={self.mark})"
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class StudentManagement:
    def __init__(self):
        self.head = None
        self.tail = None
    def insertFirst(self, data):
        new_Student = Node(data)
        t = self.head
        if t:
            new_Student.next = t
            t.prev = new_Student
            self.head = new_Student
        else:
            self.head = new_Student
            self.tail = new_Student
    def insertLast(self,data):
        new_Student = Node(data)
        t = self.tail
        if t:
            t.next = new_Student
            new_Student.prev = t
            self.tail = new_Student
        else:
            self.head = new_Student
            self.tail = new_Student
    def removeFirst(self):
        t = self.head
        if t:
            t.next.prev = None
            t = None
        else:
            return False
    def removeLast(self):
        t = self.tail
        if t:
            t.prev.next = None
            t = None
        else:
            return False
    def update(self,oldID, newData):
        t = self.head
        if t is None:
            return False
        else:
            while t:
                if oldID != t.data.id:
                    t = t.next
                else:
                    print("Old data: ", t.data)
                    print("New data", newData)
                    user_choice = ("Are you sure you wanna change ?(Y/N): ")
                    if user_choice == "Y":
                        t.data = newData
                        print("Success")
    def display(self):
        t = self.head
        arr = []
        while t:
            arr.append(t.data)
            t = t.next
        for each in arr:
            print(each)
    
    def search(self, ID):
        t = self.head
        if t is None:
            return False
        else:
            while t:
                if ID != t.data.id:
                    t = t.next
                else:
                    return True
            
student = Student(id="123", name="John Doe", mark=85)
Stu_list = StudentManagement()
Stu_list.insertFirst(student)
Stu_list.display()
Stu_list.insertLast(student)
Stu_list.display()