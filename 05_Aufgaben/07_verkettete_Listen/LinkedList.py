from Knoten import Knoten

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Knoten(value)

        if self.head == None:
            self.head = new_node
            return

        knoten = self.head
        while knoten.next:
            knoten = knoten.next

        knoten.next = new_node

    def print_list(self):
        knoten = self.head
        while knoten is not None:
            print(knoten)
            knoten = knoten.next

    def length(self):
        knoten = self.head
        length = 0
        while knoten is not None:
            length += 1
            knoten = knoten.next
        return length

    def __iter__(self):
        self.knoten = self.head
        return self

    def __next__(self):
        if self.knoten is None:
            raise StopIteration

        value = self.knoten.value
        self.knoten = self.knoten.next
        return value
