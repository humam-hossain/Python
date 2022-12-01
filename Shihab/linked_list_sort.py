class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    
    def __init__(self, arr):
        self.head = Node(arr[0], None)
        tail = self.head
        self.count = 1
        for i in range(1, len(arr)):
            n = Node(arr[i], None)
            tail.next = n
            tail = tail.next
            self.count = self.count + 1

    def sort(self):
        # x = self.head.next
        # l=Node(n.element,None)
        # x=n.next
        # tail=l
        n = self.head

        while n.next != None:
            if n.next.value < n.value:
                temp = n.value
                n.value = n.next.value
                n.next.value = temp
            n = n.next
            # self.head = n

        return (n)

    def showList(self):
        tail = self.head
        y = ""
        while tail != None:
            y += str(tail.value)+","
            tail = tail.next
        print(y[:-1])

    # def sort(self):
        # n=self.head
        # l=Node(n.element,None)
        # x=n.next
        # tail=l
        # while x!=None:
        # if x.element>x.next.element:


arr = [3, -1, 4, 5, 0]
ll = LinkedList(arr)
ll.sort()
ll.showList()

# [3, 4, 5, 0, -1]
