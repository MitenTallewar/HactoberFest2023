class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class UniqueLinkedList:
    def __init__(self):
        self.head = None

    def append_unique(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                if current.data == data:
                    return  # Don't add duplicate data
                current = current.next
            if current.data != data:
                current.next = Node(data)

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
unique_list = UniqueLinkedList()
unique_list.append_unique(1)
unique_list.append_unique(2)
unique_list.append_unique(3)
unique_list.append_unique(2)  # This will be ignored
unique_list.append_unique(4)
unique_list.display()
