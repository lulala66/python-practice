class Node(object):
    """Node Class"""
    def __init__(self, data):
        # assign data
        self.data = data
        # initialize next as None
        self.next = None


class LinkedList(object):
    """
    Implementation of LinkedList
    which contains a Node object
    """
    def __init__(self):
        # Initialize head as None
        self.head = None

    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        """
        :type new_data: int
        :rtype: void
        """
        # Instantiated a new Node object
        new_node = Node(new_data)
        # Make next of new Node as head
        new_node.next = self.head
        # Make head pointing to new Node
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        """
        :type prev_node: Node
        :type new_data: int
        :rtype: void
        """
        # Check if the prev_node exist
        if prev_node is None:
            print('The given previous node does not exist')
        # Instantiated a new Node object
        new_node = Node(new_data)
        # Make new Node pointing to next of prev_node
        new_node.next = prev_node.next
        # Make prev_node pointing to new_node
        prev_node.next = new_node

    def append(self, new_data):
        """
        :type new_data: int
        :rtype: void
        """
        # Instantiated a new Node object
        new_node = Node(new_data)
        # Check if the linkedList is empty
        if self.head is None:
            # If so, make the new_node be the head
            self.head = new_node
        # Else traverse until the last node
        else:
            last = self.head
            while(last.next):
                last = last.next

            # Make the new_node be the last
            last.next = new_node
    
    def deleteNode(self, key):
        """
        :type key: int
        :rtype: void
        """
        # Check if the linkedList is empty
        if self.head is None:
            return
        # Traverse from the head
        curr = self.head
        # If find the key at the head node
        if curr.data == key:
            self.head = curr.next
            return
        # If not so, traverse until the end
        while curr.next:
            prev = curr
            curr = curr.next
            # When finding the key in current node
            if curr.data == key:
                prev.next = curr.next
                return
        # Cannot find the key after traverse all nodes
        return

    def deleteNode2(self, position):
        """
        :type position: int
        :rtype: void
        """
        if self.head:
            curr = self.head
            pointer = 0
            if position == 0:
                self.head = curr.next
                return
            while pointer < position:
                prev = curr
                if curr.next is None:
                    print("Position exceeds the length of LinkedList")
                    return
                curr = curr.next
                pointer += 1

            prev.next = curr.next

    def swap(self, x, y):
        """
        :type x, y: int
        :rtype: void
        """
        if x == y or self.head is None:
            return

        temp_head = Node(None)
        temp_head.next = self.head
        prev = temp_head
        curr = prev.next

        while curr:
            if curr.data == x:
                prevX = prev
                currX = curr
            if curr.data == y:
                prevY = prev
                currY = curr
            prev = curr
            curr = curr.next

        prevX.next = currY
        prevY.next = currX
        temp = currX.next
        currX.next = currY.next
        currY.next = temp

        self.head = temp_head.next

    def FindKthToTail(self, k):
        if self.head is None or k <= 0:
            return None
        target = self.head
        move = self.head
        for _ in range(k - 1):
            if move.next is None:
                return None
            move = move.next

        while move.next:
            move = move.next
            target = target.next
        return target

    def reverse_link(self):
        if self.head is None or self.head.next is None:
            return self.head

        prev = None
        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev
        return self


def merge_link(head1, head2):
    temp_head = Node(None)
    curr = temp_head
    l = LinkedList()
    curr1 = head1
    curr2 = head2

    while curr1 or curr2:
        if curr1 is None:
            curr.next = curr2
            l.head = temp_head.next
            return l
        elif curr2 is None:
            curr.next = curr1
            l.head = temp_head.next
            return l
        elif curr1.data <= curr2.data:
            curr.next = curr1
            curr1 = curr1.next
            curr = curr.next
        else:
            curr.next = curr2
            curr2 = curr2.next
            curr = curr.next

    l.head = temp_head.next
    return l


# def merge_link(head1, head2):
#     if not head1:
#         return head2
#     if not head2:
#         return head1
#     if head1.data <= head2.data:
#         ret = head1
#         ret.next = merge_link(head1.next, head2.next)
#     else:
#         ret = head2
#         ret.next = merge_link(head1.next, head2.next)

#     l = LinkedList()
#     l.head = ret
#     return l

if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third
    # llist.printlist()
    # llist.push(5)
    # llist.printlist()
    # llist.insertAfter(llist.head, 9)
    # llist.printlist()
    # llist.append(10)
    # llist.printlist()
    # llist.deleteNode(3)
    # llist.printlist()
    # llist.deleteNode2(3)
    # llist.swap(3, 1)
    # llist.printlist()
    # rlist = llist.reverse_link()
    # rlist.printlist()
    llist2 = LinkedList()
    llist2.head = Node(2)
    second2 = Node(4)
    third2 = Node(6)
    llist2.head.next = second2
    second2.next = third2
    a = merge_link(llist.head, llist2.head)
    a.printlist()
