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

    def insert(self, index, node):
        # 인덱스가 사이즈보다 크면 불가능, 0보다 작으면 불가능
        if index > self.size or index < 0:
            return
        if index == 0:
            if self.head == None:
                self.head = node
            else:
                node.next, self.head = self.head, node
        else:
            preNode = self.head
            cnt = 1
            while cnt < index:
                preNode = preNode.next
                cnt += 1
            if preNode.next == None:
                preNode.next = node
            else:
                node.next, preNode.next = preNode.next, node
        self.size += 1

    def removeByIndex(self, index):
        if self.size < 1 or index+1 > self.size:
            return
        count = 0
        node = None
        while count < index:
            if node == None:
                node = self.head
            else:
                node = node.next
            count += 1
        if node == None:
            self.head = self.head.next
        elif node.next == self.tail:
            node.next = None
        else:
            node.next = node.next.next
        self.size -= 1
        
    def removeByData(self, data):
        node = None
        while True:
            if node == None:                # 첨 시작할때
                if self.head.data == data:      # 대가리가 대상이면
                    self.head = self.head.next
                    self.size -= 1
                    return
                else:                           # 아니면 진행향지
                    node = self.head
            elif node.next == None:         # 마지막까지 못찾았어
                return
            elif node.next.data == data:    # 찾은경우
                break
            else:                           # 다음거 검색
                node = node.next

        if node.next == self.tail:          # 마지막이 대상이면
            node.next = None
            self.tail = node
        else:                               # 그 외엔 연결해줘야함
            node.next = node.next.next
        self.size -= 1
        
    def printAll(self):
        curNode = self.head
        index = 0
        while index < self.size:
            print(f"{index+1}. 값 : {curNode.data}")
            curNode = curNode.next
            index += 1

    def clear(self):
        pass



# mylist = LinkedList()

# for i in range(1,6):
#     mylist.add(i)

# mylist.add(100, 2)
# mylist.printAll()
# print("-------제거--------")
# mylist.removeByData(6)
# print("리스트 사이즈 : {0}".format(mylist.size))
# mylist.printAll()
# mylist.removeByData(1)
# print("리스트 사이즈 : {0}".format(mylist.size))
# mylist.printAll()
# mylist.removeByData(6)
# print("리스트 사이즈 : {0}".format(mylist.size))
# mylist.printAll()
# mylist.removeByIndex(5)
# print("리스트 사이즈 : {0}".format(mylist.size))
# mylist.printAll()
# # mylist.removeByIndex(5)
# # print("리스트 사이즈 : {0}".format(mylist.size))
# # mylist.printAll()
# mylist.removeByIndex(0)
# print("리스트 사이즈 : {0}".format(mylist.size))
# mylist.printAll()
# mylist.insert(0, Node(9))
# print("리스트 사이즈 : {0}".format(mylist.size))
# mylist.printAll()
# mylist.insert(1, Node(99))
# print("리스트 사이즈 : {0}".format(mylist.size))
# mylist.printAll()