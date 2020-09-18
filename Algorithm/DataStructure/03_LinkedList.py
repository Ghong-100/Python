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

    def add(self, data, index = 0):  # 그냥 넣으면 맨 마지막에, 인덱스 넣으면 그 위치에
        # 인덱스가 사이즈보다 크면 불가능, 0보다 작으면 불가능
        if index > self.size or index < 0:
            print("인덱스 오류")
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            self.size += 1
        elif index == 0:
            print("last")
            newNode = Node(data)
            self.tail.next = newNode
            self.tail = self.tail.next
            if self.size == 1:
                self.head.next = self.tail
            self.size += 1
        else:
            node = self.head
            cnt = 0
            while cnt < index:
                print(cnt)
                node = node.next
                cnt += 1
            nextnode = node.next
            node.next = Node(data)
            node.next.next = nextnode
            self.size += 1
        
        printnode = self.head
        for i in range(0, self.size):
            print(f"{i+1}번째 값 {printnode.data}")
            printnode = printnode.next


    def remove(self, index):
        pass
    def printAll(self):
        curNode = self.head
        index = 0
        while index < self.size:
            print(f"{index+1}. 값 : {curNode.data}")
            curNode = curNode.next
            index += 1

    def clear(self):
        pass
    
mylist = LinkedList()

for i in range(1,6):
    mylist.add(i)

mylist.add(100, 2)
mylist.printAll()