class SingleNode:
    """Singly Linked List Node"""

    def __init__(self, val) -> None:
        self.val = val
        self.next = None

    def link(self, next_node):
        """Links this node to another node"""
        self.next = next_node
        return self


class SinglyLinkedList:
    """Singly Linked List"""

    def __init__(self, head: SingleNode) -> None:
        self.head = head

    def append(self, item):
        """Appends a new node after the last non-none node"""
        new_node = SingleNode(item)
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.link(new_node)
        return self

    def display(self):
        """Pretty prints linked list"""
        curr = self.head
        while curr:
            print(f"{curr.val} ->", end=" ")
            curr = curr.next
        print("NONE")

    def get_head(self):
        """Returns a reference to the head node"""
        return self.head


def main():
    sll = SinglyLinkedList(SingleNode("head"))
    sll.append("mid").append("body").append("end")
    sll.display()


if __name__ == "__main__":
    main()
