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

    def append(self, val):
        """Appends a new node after the last non-none node"""

        new_node = SingleNode(val)

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.link(new_node)

        return self

    def append_after(self, node_val, val):
        """Appends after a given node, appends to the end if non existent"""

        new_node = SingleNode(val)

        curr = self.head
        while curr.next and curr.val != node_val:
            curr = curr.next

        old_next = curr.next
        curr.link(new_node)
        new_node.link(old_next)

        return self

    def prepend(self, val):
        """Prepends i.e. appends a node at the head"""

        pass

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
    # should append "true_end" after "end" since "none" doesn't exist
    sll.append_after("mid", "true_mid").append_after("none", "true_end")
    sll.append_after("head", "after_head")

    sll.display()


if __name__ == "__main__":
    main()
