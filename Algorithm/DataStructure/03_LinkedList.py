class Node:
    def __init__(self, data, nextNode = None):
        self.data = data
        self.next = nextNode

# node1 = Node(1)
# node2 = Node(2)
# node1.next = node2

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, data, index = 0):
        # 인덱스가 사이즈보다 크면 불가능, 0보다 작으면 불가능
        if index > self.size or index < 0:
            print("인덱스 오류")
        else:
            node = self.head
            while index > 0:
                node = node.next
                index -= 1
            newnode = Node(data)
            newnode.next = node.next
            node.next = newnode

    def remove(self, index):
        pass
    def printAll(self):
        curNode = self.head
        index = 0
        while curNode != self.tail:
            print(f"{index}. 값 : {curNode.data}")
            curNode = curNode.next
            index += 1

    def clear(self):
        pass
    
mylist = LinkedList()

for i in range(1,6):
    mylist.add(i)

mylist.add(100, 2)
mylist.printAll()