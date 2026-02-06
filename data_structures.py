# --- بخش اول: صف حلقوی (Circular Queue) ---
class C_Queue:
    def __init__(self, max_size=10):
        self.max = max_size
        self.list = [None] * max_size
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.max == self.front

    def is_empty(self):
        return self.front == -1

    def insert(self, x):
        if self.is_full():
            print('Queue is full')
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.max
        self.list[self.rear] = x

    def delete(self):
        if self.is_empty():
            print('Queue is empty')
            return None
        k = self.list[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max
        return k

    def show_valid(self):
        if self.is_empty():
            print("Queue is empty")
            return
        i = self.front
        while True:
            print(self.list[i], end=" ")
            if i == self.rear: break
            i = (i + 1) % self.max
        print()

# --- بخش دوم: پشته (Stack) ---
class Stack:
    def __init__(self, limit=1000):
        self.st = []
        self.limit = limit

    def push(self, x):
        if len(self.st) >= self.limit:
            print('Stack is full')
            return
        self.st.append(x)

    def pop(self):
        if not self.st:
            print('Stack is empty')
            return None
        return self.st.pop()

# --- بخش سوم: لیست پیوندی (Linked List) ---
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def insert_first(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
