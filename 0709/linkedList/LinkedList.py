class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # 출력
    def listprint(self):
        printval = self.head
        while printval != None:
            print(printval.data)
            printval = printval.next

    # head 앞에 삽입 : O(1)
    def insertHead(self, newdata):
        NewNode = Node(newdata)
        # 먼저 새 노드의 next를 현재 리스트의 head로 지정
        NewNode.next = self.head
        # 그 다음 현재 리스트의 head를 새 노드로 연결
        self.head = NewNode


    # tail 뒤에 삽입 : O(1)
    def insertTail(self, newdata):
        NewNode = Node(newdata)
        # 먼저 현재 리스트 tail의 next를 새 노드로 연결
        self.tail.next = NewNode
        # 현재 리스트의 tail을 NewNode로 지정
        self.tail = NewNode

    # 노드 사이에 삽입(특정 데이터를 가진 노드 뒤에 위치하도록) : O(1)
    def insertBetween(self, middle_node, newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        NewNode = Node(newdata)
        NewNode.next = middle_node.next
        middle_node.next = NewNode

    #삭제: O(1)
    def remove(self, removeKey):
        Headval = self.head

        if (Headval is not None):
            if (Headval.data == removeKey):
                self.head = Headval.next
                Headval = None
                return
            else:
                while (Headval is not None):
                    if Headval.data == removeKey:
                        break
                    prev = Headval
                    Headval = Headval.next

            if (Headval == None):
                return

            prev.next = Headval.next
            Headval = None

        else:
            return


    #탐색: 최악 O(N)
    def find(self, findData):
        Headval = self.head
        if (Headval is not None):
            if (Headval.data == findData):
                print('{} is in list!'.format(findData))
                return
            else:
                while(Headval is not None):
                    if Headval.data == findData :
                        print('{} is in list!'.format(findData))
                        return
                    prev = Headval
                    Headval = Headval.next

                print('{} is Not in List'.format(findData))

        else:
            print('{} is Not in List'.format(findData))

Slist = SLinkedList()
Slist.head = Node('Mon')
node2 = Node('Tue')
node3 = Node('Wed')
Slist.tail = node3

# 노드들을 연결해서 단일 링크드 리스트로 만들기
Slist.head.next = node2
node2.next = Slist.tail

# 노드에 삽입
Slist.insertHead('Sun')
Slist.insertTail('Fri')
Slist.insertBetween(Slist.head.next.next.next, 'Thu')
Slist.listprint()
print('---')

# 탐색(값 존재 O)
Slist.find('Thu')
print('---')

# 삭제
Slist.remove('Thu')
Slist.listprint()
print('---')

# 탐색(값 존재 X)
Slist.find('Thu')
print('---')