from node import Node

class Row:
    def __init__(self):
        self.first = None
        self.last = None

    def __str__(self):
        return f"First: {self.first}, Last: {self.last}"
    
    def is_empty(self):
        return self.first is None

    def queue(self, value):
        _new_node = Node(value)
        if self.is_empty():
            self.first = _new_node
            self.last = _new_node 
        else:
            self.last.next = _new_node
            self.last = _new_node

    def dequeue(self):
        if not self.is_empty():
            _temp = self.first
            self.first = self.first.next
            return _temp
        else:
            return None
